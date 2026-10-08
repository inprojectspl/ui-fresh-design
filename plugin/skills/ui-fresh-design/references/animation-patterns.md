# Animation Patterns

## Core principle
Every animation must pass this test: "If I remove this animation, does the user lose information or context?" If the answer is no, the animation is decorative and should be the FIRST thing cut when performance budget is tight.

## When to animate

| Trigger | Purpose | Example |
|---------|---------|---------|
| State change | Confirm action completed | Button loading -> success checkmark |
| Navigation | Maintain spatial context | Page slide transitions, panel open/close |
| Data loading | Reduce perceived wait time | Skeleton screens, shimmer effects |
| Attention guidance | Direct user to important element | Toast notification entrance, badge pulse |
| Progressive reveal | Build narrative, reduce cognitive load | Scroll-triggered content fade-in |
| Hover/focus feedback | Confirm interactivity | Button scale, card lift, link underline |

## When NOT to animate

- Body text appearing (just show it)
- Every single list item with staggered delays (one is fine, 20 is torture)
- Background decorative elements that loop infinitely
- Anything that plays on repeat without user interaction
- Anything that takes > 500ms for a simple state change

## Duration guidelines (adjustable defaults)

| Type | Duration | Easing |
|------|----------|--------|
| Micro-interaction (hover, toggle) | 100-200ms | ease-out |
| State change (expand, collapse) | 200-300ms | ease-in-out |
| Page transition | 250-400ms | ease-out or custom cubic-bezier |
| Entrance animation | 300-500ms | ease-out |
| Complex orchestration | 500-800ms total | Staggered with 50-100ms delays |

## CSS-first approach

Always try CSS before reaching for a JS animation library.

### CSS transitions (use for simple state changes)
```css
.button {
  transition: background-color 150ms ease-out, transform 150ms ease-out;
}
.button:hover {
  background-color: var(--action-primary-hover);
  transform: translateY(-1px);
}
.button:active {
  transform: translateY(0);
}
```

### CSS keyframes (use for entrance animations, loading states)
```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.card {
  animation: fadeInUp 300ms ease-out both;
}

/* Staggered entrance for a list */
.card:nth-child(1) { animation-delay: 0ms; }
.card:nth-child(2) { animation-delay: 75ms; }
.card:nth-child(3) { animation-delay: 150ms; }
/* Cap at 4-5 items, then use IntersectionObserver for the rest */
```

### CSS scroll-driven animations (modern, performant)
```css
@keyframes reveal {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}

.scroll-reveal {
  animation: reveal linear both;
  animation-timeline: view();
  animation-range: entry 0% entry 30%;
}
```

## When to use JS animation libraries

Use Motion (formerly Framer Motion) for React, or GSAP for framework-agnostic:

- Layout animations (animating between DOM positions)
- Orchestrating complex sequences with dependencies
- Spring physics (natural-feeling motion)
- Gesture-driven animations (drag, swipe)
- Animating SVG paths
- Scroll-triggered sequences with precise control

## Reduced motion

MANDATORY: Always respect user preferences.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

For JS libraries, check the preference:
```js
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
```

Do NOT remove animations entirely for reduced-motion users if the animation conveys information. Instead, replace motion with instant state changes (opacity: 0 -> 1 without transform).

## Performance budget

- Agree on an animation JS budget using the existing stack; 20KB gzipped is an example budget, not a standard
- Prefer `transform` and `opacity` for avoiding layout work; compositing is not guaranteed, so profile the actual animation
- Layout-affecting properties can be costly; use them only when the behavior requires them and profiling supports the cost
- Use `will-change` sparingly and only on elements about to animate
- Test on low-end devices: animations that are smooth on M3 MacBooks may stutter on budget Android phones
