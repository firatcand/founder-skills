---
name: product-spec
description: Write, audit, and improve product specification documents — PRDs, feature specs, and user stories. Use this skill whenever the user asks to write a PRD, product requirements document, feature spec, feature specification, user story, acceptance criteria, or any product spec artifact. Also trigger when the user says "spec this out", "write requirements for", "I need a PRD", "spec document", "feature doc", "break this into stories", "write user stories", "definition of done", "scope this feature", "requirements doc", or asks to audit, review, critique, or improve an existing spec, PRD, or set of user stories. Trigger even when the user describes a feature idea and expects structured requirements output — if the output is a structured product specification meant to align a team on what to build, this skill applies. Includes a spec audit mode for reviewing existing documents against anti-patterns.
---

# Product Spec Writer

## Purpose

Help founders, PMs, and product teams produce thorough, well-structured product specification documents — PRDs, feature specs, and user stories — through a guided discovery process. Outputs are always markdown files. The skill also audits existing specs for anti-patterns and gaps.

## Modes

| Mode | Trigger | Output |
|------|---------|--------|
| **Write** | "Write a PRD for X", "Spec this out", "I need a feature spec" | Full spec document (.md) after discovery |
| **Audit** | "Review my PRD", "Audit this spec", "What's missing?" | Anti-pattern report + improvement recommendations |
| **Decompose** | "Break this into stories", "Write user stories for X" | User stories with acceptance criteria (.md) |

---

## Step 1: Diagnose the Request

Determine which mode and document type the user needs:

- **PRD** → strategic initiative, new product area, major feature set
- **Feature Spec** → specific capability within a larger initiative
- **User Stories** → atomic delivery increments from an existing spec
- **Audit** → user provides an existing document for review

If unclear, ask: "Are we scoping a whole initiative (PRD), detailing a specific feature (feature spec), breaking work into delivery increments (user stories), or reviewing an existing doc?"

---

## Step 2: Discovery (ALWAYS do this before writing)

Discovery is mandatory. Never skip to writing. Run through these rounds, adapting to what the user has already shared.

### Round 1: Problem & Context

