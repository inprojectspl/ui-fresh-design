# Component Patterns Reference

## Universal state matrix

Account for relevant states on changed components; mark non-applicable states when useful. Sizes, breakpoints, placement and timing below are adaptable defaults, not WCAG requirements.

| State | Visual treatment | Notes |
|-------|-----------------|-------|
| Default | Base appearance | |
| Hover | Subtle shift (background, shadow, scale) | Desktop only; must not be required for functionality |
| Focus | Clearly visible indicator; a 2px ring is a design starting point | See accessibility checklist for applicable criteria |
| Active/Pressed | Pressed appearance (slightly darker, inset) | Confirms the click registered |
| Disabled | Visibly unavailable while remaining legible | Prefer native `disabled` where appropriate; see behavior below |
| Loading | Spinner, skeleton, or shimmer | Preserve layout dimensions; announce to screen readers |
| Error | Red/destructive border + error message | Message must be programmatically associated |
| Empty | Explain the cause and next useful action, when there is one | A short message can suffice for passive displays |
| Selected | Checked, highlighted, or outlined | aria-selected or aria-checked |

---

## Disabled behavior

Native `disabled` prevents activation on supported controls and normally removes them from Tab order. `aria-disabled="true"` announces a state but does not suppress clicks, keyboard activation, navigation or form behavior; implement that behavior deliberately. Keep or remove focus according to the widget's APG pattern and discoverability needs. Disabled items in some composite widgets remain arrow-key reachable. CSS `pointer-events: none` alone does not disable keyboard activation.

A modal contains focus while open, offers keyboard dismissal, and restores focus. This is different from an inescapable keyboard trap. Ordinary navigation links use Tab/Shift+Tab; arrow keys belong to applicable composite patterns, not every sidebar.

## Layout patterns

### Bento Grid (for content with differing importance)
```css
.bento-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--space-4);
}

/* Feature cards with spanning */
.bento-item--wide { grid-column: span 2; }
.bento-item--tall { grid-row: span 2; }

/* Mobile: single column */
@media (max-width: 640px) {
  .bento-grid { grid-template-columns: 1fr; }
  .bento-item--wide,
  .bento-item--tall { grid-column: span 1; grid-row: span 1; }
}
```

### Sidebar + Content (dashboard staple)
```css
.app-layout {
  display: grid;
  grid-template-columns: 240px 1fr;
  min-height: 100dvh;
}

/* Collapsible sidebar */
.app-layout--collapsed {
  grid-template-columns: 64px 1fr;
}

/* Mobile: overlay sidebar */
@media (max-width: 768px) {
  .app-layout { grid-template-columns: 1fr; }
  .sidebar { position: fixed; transform: translateX(-100%); z-index: 40; }
  .sidebar--open { transform: translateX(0); }
}
```

### Content + Side panel (settings, detail views)
```css
.split-layout {
  display: grid;
  grid-template-columns: 1fr 380px;
  gap: var(--space-6);
}

@media (max-width: 1024px) {
  .split-layout {
    grid-template-columns: 1fr;
  }
  /* Side panel becomes a sheet/drawer on mobile */
}
```

---

## Common component patterns

### Card
- Container with consistent padding (16-24px)
- Optional: image/media area, header, body, footer/actions
- Hover: subtle shadow lift or border change (if clickable)
- Rounded corners matching system radius
- Do NOT make the entire card a link unless there is only one action

### Data table
- Sticky header row
- Horizontal scroll on mobile (inside a container, not the page)
- Row hover highlight
- Sortable columns with aria-sort
- Pagination or virtual scrolling for > 50 rows
- Empty state when no data matches filters
- Loading: skeleton rows matching expected column layout

### Form
- One column for most forms (two-column only for very wide screens with related field pairs)
- Labels ABOVE inputs (not beside -- reduces eye movement)
- Group related fields with fieldset/legend
- Error messages below the field, inline, visible without scrolling
- Submit button at the bottom-left (matches reading flow)
- Disable submit during processing, show loading state

### Navigation (sidebar)
- Sections with clear headings
- Active item visually distinct (background color + text weight, not just color)
- Collapsible groups for deep hierarchies
- Use Tab for ordinary links; use arrows only for an intentionally implemented composite widget pattern
- Responsive: overlay drawer on mobile with backdrop
- Badge indicators for notifications/counts

### Modal / Dialog
- Max width: 480px (small), 640px (medium), 800px (large)
- Centered vertically and horizontally
- Backdrop overlay (semi-transparent dark)
- Close: X button, Escape key, backdrop click
- Focus trapped inside; returns to trigger on close
- Avoid modals inside modals (use a drawer or navigate to a new page instead)

### Toast / Notification
- Position: top-right or bottom-right (consistent throughout app)
- Auto-dismiss: 4-6 seconds for success, persistent for errors
- Stack with gap when multiple
- Include dismiss button
- role="status" (informational) or role="alert" (errors)
- Never block content or require interaction for non-critical messages

---

## Empty state guidelines

Empty states are a design opportunity, not an afterthought.

### Structure
1. Illustration or icon (optional, but helps -- use brand-appropriate imagery)
2. Heading: What this space is for ("Your projects will appear here")
3. Description: Why it is empty and what to do ("Create your first project to get started")
4. Action: Primary CTA button ("Create project")

### Common empty states to design
- First-time user (no data yet)
- Filtered results with no matches ("No results for 'xyz'. Try a different search.")
- Error loading data ("We couldn't load your data. Try again." + retry button)
- Permission denied ("You don't have access. Request access from your admin.")
- Feature not enabled ("Upgrade to Pro to unlock analytics.")

---

## Responsive breakpoint strategy

```css
/* Mobile first */
/* Base styles: < 640px (mobile) */

@media (min-width: 640px)  { /* sm: Tablet portrait */ }
@media (min-width: 768px)  { /* md: Tablet landscape */ }
@media (min-width: 1024px) { /* lg: Desktop */ }
@media (min-width: 1280px) { /* xl: Wide desktop */ }
@media (min-width: 1536px) { /* 2xl: Ultra-wide */ }
```

### Responsive rules
1. Match the supported devices and content; mobile-first CSS is a useful approach, not a universal redesign requirement.
2. Navigation: bottom bar or hamburger on mobile, sidebar on desktop
3. Multi-column layouts collapse to single column on mobile
4. Prefer 44px touch targets; see the accessibility checklist for the normative minimum and exceptions
5. Font sizes: allow body text to scale naturally; headings may reduce on mobile
6. Tables: horizontal scroll wrapper on mobile, or restructure as cards
7. Modals: full-screen sheet on mobile, centered dialog on desktop
