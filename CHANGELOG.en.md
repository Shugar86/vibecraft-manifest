# Changelog

🌐 [Русский](./CHANGELOG.md) · **English**

Format — [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This is the history of the **manifesto**
(the documents), not of a separate product. The ladder of the VibeCraft methodology itself (v1.0→v1.4) is
described in [`docs/en/stack.md`](./docs/en/stack.md).

## [1.1.0] — 2026-09-05

A conceptual revision following a joint review with an AI agent. The number is
the document revision; the historical methodology ladder v1.0–v1.4 remains.

### Changed

- The manifesto develops character through decisions and shared unfinished thought.
  Persona + Skills + Autonomy is a useful model in a real environment, not a
  universal engine or a promise of entering a new domain in minutes.
- Sync separates artifact version, loading and behavior. Social retains scope,
  sources and uncertainty; shared storage does not grant universal data access.
- Reflect/Learn may revise understanding without new policy. Compression, proposal
  counts and aggregate scores do not substitute for quality; a correction does
  not become a permanent profile of the person.
- Humans decide on durable changes; an agent may execute an authorized diff.
  Status fields do not authorize action. Schemas are distinguished from absent
  runtimes/compilers and the illustrative ReflectionPass.
- RU/EN are aligned; frontmatter `version` now explicitly denotes document revision.
  Existing headings and deep links are preserved; the license link is corrected.

### Added

- `examples/aura.{ru,en}.json`: a current Persona example without invented memory
  or background initiative; historical `vibe.config*.json` remain separate.
- Offline `scripts/validate.py`, regression tests and development dependencies:
  local links/anchors, language mirrors and frontmatter, JSON schemas and examples.
- Visible historical notices on the seed manifestos; original contents retained.

JSON Schema constraints have not migrated: descriptions changed, not data shape.
The gate does not check external URLs, runtime behavior or human experience;
`format` remains an annotation rather than a separate date assertion.

## [1.0.0] — 2026-06-16

Expansion of the original seed manifesto (RU, snapshot v1.2: `MANIFEST.md`, `vibe.config.json`,
`LICENSE.md`) into a structured bilingual release (RU/EN), philosophy + engineering, v1.0→v1.4.
Dual license (CC BY 4.0 for texts, MIT for code/configs), see [`LICENSE.md`](./LICENSE.md).

### Added
- `README.md` / `README.en.md` — the showcase: the thesis (Persona + Skills + Autonomy), the version ladder, navigation for human and machine.
- `docs/{ru,en}/manifesto.md` — the vision: the soul as engineering.
- `docs/{ru,en}/stack.md` — the version ladder v1.0→v1.4, each axis: thesis + 🔧 engineering.
- `docs/{ru,en}/threads.md` — reflection across versions through six threads: human↔AI via vibe, AI↔AI, where the soul lives, how to explain vibe to an AI, self-change / changing another AI, protecting oneself and the human.
- `docs/{ru,en}/interaction.md` — how agents interact: one soul — many bodies (Sync), shared memory — shared edits (Social), the Reflect→Learn→Morph loop.
- `docs/{ru,en}/contracts.md` — formal contracts: Persona, Anchor/Surface, MorphEvent, MorphProposal, ReflectionPass, loop invariants.
- `schemas/*.json` — machine-readable JSON schemas (persona, morph-event, morph-proposal).
- `AGENTS.md` — the machine entry point: how to read the repository.

### Kept (from the original seed)
- `MANIFEST.md` — the original single-file manifesto v1.2 (RU; English: `MANIFEST.en.md`).
- `vibe.config.json` — a VibePersona v1.2 example (English: `vibe.config.en.json`).
- `LICENSE.md` — dual license (CC BY 4.0 / MIT).
