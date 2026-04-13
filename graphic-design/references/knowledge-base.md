# Graphic Design Best Practices — Full Knowledge Base

## Table of Contents
1. Color Systems and Palettes (line ~10)
2. Typography Systems (line ~120)
3. Layout, Grid Systems, and Spacing (line ~200)
4. Visual Hierarchy and Composition (line ~280)
5. Design Patterns and Component Systems (line ~340)
6. Branding and Identity Systems (line ~420)
7. Accessibility and Inclusive Design (line ~490)
8. Design Process and Decision Frameworks (line ~560)

---

## 1. Color Systems and Palettes

### Governing Principles
- WCAG 2.2 contrast: 4.5:1 normal text, 3:1 large text (AA); 7:1 / 4.5:1 (AAA)
- Non-text UI elements: 3:1 contrast (SC 1.4.11)
- Color must never be the sole means of conveying information (SC 1.4.1)
- Use perceptually uniform color spaces (Oklch, Display P3) for token definitions
- Structure tokens: primitive → semantic → component

### Domain Focus
- **Branding**: color = meaning, differentiation, recognizability → then accessibility
- **UI/UX**: color = functional system (states, semantics, density, theming) → then brand
- **Web/landing**: color = emotional impact + conversion → still must satisfy WCAG

### Palette Construction

**60-30-10 Rule**: 60% neutral/background, 30% primary surfaces, 10% accent.

**Harmony strategies**:
- Monochromatic: one hue, varied lightness/saturation — serious brands, dense UIs
- Analogous: neighboring hues — organic/lifestyle brands; needs careful contrast
- Complementary / split-complementary: opposed hues — strong CTAs, limited accent use

**Heuristics**:
- Start with warm/cool gray neutral base supporting light + dark themes
- Restrict saturated accent to small % of page — reserve for primary CTA/alerts
- For product UIs: derive tonal palettes (0–900 steps) with consistent lightness increments

**Failure patterns**:
- Overusing saturated brand colors on large surfaces → legibility issues, visual fatigue
- Building palettes in sRGB HSL without perceptual uniformity → inconsistent contrast
- Marketing-driven colors propagating into UI states without semantic mediation

### Brand Color Architecture
- **Primary**: 1–2 signature hues + core neutral (logo, CTAs, key headings)
- **Secondary**: supporting hues for sub-brands/categories (desaturated)
- **Accent**: high-saturation spots for CTAs/highlights (complementary to primary)
- **Neutrals**: grays, off-whites, near-blacks for surfaces and text context
- **Semantic**: functional colors for states (success/warning/error/info/interactive/disabled)

**Heuristics**:
- Name tokens formally (e.g., "Solaris Orange", "Midnight Navy") with hex/RGB/CMYK
- Design semantic roles first (`color.success.bg`, `color.error.border`), then map brand palette in
- Define a "conversion palette" (primary, hover, disabled, success) independent of hero colors

**Failure patterns**:
- Logo colors forced onto all UI elements → inaccessible states, visual clutter
- No defined neutral scale → arbitrary grays with inconsistent contrast
- Under-specified semantic colors → teams improvise alert colors per screen

