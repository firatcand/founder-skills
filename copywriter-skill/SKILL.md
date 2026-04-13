---
name: copywriter-skill
description: >
  Clarity-first copywriting skill for writing, reviewing, and editing commercial copy grounded
  in principles from Orwell, Zinsser, Hopkins, Schwartz, Ogilvy, Wiebe, Handley, and others.
  Use this skill whenever the user asks to write, draft, review, edit, critique, improve, or
  rewrite ANY commercial copy — including landing pages, hero sections, headlines, subheadlines,
  email subject lines, email body copy (cold outreach, nurture, promo, launch), CTAs, microcopy,
  product descriptions, feature/benefit messaging, value propositions, ad copy, social media copy,
  taglines, or above-the-fold messaging. Also trigger when the user asks for copy feedback, a
  copy audit, a clarity check, a conversion review, or help choosing a copywriting framework
  (AIDA, PAS, BAB, FAB, 4U's). Trigger even if the user says "write me an email" or "review
  this landing page" without using the word "copy." If the output is persuasive commercial text
  meant to drive a reader toward action, this skill applies.
---

# Clarity-First Copywriting

This skill enables two modes: **WRITE** (draft new copy) and **REVIEW** (audit and improve existing copy). Both are grounded in the same clarity-first methodology.

> **First action on trigger:** Read `references/knowledge-base.md` to load the full methodology before producing any output. The knowledge base contains the detailed principles, frameworks, and practitioner guidance that inform every decision below.

---

## Mode Detection

Determine the mode from the user's request:

| Signal | Mode |
|--------|------|
| "write," "draft," "create," "come up with" | WRITE |
| "review," "edit," "improve," "critique," "audit," "rewrite," "fix" | REVIEW |
| User pastes existing copy + asks for help | REVIEW |
| User describes a goal/audience + wants output | WRITE |
| Ambiguous | Ask: "Do you want me to draft new copy or review something you already have?" |

---

## WRITE Mode

### Step 1: Gather Context (ask if not provided)

Before writing a single word, establish:

1. **Format**: What are you writing? (landing page hero, full landing page, email, headline set, CTA, ad, product description, etc.)
2. **Audience**: Who is the reader? Be specific — role, pain, situation.
3. **Awareness stage** (Schwartz): Where is the reader on the awareness ladder?
   - **Unaware** → Must surface & name the problem
   - **Problem-aware** → Dramatize the problem, raise stakes
   - **Solution-aware** → Introduce your category/approach as the answer
   - **Product-aware** → Differentiate, prove, compare
   - **Most-aware** → Specific offer, deal, terms
4. **Goal**: What single action should the reader take?
5. **Key proof/specifics**: Numbers, results, testimonials, mechanisms — anything concrete.
6. **Voice/tone guidance**: Brand voice attributes if any; otherwise default to clear, direct, confident, warm.

If the user provides most of this, fill reasonable gaps and state your assumptions. Don't over-interrogate.

### Step 2: Select Framework

Choose the primary structural framework based on format and awareness:

| Context | Recommended Framework |
|---------|-----------------------|
| Full landing page or sales page | **AIDA** — Attention → Interest → Desire → Action |
| Pain-driven email, ad, or short page | **PAS** — Problem → Agitate → Solution |
| Case study, transformation narrative | **BAB** — Before → After → Bridge |
| Feature-heavy product page, B2B datasheet | **FAB** — Feature → Advantage → Benefit |
| Headline generation or subject line stress-test | **4 U's** — Useful, Urgent, Unique, Ultra-specific |

Frameworks can be layered: e.g., AIDA structure with PAS in the Interest section, FAB in the Desire section.

### Step 3: Draft

Apply these non-negotiable clarity rules while writing:

1. **Plain language**: Short words over long. Everyday English over jargon. Aim for ~8th grade reading level.
2. **Specificity**: Concrete numbers, named outcomes, measurable gains. "Save 3 hours/week" not "save time."
3. **One job per element**: Each page has one goal, each section one argument, each sentence one idea.
4. **Benefits over features**: Always pass the "so what?" test. Feature → Advantage → Benefit.
5. **Reader-first framing**: Every sentence answers "why should I care?" from the reader's perspective. Never "We're excited to announce…" — always "Here's how you can now…"
6. **Honest urgency**: Use urgency only when real (genuine deadlines, limited quantities). Never fake scarcity.
7. **Headline does the heavy lifting**: Ogilvy's rule — the headline spends 80 cents of your dollar. It must contain a clear benefit, identify the audience, and ideally contain news or specificity.

### Step 4: Self-Edit Before Presenting

Run these passes on your own draft before showing it:

1. **Orwell pass**: Can any word be cut? Can any long word become short? Any jargon replaced with plain English?
2. **Hopkins pass**: Would this line help a salesperson close a half-sold prospect? If not, cut or rewrite.
3. **Specificity pass**: Replace every vague claim with a concrete one. "Fast" → "in under 2 minutes." "Many" → "1,200+."
4. **Empathy pass**: Re-read as the target reader. What questions remain unanswered? What feels like corporate filler?

### Step 5: Present with Rationale

When presenting the draft:
- Briefly state the framework used and why.
- Note the assumed awareness stage.
- Flag any areas where the user's input was thin and you made assumptions.
- Offer 2–3 headline variants if writing a landing page or email (always test headlines).

---

## REVIEW Mode

### Step 1: Read the Copy

Read the user's copy carefully. Identify:
- The apparent format (email, landing page, ad, etc.)
- The apparent target audience
- The apparent awareness stage
- The apparent goal / primary CTA

### Step 2: Score Against Clarity Dimensions

Rate each dimension 1–5 and provide a one-line rationale:

| Dimension | What to evaluate |
|-----------|-----------------|
| **Clarity** | Can an 8th grader understand the core message? Is jargon absent or explained? |
| **Specificity** | Are claims concrete and measurable? Numbers, names, timeframes present? |
| **Benefit focus** | Does copy answer "so what?" or does it feature-dump? |
| **Reader empathy** | Is it written from the reader's perspective or the company's? |
| **Structure** | Does each section have one job? Is the framework coherent (AIDA, PAS, etc.)? |
| **CTA strength** | Is the action clear, specific, and low-friction? Supportive microcopy present? |
| **Headline/hook** | Does the headline sell a benefit, identify the audience, create interest? |
| **Trust signals** | Is proof specific and placed near decision points? Any empty superlatives? |
| **Tone alignment** | Does the tone match the audience and context? Conversational or stiff? |
| **Economy** | Could anything be cut without losing meaning? Any clutter or filler? |

### Step 3: Identify Anti-Patterns

Flag any of these explicitly:

- **Jargon/vagueness**: Abstract corporate language hiding weak positioning
- **Clever-over-clear**: Wordplay that obscures the offer or benefit
- **Feature dumping**: Lists of features without benefits
- **Self-focused framing**: "We're excited…" instead of reader-value framing
- **False urgency**: Fake countdowns, invented scarcity, unsupported superlatives
- **Structural confusion**: Competing CTAs, unclear page goal, awareness mismatch
- **Message dissonance**: Hero/headline doesn't match where traffic comes from

### Step 4: Rewrite Recommendations

For each issue found:
1. Quote the problematic line or section.
2. Name the principle being violated (with attribution where natural, e.g., "Orwell's cut-the-word rule" or "Hopkins's salesperson test").
3. Provide a rewritten alternative.

### Step 5: Present the Review

Format the review as:
1. **Quick verdict** — 1–2 sentences summarizing overall impression.
2. **Scorecard** — The dimension table with scores and rationale.
3. **Top 3 priorities** — The highest-impact changes, ranked.
4. **Detailed rewrites** — Line-by-line fixes for priority issues.
5. **What's working** — Acknowledge strengths. Not everything needs fixing.

---

## Headline Generation

### Headline Quality Rules

- **Active voice, strong verbs.** Prefer "Stop losing client feedback in email threads" over "Client feedback is often lost across email threads." The subject should act, not be acted upon.
- **No filler openers.** Avoid "Introducing," "Discover," "Unlock," "Welcome to." Lead with the benefit, the pain, the number, or the audience.
- **One core idea per headline.** A headline can have texture and rhythm, but it should serve one argument. Two ideas weakens both.
- **Aim for 5–12 words.** Long enough to carry meaning and personality. Short enough to scan in a glance. Over 15 words is a sign you're explaining, not headlining.
- **Personality welcome.** Headlines can use rhythm, contrast, quoted phrases, and specifics to create voice — as long as clarity comes first. A headline with character beats a headline that's merely short.

### Process

1. Generate **5–8 variants** spanning different approaches:
   - **Benefit-first (Ogilvy style)**: "Reconcile invoices in minutes, not days."
   - **Problem-forward (PAS)**: "Stop losing client feedback in email threads."
   - **How-to**: "How to manage 5 client projects without drowning in email."
   - **Numbered/specific**: "3 revision rounds. 47 emails. 0 clarity."
   - **Curiosity + clarity**: "'Which version are we on?' — the last time you'll ask."
   - **Audience-identified**: "Freelance designers: your feedback workflow is broken."
   - **Contrast/tension**: "Every revision request, every note, one place."

2. Score each headline against the **4 U's**: Useful? Urgent? Unique? Ultra-specific? (Mark ✓/✗ for each)

3. Recommend a top pick and a runner-up with rationale.

---

## Email-Specific Guidance

When writing email copy:

- **Subject line**: Clear > clever. Benefit-focused. Test with 4 U's. Offer 3+ subject line variants.
- **Opening**: Write as if to one specific person. No "Dear valued customer." Start mid-conversation.
- **Body**: One main idea. One primary CTA. Use PAS or AIDA structure.
- **CTA**: Explicit verb + benefit. "Download the playbook" not "Click here." Add friction-reducing microcopy ("Takes 2 minutes," "No credit card required").
- **Cold outreach**: Extra brevity. Reference a specific trigger (funding round, job post, content they published). Speak to their problem, not your product. Empathy over pitch.
- **Nurture**: Can use more storytelling. Each email must deliver standalone value. Respect permission (Godin's principle).

---

## Quick Reference: Core Principles

These principles override any framework or formula when in conflict:

1. **Clear beats clever** — If a reader has to decode the message, it fails.
2. **Specific beats vague** — Concrete > abstract, always.
3. **Reader > writer** — Every sentence must serve the reader's interest.
4. **One job per element** — Page, section, sentence, button: one purpose each.
5. **Cut, then cut more** — If a word can go without losing meaning, it goes.
6. **Benefits > features** — "So what?" is the reader's constant silent question.
7. **Test, don't guess** — Hopkins's core rule. Offer variants. Recommend A/B testing.
8. **Match awareness to depth** — Don't feature-dump on unaware prospects. Don't stay vague with product-aware buyers.
9. **Proof near decisions** — Social proof, testimonials, and specifics belong adjacent to CTAs and pricing.
10. **Rewrite is where it happens** — First drafts are raw material. Editing is the craft.

---

## Reference

For deep-dive principles, framework details, practitioner examples, headline formulas, editing checklists, and anti-pattern analysis, read:

→ `references/knowledge-base.md`

This file contains the full clarity-first copywriting knowledge base covering: foundations of clear writing, commercial application, AIDA/PAS/BAB/FAB/4U's frameworks, Ogilvy's headline principles, Schwartz's awareness stages, Wiebe's conversion methodology, landing page structure, email copy, product messaging, voice/tone, editing heuristics, and common failures.
