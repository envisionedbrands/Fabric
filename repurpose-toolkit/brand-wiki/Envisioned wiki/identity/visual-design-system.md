---
title: Visual Design System
category: identity
confidence: high
sources:
  - envisioned-brand-design.skill
last_updated: 2026-04-14
---

# Visual Design System

> Italian editorial aesthetic — Winter container, Autumn imagery. Presence over performance. Dolce far niente as infrastructure.

---

## The Operating Premise

Envisioned Systems is a **presence brand**, not a performance brand. The work is to make the low volume unmistakable. Nothing shouts. Photography does the emotional work. Typography does the structural work. Whitespace does the luxury work.

> "You don't need a heat dial turned to 10. You need the low volume to be so unmistakably *you* that the room goes quiet when you speak at 3."

**The Brand Test:** Before shipping anything — "Does this look like it belongs in an Italian architecture journal — or a SaaS landing page?" If SaaS, begin again.

---

## The Canonical Palette

**Governing principle:** Cool structure, warm imagery. The container (backgrounds, text, accents) is cool and architectural. The photography is warm and autumn-graded. Never mix the two energies.

### Core Colors

| Token | Hex | Use |
|-------|-----|-----|
| `--canvas` | `#FBFAF9` | Primary background — cool off-white, NEVER warm cream |
| `--canvas-soft` | `#F7F5F0` | Card fills, subtle alternate sections |
| `--stone` | `#EDE9E3` | Section backgrounds, cards, pull-quote blocks |
| `--stone-deep` | `#E3DED5` | Borders, deeper card fills, hover surfaces |
| `--ink` | `#1E1E1E` | Primary text — warm, never pure black |
| `--ink-soft` | `#2C2C2C` | Body copy, secondary text |
| `--olive` | `#4C5A2E` | Primary accent — kickers, rules, CTAs (never gold) |
| `--olive-deep` | `#3A4622` | Hover states, emphasis |
| `--sage` | `#8A9A6B` | Tertiary accent — dashes, dots, closing flourishes |
| `--rose` | `#B87A5D` | Emotional accent — portraits only, use sparingly |
| `--taupe` | `#8A7A68` | Metadata, captions, dates |

### Distribution: 70/20/8/2

- **~70%** canvas + stone (background, whitespace)
- **~20%** ink text
- **~8%** olive structural accent
- **~2%** sage/rose/taupe

If olive is hitting 15%+, pull back. Go thinner, not brighter.

### CSS Variables

```css
:root {
  --canvas:      #FBFAF9;
  --canvas-soft: #F7F5F0;
  --stone:       #EDE9E3;
  --stone-deep:  #E3DED5;
  --ink:         #1E1E1E;
  --ink-soft:    #2C2C2C;
  --olive:       #4C5A2E;
  --olive-deep:  #3A4622;
  --sage:        #8A9A6B;
  --sage-tint:   rgba(138, 154, 107, 0.12);
  --rose:        #B87A5D;
  --rose-tint:   rgba(184, 122, 93, 0.08);
  --taupe:       #8A7A68;
  --hair:        rgba(30, 30, 30, 0.10);
  --hair-olive:  rgba(76, 90, 46, 0.25);
}
```

---

## Typography

### The Two-Font System

**Italiana** does the ceremony. **Cormorant Garamond** does the reading. There is no third font. No sans-serif. No Playfair. No EB Garamond.

```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600&family=Italiana&display=swap" rel="stylesheet">
```

### Type Scale

| Element | Size | Weight | Family |
|---------|------|--------|--------|
| Display xxl | 7rem | 400 | Italiana |
| Display xl | 5.5rem | 400 | Italiana |
| Display lg | 4rem | 400 | Italiana |
| h2 | 2.5rem | 500 | Cormorant Garamond |
| h3 | 1.55rem | 500 | Cormorant Garamond |
| h4 | 1.15rem | 500 | Cormorant Garamond |
| body | 22-24px | 400 | Cormorant Garamond |
| lede | 26px italic | 400 | Cormorant Garamond |
| kicker | 0.72rem | 500 | Cormorant Garamond, UPPERCASE, 0.3em tracking, olive |

**Line height 1.75 on body.** Max paragraph width 38em. No line exceeds 65 characters.

### The Italic-Inside-Display Signature

When a headline has an emotional pivot, the pivot word(s) become italic Cormorant inside the Italiana display:

```html
<h1 class="display xxl">Dolce far niente,<br><em>as infrastructure.</em></h1>
```

### Fallback (when fonts don't install)

Georgia Regular only. Never Playfair Display. Never Calibri. Never sans-serif.

---

## Layout Rules

- **Margins:** 72px minimum on web, 0.6" on print
- **Max-width:** 1140px wrap, 760px narrow column
- **Section padding:** 130px vertical
- **Dividers:** 56px x 1px olive rule, or 44px sage hairline
- **Cards:** `--stone` or `--canvas-soft` fill, 1px hairline border, zero shadow, zero radius
- **Buttons:** Olive fill, canvas text, square corners, no hover glow
- **Images:** Always autumn-graded (muted olive grass, warm ivory skin)
- **Tables:** Hairline rows only, no zebra striping, olive column headers in kicker style
- **Section rhythm:** canvas -> stone -> canvas -> stone. Dark sections for hero + closing only.

