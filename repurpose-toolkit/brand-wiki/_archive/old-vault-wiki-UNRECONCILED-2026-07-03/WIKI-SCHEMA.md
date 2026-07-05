# Wiki Schema — Operating Manual

> How this wiki works, how to maintain it, and what the rules are.

---

## Purpose

This wiki is Envisioned Brands' **LLM Knowledge Base** — a structured, interlinked reference that any future AI session can read to fully understand the brand, voice, offers, frameworks, and strategy without re-reading 300KB of source docs.

Follows the Andrej Karpathy pattern: atomic articles, high interlink density, confidence-scored, source-attributed.

---

## Folder Structure

```
wiki/
├── WIKI-SCHEMA.md        ← You are here (operating manual)
├── index.md               ← Article catalog + enrichment queue
├── log.md                 ← Operations log (what changed, when)
├── identity/              ← Who Maria-Ines is, brand archetypes, positioning
├── audience/              ← ICP, buyer journey, psychographics
├── offers/                ← Every offer with pricing, deliverables, positioning
├── voice/                 ← Voice rules, forbidden phrases, NASAmeter
├── frameworks/            ← Proprietary and adopted frameworks
├── strategy/              ← Brand strategy, competitive positioning, narrative
├── content/               ← Content system, pillars, rotation, patterns
└── proof/                 ← Emotional hooks, objection handling, client stories
```

---

## Article Format

Every article uses this template:

```markdown
---
title: Article Title
category: identity | audience | offers | voice | frameworks | strategy | content | proof
confidence: high | medium | low
sources:
  - filename.md
  - filename2.md
last_updated: YYYY-MM-DD
---

# Article Title

> One-sentence summary of what this article covers.

---

## Section Heading

Content here. Use [[wikilinks]] to cross-reference other wiki articles.

---

## Sources

- [[source-file-name]] — what was extracted from it
```

---

## Rules

1. **Atomic articles.** One concept per article. If an article covers two distinct things, split it.
2. **Wikilinks everywhere.** Use `[[article-slug]]` to cross-reference. Obsidian resolves these automatically.
3. **Confidence scoring.** Every article gets `high`, `medium`, or `low`:
   - **High** — Written from primary source docs with direct quotes/data
   - **Medium** — Synthesized from multiple sources, directionally correct
   - **Low** — Stub or inferred from secondary sources
4. **Source attribution.** Every article lists which source files it was built from.
5. **No source modification.** Source docs in `00-STRATEGY/`, `01-BRAND/`, `02-CONTENT/`, `03-OFFERS/` are read-only. Only write to `wiki/`.
6. **Envisioned only.** This wiki covers Envisioned Brands. Aureum AI is a separate entity.
7. **Update the index.** After creating or modifying articles, update `index.md`.
8. **Update the log.** After any batch of work, add an entry to `log.md`.
9. **Use slugs for filenames.** Lowercase, hyphenated: `heck-yes-framework.md`, `ideal-client-profile.md`.
10. **Dates in ISO format.** Always `YYYY-MM-DD`.

---

## How to Enrich an Article

1. Read the article's current content
2. Read the source files listed (or discover new relevant sources)
3. Add specific data: quotes, numbers, frameworks, examples
4. Update `confidence` in frontmatter (usually low→medium or medium→high)
5. Update `last_updated`
6. Add new `sources` if applicable
7. Add/update wikilinks to related articles
8. Update `index.md` with new confidence level

---

## How to Create a New Article

1. Identify a concept that deserves its own article
2. Create file in appropriate category folder
3. Use the article template above
4. Cross-reference with existing articles via wikilinks
5. Add to `index.md`
6. Log in `log.md`

---

## Category Definitions

| Category | What Goes Here |
|----------|---------------|
| **identity** | Maria-Ines's profile, brand archetypes, positioning statement, brand values, the Intentional CEO |
| **audience** | Ideal client profile, psychographics, buyer journey, audience language |
| **offers** | Each offer as its own article: pricing, deliverables, positioning, target buyer |
| **voice** | Voice rules, mandatory patterns, forbidden phrases, NASAmeter, conversational register |
| **frameworks** | Proprietary frameworks (Codification Thesis, Freedom Architecture, Story-Weave) and adopted ones (Heck Yes) |
| **strategy** | Brand strategy, competitive positioning, narrative architecture, market positioning |
| **content** | Content system, 7 pillars, rotation system, posting schedule, content angles |
| **proof** | Emotional hooks, objection architecture, client stories, social proof strategy |
