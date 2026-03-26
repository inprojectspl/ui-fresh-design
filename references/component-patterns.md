# Component Patterns Reference

## Universal state matrix

Every interactive component MUST define these states. If a state is not applicable, explicitly mark it N/A.

| State | Visual treatment | Notes |
|-------|-----------------|-------|
| Default | Base appearance | |
| Hover | Subtle shift (background, shadow, scale) | Desktop only; must not be required for functionality |
| Focus | Visible focus ring (2px+ solid, 3:1 contrast) | MUST be distinct from hover |
| Active/Pressed | Pressed appearance (slightly darker, inset) | Confirms the click registered |
| Disabled | Reduced opacity (0.4-0.5) or muted colors | Remove from tab order; add aria-disabled |
| Loading | Spinner, skeleton, or shimmer | Preserve layout dimensions; announce to screen readers |
| Error | Red/destructive border + error message | Message must be programmatically associated |
| Empty | Illustration or helpful message + action | Never show just "No data" |
| Selected | Checked, highlighted, or outlined | aria-selected or aria-checked |

---

## Layout patterns

### Bento Grid (2026 staple)
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
- Keyboard navigable with arrow keys within groups
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
1. Mobile layout is the DEFAULT. Larger screens add complexity, not the reverse.
2. Navigation: bottom bar or hamburger on mobile, sidebar on desktop
3. Multi-column layouts collapse to single column on mobile
4. Touch targets: minimum 44px on mobile
5. Font sizes: allow body text to scale naturally; headings may reduce on mobile
6. Tables: horizontal scroll wrapper on mobile, or restructure as cards
7. Modals: full-screen sheet on mobile, centered dialog on desktop
