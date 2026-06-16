# AGENTS.md — machine entry point

This file tells an AI agent (or any automated reader) how to navigate this repository.
Human entry points: [`README.md`](./README.md) (RU) · [`README.en.md`](./README.en.md) (EN).

## What this repo is

A **manifesto**, not runnable code: VibeCraft — a way of thinking about how to engineer an AI agent's
character ("soul") and how agents interact. Vendor-neutral, framework-agnostic, applies to any AI
operator, not only coding agents.

## How to read

Read in this order for the full model:

1. `docs/<lang>/manifesto.md` — the vision (Persona + Skills + Autonomy; soul as data).
2. `docs/<lang>/stack.md` — the version ladder v1.0→v1.4, each axis with thesis + engineering.
3. `docs/<lang>/threads.md` — six cross-cutting threads walked through every version:
   human↔AI via vibe, AI↔AI, where the soul lives, explaining vibe to an AI, self-change, protection.
4. `docs/<lang>/interaction.md` — Sync (one soul, many bodies), Social (shared memory + shared edits), the loop.
5. `docs/<lang>/contracts.md` — formal contracts (Persona, Anchor/Surface, MorphEvent, MorphProposal, ReflectionPass).

`<lang>` is `ru` (primary) or `en`. Both directories are full mirrors.

## Machine-readable contracts

`schemas/` holds language-neutral JSON Schema (draft 2020-12):

- `persona.schema.json` — the Persona (vibe + behavior + tools).
- `morph-event.schema.json` — an atomic change to a persona.
- `morph-proposal.schema.json` — a proposed edit awaiting human review.

## Conventions

- Every doc carries YAML frontmatter (`title`, `lang`, `version`, `layer`).
- Headings are stable; deep links rely on them.
- Cross-links are relative. RU↔EN are linked via a 🌐 line at the top of each doc.

## Invariants worth honoring

- Anchor (core identity) changes only through human conversation; surface changes go through review.
- Reflection compresses memory; it must not hoard.
- No autonomous self-editing of a contract; a human is always at the gate.
