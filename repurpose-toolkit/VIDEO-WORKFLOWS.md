# Video & Content Workflows — the consolidated map

You have several tools that all touch "video → content." They are **not duplicates of each other** — each owns a different stage. This is the single source of truth for which tool does what, where the overlaps were, and how they now hand off.

## The four layers

| Layer | Tool | Lives on | Owns |
|---|---|---|---|
| 1. Strategy / creation | **Content Engine** (Aureum/Envisioned) | Google Drive + `.skill` | Monthly topic bank → ~45–55 pieces created from themes, in brand voice |
| 2. Intelligence / distribution | **repurpose-toolkit** (this folder, in Fabric) | Cloud / any machine with Fabric | Takes an existing video/podcast → picks clip moments, writes all platform copy, metadata |
| 3. Video finishing | **HyperFrame** | Local Mac (`…/VIdeos HyperFrame`) | Transcribe → cut fillers/silence → reframe to 9:16 → burn karaoke captions → `FINAL.mp4` |
| 4. Publishing | *(not built)* | — | Push finished clips + copy to platforms (GHL Social Planner / Buffer) |

Layer 1 is **idea-first** (content created from a topic bank). Layer 2 is **video-first** (content derived from something you already recorded). They feed the same brand and can share the brand-voice skill, but they are different front doors and should stay separate.

## Where the real duplication was (now fixed)

Layers 2 and 3 both transcribed the video and both reframed it to vertical. HyperFrame does both far better (filler removal, silence trim, word-by-word captions) but only outputs one finished video. The toolkit does the part HyperFrame lacks (choosing the best moments + writing every caption/thread/title).

**Resolution:** the repurpose-toolkit no longer reframes or captions video. Its `make_clips.sh` now produces **rough cuts only** (`ffmpeg … -c copy`, original framing) and hands them to HyperFrame:

```
source video ──▶ repurpose-toolkit ──▶ rough clips (clip_01.mp4 …) ──▶ HyperFrame ──▶ FINAL.mp4 (9:16, captioned)
                       │                                                                       │
                       └──▶ threads / captions / titles / metadata ──────────────────┐        │
                                                                                      ▼        ▼
                                                                             Layer 4: publish everywhere
```

Drop the rough clips into HyperFrame's studio folder manually, or set `HYPERFRAME_STUDIO=/path/to/studio` when you run `make_clips.sh` and it copies them in for you.

## HyperFrame's own cleanup (do on the Mac)

From the code audit, HyperFrame has internal duplication too:
- `process.py` (the entry pipeline) has known bugs — over-aggressive silence cuts, audio drift, and it crops landscape footage.
- `refix.py` is the **good, working version** that fixes all of those, but its improvements were never merged back.

**Recommendation:** make `refix.py`'s tuning the default in the entry pipeline and retire `process.py`'s crop-happy path. The karaoke-caption + reframe chain is the real, valuable artifact — keep it. The iMessage story-card approval loop ran once and stalled; treat it as an experiment, not core.

## Content Engine cleanup (do in Drive)

The strategy doc exists in 7+ copies across formats and dates (`content-engine.md`, `The Content Engine.docx`/`.txt`, `content-engine.skill`, and three `envisioned-content-engine-plugin*.zip`s). Designate the **Aureum wiki `content-engine.md`** (most current) as canonical and move the rest into `_ARCHIVE for Content Engine project`.

## Open item

- **`/watch` skill** — needs identifying. If it's the fswatch daemon that feeds HyperFrame's studio folder, it belongs to Layer 3. If it's a "watch this video → summarize" skill, it may overlap with the repurpose-toolkit's intake and should be folded in or retired. Confirm what it does.

## The unified pipeline: `/repurpose-studio`

After auditing all seven video skills on the Mac (clipify, cut-video, video-use, clip-cutter, hyperframes-helper, create-video, video-analyzer), the consolidation is:

- **Keep as building blocks:** video-use (edit engine), cut-video (tightener), hyperframes-helper (motion graphics), create-video (separate product — AI promo videos)
- **One clip-maker:** **clipify** (cuts + 9:16 reframe + karaoke captions). **Retire clip-cutter** (subset of clipify). **HyperFrame is legacy** — superseded by clipify + this pipeline.
- **The brain:** repurpose-toolkit selects clip moments against the **brand compass** (three pillars, Type 1/2/3 red-flag filter, sensory grounding — see `patterns/_brand_compass.md`) and writes all copy in brand voice.
- **The orchestrator:** `skills/repurpose-studio/SKILL.md` — install to `~/.claude/skills/repurpose-studio/` and one command chains: cut-video → repurpose-toolkit → clipify (→ hyperframes).

## One-line answer to "which tool do I use?"

- **Long horizontal video → everything (clean master + on-brand reels + all posts)** → `/repurpose-studio` on the Mac.
- **Just the text kit from a YouTube link** → `repurpose.sh -y` anywhere.
- **Starting from monthly themes, no video** → Content Engine.
