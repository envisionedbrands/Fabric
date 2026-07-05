# raw/ — The Inbox

Drop anything here. Claude processes it. Nothing in this folder is ever rewritten or deleted — it's the immutable source record.

---

## What goes where

| Subfolder | Drop here |
|-----------|-----------|
| `zoom/` | Zoom VTT transcripts (copy from `04-CLIENTS/zoom-transcripts/YYYY-MM/`) |
| `links/` | YouTube videos, articles, podcasts, Twitter threads — paste the URL in a new .md file, one URL per file, add a one-line note on why you saved it |
| `web-clips/` | Obsidian Web Clipper saves — full page content already fetched by the clipper |
| `notes/` | Voice memo transcripts, quick Obsidian captures, rough thoughts |
| `client-docs/` | Files received from clients — intake forms, questionnaires, documents they've sent |
| `processed/` | Files move here automatically after INGEST — do not put files here manually |

---

## How to trigger processing

Open a Claude Code session at the vault root and say:

> "Run INGEST"

Claude will:
1. Read everything in `raw/` (excluding `processed/`)
2. Identify what kind of content each file is
3. Synthesize it into the right place:
   - Zoom call → update `clients/[name].md` brief
   - Web clip → add to relevant `Envisioned wiki/` article or create a new one
   - Client doc → update `clients/[name].md` key context
   - Notes → route to wiki, client brief, or content ideas depending on content
4. Move processed files to `raw/processed/`
5. Log what was done

---

## Rules

- **Never edit files in `raw/`** — they are source material
- **Never put processed files back into raw/** — one-way flow only
- If a file is ambiguous, Claude will ask before processing
