#!/usr/bin/env python3
"""Read-only local checks; not a runtime or a test of the manifesto's philosophy.

Uses CommonMark links/fences, flat YAML frontmatter, and GitHub-style heading
anchors (Unicode letters/numbers/marks, hyphens, underscores, duplicate suffixes).
Raw HTML anchors/links and external URLs are outside this gate's coverage.
JSON Schema format keywords remain annotations, not asserted format checks.
JSON examples in contracts.md use the schema linked in their heading section;
sections without a schema are explicitly reported as syntax-only examples.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import json
import os
from pathlib import Path
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

try:
    from jsonschema.exceptions import SchemaError
    from jsonschema.validators import validator_for
    from markdown_it import MarkdownIt
    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT202012
    import yaml
except ImportError as error:
    raise SystemExit(
        f"Missing validation dependency: {error.name}. "
        "Install requirements-dev.txt in your development environment."
    ) from error


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    markdown: int = 0
    json_files: int = 0
    schemas: int = 0
    validated_examples: int = 0
    syntax_only: list[str] = field(default_factory=list)


def files_in(root: Path):
    """Ignore version-control, environments, and generated dependency trees."""
    for directory, names, files in os.walk(root):
        names[:] = sorted(name for name in names if not name.startswith(".")
                          and name not in {"node_modules", "__pycache__"})
        for name in sorted(files):
            if name.endswith((".md", ".json")):
                yield Path(directory) / name


def visible_text(tokens):
    return "".join(
        visible_text(token.children) if token.children else
        token.content if token.type in {"text", "code_inline"} else
        " " if token.type in {"softbreak", "hardbreak"} else ""
        for token in tokens
    )


def heading_anchors(tokens):
    used = set()
    for index, token in enumerate(tokens):
        if token.type != "heading_open":
            continue
        text = visible_text(tokens[index + 1].children or []).lower()
        slug = "".join(character for character in text
                       if character in " -_" or
                       unicodedata.category(character)[0] in "LNM").replace(" ", "-")
        anchor, suffix = slug, 0
        while anchor in used:
            suffix += 1
            anchor = f"{slug}-{suffix}"
        used.add(anchor)
    return used


def destinations(tokens):
    for token in tokens:
        if token.type == "link_open":
            yield token.attrGet("href")
        elif token.type == "image":
            yield token.attrGet("src")
        if token.children:
            yield from destinations(token.children)


def local_target(source: Path, destination: str):
    parsed = urlsplit(destination)
    if parsed.scheme or parsed.netloc:
        return None
    target = (source.parent / unquote(parsed.path)).resolve() if parsed.path else source
    return target, unquote(parsed.fragment)


def frontmatter(text: str):
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None, text
    for end in range(1, len(lines)):
        if lines[end].strip() == "---":
            data = yaml.safe_load("".join(lines[1:end]))
            return data, "\n" * (end + 1) + "".join(lines[end + 1:])
    raise ValueError("unterminated YAML frontmatter")


def example_section(tokens, index):
    """Select the closest heading, stopping at its next sibling or ancestor."""
    headings = [position for position in range(index) if tokens[position].type == "heading_open"]
    start = headings[-1] if headings else 0
    level = int(tokens[start].tag[1:]) if headings else 0
    end = next((position for position in range(index + 1, len(tokens))
                if tokens[position].type == "heading_open"
                and int(tokens[position].tag[1:]) <= level), len(tokens))
    return tokens[start:end]


def validate(root: Path) -> Report:
    root = root.resolve()
    report = Report()
    markdown, metadata, documents, schemas = {}, {}, {}, {}
    parser = MarkdownIt("commonmark")

    def issue(path, message):
        label = path.relative_to(root) if path.is_relative_to(root) else path
        report.errors.append(f"{label}: {message}")

    for path in files_in(root):
        try:
            text = path.read_text(encoding="utf-8")
            if path.suffix == ".md":
                report.markdown += 1
                metadata[path], body = frontmatter(text)
                markdown[path] = parser.parse(body)
            else:
                report.json_files += 1
                documents[path] = json.loads(text)
        except (OSError, UnicodeError, ValueError, yaml.YAMLError) as error:
            issue(path, f"cannot parse: {error}")

    mirrors = {lang: {path.relative_to(root / "docs" / lang) for path in markdown
                      if path.is_relative_to(root / "docs" / lang)} for lang in ("ru", "en")}
    for relative in sorted(mirrors["ru"] | mirrors["en"]):
        pair = {}
        for lang in ("ru", "en"):
            path = root / "docs" / lang / relative
            if relative not in mirrors[lang]:
                issue(path, "missing RU/EN mirror")
                continue
            data = metadata[path]
            if not isinstance(data, dict):
                issue(path, "missing or invalid frontmatter mapping")
                continue
            pair[lang] = data
            for key in ("title", "lang", "version", "layer"):
                value = data.get(key)
                if isinstance(value, bool) or not isinstance(value, (str, int, float)) or not str(value).strip():
                    issue(path, f"frontmatter requires a nonempty scalar {key}")
            if data.get("lang") != lang:
                issue(path, f"frontmatter lang must be {lang}")
        if len(pair) == 2:
            for key in ("version", "layer"):
                if str(pair["ru"].get(key)) != str(pair["en"].get(key)):
                    issue(root / "docs" / "en" / relative, f"RU/EN frontmatter {key} mismatch")

    anchors = {path: heading_anchors(tokens) for path, tokens in markdown.items()}
    for path, tokens in markdown.items():
        for destination in destinations(tokens):
            target = local_target(path, destination)
            if target is None:
                continue
            location, fragment = target
            if not location.is_relative_to(root):
                issue(path, f"local link escapes repository: {destination}")
            elif not location.exists():
                issue(path, f"broken local link: {destination}")
            elif fragment:
                heading_file = location / "README.md" if location.is_dir() else location
                if heading_file.suffix == ".md" and fragment not in anchors.get(heading_file, set()):
                    issue(path, f"unknown heading anchor: {destination}")

    for path, data in documents.items():
        if path.parent == root / "schemas" and path.name.endswith(".schema.json"):
            try:
                validator_for(data).check_schema(data)
                schemas[path] = data
                report.schemas += 1
            except (SchemaError, TypeError, AttributeError) as error:
                issue(path, f"invalid JSON Schema: {error}")

    # Explicit registry: references may use local schema IDs, never fetch the network.
    registry = Registry()
    for path, schema in schemas.items():
        resource = Resource.from_contents(schema, default_specification=DRAFT202012)
        registry = registry.with_resource(path.as_uri(), resource)
        if isinstance(schema, dict) and "$id" in schema:
            registry = registry.with_resource(schema["$id"], resource)

    def validate_example(path, value, schema_path, label):
        if schema_path not in schemas:
            issue(path, f"{label}: missing or invalid schema {schema_path.name}")
            return
        schema = schemas[schema_path]
        validator = validator_for(schema)(schema, registry=registry)
        try:
            errors = sorted(validator.iter_errors(value), key=lambda error: str(list(error.path)))
            for error in errors:
                issue(path, f"{label}: {list(error.path)}: {error.message}")
            if not errors:
                report.validated_examples += 1
        except Exception as error:
            # Includes unresolved references; fail locally instead of fetching a schema.
            issue(path, f"{label}: schema validation failed: {error}")

    for lang in ("ru", "en"):
        path = root / "examples" / f"aura.{lang}.json"
        if path in documents:
            validate_example(path, documents[path], root / "schemas/persona.schema.json", "persona example")

    for path, tokens in markdown.items():
        if path.name != "contracts.md" or not path.is_relative_to(root / "docs"):
            continue
        for index, token in enumerate(tokens):
            if token.type != "fence" or token.info.strip() != "json":
                continue
            label = f"JSON example at line {token.map[0] + 1}"
            try:
                value = json.loads(token.content)
            except ValueError as error:
                issue(path, f"{label}: invalid JSON: {error}")
                continue
            candidates = set()
            for destination in destinations(example_section(tokens, index)):
                target = local_target(path, destination)
                if target and target[0].name.endswith(".schema.json"):
                    candidates.add(target[0])
            if len(candidates) > 1:
                issue(path, f"{label}: ambiguous schema links in heading section")
            elif candidates:
                validate_example(path, value, candidates.pop(), label)
            else:
                report.syntax_only.append(f"{path.relative_to(root)}: {label}")
    return report


def main():
    arguments = argparse.ArgumentParser(description=__doc__)
    arguments.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    root = arguments.parse_args().root
    if not (root / "docs/ru").is_dir() or not (root / "docs/en").is_dir():
        arguments.error("root must contain docs/ru and docs/en")
    report = validate(root)
    for error in report.errors:
        print(f"ERROR: {error}", file=sys.stderr)
    for label in report.syntax_only:
        print(f"SYNTAX ONLY (no machine schema): {label}")
    print(f"Checked {report.markdown} Markdown files, {report.json_files} JSON files, "
          f"{report.schemas} schemas, {report.validated_examples} schema-bound examples; "
          f"{len(report.errors)} error(s).")
    return bool(report.errors)


if __name__ == "__main__":
    sys.exit(main())
