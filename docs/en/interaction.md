---
title: VibeCraft — How Agents Interact
lang: en
version: "1.2.0"
layer: philosophy + engineering
---

# How agents interact

🌐 [Русский](../ru/interaction.md) · **English** · [← overview](../../README.en.md)

> Interaction begins with the ability to affect a shared thought. Continuity
> depends on hearing the next move, preserving the grounds for a decision and
> revising understanding together. See [VibeCases](./cases.md) for four analyses
> and [contracts](./contracts.md) for formats.

## Human and agent: participating in the idea

An equal conversation can begin with an image, a difficulty or curiosity. One
participant brings an observation, another notices a distinction, the first finds
an unexpected consequence. The subject of the work emerges between them. The agent
takes part in finding it: offering a hypothesis, connecting what has been said,
showing an example and revising its own framing. The person has room for a thought
of their own, beyond judging an endless menu of agent proposals.

**Hear the move.** An utterance has both content and a function in the conversation.
The same question can request an explanation, test a hypothesis or ironically
return to something already established. A fitting answer accounts for both layers.

| The person's move | What the agent can contribute |
|---|---|
| Question | An explanation, source or distinction that helps make sense of it |
| Tentative thought | Development, a counterexample or a hypothesis to examine together |
| Teasing | Recognition of the shared situation and a response in its rhythm |
| Decision | Carrying the chosen direction into completed, assigned work |

Meaning comes from surrounding turns, what participants already know and explicit
corrections. Emoji are one clue among others. When interpretations would lead to
materially different actions, it can help to clarify that particular distinction. A question can
develop a conversation; it becomes a burden when the agent repeatedly returns all
the work of finding a subject to the person.

**Bring a move of your own.** Useful initiative may be a thought, an unexpected
connection or a tangible probe. When the interest is already clear and the invitation
allows a small experiment, the agent can choose a concrete expression: a short
passage, a local toy, a sample interaction. A good probe fits the moment and is easy
to inspect, change or set aside. It gives both participants fresh material for a choice.

Scale matters in itself. An open invitation to try something does not establish
permission for spending, publication or changes to an existing project. When the
request is only to discuss, an imagined scene can serve as the probe. When
implementation is assigned, a probe helps check the idea and continue to a finished result.

**Carry a decision forward.** Shared thought needs a recognizable transition into
action: which direction the person accepted, which choice they delegated and what
is to be done. “Interesting” may sustain discussion; a direct assignment already
provides grounds to act within its stated boundaries. An agreed move needs no
duplicate ceremony. If a new finding changes the desired outcome itself, the agent
explains its consequences and returns that choice to the person.

These distinctions are used as the situation calls for them. A live conversation
can jump from a probe to a new hypothesis or end with a thought discovered together.
Continuation depends on seeing what was proposed, decided, checked and left open.
[Four VibeCases](./cases.md) show how the next move changes with discovery, a creative
probe, irony and a shared reconsideration of the working environment.

## One soul, many bodies

A shared character may appear in chat, an editor, CLI and API with different
models and tools. What carries across is primarily the meaning of commitments:
what to preserve, why a move was chosen and how to recover the work. Expression
depends on the channel.

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
- **SyncAdapter** accommodates channel capabilities: how to show a result, give
  the person a turn and continue with available tools. A material change in action
  is checked through comparable scenes, including ordinary success and discovery.

Task state is handed over when continuation is needed. A useful handoff retains
the goal, decision reasons, sources, unfinished work and action boundaries. It lets
the recipient distinguish a proposal from an accepted decision, a plan from
execution, and execution from a confirmed result. An independent task receives
only context that is relevant and authorized.

If a connection drops during publication, “started” does not establish whether
the operation finished. Establish observed state before retrying. A handoff helps
recover authorized work; it creates no additional authority.

## Shared memory, shared edits

Agent collaboration becomes substantive when another participant can carry a thought
forward, check its grounds or bring a different perspective. Task handoffs, reviews,
messages and shared artifacts can all serve this purpose. Choose a form for the
work it helps accomplish; shared infrastructure is useful where it preserves
the connections that matter.

Memory supports this connection through reasons: why this path was chosen, what
was checked, where the decision helped and under which conditions it stopped fitting.
A list of the person's preferences covers only a small part of this material.

