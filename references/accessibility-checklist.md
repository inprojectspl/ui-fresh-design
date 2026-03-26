# Accessibility Checklist (WCAG 2.2 AA)

## Use this checklist during Step 5 of the execution workflow.

---

## Perceivable

### Color and contrast
- [ ] Text contrast ratio >= 4.5:1 (normal text) and >= 3:1 (large text >= 18px or bold >= 14px)
- [ ] UI component boundaries have >= 3:1 contrast against adjacent colors
- [ ] Focus indicators have >= 3:1 contrast
- [ ] Information is never conveyed by color alone (add icons, patterns, or text labels)
- [ ] Both light and dark themes independently meet all contrast requirements

### Images and media
- [ ] All informative images have descriptive alt text
- [ ] Decorative images use `alt=""` or are CSS backgrounds
- [ ] Complex images (charts, diagrams) have extended descriptions
- [ ] Video has captions; audio has transcripts

### Text and readability
- [ ] Text can be resized to 200% without loss of content or function
- [ ] Line height is at least 1.5x font size for body text
- [ ] Paragraph spacing is at least 2x font size
- [ ] No text in images (use real text with CSS styling)

---

## Operable

### Keyboard
- [ ] All interactive elements reachable via Tab key
- [ ] Tab order matches visual reading order
- [ ] Focus is visible on all interactive elements (never `outline: none` without replacement)
- [ ] Custom focus styles are at least as visible as browser defaults
- [ ] No keyboard traps (user can always Tab out of any component)
- [ ] Modal dialogs trap focus correctly and return focus on close
- [ ] Skip-to-content link is present and functional
- [ ] Custom components (dropdowns, tabs, accordions) follow WAI-ARIA patterns

### Touch targets
- [ ] Minimum touch target size: 24x24px (WCAG 2.2), recommended 44x44px
- [ ] Adequate spacing between adjacent targets (at least 8px)

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

1. **Automated**: Run axe DevTools or Lighthouse on every page
2. **Keyboard**: Tab through entire page without mouse
3. **Screen reader**: Test critical flows with VoiceOver (Mac) or NVDA (Windows)
4. **Zoom**: Test at 200% zoom, verify no content loss
5. **Reduced motion**: Enable reduced motion in OS settings, verify graceful degradation
6. **High contrast**: Test with Windows High Contrast Mode or forced-colors media query
