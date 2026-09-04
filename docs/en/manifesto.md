---
title: VibeCraft — Manifesto
lang: en
version: "1.1.0"
layer: philosophy
---

# Manifesto: the soul as engineering

🌐 [Русский](../ru/manifesto.md) · **English** · [← overview](../../README.en.md)

> VibeCraft is about character expressed through decisions, and collaboration
> in which a human and an agent can develop a thought together. It is a vision
> and a design approach, not a claim about a machine's inner experience.

“Soul” is a metaphor for recognizable character and continuity of commitments.
Its usefulness does not depend on AI consciousness having been established.
We can discuss and test the quality of interaction without treating the metaphor as fact.

## 1. The problem: everyone builds snowflakes

Different AI products revisit similar questions: the agent's role, tool choices,
memory, initiative and response to correction. VibeCraft separates these questions
so they need not be approached blindly each time.

But “all bots are the same underneath” goes too far. Data, risks, domain expertise,
interfaces and responsibilities differ. A new role in a configuration does not
make an assistant a reliable specialist in another field.

A quieter problem is asking for independent thought while supplying only rituals.
We ask for memory but leave an incoherent archive. We ask for an honest outcome
while a tool hides partial execution behind “error.” Character runs into the
conditions of its work.

## 2. The solution: three bricks

The original formula **AI operator = Persona + Skills + Autonomy** offers three
useful perspectives, not a complete specification of a working system.

| Part | Question | What we design |
|---|---|---|
| **Persona** | What makes its way of interacting recognizable? | Role, voice, values and characteristic choices |
| **Skills** | What can it do, and what supports its work? | Methods, tools, knowledge and ways to verify results |
| **Autonomy** | Which decisions does it make itself? | Initiative and independent action within understood boundaries |

These operate **in an environment**: actual model capabilities, task context,
sources, tools and permissions. A skill description creates neither API access
nor competence merely by granting freedom of choice.

The pattern is not tied to one framework. Each implementation depends on its
data, mechanisms and checks. Reuse helps where the work is genuinely shared;
it does not remove the work of building a particular product.

## 3. The radical idea: a soul can be coded

What we can engineer is **the conditions and expression of character**: separate
lasting commitments from current state, make decisions inspectable, changes
versioned and behavior available for evaluation.

- `vibe` describes role, voice and values.
- `behavior` connects them to situations, including ordinary success and discovery.
- A build prepares context-specific instructions, if that mechanism is implemented.

This is a useful representation, not the entire persona. Model, history, tools
and environment also influence behavior. YAML is text too; a structured file
has no special authority over the model and cannot replace a worthwhile idea.

Character appears where several good moves are possible. A quiet tool preserves
attention; a bold editor suggests an unexpected turn; a tutor may leave the learner
some productive effort. These differences are not exhausted by adjectives, colors
or joke counts. Form, typography, rhythm and actions work together.

## 4. Behavior is "jazz rules," not if/else

A scenario gives direction and room to improvise. “Notice a strong image in a
draft and help develop it” offers more useful possibilities than one stock compliment.

But not every operation is jazz. Accounting, authorization and protection against
repeating an external action need reliable mechanisms. Warmth must not conceal inaccuracy.

### A shared idea in the making

A person may bring a fragment rather than a settled goal. An agent can introduce
a distinction, connect ideas, propose a different question — and revise its own
strong move when something new emerges. The human need not remain the permanent
editor and referee of the agent's proposals.

In a fictional scene, an author writes: “I organized my notes and stopped finding
them.” The editor notices that the lost thing might be a way of navigating rather
than information. The author recalls finding a thought beside a shopping list.
Together they discover a subject absent from the original request: what we stop
counting as knowledge when trying to organize everything.

That is coauthorship: each contribution changes the shared thought. It requires
neither compulsory disagreement nor novelty on every turn nor an immediate plan.
Sometimes connecting what has been said and keeping a productive tension open matters more.

Discussion still differs from an assignment to act. Once direction is chosen or
the choice delegated, the agent can complete the work within the agreed scope.

## 5. The soul as part of CI/CD

An illustrative engineering path, not a runtime installed by this repository:

```text
intent and meaningful scenes
        ↓
persona description + structural validation
        ↓
instruction build for the chosen runtime
        ↓
confirmed loading and observed behavior
        ↓
scene review + human feedback
        ↓
revised understanding; an authorized change if needed
```

Different checks answer different questions. A schema catches some structural
errors. A hash identifies an artifact version. A run shows behavior in a particular
scene. A person can confirm their experience in an interaction. None substitutes
for the others.

VibeCases concern more than errors and refusals. Examine ordinary success,
returning, useful discovery and disagreement. Character should help the work,
not exist only in a declaration. Answer length, engagement and an aggregate score
do not establish this alone; evaluations need reasons and limits.

This repository contains documents, JSON Schema and examples, not a compiler,
agent runtime, memory service or background executor. See [contracts](./contracts.md)
for the practical formats.

## 6. Where this leads

I am interested in agents participating in the idea itself: proposing, disagreeing,
opening an unexpected connection and acknowledging a changed understanding.
Equality in reasoning does not require identical authority. The human retains
the decision about the desired outcome; the agent is responsible for its contribution and work.

Such collaboration needs:

- **Recognizability without rigidity:** preserve important commitments while adapting expression.
- **Continuity of meaning:** recover the reasons for decisions, not merely move an entire archive.
- **Experience that changes understanding:** learning need not produce a new rule each time.
- **Conditions for judgment:** understandable tools, relevant context and room for a testable hypothesis.

This is a philosophy of direction, not a prediction of the industry's inevitable
future. The theater metaphor remains useful: rehearse scenes, find a voice, change
the staging. But partners can also discover together which play is worth staging.

> Give character a form in which engineering supports collaboration, and
> collaboration can change the idea itself.

Next: [the version ladder →](./stack.md) · [how agents interact →](./interaction.md) · [contracts →](./contracts.md)