### Dark Mode & Theming
- Dark themes reuse same semantic structure (tokens, roles, component mapping)
- Use lighter tonal variants of brand colors to avoid vibrating edges
- Elevation via lighter surface overlays, not darker shadows
- Near-black backgrounds (not pure #000) to reduce eye strain
- Define paired light/dark tokens at semantic level
- Re-evaluate WCAG contrast in both modes

**Failure patterns**:
- Inverting light themes without adjusting saturation → harsh contrast, illegible colored text
- Ignoring elevation → panels/dialogs disappear into background
- Different semantic meanings for same color across modes

---

## 2. Typography Systems

### Type Scale Construction
Modular scales: sizes related by fixed ratio (musical intervals).
- Minor Third (1.20), Major Third (1.25): moderate — UI hierarchies, dense layouts
- Perfect Fourth (1.333), Augmented Fourth (1.414): dramatic — marketing, brand headlines

**Heuristics**:
- Single base size (14–18px body) + one ratio → limited ladder (-2 to +4 steps)
- Product UIs: Minor/Major Third for smooth label→body→heading transitions
- Marketing: larger ratio for heroes, gentler scale for inner content

**Failure patterns**:
- Ad hoc font sizes per screen → near-duplicates, broken hierarchy
- Overly large ratios throughout product UI → harms scannability

### Fluid & Responsive Typography
- `clamp(min, preferred, max)` for continuous scaling across viewports
- Preferred values: viewport units + rem for user font size respect
- Line length: 45–75 characters for comfortable reading

**Heuristics**:
- Fluid scaling for large display sizes/heroes; breakpoint-driven for body
- Express min/max in rem; calculate preferred values to sync multiple fluid styles
- Don't make everything fluid — harms layout predictability

### Font Pairing & Variable Fonts
- Contrast pairing: geometric sans + humanist serif (brand/editorial)
- Superfamilies: text + display variants from one family (product/UI)
- Variable fonts: continuous axes for weight/width/optical size, fewer files

**Heuristics**:
- Prefer superfamilies/variable fonts in UI work for consistent metrics
- Contrast pairings for brand/editorial; limit to 2 functional families
- Apple platforms: min 11pt, SF Text ≤19pt, SF Display ≥20pt, support Dynamic Type

### Typographic Hierarchy & Tokens
- Define hierarchy: display, h1–h6, body, caption, overline, label as tokens
- Use size + weight + color + spacing to signal hierarchy (not single dimension)
- Bind type and spacing scales together (vertical spacing = multiples of line-height)

---

## 3. Layout, Grid Systems, and Spacing

### Grid Frameworks (Müller-Brockmann)
- **Column grids**: 4–12 vertical columns, responsive web/editorial
- **Modular grids**: add horizontal divisions → dashboards, card layouts
- **Baseline grids**: align text baselines to consistent vertical rhythm
- **Compound grids**: combine grids for multi-content-type pages

**Heuristics**:
- Branding: master grids for key formats using rule of thirds / page canons
- Web/product: 12-col desktop, 4-col mobile, gutters in 8px increments
- Baseline grids tied to body line-height

### Spacing Systems (4px / 8px base)
- Single scale (4/8px) for margins, padding, gaps → predictable rhythm
- Tokens: `space.xs=4`, `space.sm=8`, `space.md=16`
- 8px for macro layout, 4px for micro layout
- Align spacing to typographic scales

**Failure patterns**:
- Mixing arbitrary spacings (5, 9, 13px) → edges/baselines never align
- Different spacing scales for web vs product without token mapping

### Layout Patterns (Eyetracking-based)
- **F-pattern**: top + left focus, horizontal sweeps — dense text/articles
- **Z-pattern**: sparse layouts, top-left → top-right → diagonal → bottom — heroes, simple landing
- **Card grids**: modular, responsive reflow — dashboards, galleries
- **Split-screen**: left/right with complementary roles

**Heuristics**:
- Match pattern to content: F for dense text, Z for focused marketing
- Card grids collapse gracefully with clear groupings/headings

### Responsive Strategy
- Container-based breakpoints (component width, not just viewport)
- Mobile-first → progressive enhancement to multi-column
- Document component behavior across density modes and breakpoints

---

## 4. Visual Hierarchy and Composition

### Hierarchy Construction (effectiveness ranking)
1. **Position** (top/left in LTR) + **isolation** (whitespace)
2. **Size and weight** (large, bold → first fixations)
3. **Color and contrast** (CTAs/alerts, used sparingly)
4. **Repetition and pattern** (predictable hierarchy)

**Heuristics**:
- Dashboards: primary KPIs upper-left/center, larger tiles, stronger contrast
- Landing pages: singular visual entry point (hero + CTA), no competing equal-strength elements

### Gestalt Principles in UI
- **Proximity**: group related controls tightly, separate groups with larger gaps
- **Similarity**: consistent styles for similar interactive roles
- **Continuity**: align along common axes for predictable scanning
- **Closure**: card containers, borders, subtle shadows for grouping
- **Figure–ground**: clear contrast/layering between content, chrome, background

### Information Density
- Progressive disclosure: high-level summaries → drill-down
- Dashboards: 6–9 top-level KPI tiles max on first view
- Marketing: resist cramming features into hero → scannable sections
- Brand microsites: generous whitespace, narrative pacing

---

## 5. Design Patterns and Component Systems

### Atomic Design (Brad Frost)
- **Atoms**: buttons, inputs, labels, icons, tokens
- **Molecules**: small functional units (label + input + button)
- **Organisms**: distinct UI sections (header with logo, nav, search)
- **Templates**: page-level layout structures
- **Pages**: real content instances of templates

### Common UI Patterns
- **Navigation**: top bars, side rails, hamburgers — expose primary sections
- **Forms**: single-column, labels above, inline validation, helper text
- **Cards**: consistent padding, header/body/action, elevation rules
- **Modals**: focused interruptive tasks only, not flow dumping grounds
- **Empty states**: informational, action-oriented, or celebratory
- **Loading states**: spinners, skeletons, progress bars per context

### Design Tokens
- Platform-agnostic variables: color, type, spacing, elevation
- Option/primitive tokens → semantic tokens → component tokens
- Drive all component styles through tokens (no hard-coded values)
- Pattern documentation: purpose, components, accessibility, anti-patterns

---

## 6. Branding and Identity Systems

### Brand Identity Architecture
- **Logo lockups**: horizontal, vertical, badge, partner — specified spacing/alignment
- **Clear space**: min exclusion zone (multiple of x-height or mark height)
- **Responsive logos**: full lockup → stacked → icon-only → one-color as size decreases
- Test legibility at small sizes (favicon 16–32px, mobile nav, print)

### Brand Consistency
- Principles + do/don't examples + governance mechanisms
- Design tokens + component libraries operationalize brand rules
- Cross-channel examples: web, app, social, email, print
- Photography/illustration guidelines mapped to layout/type systems

### Brand Book Structure
1. Brand narrative and positioning
2. Logo: variants, clear space, misuse, responsive system
3. Color: primary/secondary/neutrals/semantics + accessibility + print/digital
4. Typography: typefaces, hierarchy, responsive rules
5. Layout and grid: master grids, spacing, keylines
6. UI guidelines: buttons, cards, forms, empty/loading states
7. Accessibility: contrast, text sizes, alt text, motion

---

## 7. Accessibility and Inclusive Design

### WCAG 2.2 Visual Requirements
- **1.4.3**: 4.5:1 normal text, 3:1 large text (AA); 7:1 / 4.5:1 (AAA)
- **1.4.11**: non-text UI ≥3:1 contrast
- **1.4.1**: color not sole means of conveying info
- **2.4.7 / 2.4.11-12**: focus indicators visible, min area + contrast
- **2.5.8**: targets ≥24×24 CSS px (AA); **2.5.5**: ≥44×44 (AAA)

**Heuristics**:
- Verify contrast with tools, never eyeball
- Custom focus styles ≥3:1 against surroundings, scale with component
- Touch targets ≥44pt on mobile (iOS/Android practical guidance)

**Failure patterns**:
- Removing default focus outlines without replacement
- Color-only indication for errors, active states, required fields
- Crowded interactive elements with overlapping hit areas

### Inclusive Design (Microsoft)
Three principles: recognize exclusion, learn from diversity, solve for one → extend to many
- Visual impairments: redundant coding (icons, text, patterns)
- Cognitive load: chunking, hierarchy, progressive disclosure
- Motor impairments: large targets, adequate spacing, no precision-dependent timing

### Accessibility as Quality Lever
- High contrast → readable in bright sunlight / low-quality displays
- Large targets → better keyboard nav + touch accuracy
- Clear hierarchy → better comprehension for all users

---

## 8. Design Process and Decision Frameworks

### Systematic Critique
- Evaluate against principle hierarchy: accessibility → clarity → consistency → brand → novelty
- Use eyetracking evidence + analytics to validate hierarchy/layout
- Incorporate accessibility checks into design reviews, not just dev QA

### Principle Hierarchies
- "Clarity over density", "Consistency over novelty", "Function over style"
- Document principle pairs with examples in design system
- Reference WCAG when brand-color trade-offs arise

### Handoff & Specification
- Align design libraries with code components via tokens (1:1 mapping)
- Tokens as lingua franca: designer specifies `color.primary`, dev implements same token
- Component docs: purpose, anatomy, states, responsive behavior, accessibility, examples

**Failure patterns**:
- Divergence between design libraries and code from irregular sync
- Local overrides instead of tokens → system-wide updates impossible