### Layout Patterns

1. **The Wrap** — 1140px container, 72px padding, 760px narrow column
2. **Section Head** — Kicker (roman numeral + name) -> h2 headline -> italic lede
3. **Two-Column Comparison** — 80px gap, em-dash bullets, olive vs taupe headings
4. **Pull Quote** — Italiana 2rem, centered, olive hairlines top/bottom
5. **Card Grid** — 3-column, sage numbering, one "signature" card with olive left-border
6. **Hero / Title** — 180px top padding, display xxl, kicker + meta
7. **Closing Section** — Dark `--ink` background, centered Italiana xl, sage accents

---

## The Two Modes

Every output lives in one of two registers:

| Mode | Energy | Frequency | Examples |
|------|--------|-----------|---------|
| **Archive Mode** (30%) | Composed, deliberate, behind glass | Published essay | Decks, landing pages, lead magnets, cover images, hero shots |
| **Table Mode** (70%) | Unfiltered, daily, honest | Voice-note register | Dashboards, internal docs, scratch notes, thinking-in-progress |

Mixing them makes the work feel anxious. Keep them separated and it feels like a magazine.

---

## Voice in Visual Artifacts

### Kicker Copy

Structure: `ROMAN NUMERAL · SECTION NAME` (e.g., `II · TWO MODES`)

- Olive, all caps, 0.3em letter-spacing
- Roman numerals only (never Arabic)
- Middle dot separator (not period or colon)
- Never more than four words

### Headline Copy

Declarative. Unhurried. Slightly poetic, never sentimental. Two lines with a natural `<br>` break.

### Button / CTA Copy

Two-three words max. Sentence case. No "Get," "Grab," "Unlock." 

Good: `Read the manual` / `Begin` / `Open the letter`

### Image Overlay Copy

Cormorant italic, lower-third, cream color. Two lines max. **Cliffhanger — never a complete thought.** Pairs with upper-left kicker.

---

## The 90-Second Deploy Check

Six questions before anything ships:

1. **Mode?** — Am I in Archive Mode or Table Mode? Pick one.
2. **Hero prop visible?** — Is the signature typographic moment present?
3. **Overlay cliffhanger?** — Does text on image make the reader open the caption?
4. **World ratio?** — 2-3 of every 10 artifacts should be face-free, object-only.
5. **Heat dial?** — Volume III (ambient) is default. Volume V (campaign peak) is max. Never Volume X.
6. **Brand test?** — Italian architecture journal or SaaS landing page?

---

## The Anti-Aureum Rules

Envisioned Systems is the **direct opposite** of [Aureum](../../08-AUREUM/). If you produce anything matching this list, you've built Aureum, not Envisioned:

| NEVER (Aureum tells) | ALWAYS (Envisioned) |
|---|---|
| Warm cream backgrounds (`#FFFDF5`) | Cool off-white `#FBFAF9` |
| Gold accents (`#C4963C`, `#D4AF37`) | Deep olive `#4C5A2E` |
| Playfair Display, EB Garamond | Cormorant Garamond + Italiana |
| Any sans-serif font | Serif only, everywhere |
| Pure white `#FFFFFF` / pure black `#000000` | Warm ink `#1E1E1E` / cool canvas `#FBFAF9` |
| Rounded corners | Square everything |
| Drop shadows, gradients, glassmorphism | 1px hairlines, zero shadow |
| Three-column SaaS feature grids | Card grid with sage numbering |
| Performance posturing ("10x", "unlock") | Presence language ("considered", "unhurried") |
| Accent lines under slide titles | Kicker-rule pattern above headlines |

### Forbidden Colors

| Color | Why banned |
|---|---|
| `#FFFFFF` pure white | Too clinical |
| `#000000` pure black | Too harsh |
| `#FFFDF5` warm cream | Aureum background |
| `#C4963C` gold | Aureum accent |
| `#0066FF` indigo | Tech SaaS |
| `#7C3AED` purple | AI-hype |
| `#10B981` emerald | Too bright |
| `#EF4444` flag red | Performance energy |

### The Aureum Test (10-second check)

If any answer is "yes," start over:

1. Is there gold anywhere?
2. Is the background warmer than cool off-white?
3. Is there a sans-serif font?
4. Three cards in a row with icons on top?
5. Does the CTA have a gradient or drop shadow?
6. Does the header have an accent line under it?
7. Would this work as a wedding planner's landing page?

---

## Words That Carry the Brand

| Word/phrase | Why |
|---|---|
| Dolce far niente | Core operating principle |
| Presence over performance | The philosophy |
| Winter container | Visual framing |
| Autumn imagery | Photographic register |
| Legacy living | Creative throughline |
| The archive / the table | The two modes |
| Unhurried, considered, quiet | Adjective register |
| Composition, restraint | Design register |
| Provenance | Object-level respect |

---

## Sources

- envisioned-brand-design.skill — Complete visual design system (SKILL.md + 6 reference files: color-system, typography, layout-patterns, guard-rails, deploy-checklist, voice-and-tone)
