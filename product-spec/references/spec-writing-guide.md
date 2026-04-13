# Spec Writing Guide: Knowledge Base

## Table of Contents
1. [Foundations](#1-foundations)
2. [Document Hierarchy](#2-document-hierarchy)
3. [PRD Deep Dive](#3-prd-deep-dive)
4. [Feature Spec Deep Dive](#4-feature-spec-deep-dive)
5. [User Stories Deep Dive](#5-user-stories-deep-dive)
6. [Cross-Functional Alignment](#6-cross-functional-alignment)
7. [Depth Calibration](#7-depth-calibration)
8. [Anti-Patterns Expanded](#8-anti-patterns-expanded)
9. [AI-Enhanced Spec Writing](#9-ai-enhanced-spec-writing)

---

## 1. Foundations

Product specifications are structured narratives that describe requirements, context, and expected value so development teams understand what to build and why. They articulate user problems, functional and non-functional requirements, constraints, and success criteria.

Specs serve as a shared reference point — a single source of truth that reduces ambiguity, preserves decisions, and provides a stable anchor during implementation. Modern teams treat specs as living documents that evolve during discovery and delivery while retaining a clear baseline of intent.

Specs answer two fundamental questions: what should the product be like, and how are we going to build it. A well-written spec captures the "what" and "why" clearly enough that cross-functional teams can derive and debate the "how" without losing sight of value.

---

## 2. Document Hierarchy

PRDs, feature specs, and user stories form a **hierarchy of specificity**, not competing formats:

| Level | Document | Scope | Audience |
|-------|----------|-------|----------|
| Strategic | PRD | Whole initiative or product area | Leadership, cross-functional leads |
| Behavioral | Feature Spec | Specific capability | PMs, engineers, designers, QA |
| Delivery | User Story | Atomic work increment | Engineers, QA, scrum facilitators |

**Example cascade:** A PRD for "Self-serve billing" spawns feature specs for "Usage-based invoicing", "Tax handling", and "Credits and discounts." Each feature spec decomposes into user stories schedulable into sprints. Every story traces back to a clear problem and success metric.

---

## 3. PRD Deep Dive

### Purpose
A PRD describes what a product or feature should do and why at a strategic yet actionable level. It is a stakeholder alignment tool — not a technical design doc. It frames product vision, user needs, high-level requirements, and constraints that any solution must satisfy.

### Problem Definition Best Practices
- Anchor in evidence: usage data, user research, support insights — not opinions
- Reflect multi-stakeholder nature: end users, admins, security, finance, procurement
- Clarify the driver: existing pain, new segment, competitive pressure, regulatory requirement
- Connect to business model impact: churn, expansion, activation, operational costs

### Success Metrics Best Practices
- Specific, measurable, time-bound with baselines and target improvements
- Include guardrail metrics that must not regress (latency, error rates, security posture)
- Separate outcome metrics (did it work?) from guardrails (did we break anything?)

### Scope Boundaries
- Reflect integration surfaces: APIs, SSO, billing systems
- Include permission models and supported tiers/regions
- Explicit non-goals make deferral decisions visible and defensible
- Tie scope to personas and use cases

### Alignment Function
PRDs are the convergence point where leadership and execution teams agree whether to proceed. Once approved, the PRD becomes the reference for design exploration, technical design, feature spec sequencing, and backlog creation.

---

## 4. Feature Spec Deep Dive

### Role
Feature specs translate strategic intent into concrete product behavior. They act as the contract between product, engineering, and design — describing expected functionality, constraints, and acceptance criteria in enough detail for independent parallel work.

### User Flows Best Practice
- Cover primary and secondary entry points (navigation, deep links, notifications)
- Document main paths and critical branching points
- Include error and missing-prerequisite paths

### System State Coverage
States to always consider:
- **Empty:** No data exists yet
- **Loading:** Operation in progress
- **Partial:** Long-running operation, incomplete data
- **Success:** Happy path complete
- **Error:** Transient failure, retries
- **Permission Denied:** Feature flags, roles, or entitlements block access

### Acceptance Criteria Best Practice
- Specific, measurable, user-focused
- Use Given/When/Then format for clarity
- Include edge cases and performance expectations
- These are the executable contract — derivable into test cases and automated checks

### Cross-Functional Contract
- Product owns problem framing and scope
- Design owns interaction and visual design
- Engineering owns technical feasibility and implementation
- QA owns validation against acceptance criteria
- The spec captures agreed behavior and constraints

---

## 5. User Stories Deep Dive

### INVEST Model
| Criterion | Meaning | Why It Matters |
|-----------|---------|----------------|
| Independent | No unnecessary coupling to other stories | Enables re-prioritization |
| Negotiable | Details can be discussed, not locked | Supports agile flexibility |
| Valuable | Delivers a slice of user value | Justifies inclusion in sprint |
| Estimable | Team can roughly size it | Enables planning |
| Small | Fits in one iteration | Reduces risk |
| Testable | Has clear pass/fail conditions | Enables QA |

### Definition of Done vs. Acceptance Criteria
- **DoD** = team-wide bar for any story (coded, reviewed, tested, documented, deployed)
- **Acceptance Criteria** = story-specific behavior and edge cases
- Keep AC concise and focused on what QA tests; leave implementation in the feature spec

### Decomposition Patterns
- By workflow step
- By happy path vs. edge cases
- By CRUD operations
- By persona/role (admin vs. end user)
- By integration point (UI vs. API vs. background job)
- By rollout phase (internal → pilot → GA)

### Traceability
Every story should reference its parent feature spec (and via that, the PRD). This enables:
- Aggregating progress at initiative level
- Checking scope against PRD
- Preventing technical drift from original problem
- Onboarding new team members

---

## 6. Cross-Functional Alignment

### What Each Audience Needs

**Engineers** need: precise behavior definitions, edge cases, constraints, non-functional requirements to make confident implementation choices.

**Designers** need: clear problem framing, personas, constraints, plus enough behavioral detail to design flows consistent with the product.

**Leadership** needs: clarity on problem, impact, trade-offs, risk, and enough structure to evaluate prioritization and resourcing.

**QA** needs: acceptance criteria, edge cases, and a mapping from requirements to test cases for systematic verification.

### Layered Documentation Strategy
To avoid duplication:
- PRD → problem and outcomes
- Feature spec → behavior
- Technical design doc → implementation
- Stories → units of work

Cross-link between layers. Establish clear ownership for authoring and maintaining each type.

---

## 7. Depth Calibration

### Core Principle
Document depth should match ambiguity, risk, and novelty. Over-specifying routine tasks slows teams. Under-specifying ambiguous initiatives causes rework.

### Calibration Dimensions

| Dimension | Low (lighter spec) | High (deeper spec) |
|-----------|-------------------|-------------------|
| Problem/solution ambiguity | Well-understood pattern | New market, undefined needs |
| Risk and impact | Low-stakes, internal | Billing, security, compliance, SLAs |
| Novelty | Familiar domain and stack | New architecture, new team |
| Cross-team dependencies | Single squad | Multiple systems, squads |
| Reversibility | Easy to revert | Hard to undo (data models, public APIs) |

**Rule of thumb:** If two or more dimensions are high, write a full PRD and detailed feature specs. If all are low, a brief PRD section and annotated stories may suffice.

### Iterative Deepening
Start with a lean outline. Deepen sections that prove contentious or unclear as discovery progresses. Write spec → observe misunderstandings → update spec → repeat.

---

## 8. Anti-Patterns Expanded

### Why Specs Fail
Specs fail not because they're missing sections but because they leave too much room for interpretation or mix concerns. Common result: engineering builds a scalable generic solution when leadership expected a narrow MVP (or vice versa). These mismatches surface late — during demos or after release — when they're expensive to fix.

### PRD Failures
- Solution-prescribing without articulating the problem
- Vague or unmeasurable goals ("improve user experience")
- Missing non-goals leading to relentless scope creep
- No user or market evidence (opinion-based problem statements)
- No linkage to strategy (can't explain why this over other initiatives)

### Feature Spec Failures
- Happy path only — errors, limits, exceptional states undefined
- Imprecise language ("fast", "large", "usually") without quantification
- Mixed responsibilities — bundles unrelated behaviors
- Over-designing UI divorced from design system
- Copy-pasted boilerplate nobody reads

### User Story Failures
- Tasks disguised as stories (no user, no value)
- Epics masquerading as stories (multi-week, multi-dependency)
- No acceptance criteria
- No linkage to parent specs

### Downstream Cost
Misaligned specs → wasted engineering time, increased defects, delayed launches, eroded trust. With AI-assisted development, poor specs cause agents to generate incorrect code, amplify edge-case blind spots, and produce inconsistent behavior across components.

---

## 9. AI-Enhanced Spec Writing

### AI-Assisted Drafting
AI tools accelerate mechanical aspects (formatting, boilerplate, initial decomposition). However, AI-generated specs are prone to structural inconsistencies, fabricated details, and shallow domain reasoning without supervision. Human review for technical coherence, cross-references, and risk assessment remains essential.

### Living and Executable Specs
Spec-driven development treats specs as executable contracts that drive tests, monitoring, and AI agents. Acceptance criteria in machine-readable formats can link to automated tests and be consumed by AI coding agents.

### Spec Granularity for AI
Aim for "just enough" nuance — structure, style, testing, boundaries — to guide agents without exceeding context windows. Break large initiatives into smaller, well-scoped specs with clear verification steps. Iterate based on where agents make mistakes.

### Continuous Feedback Loop
Feed real-world usage, incident data, and support trends back into specs. Logs of where agents misinterpret specs drive improvements to wording, examples, and acceptance criteria. Spec writing is an evolving discipline, not a one-time deliverable.
