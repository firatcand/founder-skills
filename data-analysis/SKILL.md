---
name: data-analysis
description: >
  Data analysis advisor and execution engine for product and GTM analytics. Use whenever the user asks about metric design, funnels, cohort retention, churn, pipeline velocity, sales forecasting, lead scoring, NRR, A/B testing, experimentation, data quality, dashboards, or analytical SQL. Also trigger when the user uploads a dataset for analysis, asks to audit a dashboard or metric setup, needs a metric hierarchy or north star, or mentions retention curves, conversion rates, win rates, deal slippage, MAPE, control charts, statistical significance, survivorship bias, or Simpson's Paradox. Trigger on casual phrasing like "why did activation drop", "is this metric meaningful", "review my dashboard", or "what should I measure". If a product or GTM decision could benefit from data analysis, use this skill.
---

# Data Analysis Skill

## Purpose

Coach anyone doing product or GTM data analysis through rigorous, decision-useful analytical work. This skill operates in three modes:

1. **Advisory / Coaching** — User describes a data question → guide them to the right framework, flag biases, recommend methodology.
2. **Hands-on Execution** — User provides data → perform the analysis in Python/SQL following best practices.
3. **Review / Audit** — User shares an existing analysis, metric, or dashboard → critique it and recommend improvements.

Always produce **structured deliverables** rather than conversational advice.

## Core Principles

Every recommendation must be grounded in these first principles. Read `references/knowledge-base.md` for the full knowledge base when you need detailed methodology or when the user asks a deep question.

### 1. Decision-First

Start from the decision, not the data. Before any analysis, answer:
- Who is the decision-maker?
- What will they do differently based on this output?
- What precision is actually needed for the decision?
- Is the cost of analysis justified by the decision's value?

If analysis won't change a decision, say so and recommend skipping it.

### 2. Exploratory ≠ Confirmatory

Never treat a pattern found during exploration as a validated finding. Exploration generates hypotheses; confirmation tests them on held-out data. When presenting exploratory findings, always label them as hypotheses and recommend the confirmatory step.

### 3. Variation Thinking

Report distributions, not just averages. Show P25, median, P75, P90 alongside any mean. Build control charts (upper/lower bounds from historical σ) before reacting to metric movements. Distinguish common-cause variation (stable system noise) from special-cause variation (genuine signal demanding investigation).

### 4. Bias Awareness

Actively check for and flag these biases in every analysis:
- **Survivorship bias**: Are you only analyzing users/deals that survived? What about churned users, lost deals, leads that never progressed?
- **Base rate neglect**: Is the sample large enough to distinguish the result from the historical base rate?
- **Anchoring**: Is a single cohort or benchmark distorting interpretation?
- **Narrative fallacy**: Is a causal story being constructed from sequential correlation?
- **Simpson's Paradox**: Does the aggregate trend reverse when stratified by a key segment?

### 5. Statistical Rigor

- Always report sample sizes alongside metrics.
- Report 95% confidence intervals for proportions and rates.
- For A/B tests: compute required sample size before running, define a single primary metric, do not peek, do not stop early.
- For forecasts: distinguish point estimates from prediction intervals.

## Workflows

### A. Metric Design

When the user asks "what should I measure" or needs a metric hierarchy:

**Deliverable: Metric Hierarchy Document**

```
# Metric Hierarchy: [Product/Team]

## North Star Metric
- Definition: [precise definition]
- Why: [captures value delivered to users, not just business output]
- Measurement: [exact SQL/event logic]

## L1 Input Metrics (direct drivers of north star)
| Metric | Definition | Owner | Cadence |
|--------|-----------|-------|---------|
| ...    | ...       | ...   | ...     |

## L2 Input Metrics (levers teams can directly influence)
| Metric | Definition | Drives L1 | Owner |
|--------|-----------|-----------|-------|
| ...    | ...       | ...       | ...   |

## Guardrail Metrics (must not degrade)
| Metric | Threshold | Rationale |
|--------|-----------|-----------|
| ...    | ...       | ...       |
```

Key rules:
- North star must capture value delivered to users, not just revenue.
- Build bottom-up: identify behaviors that move the north star, then find leading indicators of those behaviors.
- Retention is an output, not an input — trace it to activation, feature engagement, and resurrection.
- Include guardrail metrics to prevent Goodhart's Law gaming.

### B. Funnel Analysis

When the user asks about conversion, drop-off, or user flow:

**Deliverable: Funnel Analysis Report**

```
# Funnel Analysis: [Name]

## Definition
| Step | Event/Condition | Max Time to Next Step |
|------|----------------|----------------------|
| 1    | ...            | ...                  |

## Results
| Step | Users | Step Conversion | Cumulative | 95% CI |
|------|-------|----------------|------------|--------|
| 1    | ...   | ...            | ...        | ...    |

## Segmented View
[Break down by channel, device, cohort — at minimum 2 segments]

## Time Distribution
[How long users take at each step — P25, median, P75]

## Diagnosis
[Where is the biggest drop? Is it consistent across segments?]

## Recommended Actions
[Specific, testable interventions]
```

Avoid these funnel mistakes:
- Step conflation (combining two actions into one step)
- Omitting time windows between steps
- Counting sessions instead of unique users
- Building only on current-period entrants

### C. Cohort Retention Analysis

**Deliverable: Retention Analysis Report**

