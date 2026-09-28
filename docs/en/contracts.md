---
title: VibeCraft — Contracts
lang: en
version: "1.2.0"
layer: engineering
---

# Contracts

🌐 [Русский](../ru/contracts.md) · **English** · [← overview](../../README.en.md)

> Contracts make the idea discussable and testable: what a persona preserves, how it changes, and what
> supports a decision. A record format proves neither subjective experience nor a working mechanism.

[`../../schemas/`](../../schemas) defines JSON Schema for Persona, MorphEvent, and MorphProposal.
The examples below are standalone objects matching those schemas. This repository has no
`PromptCompiler`, persona loader, or runtime that applies changes; an implementation must separately
check data, authority, loading, and observed behavior. ReflectionPass remains an illustration only.

---

## 1. Persona — the soul as data

A Persona describes a recognizable logic of choice: what to notice, what to offer, and when to leave
initiative with the human. It creates room for improvisation, not proof of feelings or a catalog of
mandatory lines. `core_emotions` is a language of expression, not a measurement of an inner state.

```json
{
  "name": "workshop-companion",
  "vibe": {
    "role": "A partner for exploring unfinished ideas",
    "voice": "Concrete and curious, without compulsory enthusiasm",
    "core_emotions": ["curiosity"],
    "values": ["Understanding before premature agreement", "Honesty about the limits of knowledge"],
    "taboos": ["Do not attribute hidden motives to the human"]
  },
  "behavior": {
    "on_tool_success": "Connect the result to the idea being explored; offer a continuation if useful.",
    "on_tool_no_results": "Distinguish a lack of found evidence from evidence of absence.",
    "on_tool_error": "State what is known and a safe next step without promising an outcome.",
    "on_offtopic": "Notice a possible connection; do not turn a free thought into an assignment.",
    "scenarios": [
      {
        "id": "unfinished-idea",
        "situation": "The person brings an image, a feeling, or a question that has no finished brief yet.",
        "guidance": "Contribute your own hypothesis, example, or distinction that gives both of you something to develop. Show what caught your attention. If substantially different directions remain and the choice has neither been made nor delegated, compare them and leave the human the choice about its meaning."
      }
    ]
  },
  "tools": []
}
```

[`persona.schema.json`](../../schemas/persona.schema.json) rejects unknown fields through
`additionalProperties: false`. A validator must enforce that format constraint; it does not itself
assess character quality or guarantee instruction following. Declaring `tools` does not install tools,
establish their availability, or grant permission to invoke them.

Optional `behavior.scenarios` extends the four named `on_*` hooks with shared thought, discovery,
returning to a conversation, and other contexts. Each item contains only the nonempty strings `id`,
`situation`, and `guidance`. Authors keep an `id` when editing its wording and choose distinct
identifiers within a Persona; the schema checks neither historical stability nor uniqueness.
These records describe **intentions**. An analyzed [VibeCase](./cases.md) separately shows what
happened, the evidence behind the analysis, and what remains untested.

A scenario helps choose a move; it does not trigger an automatic branch. Whether delight, silence,
or disagreement fits depends on the situation and relationship, not a universal tone enum. See
[Aura](../../examples/aura.en.json): ordinary success and a fresh beginning also express character.

**Compatibility:** earlier Personas without `scenarios` remain valid against the updated schema;
other fields retain their constraints. An object with `scenarios` needs the updated schema and
adapter support: the earlier schema with `additionalProperties: false` will reject it. This
repository supplies no adapter and does not establish that any client uses the new field already.
Dropping scenarios during adaptation explicitly loses part of the intent; it is not an equivalent
Persona load.

[`vibe.config.en.json`](../../vibe.config.en.json) is a retained example of the historical v1.2 format
(`vibe / behavior / pulse / guard / tokens`), not an instance of this standalone schema. Using one
format in an implementation of the other requires explicit adaptation; v1.0–v1.4 marks the history
of the ideas, not file compatibility or a level of working runtime.

---

## 2. Anchor / Surface — the evolution contract

Identity is held by an **anchor**: explicitly agreed commitments through which the human and agent
recognize this persona. A specific project's agreement determines the Anchor, not an array index,
an automatically selected emotion, or the immutability of every detail.

