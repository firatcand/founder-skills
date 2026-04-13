# AEO Optimization Checklists & Structural Patterns

## 7 Structural Patterns That Increase AI Citation

Based on analysis of 680 million citations across ChatGPT, Google AI Overviews, and Perplexity:

### 1. Question-First Headings (H2/H3)
Use "What is X?", "How does X work?", "Why does X matter?" as heading structure. Maps directly to how users phrase AI queries and enables clean extraction.

### 2. Direct Definitional Statements After Headings
First sentence after each heading = complete, self-contained answer that stands alone out of context.
Example: "Content clustering is the practice of organizing related articles around a central pillar page to signal topical authority to search engines."

### 3. Answer Length of 40–60 Words
AI engines (especially those feeding from Google's featured snippet infrastructure) extract answers in this range. Write a direct answer in 40–60 words, then elaborate.

### 4. Comparison Tables
Perplexity explicitly prioritizes comparison tables with clear headers. Tables outperform prose for comparative information because they are structurally unambiguous.

### 5. FAQ Blocks
Add a dedicated FAQ section to every key page. Format: question in H3, answer in paragraph beneath. Each answer: 50–100 words, direct, factually precise. Implement FAQPage schema.

### 6. Numbered Lists for Process/Sequential Content
AI engines preserve numbered list structure in their responses. Step-by-step processes as numbered lists are frequently cited verbatim.

### 7. Data Points with Source Attribution Inline
"According to [source], X% of Y do Z" — this format is cited significantly more often than unsourced claims. Perplexity traces claims to sources, so attribution makes your content more valuable as a citation.

**Anti-pattern:** Dense academic prose with no structural markers. Long paragraphs without headers, lists, or tables are unextractable regardless of quality.

## AI Engine Citation Preferences

| Engine | Source Preference | Freshness Bias | Key Optimization |
|--------|------------------|----------------|------------------|
| **ChatGPT** | Encyclopedic, established (Wikipedia 47.9% of top citations) | Low — 29% of citations from 2022 or earlier | Build presence in Wikipedia, industry publications, reference databases |
| **Perplexity** | Community-validated (Reddit 46.7%) | High — 50% of citations from 2025 content | Fresh content, authentic community presence, Reddit discussion |
| **Google AI Overviews** | Distributed, blends professional + social; YouTube at 23.3% | Medium | Traditional SEO performance feeds AI Overview citations (virtuous loop) |
| **Gemini** | Similar to Google AI Overviews | Medium | Multi-modal content synthesis capability |

Only 11% of domains are cited by both ChatGPT and Perplexity — decide which engine your ICP uses most and optimize primarily for that platform.

## AEO Checklists by Content Type

### Blog Posts / Editorial Articles
- ☐ H2/H3 headings phrased as questions
- ☐ Direct 40–60 word answer immediately after each heading
- ☐ TL;DR / Key Takeaways box at top
- ☐ FAQ block at bottom (4–8 questions) with FAQPage schema
- ☐ At least 2–3 inline data points with source attribution
- ☐ Article schema with datePublished, dateModified, author
- ☐ Internal links to pillar page and related cluster content

### Product / Landing Pages
- ☐ Explicit "What is [product]?" definitional statement above the fold
- ☐ Organization schema with complete sameAs properties
- ☐ Product schema with pricing, availability, category
- ☐ FAQ block addressing "vs. competitor" and "use case" questions
- ☐ Comparison table vs. top 2–3 alternatives
- ☐ Trust signals: customer logos, review counts, G2/Capterra badges with Review schema

### Documentation / How-To Guides
- ☐ HowTo schema marking each step
- ☐ Numbered step format (not prose paragraphs)
- ☐ Code snippets marked up semantically
- ☐ Breadcrumb schema reflecting docs hierarchy
- ☐ Clear prerequisites and outcome statement at top

### Glossary / Definition Pages
- ☐ Direct definitional sentence in the first paragraph
- ☐ DefinedTerm or Article schema with clear term/definition structure
- ☐ Related terms section with internal links
- ☐ "Used in a sentence" example
- ☐ Related FAQ at the bottom

## Entity Authority Building

### Authority Levels
| Level | Sources | Difficulty | Impact |
|---|---|---|---|
| **Level 1: Owned** | Website + Organization schema + social profiles | Easy | Foundation |
| **Level 2: Directories** | Crunchbase, LinkedIn, Google Business Profile, industry directories | Easy–Medium | Moderate |
| **Level 3: Third-Party** | Wikipedia/Wikidata, industry press, G2, Capterra | Medium–Hard | High |
| **Level 4: Cross-Source** | Multiple independent authoritative sources describing brand consistently | Hard | Very High |

### Practical Path from Zero
1. **Day 1**: Organization schema with sameAs properties linking to all owned profiles
2. **Week 1**: Create/complete Crunchbase, LinkedIn Company Page, industry directories. NAP data must be identical everywhere.
3. **Month 1–3**: Earn at least one mention in recognized industry publication (digital PR, HARO, guest contribution)
4. **Month 6+**: Pursue Wikidata entry for structured entity recognition

### Entity Recognition Test
Query ChatGPT, Perplexity, and Gemini: "Tell me about [your brand]"
- Vague/inaccurate/nonexistent responses → entity authority needs work
- Google Knowledge Panel appearing → entity is recognized

## AI Citation Monitoring

### Paid Tools (2025–2026)
| Tool | Platforms | Key Feature |
|---|---|---|
| **Siftly** | ChatGPT, Perplexity, Google AI, Copilot | Cross-platform tracking, competitive benchmarking |
| **LLMrefs** | ChatGPT, Perplexity | Citation tracking, source domain analysis |
| **Riff Analytics** | ChatGPT, Perplexity | Brand mention sentiment, co-mention patterns |
| **llmclicks.ai** | ChatGPT, Perplexity, Gemini, Copilot | Real-time continuous monitoring |

### Free Manual Protocol
Weekly queries to ChatGPT, Perplexity, and Gemini using 10–15 prompts representing target queries. Track which competitor brands appear and which of your pages get cited. Creates a "Share of Model" baseline.

Note: GA4 doesn't capture AI referrals well — ChatGPT links show as direct traffic; Perplexity may appear as referral from perplexity.ai but attribution is incomplete.

## Proven vs. Speculative AEO Tactics

### Proven (supported by empirical citation data)
- Pages with clean H2/H3 hierarchy + aligned schema → 2.8x higher AI citation rates
- Content freshness significantly impacts Perplexity citation probability
- Platform-specific source preferences are real and actionable
- FAQPage schema increases extractability in Google AI Overviews
- Entity consistency across web (sameAs corroboration) improves AI entity recognition

### Speculative (logical but not empirically established)
- `llms.txt` files as a direct citation signal
- Exact weighting of schema markup in LLM training data vs. real-time retrieval
- Whether GEO efforts affect ChatGPT's base model vs. web search mode differently
- Precise role of Reddit presence in Perplexity ranking beyond observed correlation
