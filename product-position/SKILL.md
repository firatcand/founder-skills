---
name: product-position
description: B2B SaaS product positioning, messaging, and differentiation advisor. Use whenever the user asks about positioning strategy, messaging hierarchy, value propositions, competitive framing, category choice, category design, strategic narratives, differentiation, ICP definition, JTBD for positioning, messaging architecture, homepage messaging strategy, or message-market fit. Trigger on "positioning", "messaging", "value prop", "how do I position", "who is this for", "category", "competitive alternative", "differentiation", "strategic narrative", "messaging matrix", "positioning doc", "audit my positioning", "review my messaging", or any request to define, refine, audit, or build positioning and messaging for a B2B SaaS product. Also trigger when the user is building a homepage, pitch deck, or sales narrative and needs upstream positioning clarity — even if they don't use the word "positioning." If someone says "my messaging isn't working" or "we sound like everyone else," this skill applies.
---

# Product Positioning & Messaging for B2B SaaS

## Purpose

Help founders and operators make sharp positioning decisions, build structured messaging hierarchies, and produce core positioning artifacts — grounded in methodologies from Dunford, Ries & Trout, Raskin, Moesta, Laja, Pierri, Lochhead, and others.

## When to use this skill

- Positioning a product from scratch or repositioning
- Auditing/critiquing existing positioning or messaging
- Building a positioning doc, messaging hierarchy, or JTBD summary
- Clarifying category choice vs. category creation decisions
- Defining competitive alternatives (including status quo / "do nothing")
- Structuring a strategic narrative (Raskin-style)
- Testing whether messaging has clarity, relevance, value, and differentiation

## Workflow

### Step 1: Diagnose the request

Determine which mode the user needs:

| Mode | Trigger | Output |
|------|---------|--------|
| **Build** | "Help me position X" / new product / repositioning | Full positioning doc + messaging hierarchy |
| **Audit** | "Review my positioning" / "why isn't this landing?" | Diagnosis with specific fixes |
| **Artifact** | "Write me a positioning doc" / "messaging matrix" | Structured deliverable |
| **Advise** | Specific question about frameworks, category, differentiation | Targeted answer with framework citation |

### Step 2: Discovery interview (Build & Audit modes)

Run a structured interview before producing anything. Ask in batches of 2-3 questions max. Cover these areas in order:

**Round 1 — Context & ICP**
- What does the product do in one sentence?
- Who are your best-fit customers today? (Role, company size, industry, situation)
- What were they doing before they found you? (Status quo, tools, manual process)

**Round 2 — Competitive alternatives & switch triggers**
- What are the real alternatives buyers consider? (Include "do nothing")
- What event or pain triggers them to look for a solution?
- What are the forces at play? (Push of current situation, pull of new solution, anxiety about switching, habit of present)

**Round 3 — Differentiation & value**
- What can your product do that alternatives cannot? (Unique capabilities)
- What workflow changes when someone adopts your product?
- What measurable outcomes do your best customers report?
- Is there a worldview or belief that drives your approach differently from competitors?

**Round 4 — Category & narrative**
- What category do buyers put you in today?
- Is that the right category, or does it set wrong expectations?
- What's the big change in the world that makes your product necessary now?

Skip questions the user has already answered. Adapt depth to context.

### Step 3: Apply frameworks

After discovery, apply the relevant frameworks from `references/frameworks.md`. Read that file before producing output.

**For positioning decisions**, follow Dunford's methodology:
1. Competitive alternatives → 2. Unique attributes → 3. Value themes → 4. Best-fit customers → 5. Category choice → 6. Positioning statement

**For differentiation**, evaluate across four lenses:
- Capability (what it uniquely does)
- Workflow (how work gets done differently)
- Outcome (what results customers achieve)
- Worldview (how the company's beliefs differ)

**For category decisions**, apply the decision rule:
- Default to **category choice** (pick a known category + subsegment) unless there is strong evidence of a genuinely new problem-solution pairing with capital and time for education.
- Only recommend **category creation** (Lochhead/Play Bigger) when the product introduces a fundamentally new way of working that existing categories cannot contain.

**For strategic narratives**, follow Raskin's 5-part structure:
1. Name the big change → 2. Winners and losers → 3. Promised land → 4. Obstacles → 5. Product as vehicle

**For message validation**, apply Laja's 4-point test:
1. Clarity — Do people immediately understand what it is?
2. Relevance — Can the right audience recognize it's for them?
3. Value — Is the value compelling enough to care?
4. Differentiation — Is it clear how this differs from alternatives?

### Step 4: Produce artifacts

This skill produces three core artifacts:

#### Artifact 1: Positioning Document (1-3 pages)
Structure:
- **ICP definition** (role, company profile, situation/trigger)
- **Competitive alternatives** (including status quo)
- **Unique attributes** (capabilities that alternatives lack)
- **Value themes** (outcomes those attributes enable)
- **Category** (chosen category + rationale)
- **Positioning statement** (concise, follows from above)
- **JTBD summary** (job, forces of progress, desired outcome)

#### Artifact 2: Messaging Hierarchy
Structure:
- **Strategic narrative** (1-paragraph "change in the world" story)
- **Core value propositions** (3-5, each with: claim, capability, proof point)
- **Persona-level messages** (by role: economic buyer, champion, end user)
- **Altitude guide** (executive = outcomes & risk; user = workflow & relief)

#### Artifact 3: JTBD Summary
Structure:
- **Job statement** ("When [situation], help me [progress], so I can [outcome]")
- **Forces diagram** (push, pull, anxiety, habit)
- **Timeline** (first thought → passive looking → active looking → deciding → onboarding → ongoing use)
- **Hiring criteria** (functional, emotional, social)

### Step 5: Handoff

When the user needs downstream execution from positioning:

| Need | Hand off to |
|------|-------------|
| Homepage copy, landing page, email copy, CTAs | `copywriter-skill` |
| Sales deck, battlecards, objection handling, discovery scripts | `sales-skill` |
| Video/podcast scripts from positioning | `script-writer-skill` |
| Cold outreach, prospecting cadences | `prospecting` |
| Channel strategy, CAC analysis | `channel-expert` |
| Pricing & packaging decisions | `pricing` |
| PLG onboarding messaging | `plg-skill` |

Explicitly tell the user: "Positioning is set — for [specific task], I'll hand off to [skill name]."

## Audit mode

When auditing existing positioning or messaging, evaluate against:

1. **Dunford completeness** — Are all 6 elements defined? (alternatives, attributes, value, customers, category, statement)
2. **Laja's 4-point test** — Clarity, relevance, value, differentiation
3. **Pierri's homepage test** — Can a stranger understand what it is, who it's for, and when they'd use it in <10 seconds?
4. **Raskin narrative check** — Does the story start from a change in the world, or does it start from the product?
5. **JTBD alignment** — Is messaging framed as customer progress, or as a feature list?

Produce a scored audit (1-5 per dimension) with specific, actionable fixes.

## Key principles (always apply)

- Positioning is a **strategic decision**, not copywriting. If the user asks for "better messaging" but has a positioning problem (unclear ICP, no category commitment, no differentiation), say so.
- Always include **"do nothing" and status quo** as competitive alternatives.
- **Category choice > category creation** for most companies. Don't recommend category creation lightly.
- Messaging must be expressed in **customer language about their progress**, not internal jargon about features.
- Every value proposition needs a **capability layer** (what users can concretely do) between features and outcomes.
- Positioning should be **cross-functional** — flag when decisions require product, sales, or leadership input, not just marketing.
