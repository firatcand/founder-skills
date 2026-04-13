# UX Design Principles Reference

## Table of Contents
1. [Gestalt Principles](#gestalt-principles)
2. [Progressive Disclosure](#progressive-disclosure)
3. [Affordance and Feedback](#affordance-and-feedback)
4. [Visual Hierarchy](#visual-hierarchy)
5. [Accessibility](#accessibility)
6. [White Space and Spacing](#white-space-and-spacing)
7. [Proximity and Grouping](#proximity-and-grouping)
8. [Consistency and Pattern Reuse](#consistency-and-pattern-reuse)
9. [Typography](#typography)
10. [Color Usage](#color-usage)
11. [Responsive and Adaptive Layout](#responsive-and-adaptive-layout)
12. [Alignment and Grids](#alignment-and-grids)
13. [Information Density](#information-density)

---

## Gestalt Principles

The Gestalt laws describe how humans perceptually organize visual information. They are the most fundamental lens for evaluating whether a UI "reads" correctly.

### Proximity
- Items close together are perceived as related; items far apart as separate groups.
- Proximity can overpower similarity — spacing choices can correct or confuse perceived relationships.
- Controls too far from the objects they act on get overlooked entirely (NN/g research).
- **Guideline**: Within-group spacing should be meaningfully smaller than between-group spacing. Ratio ~1:2 or 1:3 (e.g., 8px inside, 24px between).

### Similarity
- Elements sharing visual characteristics (shape, color, size, texture) are perceived as part of the same group.
- Use consistent styling for same-behavior elements (all primary buttons share color/shape).
- Differentiate destructive actions with distinct color and iconography.

### Continuity
- The eye follows continuous paths, lines, and curves rather than jumping between disjointed elements.
- Align content in predictable rows and columns for natural scanning.
- In multi-step flows, use directional lines or aligned steps for progression.
- Avoid jagged alignment that breaks scan lines.

### Closure
- The mind "closes" incomplete shapes, inferring whole forms from partial information.
- Use partially outlined cards or grouped backgrounds to imply grouping without heavy borders.
- Employ minimalist toggles/icons where users can infer state from partial cues (ensure accessibility via labels).

### Common Region
- Elements within the same closed region (box, background) are perceived as grouped, even without proximity.
- Use containers (cards, panels, modals) with distinct backgrounds or borders.
- Leverage section backgrounds or subtle rules to delineate logical zones.

### Figure–Ground
- People perceive elements as either foreground (figure) or background (ground).
- Ensure adequate contrast and whitespace around primary content to pull it forward.
- Use overlays and dimmed backdrops to separate modals/dialogs from parent context.

---

## Progressive Disclosure

Defer advanced or infrequent information to secondary UI, revealing only when needed.

### Cognitive rationale
- Reduces cognitive overload by focusing primary interface on core tasks.
- Baymard research: even well-funded sites overwhelm users with poorly structured product information.

### When to show vs hide
- **Always visible**: Core task information and primary actions.
- **Hidden by default**: Advanced settings, rare filters, verbose explanations.

### Patterns
- Accordions and expandable sections for details.
- Tabs or segmented controls for alternate views (Overview / Details / Activity).
- "Advanced options" panels collapsed by default.
- Card-based layouts: summary view with more detail on expansion.

### Balancing scannability and completeness
- Identify primary decision-making attributes for the domain and ensure they're visible in list/grid views.
- Secondary details within one click/tap but not overloading initial presentation.

---

## Affordance and Feedback

### Affordance
- The perceived action possibility of an element — what a user believes they can do with it.
- When well-designed, users "know what to do just by looking" (Don Norman).

### Visual affordance cues
- Make tappable/clickable elements look interactive: consistent button styles with elevation, borders, or fills.
- Style links with underlines or distinct colors consistently.
- Use signifiers (icons, arrows, carets) to cue expandable or draggable regions.

### State communication
Define explicit visual states with clear differences:
- **Default/rest**: Standard fill/border/text.
- **Hover/focus**: Increased contrast, elevation, or outline. WCAG 2.4.7 requires visible keyboard focus.
- **Active/pressed**: Immediate short-lived change (darker fill, depressed shadow).
- **Disabled**: Reduced opacity, no hover/press states, but maintain contrast for legibility.
- **Error/success/loading**: Dedicated colors, icons, messages. Loading = spinners, skeletons, or progress indicators.

### Microinteraction timing
- 150–250ms for state transitions (feels responsive without jarring).
- Up to 500ms for progress or context changes.

### Feedback rationale
- Provides closure and reduces anxiety.
- Immediate, understandable feedback reinforces correct actions and reduces error repetition.

---

## Visual Hierarchy

Intentional ranking of elements by perceptual importance using size, weight, color, contrast, position, whitespace.

### Perceptual rationale
- People scan, not read. Eye-tracking: content near top and in prominent positions gets disproportionate attention (F-pattern, layer-cake scanning).
- High contrast, larger size, and unique color create focal points as entry points.
- Consistent hierarchy reduces decision time (Hick's law).

### Primary levers
- **Size and weight**: Most important element clearly largest/boldest. At least 3 levels of contrast/importance (primary, secondary, tertiary).
- **Color and contrast**: High-saturation accent sparingly for primary actions. WCAG contrast: 4.5:1 body text, 3:1 large text (AA).
- **Position**: Primary content/actions near top of viewport. Align major headings and CTAs along F/Z scan paths.

### Type scale
- Use consistent ratios: modular 1.25× or 1.333×.
- Common web base: 16px body. Example: 16, 20, 25, 31, 39px (body through H1).
- Avoid more than 3 simultaneous contrast levels — too many weights/colors flatten hierarchy.

---

## Accessibility

Design for people with visual, motor, auditory, cognitive, and situational differences.

### Contrast
- **Text (AA)**: 4.5:1 normal, 3:1 large (≥18pt or ≥14pt bold).
- **Text (AAA)**: 7:1 normal, 4.5:1 large.
- **Non-text UI components (AA)**: ≥3:1 against adjacent colors (WCAG 1.4.11).

### Focus indicators
- WCAG 2.4.7: keyboard focus must be visible.
- Use focus ring/outline visually distinct from hover, with good contrast.
- Never remove focus outlines without accessible replacement.

### Touch targets
- 44×44 CSS px (AAA, strongly encouraged).
- 24×24 CSS px (minimum).
- Apple HIG: minimum 44×44pt.

### Semantic structure
- Use semantic elements and landmarks (headings, lists, nav, main, form).
- Interactive controls must be actual buttons/links or have correct ARIA roles.

### Motion sensitivity
- Use `prefers-reduced-motion` to suppress/simplify animations.
- Provide non-animated alternatives. Avoid auto-playing large animations.

### Universal benefit
- Higher contrast, larger targets, clear focus indicators improve usability for ALL users.

---

## White Space and Spacing

### Micro white space (inside components)
- 4–8px base unit for intra-component spacing.
- 4px for tight relationships (label–value, icon–label).
- 8–12px between closely related controls.
- Align text to 4px or 8px vertical baseline grid.

### Macro white space (between groups/sections)
- 8px spacing system: 8, 16, 24, 32, 40, 48, 64, 80px.
- 32–80px for page-level separation and hero sections.

### When to adjust density
- **Increase white space**: Scanning high-stakes/unfamiliar content, reading/interpretation tasks, calm/luxury/focus brand.
- **Increase density**: Expert users comparing many data points, constrained screen with well-learned tasks, provide density toggle options.

### Practical ranges
- Content-heavy pages: 24–40px between sections.
- Dense admin/data UIs: 16–24px between groups, 8–12px between related controls.

---

## Proximity and Grouping

### Relative spacing ratios
- Inside a group: meaningfully smaller than between groups. Ratio ~1:2 or 1:3.
- Forms: label–field spacing < inter-field spacing.

### Concrete ranges (8px scale)
- Tightly related items (icon + label, label + field): 4–8px.
- Items in same group (list items in card, radio buttons in set): 8–12px.
- Separate groups within a panel/card: 16–24px.
- Logically distinct sections on page: 32–80px.

### Key rule
- Place action controls immediately adjacent to content they affect.
- Avoid mixing unrelated controls inside the same tight cluster.

---

## Consistency and Pattern Reuse

### Component-level
- Single documented set of core components with clear variant guidance.
- Centralized design tokens for color, spacing, typography.

### Interaction-level
- Reuse layout and interaction structure for similar flows.
- Consistent navigation patterns across sections.

### Platform conventions
- iOS: nav bars top, tab bars bottom, 44×44pt targets, standard gestures.
- Android: top app bars, FAB placement, 48×48dp targets, standard nav bar.
- Jakob's Law: people spend most time using other products — reuse ecosystem patterns.

### Cost of inconsistency
- Forces recognition-then-verification loops: "Is this the same action?"
- Major driver of abandonment (Baymard benchmarking).

---

## Typography

### Size guidelines
- Body text: 16–18px/pt for standard reading distance.
- iOS: 17pt body, 34pt large titles, 13–15pt secondary, 10pt smallest labels.
- Large text threshold: 18pt regular or 14pt bold (WCAG).

### Line height and length
- Line height: 1.4–1.6× font size for body.
- Line length: 45–75 characters (60–70 for desktop).

### Type scale
- Use semantic tokens (heading.lg, body.md, label.sm).
- Modular ratio: 1.25× or 1.333×.
- Limit to 1 primary UI typeface + 1 optional display face.

### Responsive
- Use relative units (rem, em) for user preference scaling.
- Define breakpoint-aware type tokens.

---

## Color Usage

### Three roles
- **Functional**: Signaling state, actions, feedback.
- **Semantic**: Success (green), warning (amber), error (red), info (blue).
- **Expressive**: Brand and aesthetics.

### Palette construction
- Primary: 1–2 brand hues with 8–10 tonal steps.
- Secondary/accent: 1–2 hues for secondary actions, charts.
- Neutrals: grayscale for backgrounds, borders, text.
- Semantic: success, warning, error, info with background/border/text roles each.

### Dark mode
- Dark neutral background (~#121212).
- Increase luminance range between surfaces instead of inverting.
- Reduce saturation for large colored surfaces.
- Maintain contrast ratios for text and icons.

### Key rule
- Never rely on color alone — significant users have color vision deficiencies.

---

## Responsive and Adaptive Layout

### Breakpoints
- <600px mobile, 600–960px tablet, ≥960/1200px desktop.
- Content-driven breakpoints preferred over device-specific.

### Fluid vs fixed
- Fluid widths for primary content within max-width (1080–1200px).
- Fixed/pinned navigation, FABs for muscle memory.

### Content reflow (small breakpoints)
- Stack columns into single column.
- Collapse secondary controls into menus/overflow.
- Keep primary actions visible.

### Content reflow (large breakpoints)
- Expose secondary functionality inline (filters panel, detail sidebars).

---

## Alignment and Grids

### Grid systems
- 12-column grids for web. 4/8/12/16 responsively.
- IBM Carbon: 4 columns at 320px, 8 at medium, 16 from 1056px+.
- Gutters: 16–32px.

### Base unit
- Single base (4 or 8px) for columns, gutters, component dimensions, spacing tokens.
- Baseline grid: align text to 4px or 8px for vertical rhythm.

### Breaking the grid
- Intentional: offset one hero element for emphasis, modals/toasts on different layer.
- Must be rare and documented; uncontrolled exceptions erode grid benefits.

---

## Information Density

### Card-based layouts
- Cards group related content into digestible units (Gestalt common region + proximity).
- Summary view with expansion for detail.

### Balancing density
- Show primary decision-making attributes in list/grid views.
- Secondary details within one click/tap.
- Expert users: higher density acceptable. New/casual users: more breathing room.
