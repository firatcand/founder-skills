# Technical SEO Checklist & Schema Implementation

## Minimum Viable Technical SEO Checklist (Launch)

1. ☐ HTTPS enabled with valid SSL certificate
2. ☐ XML sitemap submitted to Google Search Console
3. ☐ robots.txt configured (block admin, internal search, faceted navigation)
4. ☐ Canonical tags set on all pages pointing to preferred URL
5. ☐ Meta title and description on every page (unique per page)
6. ☐ Proper H1–H3 heading hierarchy (one H1 per page)
7. ☐ LCP < 2.5s, INP < 200ms, CLS < 0.1 (verified in PageSpeed Insights)
8. ☐ Mobile-responsive layout validated
9. ☐ Images compressed to WebP with descriptive alt text
10. ☐ Organization schema on homepage
11. ☐ No accidental noindex on important pages (confirm via GSC Coverage report)
12. ☐ Internal links from homepage to all top-level content pages
13. ☐ GPTBot, ClaudeBot, PerplexityBot NOT blocked in robots.txt
14. ☐ Consider adding llms.txt file to guide AI crawlers on site structure

## Core Web Vitals Thresholds

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| **LCP** (Largest Contentful Paint) | ≤ 2.5s | ≤ 4s | > 4s |
| **INP** (Interaction to Next Paint) | ≤ 200ms | ≤ 500ms | > 500ms |
| **CLS** (Cumulative Layout Shift) | ≤ 0.1 | ≤ 0.25 | > 0.25 |

**Highest-leverage CWV fixes for startups:**
- Compress images to WebP format
- Implement lazy loading for below-the-fold content
- Use a CDN
- Remove render-blocking JavaScript
- Set explicit image/video dimensions to prevent layout shift

## Site Architecture Rules

- Keep navigation to 2 levels deep for sites under 500 pages: homepage → category → content
- Use hub-and-spoke (pillar-and-cluster) model
- No orphan pages — every page needs 2–3+ internal links pointing to it
- Choose brand-forward domain name (not keyword-stuffed)
- Prefer .com unless strongly regional market
- Set up canonical redirects (www vs non-www)

## Schema Markup Implementation Guide

### Priority Order
1. **Organization** — entity foundation with sameAs links to social profiles
2. **WebSite** with SearchAction — sitelinks search box
3. **Article / BlogPosting** — on all editorial content with author Person markup, datePublished, dateModified
4. **FAQPage** — on any Q&A content (highest AEO leverage schema type)
5. **HowTo** — on tutorials/step-by-step content
6. **Product** — pricing, availability, review schema
7. **BreadcrumbList** — site hierarchy signal

### AEO-Specific Schema Types
- **FAQPage**: Highest-leverage for AEO. Marks Q&A pairs for AI extraction.
- **HowTo**: Each step as structured data object (name, text, optional image/URL). AI engines disproportionately surface HowTo content for process queries.
- **Speakable**: Marks sections suitable for audio/voice search playback. Also signals importance for AI extraction.
- **Dataset**: For original research/statistics pages. Signals primary data source.
- **SameAs** (in Organization): Links entity to LinkedIn, Crunchbase, Wikidata, Twitter. Cross-source entity corroboration mechanism for AI model recognition.

### Implementation Rules
- Always use JSON-LD format (not Microdata or RDFa)
- Place in `<head>` tag
- Validate every implementation with Google Rich Results Test before publishing
- Schema MUST match on-page visible content exactly — misleading markup can trigger penalties
- Keep schema updated when page content changes

## Indexing Strategy

### What to Index
Homepage, product/service pages, pillar content, cluster articles, glossary terms, comparison pages, landing pages

### What to Noindex
Thank-you pages, login/admin pages, internal search results, pagination pages beyond page 2, NDA/paywall content, tag archives that duplicate category content

### AI Crawlers
- Add `llms.txt` at root domain (plain-text summary of important pages for AI crawlers)
- Ensure GPTBot, ClaudeBot, PerplexityBot are NOT blocked in robots.txt
- This is speculative as a direct ranking signal but logical infrastructure

## Common Technical Mistakes

1. **Blocking crawlers** — `Disallow: /` left from dev environment
2. **Duplicate homepage** — both `example.com` and `www.example.com` accessible without canonical redirect
3. **Missing meta tags** on inner pages
4. **No GSC setup** — losing early indexing data
5. **JS-rendered content not indexable** — React/Next.js SPA without SSR making content invisible to crawlers
