---
title: VibeCraft — The Version Ladder
lang: en
version: "1.1.0"
layer: philosophy + engineering
---

# The version ladder: v1.0 → v1.4

🌐 [Русский](../ru/stack.md) · **English** · [← overview](../../README.en.md)

> The ladder is a historical map of how VibeCraft's intent expanded, not releases of an installed
> framework or a required implementation sequence. Frontmatter `version` identifies the document
> revision. Each axis explores **why** and a possible **🔧 how**.
> The whole vision — [`manifesto.md`](./manifesto.md).

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

- **VibeSpark** — why the experience is worth creating; what action, understanding, or feeling it enables.
- **VibeCore** — a recognizable logic of choice from which concrete decisions follow. For example,
  "an unfinished thought is already something we can work on together here." A vibe token can give
  it a short name, but cannot replace its meaning and is not a required ceremony.

---

## v1.1 — Character: "emotion is data"

Part of the intent can move from an incidental prompt formulation into an explicit, versioned contract.
But a file describes character rather than guarantees it: character becomes discernible through choices.

- **VibePersona** — a position and room for improvisation: what matters, what the persona notices,
  which role it occupies, how it sounds, and which commitments it preserves.
- **VibeBehavior** — how it develops a thought, offers a move after success, leaves initiative to
  the human, handles difficulty, and revises a mistake. Jazz rules, not a catalogue of lines.
- **VibeCases** — scenes that distinguish the intent from a generic wrapper: a successful move,
  discovery, repeated use, a relevant difficulty. Observable results and human feeling are different
  kinds of evidence; automated tone assessment substitutes for neither.

### 🔧 Engineering

One possible path: `persona data → format validation → runtime adapter → instructions available to the model`.
The existing [JSON Schemas](./contracts.md) help validate data structure, not the substance of
collaboration. `PromptCompiler` names a possible adapter, not a function shipped here.
It may assemble fields, explanations, and examples for a client; benefits for a particular model need testing.

Structure is not opposed to prose: a machine format makes fields precise, a short rationale supports
judgment, and an example shows the difference. Existing context is enough for a small edit;
a new persona questionnaire or manifesto is not required.

---

## v1.1.1 — Operations: "emotion is operation"

For the promises of character to survive a second session, the environment must help work continue,
make tool responses intelligible, and recover the reasons behind decisions.

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
  not merely propose it. An artifact saying `approved` does not itself create authority.
- **MorphHistory** preserves reasons and consequences. **MorphExperiment** compares meaningful
  scenes and allows the original intent to be wrong; the number of edits does not measure development.

### VibeSync — one soul, many bodies → [interaction.md](./interaction.md#one-soul-many-bodies)

A common persona source helps retain commitments while their expression varies across channels.
A hash checks the equality of a particular artifact, not agent identity, loading, or identical behavior.
Full prompts for different clients may reasonably differ.

### VibePulse — proactivity

Initiative may be a useful connection within a discussion, a proposed next experience, or authorized
monitoring. It does not require constant novelty: sometimes the best move is leaving space for the
human. Background action needs a working scheduler, a specified task, and authority.
`PulsePolicy` may define quiet hours, cooldowns, and urgency criteria; "urgent" does not override boundaries.

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
  be resolved through a check; a human priority through clarification. → [interaction.md](./interaction.md#shared-memory-shared-edits)
- **VibeLearn** — `experience → revised understanding → useful next move`. That may be a new
  question, a check, a tool repair, knowledge saved to authorized memory, or a MorphProposal.
  The last is for a justified durable contract change, not for every lesson.
- **VibeForge** — reusing tested parts of a persona while preserving authorial intent.
  Templates and interviews are possible means, not a promise of a finished character in a fixed time.
  A new persona is tested in its own scenes, not merely by whether its fields are filled.
- **VibeScale** — visibility into versions, access, costs, result quality, and unfinished operations.
  Shared memory retains access boundaries; publishing a record does not mean everyone read and checked it.
  Fleet policy needs a verified signal and an authorized mechanism, not a single magical score.

---

## v1.4 — Reflection: "emotion is reflection"

Between "notice" and "change," **make sense** of what happened and which explanation survives the
evidence. A correction may concern one episode, the environment, one's own conclusion, or a rule;
these are not the same change.

- **VibeReflect** — a "dream" as a metaphor for a separate pass over available experience.
  Self / User / Env are perspectives: the agent's decisions, what the human explicitly said, and
  conditions and tools. Hypotheses about the human remain hypotheses, not hidden knowledge about them.
- **VibeLearn** — extracting understanding usable in the next decision. Consolidation may remove
  duplicates, connect material, or preserve a contradiction; mandatory compression damages learning
  when it loses a source or counterexample. No MorphProposal does not mean no lesson.

The triad **Reflect → Learn → Morph** names one branch: make sense → revise understanding → change
the contract if needed under an accepted decision. Without checking subsequent behavior, a written
conclusion cannot establish durable learning. More in
[interaction.md](./interaction.md#the-self-learning-loop) and [contracts.md](./contracts.md).

---

[← manifesto](./manifesto.md) · [interaction →](./interaction.md) · [contracts →](./contracts.md)
