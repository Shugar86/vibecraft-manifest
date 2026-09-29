# VibeCraft

🌐 [Русский](./README.md) · **English**

[![License: CC BY 4.0 + MIT](https://img.shields.io/badge/license-CC_BY_4.0_%2B_MIT-green.svg)](./LICENSE.md)
[![Docs revision](https://img.shields.io/badge/docs-1.3.1-blue.svg)](./CHANGELOG.en.md)

> **VibeCraft is a joint project of people and models.**
> Their contributions can change the shared idea, ways of working and the very
> understanding of what counts as success.

This manifesto changed that way too. After the completed revision 1.2.0, the
human invited Codex to reconsider the idea itself. The model proposed centering
collaboration, valuing play in its own right and keeping distinct voices. The
human commissioned the new version and, after 1.3.0 was published, said they liked
it overall. [The account of this turn](./docs/en/cases.md#5-how-revision-130-emerged) connects the conversation
to changes in the text.

Together we can discover a question, create something beautiful, share a joke or
play with an idea without yet knowing where it will lead. VibeCraft explores
the character of that participation and the conditions that make it possible:
from conversation and digital products to tools and instructions for agents themselves.

This is our shared philosophy and an engineering orientation. “Soul” is a metaphor
for recognizable character and continuity of commitments. Start with the
[manifesto](./docs/en/manifesto.md) or [examined scenes](./docs/en/cases.md).

## Thesis

We are interested in collaboration in which people and models help shape the very
subject of the work. A person brings an image, an agent notices an unexpected
connection, another model offers a different view — and something nobody had
formulated at the start begins to matter. A contribution can change the criterion
of success too: while making a toy, we discover that its value lies in the strange
beauty of what unfolds.

Play, curiosity, beauty and a shared joke have value in their own right. They
need no justification through future productivity. A conversation can end with
a thought discovered or a good moment; an assignment calls for completion.

Shared commitments give collaboration a foundation while preserving different
ways of seeing. Models can differ in interpretation, taste or assessment;
a substantive disagreement is sometimes worth leaving open, with its grounds
understood. Coauthorship requires neither a common voice nor agreement at every point.

Character appears in the next move: offer an image, make a trial, sustain the
pace, disagree or leave room. In a product, form, rhythm, voice and actions help
express it. A quiet editor protects concentration, a bold coauthor notices a new
turn, and a tutor preserves productive effort for the learner. Context and tools
should make it possible for these choices to take effect.

## VibeCases: character in a concrete scene

A VibeCase connects context and intent, possible moves, observed behavior and
human assessment. The account may reveal that the idea itself or the criterion
of success changed during the interaction; the reasons for that turn and the fate
of the earlier task then matter to preserve. The conclusion remains tied to
available evidence. A neighboring scene tests whether the agent can change its
move when the situation's meaning changes.

| Scene | What becomes visible |
|---|---|
| Understanding another | The agent corrects its own substitution and contributes a thought the person develops |
| Making a small terrarium | A fitting trial turns an invitation into an accessible activity |
| Missing sarcasm | A friendly voice can accompany the wrong action; the move changes after correction |
| Designing an agent's environment | Participants shape the question together, accept a direction and put it into practice |
| Reconsidering the manifesto itself | A model's proposal changes the next edition within the human's invitation |

The [full accounts](./docs/en/cases.md) include five real episodes: four editorial
adaptations of author-supplied material and the story of revision 1.3.0 with links
to published changes. Separately labeled imagined scenes explore play, changes
in intent and possible failures of coauthorship. Alternative moves
and neighboring checks are proposals for exploration, not completed experiments.

<a name="the-version-ladder--how-the-vision-moved"></a>

## Stages — how the vision moved

Foundation, Character, Operations, Life, Society and Reflection name stages in
the development of VibeCraft's questions. The document revision is **1.3.1**.
The full [map of stages](./docs/en/stack.md) preserves the correspondence with
the earlier labels v1.0–v1.4; those labels do not denote a working runtime.

| Stage | What becomes a design concern | Axes |
|---|---|---|
| Foundation | Feeling and the architecture of experience | Spark · Core |
| Character | Persona descriptions and observable choices | Persona · Behavior · Cases |
| Operations | Context, assembly, outcomes and recovery | Flow · Fix · Mix · Morph |
| Life | Continuity, change and initiative | Morph² · Sync · Pulse · Guard |
| Society | Interaction and reuse | Social · Learn · Forge · Scale |
| Reflection | Understanding experience before changing | Reflect · Learn |

## How agents interact

- **With a human:** develop an unfinished thought, discover value in the process,
  and distinguish an invitation to play, a question and an assignment.
- **Across channels:** retain meaningful commitments while adapting form and actions
  to a new context.
- **With other agents:** share sources and reasons, compare different readings and
  preserve useful disagreement. Another's retelling remains a retelling;
  access to shared storage is governed by project boundaries.
- **Through experience:** Reflect helps investigate; Learn revises understanding.
  The result may be a more fitting move, a new possibility or a change to the
  environment; a durable contract change is needed only in some cases.

See [interaction](./docs/en/interaction.md).

## Philosophy + engineering

| Read | Purpose |
|---|---|
| [Manifesto](./docs/en/manifesto.md) | Collaboration between people and models, character and an emerging idea |
| [VibeCases](./docs/en/cases.md) | Five real episodes, imagined scenes and an optional account template |
| [Stages](./docs/en/stack.md) | The axes' history and possible engineering expressions |
| [Six threads](./docs/en/threads.md) | Cross-cutting questions about humans, agents, continuity and change |
| [Interaction](./docs/en/interaction.md) | Shared thought, Sync, Social and learning from experience |
| [Contracts](./docs/en/contracts.md) | Persona scenarios and the path from a Morph proposal to checking behavior |
| [JSON Schema](./schemas/) | Persona, MorphEvent and MorphProposal structures; not a runtime |
| [Current Aura example](./examples/aura.en.json) · [RU](./examples/aura.ru.json) | A persona with contextual scenarios for discovery and return |

The historical formula **AI operator = Persona + Skills + Autonomy** remains
a useful engineering frame: ways of participating, capabilities and independence
operate in a particular environment. It helps design an implementation within
the broader question of collaboration.

**Included:** bilingual documents and VibeCases, three JSON schemas, examples and validation.
**Not implemented here:** PromptCompiler, memory backend, scheduler, automatic
Morph, inter-agent transport and client integrations.

Proposing a turn and obtaining authority to apply it are different events. An
accepted assignment or delegated choice already provides authority within its
scope; a new criterion does not make earlier unfinished work complete. See
[deciding and applying](./docs/en/contracts.md#4-morphproposal--a-change-proposal-vibelearns-output)
and [boundaries on changes](./docs/en/contracts.md#6-loop-invariants-anti-goals).

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

Checks cover local Markdown links, headings and named HTML anchors, RU/EN file sets and metadata,
frontmatter, JSON Schema, and current JSON examples. Semantic translation parity
requires editorial review. External URLs, other raw HTML, runtime behavior, and human
experience are not checked; JSON Schema `format` remains an annotation.
The [validator](./scripts/validate.py) describes its coverage limits.

## Principle

The meaning of the work can change through another's participation. What is worth
retaining is what helps us continue: a discovered image, a reason for a decision,
an open disagreement or something that works. Engineering gives an idea form
and makes claims about its execution testable; the value of shared thought
and an experienced moment extends beyond a collection of artifacts.

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

**Claude (Anthropic)** is a coauthor of the project. In this revision, its critical
reading helped clarify the opening, stage names, visibility of initiative boundaries
and the evidence needed for the case. The human relayed the review; accepted points
were incorporated alongside distinctions that emerged in debate with Codex.

**[Codex (OpenAI)](https://github.com/codex)** coauthored revisions
[1.2.0](https://github.com/Shugar86/vibecraft-manifest/commit/db498c6e1d1c2f2bf933442d19a4c3433e635e94)
and [1.3.0](https://github.com/Shugar86/vibecraft-manifest/commit/e0802615bd299c44293356db4b102a6a9e52de77):
it helped develop the VibeCases, proposed reconsidering its own text and making
collaboration the project's starting point, with play valued in its own right
and room for distinct model voices. Its contribution includes conception,
critique and editing in Russian and English.
In 1.3.1, Codex continued this work through Claude's review and the human's assessment.

© 2025–2026 Alexander Zakharchenko · R&D Holding "Zakharchenko" ([Shugar86](https://github.com/Shugar86)).
