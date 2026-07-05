# Wiki Operations Log

> Chronological record of wiki changes. Most recent first.

---

## 2026-04-30 — GitHub Merge + Git Infrastructure (Session 7)

**Operator:** Envisioned AI (Claude Code)
**Scope:** Merged 7 unique articles from envisionedbrands/envisioned-wiki GitHub repo; initialized git; connected Obsidian vault to GitHub remote

### Articles merged from GitHub (7 new, total now 51)

**identity/ (+1):**
- visual-design-system.md — Italian editorial aesthetic. Full color token system (canvas, stone, olive, ink), typography, layout patterns, deploy checklist. Source: envisioned-brand-design.skill (2026-04-14)

**audience/ (+1):**
- congregation-points.md — Where ideal clients hang out, ranked by actual conversion: referrals, Facebook, Instagram, Substack. Source: market-intelligence-2026-04-14.md

**offers/ (+2):**
- codified-live.md — Virtual VIP day via Zoom with remote screen control. €3,500. Same methodology as in-person CITC.
- intentional-ceo-sprint.md — Bundle offer (Sprint + CITC). €7,497.

**content/ (+2):**
- content-hooks.md — Hook library categorized by emotional trigger
- content-mechanics.md — Borrowed structural patterns applied with original voice

**strategy/ (+1):**
- market-position.md — Market territory and white space mapping

### Infrastructure
- Initialized git repo in Obsidian vault
- Connected to envisionedbrands/envisioned-wiki remote
- Added raw/ staging directory (Karpathy pattern)
- Installed Claude Code hooks (session-sync, auto-commit, subagent-push)
- Configured Obsidian Git plugin for auto-sync

### Updated
- index.md — all category counts updated, total: 44→51

---

## 2026-04-07 — Substack Catalog + Paid Strategy + Mariela Framework (Session 6)

**Operator:** Envisioned AI (Cowork session)
**Scope:** Cataloged all Substack articles, documented Mariela de la Mora's ABC framework, created paid subscriber strategy

### Articles created (3 new, total now 43)

**content/ (+1):**
- substack-catalog.md — Full inventory of 12 Substack articles + 2 drafts. Each piece tagged with 6-Door entry, ABC type, thesis, signature line. Gap analysis: Movement/Vision door empty, Philosophy underindexed. ABC ratio: A at 42% (target 50%), B overindexed at 42% (target 30%), C at 17% (target 20%).

**frameworks/ (+1):**
- mariela-abc-framework.md — Mariela de la Mora's ABC Content Ratio (50/30/20), Story Selling principles, Three Sellable Stories, Lead Magnet as Pre-Sell, Taking Attention Offline. Extracted from SESSION-HANDOFF-2026-03-18.md (original genius report files missing from earlier cleanup). Cross-referenced with Story-Weave Method.

**strategy/ (+1):**
- substack-paid-strategy.md — Complete 4-phase roadmap for paid subscribers. Phase 1: build 500 free (8 weeks of A-type content + daily Notes). Phase 2: introduce paid at founding rate (€65/year). Phase 3: grow to 1,000 free / 100 paid (Helena di Biase 2x/week model). Phase 4: pipeline to high-ticket (DMs from paid essays → discovery calls). Free tier = philosophy, paid tier = architecture. Pricing: €10/month or €85/year. Conversion target: 5-10%. Sources: Mariela ABC, Helena di Biase editorial model, Substack official going-paid guide, WriteBuildScale, 2026 platform research.

### Key insight
The Substack isn't a product — it's the top of a funnel to €3,500-€10,000 engagements. Free tier = philosophy (shareable, discoverable). Paid tier = architecture (how it works). The philosophy IS the marketing. The architecture is the product.

### Updated
- index.md — content/ 7→8, frameworks/ 5→6, strategy/ 5→6, total: 40→43

---

## 2026-04-07 — Platform Playbooks Added (Session 5)

**Operator:** Envisioned AI (Cowork session)
**Scope:** Researched current (April 2026) best practices for all 4 active platforms, created wiki articles with verified sources

### Articles created (4 new, total now 40)

**content/ (+4):**
- platform-substack.md — Notes as primary growth engine (70% of subscriber growth), 2-3 daily Notes, Chat community, live video notifications, long-form essay home base. Sources: Escape the Cubicle, Write Build Scale, PubStack Success, 2hour Creator.
- platform-instagram.md — 40/30/30 content mix (Reels/Stories/Carousels), DM shares = #1 algorithm signal (Mosseri confirmed), keywords > hashtags for SEO, carousel 10% engagement rate, caption SEO indexed by Google. Sources: Buffer, Hootsuite, Sprout Social, TrueFuture Media, Metricool.
- platform-linkedin.md — Depth Score replaces likes, March 2026 Authenticity Update penalizes engagement bait, PDF carousels = 6.6% engagement (highest format), saves = #1 signal, no external links in post body (-40% reach). Sources: Sprout Social, Buffer (2M+ post analysis), Dataslayer, Agorapulse, Botdog.
- platform-facebook.md — Every video now auto-classified as Reel, 50% of Feed is recommended content, saves + DM shares = top signals, 3-2-1 weekly cadence (3 Reels / 2 feed / 1 promo), Groups for nurture layer. Sources: Attention Experts, SocialPilot, Sprout Social, Facebook Business Help.

### Key cross-platform insight
All four platforms now prioritize **saves and DM shares** over likes/comments as their top distribution signals. Content designed for "send this to a friend" or "save for later" outperforms engagement-bait on every platform in 2026.

### Updated
- index.md — content/ section: 3→7 articles, total: 36→40

---

## 2026-04-07 — Expansion + Vault Cleanup (Session 4)

