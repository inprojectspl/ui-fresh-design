# Color Systems Reference

## Palette Construction Method

### Step 1: Define semantic roles
Every color in the system must have a role, not just a name.

```css
:root {
  /* Surfaces */
  --surface-primary: ;      /* Main background */
  --surface-secondary: ;    /* Cards, panels */
  --surface-tertiary: ;     /* Nested elements, wells */
  --surface-elevated: ;     /* Modals, popovers, dropdowns */

  /* Actions */
  --action-primary: ;       /* Primary CTA */
  --action-primary-hover: ; /* Primary CTA hover */
  --action-secondary: ;     /* Secondary actions */
  --action-destructive: ;   /* Delete, remove, danger */

  /* Text */
  --text-primary: ;         /* Headings, body text */
  --text-secondary: ;       /* Descriptions, labels */
  --text-tertiary: ;        /* Placeholders, disabled */
  --text-on-action: ;       /* Text on action-colored backgrounds */

  /* Borders */
  --border-default: ;       /* Standard borders */
  --border-strong: ;        /* Emphasized borders */
  --border-focus: ;         /* Focus rings */

  /* Semantic */
  --status-success: ;
  --status-warning: ;
  --status-error: ;
  --status-info: ;

  /* Semantic backgrounds (for banners, badges, toasts) */
  --status-success-bg: ;
  --status-warning-bg: ;
  --status-error-bg: ;
  --status-info-bg: ;
}
```

### Step 2: Generate the scale
For each brand color, generate a 10-step scale (50-950) using OKLCH for perceptual uniformity:
- 50-100: Tinted backgrounds
- 200-300: Borders, dividers
- 400-500: Icons, secondary text
- 600-700: Primary interactive elements
- 800-900: Text on light backgrounds
- 950: Near-black for maximum contrast

### Step 3: Map scale to roles
Do not let developers use scale values directly. Map every usage to a semantic token:
- `--blue-600` (BAD - what does blue mean here?)
- `--action-primary` (GOOD - the intent is clear)

## Contrast Verification

### WCAG 2.2 AA Requirements
| Element | Minimum ratio |
|---------|--------------|
| Normal text (< 18px / < 14px bold) | 4.5:1 |
| Large text (>= 18px / >= 14px bold) | 3:1 |
| UI components and graphical objects | 3:1 |
| Focus indicators | 3:1 against adjacent colors |

### Testing method
1. Test every text/background combination in BOTH light and dark themes
2. Test status colors against their background variants
3. Test interactive elements in all states (default, hover, active, disabled, focus)
4. Use tools: Chrome DevTools contrast checker, axe DevTools, or WebAIM contrast checker

## Dark Mode Palette Rules

1. Surface scale in dark mode: #121212 (base) -> #1e1e1e -> #242424 -> #2d2d2d -> #333333
2. Never use pure #000000 as background (causes halation on OLED screens)
3. Never use pure #ffffff for text in dark mode (too harsh). Cap at #f0f0f0.
4. Reduce saturation of brand colors by 10-15% in dark mode to prevent "neon glow" effect
5. Shadows in dark mode: replace `box-shadow` with subtle lighter borders or luminous edges
6. Status colors may need lightened variants in dark mode for readability

## Color palette archetypes for common product types

### Enterprise SaaS / B2B
- Surfaces: Cool grey scale (slate, zinc)
- Action: One saturated primary (blue, indigo, or teal)
- Tone: Professional, restrained, trustworthy
- Avoid: Playful colors, gradients, neon accents

### Consumer / Lifestyle
- Surfaces: Warm neutrals or bold base colors
- Action: Contrasting warm accent
- Tone: Energetic, approachable, distinctive
- Allow: Gradients, dopamine accents, playful combinations

### Developer tools
- Surfaces: Deep dark backgrounds by default
- Action: High-visibility accent (cyan, green, amber)
- Tone: Technical, focused, information-dense
- Allow: Monospace-friendly, syntax-highlighting-aware palettes

### Healthcare / Finance
- Surfaces: Clean whites, light greys
- Action: Conservative blues, greens
- Tone: Trustworthy, calm, regulated
- Avoid: Experimental colors, high-saturation palettes, "AI purple"

### Creative / Portfolio
- Anything goes as long as there is INTENTION behind the choice
- This is where liquid glass, neo-brutalism, dopamine colors shine
- Still must meet accessibility minimums
