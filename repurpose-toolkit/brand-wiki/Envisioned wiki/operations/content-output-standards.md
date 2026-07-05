---
title: Content Output Standards — HTML, Articles, Web
category: operations
confidence: high
sources:
  - memory/content-output-standards.md
last_updated: 2026-04-19
---

# Content Output Standards — HTML, Articles, Web

> Standards for any content the pipeline outputs as web/article format. Applies to long-form HTML, Substack articles, blog posts, landing pages.

---

## 1. Human + LLM + SEO + GEO Optimized

Every long-form output must be readable by **three audiences**:

- **Humans:** editorial typography, generous whitespace, image breaks, scannable structure
- **Search engines (SEO):** semantic HTML5, H2/H3 hierarchy, descriptive title/meta, Open Graph + Twitter cards, schema.org Article + FAQPage structured data, alt text, internal links
- **LLMs (GEO / Generative Engine Optimization):** clear TL;DR at top, scannable section headers as questions or claims, FAQ-style sections at end, quotable factoids, confident assertions, proper-noun consistency

### Required HTML Elements

- `<title>` and `<meta name="description">`
- Open Graph: `og:title`, `og:description`, `og:image`, `og:type`, `og:url`
- Twitter Card: `summary_large_image`
- JSON-LD: Article schema with author, datePublished, image, headline; optional FAQPage schema for Q&A sections
- Semantic structure: `<article>`, `<header>`, `<section>`, `<h2>`, `<figure>`, `<figcaption>` only when functional
- Image alt text: descriptive (NOT "Maria-Ines portrait" — say "Maria-Ines wearing cream cashmere, three-quarter portrait, soft window light")
- Reading time estimate visible at top
- Optional FAQ section at end ("Common questions about this argument") for LLM citation

---

## 2. Em-Dash Discipline

See [[voice-guide#The Em Dash]] — the canonical voice rule.

**Summary:** Maximum 1–2 em-dashes per paragraph, ideally zero. Maria-Ines uses parentheses more often than em-dashes. An em-dash should feel like an earned tonal shift, not reflexive punctuation. When in doubt, period.

**Replacements:**
- Em-dash for emphasis → period
- Em-dash for aside → parentheses or commas
- Em-dash for connection → colon or semicolon
- Em-dash for dramatic pause → period

---

## 3. Image Captions — Default NO Captions

Maria-Ines does **not** want overly poetic or precious captions under images. Examples that failed:

- "A place that has held generations and is still standing, quietly, in warm light."
- "The hand of someone who has done the work."
- "Coming home to a life she built."

These read as twee / over-art-directed. The image should speak for itself; the caption shouldn't perform.

**Default rule: NO visible captions.** Use the alt text attribute (invisible to readers, read by screen readers + crawlers) for descriptive accessibility/SEO.

**When a caption IS warranted:**
- Functional context (location, date, attribution)
- A specific quote pulled from the article that the image illustrates
- Never poetic interpretation of what the image "means"

If unsure, omit.

---

## 4. Vocabulary Check (the "would Maria-Ines say this?" test)

Before locking any article draft, scan for words the **author** would not naturally use in conversation. If there's a word Maria-Ines would have to Google, her readers (founders, mostly not English professors, many non-native speakers) will too.

**Failure caught 2026-04-18:** the word "homophone" in the Privilege article. The piece is literally about the humiliation of being corrected for English. Using a linguistics term the author doesn't know defeats the piece's argument.

**Rule:**
- If a word is academic, clinical, or specialist, check whether Maria-Ines uses it unprompted
- If she doesn't → swap for plain language OR drop the line
- The bar is NOT "is it grammatically correct?" The bar is **"would she say this at a dinner party?"**
- Jargon that IS part of her voice (codification, intelligence transfer, Italian Afternoon, etc.) is fine
- Jargon that's drift (homophone, idiomatic, heuristic, epistemic, etc.) gets cut

When in doubt, ask or cut.

---

## See Also

- [[article-structure]] — The 7 required beats for long-form articles
- [[voice-guide]] — Em-dash discipline (canonical)
- [[../content/content-strategy|content-strategy]] — Story-Weave Method, 6 Doors rotation
- [[visual-generation-rules]] — Image specs for article assets
- [[email-deliverability]] — Spam trigger words, subject line rules, pre-send checklist
