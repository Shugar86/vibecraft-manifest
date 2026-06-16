---
title: VibeCraft — The Version Ladder
lang: en
version: 1.4
layer: philosophy + engineering
---

# The version ladder: v1.0 → v1.4

🌐 [Русский](../ru/stack.md) · **English** · [← overview](../../README.en.md)

> Each version is a thesis about what emotion became. Under each axis, two levels: **why** (in prose)
> and **🔧 how** (engineering). The whole vision — [`manifesto.md`](./manifesto.md).

```
v1.0   Foundation  emotion is architecture      VibeSpark · VibeCore
v1.1   Character   emotion is data              VibePersona · VibeBehavior · VibeCases
v1.1.1 Operations  emotion is operation         VibeFlow · VibeFix · VibeMix · VibeMorph
v1.2   Life        emotion is a living process  VibeMorph² · VibeSync · VibePulse · VibeGuard
v1.3   Society     emotion is a network         VibeSocial · VibeLearn · VibeForge · VibeScale
v1.4   Reflection  emotion is reflection        VibeReflect · VibeLearn
```

---

## v1.0 — Foundation: "emotion is architecture"

Emotion is not cosmetics on a finished product but an architectural decision: color, rhythm, button,
animation, information density shape the feeling before any text.

- **VibeSpark** — why a persona/feature exists at all; what feeling remains after the interaction (one sentence).
- **VibeCore** — how the product feels: a vibe token (`calm` / `professional` / `energetic` / `playful`) + 3 observable rules.

---

## v1.1 — Character: "emotion is data"

The soul moves from code into config and becomes a validatable, testable, composable artifact.

- **VibePersona** — who speaks: role, voice, emotions, values, taboos.
- **VibeBehavior** — how it reacts: scenarios for success/empty/error/off-topic (jazz rules, not if/else).
- **VibeCases** — how we verify: a human said "yes, that's the feeling." A tone autotest is optional, the human one is mandatory.

### 🔧 Engineering

```python
class VibePersona(BaseModel):       # static — "who you are"
    role: str; voice: str
    core_emotions: list[str]; values: list[str]; taboos: list[str]

class VibeBehavior(BaseModel):      # dynamic — "how you react"
    on_tool_success: str | None = None
    on_tool_no_results: str | None = None
    on_tool_error: str | None = None
    on_offtopic: str | None = None
    model_config = ConfigDict(extra="forbid")   # a typo → ValidationError, not a silent bug
```

Assembly pipeline: `persona.yaml → validate → PromptCompiler → system prompt`. The compiler is an
interpreter of a declarative DSL into a context-aware prompt (like CSS-in-JS: you set the structure,
it generates the final). This gives versioning, optimization for cheap models, and diagnostics.

---

## v1.1.1 — Operations: "emotion is operation"

The v1.1 contract is on paper. v1.1.1 is what a persona won't survive to its second session without.

- **VibeFlow** — how it remembers: layered memory + a deterministic boot sequence + crash recovery.
- **VibeFix** — how it survives: schema validation, dual deploy, kill switch, selective silence.
- **VibeMix** — how it's assembled: `persona.yaml → compiler → prompt`; multi-persona = picking another YAML.
- **VibeMorph (v1)** — how it reloads: hot-reload of rules instead of "in the chat's head."

### 🔧 Engineering

**Memory in layers, with a fixed load order:**

```
operational  STATE.md            current task, status          TTL: session
daily        memory/<date>.md    raw logs of the day           TTL: 2-3 days
long-term    MEMORY.md           curated knowledge (private)   TTL: while relevant
atomic       entities/<name>.md  one dossier = one entity      TTL: permanent
```

- **Boot sequence** — the model doesn't "recall on demand," it either loads a file or it doesn't.
  A fixed order (`identity → user → state → today → long-term`) = the same minimal consciousness at startup.
