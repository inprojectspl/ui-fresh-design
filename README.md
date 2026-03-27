# ui-fresh-design

A Claude Code skill that delivers opinionated, buildable UI/UX guidance for web applications — and actively fights the generic, over-smoothed design output that AI models produce by default.

## The problem this skill solves

AI models suffer from **distributional convergence**: they predict tokens from the statistical center of their training data, producing the "average of modern web design." The result is Inter fonts, purple gradients, three-column card grids, and recommendations like "use a clean color palette with a professional blue primary." This is **AI slop** — design guidance that sounds professional but makes no real decisions and could apply to any product.

ui-fresh-design forces Claude to fight this tendency. Every recommendation must be grounded in the specific product context, pass explicit anti-slop checks, and reflect a genuine design judgment — not a statistical default.

## What it does

When activated, this skill turns Claude into a senior product designer and frontend architect who:

- **Diagnoses** the product context before making any visual decisions (mandatory, structured, non-skippable)
- **Commits** to a single opinionated direction with explicit justification — not a menu of options
- **Plans** visual direction with exact specifications (colors, typography, layout, motion, signature element)
- **Reviews** existing UIs for quality, trend alignment, accessibility gaps, and AI-slop markers
- **Guides** component design with full state coverage (hover, focus, error, empty, loading)
- **Self-checks** every recommendation against originality tests (substitution, convergence, authorship)
- **Tags** every recommendation with an implementation cost signal (LOW / MEDIUM / HIGH)

## What makes it different

| Problem | How ui-fresh-design solves it |
|---|---|
| AI defaults to generic "modern SaaS" output | Built-in anti-AI-slop protocol with mandatory self-checks (substitution test, convergence test, authorship test) |
| Style catalogs with 67 options ("pick one") | Analyzes context, recommends ONE direction, names what was rejected and why |
| Recommendations that could apply to any product | Mandatory context diagnosis before any design decisions; every recommendation must reference the diagnosis |
| No originality verification | Anti-slop gate in quality checklist: font specificity, color dominance, layout justification, signature element |
| Zero accessibility guidance | WCAG 2.2 AA woven into every step |
| No performance awareness | Core Web Vitals as a design constraint |
| Trend-chasing without substance | Trends context-gated by product fit, with explicit slop-risk ratings |
| Art direction without implementation reality | Every recommendation includes cost signals and trade-off analysis |

## Installation

### Claude Code (CLI / Desktop / Web)

**Option A — Clone into project skills:**

```bash
cd your-project
git clone https://github.com/inprojectspl/ui-fresh-design .claude/skills/ui-fresh-design
```

**Option B — Clone into user-level skills (available in all projects):**

```bash
git clone https://github.com/inprojectspl/ui-fresh-design ~/.claude/skills/ui-fresh-design
```

**Option C — Add as a git submodule:**

```bash
cd your-project
git submodule add https://github.com/inprojectspl/ui-fresh-design .claude/skills/ui-fresh-design
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

The skill follows a structured workflow with anti-slop enforcement at every stage:

1. **Context diagnosis** (mandatory) — Structured analysis of product type, audience, session character, job-to-be-done, and competitive differentiation. Must be completed before any design decisions.
2. **Design direction** — Proposes ONE opinionated direction with full specifications. Names what was rejected and why. Identifies a signature element. Runs anti-convergence check.
3. **Layout and components** — Defines hierarchy, components, states, responsive behavior — justified by content structure, not trend popularity.
4. **Implementation guidance** — Framework-specific code direction and patterns with cost signals.
5. **Quality verification with anti-slop gate** — Checks against originality (substitution, convergence, authorship tests), visual quality, UX, accessibility, performance, and implementation realism.

## Anti-AI-slop defenses

The skill embeds specific mechanisms to prevent distributional convergence:

- **Mandatory context diagnosis** before any visual decisions — no guessing product context
- **Substitution test**: could the recommendation apply to a different product? If yes, it's too generic
- **Convergence test**: would 10 runs produce the same output? If yes, the model is sampling from the statistical center
- **Authorship test**: does a human designer recognize this as a deliberate choice? If not, it's filler
- **Explicit font blacklist** for AI-default fonts (Inter, Roboto, Poppins) unless already in the user's system
- **Secondary convergence prevention**: banning one default must not create a new default (e.g., always using Geist)
- **Rejection justification**: every design direction must name what was considered and rejected
- **Signature element requirement**: every design must have one intentionally distinctive element
- **Guidance-level anti-patterns**: catches not just visual clichés but recommendation clichés (hedge words, palette hedges, font non-decisions, layout autopilot)

## 2026 design knowledge built in

The skill has internalized current trends — but applies them only when context-justified, never for trend signaling:

- Liquid Glass / Glassmorphism (high slop-risk — only when backgrounds are controlled)
- Bento Grid layouts (medium slop-risk — only when content naturally varies in importance)
- Variable fonts and kinetic typography (hero/storytelling only, never body text)
- Mature dark mode (dark grey, not black; separate palettes)
- Agentic UX patterns (transparency and escape hatches mandatory)
- Machine Experience (MX) — semantic HTML for AI agents
- Neo-Brutalism (low slop-risk, but context-gated to brands that fit)
- Nature-Distilled and Dopamine color strategies (each gated by session type)

It actively rejects both visual anti-patterns (meaningless parallax, unreadable glass, purple-gradient-on-white) and guidance-level anti-patterns (safe recommendations, trend name-dropping, font non-decisions, layout autopilot).

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
