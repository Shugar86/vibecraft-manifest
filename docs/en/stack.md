---
title: VibeCraft — The Version Ladder
lang: en
version: "1.2.0"
layer: philosophy + engineering
---

# The version ladder: v1.0 → v1.4

🌐 [Русский](../ru/stack.md) · **English** · [← overview](../../README.en.md)

> The ladder is a historical map of how VibeCraft's intent expanded, not releases of an installed
> framework or a required implementation sequence. Frontmatter `version` identifies the document
> revision. Each axis explores **why** and a possible **🔧 how**.
> The whole vision — [manifesto](./manifesto.md); analyses of concrete scenes — [VibeCases](./cases.md).

```
v1.0   Foundation  emotion is architecture      VibeSpark · VibeCore
v1.1   Character   emotion is data              VibePersona · VibeBehavior · VibeCases
v1.1.1 Operations  emotion is operation         VibeFlow · VibeFix · VibeMix · VibeMorph
v1.2   Life        emotion is a living process  VibeMorph² · VibeSync · VibePulse · VibeGuard
v1.3   Society     emotion is a network         VibeSocial · VibeLearn · VibeForge · VibeScale
v1.4   Reflection  emotion is reflection        VibeReflect · VibeLearn
```

"Emotion," "soul," and "life" are a language for designing experience and continuity of character,
not evidence of a model's inner experience. The schemas in this repository describe data formats;
a concrete runtime must implement prompt compilation, memory, scheduling, background passes, and rollout.

---

## v1.0 — Foundation: "emotion is architecture"

Feeling arises from how work is arranged: what draws attention, what can be trusted, where one
pauses, and what invites continuation. Color, rhythm, density, and movement participate alongside
the logic of action. Character is more than the absence of friction: a workshop may invite
exploration, an editor protect concentration, a partner notice a connection not yet fully formed.

**The working unit of character is the next move in a situation:** a reply, action, draft or pause.
Voice makes that move recognizable; the product's design determines what it enables.
For example, a good result can be celebrated, developed further or quietly left with the person.

- **VibeSpark** — why the experience is worth creating; what action, understanding, or feeling it enables.
- **VibeCore** — a recognizable logic of choice from which concrete decisions follow. For example,
  "an unfinished thought is already something we can work on together here." A vibe token can give
  it a short name, but cannot replace its meaning and is not a required ceremony.

---

## v1.1 — Character: "emotion is data"

An explicit, versioned contract preserves part of the intent and makes it easier to discuss.
Both the written direction and its grounds matter: what to notice, what to leave room for,
which possibility to open. The actual choice is checked in use.

- **VibePersona** — a position and room for improvisation: what matters, what the persona notices,
  which role it occupies, how it sounds, and which commitments it preserves.
- **VibeBehavior** — choosing in response to what is happening: developing a tentative thought,
  joining a teasing exchange, celebrating success, carrying out an accepted decision. A question
  can perform different actions in a conversation; context helps choose the move. Jazz rules
  guide judgment and improvisation.
- **VibeCases** — analyzing a scene through possible moves, observed behavior, the person's assessment
  and a conclusion with limits. A neighboring case calls for a different move: for example,
  a serious question alongside a sarcastic one. Discovery, ordinary success, return and difficulty
  offer different tests of character. [Four analyses](./cases.md) demonstrate this approach.

### 🔧 Engineering

One possible path: `persona data → format validation → runtime adapter → instructions available to the model`.
The existing [JSON Schemas](./contracts.md) help validate data structure, not the substance of
collaboration. `PromptCompiler` names a possible adapter, not a function shipped here.
It may assemble fields, explanations, and examples for a client; benefits for a particular model need testing.

The current Persona's optional `behavior.scenarios` describes situations beyond the named `on_*`
responses. An entry with `id`, `situation` and `guidance` preserves authored intent; observed behavior
and human assessment belong to a separate VibeCase. Existing objects without this field remain valid.
Objects using it need the updated schema and adapter support; validation against the old schema
with `additionalProperties: false` rejects them. See [contracts](./contracts.md) for details.

A machine format makes fields precise, a short rationale supports judgment, and a scene shows
the difference. A small edit needs only the context relevant to it. A full analysis belongs where
it helps choose or check behavior, rather than becoming a required questionnaire before every task.

---

## v1.1.1 — Operations: "emotion is operation"

The environment makes judgment possible: it helps find material context, understand a tool response
and recover the grounds for decisions. In a second session, this lets a useful discovery be developed;
in a new situation, it helps choose a move without gathering known information all over again.

- **VibeFlow** — context available as needed, sources, and distinguishable task state.
- **VibeFix** — diagnostics explaining an error's effect and recovery path, format checks,
  controlled introduction of changes, and stopping a problematic function when necessary.
- **VibeMix** — assembling an appropriate representation of the persona for the client and tools.
- **VibeMorph (v1)** — controlled version changes; hot reload is possible only where implemented.

### 🔧 Engineering

Distinguish the roles of context without imposing identical files and TTLs on every project:

| Role | What it helps preserve | When to consult |
|------|-------------------------|------------------|
| Contract | Purpose, commitments, boundaries | When loading applicable instructions |
| Task state | Goal, accepted decision, work done, verified results, unknowns | On resumption and before dependent actions |
| Episodic memory | Event, source, conditions, corrections, counterexamples | When history could change the current conclusion |
| Curated knowledge | Verified generalization with limits of applicability | When relevant to the current task |

- **Boot sequence** establishes the necessary foundations; further context answers a missing question.
  File availability does not mean the client loaded it; an entire archive need not enter every startup.
  Retention depends on purpose, agreed policy, and the cost of losing context, not on a layer alone.
