# Changelog

🌐 [Русский](./CHANGELOG.md) · **English**

Format — [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This is the history of the **manifesto**
(the documents), not of a separate product. Named stages in the development of the idea are
described in [`docs/en/stack.md`](./docs/en/stack.md).

## [1.3.1] — 2026-09-29

An editorial refinement of 1.3.0 through Claude's review, Codex's analysis and
human feedback. The project's foundations remain; they are easier to see and examine.

### Changed

- The README and manifesto open with a real episode of reconsidering the text.
  Manifesto headings match their current content, with links to the contracts'
  rules for deciding on and applying changes.
- Foundation, Character, Operations, Life, Society and Reflection are named
  stages. Earlier labels v1.0–v1.4 remain as a historical correspondence;
  document revision numbers no longer compete with stage headings.
- Substantive contribution is distinguished from authority: coauthorship can
  occur within an assignment. An accepted new criterion requires a clear account
  of the earlier task; a shift of interest does not make an unfinished feature complete.
- The README explicitly describes Claude's and Codex's contributions to this revision.

### Added

- A fifth real VibeCase: the move from completed revision 1.2.0 to 1.3.0.
  Invitation, proposal, acceptance, implementation and the human's overall positive
  assessment are distinct; commits and a diff make the text's history accessible.
- Two imagined scenes: assent in place of contribution, and a changed criterion
  used to excuse unfinished work. Neighboring cases show fitting agreement or turns.
- An optional, readable turn card in VibeCases.
- Named HTML anchors preserve earlier links after headings change. The validator
  checks these link targets, with two added regression tests.

### Compatibility and evidence

RU/EN are updated together. The first four real cases, historical seed files and
JSON Schemas are preserved. The new real case establishes an accepted revision
of documents; it does not establish lasting model improvement or that each
proposal surprised the human. Imagined failures are not presented as observations.
No new machine format or runtime was added.

## [1.3.0] — 2026-09-29

A shared revision following a model's proposal to reconsider its own previous
edition. Collaboration becomes the project's starting point; participants can
change both the intent and their idea of success. This number identifies a
document revision, separately from the historical v1.0–v1.4 ladder.

### Changed

- The manifesto and README begin with interaction between humans and models.
  Persona, Skills and Autonomy remain engineering supports for that interaction.
- Play, beauty, curiosity and conversation are recognized as values in their own
  right; each episode need not justify itself with a lesson, product or improvement.
- Shared commitments allow different voices and reasoned positions across models.
  A substantive disagreement can remain open when no decision is needed.
- Interaction, the ladder and the six threads also consider a changing criterion
  for success. An accepted change of direction is distinguished from fulfilling the earlier task.
- The main text is shorter; detailed engineering boundaries are concentrated in
  the contracts. The Russian and English bodies of work are updated together.

### Added

- Open questions in the manifesto about different models, continuity and changing
  criteria for success, without claiming final answers in this edition.
- Separately labeled imagined scenes of shared play and shifting interest in
  VibeCases. The four real episodes retain their record without invented continuations.
- A free-play scenario in the Persona example; the unfinished-idea scenario now
  allows a changing question and different reasoned views to remain open.

### Compatibility and evidence

JSON Schemas and their constraints are unchanged. Examples use the existing
`behavior.scenarios`; its support requirements remain the same. The new imagined
scenes are not observations, test runs or evidence of changed model behavior.
This revision adds no runtime.

## [1.2.0] — 2026-09-28

A substantive revision coauthored by the author and AI agents. This number denotes
the documents; the historical v1.0–v1.4 ladder and v1.2 seed retain separate meanings.

### Added

- `docs/{ru,en}/cases.md`: four complete VibeCases — understanding another,
  a creative trial, missed sarcasm and coauthoring the working environment. Public
  adaptations of author-supplied episodes distinguish observations, human assessments,
  editorial alternatives and neighboring checks that have not yet been performed.
- Optional `behavior.scenarios` in Persona: authored situations and directions for
  choice using `id`, `situation`, `guidance`. Aura gains discovery and return scenes;
  the companion example gains a scene for developing an unfinished thought.
- An entirely fictional end-to-end example in contracts connects a MorphProposal
  to an exact diff, human decision, application, loading and observed behavior.
- Checks for earlier Persona compatibility, new scenarios and unknown fields.

### Changed

- The manifesto treats the next move in a situation as the working unit of character:
  a reply, trial, action, pause or completion. The agent's contribution can change
  the idea; its appropriateness depends on context and decisions already made.
- Interaction, the ladder and six threads connect to VibeCases through conversational
  action, proportionate initiative, conditions for judgment, bounded lessons and transfer checks.
- README and machine navigation cover the new material. RU/EN remain semantic mirrors;
  private primary records are not included in the publication.

### Compatibility and evidence

Earlier Persona objects remain valid under the updated schema. The new `scenarios`
field requires an updated validator and adapter support; the older strict schema
rejects it. Other field constraints and both Morph schemas are unchanged.

VibeCases show individual episodes, including a failure and local correction;
they are not a comparative experiment or proof of lasting model improvement.
The repository still supplies no runtime, compiler, memory or scheduler.

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
