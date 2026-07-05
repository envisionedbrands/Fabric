---
title: Visual Generation Rules — Nano Banana 2 Operational Ruleset
category: operations
confidence: high
sources:
  - memory/visual-generation-rules.md (Nano Banana 2 testing, 2026-04-18)
  - Maria-Ines age-rendering correction, 2026-04-19
last_updated: 2026-04-19
---

# Visual Generation Rules — Nano Banana 2 Operational Ruleset

> Locked rules learned from Nano Banana 2 (Gemini 3.1 Flash Image / Nano Banana Pro) testing for Maria-Ines portraits and lifestyle imagery. Apply to **every** face-generation prompt.

---

## Expression Default — Warm, Not Stoic (CRITICAL)

**Default to warm and happy, not stoic.** Maria-Ines's brand VOICE is bold/confrontational but **she** is warm, playful, emotional. Translating "philosophy-first, no fluff" voice into stoic/serious faces produces "haggard, tired, disapproving academic" — wrong.

- **Default:** genuine smile or hint of smile, relaxed bright eyes, approachable warmth, the look of someone enjoying the moment
- **Stoic/composed expression:** reserve for specific serious pieces only (vulnerability posts, hard-truth reframes). Never the default.
- "Composed, neutral, inward, not smiling" in a prompt = haggard output. Don't use.

> Maria-Ines, 2026-04-18: "I do want some emotion and happiness I'm not that serious :)"

---

## Face Lighting

- Soft, front-ish or gentle 45° side
- Window to camera side or slightly behind camera, never behind her
- **Never hard backlight** — creates squint, shadows under eyes, aged look

---

## Topaz Upscaling — Never On Faces

- **Never on face-focused imagery.** Topaz sharpens every pore/line/texture → visually ages the subject
- Topaz reserved for environmental shots, products, textures, B-roll
- For face-shot sharpness: solve in the prompt (tack sharp focus, crisp editorial detail), not in post

---

## Aspect Ratios

- **Website / Facebook:** 16:9
- **Instagram Reels / Stories / 9:16 feed:** 9:16
- **NOT 4:5, NOT 1:1** — she almost never uses these. Drop from defaults.

---

## Age Rendering Rule — Drop Age Anchors (CRITICAL — fixed 2026-04-19)

**Drop all age-anchoring language from prompts.** It compounds in the model and ages her by ~10 years vs reality.

**STOP using:**
- "Mid-40s woman" / "mid-40s Venezuelan woman"
- "Authentic mid-40s skin"
- "Visible pores, fine laugh lines"
- "Natural matte skin with pores intact"
- "Do not youthen" (paradoxically pushes the model older)

**INSTEAD use:**
- (no age number — let the identity pack carry the rendering)
- "Clear luminous skin, warm healthy glow, well-rested"
- "Natural radiant complexion"
- "Smooth natural skin without overemphasized texture"
- "Vibrant, present"

**Why:** The 6-image identity pack already encodes her actual face. Adding age modifiers tells the model to **exaggerate** age signals. The pack alone gives accurate likeness without inflation.

---

## Hands Specification (CRITICAL — AI default produces manly hands)

Maria-Ines has **elegant slim hands with long graceful fingers** — prominent feature in most lifestyle shots. AI defaults aggressively to chubby/thick/stocky hands unless explicitly directed.

**Inject in every lifestyle generation where hands are visible:**

> "Hands: elegant slim hands with long graceful fingers, refined and feminine, NOT chubby, NOT thick, NOT stocky, NOT manly. Well-groomed clean nails."

### Manicure Direction
- **Default rotation:** ~40% natural/nude soft polish, ~40% clean white french tip, ~20% bare/unpainted. Vary across content — do NOT french tip every image.
- **Nail shape: ALWAYS straight/square edge** — natural square tip. NEVER oval, NEVER almond, NEVER pointed/coffin/stiletto. Her nails are always straight across.
- **French tip style: straight white line** across the tip — classic square french, NOT a curved smile line, NOT oval sweep.
- **Never:** chipped polish, overgrown nails, dark/dramatic colors, gel art, glitter, pointed claws, oval-shaped nails.

### When Hands Are Prominent in Composition
(holding cup, on steering wheel, on notebook, in kitchen action) — double the specification weight: "focused camera attention on hand elegance, slim fingers tack sharp, graceful hand posture."

---

## Composition / Camera Angle Rules

Certain angles make her face read fuller than it is. **Avoid:**
- Low camera angles shot from below (emphasizes cheek/jaw fullness)
- Shoulders square to camera + face fully turned back (flattens and widens)
- Hair pulled fully back exposing full face width
- Wide full-face grins (maxes out cheek-to-cheek dimension)

**Favor:**
- Profile shots (clean side view, slim line of jaw/nose visible)
- Three-quarter turn ≤30° with chin slightly lifted
- Hair framing one side of the face (partial softening)
- Elevated camera angles (camera 30° above looking down — slims naturally)
- Hint of smile rather than wide grin when cheek volume matters

---

## CD Review Checklist (Run BEFORE Rating Any Generated Image)

Don't assume the model got these right. Scan explicitly:

1. **Prop placement errors** — are objects in their RIGHT LOCATION? (book on HOOD vs. passenger seat, lavender INSIDE car vs. outside)
2. **Face presence when face was prompted** — AI sometimes crops face out
3. **Hand anatomy** — stubby fingers, 6 fingers, disappearing hands, chubby/manly renderings
4. **Age drift** — did it youthen or haggard her vs. reference pack?
5. **Color violations** — emerald/saturated greens, cool blue tones (brand-prohibited)
6. **Collar/neckline** — turtleneck sneaking back in even when crew was specified
7. **Composition sanity** — limbs in logical places, correct number of passengers, physics
8. **Text rendering** — if any text in frame (signs, book titles), is it actual words or AI garbage?
9. **Background coherence** — trees / architecture not "AI repetitive/topiary-like"
10. **Lighting integrity** — face shadows match the stated light direction
11. **Vehicle / structure integrity** — AI drops parts of complex structures (convertible tops, windshield frames, doors). Check: is the full roof structure coherent both sides? All 4 corners of windshield rendered? Does the car look complete?
12. **Driving side** — Maria-Ines drives **left-hand-side** (European/US standard). The Figaro was originally right-hand-drive (JDM), but for her imagery default to LHD unless explicitly directing otherwise. Always specify "left-hand drive" when vehicle is centered.

Flag any failures explicitly before giving a rating.

---

## Scene Preference

- Environmental/action scenes with Maria-Ines mid-ritual work better than static hero portraits. (Kitchen with kettle + moka pot was the strongest result.)
- Pure hero close-ups are "boring — nothing happening." Use only for specific cases (about page, quote cards, launch moments).

---

## Reference Pack (The Durable Identity Artifact)

`01-BRAND/identity-pack.md` — 6 photos passed into every face generation. Flagged gap: no true profile, no controlled studio shots.

See [[visual-assets-locations]] for the full asset path map.

---

## Tool & Model

- **Model:** Nano Banana 2 (Gemini 3.1 Flash Image / Nano Banana Pro) via `mcp__kie-ai__nano_banana_image`
- **Resolution:** 2K (4K oversaturates per research)
- **Reference hosting:** uguu.se for test URLs (expires ~24h — needs durable host for production: GitHub raw, Cloudflare R2, or similar)
- **kie.ai cannot fetch catbox.moe URLs** — don't use catbox

---

## How to Apply (Every Face-Gen Prompt)

1. Start with identity lock prefix from `01-BRAND/identity-pack.md`
2. Specify warm/happy/smiling expression by default
3. Specify soft front or 45° side lighting, never backlit
4. Never follow with Topaz upscale if it's a face shot
5. Output in 16:9 or 9:16, not 4:5/1:1
6. Run the 12-point CD checklist before rating

---

## Color World Rotation — No Single-Color Monoculture (CRITICAL)

> Maria-Ines, 2026-04-19: "please not all the images now have to be terracotta ok? I'm not saying change it now i'm just saying for future reference"

When generating a multi-image set (carousel, batch, theme series), **do not anchor every image to the same color world.** Terracotta is one signature color but it is NOT the brand. Repeating it across all 7 carousel slides (wall + dress + tablecloth + alley) creates monotony and reads as cheap stock.

### Rule for any multi-image set
- **Maximum ~40% of images in any single dominant color** (terracotta, sage, cream, espresso, etc.)
- **Minimum 3 distinct color worlds** in any 5+ image batch
- **Mix warm + cool restraint** — Italian Afternoon grade unifies them; the underlying color story should still vary

### Brand color palette (rotate through these)
- Terracotta / burnt sienna (warm wall, dress, ground)
- Cream / ivory / warm off-white (light walls, linen, soft contrast)
- Espresso / chocolate brown (deep depth, kitchen, leather)
- Warm camel / honey (cashmere, sand, stone)
- Dusty muted sage (NOT emerald — gardens, foliage, accents)
- Soft warm pink / dusty rose (florals, fabric accents)
- Black (her wardrobe default — silk, lace, halter)
- Stone gray / weathered concrete (urban, architectural)

### What unifies a varied set
The **Italian Afternoon color grade** + **lighting consistency** (warm afternoon sun, soft shadows) — not the wall color. Cohesion comes from atmosphere, not pigment.

### How to apply when generating multi-image sets
1. Sketch the color world map BEFORE generating: which slide gets terracotta, which gets cream, which gets sage, etc.
2. Vary surfaces too: stucco wall, painted wood, stone, fabric, foliage, water
3. Vary settings: warm interior, garden, courtyard, alley, kitchen, balcony
4. The 7-slide Privilege carousel (2026-04-19) violated this — half the slides were terracotta-walled. Use as cautionary example.

---

## Face Generation at Scale — Known Limitation (2026-04-19)

Nano Banana 2 with the 6-image identity pack reliably preserves Maria-Ines's likeness in **¾ body shots and atmospheric crops** but **drifts in tight face crops** (collarbone-up, headshots). The model defaults to "generic warm Latina woman" features when face dominates the frame.

### Reliable use cases
- ¾ body and full body with face visible (hero portraits) ✅
- Body crops with no face ✅
- Hand details, atmospheric, environmental ✅

### Unreliable use cases
- Tight headshot crops, collarbone-up close-ups ⚠️
- CTA portraits where face must read instantly ⚠️

### Workaround for face-critical content
- **Use one of her actual selfies** from `01-BRAND/AI-training-images/AI training images MI/` lightly graded to Italian Afternoon
- OR avoid face-tight shots — use body crop + typography overlay instead
- OR generate a wider shot and crop in post (her face was preserved at the wider distance)

---

## See Also

- [[representation-rules]] — Demographic distribution for non-self imagery
- [[visual-assets-locations]] — Where all visual assets live
- [[personal-preferences]] — Clothing, makeup, props, lifestyle defaults
- [[brand-strategy]] — Updated color palette (April 2026)