- **Crash recovery** restores the goal and actual state. "Started," "finished," and "result confirmed"
  are different records; a timeout does not establish failure. Before repeating an external action,
  check its effect and current authority. Safe work within the existing scope can continue.
- **VibeFix** distinguishes errors, optional configuration, and unverified capabilities. A tool's
  recommendation helps choose a move but grants no permission. Memory is read only in an authorized
  context; a private session alone does not authorize any profile or access to another project.

---

## v1.2 — Life: "emotion is a living process"

Character does not freeze in its first successful line: it changes expression, preserves commitments,
and finds an appropriate next move. "Living process" is a metaphor for that work over time, not a
property that follows from having a config or background service.

### VibeMorph² — evolution without losing identity (Ship of Theseus)

**Anchor** names agreed foundations of identity; **Surface** is their changeable expression.
The distinction follows the persona's meaning, not universal indices such as `values[0]` or
`core_emotions[0]`. Changing a word need not change character; keeping a name does not guarantee
the same commitments.

- **MorphEvent** — an atomic record: who, what, old → new, why, and claimed rollback safety.
  The project workflow links it to verification methods and results; the current schema does not
  contain all the fields such an audit needs. → [Contracts](./contracts.md)
- **MorphPolicy** — who decides, what gets checked, and how a change is applied and recovered.
  Anchor changes require substantive conversation and an explicit human decision; Surface changes
  stay within authorized scope following a human decision. An agent may apply an approved diff,
  not merely propose it. The current assignment may already contain that decision; no separate
  ceremony is then needed. An artifact saying `approved` does not itself create authority.
- **MorphHistory** preserves reasons and consequences. **MorphExperiment** compares meaningful
  scenes and allows the original intent to be wrong; the number of edits does not measure development.

### VibeSync — one soul, many bodies → [interaction.md](./interaction.md#one-soul-many-bodies)

A common persona source helps retain commitments while their expression varies across channels.
A hash checks the equality of a particular artifact, not agent identity, loading, or identical behavior.
Full prompts for different clients may reasonably differ.

### VibePulse — proactivity

Initiative may be a useful connection within a discussion, a small separate probe or authorized
monitoring. Its scale depends on interest, the cost of error, established boundaries and the ability
to set the probe aside. A tangible result may open a new activity; a pause may leave room for
the person's next thought. Neither requires constant novelty.

An invitation to try something does not establish permission for spending or publication.
An accepted assignment allows work to continue within its boundaries. Background action needs
a working scheduler, a specified task and authority. `PulsePolicy` may define quiet hours,
cooldowns and urgency criteria; "urgent" does not override boundaries.

### VibeGuard — the immune system

"Immune system" means feedback about the loss of desired properties. A `GuardRule` may check
structure, a concrete violation, or behavior diverging from VibeCases. A model judge contributes an
observation, not a final verdict. A `GuardScore`, if useful, is a condensed signal with components
and limitations, not the persona's health or worth. Choose an action by cause and risk:
investigate, warn, stop unsafe execution, or roll back an authorized change.

> A possible v1.2 feedback path: Sync → appropriate initiative → observation → understanding → needed action.
> Not every signal requires Morph; confirming the previous decision can also be the right result.

---

## v1.3 — Society: "emotion is a network of personas"

Working together is valuable when different positions reveal what one alone misses. The aim is not
the number of agents or their agreement, but stronger shared understanding and a complete result.

- **VibeSocial** — explicit roles, addressing, provenance, and access to needed context.
  `knows / trusts / defers_to` describe relationships, not wider permissions. A technical dispute can
  be resolved through a check; a human priority through clarification. Several retellings of one
  source retain a single basis. → [interaction.md](./interaction.md#shared-memory-shared-edits)
- **VibeLearn** — `experience → revised understanding → useful next move`. That may be a new
  question, a check, a tool repair, knowledge saved to authorized memory, or a MorphProposal.
  The last is for a justified durable contract change, not for every lesson.
- **VibeForge** — reusing tested parts of a persona while preserving authorial intent.
  A template may preserve a useful logic of choice while a new scene reveals a different expression.
  For example, what will this editor notice in a good draft, and how will it help develop that finding?
  This tests the new persona's own character; filled fields alone are insufficient.
- **VibeScale** — visibility into versions, access, costs, result quality, and unfinished operations.
  Shared memory retains access boundaries; publishing a record does not mean everyone read and checked it.
  Fleet policy needs a verified signal and an authorized mechanism, not a single magical score.

---

## v1.4 — Reflection: "emotion is reflection"

Making sense of experience helps reveal what to preserve and what to reconsider. A successful
improvisation can expose a possibility absent from the original intent; a miss can show where
the agent answered a neighboring question. Look for the cause in the particular episode,
the environment, the agent's own conclusion or a durable rule.

- **VibeReflect** — a "dream" as a metaphor for a separate pass over available experience.
  Self / User / Env are perspectives: the agent's decisions, what the human explicitly said, and
  conditions and tools. Hypotheses about the human remain hypotheses, not hidden knowledge about them.
- **VibeLearn** — extracting understanding usable in the next decision. Consolidation may remove
  duplicates, connect material, or preserve a contradiction; mandatory compression damages learning
  when it loses a source or counterexample. No MorphProposal does not mean no lesson.

The triad **Reflect → Learn → Morph** names one branch: make sense → revise understanding → change
the contract if needed under an accepted decision. A repaired answer after an explicit correction
is observable now. Durable learning needs later relevant episodes, including a neighboring case
under different conditions. The agent's account of what it understood cannot replace that check.
More in [VibeCases](./cases.md), [interaction.md](./interaction.md#the-self-learning-loop)
and [contracts.md](./contracts.md).

---

[← manifesto](./manifesto.md) · [VibeCases →](./cases.md) · [interaction →](./interaction.md) · [contracts →](./contracts.md)
