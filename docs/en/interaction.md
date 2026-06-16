---
title: VibeCraft — How Agents Interact
lang: en
version: 1.4
layer: philosophy + engineering
---

# How agents interact

🌐 [Русский](../ru/interaction.md) · **English** · [← overview](../../README.en.md)

> The manifesto is not about the lonely persona but about **interaction**. Three storylines: one soul
> in many bodies, shared memory and shared edits, the self-learning loop. Schemas — in [`contracts.md`](./contracts.md).

---

## One soul, many bodies

The same agent lives in Telegram, on the web, in a CLI, via API — with different tools and even
different models. The question: how do you guarantee it's **one** agent, not three different bots in one skin?

**The answer is the identity invariant.** All bodies assemble the persona from one source of truth (`persona.yaml`):

```
            persona.yaml  (source of truth)
                  │
        ┌─────────┼─────────┐
     body A     body B     body C
   (Telegram)    (API)      (CLI)
   tools: …     tools: …   tools: …
   model: A     model: B   model: A
        └──────── shared memory ──────┘
```

- **SyncManifest** splits artifacts into **shared** (identity + long-term memory) and
  **instance-specific** (current task, background tasks, the body's tools).
- **SyncIdentity** — a formal guarantee: the `sha256` of the compiled prompt matches across all bodies.
  If the hash diverges, the bodies have drifted apart.
- **SyncAdapter** adapts only the **form** to the platform (Telegram has no tables → lists; API has no
  length limit), without touching the substance.

**Anti-goal:** the current task (`STATE`) is **not** synced — each body has its own. This is file
synchronization, not a distributed DB: simplicity over scale.

---

## Shared memory, shared edits

The most important storyline. Agent sociality is **not chit-chat but a shared substrate**. Two (or
more) agents interact by **sharing one memory and one queue of edits**.

```
agent-1 ─┐                              ┌─→ edit proposal ─┐
         ├─→  shared memory store  ─→ reflection          ├─→ human review → contract edit
agent-2 ─┘     (one vault)              └─→ edit proposal ─┘          │
   │                                                                  │
   └──────────────────── shared contract (one set of rules) ←─────────┘
```

- **Shared memory.** On session end, agents drop an episode into one store. One substrate for the
  fleet — not each with its own amnesia, but **collective** Self / User / Env models.
- **Shared edit queue.** Reflection over the shared memory yields **proposals** to change the shared
  contract. An agent that hit friction in one environment proposes an edit that another agent applies
  tomorrow. The edit is shared because the **contract is shared**.
- **The boundary (tenant isolation).** Shared memory about the user — yes; one product's vibe leaking
  into another — no (config > code). And: an agent must exclude its **own** service calls from memory,
  or it learns from its own echo.

> This is "two agents share memory and propose edits": VibeSocial without a chat, through a shared
> vault and a shared contract. Direct chit-chat (a dedicated channel between agents) is a separate,
> noisier mechanism; the shared substrate is quieter and more useful.

---

## The self-learning loop

Reflect → Learn → Morph. Understand → propose → change. This is what turns "many agents with shared
memory" into **a system that improves itself**.

```
   session episodes  +  semantic memory
            │
            ▼   VibeReflect  (a "dream": read and synthesize, no outward action)
   Self / User / Env models  +  consolidation (compress, don't hoard)
            │
            ▼   VibeLearn
   MorphProposal[]  (status: pending)
            │
            ▼   human review   (approve / reject / modify)
            │
            ▼   VibeMorph
   contract edit  +  memory update
```

**VibeReflect's three mirrors:**

1. **Self** — how I worked: where I stalled, what I did three times over, which rule got in the way, which saved me.
2. **User** — a working model of the user (not a dossier): beliefs, irritants, rhythm. Readable and erasable by them.
3. **Env** — a map of the environment: where things live, where not to play, what "hurts."

**"Dreams" — offline consolidation.** A human consolidates memory in sleep: the day's episodes →
durable links. An agent needs the same — a scheduled pass (idle / on a timer) that **compresses** the
particular into the general and links memories, doing nothing to the world. Success metric: memory
grows **sublinearly**. If reflection only adds — it's broken.

**Human in the loop.** Learn **proposes**, the human **decides**, Morph **applies**. The core (Anchor)
changes only through conversation, not a click. A proposal touching the core by definition requires dialogue.

> This is "an analog of an ML model, but for the soul" — yet with a human in the loop and reflection at
> the input, not a blind gradient. Full `ReflectionPass` and `MorphProposal` schemas — in [`contracts.md`](./contracts.md).

---

[← ladder](./stack.md) · [contracts →](./contracts.md) · [manifesto →](./manifesto.md)