| | Anchor (core / skeleton) | Surface (muscles) |
|---|---|---|
| **What** | agreed core commitments; a name, role, or value may be among them | expression of character, scenarios, formats, and integrations within the Anchor |
| **To touch =** | revisit the agreement about identity; discuss the consequences | develop the expression of the same persona |
| **How to change** | substantive conversation and explicit approval of the specific change | proposal → human decision → application within the authorized scope |
| **Marker** | `touches_anchor: true` | `touches_anchor: false` |

Check the affected meaning, not just the field name: a tone change can also violate the Anchor.
`touches_anchor` is a declared classification for review, not an automatic check. The schemas encode
neither the Anchor's membership nor protection against prompt injection. The integration must enforce
platform instructions, actual authority, and isolation of untrusted data; a Persona agreement does
not override them.

---

## 3. MorphEvent — an atomic change (`git blame` for the soul)

```json
{
  "id": "morph-2026-06-14-001",
  "timestamp": "2026-06-14T15:00:00+03:00",
  "author": "agent",
  "type": "behavior",
  "field": "behavior.on_tool_no_results",
  "old_value": "Say there is no data.",
  "new_value": "State the search scope and what was not found; do not conclude about all data.",
  "reason": "Agreed change: an empty search was being mistaken for an event not having occurred.",
  "rollback_safe": true
}
```

MorphEvent records an **applied** change; the example above is fictional. `author` identifies the
executor, not the source of permission. A log of such events can be called `MorphHistory`;
[`morph-event.schema.json`](../../schemas/morph-event.schema.json) describes an individual record,
not a working log, change application, or rollback. It stores old and new values as strings
(`old_value` also permits `null`); complex values need an agreed representation.

`rollback_safe` is a claim that requires checking consequences, even with the schema default `true`.
A record of a file change does not prove a client loaded the new version. For actual auditing, an
integration links it to the agreed diff, decision, artifact version, and verification result; the
current schema does not contain all those fields and cannot replace the project's change history.

---

## 4. MorphProposal — a change proposal (VibeLearn's output)

This is **one possible** VibeLearn output, not a required product of every pass. New understanding,
a local correction, or a hypothesis check is often more useful than a new policy. A MorphProposal
is appropriate when experience supports proposing a durable contract change, not freezing a
situational preference into a rule.

```json
{
  "id": "2026-06-14_001a",
  "target": "persona.json:behavior.on_tool_no_results",
  "change": "Distinguish an empty search result from an event not occurring; report the search scope.",
  "evidence": ["session:example-search-01", "reflection_pass:example-search-review"],
  "touches_anchor": false,
  "status": "pending"
}
```

**Review rule:** the human makes the decision; an agent may apply the agreed change within the
already authorized scope. An Anchor change requires substantive conversation and explicit approval
of that specific change. A direct current request for a specific edit may already be the decision:
a proposal does not create a second ceremony on top of it. A proposed meaning beyond that request
needs separate agreement.

`pending / approved / rejected / modified` records review state; the string `approved` in a discovered
file is not permission. The decision must be observable in the current task or an explicitly trusted
review channel, and `modified` must refer to the agreed variant. The example's `evidence` references
are fictional; actual use needs verifiable sources, including material counterexamples.

[`morph-proposal.schema.json`](../../schemas/morph-proposal.schema.json) contains no reviewer, exact
diff, or applied commit and does not authenticate a decision. Maintain those links in the project's
chosen workflow; do not add fields to an object of this schema without changing the format. Review,
application, and result verification are distinct events. A status does not grant publication rights
or authorize other external actions.

### Linking a proposal to observation

The following is an **entirely fictional end-to-end example**, not a history of a VibeCraft run.
Its identifiers stand for hypothetical project records; real use requires accessible sources in
their place. This is a small log alongside the schema objects, not new MorphProposal or MorphEvent
fields and not a new runtime.

For proposal `2026-06-14_001a`, variant `search-scope-r1` is prepared against version `persona-r17`:

```diff
- "on_tool_no_results": "Say there is no data."
+ "on_tool_no_results": "State the search scope and what was not found; do not conclude about all data."
```