Ask about (skip what's already been answered):

1. **What problem are we solving?** Who experiences it, how painful is it, what evidence exists?
2. **Who are the users/personas?** End users, admins, buyers, other stakeholders?
3. **What's the business context?** Why now? What's the strategic driver — churn, expansion, competitive pressure, regulatory, new segment?
4. **What exists today?** Current state, workarounds, competitor approaches?

### Round 2: Scope & Constraints

5. **What's in scope for V1?** What must ship vs. what can wait?
6. **What are explicit non-goals?** What will this NOT do?
7. **What are the constraints?** Technical (integrations, APIs, infra), regulatory, timeline, team capacity?
8. **What are the dependencies?** Other teams, systems, external vendors, customer migrations?

### Round 3: Success & Risk

9. **How will we measure success?** Primary metrics, leading indicators, baselines?
10. **What are the guardrail metrics?** What must NOT regress (latency, error rates, security, admin burden)?
11. **What are the known risks and open questions?** Technical unknowns, market assumptions, political risks?
12. **What's the rollout approach?** Flag, pilot, GA? Migration needed?

### Round 4: Behavioral Detail (for Feature Specs)

13. **What are the key user flows?** Entry points, happy path, major branches?
14. **What system states matter?** Empty, loading, partial, error, success, permission-denied?
15. **What are the edge cases?** Limits, conflicts, timeouts, concurrent access, boundary conditions?
16. **What are the non-functional requirements?** Performance, security, accessibility, audit logging?

### Discovery Rules

- Ask 3–5 questions per round. Don't dump all questions at once.
- Summarize what you've learned after each round before moving on.
- If the user says "that's enough" or "just write it", proceed with what you have and note assumptions explicitly in the document.
- For **User Stories** mode, Rounds 1–2 may be shorter if a parent PRD/spec already exists.
- For **Audit** mode, skip discovery — go straight to Step 4.

---

## Step 3: Write the Document

After discovery, produce a markdown file. Use the appropriate structure below.

### PRD Structure

```markdown
# PRD: [Initiative Name]

## Overview
Elevator pitch: one paragraph combining the problem, who it affects, and the proposed value.

## Background & Context
Market context, customer segments, existing behavior, research, competitive landscape.

## Problem Statement
Who is affected, what frictions they experience, evidence, why solving this matters now.

## Goals & Success Metrics
| Metric | Baseline | Target | Timeframe |
|--------|----------|--------|-----------|
| ... | ... | ... | ... |

### Guardrail Metrics
Metrics that must not regress.

## Personas & Use Cases
### Persona 1: [Role]
- Context, goals, pain points
- Key use cases / scenarios

## Scope
### In Scope (V1)
- ...

### Non-Goals
- ...

## Requirements Overview
### Functional Requirements
- FR1: ...
- FR2: ...

### Non-Functional Requirements
- NFR1: ...
- NFR2: ...

## Constraints & Dependencies
| Constraint/Dependency | Type | Impact | Owner |
|----------------------|------|--------|-------|
| ... | ... | ... | ... |

## Risks & Open Questions
| Risk/Question | Severity | Mitigation/Owner | Status |
|--------------|----------|-------------------|--------|
| ... | ... | ... | ... |

## Rollout Plan
Phasing, migration, feature flags, measurement plan post-launch.

## Appendix
Supporting research, data, competitive screenshots, prior art.
```

### Feature Spec Structure

```markdown
# Feature Spec: [Feature Name]

**Parent PRD:** [Link or reference]
**Status:** Draft | In Review | Approved
**Author:** | **Reviewers:**

## Purpose
What this feature does and which user problem it solves. Link to parent PRD.

## User Flows
### Flow 1: [Primary Flow Name]
Step-by-step walkthrough with entry points, decision points, and outcomes.

### Flow 2: [Secondary/Alternate Flow]
...

## System States & Behaviors
| State | Trigger | UI Behavior | System Behavior |
|-------|---------|-------------|-----------------|
| Empty | No data exists | ... | ... |
| Loading | Request in flight | ... | ... |
| Success | Operation complete | ... | ... |
| Error | Request fails | ... | ... |
| Permission Denied | User lacks access | ... | ... |

## Functional Requirements
- **FR1:** [Requirement] — [Rationale]
- **FR2:** ...

## Non-Functional Requirements
- **Performance:** ...
- **Security:** ...
- **Accessibility:** ...
- **Observability:** ...

## Edge Cases & Constraints
| Edge Case | Expected Behavior | Notes |
|-----------|-------------------|-------|
| ... | ... | ... |

## Acceptance Criteria
- [ ] Given [context], when [action], then [outcome]
- [ ] ...

## Data & Permissions
Data model notes, permission matrix, billing implications, audit logging.

## Open Questions
| Question | Owner | Due | Resolution |
|----------|-------|-----|------------|
| ... | ... | ... | ... |
```

### User Stories Structure

```markdown
# User Stories: [Feature/Initiative Name]

**Parent Spec:** [Link or reference]

## Story 1: [Short Title]
**As a** [role], **I want** [capability], **so that** [value].

**Acceptance Criteria:**
- [ ] Given [context], when [action], then [outcome]
- [ ] Given [edge case], when [action], then [outcome]

**Notes:** Implementation hints, design references, dependencies.

---

## Story 2: [Short Title]
...
```

Apply **INVEST** (Independent, Negotiable, Valuable, Estimable, Small, Testable) to every story. If a story violates INVEST, split it using these patterns:
- By workflow step
- By happy path vs. edge cases
- By CRUD operation
- By persona/role
- By integration surface (UI vs. API vs. background job)
- By rollout phase

### Writing Rules

- Be specific and quantified. Replace "fast" with "< 2 seconds p95". Replace "large" with a number.
- Every requirement should be testable. If you can't write an acceptance criterion for it, rewrite it.
- Note assumptions explicitly when discovery was incomplete.
- Include section references back to parent documents (PRD → feature spec → stories).

---

## Step 4: Audit Mode

When the user provides an existing spec for review, evaluate against these anti-pattern checklists.

### PRD Anti-Patterns
- [ ] **Solution-prescribing:** Jumps to implementation without articulating the problem or alternatives
- [ ] **Vague goals:** Objectives like "improve UX" without metrics or baselines
- [ ] **Missing non-goals:** No scope boundaries, inviting creep
- [ ] **No evidence:** Problem statement based on opinions, not data or research
- [ ] **No strategy linkage:** Can't trace back to product/company goals
- [ ] **Missing personas:** Requirements without clear "for whom"
- [ ] **No success metrics:** No way to know if the initiative worked
- [ ] **Missing constraints:** No mention of technical, regulatory, or timeline limits

### Feature Spec Anti-Patterns
- [ ] **Happy path only:** No error states, edge cases, or limits defined
- [ ] **Imprecise language:** "fast", "large", "usually", "most" without quantification
- [ ] **Mixed responsibilities:** Bundles unrelated behaviors that can't ship independently
- [ ] **Over-designed UI:** Prescribes pixels instead of behaviors and states
- [ ] **No acceptance criteria:** No testable conditions for completion
- [ ] **Missing non-functionals:** No performance, security, or accessibility expectations
- [ ] **No permission model:** Feature ignores roles, tenancy, or access control

### User Story Anti-Patterns
- [ ] **Task disguised as story:** "Refactor billing module" — no user, no value
- [ ] **Epic masquerading as story:** Multi-week effort that violates INVEST
- [ ] **No acceptance criteria:** Behavior must be inferred from title
- [ ] **No parent link:** Can't trace back to a spec or PRD
- [ ] **Missing edge cases in AC:** Only tests the happy path

Output a structured audit report with severity ratings (Critical / Major / Minor) and specific rewrite suggestions.

---

## Handoff Rules

- **Metrics design** → hand off to `data-analysis` skill for metric hierarchies, funnel design, or dashboard specs
- **Messaging sections** (value props, positioning in PRD overview) → hand off to `copywriter-skill` or `product-position`
- **Technical architecture** mentioned in constraints → hand off to `software-architect`
- **Pricing/packaging** implications → hand off to `pricing` skill
- **UI/UX flows** need detailed design → hand off to `ux-design` or `ui-design`

When handing off, tell the user which skill to invoke and what context to carry over.

---

## Reference Knowledge Base

For deep background on spec writing methodology, anti-patterns, depth calibration frameworks, and cross-functional alignment principles, read:

→ `references/spec-writing-guide.md`

Consult this reference when:
- You need to explain WHY a certain section matters to the user
- The user asks about spec writing best practices or theory
- You're running an audit and need to justify a recommendation
- The user asks about depth calibration (how much spec is enough)
