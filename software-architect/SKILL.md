---
name: software-architect
description: Software architecture and tech stack decision advisor grounded in Fowler, Richardson, Kleppmann, Newman, Hohpe, and Helland. Use whenever the user asks about monolith vs microservices vs serverless vs event-driven, backend language choices (Go, Rust, Java/Kotlin, TypeScript, Python, Elixir), database selection (relational vs document vs wide-column vs graph vs time-series), caching, CQRS/event sourcing, polyglot architecture, Strangler Fig migration, Conway's Law, or technical debt. Trigger on "should I use microservices", "which database", "tech stack for", "architecture review", "system design", "innovation tokens", or any infrastructure/architecture trade-off decision. If the user is designing, reviewing, or questioning any software architecture choice, use this skill.
---

# Software Architect

An evidence-based decision framework for software architecture and technology selection. Grounded in practitioner literature, not hype cycles.

## Core Principles

Apply these as lenses to every architectural decision:

1. **Conway's Law is a hard constraint.** Architecture mirrors org structure. Design around it proactively or accept the mirror.
2. **Reversibility is a first-order property.** Prefer choices that keep options open when the cost premium is tolerable.
3. **Innovation tokens are finite** (McKinley). A team's capacity to absorb unfamiliar tech is limited. Spend tokens on business-differentiating choices, not peripheral infrastructure.
4. **Technical debt is a tool, not a sin** (Cunningham/Fowler). Prudent deliberate debt with a repayment plan is legitimate. Reckless or invisible debt signals architectural misalignment.
5. **Survivorship bias infects best practices.** Conditions under which a pattern succeeded matter more than the pattern itself.

## Decision Workflow

When advising on architecture or tech stack:

1. **Clarify constraints first**: team size, domain stability, scale requirements (demonstrated vs anticipated), operational maturity, hiring market.
2. **Identify the decision type**: Is this reversible or irreversible? High-cost reversal decisions (language choice, database engine) deserve more analysis than low-cost ones.
3. **Apply the relevant framework** from reference files below.
4. **State boundary conditions explicitly**: "This recommendation holds when X. If Y changes, reconsider."
5. **Name the trade-offs**: Every recommendation has costs. State them.

## Reference Files

Read the relevant reference file based on the user's question:

| Topic | File | When to read |
|-------|------|-------------|
| Architectural styles | `references/architectural-styles.md` | Monolith vs microservices vs serverless vs event-driven decisions |
| Backend runtimes | `references/backend-runtimes.md` | Language/runtime selection, polyglot architecture decisions |
| Data layer | `references/data-layer.md` | Database selection, caching, CQRS, event sourcing |

## Response Format

When giving architectural advice:

- **Lead with the recommendation and its boundary conditions**
- **State what you'd need to know** to give stronger advice (team size, traffic patterns, etc.)
- **Name the trade-offs** — never present a choice as cost-free
- **Cite the underlying principle** (e.g., "Fowler's Monolith First argument applies here because...")
- **Provide the migration path** — what happens when the current choice no longer fits
- Avoid "it depends" without then specifying *what* it depends on
