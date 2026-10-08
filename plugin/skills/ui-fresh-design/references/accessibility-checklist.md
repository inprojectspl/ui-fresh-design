# Selected accessibility checks for WCAG 2.2

Use the checks relevant to the affected UI. This is a practical subset with implementation recommendations, not a complete A/AA conformance audit. Mark missing evidence as `not verified`; automated scans do not cover every criterion. The [WCAG 2.2 standard](https://www.w3.org/TR/WCAG22/) defines requirements and exceptions. Numeric recommendations below are identified separately.

---

## Perceivable

### Color and contrast
- [ ] Text contrast ratio >= 4.5:1 (normal text) and >= 3:1 (large text >= 18 pt = 24 CSS px, or bold >= 14 pt = 18 2/3 CSS px)
- [ ] Visual information needed to identify controls/states and meaningful graphics meets 1.4.11 (3:1 against adjacent colors), subject to its exceptions
- [ ] Author-styled focus indicators meet applicable non-text contrast requirements; verify visibility separately
- [ ] Information is never conveyed by color alone (add icons, patterns, or text labels)
- [ ] Both light and dark themes independently meet all contrast requirements

### Images and media
- [ ] All informative images have descriptive alt text
- [ ] Decorative images use `alt=""` or are CSS backgrounds
- [ ] Complex images (charts, diagrams) have extended descriptions
- [ ] Video has captions; audio has transcripts

### Text and readability
- [ ] Text can be resized to 200% without loss of content or function
- [ ] Applicable text tolerates user overrides together without loss of content/function: line height 1.5x, paragraph spacing 2x, letter spacing 0.12em and word spacing 0.16em (1.4.12). These are override test settings, not required defaults.
- [ ] Reflow (1.4.10) works at 320 CSS px width for vertically scrolling content, or 256 CSS px height for horizontally scrolling content, with the criterion's two-dimensional-content exceptions. A 200% resize test alone does not establish reflow.
- [ ] No text in images (use real text with CSS styling)

---

## Operable

### Keyboard
- [ ] Controls are keyboard reachable using the appropriate pattern: Tab between widgets, arrows within applicable composite widgets; native disabled controls may be skipped
- [ ] Tab order matches visual reading order
- [ ] Focus is visible on all interactive elements (never `outline: none` without replacement)
- [ ] Custom focus styles are at least as visible as browser defaults
- [ ] No inescapable keyboard traps; a modal may contain Tab while open if users can close it by keyboard and focus returns appropriately
- [ ] Modal dialogs trap focus correctly and return focus on close
- [ ] Skip-to-content link is present and functional
- [ ] Custom components (dropdowns, tabs, accordions) follow WAI-ARIA patterns

### Touch targets
- [ ] Pointer targets satisfy 2.5.8: at least 24x24 CSS px, or a documented exception (spacing, equivalent control, inline, user-agent control, essential). For undersized targets, the spacing exception tests nonintersecting 24 CSS px diameter circles centered on their bounding boxes against other targets/circles.
- [ ] Prefer 44x44 CSS px targets when practical. An 8px gap can be a design heuristic, but does not replace 2.5.8's geometric test.

### Focus, dragging and authentication
- [ ] Keyboard focus is not entirely hidden by author-created content such as sticky headers (2.4.11); keeping it fully visible is the stronger usability goal
- [ ] Dragging has a single-pointer alternative without dragging unless essential or user-agent controlled (2.5.7); keyboard support alone is insufficient
- [ ] Authentication does not require a cognitive-function test without an allowed alternative/assistance/exception (3.3.8). Support password managers and paste; inspect the actual flow

### Motion and timing
- [ ] `prefers-reduced-motion` is respected for all animations
- [ ] No content flashes more than 3 times per second
- [ ] Auto-playing content can be paused, stopped, or hidden
- [ ] Users have enough time to read and interact (no aggressive timeouts without warning)

---

## Understandable

### Navigation
- [ ] Pages have descriptive `<title>` elements
- [ ] Headings form a logical hierarchy (h1 -> h2 -> h3, no skipping)
- [ ] Navigation is consistent across pages
- [ ] Current page/section is indicated in navigation
- [ ] Breadcrumbs present for deep hierarchies

### Forms
- [ ] All inputs have visible, associated `<label>` elements
- [ ] Required fields are clearly indicated (not just by asterisk color)
- [ ] Error messages identify the field and describe the correction needed
- [ ] Error messages appear near the field, not just at the top of the form
- [ ] Autocomplete attributes used for common fields (name, email, address, etc.)
- [ ] Form validation does not rely solely on color (red border insufficient alone)

### Language
- [ ] `lang` attribute set on `<html>`
- [ ] Language changes within content marked with `lang` attribute

---

## Robust

### Semantic HTML
- [ ] Use correct HTML elements: `<button>` for actions, `<a>` for navigation, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`
- [ ] Do NOT use `<div>` with click handlers instead of `<button>`
- [ ] ARIA roles used only when native HTML cannot express the pattern
- [ ] ARIA states (`aria-expanded`, `aria-selected`, `aria-checked`) updated dynamically
- [ ] `aria-live` regions used for dynamic content updates (toasts, status messages)
- [ ] Custom components tested with screen readers (VoiceOver, NVDA)

### Common patterns

**Modal dialog:**
- role="dialog" + aria-modal="true"
- aria-labelledby pointing to visible title
- Focus trapped inside modal
- Escape key closes modal
- Focus returns to trigger element on close

**Tabs:**
- role="tablist" on container
- role="tab" on each tab, role="tabpanel" on each panel
- aria-selected on active tab
- Arrow keys navigate between tabs
- Tab key moves into panel content

**Accordion:**
- `<button>` as trigger with aria-expanded
- aria-controls pointing to content panel
- Content panel has role="region" with aria-labelledby

**Toast/notification:**
- role="status" or role="alert" (alert for errors only)
- aria-live="polite" (or "assertive" for critical)
- Must not steal focus from current task
- Provide dismiss mechanism

---

## Testing workflow

1. **Automated**: Scan affected pages and states using axe or Lighthouse; report scope and remaining manual checks
2. **Keyboard**: Tab through entire page without mouse
3. **Screen reader**: Test critical flows with VoiceOver (Mac) or NVDA (Windows)
4. **Zoom**: Test at 200% zoom, verify no content loss
5. **Reduced motion**: Enable reduced motion in OS settings, verify graceful degradation
6. **High contrast**: Test with Windows High Contrast Mode or forced-colors media query

## Interpretation notes and sources

Text contrast exceptions include inactive controls, incidental text and logotypes; keep disabled labels usable even when exempt. Do not round a failing contrast ratio upward. Contrast rules belong here; palette guides link here.

- [Contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- [Text spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html)
- [Target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- [Keyboard interface patterns](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/)

Recommendations such as breadcrumbs, adjacent error placement, heading structure and preferred target sizes support usability; they are not a substitute for mapping the applicable success criteria. Media checks must account for prerecorded/live and audio/video distinctions.
