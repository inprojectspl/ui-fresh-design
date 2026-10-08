# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.1] - 2026-10-08

### Changed

- Rewrote the skill description with concrete trigger situations and Polish request phrases, so agents that route by description alone, such as Claude Code, select the skill reliably.

## [1.2.0] - 2026-10-08

### Added

- Added scoped new-design, existing-product and audit workflows, evidence statuses and representative evaluation tasks.
- Added generated plugin packaging while preserving the marketplace identifier ui-design.

### Changed

- Consolidated repeated instructions and made novelty, font choices, dark mode, loading and complexity estimates depend on product needs.
- Marked historical analysis as superseded and aligned installation and reference documentation.

### Fixed

- Corrected large-text units, text-spacing overrides and target-size interpretation against WCAG 2.2.
- Distinguished selected accessibility checks from a full conformance audit, and disabled semantics from activation and focus behavior.
- Removed contradictory font bans and unsupported measurement or performance claims.

## [1.1.0] - 2026-03-27

### Added
- **Anti-AI-Slop Protocol** - new mandatory section in SKILL.md explaining distributional convergence and defining slop markers across five categories: typography, color, layout, motion, and guidance-level
- **Three mandatory self-checks** before delivering any recommendation: substitution test, convergence test, authorship test
- **Anti-slop gate** in Step 5 quality verification - 8-point originality checklist that must pass before delivery
- **Mandatory structured context diagnosis** (Step 1) - requires product differentiation analysis and session character assessment before any design decisions
- **Rejection justification** requirement in Step 2 - every design direction must name what was considered and rejected
- **Signature element** requirement - every design must identify one intentionally distinctive element
- **7 guidance-level anti-patterns**: safe recommendations, trend name-dropping, font non-decisions, palette hedges, motion hand-waving, layout autopilot, consistency theater
- **7 anti-AI-slop critical rules**: font blacklist (Inter, Roboto, Poppins, Arial, Helvetica), hedge language ban, secondary convergence prevention, signature element mandate
- **Slop-risk ratings** on every visual direction in the design landscape table
- **Anti-AI-slop defenses** section in README.md listing all 9 mechanisms

### Changed
- Design landscape table restructured from "Best for / Watch out for" menu to context-gated decisions with "Use ONLY when / Reject when / Slop risk" columns
- Step 1 renamed from "Context analysis" to "Context diagnosis" with stricter requirements
- Step 2 expanded with font blacklist warnings, border radius default warning, shadow specificity requirement
- Response format template updated to require Context Diagnosis, Rejection justification, Signature element, and Motion Strategy
- Critical Rules section expanded from 10 to 17 rules (split into design rules and anti-slop rules)
- Anti-patterns section expanded from 10 to 17 entries (split into visual and guidance-level)
- README repositioned around anti-AI-slop as core capability
- README "What makes it different" table expanded from 6 to 8 rows
- Skill description in YAML frontmatter updated to mention anti-AI-slop defenses

## [1.0.1] - 2026-03-26

### Fixed
- Repository URL corrected in installation instructions (README.md)

## [1.0.0] - 2026-03-26

### Added
- Initial release of ui-fresh-design Claude Code skill
- SKILL.md with 6 core principles, 5-step execution workflow, quality verification checklist, 10 anti-patterns, 10 critical rules
- 2026 design landscape reference knowledge (8 visual directions, 5 interaction patterns)
- Machine Experience (MX) awareness section
- Dark mode implementation standard
- Cost signals system (LOW / MEDIUM / HIGH)
- Response format templates for design planning, review/audit, and component implementation
- `references/color-systems.md` - palette construction, contrast verification, dark mode rules, product-type archetypes
- `references/typography-guide.md` - type scale, font selection guidelines, variable font implementation, font overuse warnings
- `references/animation-patterns.md` - functional motion philosophy, duration guidelines, CSS-first approach, reduced motion support, performance budget
- `references/accessibility-checklist.md` - complete WCAG 2.2 AA checklist (perceivable, operable, understandable, robust) with common component patterns and testing workflow
- `references/component-patterns.md` - universal state matrix, layout patterns (Bento Grid, Sidebar + Content, Split), common components, empty state guidelines, responsive breakpoint strategy
- ANALYSIS.md with design rationale, competitor skill analysis, and example invocations
- README.md with installation instructions (clone, user-level, submodule), file structure, workflow explanation
- MIT License

[1.1.0]: https://github.com/inprojectspl/ui-fresh-design/compare/v1.0.1...v1.1.0
[1.0.1]: https://github.com/inprojectspl/ui-fresh-design/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/inprojectspl/ui-fresh-design/releases/tag/v1.0.0

[Unreleased]: https://github.com/inprojectspl/ui-fresh-design/compare/v1.2.1...HEAD
[1.2.1]: https://github.com/inprojectspl/ui-fresh-design/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/inprojectspl/ui-fresh-design/releases/tag/v1.2.0