- **Crash recovery** — if `STATE.status ∉ {DONE, IDLE}`, the task resumes immediately, no questions.
- **VibeFix:** `extra="forbid"` forbids silent config errors; one source of truth — many bodies with
  different tools; staged rollout with KPI gates and an instant kill switch; the rule "stay silent if
  the reply is just 'ok'" (in a live chat people don't answer every message).

---

## v1.2 — Life: "emotion is a living process"

The persona becomes alive: it evolves, stays itself across platforms, acts on initiative, and watches
its own integrity. The four properties of the living: adaptation, presence, initiative, self-preservation.

### VibeMorph² — evolution without losing identity (Ship of Theseus)

What is the skeleton (don't touch), what are the muscles (train them):

```yaml
anchor.immutable:      [name, values[0], core_emotions[0]]   # touched → it's NO LONGER that persona
anchor.semi_immutable: [role, taboos]                        # allowed, but review + justification
surface.free_evolve:   [behavior.*, router_examples]         # change freely
surface.guided_evolve: [voice, core_emotions[1:], taboos[1:]] # by data
```

- **MorphEvent** — an atomic change with `author / type / field / old→new / reason / rollback_safe`. It's `git blame` for the soul.
- **MorphPolicy** — boundaries: per-session/per-week edit limits, a rollback window, "run VibeCases after N edits."
- **MorphHistory** — a versioned journal; **MorphExperiment** — A/B testing of vibe (control vs treatment + metrics).

### VibeSync — one soul, many bodies → [interaction.md](./interaction.md#one-soul-many-bodies)

### VibePulse — proactivity

`PulseSchedule` — monitors with priorities (frequent ones on a cheap model, expensive ones every few
hours), `PulsePolicy` — quiet hours, cooldown, a daily initiative limit. Escalation Level 0→3:
background (silent) → note (mention later) → message (send) → urgent (ignore the silence).

### VibeGuard — the immune system

`GuardRule` catches drift: pattern-match (taboo phrases), `llm-as-judge` (compliance with the persona,
a threshold), `schema-validation` (integrity → block deploy). `GuardScore` (0-100) aggregates
tone/taboo/schema/sync. Guard **alerts, it doesn't censor** (except schema integrity).

> **The closed loop of v1.2:** Sync (one source) → Pulse (acts) → Guard (monitors) → Morph
> (evolves on Guard's data) → back to the persona. Feedback, not a static config.

---

## v1.3 — Society: "emotion is a network of personas"

One living agent is powerful. The power is when agents **talk, learn, and are created from templates**.

- **VibeSocial** — `SocialGraph` (`knows / trusts / defers_to`) + `SocialProtocol` (message types,
  "a request needs a response," conflict → escalate to a human) + a shared fleet knowledge base. → [interaction.md](./interaction.md#shared-memory-shared-edits)
- **VibeLearn** — from logs to a proposal: `pattern → edit proposal → human review → commit`.
  **Human-in-the-loop is mandatory**: Learn proposes, it doesn't apply.
- **VibeForge** — a persona factory in 15 minutes: inheritable templates (`extends` / `overrides`) + a 10-question interview → a ready `persona.yaml`.
- **VibeScale** — fleet management: a dashboard (personas × instances × GuardScore), global policies (`auto_rollback_if_guard_below`), cost-routing by task type.

---

## v1.4 — Reflection: "emotion is reflection"

Between "notice" (Guard) and "change" (Morph), a link is missing — **making sense**. You can't honestly
change without understanding what happened to you.

- **VibeReflect** — a "dream": a pass over memory + sessions → three mirrors (Self / User / Env), consolidation (compress, don't hoard).
- **VibeLearn** — reflection yields a `MorphProposal`; a human reviews; the core (Anchor) changes only through conversation.

The triad **Reflect → Learn → Morph** (understand → propose → change) — in detail in
[interaction.md](./interaction.md#the-self-learning-loop) and [contracts.md](./contracts.md).

---

[← manifesto](./manifesto.md) · [interaction →](./interaction.md) · [contracts →](./contracts.md)
