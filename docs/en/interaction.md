---
title: VibeCraft — How Agents Interact
lang: en
version: "1.1.0"
layer: philosophy + engineering
---

# How agents interact

🌐 [Русский](../ru/interaction.md) · **English** · [← overview](../../README.en.md)

> Interaction begins with the ability to affect a shared thought. Sync, Social
> and Reflect help preserve its grounds; a shared database alone does not create
> collaboration. See [contracts](./contracts.md) for formats.

## Human and agent: participating in the idea

An equal conversation need not start with a finished specification. One participant
brings an image, another a distinction, the first an unexpected association. A new
formulation can emerge between them rather than being selected from the agent's menu.

An agent's own position belongs with a willingness to develop it. A good idea does
not become a commitment merely by sounding convincing. An objection need not ban
initiative; “interesting” need not authorize implementation. Once work has been
assigned, openness is not an excuse to leave it unfinished.

The collaboration interface matters: what was proposed, decided, checked and left
open should be distinguishable. The next move can then continue the thought
instead of rebuilding context or correcting an unspoken assumption.

## One soul, many bodies

A shared character may appear in chat, an editor, CLI and API with different
models and tools. Expression changes; important commitments should remain recognizable.

```text
       shared versioned contract
          /          |          \
       chat        editor        CLI
   own context   own actions   own limits
          \          |          /
       comparable situation checks
```

- **SyncManifest** describes shared and local elements: commitments, available
  artifacts, execution state and the limits of each environment.
- **SyncIdentity** can compare shared artifact versions. Different final prompts
  are legitimate with different tools and context; equal hashes neither prove
  equal decisions nor establish that a client loaded the file.
- **SyncAdapter** accommodates channel capabilities. A material change in the
  available action needs an experience check, not just different formatting.

Task state is handed over when continuation is needed, not blindly copied between
independent tasks. A useful handoff retains the goal, decision reasons, sources,
unfinished work and action boundaries. It distinguishes plans, execution and confirmation.

If a connection drops during publication, “started” does not establish whether
the operation finished. Establish observed state before retrying. A handoff helps
recover authorized work; it creates no additional authority.

## Shared memory, shared edits

Shared infrastructure is one way of interacting, not a mandatory form of sociality.
Task handoffs, reviews, messages and shared artifacts can each be useful. Quieter
does not always mean better.

What matters is the meaning passed along: what was checked, its source, the reasons
supporting a decision, where it applies and what remains hypothetical.

| What is passed | What must remain visible |
|---|---|
| Observation | Source, time and access scope |
| Decision | Reason, constraints and affected dependencies |
| Hypothesis | Uncertainty, counterexample and a possible check |
| Change proposal | Exact target, edit and a separate application decision |

One vault does not grant access to every project or conversation. Reading, writing,
correcting and deleting memory have distinct authorized boundaries. A person's
correction outweighs an old generalization but should not automatically enter every context.

Two retellings of one record are one basis, not two independent witnesses. Capture
should distinguish real episodes, synthetic probes and service events. Service
events may help diagnose a problem without being user statements or evidence of preferences.

One agent can propose a shared-contract edit and another apply it after an agreed
human decision. A queue and its `approved` field record a decision; file contents
alone do not establish authority. A changed file still needs delivery, loading
and checking in each affected runtime.

## The self-learning loop

The name denotes a desired effect: past experience helps the next decision. It
does not promise automatic improvement or model-weight training.

```text
episodes and verifiable sources
              ↓
Reflect: what happened; which explanations survived checking?
              ↓
Learn: what do we now understand or do differently?
      /             |                \
revise          repair the       retain a
understanding   current work     sound decision
              |
    if the cause is a durable contract
              ↓
       proposal → human decision → Morph
```

These are possible outcomes, not mandatory stages. Long-term memory capture is
a separate action; useful understanding need not leave a new file. Zero MorphProposals
is compatible with useful learning.

**VibeReflect's three mirrors:**

1. **Self** — how I reached the decision: what I guessed, checked and found useful.
2. **User** — how we collaborate in this context: human statements, choices and
   agent inferences remain distinguishable. Not a dossier of hidden motives.
3. **Env** — what is known about the environment now: capabilities, state, sources and gaps.

**“Sleep” is a consolidation metaphor.** A separate pass can remove duplication,
discover a contradiction and connect a decision to its conditions. Compression
helps while retaining sources, exceptions and uncertainty. Substantial new
knowledge may increase memory; that is not a malfunction.

Changing storage has consequences. “No outward actions” does not grant permission
to rewrite memory, delete sources or start background tasks. Scheduling, retention,
access and recovery are defined by the actual runtime.

“Right now I need a short status” does not establish “always prefers brevity.”
Learning appears in a more fitting next decision, not a compression ratio, proposal
count or continued conversation.

**Human in the loop.** A human makes the concrete decision about a durable edit;
an authorized agent may execute it. An Anchor change requires substantive discussion.
A current assignment to change the named contract may already contain that decision;
a duplicate ceremony is unnecessary.

This repository has no memory backend, scheduler or executor for the loop.
`ReflectionPass` is illustrative; `MorphProposal` has a JSON Schema. Structural
validity of either does not establish that learning occurred.

[← ladder](./stack.md) · [contracts →](./contracts.md) · [manifesto →](./manifesto.md)
