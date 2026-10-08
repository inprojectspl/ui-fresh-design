# ui-fresh-design

Design, implement and review web interfaces with concrete decisions grounded in user goals, product content and the existing design system.

The skill has three scopes: new design/exploration, a focused existing-product change, and audit. It preserves the emphasis on specificity, accessibility, useful states and implementation cost without requiring novelty, a font blacklist or a redesign for every fix. Requested variants are supported.

The accessibility reference covers selected WCAG 2.2 checks, not a complete AA audit. Reports distinguish verified measurements, estimates, unverified areas and non-applicable checks. Core Web Vitals budgets, lab measurements and field data are separate. Aesthetic quality still needs human judgment.

## Installation

### AI Marketplace

The plugin is distributed through `inprojects-ai-tools` from this repository's `plugin/` directory, pinned to tag `v1.2.0`. After the tag and marketplace update are published, install it in Claude Code:

```text
/plugin install ui-design@inprojects-ai-tools
```

For Codex, refresh the marketplace and select `ui-design` in the plugin directory, or use the commands supported by your installed CLI. The contained skill is `ui-fresh-design`. For UI design, the existing plugin selector `ui-design` is preserved.

### Standalone project or user installation

Keep a source checkout outside the application's skills directory, then export only the skill files. This avoids a nested `.git` directory and excludes generated plugin copies and evaluations:

```sh
skill_checkout=$(mktemp -d)
git clone --branch v1.2.0 --depth 1 https://github.com/inprojectspl/ui-fresh-design.git "$skill_checkout/source"
mkdir -p .claude/skills/ui-fresh-design
git -C "$skill_checkout/source" archive HEAD SKILL.md references LICENSE | tar -x -C .claude/skills/ui-fresh-design
```

Commit that ordinary directory in the parent project. For Claude user installation replace the destination with `~/.claude/skills/ui-fresh-design`. For Codex use `.agents/skills/ui-fresh-design` or `~/.agents/skills/ui-fresh-design`. Copy both `SKILL.md` and `references/`; copying only the entrypoint is insufficient. Existing root-level `SKILL.md` paths remain available.

To update, review the next release, fetch/check out its tag in the source checkout, repeat the archive export and commit the resulting diff. Review removed reference files as well; archive extraction does not delete obsolete files.

If the team deliberately uses submodules, configure one explicitly instead of committing an ordinary nested clone:

```sh
git submodule add https://github.com/inprojectspl/ui-fresh-design.git .claude/skills/ui-fresh-design
git -C .claude/skills/ui-fresh-design checkout v1.2.0
git add .gitmodules .claude/skills/ui-fresh-design
```

Other clones need `git submodule update --init --recursive` (or `git clone --recurse-submodules`). To update, fetch/check out the new tag within the submodule and commit the new gitlink in the parent. A submodule includes authoring/package files; prefer the archive method when only skill resources should be installed.

## Usage and results

- "Fix this button's focus without redesigning the page" preserves typography, palette and layout.
- "Design three dashboard variants for fleet dispatchers" provides grounded alternatives.
- "Audit this settings page" reports evidence, consequences and fixes without claiming unmeasured compliance.

The skill uses conditional references for color, typography, motion, components and selected accessibility checks. `ANALYSIS.md` is explicitly historical authoring context from March 2026, superseded by current instructions; its examples are not empirical evaluations.

## Maintenance and verification

`SKILL.md` and `references/` at the repository root are the authoring sources. `plugin/.claude-plugin/plugin.json` holds the release metadata. The generated `plugin/skills/`, portable `plugin/plugin.json` and compatibility `.codex-plugin/plugin.json` are committed so installing a tag requires no build step:

```sh
python3 scripts/package_plugin.py
python3 scripts/package_plugin.py --check
claude plugin validate plugin
```

This preserves standalone source paths while providing conventional plugin packaging for both runtimes. Generated files must not be edited directly. No MCP server, hook, extra permission or explicit-only invocation policy is required.

See [evaluation record](evals/README.md) for audit decisions, executable examples, exact versions and limitations. Example execution and agent behavioral evaluation are separate. See [CHANGELOG](CHANGELOG.md) for releases.

## License

MIT.
