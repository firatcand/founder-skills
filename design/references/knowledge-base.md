# Design Knowledge Base

The full best-practices framework behind the design advisor — visual layer, UX/perceptual layer, and brand identity in one place. Numeric defaults are evidence-based (WCAG 2.2, Apple HIG, Material, IBM Carbon, Atlassian, Nielsen Norman Group, Baymard, Müller-Brockmann, Brad Frost). Use these as the source of truth.

## Table of Contents
1. [White Space and Spacing](#white-space-and-spacing)
2. [Proximity and Grouping](#proximity-and-grouping)
3. [Visual Hierarchy and Composition](#visual-hierarchy-and-composition)
4. [Alignment and Grids](#alignment-and-grids)
5. [Consistency and Pattern Reuse](#consistency-and-pattern-reuse)
6. [Color Systems and Palettes](#color-systems-and-palettes)
7. [Typography Systems](#typography-systems)
8. [Responsive and Adaptive Layout](#responsive-and-adaptive-layout)
9. [Affordance and Feedback](#affordance-and-feedback)
10. [Accessibility and Inclusive Design](#accessibility-and-inclusive-design)
11. [Information Density and Progressive Disclosure](#information-density-and-progressive-disclosure)
12. [Gestalt Principles](#gestalt-principles)
13. [Branding and Identity Systems](#branding-and-identity-systems)
14. [Design Patterns and Component Systems](#design-patterns-and-component-systems)
15. [Decision Frameworks and Handoff](#decision-frameworks-and-handoff)

---

## White Space and Spacing

### Micro white space (inside components)
- 4–8px base unit for intra-component spacing.
- 4px for tight relationships (label–value, icon–label).
- 8–12px between closely related controls.
- Align text to a 4px or 8px vertical baseline grid.

### Macro white space (between groups/sections)
- 8px spacing system: 4, 8, 12, 16, 24, 32, 40, 48, 64, 80px. Tokenize it: `space.xs=4`, `space.sm=8`, `space.md=16`.
- 8px governs macro layout, 4px governs micro layout.
- 32–80px for page-level separation and hero sections.

### When to adjust density
- **More white space**: high-stakes/unfamiliar content, reading/interpretation tasks, calm/luxury/focus brand, new or casual users.
- **More density**: expert users comparing many data points, constrained screens with well-learned tasks; offer a density toggle.

### Practical ranges
- Content-heavy pages: 24–40px between sections.
- Dense admin/data UIs: 16–24px between groups, 8–12px between related controls.

### Failure patterns
- Mixing arbitrary spacings (5, 9, 13px) → edges and baselines never align.
- Different spacing scales for web vs product without a token mapping.

---

## Proximity and Grouping

Items close together are perceived as related; items far apart as separate. Proximity can overpower similarity — and controls placed too far from the objects they act on get overlooked entirely (NN/g).

### Relative spacing ratios
- In-group spacing must be meaningfully smaller than between-group spacing. Ratio ~1:2 or 1:3 (e.g., 8px inside, 24px between).
- Forms: label–field spacing < inter-field spacing.

### Concrete ranges (8px scale)
- Tightly related (icon + label, label + field): 4–8px.
- Same group (list items in a card, radios in a set): 8–12px.
- Separate groups within a panel/card: 16–24px.
- Logically distinct page sections: 32–80px.

### Key rule
- Place action controls immediately adjacent to the content they affect. Don't mix unrelated controls in one tight cluster.

---

## Visual Hierarchy and Composition

Intentional ranking of elements by perceptual importance using size, weight, color, contrast, position, and whitespace.

### Perceptual rationale
- People scan, not read. Eye-tracking shows content near the top and in prominent positions gets disproportionate attention (F-pattern, layer-cake scanning).
- High contrast, larger size, and a unique color create focal points that act as entry points.
- Consistent hierarchy reduces decision time (Hick's law).

### Levers, by effectiveness
1. **Position** (top/left in LTR) + **isolation** (whitespace) — first fixations.
2. **Size and weight** — most important element clearly largest/boldest; aim for ≥3 levels (primary, secondary, tertiary).
3. **Color and contrast** — high-saturation accent used sparingly for CTAs/alerts; respect WCAG (4.5:1 body, 3:1 large).
4. **Repetition and pattern** — predictable, repeated hierarchy.

### Application
- Dashboards: primary KPIs upper-left/center, larger tiles, stronger contrast.
- Landing pages: a single visual entry point (hero + CTA); avoid competing equal-strength elements.
- Avoid more than ~3 simultaneous contrast levels — too many weights/colors flatten hierarchy.

---

## Alignment and Grids

### Grid frameworks (Müller-Brockmann)
- **Column grids**: 4–12 vertical columns, for responsive web/editorial.
- **Modular grids**: add horizontal divisions → dashboards, card layouts.
- **Baseline grids**: align text baselines to a consistent vertical rhythm (tie to body line-height).
- **Compound grids**: combine grids for multi-content-type pages.

### Concrete defaults
- 12-column desktop, 4-column mobile; IBM Carbon: 4 cols at 320px, 8 at medium, 16 from 1056px+.
- Gutters: 16–32px, in 8px increments.
- Single base unit (4 or 8px) for columns, gutters, component dimensions, and spacing tokens.

### Breaking the grid
- Intentional only: offset one hero element for emphasis; modals/toasts on a different layer. Must be rare and documented — uncontrolled exceptions erode the grid's benefits.

---

## Consistency and Pattern Reuse

### Component & interaction level
- A single documented set of core components with clear variant guidance; centralized tokens for color, spacing, typography.
- Reuse layout and interaction structure for similar flows; consistent navigation across sections.

### Platform conventions
- iOS: top nav bars, bottom tab bars, 44×44pt targets, standard gestures.
- Android: top app bars, FAB placement, 48×48dp targets, standard nav.
- **Jakob's Law**: people spend most of their time on other products — reuse ecosystem patterns.

### Cost of inconsistency
- Forces recognition-then-verification loops ("Is this the same action?") — a major driver of abandonment (Baymard).

---

## Color Systems and Palettes

### Governing principles
- WCAG 2.2 contrast: 4.5:1 normal text, 3:1 large text (AA); 7:1 / 4.5:1 (AAA). Non-text UI: 3:1 (1.4.11).
- Color must never be the sole means of conveying information (1.4.1).
- Define tokens in perceptually uniform spaces (Oklch, Display P3). Structure: primitive → semantic → component.

### Domain focus
- **Branding**: color = meaning, differentiation, recognizability → then accessibility.
- **UI/UX**: color = functional system (states, semantics, theming) → then brand.
- **Web/landing**: color = emotional impact + conversion → still must satisfy WCAG.

### Palette construction
- **60-30-10**: 60% neutral/background, 30% primary surfaces, 10% accent.
- Harmony: monochromatic (serious brands, dense UIs); analogous (organic/lifestyle, needs careful contrast); complementary/split-complementary (strong CTAs, limited accent).
- Start from a warm/cool gray neutral base supporting light + dark. Restrict saturated accent to a small % — reserve for primary CTA/alerts. Derive tonal palettes (0–900 steps) with consistent lightness increments.

### Brand color architecture
- **Primary**: 1–2 signature hues + core neutral (logo, CTAs, key headings).
- **Secondary**: supporting hues (desaturated) for sub-brands/categories.
- **Accent**: high-saturation spots for CTAs/highlights, complementary to primary.
- **Neutrals**: grays, off-whites, near-blacks for surfaces and text context.
- **Semantic**: success, warning, error, info, interactive, disabled — each with bg/border/text roles.
- Name tokens formally ("Solaris Orange", "Midnight Navy") with hex/RGB/CMYK. Design semantic roles first (`color.success.bg`), then map the brand palette in. Define a conversion palette (primary, hover, disabled, success) independent of hero colors.

### Dark mode & theming
- Reuse the same semantic structure; define paired light/dark tokens at the semantic level.
- Near-black background (~#121212, not pure #000) to reduce strain.
- Increase luminance range between surfaces instead of inverting; use lighter tonal brand variants to avoid vibrating edges. Convey elevation via lighter surface overlays, not darker shadows.
- Re-verify WCAG contrast in both modes.

### Failure patterns
- Saturated brand colors on large surfaces → fatigue and legibility issues.
- Building palettes in sRGB HSL without perceptual uniformity → inconsistent contrast.
- Logo colors forced onto all UI elements → inaccessible states, clutter.
- No defined neutral scale; under-specified semantics → teams improvise per screen.
- Inverting light themes without adjusting saturation; ignoring elevation so panels disappear.

---

## Typography Systems

### Size guidelines
- Body: 16–18px/pt for standard reading distance.
- iOS: 17pt body, 34pt large titles, 13–15pt secondary, 10pt smallest. Apple: min 11pt, SF Text ≤19pt, SF Display ≥20pt, support Dynamic Type.
- Large-text threshold: 18pt regular or 14pt bold (WCAG).

### Line height and length
- Line height: 1.4–1.6× font size for body.
- Line length: 45–75 characters (60–70 for desktop).

### Type scale (modular)
- Sizes related by a fixed ratio (musical intervals): Minor Third (1.20) / Major Third (1.25) for moderate UI hierarchies and dense layouts; Perfect Fourth (1.333) / Augmented Fourth (1.414) for dramatic marketing/brand headlines.
- Single base size (14–18px body) + one ratio → a limited ladder (−2 to +4 steps). Example: 16, 20, 25, 31, 39px (body → H1).
- Product UIs: smaller ratios for smooth label→body→heading transitions. Marketing: larger ratio for heroes, gentler scale for inner content.
- Signal hierarchy with size + weight + color + spacing — not a single dimension. Use semantic tokens (display, h1–h6, body, caption, overline, label). Bind type and spacing scales (vertical spacing = multiples of line-height).

### Fluid & responsive
- `clamp(min, preferred, max)` for continuous scaling; express min/max in rem to respect user font size. Fluid for large display/heroes, breakpoint-driven for body — don't make everything fluid.
- Use relative units (rem, em); define breakpoint-aware type tokens.

### Font pairing & variable fonts
- Contrast pairing (geometric sans + humanist serif) for brand/editorial; superfamilies (text + display from one family) for product/UI. Limit to 2 functional families.
- Prefer variable fonts/superfamilies in UI for consistent metrics and fewer files.

### Failure patterns
- Ad hoc font sizes per screen → near-duplicates, broken hierarchy.
- Overly large ratios throughout a product UI → harms scannability.

---

## Responsive and Adaptive Layout

### Breakpoints
- <600px mobile, 600–960px tablet, ≥960/1200px desktop. Prefer content-driven (and container-based) breakpoints over device-specific.

### Fluid vs fixed
- Fluid widths for primary content within a max-width (1080–1200px). Fixed/pinned nav and FABs for muscle memory.

### Reflow
- **Small breakpoints**: stack columns into one; collapse secondary controls into menus/overflow; keep primary actions visible.
- **Large breakpoints**: expose secondary functionality inline (filter panels, detail sidebars).
- Mobile-first → progressive enhancement to multi-column. Document component behavior across density modes and breakpoints.

---

## Affordance and Feedback

### Affordance
- The perceived action possibility of an element. Well-designed, users "know what to do just by looking" (Don Norman).
- Make tappable/clickable elements look interactive (consistent button styles with fills, borders, or elevation). Style links with underlines/distinct color. Use signifiers (icons, arrows, carets) for expandable/draggable regions.

### State communication
- **Default/rest**: standard fill/border/text.
- **Hover/focus**: increased contrast, elevation, or outline. WCAG 2.4.7 requires visible keyboard focus.
- **Active/pressed**: immediate, short-lived change (darker fill, depressed shadow).
- **Disabled**: reduced opacity, no hover/press, but keep legible contrast.
- **Error/success/loading**: dedicated colors, icons, messages. Loading = spinners, skeletons, or progress per context.

### Timing
- 150–250ms for state transitions (responsive without jarring); up to 500ms for progress or context changes.

### Rationale
- Immediate, understandable feedback provides closure, reduces anxiety, reinforces correct actions, and reduces error repetition.

---

## Accessibility and Inclusive Design

### WCAG 2.2 visual requirements
- **1.4.3**: 4.5:1 normal text, 3:1 large (≥18pt / ≥14pt bold) (AA); 7:1 / 4.5:1 (AAA).
- **1.4.11**: non-text UI components ≥3:1 against adjacent colors.
- **1.4.1**: color not the sole means of conveying information.
- **2.4.7 / 2.4.11–12**: focus indicators visible, with min area and contrast. Focus styles ≥3:1 against surroundings, distinct from hover; never remove without an accessible replacement.
- **2.5.8**: targets ≥24×24 CSS px (AA); **2.5.5**: ≥44×44 (AAA). Touch ≥44pt on mobile (iOS/Android practical guidance).
- Verify contrast with tools — never eyeball.

### Semantic structure & motion
- Use semantic elements and landmarks (headings, lists, nav, main, form). Interactive controls must be real buttons/links or carry correct ARIA roles.
- Respect `prefers-reduced-motion`; provide non-animated alternatives; avoid auto-playing large animations.

### Inclusive design (Microsoft)
- Recognize exclusion, learn from diversity, solve for one → extend to many.
- Visual: redundant coding (icons, text, patterns). Cognitive: chunking, hierarchy, progressive disclosure. Motor: large targets, adequate spacing, no precision/timing dependence.

### Accessibility as a quality lever
- High contrast → readable in sunlight / low-quality displays. Large targets → better keyboard nav + touch. Clear hierarchy → better comprehension for everyone.

### Failure patterns
- Removing default focus outlines without replacement; color-only indication for errors/active/required states; crowded interactive elements with overlapping hit areas.

---

## Information Density and Progressive Disclosure

Defer advanced or infrequent information to secondary UI, revealing it only when needed — this reduces cognitive overload by focusing the primary interface on core tasks (Baymard: even well-funded sites overwhelm users with poorly structured info).

### When to show vs hide
- **Always visible**: core task information and primary actions; the primary decision-making attributes for the domain (in list/grid views).
- **Hidden by default**: advanced settings, rare filters, verbose explanations — within one click/tap.

### Patterns
- Accordions/expandable sections; tabs or segmented controls for alternate views (Overview / Details / Activity); collapsed "Advanced options"; card layouts with summary → expansion.
- Dashboards: 6–9 top-level KPI tiles max on first view. Marketing: resist cramming features into the hero — use scannable sections. Brand microsites: generous whitespace, narrative pacing.
- Expert users tolerate higher density; new/casual users need more breathing room.

---

## Gestalt Principles

The Gestalt laws describe how humans perceptually organize visual information — the most fundamental lens for whether a UI "reads" correctly.

- **Proximity**: items close together read as related. Within-group spacing meaningfully smaller than between-group (~1:2 or 1:3). Controls too far from their objects get overlooked.
- **Similarity**: shared visual characteristics (shape, color, size, texture) signal the same group. Use consistent styling for same-behavior elements; differentiate destructive actions with distinct color/iconography.
- **Continuity**: the eye follows continuous paths. Align content in predictable rows/columns; use directional lines or aligned steps in multi-step flows; avoid jagged alignment that breaks scan lines.
- **Closure**: the mind completes incomplete shapes. Use partially outlined cards or grouped backgrounds to imply grouping without heavy borders (ensure accessibility via labels).
- **Common region**: elements in the same closed region (box, background) read as grouped even without proximity. Use cards, panels, modals, section backgrounds, or subtle rules.
- **Figure–ground**: people perceive foreground vs background. Ensure adequate contrast and whitespace around primary content; use overlays/dimmed backdrops to separate modals from parent context.

---

## Branding and Identity Systems

### Brand identity architecture
- **Logo lockups**: horizontal, vertical, badge, partner — with specified spacing/alignment.
- **Clear space**: a minimum exclusion zone (a multiple of x-height or mark height).
- **Responsive logos**: full lockup → stacked → icon-only → one-color as size decreases. Test legibility small (favicon 16–32px, mobile nav, print).

### Brand consistency
- Principles + do/don't examples + governance. Tokens and component libraries operationalize brand rules. Provide cross-channel examples (web, app, social, email, print) and photography/illustration guidelines mapped to layout/type.

### Brand book structure
1. Brand narrative and positioning.
2. Logo: variants, clear space, misuse, responsive system.
3. Color: primary/secondary/neutrals/semantics + accessibility + print/digital.
4. Typography: typefaces, hierarchy, responsive rules.
5. Layout and grid: master grids, spacing, keylines.
6. UI guidelines: buttons, cards, forms, empty/loading states.
7. Accessibility: contrast, text sizes, alt text, motion.

---

## Design Patterns and Component Systems

### Atomic Design (Brad Frost)
- **Atoms**: buttons, inputs, labels, icons, tokens.
- **Molecules**: small functional units (label + input + button).
- **Organisms**: distinct sections (header with logo, nav, search).
- **Templates**: page-level layout structures.
- **Pages**: real content instances of templates.

### Common UI patterns
- **Navigation**: top bars, side rails, hamburgers — expose primary sections.
- **Forms**: single-column, labels above, inline validation, helper text.
- **Cards**: consistent padding, header/body/action, elevation rules (Gestalt common region + proximity).
- **Modals**: focused interruptive tasks only — not flow-dumping grounds.
- **Empty states**: informational, action-oriented, or celebratory.
- **Loading states**: spinners, skeletons, progress bars per context.

### Layout patterns (eye-tracking based)
- **F-pattern**: top + left focus, horizontal sweeps — dense text/articles.
- **Z-pattern**: top-left → top-right → diagonal → bottom — sparse heroes, simple landing pages.
- **Card grids**: modular, responsive reflow with clear groupings/headings — dashboards, galleries.
- **Split-screen**: left/right with complementary roles. Match the pattern to content density.

### Design tokens
- Platform-agnostic variables: color, type, spacing, elevation. Option/primitive → semantic → component. Drive all component styles through tokens — no hard-coded values. Document patterns: purpose, anatomy, states, responsive behavior, accessibility, anti-patterns, examples.

---

## Decision Frameworks and Handoff

### Priority hierarchy
Resolve trade-offs in this order: **Accessibility → Clarity → Consistency → Brand Expression → Novelty.** Companion rules: "Clarity over density", "Consistency over novelty", "Function over style". Reference WCAG when brand-color trade-offs arise.

### Systematic critique
- Evaluate against the priority hierarchy; structure feedback as what works → ranked issues → specific fixes.
- Use eye-tracking evidence and analytics to validate hierarchy/layout. Build accessibility checks into design reviews, not just dev QA.

### Handoff & specification
- Align design libraries with code components via tokens (1:1 mapping). Tokens are the lingua franca: the designer specifies `color.primary`, the developer implements the same token.
- Component docs: purpose, anatomy, states, responsive behavior, accessibility, examples.

### Failure patterns
- Divergence between design libraries and code from irregular sync.
- Local overrides instead of tokens → system-wide updates become impossible.
