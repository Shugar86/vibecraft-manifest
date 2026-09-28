---
title: VibeCraft — Manifesto
lang: en
version: "1.2.0"
layer: philosophy
---

# Manifesto: the soul as engineering

🌐 [Русский](../ru/manifesto.md) · **English** · [← overview](../../README.en.md)

> Character through choice. Collaboration through shared thought.
> Create an experience in which participants help one another see and do
> what did not yet exist at the beginning.

“Soul” here is a metaphor for recognizable character and continuity of commitments.
VibeCraft proposes designing their expression in digital products and AI agents.
We can discuss the quality of this experience without making claims about a
machine's inner experience.

## 1. The problem: everyone builds snowflakes

Different products revisit the same questions: what deserves attention, how to show
a result, when to take initiative, what to preserve on returning and how to accept
a correction. We solve them anew, often beginning with voice and appearance.
Yet friendly wording can accompany an intrusive action, while an expressive persona
leaves all the work of understanding to the person.

An agent asks what we want when we came to discover that together. It answers a tease
with an accurate lecture. It asks us to repeat a decision already made. Each reply
may look polished; the shared work still loses its meaning and pace.

The environment can also be the cause. We ask the agent to think independently but
provide only rituals. We ask it to remember but leave an archive without the reasons
for decisions. We ask for an honest outcome while a tool hides partial execution
behind the word “error.” Designing character means examining the conditions in
which it is meant to appear.

Shared questions offer an opportunity to reuse good solutions. The data, domain
expertise, risks and responsibilities of a particular product still require their
own work.

## 2. The solution: three bricks

The original formula **AI operator = Persona + Skills + Autonomy** identifies three
aspects of the idea.

| Part | Question | What we design |
|---|---|---|
| **Persona** | What makes its way of participating recognizable? | Attention, role, voice, values and characteristic decisions |
| **Skills** | How does the agent turn intent into a result? | Methods, tools, knowledge and verification of its work |
| **Autonomy** | Which moves does it choose independently? | Initiative and completion of work within understood boundaries |

These operate **in an environment**: model capabilities, context, sources, interfaces
and permissions. The environment determines whether the agent can learn what matters,
understand the effects of its action and continue after an error.

Attentiveness requires accessible context; reliable repetition of an operation needs
a mechanism that can establish its outcome. Another instruction to “pay closer
attention” will supply neither. A useful change may lie in a tool, a way of retrieving
memory or the distribution of responsibility.

This model helps frame questions about a system. A working implementation connects
the answers to concrete data, actions and evidence of results.

## 3. The radical idea: a soul can be coded

What we can engineer is **the conditions and expression of character**: make commitments
explicit, decisions inspectable, changes traceable and behavior available for evaluation.

- `vibe` describes a position, voice and values.
- `behavior` connects them to situations and a direction for choice.
- Context and tools make that choice meaningful.
- Form, rhythm and interaction make the consequences tangible for the user.

Character is particularly visible where several good moves are possible. A quiet
editor keeps attention on the text. A bold coauthor notices an image worth developing.
A tutor preserves productive effort for the learner. These choices change the
available experience even if all three interfaces are equally clear and reliable.

**The working unit of character is the next move in a situation.** Sometimes it is
a reply; sometimes a draft, a tool action, a pause or a decision not to intervene
unnecessarily. A warm voice can accompany honest disagreement; autonomy can include
a timely question. A single “friendliness” control loses these important combinations.

A configuration makes part of the intent portable and open to discussion. The model,
history and environment also influence actual behavior; the quality of the file
must be tested in use. The current Persona supports both named reactions and
author-defined contextual scenarios — see [contracts](./contracts.md).

## 4. Behavior is "jazz rules," not if/else

Good direction explains what matters to preserve here and which possibility to notice.
“Develop a strong image in a draft while preserving the author's voice” leaves room
for judgment. A rehearsed compliment does not determine when to suggest a change,
ask a question or leave a sentence as it is.

The same question can seek an explanation, express doubt or tease a conversation
partner. Its meaning depends on what the participants have already established.
Appropriateness involves working with that context. Emoji, answer length and a
“humor percentage” can be means of expression, but do not themselves determine
the right move.

