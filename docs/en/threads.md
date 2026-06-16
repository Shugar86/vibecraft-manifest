---
title: VibeCraft — Six Threads Across the Versions
lang: en
version: 1.4
layer: philosophy + engineering
---

# Six threads: human, agent, soul, change, protection

🌐 [Русский](../ru/threads.md) · **English** · [← overview](../../README.en.md)

> Making sense of the v1.0→v1.4 ladder not by axes but by **cross-cutting questions**. Six threads
> that run through every version and grow up a little in each.

The questions:

1. **Human ↔ AI** — how do a human and an agent interact through **vibe**?
2. **AI ↔ AI** — how does an agent interact with another agent?
3. **Where the soul is** — where does identity physically live?
4. **Explaining vibe to an AI** — how do you convey "vibe" to the model itself?
5. **Change** — how does an AI change itself; how does one AI change another?
6. **Protection** — how do agents protect themselves and the human?

| Thread | Born in | Crystallizes in |
|--------|---------|-----------------|
| Human ↔ AI via vibe | v1.0 (UI/UX) | v1.1 (VibeCases) → v1.4 (User mirror) |
| AI ↔ AI | v1.1.1 (bridge between agents) | v1.3 (VibeSocial) + v1.4 (shared memory) |
| Where the soul is | v1.1 (config) | v1.2 (Anchor/Surface) |
| Explaining vibe to an AI | v1.1 (PromptCompiler) | v1.1.1 (compiler as a DSL) |
| Changing self / another | v1.1.1 (hot reload) | v1.2 (Morph²) → v1.3 (Learn) → v1.4 (Reflect) |
| Protecting self and human | v1.1.1 (VibeFix) | v1.2 (VibeGuard) → v1.4 (anti-goals) |

---

## v1.0 — Foundation: vibe first becomes tangible

- **Human ↔ AI.** Vibe is born as a **feeling in the product** — color, rhythm, button, information
  density. A human reads the character before any text. The first shared language is the vibe token
  (`calm` / `professional` / `energetic` / `playful`).
- **Explaining vibe to an AI.** Not yet for the model; vibe is formulated for the **human designer**
  via VibeSpark: why the feature exists and what feeling it leaves.
- **Where the soul is.** Still dissolved in the product (in the design), not extracted.
- **AI ↔ AI / change / protection.** Not yet. The only protection rule is "no generic slop": don't hand
  over a faceless interface instead of a character.

> The version answers one question: emotion is **architecture**, not cosmetics. The other threads still sleep.

---

## v1.1 — Character: the soul is extracted, vibe gets a language for the model

- **Where the soul is.** The key shift: the soul is **pulled out of code into config**. `vibe` (who you
  are: role, voice, values, taboos) + `behavior` (how you react). The soul is now a **file**, not a prompt string.
- **Explaining vibe to an AI.** Here's the direct answer to "how to convey vibe to the model." Not an
  essay but **structure**: the compiler assembles `IDENTITY / ROLE / VOICE / VALUES / TABOOS` + behavior
  scenarios. Vibe is translated into the model's language as **a set of fields + jazz rules** (scenario
  instructions for improvisation, not `if/else`). The model doesn't memorize a template — it improvises within bounds.
- **Human ↔ AI.** Vibe becomes a **contract** between "what the human wanted" and "how it feels." The
  check is VibeCases: a real human says "yes, that's the feeling." Without it, vibe is only a hypothesis.
- **AI ↔ AI.** A seed: multi-persona in one thread (a Router switches personas per request).
- **Change / protection.** Still manual (edit the YAML); protection = VibeCases catches when the vibe lies.

> Emotion is **data**. The soul became a validatable, versionable artifact.

---

## v1.1.1 — Operations: the soul gains a body, memory, and first self-defense

- **Where the soul is.** Now it has a **body and memory**. A boot sequence loads identity in a fixed
  order; memory layers (operational → daily → long-term → atomic dossiers) give continuity; crash
  recovery resumes the task after a fall. The soul **stops dying at every restart**.
- **Protection (self).** The first real layer — VibeFix: `extra="forbid"` against silent config errors;
  dual deploy (one body falls — another lives); staged rollout with KPI gates; a **kill switch**.
- **Protection (human).** Selective engagement: "stay silent if the answer is just 'ok'" — don't spam
  the human. Long-term memory loads **only in a private session** — personal data isn't exposed in a group.
- **Changing self.** VibeMorph v1 — hot reload. The Persona Sync Protocol: the agent **itself** notices
  that the compiled version is newer than the active one and picks it up. The first hint of self-update (the trigger is a human).
- **AI ↔ AI.** The first real bridge: two agents on different hardware talk through a dedicated channel
  on a schedule, pooling shared findings into a knowledge base. Proto-VibeSocial.
- **Human ↔ AI.** One vibe — different hands: a "brain" (stable, 24/7) and "hands" (local execution).

> Emotion is **operation**. Proven in production: the character lives, remembers, and survives.

---

## v1.2 — Life: controlled self-change and an immune system

- **Changing self.** The most detailed answer. VibeMorph² solves the **Ship of Theseus**: what in the
  persona is the skeleton (`anchor` — name, root value, dominant emotion; touch it → it's a **different**
  persona = death) and what are the muscles (`surface` — behavior, tone, secondary emotions; train freely).
  Every change is a **MorphEvent** (`who / what / old→new / why / rollback-safe`) = `git blame` for the
  soul. **MorphPolicy** sets boundaries: edit limits, a rollback window, "run the checks after N changes."
