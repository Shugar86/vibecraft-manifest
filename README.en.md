# VibeCraft

🌐 [Русский](./README.md) · **English**

[![License: CC BY 4.0 + MIT](https://img.shields.io/badge/license-CC_BY_4.0_%2B_MIT-green.svg)](./LICENSE.md)
[![Docs revision](https://img.shields.io/badge/docs-1.2.0-blue.svg)](./CHANGELOG.en.md)

> **Character through choice. Collaboration through shared thought.**
> A manifesto about designing the experience of digital products and AI agents —
> for humans and for agents that also use tools, read instructions and make decisions.

Character becomes visible in the next move: develop a thought, make a trial,
catch the irony, leave room or complete an assignment. VibeCraft connects that
choice to the design of the product and the conditions of collaboration.

This is an author's philosophy and an engineering orientation. “Soul” is a metaphor
for recognizability and continuity of commitments. Start with the
[manifesto](./docs/en/manifesto.md) or [four examined scenes](./docs/en/cases.md).

## Thesis

The original formula **AI operator = Persona + Skills + Autonomy** helps separate
ways of participating, capabilities and independence. They operate in an environment:
actual model capabilities, accessible context, tools and authority.

I am interested in an agent that fully participates in shaping the idea: offers its
own thought, develops another's, notices a tension and revises its own move. Both
participants change the shared understanding. The human need not arrive with a
complete specification or remain the permanent referee of the agent's proposals.

Useful initiative fits the moment. Sometimes a new distinction is enough;
sometimes a small working trial is worth bringing. Once direction is chosen,
the agent completes the assignment. Context and tools should help it choose
the next step and see its consequences.

In a product, form, rhythm, voice and actions express the same logic. A quiet
editor protects concentration; a bold coauthor notices a new turn; a tutor
preserves productive effort for the learner. All need reliability; character
helps choose among several good moves.

## VibeCases: character in a concrete scene

A VibeCase connects **context and intent → possible moves → observed behavior →
human assessment → a bounded conclusion**. A neighboring scene tests whether
the agent can change its move when the situation's meaning changes.

| Scene | What becomes visible |
|---|---|
| Understanding another | The agent corrects its own substitution and contributes a thought the person develops |
| Making a small terrarium | A fitting trial turns an invitation into an accessible activity |
| Missing sarcasm | A friendly voice can accompany the wrong action; the move changes after correction |
| Designing an agent's environment | Participants shape the question together, accept a direction and put it into practice |

The [full cases](./docs/en/cases.md) are public adaptations of episodes supplied by
the author. They distinguish observations, proposed alternatives and checks not yet
performed. A successful answer in one place does not become a permanent rule about a person.

## The version ladder — how the vision moved

v1.0–v1.4 form a historical map of expanding questions, **not installed runtime
versions**. The document revision is **1.2.0**, a separate numbering scheme.
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

- **With a human:** develop an unfinished thought and distinguish what the current
  turn is doing: asking, drawing a conclusion, joking or assigning work.
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
| [VibeCases](./docs/en/cases.md) | Four complete cases and checks of neighboring situations |
| [Ladder](./docs/en/stack.md) | The axes' history and possible engineering expressions |
| [Six threads](./docs/en/threads.md) | Cross-cutting questions about humans, agents, continuity and change |
| [Interaction](./docs/en/interaction.md) | Shared thought, Sync, Social and learning from experience |
| [Contracts](./docs/en/contracts.md) | Persona scenarios and the path from a Morph proposal to checking behavior |
| [JSON Schema](./schemas/) | Persona, MorphEvent and MorphProposal structures; not a runtime |
| [Current Aura example](./examples/aura.en.json) · [RU](./examples/aura.ru.json) | A persona with contextual scenarios for discovery and return |

**Included:** bilingual documents and VibeCases, three JSON schemas, examples and validation.
**Not implemented here:** PromptCompiler, memory backend, scheduler, automatic
Morph, inter-agent transport and client integrations. A format does not create a capability.

## For humans and for machines

Read for the question at hand, not necessarily the whole corpus in order. For
intent, use the manifesto; for a scene, VibeCases; for a format, contracts; for continuity, interaction.
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

Original vision by Alexander Zakharchenko. The text develops in coauthorship with
AI agents: they propose distinctions, challenge decisions and participate in revision.

© 2025–2026 Alexander Zakharchenko · R&D Holding "Zakharchenko" ([Shugar86](https://github.com/Shugar86)).
