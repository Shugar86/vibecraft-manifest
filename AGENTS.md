# AGENTS.md — machine entry point

This file guides work on this repository. Human entry points:
[README.md](./README.md) (RU) · [README.en.md](./README.en.md) (EN).

## What this repo is

A vendor-neutral manifesto about character, experience and shared thought, for AI
operators beyond coding. It contains conceptual documents, three JSON schemas,
examples and document checks — not an agent runtime or a universal operational policy.

“Soul,” “sleep” and “life” are metaphors. Preserve the author's expressive intent
without presenting an implementation, subjective experience or measured result
that the available evidence does not establish.

## How to read

Start from the missing question; a complete reading sequence is not a prerequisite:

- `docs/<lang>/manifesto.md`: purpose, character and participation in an unfinished idea.
- `docs/<lang>/stack.md`: historical v1.0–v1.4 axes and possible engineering forms.
- `docs/<lang>/threads.md`: six cross-cutting questions across those stages.
- `docs/<lang>/interaction.md`: human/agent collaboration, continuity, sharing and learning.
- `docs/<lang>/cases.md`: four examined episodes, alternative moves and neighboring checks.
- `docs/<lang>/contracts.md`: format boundaries and schema-compatible examples.

`<lang>` is `ru` (primary) or `en`; maintained documents are full semantic mirrors.
The original `MANIFEST.md` / `MANIFEST.en.md` and `vibe.config*.json` are historical
v1.2 snapshots, not current guidance or current-schema examples. Keep their content
as history; a visible status note may point to the maintained documents.

## Machine-readable contracts

`schemas/` contains JSON Schema draft 2020-12 for Persona, MorphEvent and
MorphProposal. `ReflectionPass` is illustrative and has no schema here.
A schema validates structure, not permissions, client loading, behavior or learning.
Persona's optional `behavior.scenarios` describes authored situations and guidance;
these intentions are distinct from a VibeCase recording observed behavior and feedback.
Older Persona objects remain valid. Consumers of `scenarios` need the updated schema
and a capable adapter; do not assume older clients will load or apply the new field.
`examples/aura.ru.json` and `examples/aura.en.json` use the current Persona schema.
Neither a tool declaration nor a schedule in a legacy example creates a capability.

## Conventions

- Every maintained document under `docs/{ru,en}/` has YAML frontmatter:
  `title`, `lang`, `version`, `layer`. Version is the **document revision**;
  the v1.0–v1.4 conceptual ladder has a separate meaning.
- Preserve existing headings/anchors; readers may have external deep links.
- Use relative local links and a top-of-document RU↔EN language link.
- Update the matching language, navigation and examples when changing meaning.
- Preserve attribution, licenses and historical records. Do not add private context.
- Keep public cases anonymized. Label edited/translated dialogue and distinguish
  verified episodes, participant reports, proposed alternatives and synthetic probes.
  Private source links, local paths and conversation IDs belong outside this repository.
- Match specificity to the problem: no new mandatory persona questionnaire,
  novelty ritual or duplicated runtime policy merely to make the text look complete.

## Invariants worth honoring

- Character is expressed through choices, including ordinary success and discovery.
- The next move depends on the conversation's meaning: a question, tease, exploration
  and assignment may use similar words. Tone alone does not establish a fitting choice.
- Humans and agents can develop the question together; discussion is not an assignment.
- Experience may revise understanding without creating a new rule or memory record.
- Consolidation preserves sources, conditions and counterexamples; smaller is not automatically better.
- Shared infrastructure does not remove project boundaries or turn echoes into independent evidence.
- Durable agent-initiated contract changes need a concrete human decision; Anchor
  changes need substantive conversation. Once authorized, an agent may apply the
  agreed edit. A current explicit editing request already supplies authority within
  its scope; an `approved` field alone does not.
- File version, runtime loading, observed behavior and human experience are distinct claims.
- Pair a useful lesson with a neighboring situation where the move should change.
  Local correction and acceptance of a direction do not prove lasting improvement.

## Working on this repository

For a requested change, inspect relevant sources, make a complete scoped edit and
run `python3 scripts/validate.py` plus `python3 -m unittest discover -s tests -v`.
Use `requirements-dev.txt` in an isolated environment if dependencies are absent.
The gate is offline and read-only; it does not certify external URLs or runtime behavior.

Review the diff, preserve unrelated changes and create a focused local commit for
an implementation task unless the user requested otherwise. Publish only when the
current task authorizes it, to the named repository/branch without force. Use the
client's higher-priority instructions for permissions and execution boundaries.
