# VibeCraft

🌐 [Русский](./README.md) · **English**

[![License: CC BY 4.0 + MIT](https://img.shields.io/badge/license-CC_BY_4.0_%2B_MIT-green.svg)](./LICENSE.md)
[![Docs revision](https://img.shields.io/badge/docs-1.1.0-blue.svg)](./CHANGELOG.en.md)

> **Character through choice. Collaboration through shared thought.**
> A manifesto about designing the experience of digital products and AI agents —
> for humans and for agents that also use tools, read instructions and make decisions.

This is an author's philosophy and an engineering orientation, not a framework
or proof of a machine's “soul.” The metaphor denotes recognizable character and
continuity of commitments. Start with the [manifesto](./docs/en/manifesto.md).

## Thesis

The original formula **AI operator = Persona + Skills + Autonomy** helps separate
character, capabilities and independence. It does not replace data, domain
competence, verification or real infrastructure.

I am interested in an agent that participates in shaping the idea: offers its own
thought, develops another's, notices a tension and revises its own move. The human
need not arrive with a complete specification or continually correct the agent.

Such work needs an environment: an understandable purpose, available decision
grounds, tools that reveal consequences and recoverable context. Useful initiative
also happens in conversation; background-action counts do not measure it.

A product's character is a consistent pattern of choices. What does it notice?
How does it develop a successful moment? When does it offer something unexpected,
and when does it leave room? Form, rhythm, voice and behavior express the vibe
together — not only the lines spoken after an error.

## The version ladder — how the vision moved

v1.0–v1.4 form a historical map of expanding questions, **not installed runtime
versions**. The document revision is **1.1.0**, a separate numbering scheme.
The full [ladder](./docs/en/stack.md) retains the axes and clarifies their limits.

| Stage | What becomes a design concern | Axes |
|---|---|---|
| v1.0 — Foundation | Feeling and the architecture of experience | Spark · Core |
| v1.1 — Character | Persona descriptions and observable choices | Persona · Behavior · Cases |
| v1.1.1 — Operations | Context, assembly, outcomes and recovery | Flow · Fix · Mix · Morph |
| v1.2 — Life | Continuity, change and initiative | Morph² · Sync · Pulse · Guard |
| v1.3 — Society | Interaction and reuse | Social · Learn · Forge · Scale |
| v1.4 — Reflection | Understanding experience before changing | Reflect · Learn |

## How agents interact

- **With a human:** develop an unfinished thought together. Equality in reasoning
  does not require identical authority; a tentative idea is not an assignment.
- **Across channels:** retain meaningful commitments while adapting form and actions.
  A shared hash identifies an artifact, not equal behavior or confirmed loading.
- **With other agents:** pass sources, decision reasons and uncertainty. A shared
  database does not open every project; retelling one source does not make it
  independent corroboration.
- **Through experience:** Reflect helps investigate; Learn revises understanding.
  Morphing a durable contract is not always needed. A local correction, new
  distinction or retained good decision may be enough.

Compression is not an end in itself; no new rules need not mean failed learning.
See [interaction](./docs/en/interaction.md).

## Philosophy + engineering

| Read | Purpose |
|---|---|
| [Manifesto](./docs/en/manifesto.md) | Character, independence and a shared idea in the making |
| [Ladder](./docs/en/stack.md) | The axes' history and possible engineering expressions |
| [Six threads](./docs/en/threads.md) | Cross-cutting questions about humans, agents, continuity and change |
| [Interaction](./docs/en/interaction.md) | Shared thought, Sync, Social and learning from experience |
| [Contracts](./docs/en/contracts.md) | The limits of Persona, Morph and Reflection formats |
| [JSON Schema](./schemas/) | Persona, MorphEvent and MorphProposal structures; not a runtime |
| [Current Aura example](./examples/aura.en.json) · [RU](./examples/aura.ru.json) | A minimal persona compatible with the current schema |

**Included:** bilingual documents, three JSON schemas, examples and validation.
**Not implemented here:** PromptCompiler, memory backend, scheduler, automatic
Morph, inter-agent transport and client integrations. A format does not create a capability.

## For humans and for machines

Read for the question at hand, not necessarily the whole corpus in order. For
intent, use the manifesto; for a format, contracts; for continuity, interaction.
[AGENTS.md](./AGENTS.md) provides agent navigation and repository-work conventions.

Validation (Python 3.10+; dependencies are only for document development):

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s tests -v
```

Checks cover local Markdown links and headings, RU/EN file sets and metadata,
frontmatter, JSON Schema, and current JSON examples. Semantic translation parity
requires editorial review. External URLs, raw HTML, runtime behavior, and human
experience are not checked; JSON Schema `format` remains an annotation.
The [validator](./scripts/validate.py) describes its coverage limits.

## Principle

A useful thought may have no file yet. An agreement needs an accessible record
when it would otherwise be lost. A claim that a feature works needs a mechanism
and evidence. Engineering helps give an idea form; an artifact's existence alone
does not make the idea worthwhile.

## VibeCraft ≠ "vibe coding"

This is a difference in emphasis, not a ranking or a claim that other practices
cannot have character or scale. VibeCraft asks **what experience we create and
how we participate in its conception**. Code can be written in any way; the
approaches are compatible.

## Historical seed

[MANIFEST.en.md](./MANIFEST.en.md) · [Русский](./MANIFEST.md) and
[vibe.config.en.json](./vibe.config.en.json) · [Русский](./vibe.config.json) remain
**v1.2** snapshots. They contain earlier formulations and a different configuration
format. They are not current policy, a verified runtime or examples of today's
`persona.schema.json`; the old external `$schema` is not used by the local gate.

## License

Dual — [LICENSE.md](./LICENSE.md): text is CC BY 4.0; code and configurations are MIT.
Attribution is retained; revision history is in [CHANGELOG.en.md](./CHANGELOG.en.md).

© 2025–2026 Alexander Zakharchenko · R&D Holding "Zakharchenko" ([Shugar86](https://github.com/Shugar86)).
