---
name: ui-fresh-design
description: Design, implement, and review web UI/UX grounded in the product's users, existing design system, accessibility, and performance. Use for screens, components, visual direction, and UI improvements; excludes backend-only work, brand strategy, and native mobile design.
---

# ui-fresh-design

Produce specific, buildable UI decisions tied to the user's task. Preserve the product's identity and conventions. Familiar patterns are useful when they fit; novelty is not a quality requirement.

## Choose the scope

- **New interface or visual exploration:** establish the primary user task, audience, content, constraints and existing assets. Recommend a coherent direction with concrete tokens and component behavior. Provide variants when requested or when material trade-offs warrant them. A signature detail is optional when it serves the product.
- **Existing product change:** inspect code, tokens, components and conventions first. Make the smallest change that solves the requested problem. A focus fix does not require new typography, a palette or competitor research.
- **Audit:** report located findings, evidence, user impact and actionable corrections. Separate accessibility defects from aesthetic preferences. Do not implement a redesign unless requested.

Infer context from available material. Ask only about unknowns that materially affect the decision. State reasonable assumptions; do not force a questionnaire or a fixed report template on a small task.

## Decision priorities

1. **Intent before aesthetics.** Define the main action, information hierarchy and the states users need: loading, error, empty, focus and recovery. Clear but plain is valid.
2. **Product fit before trends.** Explain concrete choices in terms of content and workflow. Avoid generic advice such as "make it modern". Popular fonts, standard grids and sidebars are not defects by themselves. Do not replace one automatic style choice with another.
3. **Accessibility from the start.** Use semantic HTML, appropriate labels, predictable keyboard behavior and reduced-motion alternatives. Design toward the applicable WCAG target, usually 2.2 AA; a checklist or automated scan alone cannot establish conformance.
4. **Implementation realism.** Reuse the user's stack and design system. Assess dependencies and heavy visuals against the main task, device constraints and performance budget. Group related changes by complexity where useful; time estimates require stated assumptions.
5. **Evidence before claims.** Distinguish normative requirements, recommended defaults and aesthetic heuristics. Explain exceptions using the task and the relevant standard's scope.

## Workflow

### Inspect

Read the affected UI, tokens, layout, dependencies and available screenshots or design files. Identify the actual problem and primary user action. For a new design, establish audience, density, visual tone and constraints; for a local fix, inspect only what affects it.

### Specify

For a new direction or requested redesign, define concrete colors by semantic role, typography, spacing, radius, elevation and responsive behavior. Use one or more font families based on language coverage, legibility, loading cost and product fit. Specify what moves, when, for how long and why. Explain material trade-offs; do not require a surprising element or an originality score.

For each changed component, cover relevant states and recovery, keyboard behavior, focus order, names and relationships. Choose breakpoints from content and supported devices. Respect reflow and zoom without automatically redesigning a desktop workflow as a mobile application.

### Implement

Use the existing component library and project conventions. Preserve scope and the established design system. Prefer native controls and semantic structure over custom ARIA. For color, motion and component details, load only the relevant reference below.

Dark mode is a product decision, not a rule triggered by session length. If included, design and test palettes independently, respect system preference and the project's choice persistence. Pure black or white is not prohibited by a standard.

Defer noncritical heavy components when that helps loading. Do not blindly lazy-load the map or chart that is the user's primary screen. Preload fonts selectively; measure competition with other critical resources.

### Verify and report

Check the affected states, keyboard paths, responsive layout and reduced motion with available tools. Calculate contrast from actual foreground/background values, including alpha compositing and state changes. A screenshot can reveal risks but cannot certify an entire interface.

Use these statuses when reporting checks:
- **verified:** give the method, result, revision and scope;
- **estimated:** give assumptions and uncertainty;
- **not verified:** name the missing measurement or access;
- **not applicable:** explain why the criterion does not apply.

Separate a design budget from a laboratory measurement and from field Core Web Vitals. Field assessment uses the 75th percentile with mobile and desktop segmented; "good" thresholds are LCP <= 2.5 s, INP <= 200 ms and CLS <= 0.1. Report conditions and available metrics; never infer passing Core Web Vitals from CSS or a mockup. See [Web Vitals](https://web.dev/articles/vitals).

For implementation, report changes and actual relevant check commands/results, plus unverified areas. For a plan, report decisions and assumptions without implying execution. For an audit, prioritize findings by demonstrated impact. Keep the response proportional to the task.

## Load references when needed

- [Accessibility checklist](references/accessibility-checklist.md): when assessing accessibility, focus, contrast, reflow or input patterns; selected checks, not a complete WCAG audit.
- [Color systems](references/color-systems.md): when defining palettes, themes or semantic color tokens.
- [Typography](references/typography-guide.md): when selecting fonts, scales, loading and reading layout.
- [Component patterns](references/component-patterns.md): when designing states, navigation, dialogs or responsive layouts.
- [Animation patterns](references/animation-patterns.md): when adding or reviewing motion and its performance.

Do not load all references for every task. Historical design research is not an additional instruction source.
