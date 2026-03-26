# ui-fresh-design

A Claude Code skill that delivers opinionated, buildable UI/UX guidance for web applications — grounded in 2026 design trends, with built-in accessibility, performance awareness, and implementation cost signals.

## What it does

When activated, this skill turns Claude into a senior product designer and frontend architect who:

- **Plans** visual direction for new interfaces (colors, typography, layout, motion)
- **Reviews** existing UIs for quality, trend alignment, and accessibility gaps
- **Guides** component design with full state coverage (hover, focus, error, empty, loading)
- **Provides** framework-specific implementation guidance (React, Next.js, Vue, Svelte, Tailwind, shadcn/ui)
- **Tags** every recommendation with an implementation cost signal (LOW / MEDIUM / HIGH)

## What makes it different

| Problem with existing UI skills | How ui-fresh-design solves it |
|---|---|
| Style catalogs with 67 options ("pick one") | Analyzes context, recommends ONE direction with rationale |
| Zero accessibility guidance | WCAG 2.2 AA woven into every step |
| No performance awareness | Core Web Vitals are a design constraint |
| Generic "make it clean and modern" advice | Exact color values, font names, spacing values |
| Trend-chasing without substance | Trends applied only when they solve a real problem |
| Art direction without implementation reality | Every recommendation includes cost and complexity |

## Installation

### Claude Code (CLI / Desktop / Web)

**Option A — Clone into project skills:**

```bash
cd your-project
git clone https://github.com/YOUR_USERNAME/ui-fresh-design .claude/skills/ui-fresh-design
```

**Option B — Clone into user-level skills (available in all projects):**

```bash
git clone https://github.com/YOUR_USERNAME/ui-fresh-design ~/.claude/skills/ui-fresh-design
```

**Option C — Add as a git submodule:**

```bash
cd your-project
git submodule add https://github.com/YOUR_USERNAME/ui-fresh-design .claude/skills/ui-fresh-design
```

### Verify installation

In Claude Code, type:

```
/skills
```

You should see `ui-fresh-design` in the list. Then just ask Claude to do any UI/UX work — the skill activates automatically based on context.

### Manual trigger

You can also invoke it directly:

```
/ui-fresh-design redesign the settings page for our SaaS app
```

## File structure

```
ui-fresh-design/
  SKILL.md                                # Main skill file (loaded by Claude)
  ANALYSIS.md                             # Design rationale and research synthesis
  references/
    color-systems.md                      # Palette construction, contrast, dark mode
    typography-guide.md                   # Font pairing, variable fonts, type scale
    animation-patterns.md                 # Motion principles, CSS vs JS, performance
    accessibility-checklist.md            # WCAG 2.2 AA complete checklist
    component-patterns.md                 # Layout patterns, states, responsive rules
```

The `references/` folder uses Claude's progressive disclosure — files are loaded only when Claude needs the detailed guidance, keeping the main context lean.

## How it works

The skill follows a structured workflow:

1. **Context analysis** — Understands product type, audience, constraints, existing stack
2. **Design direction** — Proposes one opinionated direction with full specifications
3. **Layout and components** — Defines hierarchy, components, states, responsive behavior
4. **Implementation guidance** — Framework-specific code direction and patterns
5. **Quality verification** — Checks against visual quality, UX, accessibility, performance, and implementation realism checklists

## 2026 design knowledge built in

The skill has internalized current trends and knows when to apply them:

- Liquid Glass / Glassmorphism (with legibility safeguards)
- Bento Grid layouts
- Variable fonts and kinetic typography
- Mature dark mode (dark grey, not black; separate palettes)
- Agentic UX patterns
- Machine Experience (MX) — semantic HTML for AI agents
- Neo-Brutalism / Cute-alism (with usability guardrails)
- Nature-Distilled and Dopamine color strategies

It also actively rejects anti-patterns: meaningless parallax, unreadable glass effects, purple-gradient-on-white, AI-generated design systems without UX strategy, and accessibility as afterthought.

## Example prompts

```
Design a dashboard for a fleet management SaaS. We use Next.js + Tailwind + shadcn/ui.
```

```
Review this mockup for trend alignment and accessibility issues. [attach screenshot]
```

```
Plan the visual direction for a fitness app onboarding flow. Mobile-first.
```

```
Our settings page looks dated. How should we modernize it? We use React + Radix UI.
```

```
I need a data table component with sorting, filtering, and pagination.
Accessible, responsive, works in dark mode.
```

## License

MIT