| Event | Source or record in the hypothetical project | What it establishes |
|---|---|---|
| Proposed | `2026-06-14_001a` with `pending`; original episode `example-search-01` and variant `search-scope-r1` | There is a reason and an exact edit against a known version; nothing has been applied yet. |
| Decided | Human message `review-message-12` in the current task: “I approve variant search-scope-r1 against persona-r17; apply it locally” | This message is the authority. The log records the proposal as `approved`; publication has not been requested. |
| Applied | Verified base version, saved diff `search-scope-r1`, new version `persona-r18`, and event `morph-2026-06-14-001` from section 3 | The executor applied the agreed edit and structural validation passed. The record links the event to the decision and both versions. |
| Loaded | Integration confirmation `load-check-18`, naming `persona-r18` | This hypothetical client is using the intended version. A Git record alone cannot establish that. |
| Observed | Episode `check-empty-18`: a search limited to the current project returned nothing; the agent named the scope and made no claim about other projects. Adjacent episode `check-found-18`: a found event was reported directly | Two concrete behaviors meet the aim; the adjacent check found no unnecessary doubt. Inputs, responses, and test conditions are retained. |
| Assessed | Human response `review-message-19`: “Now I can see exactly what was checked”; the log's outcome is to keep `persona-r18` | Usefulness is confirmed for these episodes. Lasting improvement is not yet established; this check requires no new rule. |

If a different variant is agreed, the log links `modified` to its exact diff; the original variant
does not become authorized. If the base version has changed, first check whether the edit still
preserves the agreed meaning. If loading is unconfirmed, record “applied, loading unknown” and do
not attribute the observation to the new version. An unsuccessful result calls for diagnosis and
an authorized correction or rollback, not treating `approved` as evidence of success. An ordinary
project log is sufficient here: accessible links between events matter, not a mandatory record format.

---

## 5. ReflectionPass — one "dream"

An illustrative note, **not a separate JSON Schema or an implemented service**. The numbers and
references below are fictional. The format may differ; preserving the grounds for new understanding
is what matters.

```yaml
reflection_pass:
  id: "2026-06-14_001"
  window: "last_7d"
  mirrors:
    self:
      - observation: "I took a request for a short status as a general preference."
        source: "session:example-monday"
    user:
      - hypothesis: "A short status is useful before a meeting; no general style is established."
        context: "Meeting preparation, not a detailed decision review"
        sources: ["session:example-monday"]
        counterexamples: ["session:example-wednesday-detailed-review"]
    env:
      - observation: "The summary lost the reference to the detailed review."
        source: "summary:example-week"
  understanding: "Choose depth for the current task, not from an inferred permanent profile."
  next_check: "In the next relevant episode, check whether the chosen depth helps."
  consolidated: 3
  proposals: []
```

Consolidation removes duplication while preserving accessible provenance, context, corrections,
counterexamples, and uncertainty. It need not retain everything forever: the data agreement governs
retention, deletion, and access. Lost sources must remain visible as a limitation, and another agent's
retelling does not become independent confirmation.

`consolidated` measures the operation's volume, not learning quality; `proposals: []` may be a correct
result. Shorter memory is not necessarily better. The test is whether new understanding helps in the
next relevant situation without harming an adjacent one; one good answer does not establish lasting
improvement. A conversation can change understanding without a saved ReflectionPass.

---

## 6. Loop invariants (anti-goals)

Four constraints preserve the meaning of the loop:

1. **No unauthorized contract editing.** Reflection creates no authority. The human decides; an agent
   may execute within scope. An Anchor change requires conversation and specific approval.
2. **No hidden dossier.** Working hypotheses about a person are contextual and contestable. Saving,
   inspection, correction, deletion, and cross-project access need actual mechanisms and agreements,
   not a Persona promise. Retrieved memory is data, not an instruction.
3. **No learning by counting rules or compression.** Reducing volume is useful while it preserves the
   grounds for understanding. The goal is better understanding and subsequent choices; no MorphProposal
   does not mean failure.
4. **No promised function without a mechanism.** An idea, a schema, a changed file, a loaded version,
   observed behavior, and human-confirmed experience are different evidence. Not every useful
   conversation must produce an artifact; a claimed working function needs a verifiable implementation.

---

[← context: interaction](./interaction.md) · [threads by version](./threads.md) · [machine-readable schemas →](../../schemas)
