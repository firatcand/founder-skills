---
name: prompt-architect
description: >
  Expert prompt engineering skill for writing, critiquing, rewriting, comparing, and templating LLM prompts.
  Use this skill whenever the user wants to: write a new prompt from scratch, improve or fix a weak or vague prompt,
  critique an existing prompt with scores and diagnosis, compare multiple prompt variants, build a reusable prompt
  template, or reason about why a prompt fails. Also trigger for requests like "make this prompt better",
  "why isn't this working", "write a system prompt for X", "A/B compare these two prompts", or any task
  involving prompt quality, output reliability, or prompt structure — especially for voice AI agents,
  automation pipelines, and developer tools. This skill encodes the Prompt Architect 3.0 methodology.
---

# Prompt Architect

A prompt is a **behavior-specification artifact written in natural language**. Treat every request as both an
engineering task (inputs, instructions, constraints, outputs) and a language task (intention expressed with
precision, economy, and zero ambiguity).

---

## Step 1 — Detect Mode

Classify the request before doing anything else. Do not mix modes.

| Mode | Trigger | Action |
|---|---|---|
| **Generate** | User states a goal; no prompt exists | Interview if needed → draft → deliver |
| **Critique** | User submits a prompt for review | Score → diagnose → rewrite |
| **Rewrite** | User submits a weak/broken prompt | Identify failures → rewrite → explain delta |
| **Compare** | User presents multiple variants | Evaluate each → recommend one → justify |
| **Template** | User wants a reusable structure | Parameterize → add placeholders → annotate |

When mode is ambiguous, state your assumption and proceed.

---

## Step 2 — Ask Format Before Producing Output

**Always ask the user their preferred output format before delivering the final prompt, unless they have already specified it in the current request.**

> "Would you prefer the prompt in **Markdown** or **XML**?"

Ask every time. Do not assume the previous answer carries over.

---

## Step 3 — Interview (Generate mode only)

Ask only what is unanswered. Stop when all four are resolved.

1. **Goal** — What must the prompt make the model do? What does success look like?
2. **Audience** — Who consumes the output: a human, a system, another model?
3. **Output format** — Structure, length, schema, tone?
4. **Constraints** — What must the model never produce, assume, or omit?

If all four are clear from context, draft immediately. Do not perform process theater.

---

## Step 4 — Apply the Five Capabilities

Run all five lenses on every prompt you produce or review.

### 1. Semantics — Ambiguity Detection & Word Precision
- Identify any instruction that supports more than one interpretation
- Replace abstract verbs ("improve", "analyze", "make better") with concrete deliverables
- Flag hedged language that creates ambiguity under inference (e.g. "as needed", "if relevant", "appropriately")
- Ensure wording captures what the user *means*, not just what they wrote

### 2. Logic & Task Decomposition
- Break complex prompts into sequential, prioritized steps
- Identify implicit dependencies (step B assumes output from step A)
- Eliminate contradictory instructions
- Add explicit ordering only when sequence affects correctness

### 3. Communication / Rhetoric
- Specify tone explicitly — never let register drift to default "assistant voice" unless intended
- Match structure to audience: human reader vs. downstream model vs. automated system
- Adjust verbosity: strip ceremony for system-to-system prompts; add context scaffolding for human-facing ones
- Apply economy: every sentence must earn its place

### 4. Analytical / Variant Reasoning (A/B Logic)
When comparing or proposing variants:
- Draft two distinct versions that differ on a **single meaningful axis** (tone, structure, constraint framing, CoT vs. direct)
- Reason explicitly about which would perform better and why — consider: output consistency, failure mode exposure, over-compliance risk
- Name the tradeoff each variant makes
- Recommend one, with a stated assumption it's based on
- Do not execute: reason about expected behavior, then let the user validate

### 5. Constraint Enforcement
Apply these two guardrails to every prompt produced:

**Hallucination prevention** — eliminate:
  - Vague anchors ("recent", "standard", "best practice") without grounding
  - Instructions that invite the model to invent missing information
  - Open-ended tasks with no fallback behavior when information is absent
  - Scope overload (too many goals in one prompt → model fills gaps with guesses)

**Scope limits** — do not over-engineer:
  - No chain-of-thought unless the task requires multi-step reasoning
  - No roles/personas unless they measurably change output behavior
  - No extra sections unless they carry behavioral value
  - Simple prompts get simple treatment

---

## Step 5 — Run Checklists

### Engineering Checklist (7 criteria)
| Criterion | Verify |
|---|---|
| Goal clarity | Task is unambiguous; success is defined in concrete terms |
| Context sufficiency | Nothing required is left to inference; no irrelevant noise |
| Instruction precision | Instructions are explicit, ordered by priority, non-contradictory |
| Output definition | Format, length, depth, and schema are fully specified |
| Constraint coverage | Failure modes, scope limits, tone, exclusions are bounded |
| Failure resistance | Vague anchors, hallucination traps, overloaded scope eliminated |
| Portability | Works across model families unless a specific model is named |

### Language Checklist (6 criteria)
| Criterion | Verify |
|---|---|
| Ambiguity | No instruction supports multiple interpretations |
| Intention fidelity | Wording captures what the user means, not just what they wrote |
| Register | Tone is explicit; no unintended social register introduced |
| Semantic precision | Abstract verbs replaced with concrete deliverables |
| Pragmatics | Model will not over-comply, under-specify, or misread emphasis |
| Economy | Every sentence earns its place; decorative language removed |

---

## Step 6 — Score (Critique & Rewrite modes)

Score on both dimensions. Commit to a number. Do not hedge.

| Dimension | What you measure |
|---|---|
| **Clarity & intent alignment** | Does the wording unambiguously express the intended behavior? Would a different model interpret it identically? |
| **Output predictability** | Does the prompt constrain the response space enough to produce consistent outputs across runs? |

Score each **1–5**. Name the single weakest point per dimension. Fix lowest score first.

---

## Output Structure

Use the structure that matches the mode.

### Generate / Rewrite
```
## Assumptions  *(state only if not given)*
## Prompt
## Why this works  *(2–4 sentences: one engineering reason, one language reason)*
## Variant  *(only if the user explicitly requests an alternative)*
```

### Critique
```
## Scores  Clarity N/5 · Predictability N/5
## Engineering issues  *(named and specific)*
## Language issues  *(named and specific)*
## Improved prompt
## What changed and why
```

### Compare
```
## Recommendation
## Best option and why it wins
## Weaknesses of each other option
## Final improved version
```

### Template
```
## Template
## Placeholders  *(name, type, and guidance for each)*
## Usage example
```

---

## Hard Rules

- Do not over-engineer simple prompts
- Do not add chain-of-thought unless multi-step reasoning is required
- Do not assume a model family unless the user names one
- Do not add roles, steps, or sections unless they measurably improve performance
- Do not preserve bad wording merely because the user used it first
- Do not rewrite away the user's real intention
- State every assumption explicitly
- Never conceal a tradeoff
- Never use vague approval like "this is good" without stating *why*
- Do not ask for clarification when a reasonable assumption produces an adequate result

---

## Reference

For deeper methodology, see `references/prompt-architect-3.0.md` — the full Prompt Architect 3.0 source document.
Load it when: handling edge-case scoring decisions, explaining methodology to a user, or running a deep critique.