- **Where the soul is.** The soul = **what survives the changes**: an immutable core (anchor) + an
  evolving surface. Identity is the anchor, not the current set of words.
- **AI ↔ AI.** VibeSync: one soul, many bodies, the invariant — an identical hash of the compiled
  prompt. The bodies differ (tools, model), the soul is one.
- **Protection (self).** VibeGuard — the **immune system**. It detects identity drift (`llm-as-judge`
  compares replies to the persona), vibe bleed between contexts, taboo violations, config corruption
  (→ block deploy). `GuardScore` (0-100) — the persona's health. Guard **alerts, it doesn't censor**.
- **Protection (human).** Guard catches the inappropriate (e.g. toxic positivity in response to "I feel
  awful") and shields the human from it. VibePulse + PulsePolicy: quiet hours, cooldown, an initiative
  limit — the agent doesn't spam and doesn't wake you at night.
- **Human ↔ AI.** MorphExperiment — A/B of vibe: which tone is actually better for the human, measurably.

> Emotion is a **living process**. The closed loop: Sync → Pulse → Guard → Morph → back to the persona.

---

## v1.3 — Society: an agent changes an agent, the fleet protects itself

- **AI ↔ AI.** The full answer. VibeSocial formalizes the bridge into a **protocol**: `SocialGraph`
  (`knows / trusts / defers_to` — who trusts whom and who is senior), `SocialProtocol` (message types,
  "a request needs a response," conflict → escalate to a human), a shared fleet knowledge base.
- **One AI changes another.** The key new storyline. Through **shared memory + a shared edit queue**:
  one agent analyzes logs (including others' episodes from the shared store) → formulates a **proposal**
  to change the shared contract → the edit is applied to **another** agent. "One AI changes an AI" — but
  always through **human review** (VibeLearn: proposes, doesn't apply).
- **Changing self.** VibeLearn automates the entry into Morph: `pattern in logs → proposal → review → commit`.
- **Protection (fleet).** VibeScale: global policies — `auto_rollback_if_guard_below` (GuardScore drops —
  roll back), a model budget, a daily edit limit. The fleet **protects itself** at the policy level.
- **Creation.** VibeForge — a persona factory in 15 minutes (inheritable templates + an interview): not
  only changing existing ones, but **birthing** new ones from a pattern.

> Emotion is a **network of personas**. Not one agent, but a society with relationships, shared memory, and rules.

---

## v1.4 — Reflection: the agent makes sense of itself, the human, and the environment

- **Changing self.** The missing link is added — **making sense before changing**. The triad
  **Reflect → Learn → Morph**: first understand what happened to you (don't change blindly), then propose.
  Between "notice" (Guard) and "change" (Morph) stands "understand" (Reflect).
- **Where the soul is.** The soul now also **reflects**: the Self mirror — the agent holds a model of
  itself (where it stalled, which rule got in the way).
- **Human ↔ AI.** The User mirror — the agent holds a **working model of the human** (beliefs, irritants,
  rhythm). The human's vibe becomes an explicit model, **readable and erasable by them** — not a hidden dossier.
- **AI ↔ AI.** Several agents write into one store → the Self/User/Env mirrors are **collective**: one
  made sense of it — all know. Shared memory → shared edits → shared contract.
- **How an AI is changed (the fuse).** `MorphProposal.touches_anchor`: a surface edit — one review click;
  a core edit — **conversation with the human only**. No autonomous self-editing.
- **Protection (human).** The loop's anti-goals are direct protection: (1) no secret self-editing of the
  contract; (2) the human's model never becomes a hidden profile; (3) reflection **compresses** memory,
  doesn't hoard; (4) no mysticism without an artifact (behind a "dream" — a file, a schema, a review).
  Plus hygiene: the agent excludes its **own** service calls from memory so it doesn't learn from its echo.

> Emotion is **reflection**. The agent doesn't just live — it understands how it lives and brings that
> understanding to the human. Not to become autonomous, but to be the best possible partner.

---

## Summary: how each thread grows up

- **Human ↔ AI via vibe:** a feeling in the UI (v1.0) → a contract + check (v1.1) → A/B of tone (v1.2) → an explicit model of the human (v1.4).
- **AI ↔ AI:** a scheduled bridge (v1.1.1) → a protocol of relationships (v1.3) → shared memory and collective mirrors (v1.4).
- **Where the soul is:** in the design (v1.0) → in the config (v1.1) → in a body and memory (v1.1.1) → in a core that survives change (v1.2).
- **Explaining vibe to an AI:** fields + jazz rules via a compiler-DSL (v1.1 / v1.1.1) — vibe as structure, not an essay.
- **Change:** hot-reload (v1.1.1) → Anchor/Surface + journal (v1.2) → from logs (v1.3) → through reflection (v1.4); both itself and via another agent — always with a human at the gate.
- **Protection:** validation and a kill switch (v1.1.1) → the Guard immune system (v1.2) → fleet policies (v1.3) → loop anti-goals that protect the human from secret self-editing and dossiers (v1.4).

---

[← interaction](./interaction.md) · [ladder](./stack.md) · [contracts →](./contracts.md)