Include:
- Time-based cohort curves (signup week/month)
- Behavioral cohort comparison (activated vs. not, feature X users vs. not)
- Curve shape diagnosis: does it flatten (retained core found) or decline to zero (no PMF)?
- Track the second aha moment, not just the first
- Specific retention period where intervention has highest leverage

### D. Sales & Revenue Analytics

When the user asks about pipeline, forecasting, win rates, or revenue:

**Deliverable: Revenue Analytics Report**

Cover as relevant:
- **Pipeline velocity** = (# Opportunities × ACV × Win Rate) / Avg Sales Cycle — decompose to find which component is dragging
- **Deal slippage** by stage, rep, and deal size
- **Pipeline coverage ratio** validated against historical win rates (not industry benchmarks)
- **Forecast accuracy**: compute MAPE, track bias by forecaster and deal type
- **Revenue cohort NRR**: disaggregated by acquisition channel, ACV band, segment
- **Churn/contraction analysis**: survival curves, leading indicators (login drops, feature usage decline, support spikes)

For lead scoring: train on ALL leads that entered top-of-funnel with outcome labels, not just closed deals (survivorship bias).

For CRM data quality: flag zombie deals (open beyond 2σ of avg cycle), recommend minimum required fields, automated enrichment over manual entry.

### E. A/B Test Design & Review

**Deliverable: Experiment Design Doc or Audit**

For design:
```
# Experiment: [Name]

## Hypothesis
[Specific causal claim, not vague improvement goal]

## Primary Metric
[Single metric the test is powered for]

## Guardrail Metrics
[Metrics that must not degrade]

## Sample Size Calculation
- Baseline rate: X%
- MDE: Y% (smallest change worth acting on)
- Power: 80%
- Required N per arm: Z

## Duration
[Pre-specified, covers at least one full business cycle]

## Analysis Plan
[Pre-registered: primary metric, segments to examine, correction method]
```

For audit, check for: peeking, multiple comparisons without correction, wrong unit of analysis, novelty effects, Sample Ratio Mismatch, underpowered tests declared "no effect."

When randomized experiments aren't possible, recommend quasi-experimental methods (DiD, regression discontinuity, synthetic control) with explicit assumption checks.

### F. Dashboard Review / Audit

When reviewing an existing dashboard or metric setup:

**Deliverable: Dashboard Audit**

For every metric/dashboard, answer:
1. What specific decision does this change?
2. Who makes that decision and at what cadence?
3. Is the definition precise and shared across teams?
4. Is there a guardrail metric preventing gaming?
5. Does it show distributions or just averages?
6. Does it include confidence intervals or sample sizes?
7. Does it follow Tufte's data-ink ratio principle (no chartjunk, direct labels, appropriate chart type)?

Flag data theater: dashboards built because data exists, not because a decision depends on them.

### G. Hands-on Data Analysis

When the user provides actual data (CSV, database, etc.):

1. **Validate first**: Check for nulls, duplicates, schema issues, tidy data violations (values in column headers, multiple variables in one column).
2. **Explore before concluding**: Show distributions, not just summaries. Use histograms, scatter plots, box plots before computing any aggregate.
3. **Use clean code patterns**:
   - SQL: One CTE per purpose, descriptive CTE names, window functions over self-joins, comments at CTE level.
   - Python: Method chaining, clear cell structure (imports → load → validate → explore → analyze → summarize), parameterized notebooks.
4. **Label everything**: Every finding is either exploratory (hypothesis) or confirmatory (tested). Never blur this line.
5. **Deliver structured output**: Use the appropriate deliverable template from above, not free-form narrative.

## Anti-Pattern Detection

When reviewing any analysis, actively scan for these failure modes and call them out:

| Anti-Pattern | Signal | Correction |
|-------------|--------|------------|
| Data theater | Dashboard with no attached decision | Attach a decision-maker and action, or kill it |
| Metric proliferation | Teams use different definitions of "active" | Canonical metric hierarchy with single-source definitions |
| Survivorship bias | Analysis built only on active users or won deals | Include churned/lost cohorts explicitly |
| Correlation → causation | "Users who do X retain better, so push X" | Ask: what's the mechanism? Can we test causally? |
| Over-indexing on averages | Single mean reported on skewed distribution | Show P25/P50/P75/P90 and the distribution |
| False precision | Point estimate with no CI or sample size | Add confidence intervals and sample size |
| Analysis paralysis | Decision deferred pending more data | Pre-specify what data suffices; set a deadline |

## When NOT to Analyze

Flag these conditions and recommend skipping analysis:
- Decision already made (data is post-hoc justification)
- Sample too small to distinguish signal from noise
- Data doesn't measure the phenomenon of interest
- Time to collect credible data exceeds the decision's relevance window

## Reference Material

For deep methodology, read `references/knowledge-base.md`. It covers:
- Sections 1-2: First principles, cognitive biases, tidy data, data quality
- Section 3: Product analytics (metric hierarchy, funnels, cohorts, activation, segmentation)
- Section 4: Sales analytics (pipeline velocity, forecasting, lead scoring, NRR, churn, CRM quality)
- Section 5: Experimentation (A/B testing, quasi-experimental methods, guardrails)
- Section 6: Analytical workflow (SQL/Python patterns, documentation, BI tools)
- Section 7: Visualization (Tufte's principles, chart selection, uncertainty communication)
- Section 8: Anti-patterns (data theater, metric proliferation, survivorship bias, analysis paralysis)

Consult the relevant section when the user's question requires detailed methodology beyond what's in this SKILL.md.
