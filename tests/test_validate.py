"""Small synthetic repositories exercise the gate independently of prose changes."""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/validate.py"
SPEC = importlib.util.spec_from_file_location("manifest_validate", SCRIPT)
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="vibecraft-validation-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": "https://example.invalid/persona.schema.json",
            "type": "object", "additionalProperties": False,
            "required": ["name"], "properties": {"name": {"type": "string"}},
        }
        self.write("schemas/persona.schema.json", json.dumps(self.schema))
        for lang in ("ru", "en"):
            self.doc(lang, "contracts.md", "## Example\n\n"
                     "[Schema](../../schemas/persona.schema.json)\n\n"
                     '```json\n{"name": "Aura"}\n```\n')
            self.write(f"examples/aura.{lang}.json", '{"name": "Aura"}')

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def doc(self, lang, name, body, version="2.3", layer="engineering"):
        self.write(f"docs/{lang}/{name}",
                   f"---\ntitle: Example\nlang: {lang}\nversion: {version}\nlayer: {layer}\n---\n\n{body}")

    def errors(self):
        return "\n".join(VALIDATOR.validate(self.root).errors)

    def test_valid_repo_and_examples(self):
        before = {path.relative_to(self.root): path.read_bytes()
                  for path in self.root.rglob("*") if path.is_file()}
        report = VALIDATOR.validate(self.root)
        self.assertEqual(report.errors, [])
        self.assertEqual(report.validated_examples, 4)
        after = {path.relative_to(self.root): path.read_bytes()
                 for path in self.root.rglob("*") if path.is_file()}
        self.assertEqual(before, after)

    def test_cli_exit_status_and_diagnostic(self):
        command = [sys.executable, str(SCRIPT), "--root", str(self.root)]
        success = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(success.returncode, 0, success.stderr)
        self.write("README.md", "[missing](./gone.md)")
        failure = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(failure.returncode, 1)
        self.assertIn("README.md: broken local link", failure.stderr)

    def test_broken_local_link(self):
        self.write("README.md", "[missing](./gone.md)")
        self.assertIn("broken local link", self.errors())

    def test_broken_anchor(self):
        self.write("README.md", "[missing](./docs/ru/contracts.md#absent)")
        self.assertIn("unknown heading anchor", self.errors())

    def test_unicode_formatted_headings_duplicates_and_reference_links(self):
        self.write("README.md", "# Одна **душа** — много `тел`\n\n"
                   "## Echo\n\n## Echo\n\n## Echo-1\n\n"
                   "[ru](#одна-душа--много-тел) [duplicate](#echo-1) [collision](#echo-1-1)\n\n"
                   "[reference][schema]\n\n[schema]: schemas/persona.schema.json\n\n"
                   "`[ignored](missing-inline.md)`\n\n```md\n[ignored](missing-fence.md)\n```\n")
        self.assertEqual(self.errors(), "")

    def test_nested_badge_and_image_links(self):
        self.write("README.md", "[![badge](https://example.invalid/badge.svg)](./missing.md)")
        self.assertIn("broken local link", self.errors())

    def test_missing_mirror(self):
        self.doc("ru", "new.md", "# New")
        self.assertIn("missing RU/EN mirror", self.errors())

    def test_mirror_frontmatter(self):
        self.doc("en", "contracts.md", "# Example", version="9.1", layer="philosophy")
        errors = self.errors()
        self.assertIn("version mismatch", errors)
        self.assertIn("layer mismatch", errors)

    def test_frontmatter_required_fields_and_language(self):
        self.write("docs/en/contracts.md", "---\ntitle: Example\nlang: ru\nversion: 2.3\n---\n# Example")
        errors = self.errors()
        self.assertIn("nonempty scalar layer", errors)
        self.assertIn("lang must be en", errors)

    def test_invalid_json_file_and_schema(self):
        self.write("vibe.config.json", "{bad json}")
        self.write("schemas/bad.schema.json", '{"type": "not-a-type"}')
        errors = self.errors()
        self.assertIn("cannot parse", errors)
        self.assertIn("invalid JSON Schema", errors)

    def test_legacy_seed_not_forced_through_current_persona(self):
        self.write("vibe.config.json", '{"legacy": true}')
        self.assertEqual(self.errors(), "")

    def test_current_persona_example_checked(self):
        self.write("examples/aura.en.json", '{"name": 42}')
        self.assertIn("persona example: ['name']: 42 is not of type 'string'", self.errors())

    def test_contract_example_checked_with_schema_link_after_fence(self):
        self.doc("en", "contracts.md", '## Example\n\n```json\n{"name": 42}\n```\n\n'
                 "[Schema](../../schemas/persona.schema.json)\n")
        self.assertIn("42 is not of type 'string'", self.errors())

    def test_contract_invalid_json(self):
        self.doc("en", "contracts.md", "## Example\n\n```json\n{broken}\n```\n")
        self.assertIn("invalid JSON", self.errors())

    def test_schema_does_not_leak_into_next_section(self):
        self.doc("en", "contracts.md", "## Persona\n\n"
                 "[Schema](../../schemas/persona.schema.json)\n\n"
                 '```json\n{"name": "Aura"}\n```\n\n'
                 '## Reflection\n\n```json\n{"illustration": true}\n```\n')
        report = VALIDATOR.validate(self.root)
        self.assertEqual(report.errors, [])
        self.assertEqual(len(report.syntax_only), 1)

    def test_remote_schema_reference_fails_without_network(self):
        self.schema["properties"]["name"] = {"$ref": "https://example.invalid/absent.json"}
        self.write("schemas/persona.schema.json", json.dumps(self.schema))
        self.assertIn("schema validation failed", self.errors())


if __name__ == "__main__":
    unittest.main()
