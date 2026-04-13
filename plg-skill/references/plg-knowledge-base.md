# PLG Knowledge Base

## Table of Contents
1. [Definitions & Evolution](#1-definitions--evolution)
2. [Free Access Models](#2-free-access-models)
3. [Onboarding, Activation & Aha Moments](#3-onboarding-activation--aha-moments)
4. [PQLs, Viral Loops & Conversion](#4-pqls-viral-loops--conversion)
5. [PLG vs Sales-Led vs Hybrid](#5-plg-vs-sales-led-vs-hybrid)
6. [When PLG Works and Fails](#6-when-plg-works-and-fails)
7. [Metric Stack: Acquisition & Activation](#7-metric-stack-acquisition--activation)
8. [Metric Stack: Conversion, Expansion & Retention](#8-metric-stack-conversion-expansion--retention)
9. [Cohort Analysis](#9-cohort-analysis)
10. [Future Directions](#10-future-directions)

---

## 1. Definitions & Evolution

**Core definition (OpenView/Bartlett 2016):** PLG is a go-to-market strategy where the product itself acts as the primary driver of acquisition, retention, and expansion — replacing traditional sales and marketing as the central GTM engine.

**End-user era:** Employees evaluate tools the way they evaluate consumer apps — by signing up and trying them instantly. PLG funnels are defined by organic discovery, self-serve signup, in-product activation, and free-to-paid conversion, not MQL volume or SDR capacity.

**Operating model, not tactic:** PLG fuses product and revenue cross-functionally. Features are built to create usage patterns that sales can monetize. Sales teams are fed by product telemetry (usage, account health, PQL signals) instead of cold outbound. Result: higher revenue per employee, better Rule of 40/50 performance, more automated growth.

---

## 2. Free Access Models

### Freemium
- Permanently free tier with limited features/usage
- Works when free users generate strategic value: network effects, viral sharing, brand ubiquity
- Design principles: free must be genuinely valuable alone; limits should be natural (message history, storage, seats); upgrade paths obvious when teams outgrow constraints
- Exemplars: Slack, Dropbox, Zoom, Canva

### Free Trial
- Full-feature access for limited time (7–30 days)
- Better for products requiring meaningful setup/experimentation to show value, or higher ACV products
- Converts at higher rates than freemium (mid-teens to high-twenties %) because users are more intent-driven

### Reverse Trial
- Start every signup on premium tier, downgrade to free after time limit
- Combines freemium's engagement with trial's conversion pressure
- Creates fear-of-loss around premium features
- Exemplars: Loom, Asana, Airtable
- Only works with strong instrumentation to understand which premium features drive PQL status

### Decision Framework
| Factor | → Freemium | → Free Trial | → Reverse Trial |
|--------|-----------|-------------|-----------------|
| Market size | Large, horizontal | Niche or vertical | Either |
| Viral potential | Strong | Weak | Either |
| Value clarity | Immediate for individuals | Requires setup/exploration | Premium features need exposure |
| ACV | Lower | Higher | Either |
| Network effects | Strong | Weak | Either |

---

## 3. Onboarding, Activation & Aha Moments

### Self-Serve Onboarding
Replaces education, demo, and configuration work that human sales/implementation teams perform. Narrows the path from signup to a clearly defined activation event.

### Activation Rate
- % of new signups reaching an "aha moment" within a given time window
- Single most important PLG metric: everything upstream is wasted if users don't activate; everything downstream depends on it
- Target: roughly 25%+ of signups (varies by complexity)
- Must be defined behaviorally: "created a project and invited teammates", "sent first campaign", "shared a file across devices"

### Time-to-Value (TTV)
- Time between signup and activation
- Shorter TTV → higher conversion and retention
- Users who activate within Day 1 convert at significantly higher rates than those taking several days
- Reduce via: default configurations, templates, integrations, progressive disclosure

### Case Study: Slack
- Free tier: full core functionality, 10K message searchable history, restricted integrations
- Typical team hits message limit 1–3 months after adoption
- By that point Slack is embedded in workflows → loss of history is a powerful upgrade trigger

### Onboarding Patterns
- **Progressive disclosure**: show only the next necessary step; introduce secondary features later via behavior-based nudges
- **In-app guides**: checklists, contextual tooltips focused on minimum actions for value
- **Experimentation**: A/B test signup flows, templates, defaults — treat onboarding as revenue-critical

---

## 4. PQLs, Viral Loops & Conversion

### PQL vs MQL vs SQL
| Lead Type | Defined By | Signal Source | Typical Conversion |
|-----------|-----------|---------------|-------------------|
| MQL | Marketing touchpoints (content, ads, webinars) | Marketing automation | Lower |
| PQL | In-product behavior + usage thresholds | Product analytics | Higher (often multiples of MQL) |
| SQL | Sales-vetted for fit, budget, timing | CRM / sales team | Highest |

### PQL Scoring
Combine: feature usage, frequency, recency, breadth of users in account, firmographic fit (company size, industry, role). Feed into CRM/product-led sales tooling. ~25% of SaaS companies use PQLs; those that do see materially higher free-to-paid conversion.

### Viral Loops
- **Slack**: users invite colleagues into channels
- **Calendly**: scheduling links expose new users at moment of need
- **Figma**: shared design files and team libraries
- Each active user becomes a distribution node → flywheel with freemium access

### Conversion Triggers
Effective triggers are **natural extensions of value**, not arbitrary walls:
- Hitting message/storage limits
- Needing more seats
- Requiring SSO/governance/admin controls
- Accessing advanced analytics or integrations
- Pricing/packaging should align monetization with value realization

---

## 5. PLG vs Sales-Led vs Hybrid

### Funnel Differences
- **Sales-led**: Traffic → MQLs → SDR-worked opportunities → customers (before product is meaningfully touched)
- **PLG**: Visitors → self-serve signup → product usage/activation → PQLs → opportunities (product usage is the central gating function)
- **Hybrid**: Multiple on-ramps (self-serve, demo, sales contact) with product usage qualifying and prioritizing enterprise outreach

### Unit Economics
PLG companies often show: lower CAC, shorter CAC payback, higher revenue multiples, stronger Rule of 40. Growth is more automated and less headcount-constrained. But PLG is not immune to macro headwinds — NDR has compressed across the board.

### Hybrid in Practice
Most scaled PLG companies evolve into hybrid. Examples:
- **Datadog**: Self-service developer PLG + large direct sales force for multi-product enterprise
- **Slack/Zoom/Calendly**: Bottoms-up virality seeds accounts → enterprise sales once strong in-account champions and usage data exist
- McKinsey calls this "product-led sales" — sales works from product telemetry, not cold leads

### When Sales-Led Remains Better
- Complex products requiring deep solution selling
- Multi-stakeholder procurement navigation
- Value only apparent through tailored configuration or integration
- Organization-wide process change needed before value is visible
- Can still add PLG elements: in-app trials, guided sandboxes, self-serve add-ons post-sale

---

## 6. When PLG Works and Fails

### Conditions Favoring PLG
- Easy to adopt without extensive implementation
- Clear value to individual end users (not just executives)
- Broad, horizontal use cases
- Large addressable user base
- Low marginal cost to serve
- Strong network/collaboration effects
- Examples: collaboration tools, developer tools, SMB SaaS

### Where PLG Struggles
- Complex integrations / lengthy setup required
- Organization-wide process changes needed before value visible
- Legacy vertical software, highly regulated industries
- Bespoke enterprise deployments
- Narrow markets where free tier cannibalizes monetizable demand

### Common Failure Modes
1. **No upgrade triggers**: Large free populations that never convert, consuming support resources
2. **No product-market fit**: Expecting "the product sells itself" without investing in messaging, onboarding, analytics
3. **Organizational silos**: Usage data never informs GTM; PQLs neither defined nor operationalized
4. **Shallow PLG bolted on**: Incumbents adding trivial trials without cultural/architectural change
5. **Over-generous free tier**: In narrow markets, giving away too much cannibalizes revenue

### PLG as Competitive Weapon
PLG-first entrants disrupt incumbent sales-led vendors via lower friction and usage-based pricing (Datadog vs legacy monitoring, Figma vs traditional design software). Once teams adopt a better self-serve product, enterprise deals can follow top-down.

---

## 7. Metric Stack: Acquisition & Activation

### Natural Rate of Growth (NRG)
- Formula: Annual ARR growth rate × % organic signups × % new ARR from product (no sales)
- Measures how much growth comes "for free" from the PLG engine
- Benchmarks (sub-$10M ARR): NRG > 150% is world-class; lower targets for larger companies
- High NRG = strong PMF + viral/referral growth
- Low NRG despite high overall growth = overdependence on paid channels

### Activation Rate
- North-star early funnel metric
- Target: ~25%+ of signups (varies)
- Define behaviorally at person AND account level
- Track by cohort to see improvement over time

### Time-to-Value (TTV)
- Leading indicator of conversion and retention
- Goal: value within minutes for simple products, hours for complex ones
- Day-1 activators convert at significantly higher rates

---

## 8. Metric Stack: Conversion, Expansion & Retention

### Free-to-Paid Conversion
- Free trials > freemium in conversion rate
- PQL-based outreach drives multiples higher conversion vs non-PQL
- Top quartile PLG: low teens % overall, substantially higher for PQL-flagged accounts
- Don't chase universal "good" numbers — focus on cohort-level consistency and trends

### Net Dollar Retention (NDR / NRR)
- Captures expansion + contraction + churn on existing revenue
- NDR > 100% = growth from existing base alone
- Exemplars: Snowflake, Figma with NDR well above 120%
- NDR > 120% is the clearest signal of a healthy PLG business

### Expansion Revenue
- Upsells, cross-sells, seat/usage growth from existing customers
- Often eclipses new-customer ARR at scale
- Track by cohort: seats per account, modules adopted, expansion MRR, upgrade events

### CAC Payback
- PLG companies historically show meaningfully shorter CAC payback than sales-led peers
- Higher ARR per employee = capital efficiency signal
- Recent pressure on NDR/growth, but investor emphasis on efficient PLG motions continues

### Product-Led Sales Metrics
- PQL volume, PQL-to-opportunity conversion, win rates vs MQL/outbound-sourced
- Well-defined PQLs dramatically improve sales productivity
- Shift dashboards from top-of-funnel marketing metrics → product-centric KPIs

---

## 9. Cohort Analysis

### Why Cohorts Matter
- Reveal retention, conversion, expansion patterns that aggregate metrics obscure
- Essential for disentangling acquisition vs onboarding vs customer mix improvements
- Investors expect cohort-based charts for activation, retention, NRR in board decks

### Core Cohort Cuts
- **Acquisition channel**: Organic vs paid vs viral signups
- **Plan type**: Free vs trial vs paid
- **Segment**: SMB vs midmarket vs enterprise
- **Activation event**: Cohort by first activation rather than raw signup for cleaner signals

### What to Track by Cohort
- Retention curves: Day 7, 30, 90 (user activity); monthly/annual (revenue)
- Gross retention vs NRR/NDR (separate to see expansion contribution)
- Expansion: seats per account, modules adopted, expansion MRR, time-to-upgrade

### Instrumentation Requirements
- Event-based analytics (Amplitude, Mixpanel, Heap)
- CDPs + data warehouses for unified user-account-revenue views
- Integration between product analytics, CRM, and billing
- Without this: can't define activation rigorously, measure NRG, or attribute expansion to product behaviors

---

## 10. Future Directions

### Post-Hype PLG
- NDR declining across PLG and traditional SaaS; valuations compressed
- Focus shifting from "growth at all costs" to profitability, ARR/FTE, disciplined experimentation
- More skepticism about free tiers that don't contribute to monetization

### Product-Led Sales as Default
- Future is hybrid: human sales working from product telemetry, not cold leads
- Open questions: org design, compensation models, making usage data actionable for reps
- Datadog as exemplar of strong PLG metrics + robust enterprise sales

### AI-Native PLG
- New patterns: interactive sandboxes, usage-based free credits, in-product copilots
- Traditional seat-based freemium less relevant than usage metering
- Challenge: balancing experimentation, infrastructure cost, and upgrade value

### Where It's Heading
- Beyond binary "PLG vs sales-led" toward coordinated growth systems
- Usage data → lifecycle orchestration (onboarding, upsell nudges, sales outreach)
- Monetization aligned with realized product value
- Adaptive, data-rich GTM engines where free access, self-serve, and sales work from a common product-centric source of truth
