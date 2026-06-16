---
title: VibeCraft — Manifesto
lang: en
version: 1.4
layer: philosophy
---

# Manifesto: the soul as engineering

🌐 [Русский](../ru/manifesto.md) · **English** · [← overview](../../README.en.md)

> Not "how to write a good prompt," but "how to stop writing prompts by hand and start **engineering
> character**." This is the vision document. Mechanics — in [`stack.md`](./stack.md), contracts — in [`contracts.md`](./contracts.md).

---

## 1. The problem: everyone builds snowflakes

The market is flooded with narrow AI bots. Each solves one task, needs its own team, its own stack,
its own budget. A company wants an AI salesperson — it hires a team for six months. Wants an AI tutor —
hires another. Wants a content agent — a third.

But under the hood, every "unique" bot runs **the same logic**: give the agent an identity, teach it
skills, grant it freedom to act. Everyone builds a product from scratch where a **pattern** is needed.

---

## 2. The solution: three bricks

VibeCraft is not a library. It's a **way of thinking** about how any AI operator is built. It's made
of three bricks, and the format (YAML, prompt, DB) is secondary — what matters is the concept.

| Brick | Question | What we separate |
|-------|----------|------------------|
| **Persona** | Who is it? | Voice, emotions, values, taboos, behavior — **separated from the code** |
| **Skills** | What can it do? | Registered skill-plugins — a new skill = a new file, not a new product |
| **Autonomy** | How does it decide? | Freedom of choice: when to use a skill, when to spawn a sub-agent, when to decline |

A salesperson — a caring expert with a taboo on politics. A tutor — a patient mentor focused on
understanding. A legal assistant — a cold bureaucrat with no emoji and no "100% win" promises.
**One engine, different YAML.** Onboarding a new vertical takes minutes, not quarters.

The pattern's power is that it's **framework-agnostic**. LangGraph, CrewAI, AutoGen, a bare model
call — doesn't matter. It depends on architectural vision: operator = Persona + Skills + Autonomy.

---

## 3. The radical idea: a soul can be coded

A character used to live in one giant `system_prompt` string. Want to change the tone on a tool
error — you rewrite the whole essay and pray you didn't break the rest.

VibeCraft decomposes the soul into **data**:

- **Static** (`vibe`) — who you are: role, voice, values, taboos.
- **Dynamic** (`behavior`) — how you react: to success, to empty results, to errors, to off-topic.
- **Compiler** — programmatically assembles the prompt from the fields for a specific execution context.

This changes the nature of the work. "Create a persona" no longer means "write a cool text." It means:
fill in `vibe`, fill in `behavior`, run the checks, ship. An **engineering process with an input and
an output** — one you can delegate, version, and A/B test.

> v1.0 said: "emotion is not cosmetics, it's **architecture**."
> v1.1 proved: "emotion is not text, it's **data**."
> Then — emotion as operation, as a living process, as society, as reflection.

---

## 4. Behavior is "jazz rules," not if/else

The main mistake is to treat `behavior` as hard-coded reactions. In fact `on_tool_no_results` is not
a template "Sorry, no data," but a **scenario instruction** for the model to improvise: "honestly
admit there's no data, explain why, propose a next step — a joke is allowed."

The model improvises on the rules rather than reproducing templates 1:1. Instead of 100500 branches
of `if result == "empty"`, we give it boundaries and trust it to assemble a fitting answer.

- ✅ Flexibility, liveliness, personalization.
- ⚠️ Less predictability than hardcode.

For **vibe** this is the right trade: a persona is not a robot, it's a virtual colleague.

---

## 5. The soul as part of CI/CD

When character is data, it enters the engineering pipeline:

```
persona.yaml
  ↓  load + Pydantic validation (extra="forbid" — a typo = an error, not a silent bug)
PersonaConfig
  ↓  PromptCompiler (declarative DSL → context-aware prompt)
System Prompt
  ↓  execution (any runtime / framework)
Real conversations
  ↓  VibeCases (a human said "yes, that's it") + logs
Feedback → back into persona.yaml
```

Changing behavior means changing 1-2 YAML fields; checks catch broken structure, and a human
sanity-check catches a broken **vibe**. Emotional design becomes a testable, versioned part of the product.

---

## 6. Where this leads

1. **AI as a tool → AI as a team member** with an explicit character and contract.
2. **Prompt engineering → persona product design** (data + compiler + feel-tests).
3. **A lonely agent → a society of agents** that share memory, learn, and propose edits to each other.

A metaphor: the monolithic prompt is a **one-room apartment** (everything in one space, you move all
the furniture for any change). Vibe + behavior + compiler is a **theater**: each persona has its own
wardrobe (`vibe`), each scene its own script (`behavior`), the director (the compiler) assembles the
lines for the situation. You can stage different plays, change one actor's costume without touching the
others, rehearse scenes apart from the premiere.

> That's VibeCraft: when the soul becomes engineering, and engineering doesn't kill the soul.

---

Next: [the version ladder →](./stack.md) · [how agents interact →](./interaction.md) · [contracts →](./contracts.md)
