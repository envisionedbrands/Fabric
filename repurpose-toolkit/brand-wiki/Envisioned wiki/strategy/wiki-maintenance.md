---
title: Wiki Maintenance — When and How to Update
category: strategy
confidence: high
sources:
  - WIKI-SCHEMA.md
  - CLAUDE.md
last_updated: 2026-04-07
---

# Wiki Maintenance — When and How to Update

> The wiki is a living system, not a static document. This article defines when updates happen, what triggers them, and how to keep the knowledge base current without it becoming a chore.

---

## The Three Operations (Karpathy Pattern)

Following the LLM Knowledge Base pattern, this wiki supports three core operations:

### 1. Ingest

**What:** New information enters the wiki from source material.

**Triggers:**
- New client engagement completed → update [[case-studies]], [[story-bank]]
- New offer launched or pricing changed → update [[offer-architecture]] and specific offer articles
- Maria-Ines shares a new story in conversation → add to [[story-bank]]
- Strategic direction shifts (new positioning, new framework) → update relevant identity/strategy articles
- Competitive landscape changes → update [[competitive-positioning]]
- New AI tools/connections added → update [[ai-infrastructure]]

**Process:**
1. Identify which article(s) the new information affects
2. Read current article content
3. Add new information with proper attribution
4. Update `last_updated` in frontmatter
5. Add new wikilinks if cross-references are needed
6. Update [[index.md]] if confidence level changed
7. Log the change in [[log.md]]

### 2. Query

**What:** An AI session or person reads the wiki to answer a question or create content.

**How it works:** The wiki is designed so that any article can be read standalone AND in context. Wikilinks provide the web. The index provides the map. WIKI-SCHEMA provides the rules.

**For AI sessions:** Read the index first to understand coverage. Follow wikilinks into relevant articles. The YAML frontmatter tells you confidence level and source attribution.

### 3. Lint

**What:** Periodic review to catch stale information, broken links, confidence decay, and gaps.

**Frequency:** Monthly minimum. After any major business change (new offer, new positioning, pivoted strategy).

**Lint checklist:**
- [ ] Are all `last_updated` dates within 60 days? If not, verify content still accurate.
- [ ] Do all wikilinks resolve to existing articles? (Obsidian shows broken links in red)
- [ ] Are any articles still `medium` or `low` confidence that could be upgraded with available sources?
- [ ] Has any offer pricing changed since last update?
- [ ] Are there new stories that should be in [[story-bank]] but aren't?
- [ ] Does the [[glossary]] include any new proprietary terms Maria-Ines has coined?
- [ ] Does [[competitive-positioning]] reflect current market landscape?
- [ ] Has [[ai-infrastructure]] been updated with new MCP connections or skills?

---

## Confidence Decay Rules

Confidence isn't permanent. Here's when to downgrade:

| Condition | Action |
|-----------|--------|
| Article unchanged for 90+ days | Review. Re-confirm or downgrade to medium. |
| Offer pricing changed | Update immediately. Stale pricing = high → low. |
| Source document superseded | Re-ingest from new source. Mark as medium until verified. |
| Maria-Ines contradicts article content in conversation | Update immediately. Her word > documented history. |
| Market positioning shifts | Update [[competitive-positioning]] and [[positioning-statement]]. Medium until re-verified. |

---

## What Triggers an Immediate Update

These events should trigger a wiki update THE SAME DAY:

1. **New offer launched** — Create new offer article, update [[offer-architecture]]
2. **Offer discontinued or pricing changed** — Update immediately
3. **New client story worth documenting** — Add to [[story-bank]], potentially [[case-studies]]
4. **Maria-Ines coins a new term** — Add to [[glossary]]
5. **Voice rule changes** — Update [[voice-guide]] or [[forbidden-phrases]]
6. **New MCP connection added** — Update [[ai-infrastructure]]
7. **Strategic pivot or reposition** — Update relevant strategy/identity articles

---

## What Can Wait for Monthly Lint

- Content performance pattern changes → [[content-strategy]], [[content-pillars]]
- Audience language evolution → [[audience-language-bank]]
- Competitive landscape shifts → [[competitive-positioning]]
- Framework refinements → relevant framework article

---

## Article Creation Decision Tree

When new information appears, ask:

1. **Does an existing article cover this?** → Update that article
2. **Is this a new concept that deserves its own article?** → Create new article in appropriate category
3. **Is this a sub-concept of an existing article?** → Add as a section, don't split unless it exceeds ~500 words
4. **Is this a one-off fact with no broader significance?** → Don't add. The wiki is for structural knowledge, not trivia.

---

## Automated Maintenance (Future)

The following could be scheduled as recurring tasks:

- **Weekly:** Check for new Zoom transcripts → extract any new client stories or methodology refinements
- **Monthly:** Run lint checklist above
- **After each client engagement:** Update case studies and story bank
- **After each content batch:** Note which stories/angles performed for [[content-strategy]] updates

See [[WIKI-SCHEMA]] for the full operating manual.

---

## See Also

- [[WIKI-SCHEMA]] — The structural rules for how the wiki works
- [[ai-infrastructure]] — The systems that feed the wiki
- [[glossary]] — Term definitions that need regular updating
- [[case-studies]] — The article most likely to need frequent updates
