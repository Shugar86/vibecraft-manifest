---
title: VibeCraft — Contracts
lang: en
version: 1.4
layer: engineering
---

# Contracts

🌐 [Русский](../ru/contracts.md) · **English** · [← overview](../../README.en.md)

> The formal schemas behind the words "soul," "evolution," "reflection." Each is data with validation, a
> status, and (where needed) a human at the gate. Machine-readable versions — in [`../../schemas/`](../../schemas).

---

## 1. Persona — the soul as data

```yaml
name: "<identifier>"
vibe:                       # static: who you are
  role: "..."
  voice: "..."
  core_emotions: [...]
  values: [...]
  taboos: [...]
behavior:                   # dynamic: jazz rules (scenarios, not if/else)
  on_tool_success: "..."
  on_tool_no_results: "..."
  on_tool_error: "..."
  on_offtopic: "..."
tools: [ { name, type, description, router_examples } ]
```

Validated by Pydantic with `extra="forbid"`: a typo in a field name = a load error, not a silently
wrong bot. The `PromptCompiler` assembles the system prompt from this for the execution context.
Schema: [`persona.schema.json`](../../schemas/persona.schema.json).

---

## 2. Anchor / Surface — the evolution contract

Identity is held by an **anchor**. Not everything in a persona can be changed equally.

| | Anchor (core / skeleton) | Surface (muscles) |
|---|---|---|
| **What** | name, root value, dominant emotion; (for a dev agent — language, base principles, "never commit secrets") | behavior, tone, secondary emotions/taboos, formats, integrations |
| **To touch = ** | create a **different** persona (death of the former) | evolution of the same persona |
| **How to change** | **conversation only** with the human | proposal → review → commit |
| **Marker** | `touches_anchor: true` | `touches_anchor: false` |

The rule: reflection may propose anything, but the Anchor is untouchable without dialogue. This is the
immunity against "break yourself with one prompt."

---

## 3. MorphEvent — an atomic change (`git blame` for the soul)

```yaml
morph_event:
  id: "morph-2026-02-19-001"
  timestamp: "2026-02-19T15:00:00+03:00"
  author: "human"          # human | agent | system
  type: "behavior"         # anchor | surface | behavior | tool | value | emotion | taboo
  field: "behavior.on_offtopic"
  old_value: "..."
  new_value: "..."
  reason: "why this change is needed"
  rollback_safe: true
```

Without MorphEvent, six months on no one knows *who and why* changed the persona. The journal of all
events is `MorphHistory`. Schema: [`morph-event.schema.json`](../../schemas/morph-event.schema.json).

---

## 4. MorphProposal — a change proposal (VibeLearn's output)

A hypothesis, not a command: the agent brings a reasoned diff and waits.

```yaml
morph_proposal:
  id: "2026-06-14_001a"
  target: "<file/section of the contract>"
  change: "a human-readable description of the edit"
  evidence: ["session:…", "reflection_pass:…"]   # what it's based on
  touches_anchor: false                           # true → conversation required
  status: pending                                 # pending | approved | rejected | modified
```

**Review rule:** only a **human** applies the edit. `touches_anchor: false` — approve/reject/modify in
one action; `touches_anchor: true` — first a conversation with the human, a click is not enough.
Schema: [`morph-proposal.schema.json`](../../schemas/morph-proposal.schema.json).

---

## 5. ReflectionPass — one "dream"

```yaml
reflection_pass:
  id: "2026-06-14_001"
  window: "last_7d"          # the window of memory/sessions examined
  mirrors:
    self: [...]              # how I worked
    user: [...]              # a working model of the human (not a dossier)
    env:  [...]              # a map of the environment
  consolidated: 3            # how many episodes were compressed (metric: memory grows sublinearly)
  proposals: ["2026-06-14_001a"]
```

Invariant: if `consolidated` doesn't grow while memory swells — reflection is **broken**. A "dream" must compress.

---

## 6. Loop invariants (anti-goals)

The contract holds only while all four are true:

1. **No autonomous self-editing.** Changing the contract — only through a human; the Anchor — conversation only.
2. **No dossier.** The User mirror is a working model the human can read and erase, not a hidden profile.
3. **Reflection compresses.** Success means memory does not grow linearly.
4. **No mysticism without an artifact.** Behind a "dream" and a "soul" — a file, a schema, a review. No artifact → it's noise.

---

[← context: interaction](./interaction.md) · [threads by version](./threads.md) · [machine-readable schemas →](../../schemas)
