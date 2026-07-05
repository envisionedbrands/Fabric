---
name: repurpose-studio
description: Full repurposing pipeline in one command. Give it a long horizontal talking-head video and it produces — a tightened master (silences, fillers, retakes removed), on-brand 9:16 vertical clips with karaoke captions chosen against the Envisioned brand pillars, and a complete written content kit (LinkedIn, X thread, Instagram, YouTube metadata) in María-Inés's voice. Triggers on "repurpose this video", "/repurpose-studio", "full repurpose", "run the studio on this", or a video path with a request for short-form + content.
---

# Repurpose Studio

One command: long horizontal video in → clean master + on-brand vertical clips + full written content kit out.

This skill ORCHESTRATES existing tools — it does not duplicate them:
- **cut-video** skill → tightens the master (silences, fillers, retakes)
- **repurpose-toolkit** (`~/fabric/repurpose-toolkit/repurpose.sh`) → the brand brain: writes all text content AND selects clip moments against the Envisioned pillars
- **clipify** skill → cuts the chosen moments to 9:16 with karaoke word-by-word captions
- **hyperframes-helper** skill (optional) → motion-graphic overlays on hero clips

## Pipeline — follow in order

### Step 1 — Tighten the master (cut-video)
Run the **cut-video** skill on the input video. Remove silences, fillers (um/uh), retakes, and dead air; preserve intentional pauses. Save the result as `<name>_master.mp4` next to the original. ALL later steps use this cleaned master, never the raw original (timestamps must match the cleaned cut).

### Step 2 — Brand brain: text kit + on-brand clip selection (repurpose-toolkit)
```bash
cd ~/fabric/repurpose-toolkit
./repurpose.sh -a "/path/to/<name>_master.mp4"
```
This transcribes the cleaned master and produces the output folder: linkedin_post.md, twitter_thread.md, instagram.md, youtube_metadata.md, summary, newsletter — all in her voice — plus `shorts_clips.md`, where moments are selected against the brand compass (≥2 pillars, no Type 1/2/3-sounding moments, sensory grounding) with timestamps, hooks, and captions.

### Step 3 — Cut the verticals (clipify)
For each clip in `shorts_clips.md`: run the **clipify** skill on the cleaned master with that clip's start–end timestamps. Requirements:
- Reformat 16:9 → 9:16 (face-pan mode for a single talking head)
- Burn karaoke-style word-by-word captions
- Name outputs `<name>_clip01.mp4`, `<name>_clip02.mp4`, …
- Use the HOOK text from shorts_clips.md as the opening on-screen text if clipify supports title cards
Important: clipify's own "find funny moments" analysis is NOT used — the moments come from Step 2 (brand-selected). Clipify only cuts, reframes, and captions.

### Step 4 (optional, on request) — Motion graphics (hyperframes-helper)
If asked for motion graphics / story cards: run **hyperframes-helper** on the best 1–2 clips using the brand design system (Cormorant Garamond, sage #516b62, glass cards).

### Step 5 — Deliver
Report a single summary: path to the cleaned master, list of finished vertical clips with their pillar tags, and the text-kit folder. Suggest which clip to post first (the one touching the most pillars with the strongest hook).

## Rules
- Never analyze the raw original for clip moments — always the cleaned master.
- If cut-video fails or the video is already tight, proceed with the original and say so.
- If a clip's timestamps look misaligned after cutting (word cut mid-sentence), re-check against the transcript and adjust by up to ±2 seconds at each end to land on sentence boundaries.
- Text content and clip selection are already brand-filtered by the toolkit — do not re-write them, only flag anything that seems off-voice.