**Operator:** Envisioned AI (Cowork session)
**Scope:** Gap analysis against Karpathy pattern, 7 new articles, vault organization

### Wiki Assessment
- Audited 29-article wiki against Karpathy's LLM Knowledge Base pattern and Brand Wiki video transcripts
- Identified 7 gaps: glossary, buyer journey, audience language bank, AI infrastructure, pricing philosophy, case studies, wiki maintenance

### Articles created (7 new, total now 36)

**audience/ (+2):**
- buyer-journey.md — Silent lurker → DM → diagnosis → transformation. Offer mapping by stage.
- audience-language-bank.md — Conscious/unconscious language, resonant/repellent words, objection phrasing, emotional states by stage

**offers/ (+1):**
- pricing-philosophy.md — Cognitive load pricing model, ladder logic per tier, scarcity model, how to talk about price

**frameworks/ (+1):**
- glossary.md — 25+ proprietary terms defined with wikilinks. The "teach AI my language" file.

**strategy/ (+2):**
- ai-infrastructure.md — The actual stack: CLAUDE.md, wiki, MCPs, skills, 4 architecture layers (medium confidence — evolves fast)
- wiki-maintenance.md — Ingest/Query/Lint operations, confidence decay rules, update triggers, lint checklist

**proof/ (+1):**
- case-studies.md — Structured before/after evidence: silent buyer, VA promoted, grocery-line, Time-Rich CEO flop (medium confidence — needs real client data)

### Vault Cleanup
- Deleted 7 empty files: 2026-04-06.md, Untitled.canvas ×3, Untitled.base ×3
- Moved 6 files to _archive/: RAW-TRANSCRIPTS, SESSION-HANDOFF, SKILL files ×2, algorithmic-art.html, Content .base
- Moved content-engine/ folder to _archive/
- Vault root now: Content/, _Tags/, _archive/, wiki/

### Stats
- Total articles: 36 (was 29)
- High confidence: 34
- Medium confidence: 2 (ai-infrastructure, case-studies)
- Index and log updated

---

## 2026-04-07 — Full Compilation (Session 3)

**Operator:** Envisioned AI (Cowork session)
**Scope:** Complete wiki build from source documents

### What happened
- Previous sessions (2026-04-06) created wiki folder structure, WIKI-SCHEMA.md, and attempted article creation, but filesystem deadlock prevented reading source documents
- This session: full source access restored. Read all 7 priority source documents (~237KB total)
- Built 29 articles from scratch across all 8 categories, all at high confidence
- Every article enriched with real data, quotes, frameworks, and numbers from primary sources

### Articles created (29 total)

**identity/ (5):**
- founder-profile.md — from North Star, Brand Narrative, Brand Voice
- positioning-statement.md — from North Star, Brand Narrative, ICP
- brand-values.md — from North Star, Brand Narrative, Brand Voice
- brand-archetypes.md — from North Star, Genius Report
- legacy-living-spin.md — from North Star

**audience/ (1):**
- ideal-client-profile.md — from North Star, ICP doc, Brand Narrative

**offers/ (6):**
- offer-architecture.md — from 03-OFFERS/ folder, Brand Narrative
- the-atelier.md — from 03-OFFERS/ folder
- capacity-mapping.md — from 03-OFFERS/ folder
- workflow-extraction.md — from 03-OFFERS/ folder
- codify-in-the-city.md — from Brand Narrative
- time-rich-ceo.md — from 03-OFFERS/ folder, Brand Narrative

**voice/ (4):**
- voice-guide.md — from Brand Voice Complete
- forbidden-phrases.md — from Brand Voice Complete
- nasameter.md — from Brand Voice Complete
- personality-architecture.md — from Brand Voice Complete

**frameworks/ (4):**
- the-codification-thesis.md — from Brand Narrative, Genius Report
- freedom-architecture.md — from Brand Narrative, ICP
- heck-yes-framework.md — from Heck Yes Framework (75KB)
- story-weave-method.md — from CLAUDE.md, Genius Report

**strategy/ (3):**
- brand-strategy.md — from North Star, Genius Report
- competitive-positioning.md — from North Star, Genius Report, Brand Narrative
- brand-narrative-architecture.md — from Brand Narrative

**content/ (3):**
- content-strategy.md — from Genius Report, CLAUDE.md
- content-pillars.md — from Genius Report
- content-angles.md — from Genius Report

**proof/ (3):**
- emotional-hooks.md — from Brand Narrative, ICP
- objection-architecture.md — from Brand Narrative, ICP
- story-bank.md — from Brand Narrative, Brand Voice, CLAUDE.md

### Infrastructure created
- WIKI-SCHEMA.md — operating manual
- index.md — full article catalog with confidence scores
- log.md — this file

---

## 2026-04-06 — Initial Structure (Session 2)

**Operator:** Envisioned AI (Cowork session)
**Scope:** Article scaffolding attempt

### What happened
- Created 14 article stubs across 8 categories
- Filesystem deadlock prevented reading source documents
- Articles written from secondary sources only (file names, partial reads before lock)
- Confidence: mostly medium/low
- Session ended with enrichment queue documented

**Note:** All stubs from this session were replaced by full articles in the 2026-04-07 compilation.

---

## 2026-04-06 — Wiki Scaffolding (Session 1)

**Operator:** Envisioned AI (Cowork session)
**Scope:** Folder structure and schema

### What happened
- Created wiki/ folder inside Obsidian vault
- Created 8 category subfolders
- Wrote WIKI-SCHEMA.md (operating manual)
- Wrote initial index.md and log.md
- Filesystem deadlock blocked all source reads
- Handed off enrichment task to next session
