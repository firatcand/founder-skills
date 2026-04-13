# Benchmarks, Timelines & Metrics

## Google's Core Ranking Signals (2025–2026)

Five pillars — weakness in any one creates drag on the others:

1. **Content quality & topical relevance** — dominant signal. Intent-understanding models evaluate whether page satisfies meaning behind query. Topical authority (depth + consistency across a topic area) is a first-class signal.
2. **Backlinks** — primary off-page authority signal. Top positions have 3.8x more backlinks than bottom-half page 1. Emphasis shifted from quantity to relevance and topical alignment.
3. **Technical health** — crawlability, Core Web Vitals, mobile-first indexing. Acts as a floor.
4. **User experience signals** — CTR, dwell time, scroll depth. Behavioral feedback that can re-rank results (NavBoost-type logic).
5. **E-E-A-T** — not a direct factor but qualities Google's systems detect. After Dec 2025 Core Update: generic content farms -60% traffic; sites with demonstrable expertise +23%.

Anti-pattern: treating these as independent checkboxes. Must be present across all.

## AI Search Market Data (2025–2026)

- AI search engines handle ~15% of global search queries, 2B+ searches/month
- Perplexity alone: 780M queries in May 2025
- Only 11% of domains cited by both ChatGPT and Perplexity
- Pages with clean heading hierarchy + aligned schema → 2.8x higher AI citation rates

## Zero-Click Search Data

- 80% of consumers rely on zero-click results in ≥40% of their searches
- Only ~40.3% of U.S. Google searches ended in an organic click (Q1 2025), down from ~44.2% prior year
- Accelerating on mobile — AI Overviews satisfy intent so completely users skip follow-up queries
- Zero-click disproportionately affects informational/TOFU queries
- Commercial and transactional queries continue to drive clicks (users need to validate before purchasing)

## SEO Timeline Expectations

| Period | Expected Outcomes | If Not Happening |
|---|---|---|
| Months 1–2 | Pages indexed, GSC impressions starting | Check robots.txt, submit sitemap, fix indexing errors |
| Months 3–4 | Long-tail rankings appearing (positions 20–50) | Check content quality, add internal links, verify schema |
| Months 4–6 | First page-1 rankings on very long-tail; organic traffic > 0 | Content audit: are target pages matching intent? |
| Months 6–12 | Measurable organic traffic, first BOFU conversions | If flat, audit link profile — may need more authority |
| Year 2 | Competing on mid-competition head terms | Scale content velocity, scale link building |

Most businesses see measurable improvements in 3–6 months; significant growth after 6–12 months. Early signals (ranking movement, impression increases) typically appear in days 61–90.

## Domain Authority Growth Timeline

DA follows logarithmic curve — 0→15 easier than 15→30, far easier than 30→50:

- **Months 1–3**: DR/DA 0–10. Technical foundation, content production, foundational links (Product Hunt, AngelList, Crunchbase, LinkedIn).
- **Months 3–6**: DR/DA 10–20. First guest posts, HARO mentions, resource page links. Long-tail ranking on page 2–3.
- **Months 6–12**: DR/DA 20–35. Organic traffic measurable. Mid-competition keywords enter page 1. Digital PR generating media backlinks.
- **Year 2+**: DR/DA 35–50+. Head terms achievable. AI engines consistently recognize brand as entity.

B2B companies: 4–6 months of consistent work → first measurable organic gains.

## Content Production Expectations

A startup publishing 8 articles/month with 6-month lead time:
- **Month 6**: ~50 indexed pages, 5–15K monthly impressions
- **Month 12**: ~100 indexed pages, 20–60K impressions, 500–2,000 sessions
- **Month 24**: ~200 indexed pages, 100K+ impressions, 5,000–20,000 sessions (with consistent link building)

Shape of curve: slow early returns, accelerating compounding by month 12+.

## Key Metrics by Stage

### Months 1–3 (Leading Indicators)
- Pages indexed (target: all important pages within 2–4 weeks)
- Impressions in GSC
- Core Web Vitals scores
- Technical errors in GSC Coverage (target: zero critical)

### Months 3–6 (Emerging Signals)
- Keyword rankings on long-tail targets (page 2–3 = success)
- Organic CTR by page (low CTR + high impressions = title/description opportunity)
- Referring domains (10–20 is meaningful progress)

### Months 6–12 (Revenue-Adjacent)
- Organic sessions growth (target: MoM >10%)
- Organic conversion rate by landing page
- Organic-attributed leads/trials/purchases in GA4
- Share of Model in target AI engines

Anti-pattern: tracking daily keyword rankings as primary metric. Rankings fluctuate daily, don't capture AI referrals or featured snippets. Track 30-day rolling trends.

## Conversion Benchmarks

- BOFU commercial keywords: 4.78% conversion rate
- Informational keywords: 0.19% conversion rate
- 25x conversion rate difference (BOFU vs. informational)
- Comparison pages convert at 2–5x rate of general blog content
- B2B SaaS visitor-to-lead average: ~1.9%
- BOFU organic page target: 3–8% conversion
- TOFU page target: 0.5–2% (low-commitment action)
- SEO + CRO integrated: 30–50% higher conversion from organic

## Search-to-Conversion Funnel Benchmarks

| Stage | Entry Signal | Key Metric | Early-Stage Benchmark |
|---|---|---|---|
| **Discovery** | SERP/AI impression | Impressions, Share of Model | 10K+ monthly impressions by Month 6 |
| **Click** | Visit organic page | Sessions, CTR | CTR: 3–5% (informational), 6–10% (branded) |
| **Engagement** | Read/explore | Pages/session, time on site | 2+ pages/session, 2+ min average |
| **Lead Capture** | Signup/trial | Page conversion rate | TOFU: 1–3%; BOFU: 3–8% |
| **Nurture** | Email engagement | Open rate, return visits | 25–35% email open rate |
| **Revenue** | Closed deal | MQL→SQL rate, CAC | Track vs. paid channels |

## SEO ROI Formula

SEO ROI (%) = (Organic Revenue – SEO Cost) ÷ SEO Cost × 100

Where SEO Cost = tool subscriptions + content production + link building + internal time at loaded hourly rate.

### GA4 Attribution Setup
1. Link GSC to GA4 (Admin > Property Settings > Search Console Links)
2. Define all conversion-relevant actions as Key Events
3. For lead-gen: assign monetary values using (Average Deal Size × Close Rate) ÷ Average Leads-to-Close
4. Use GA4 Advertising > Attribution > Conversion Paths report
5. Switch to Data-Driven attribution (organic's contribution typically 20–40% higher vs. Last Click)

## When to Pivot (6-Month Checkpoint)

If after 6 months of consistent execution:
- Fewer than 5K impressions/month
- Zero long-tail rankings

Investigate:
1. Are critical pages actually indexed?
2. Is keyword targeting realistic for current DA?
3. Is content quality meeting E-E-A-T standards?
4. Are there technical barriers blocking crawl?