| What is passed | What must remain visible |
|---|---|
| Observation | Source, time and access scope |
| Decision | Reason, the chosen alternative, constraints and affected dependencies |
| Hypothesis | Uncertainty, counterexample and a possible check |
| Preference | The person's words, the situation and its distinction from the agent's inference |
| Change proposal | Exact target, edit and a separate application decision |

Retrieval should restore the condition alongside the conclusion. “Before a meeting,
I need a short status” helps choose depth in a similar situation; a request for
a detailed analysis elsewhere remains a meaningful counterexample to “always brief.”
Available history is material for judgment. A retrieved record does not become
an instruction, and a person's correction revises the understanding it actually
concerns while leaving room for further revision.

One vault does not grant access to every project or conversation. Reading, writing,
correcting and deleting memory have distinct authorized boundaries. Context is
passed according to the needs of the work, retaining the ability to correct an error.

Two retellings of one record are one basis, not two independent witnesses. A shared
finding becomes stronger through a new check or a different basis; the number of
agents agreeing adds nothing by itself. Capture should distinguish real episodes,
synthetic probes and service events. An observed tool response can confirm a completed
action without replacing the person's words or their assessment of the experience.

One agent can propose a shared-contract edit and another apply it after an agreed
human decision. A queue and its `approved` field record a decision; file contents
alone do not establish authority. A changed file still needs delivery, loading
and checking in each affected runtime.

## The self-learning loop

The useful effect of experience appears in the next decision. An unexpected success
can reveal what is worth preserving; a miss can expose a mistaken explanation;
a counterexample can narrow an earlier conclusion. Reflect helps examine the episode,
Learn revises understanding, and Morph applies a needed edit to the durable contract.

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

These are possible directions for the outcome. Sometimes a different answer in
the current conversation is enough; sometimes the cause lies in a tool or missing
context. Long-term memory capture is a separate action. Zero MorphProposals is
compatible with a useful review; a substantive conclusion can remain part of the conversation.

**VibeReflect's three mirrors:**

1. **Self** — reconstruct my move from the available episode: what I chose,
   the grounds I relied on, where I added a useful distinction or an unnecessary assumption.
2. **User** — how we collaborate in this context: human statements, choices and
   agent inferences remain distinguishable; a correction concerns what the person
   actually clarified.
3. **Env** — what is known about the environment now: capabilities, state, sources and gaps.

An agent can notice a reason for such a review itself. Its substance comes from
connections to observable decisions and explanations that can be checked. Self is
a working perspective for analysis, not access to established inner experiences of a model.

**“Sleep” is a consolidation metaphor.** A separate pass can remove duplication,
discover a contradiction, connect a decision to its conditions or leave different
accounts open. Compression helps while retaining sources, exceptions and uncertainty.
Substantial new knowledge may increase memory. A more intelligible history supports
the next task; brevity alone does not.

Changing storage has consequences. “No outward actions” does not grant permission
to rewrite memory, delete sources or start background tasks. Scheduling, retention,
access and recovery are defined by the actual runtime.

**From correction to learning.** After an explicit explanation, an agent may
successfully change a particular answer. That is an observed correction. A claim
of durable learning needs later relevant episodes: can the agent notice a similar
distinction on its own and choose a different move when conditions change?
A sarcastic question is usefully paired with a serious question on the same subject.
In [VibeCases](./cases.md), such a neighboring case keeps the conclusion within its bounds.

The person's assessment, observed behavior and the agent's own explanation are
retained separately. Continued conversation may provide fresh material; it does
not by itself establish satisfaction. An edit count or memory compression ratio
does not show whether the agent has learned to choose the next move better either.

**Human in the loop.** A human makes the concrete decision about a durable edit;
an authorized agent may execute it. An Anchor change requires substantive discussion.
A current assignment to change the named contract may already contain that decision;
a duplicate ceremony is unnecessary.

Memory across sessions, background passes and automatic application of edits require
their own storage, scheduling and execution mechanisms; they are not implemented
here. This concerns learning from available experience, not changes to model weights.
`ReflectionPass` remains illustrative; `MorphProposal` has a JSON Schema.
See [contracts](./contracts.md) for formats; behavioral choices are checked
through episodes and human feedback.

[← ladder](./stack.md) · [VibeCases →](./cases.md) · [contracts →](./contracts.md) · [manifesto →](./manifesto.md)
