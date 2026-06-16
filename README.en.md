# VibeCraft

🌐 [Русский](./README.md) · **English**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/VibeCraft-v1.4-blue.svg)](./CHANGELOG.md)
[![Docs: RU · EN](https://img.shields.io/badge/docs-RU%20%C2%B7%20EN-success.svg)](./docs)
[![Layer: philosophy + engineering](https://img.shields.io/badge/layer-philosophy%20%2B%20engineering-D97757.svg)](./docs/en/stack.md)

> **A manifesto on how to engineer an AI agent's "soul" — and how agents interact with each other.**
> Not a framework. A way of thinking about how AI systems are built — any of them, not just coding ones.

---

## Thesis

The market builds **snowflakes**: one bot per task, one team, one stack. But under the hood, every
"unique" agent runs the same logic. VibeCraft claims:

> **An AI operator = Persona + Skills + Autonomy.**
> Give the agent an identity (who it is), teach it skills (what it can do), and grant it freedom to
> decide (how it acts) — whether it's a salesperson, a tutor, a content agent, or a legal assistant.

This pattern is **framework-agnostic** (LangGraph, CrewAI, AutoGen, a bare SDK — doesn't matter).
It depends on architectural vision. And on one radical idea: **an agent's emotion and character can
be coded, tested, versioned, and rolled back**, like any other layer.

---

## The version ladder — how the vision moved

A version is not a number but a **thesis about what emotion became**. Full map — [`docs/en/stack.md`](./docs/en/stack.md).

| Version | Layer | Thesis | Axes |
|---------|-------|--------|------|
| **v1.0** | Foundation | emotion is **architecture** | VibeSpark · VibeCore |
| **v1.1** | Character | emotion is **data** | VibePersona · VibeBehavior · VibeCases |
| **v1.1.1** | Operations | emotion is **operation** | VibeFlow · VibeFix · VibeMix · VibeMorph |
| **v1.2** | Life | emotion is a **living process** | VibeMorph² · VibeSync · VibePulse · VibeGuard |
| **v1.3** | Society | emotion is a **network of personas** | VibeSocial · VibeLearn · VibeForge · VibeScale |
| **v1.4** | Reflection | emotion is **reflection** | VibeReflect · VibeLearn |

---

## How agents interact

The manifesto's main plot is not the lonely persona but the **interaction**. In full — [`docs/en/interaction.md`](./docs/en/interaction.md).

- **One soul, many bodies** (VibeSync): one source of truth (`persona.yaml`), many runtimes
  (Telegram, web, CLI, API) with different tools and models. The invariant — an identical hash of the compiled prompt.
- **Shared memory, shared edits** (VibeSocial): several agents share one memory store and one
  proposal queue. Friction noticed by one becomes an edit another applies.
- **The self-learning loop** (VibeReflect → VibeLearn → VibeMorph): the agent makes sense of what
  happened to it, proposes a change to itself — and changes **under human review**, keeping an untouchable core.

---

## Philosophy + engineering

Every axis is given on two levels: **why** (in prose) and **how** (schemas, contracts, pipelines).

| Document | About |
|----------|-------|
| [`docs/en/manifesto.md`](./docs/en/manifesto.md) | The vision: why an agent needs an engineered soul |
| [`docs/en/stack.md`](./docs/en/stack.md) | The ladder v1.0→v1.4, each axis: thesis + engineering |
| [`docs/en/threads.md`](./docs/en/threads.md) | **Walkthrough by version:** human↔AI, AI↔AI, where the soul is, change, protection |
| [`docs/en/interaction.md`](./docs/en/interaction.md) | How agents interact: Sync, Social, shared memory, the loop |
| [`docs/en/contracts.md`](./docs/en/contracts.md) | Formal contracts: Persona, Anchor/Surface, Morph, Reflection |
| [`schemas/`](./schemas) | Machine-readable JSON schemas (language-neutral) |

Russian: [`docs/ru/`](./docs/ru). For an agent reader: [`AGENTS.md`](./AGENTS.md).

---

## For humans and for machines

- **For humans** — start with the [manifesto](./docs/en/manifesto.md) (vision), then the [ladder](./docs/en/stack.md) (mechanics).
- **For machines** — [`AGENTS.md`](./AGENTS.md) describes how to read the repo; [`schemas/`](./schemas)
  gives the contracts as JSON Schema. Heading structure and frontmatter are stable and parseable.

---

## Principle

> Behind every word, an artifact. "Soul," "dreams," "reflection" are metaphors for an engineering
> process (config, validation, consolidation, review). If a word has no file, schema, and check
> behind it — it's noise, not VibeCraft. The goal is to travel from artistic intuition to engineering
> discipline **without losing the soul**.

---

## License

[MIT](./LICENSE) © 2026 Shugar86. Ideas — free to use and build upon.
