# agents.md — Envisioned Vault Operating Instructions

> This file tells Claude how to operate inside this vault. Load it at the start of any session that touches brand content, client work, or content creation.

---

## What This Vault Contains

```
wiki/                ← canonical brand brain (voice, identity, offers, frameworks, audience, strategy, content, proof, operations). THE source of truth.
clients/             ← active client briefs (working intelligence — updated after every call)
Workshop/            ← training files (Connection 101, member Q&A prep)
raw/
  zoom/              ← Zoom VTT transcripts to be processed
  web-clips/         ← Obsidian Web Clipper saves (full page content, already fetched)
  links/             ← URLs to fetch: YouTube, articles, podcasts, threads (one URL per .md file)
  notes/             ← voice memo transcripts, quick captures, rough thoughts
  client-docs/       ← files received from clients (intake forms, questionnaires, docs)
  processed/         ← files move here after INGEST — immutable archive
content/
  ideas/             ← hooks, angles, seeds generated during INGEST
  drafts/            ← full draft posts ready for review
  published/         ← APPROVED content lives here (the record of what you stand behind)
  _templates/        ← note templates (e.g. published-piece template)
"Content "/          ← archive of ~1,736 past social posts (Airtable export). Read-only reference. (Trailing space is intentional — avoids a name clash with content/.)
_Tags/               ← topic & pillar pages
_archive/            ← retired material: the OLD "wiki", old engines, handoffs, skill templates. DO NOT read for brand truth.
```

External (outside vault, in main project folder):
```
04-CLIENTS/clients/[name]/     ← deep content per client (all Zoom VTTs, deliverables, raw docs)
04-CLIENTS/zoom-transcripts/   ← raw VTT files organised by YYYY-MM
```

---

## Operation: INGEST (process anything in raw/)

Use when new files land in `raw/zoom/`, `raw/web-clips/`, `raw/notes/`, or `raw/client-docs/`.

### Step 1 — Scan the inbox
List all files in `raw/` subfolders (excluding `raw/processed/`). Identify each file type.

### Step 2 — Process by type

**Zoom VTT (`raw/zoom/`)**
1. Read the transcript
2. Identify the client(s) — check names against `clients/_index.md`
3. Extract: date + duration, what was covered (2–4 bullets), decisions made, open threads, any new context about the client
4. Open `clients/[name].md` and update: Last Session, Key Context (if new), Open Threads
5. If no brief exists → create one from the template in `clients/_index.md`
6. Move file to `raw/processed/`

**Link / URL (`raw/links/`)**
1. Read the file — it contains a URL and optionally a one-line note on why it was saved
2. Identify the URL type:
   - **YouTube** → fetch the page, extract the transcript (look for the transcript panel or `timedtext` in the page source). If no transcript is available, use the description + comments for context.
   - **Article / blog post** → fetch and read the full text
   - **Podcast with transcript** → fetch and read
   - **Twitter/X thread** → fetch and read
