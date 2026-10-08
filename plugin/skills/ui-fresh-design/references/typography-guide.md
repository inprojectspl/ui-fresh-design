# Typography Guide

## Type Scale (recommended)

Use the existing scale or choose a readable hierarchy. The following practical scale is not a strict 1.25 geometric progression; rem comments assume a 16px root:

```css
:root {
  --text-xs:   0.75rem;   /* 12px - captions, labels */
  --text-sm:   0.875rem;  /* 14px - secondary text, metadata */
  --text-base: 1rem;      /* 16px - body text baseline */
  --text-lg:   1.125rem;  /* 18px - emphasized body, card titles */
  --text-xl:   1.25rem;   /* 20px - section headings */
  --text-2xl:  1.5rem;    /* 24px - page section titles */
  --text-3xl:  1.875rem;  /* 30px - page titles */
  --text-4xl:  2.25rem;   /* 36px - hero headings */
  --text-5xl:  3rem;      /* 48px - display/hero (marketing pages only) */

  --leading-tight:  1.25;
  --leading-normal: 1.5;
  --leading-relaxed: 1.75;

  --tracking-tight:  -0.025em;
  --tracking-normal:  0;
  --tracking-wide:    0.025em;
}
```

## Font Selection Guidelines

### Body text requirements
- High x-height for screen readability
- Clear distinction between similar characters (Il1, O0)
- Comfortable at 14-16px
- Available in at least 3 weights (regular, medium, bold)

### Display/heading requirements
- Personality and character
- Works at large sizes (24px+)
- Can be more decorative than body
- Pairs well with the body font (contrast in style, harmony in tone)

### Recommended pairings by product type

**Enterprise SaaS**
- Display: Inter, Geist, General Sans, Satoshi
- Body: Inter, Geist, system-ui stack
- Why: Neutral, professional, highly legible at small sizes

**Developer Tools**
- Display: JetBrains Mono, Berkeley Mono, Geist Mono
- Body: Geist, Inter, system-ui
- Mono: JetBrains Mono, Fira Code, Berkeley Mono
- Why: Monospace-aware, technical character

**Consumer / Lifestyle**
- Display: Cabinet Grotesk, Clash Display, Outfit, Plus Jakarta Sans
- Body: Plus Jakarta Sans, DM Sans, Outfit
- Why: Warm, friendly, distinctive without being distracting

**Editorial / Content**
- Display: Fraunces, Playfair Display, Lora
- Body: Source Serif 4, Literata, Charter
- Why: Serif warmth, readability for long-form content

**Creative / Portfolio**
- Display: Anything distinctive -- Basement Grotesque, Syne, Space Mono, Migra
- Body: Match the energy or deliberately contrast it
- Why: Personality-first, the type IS the design

### Selection rule

No font blacklist applies. Preserve existing type unless the task justifies a change. Choose by legibility, language/glyph coverage, licensing, available files, loading cost and product character. One family can cover headings and body. Examples above are candidates, not mandates; Inter does not require customized tracking to be a valid choice.

## Variable Fonts

Use variable fonts when available. Benefits:
- Single file for all weights and widths
- Enables kinetic typography (weight/width animation)
- Potentially smaller download than many static weights; compare actual files when only a few weights are needed

### Implementation
```css
@font-face {
  font-family: 'MyFont';
  src: url('/fonts/myfont.woff2') format('woff2-variations');
  font-weight: 100 900;
  font-display: swap;
}

/* Animating weight on hover */
.heading {
  font-variation-settings: 'wght' 400;
  transition: font-variation-settings 0.3s ease;
}
.heading:hover {
  font-variation-settings: 'wght' 700;
}
```

### Performance
- Choose `font-display` for the product: `swap` is a common default; assess fallback metrics and layout shift
- Preload only critical font files when measurement supports it: `<link rel="preload" href="/fonts/myfont.woff2" as="font" type="font/woff2" crossorigin>`
- Subset only when required language coverage is preserved; measure savings on actual files
- Prefer few loaded families; additional families need a product reason and measured budget.

## Line length
- Body text: 45-75 characters per line (65 is ideal)
- Use `max-width: 65ch` on text containers
- Constrain prose line length where helpful; dense tabular interfaces have different needs

Honor reduced motion when animating font axes and check for reflow. Read the animation reference when implementing motion.