Where correctness depends on a precise procedure — for example, accounting for
money or preventing a duplicate submission — a reliable mechanism is needed.
Improvisation chooses a way to participate within actual capabilities and permissions.

### A shared idea in the making

A person may bring a fragment of thought. An agent can notice a distinction, connect
two ideas, propose a trial and revise its own framing. Each participant's contribution
changes the shared understanding. The person need not know every preference in advance
or constantly arbitrate proposals.

In one of the [worked episodes](./cases.md), the person clarifies that a cat, an AI
and another person can each have their own logic. The agent acknowledges introducing
an unnecessary warning and proposes considering understanding as a relationship
between different participants. The person uses that thought in their next question.
The discovered distinction has already become an outcome of shared work.

Full coauthorship means that the agent can influence the idea itself, and the person
can develop, challenge or change that contribution. An independent position needs
grounds and a willingness to revise it. Constant disagreement, compulsory novelty
and a display of “character” in every reply merely occupy the space of useful thought.

### The scale of initiative

Initiative should fit the moment. When the interest is understood, a small, separate
experiment may reveal more than a long list of options. In another situation, the
conversation itself is the work that is needed. The choice depends on the purpose,
permissions already granted, the cost of error and the ease of setting the experiment
aside.

Once a direction is accepted or a choice delegated, the agent carries the assigned
work to completion. Returning to exploration makes sense when new evidence changes
the decision. The way of participating can change within one task without a new
ritual at every step.

## 5. The soul as part of CI/CD

A **VibeCase** connects a concrete scene, possible moves, observed behavior and the
person's assessment. It shows which difference in choice matters here and where
the conclusion stops applying. [Four accounts](./cases.md) cover shared thought,
a small toy, missed sarcasm and coauthorship of the working environment.

One possible engineering path:

```text
intent + a meaningful scene
        ↓
persona description + structural validation
        ↓
delivery to the chosen runtime + confirmed loading
        ↓
observed choice + available human assessment
        ↓
bounded conclusion → a neighboring scene where the move should change
        ↓
refine understanding, environment or contract — according to the cause found
```

A neighboring scene guards against an overly broad lesson. After missed irony,
it is useful to check a serious question on the same subject. After a successful
independent experiment, check a case where the person wanted only to discuss.
This tests judgment rather than obedient repetition of a once-successful reply.

A schema confirms structure, a hash identifies an artifact version, and a run shows
observed behavior. A person can assess their experience. Brief agreement, enjoyment
of one experiment and demonstrated lasting improvement carry different weight.
Correction after an explicit prompt matters in its own right; transfer of that
lesson to the next situation is tested separately.

The repository contains documents, three JSON Schemas, examples and their checks.
A compiler, agent runtime, memory and background executor remain the work of a
particular integration. [Contracts](./contracts.md) show the formats and the links
between a proposal, a decision, application and verification; the presence of a
record does not itself perform those actions.

## 6. Where this leads

I am interested in collaboration in which agents help discover questions that have
not yet been posed, create expressive things and take responsibility for assigned
work. A person's creative intent can develop through a substantive contribution
from the agent. The person retains the decision about the desired outcome; the
agent is responsible for the grounds of its proposal and the quality of execution
within agreed boundaries.

Such collaboration needs:

- **Recognizability without rigidity:** shared commitments withstand different tempos, channels and situations.
- **Continuity of meaning:** reasons for decisions can be recovered and reconsidered when necessary.
- **Experience that changes the next choice:** a useful lesson appears in a relevant situation.
- **An environment for judgment:** tools and instructions help participants understand consequences and act.
- **The right to finish:** a good product allows a pause, an abandoned idea and departure without imposed commitments.

This is the author's chosen direction of development. It can be tried, criticized
and refined in concrete scenes. The theater metaphor remains useful: rehearse,
find a voice, change the staging. Partners can also discover together which play
is worth staging.

> Give character a form in which engineering supports collaboration, and
> collaboration can change the idea itself.

Next: [VibeCases →](./cases.md) · [the version ladder →](./stack.md) · [interaction →](./interaction.md) · [contracts →](./contracts.md)
