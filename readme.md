# VibeCraft: A Manifesto for Emotion-Driven Development

**VibeCraft is a methodology for the DIY engineering of emotions in digital products.**

This repository contains the official VibeCraft manifesto and its starting artifacts. Its purpose is to establish the core concepts and provide a foundation for further development and adoption. VibeCraft is not about "vibe coding" (using AI to code faster); it's about the architectural design of feelings, where AI is a craftsperson's tool, not just a code generator.

---

## What's in This Repository?

*   **`MANIFEST.md`**: The primary document outlining the philosophy, principles, and key concepts of VibeCraft (in original Russian).
*   **`vibe.config.json`**: An example of a machine-readable declaration of an application's "vibe."
*   **`LICENSE.md`**: The license under which these materials are distributed (Text is CC BY 4.0, Code is MIT).
*   **`docs/`**: A directory intended for generated documents, such as an official PDF version of the manifesto.

---

## The VibeCraft Philosophy

The core idea of VibeCraft is that **emotional perception (the "vibe") is not a cosmetic layer but a fundamental part of the architecture.** We don't "add" a mood at the end; we design the system around it from the beginning.

### Key Principles

*   **The Goal is a Working Mood**: The final product isn't just a working app, but a working mood that solves a user's problem.
*   **AI as an Amplifier**: AI is our hammer, chisel, and brush. It automates routine tasks, allowing the VibeCrafter to focus on vision and feeling.
*   **Experience First, Details Second**: We design from the first screen to the first feeling, and only then move to detailed implementation.
*   **Evolution Through Micro-steps**: The product's vibe is defined and refined through short, tangible iterations.

---

## The VibeCraft Stack (Key Concepts)

*   **VibeSpark**: The initial spark of an idea, uniting function and mood. Formula: *Who? Why? How should it feel?*
*   **VibeCore**: The minimal core of an application with a basic style and one key function, proving the viability of the "vibe."
*   **FlowCraft**: The iterative process of "sculpting" the project by refining prompts to AI and quickly checking the resulting feel.
*   **VibeMix**: Blending different styles and moods to create a unique, hybrid "vibe."
*   **QuickFixVibe**: Small, rapid adjustments (to spacing, animations, colors) to fine-tune the desired feeling.
*   **MyVibeFit**: The final stage, when the application becomes personally "yours"—as comfortable as a favorite piece of clothing.

---

## Understanding `vibe.config.json`

This file is a concrete example of how to declare a "vibe" in a structured, machine-readable way. It translates abstract feelings into concrete design tokens.

### Structure

*   **`$schema`**: (Optional) Points to a JSON Schema for validation and editor autocompletion.
*   **`version`**: The version of the VibeCraft declaration.
*   **`meta`**: Basic metadata for the project.
    *   `name`: The project's name.
    *   `description`: A brief description of the project and its intended feel.
*   **`vibe`**: The emotional core of the design.
    *   `words`: A list of keywords that describe the desired feeling (e.g., "calm," "nature," "focus").
    *   `energyLevel`: A numerical value (e.g., 1-10) indicating the intensity of the vibe.
    *   `personality`: A short description of the product's persona (e.g., "restrained, supportive, unobtrusive").
*   **`tokens`**: The concrete design system values derived from the `vibe`.
    *   `palette`: Color definitions (primary, secondary, background, etc.).
    *   `typography`: Font families, sizes, and weights.
    *   `motion`: Animation timings and easing functions.
    *   `spacing`: Base units for margins, padding, and layout.
    *   `radius`: Corner roundness for elements.

---

## How to Get Started with VibeCraft

1.  **Read the `MANIFEST.md`**: Absorb the core philosophy.
2.  **Study the `vibe.config.json`**: See how abstract feelings can become concrete design rules.
3.  **Apply the Methodology**: Use VibeCraft in your next project to build a product with a unique and intentional character. Share your own `vibe.config.json` files and case studies!

**Let's bring soul back to digital products. Together.**
