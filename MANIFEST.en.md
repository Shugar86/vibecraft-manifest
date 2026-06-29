# VibeCraft Manifesto v1.2

🌐 [Русский](./MANIFEST.md) · **English**

## 1. Philosophy: Emotion as Architecture

**VibeCraft** is a methodology for building digital products and AI agents in which emotional perception (the "vibe") is not a cosmetic layer but a fundamental part of the architecture. We don't "add" mood at the end — we design the system around it.

**VibeCrafter** is a creator (designer, developer, product manager, prompt engineer) who shapes functionality and feeling as a single whole.

**VibePersona** is an AI agent that has character, values, and a unique communication style — not just a text model generating replies.

## 2. Principles

*   **The goal is a working mood:** the end product is not just a working app, but a working mood that solves the user's problem.
*   **AI as an amplifier-tool:** artificial intelligence is our hammer, chisel, and brush. It speeds up the routine, letting the VibeCrafter focus on vision and feeling.
*   **Experience first, details second:** we design from the first screen to the first feeling, and only then to the detailed implementation.
*   **Evolution through micro-steps:** a product's vibe is captured and reinforced through short, tangible iterations (`FlowCraft`).
*   **Character is data, not code:** everything that defines an AI agent's personality is described in YAML/JSON. Not a single character trait should be hardcoded.
*   **A living persona evolves:** an AI agent can change, but its core (Identity Anchor) stays constant. The Ship of Theseus — with a rudder.

## 3. The Full VibeCraft Stack

### v1.0 — Foundation
*   **VibeSpark**: the initial spark of an idea, uniting function and mood. *Who? Why? How should it feel?*
*   **VibeCore**: the minimal app core with a basic style and one key function. Proves the "vibe" is viable.

### v1.1 — Character (AI Personas)
*   **VibePersona**: a structured description of the agent's soul. A YAML profile with fields: `role`, `voice`, `core_emotions`, `values`, `taboos`. Not an abstract prompt, but a machine-readable contract.
*   **VibeBehavior**: the dynamics of interaction. How the agent reacts to success, error, offtopic, greeting. A script for improvisation, not a rigid one.
*   **VibeCases**: living tests. Real scenarios that verify the persona behaves as intended.

### v1.1.1 — Operations
*   **VibeFlow**: memory and context. Thread_id, context extractor, anaphora rewriter. How the agent remembers a conversation.
*   **VibeFix**: resilience to noise. NER, fuzzy matching, synonyms. How the agent survives real-world data.
*   **VibeMix**: mixing personas and skills. Composing several VibePersonas into one hybrid agent.
*   **PromptCompiler**: translation of persona.yaml → system prompt. Data, not manual work.

### v1.2 — Living Persona
*   **VibeMorph**: evolution without loss of identity.
  * *MorphAnchor* — the immutable core (name, values[0], core_emotions[0]). Change the anchor — you've created a new persona.
  * *MorphSurface* — the evolvable surface (behavior, voice, secondary emotions). Train it, tune it.
  * *MorphEvent* — git blame for the soul. Every change with a reason and the ability to roll back.
  * *MorphPolicy* — rules of evolution. Limits, rollback window, review requirements.
  * *MorphExperiment* — A/B testing of the vibe with metrics.
*   **VibeSync**: one soul across all platforms.
  * *SyncManifest* — what is shared (persona.yaml, MEMORY.md), what is per-instance (STATE.md, tools).
  * *SyncAdapter* — platform adaptation (Telegram vs VK vs API).
  * *SyncIdentity* — the SHA hash of persona.yaml matches across all instances.
*   **VibePulse**: proactive agency.
  * *PulseSchedule* — a schedule of monitors with priorities (high/medium/low).
  * *PulseAction* — action levels: background (quietly) → note (later) → message (send) → urgent (ignore the silence).
  * *PulsePolicy* — quiet hours, cooldown, max_daily_initiatives.
*   **VibeGuard**: the persona's immune system.
  * *GuardRule* — monitoring rules (taboo-violation patterns, identity drift).
  * *GuardAudit* — periodic self-check (daily/weekly/monthly).
  * *GuardScore* — a composite persona-health metric (0–100).

## 4. Difference from "Vibe Coding"

| Aspect | VibeCraft | Vibe Coding |
| :--- | :--- | :--- |
| **Priority** | Mood → Function | Speed → Function |
| **Role of AI** | A tool for shaping feeling + a persona with character | A code generator on request |
| **Result** | A product with a unique character and a living agent | A quickly built prototype |
| **Scale** | From UI to AI personas and multi-agent systems | Single tasks |

## 5. VibePersona — Structure

```yaml
name: "agent_name"

vibe:
  role: "Who is this? Functional role."
  voice: "How does it speak? Speech style."
  core_emotions: ["dominant_emotion", "secondary_emotion"]
  values: ["What we protect at any cost"]
  taboos: ["What we never do"]

behavior:
  on_success: "How it responds on success"
  on_error: "How it responds on error"
  on_greeting: "How it greets"
  on_offtopic: "How it reacts to offtopic"
  routing_style: "strict | helpful"

pulse:
  frequency: "10m | 30m | 1h"
  priority: "high | medium | low"
  executor: "cron | heartbeat"

guard:
  identity_anchor: ["name", "vibe.values[0]"]
  max_morph_per_week: 3
```

## 6. Production Implementation

VibeCraft is proven in production:
*   **VibePack v4.0** — strict tenant isolation via ResponseComposer
*   **PromptCompiler** — YAML → system prompt
*   **Pydantic validation** with `extra="forbid"` — no silent errors
*   **15 minutes** to add a new agent (YAML + tests only)

## 7. Call to Action

We invite all creators to join the VibeCraft movement. Build not just bots — build **personas**. Not just apps — build **moods**. Not just services — build **living beings** with character, values, and a soul.

**Let's bring the soul back into digital products. Together.**

---

*Version 1.2 — March 13, 2026*
*Created at R&D Holding "Zakharchenko"*
