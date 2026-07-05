---
title: Personal Preferences — Wardrobe, Props, Lifestyle Defaults
category: operations
confidence: high
sources:
  - memory/personal-preferences.md
  - Maria-Ines wardrobe correction, 2026-04-19
last_updated: 2026-04-19
---

# Personal Preferences — Wardrobe, Props, Lifestyle Defaults

> Specific personal details that add authenticity to AI imagery and content. Use as the default vocabulary when generating Maria-Ines or her environment.

---

## Dream Car (Tuscany / Aspirational Travel)

**Sage green Nissan Figaro (1991)** with the roof retracted — iconic pill-shaped vertical headlights, chrome accents, cream/ivory leather interior, curved retro-modern silhouette. Muted dusty sage green (NOT emerald, NOT saturated). Perfect brand fit: editorial-famous, Kinfolk/Jacquemus-adjacent, quiet luxury.

**How to apply:** When generating travel/aspirational imagery involving a vehicle, the Figaro is the default unless she specifies otherwise. Always emphasize muted sage (brand-safe), NOT emerald (brand-prohibited). LHD per [[visual-generation-rules]].

---

## Clothing / Styling (CRITICAL — Updated 2026-04-19)

Default to "boring round-neck sweater" generations is **wrong**. Her actual style has detail and personality.

### What She DOES Wear

**Base color: BLACK** (most often) — but never plain. Always with one of these details:

- Lace insets or trim
- Eyelet pattern
- Embroidery
- Cutout details (asymmetric, back, side)
- Pleating or draping
- Interesting straps (halter, asymmetric, crossover, single-shoulder)
- Open back
- Mesh insets
- Contrast trim

**Brand-color alternatives (when not black):**
- Terracotta / burnt orange (warm, editorial)
- Deep cream, warm ivory
- Espresso / chocolate brown
- Warm camel / honey
- Dusty muted sage (NOT emerald)

**Silhouettes:**
- Halter dresses
- Draped midi dresses
- Pleated dresses or tops
- Asymmetric necklines
- Fitted-but-soft (silk, satin, fine knit)
- Structured-but-flowing
- Wrap details
- Soft tailoring (NOT structured boxy blazers)

**Outerwear:**
- Camel wool coat (soft, draped, not boxy)
- Long cardigans (oversized, soft knits with detail)
- Open kimono-style robes (silk, embroidered, NOT terrycloth)

### What She Does NOT Wear

- **Boring round-neck sweaters** — generic crew sweaters were a lazy default. Drop them.
- Plain t-shirts (too casual, no personality)
- Turtlenecks (collar-jaw seam fails in AI rendering anyway)
- Scarves / silk scarves / kerchiefs — not her, ever
- Blazers (structured "boss" blazer cliché is wrong)
- Stiff structured pieces — her aesthetic is structured BUT soft
- Visible logos / branding on clothing
- Cheap-looking finishes — even when casual, fabric reads quality

### Replacement Vocabulary

Replace "soft cream cashmere crew-neck sweater" with one of:

- "Soft black silk halter dress with subtle pleating"
- "Black silk camisole with lace trim at neckline"
- "Black eyelet midi dress with structured but soft silhouette"
- "Terracotta linen halter dress, draped silhouette"
- "Cream silk top with asymmetric neckline detail"
- "Camel cashmere wrap with delicate detail at edges"
- "Deep cream silk blouse with subtle ruffle or pleating"

### Body-Only Crops Work Great

Body-only crops (no face) carry editorial weight beautifully and dodge face-rendering issues. For quote covers especially, body + garment + warm wall works.

---

## Makeup Signature — RED LIPS (~50% rotation)

It's a signature look she wears often. She uses the kiss emoji frequently.

**How to apply:**
- Roughly every other face-in-frame generation = red lips visible
- Other generations = bare/natural lip color
- Don't EVERY generation = signature loses its punch
- Don't ZERO generations = missing a brand identifier
- Track loosely; doesn't have to be exact alternation

**Style of red:**
- Classic warm red (NOT orange-red, NOT pink-red, NOT bright primary)
- Matte or satin finish (NOT glossy)
- Specifically: warm berry-red or true red with brown undertones
- Reference shades: Chanel "Pirate," Tom Ford "Ruby Rush," Charlotte Tilbury "Walk of No Shame"

**Even with red lips: rest of makeup natural.** No heavy contouring, no smoky eye, no foundation cake. The lip carries the look.

---

## Nails (LOCKED — 2026-04-19)

- **Shape: always straight/square** — natural square tip, straight across. NEVER oval, NEVER almond, NEVER pointed/coffin/stiletto.
- **French tip: straight white line** across the tip — classic square french. NOT a curved smile line, NOT an oval sweep.
- When specifying in prompts: *"square/straight-edge french tip, straight white line across nail — NOT oval-shaped nails"*

**Pairs particularly well with:** black silk halter, cream/ivory silk, camel coat, any moment that needs "main character energy."

---

## Lifestyle Defaults — What She Does NOT Do

- **No napping.** Drop "afternoon nap" from any leisure-scene generation. Not her.
- (Add others as they emerge.)

---

## Daughter — ETHICAL CONSTRAINT

Her daughter is named **Merida**. Same ethical rule as in [[indications-of-life-theme]]: **no face generation, only back-view / fragment / hint.** Real photos Maria-Ines shares of Merida are for STYLE/composition reference only — never to be used as identity reference for generation.

---

## How to Apply

When generating any image of Maria-Ines or her environment:
1. Default to her actual wardrobe vocabulary (NOT generic crew sweater)
2. Roll the ~50% red-lips rotation when face is in frame
3. Never include nap scenes or scarves or blazers or turtlenecks
4. Never generate Merida's face
5. Default car (when applicable): sage Figaro, LHD

---

## Fonts in Decks & Documents (CRITICAL — set 2026-06-15)

Maria-Ines has repeatedly flagged that decks/PDFs come out with fonts that are **too small and hard to read**. This is a standing rule for any presentation, PDF, or document deliverable:

- **Do NOT use Cormorant Garamond for body text.** It is thin and light and reads small/unreadable on slides and handouts — it was the repeat offender.
- **Default typeface for decks and documents is Georgia** (or another heavy, highly legible serif). Use it for headers AND body. Bold the headers.
- **Size up, always.** Minimums: slide body ≥ 16pt, slide titles ≥ 32pt; PDF/handout body ≥ 12pt, headers ≥ 16pt. When in doubt, go bigger.
- Italiana (the brand display face) is also too thin at small sizes — avoid it for anything that must be *read* quickly; reserve for large ceremonial display only, if at all.
- This **overrides** the `envisioned-brand-design` skill's Cormorant/Italiana mandate whenever readability is at stake (which is most of the time for working decks and client handouts). Brand palette (olive/sage/cool off-white/ink) still applies.

Reference build: `00-STRATEGY/escape-hub-presentation/` (Georgia throughout, sized up).

---

## See Also

- [[visual-generation-rules]] — Nano Banana 2 ruleset (expression, lighting, hands, age)
- [[indications-of-life-theme]] — Family / Dutch home theme (where Merida rule originates)
- [[legacy-living-theme]] — Aspirational lifestyle motifs
- [[representation-rules]] — Non-self imagery rules