3. Identify what the content is about — brand strategy, competitor, audience insight, content idea, framework, research
4. Synthesize the key intelligence (not a summary — extract what's *useful for Envisioned*): claims that challenge or reinforce positioning, frameworks worth knowing, audience language, content angles
5. Determine which wiki article it should enrich (check `wiki/index.md`), or create a new article if the gap is significant
6. Move file to `raw/processed/`

**Web clip (`raw/web-clips/`)**
1. Read the file — Obsidian Web Clipper has already fetched the full content
2. Same as steps 3–6 above (identify → synthesize → route to wiki → move to processed)

**Notes / voice memos (`raw/notes/`)**
1. Read the file
2. Classify: brand insight → wiki update; client context → client brief; content idea → `content-engine/`; operational decision → relevant offer or strategy file
3. Route accordingly and write the update
4. Move file to `raw/processed/`

**Client docs (`raw/client-docs/`)**
1. Read the file
2. Identify which client it belongs to
3. Extract anything that updates Key Context, Open Threads, or changes the engagement
4. Update `clients/[name].md`
5. Move original to `04-CLIENTS/clients/[name]/` for deep storage
6. Move file to `raw/processed/`

### Step 3 — Generate content output
For each processed file, extract content seeds:

- Create a dated file: `content/ideas/YYYY-MM-DD-[source-name].md`
- Pull out: 3–5 strong hooks or opening lines; 2–3 post angles; any client quotes worth using; the single strongest idea that could stand alone as a post
- If the material is rich enough, write 1 full draft in Envisioned voice and save to `content/drafts/YYYY-MM-DD-[topic].md`
- Label each draft with suggested platform: LinkedIn / Instagram / Substack / Email

### Step 4 — Log
Add one line per processed file to ## Log below.

**Rule:** Do not summarise raw content verbatim in briefs or wiki. Extract the intelligence. Keep it scannable.

---

## Operation: QUERY (answer a brand question)

Use when asked anything about voice, offers, audience, positioning, frameworks.

1. Check `wiki/index.md` to find the right article(s)
2. Read the relevant wiki file(s)
3. Answer using the wiki as ground truth
4. If the answer reveals a gap in the wiki → flag it or update the wiki article

**Do not answer brand questions from memory or this file alone.** The wiki is the brain.

---

## Operation: CREATE CONTENT (write a post, article, email, caption)

Use for any content creation task.

1. Load (in this order):
   - `wiki/voice/` — voice rules, forbidden phrases, NASAmeter
   - `wiki/identity/` — positioning, values, founder profile
   - `wiki/operations/content-output-standards.md` — HTML, SEO, formatting
   - `wiki/operations/article-structure.md` — if writing an article (7 beats)
   - `wiki/content/` — pillars, angles, platform playbooks
   - **If writing an email or email subject line → also load `wiki/operations/email-deliverability.md`** — spam trigger words, subject line rules, pre-send checklist
2. Write content
3. Self-audit: no forbidden phrases, NASAmeter check, em-dash count (max 1–2 per paragraph, ideally zero), no hedging, no softening
4. **If email:** run the pre-send checklist from `email-deliverability.md` — flag any spam trigger words in the subject line and body, note which tool to use (sendcheckit.com for subject, spamcheck.postmarkapp.com for full copy) before finalising
5. Present as draft — do not auto-publish.
6. **When Maria-Ines approves it → run Operation: APPROVE CONTENT** (below).

---

## Operation: APPROVE CONTENT (save approved work into the vault) ⭐

**This is the loop that keeps the vault alive.** Trigger when Maria-Ines says any of: "approve this", "approved", "save this", "log this", "this is good — file it".

Works for ALL content types: social posts/captions, carousels, emails/newsletters, client deliverables.

### Step 1 — Save the approved piece
Create `content/published/YYYY-MM-DD-[platform]-[short-slug].md` using the template in `content/_templates/published-piece.md`. Fill the frontmatter:
- `date`, `platform` (instagram/facebook/linkedin/substack/email), `type` (post/carousel/email/client), `client` (if any), `pillar`, `status: approved`, `source` (live URL once posted)
Paste the FINAL approved copy in the body. For carousels, save slide-by-slide copy; for client work, tag the client.

### Step 2 — Log it
Prepend one row (newest first) to `content/published/_index.md`:
`| date | platform | type | title | client | link |`

### Step 3 — Feed the brain (this is what makes future content better)
Ask: did this piece contain a hook, phrase, story beat, or angle worth reusing?
- New reusable hook/angle → add to `wiki/content/content-angles.md`
- New story or proof moment → add to `wiki/proof/story-bank.md`
- A phrase that's unmistakably her → add to `wiki/voice/voice-guide.md`
Make targeted additions only. Note the change in `wiki/log.md` (or wiki/index).

### Step 4 — For client deliverables
Also update `clients/[name].md` (what was delivered / what's next) and deep-store the asset under `04-CLIENTS/clients/[name]/`.

### Step 5 — Confirm
Tell her exactly what was saved and where (file path + index updated + any wiki enrichment).

> The point: every approval makes the vault more *you*. Approved content is the highest-quality voice training data that exists — richer than the old archive, because you stood behind it.

---

## Operation: UPDATE CLIENT BRIEF (after a call or new info)

Use when Maria-Ines shares new client information between calls.

1. Open `clients/[name].md`
2. Update the relevant section(s)
3. If a new open thread is resolved → move it to a Done section or remove it
4. If context has fundamentally shifted → update Key Context

---

## Operation: UPDATE WIKI (new brand doctrine)

Use when something in the wiki needs updating — new offer, refined positioning, new framework.

1. Identify which wiki article(s) to update
2. Read the current article
3. Make targeted edits — do not rewrite unless the whole article is wrong
4. Log the change in `wiki/index.md` if it's a structural addition
5. Add one line to ## Log below

---

## The ONE Thesis

> AI isn't a productivity hack — it's a mirror that forces you to decide who you are when effort no longer proves worth.

Every piece of content, every answer, every client brief points here.

---

## Voice Baseline (full rules in `wiki/voice/`)

- Story-first openings. Thesis emerges from the story.
- Reframe formula: "This isn't [surface]. It's [deeper truth]."
- Em-dashes: max 1–2 per paragraph, ideally zero. Parentheses preferred.
- No "Listen." / "Here's the truth." as openers — emergency fallbacks only.
- No softening, no hedging, no generic business advice.
- She is NOT a business coach. She builds AI-powered infrastructure that codifies founder intelligence.
- Forbidden phrases, NASAmeter, full voice architecture → `wiki/voice/`

---

## Active Clients (as of 2026-05-07)

| Client | Offer | Brief |
|--------|-------|-------|
| Rachel Cook | CITC | [[clients/rachel-cook]] |
| Laura Muirhead | Brand + AI | [[clients/laura-muirhead]] |
| Suzi Gray | Brand + AI | [[clients/suzi-gray]] |
| Holly MacCue | Brand + AI | [[clients/holly-maccue]] |
| Amber McCue | Brand + AI | [[clients/amber-mccue]] |
| Dr Nathalie Yercovich | Brand + AI | [[clients/nathalie-yercovich]] |

---

## Log

| Date | Operation | Notes |
|------|-----------|-------|
| 2026-06-17 | UPGRADE | Repointed all instructions from the deprecated `Envisioned wiki/` to the live `wiki/`. Added Operation: APPROVE CONTENT (approve → save to content/published + log + enrich wiki). Set up content/published/_index.md + _templates/. |
| 2026-05-07 | INIT | agents.md created. Client briefs scaffolded for 6 active clients. Tracy Litt moved to standalone Aureum second brain at `04-CLIENTS/clients/tracy-litt/second-brain/`. raw/ inbox created with zoom/, web-clips/, notes/, client-docs/, processed/ subfolders. |
