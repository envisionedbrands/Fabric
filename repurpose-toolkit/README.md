# Repurpose Toolkit

Turn one piece of long-form content into a full kit of platform-ready assets with a single command — the "transform" engine of a repurpose.io-style workflow, built on [Fabric](https://github.com/danielmiessler/fabric) and running entirely on your own machine with your own AI API key.

**One input** (a YouTube URL, a local video/audio file, or a transcript) **→ nine outputs:**

| File | What it is |
|---|---|
| `twitter_thread.md` | 6–10 post X thread + 3 alternate hooks |
| `linkedin_post.md` | LinkedIn post with hook, formatting, hashtags + alternates |
| `instagram.md` | Reel caption + hashtags, carousel concept, story sequence |
| `shorts_clips.md` | 3–6 clip-worthy moments with timestamps, hooks, captions |
| `make_clips.sh` | Runnable ffmpeg script that cuts those clips to vertical 9:16 |
| `youtube_metadata.md` | 5 titles, description, chapters, tags, pinned comment |
| `key_ideas.md` | Extracted insights, quotes and references |
| `summary.md` | 5-sentence summary |
| `newsletter.md` / `chapters.md` | Newsletter blurb and video chapter list |

## Setup (once, ~10 minutes)

1. **Install Fabric** — download a release from [github.com/danielmiessler/fabric/releases](https://github.com/danielmiessler/fabric/releases) or:
   ```bash
   go install github.com/danielmiessler/fabric/cmd/fabric@latest
   ```
2. **Configure it** with an AI provider key (Anthropic, OpenAI, or a local model via Ollama):
   ```bash
   fabric --setup
   ```
3. **(Optional, for local video/audio)** install `ffmpeg` for clip cutting, and configure a transcription model in fabric setup (e.g. OpenAI Whisper) to use `-a`.

That's it — the script installs its custom patterns into `~/.config/fabric/patterns` automatically on first run.

## Usage

```bash
cd repurpose-toolkit

# From a YouTube video (needs captions; timestamps enable real clip cuts)
./repurpose.sh -y "https://www.youtube.com/watch?v=VIDEO_ID"

# From a local video or podcast audio file (transcribed first)
./repurpose.sh -a episode.mp3

# From an existing transcript, article, or blog post
./repurpose.sh -f transcript.txt

# Pick a specific model, custom output folder
./repurpose.sh -y "URL" -m claude-sonnet-5 -o ./client-acme/ep42
```

Then to cut the vertical clips from the source video:

```bash
cd output/<name>-<date>
VIDEO=/path/to/source.mp4 ./make_clips.sh
```

> Always eyeball the timestamps in `shorts_clips.md` before publishing — the AI picks the moments, but a human should confirm the cut points.

## Using it for clients

- Keep one output folder per client/episode: `-o ./clients/acme/2026-07-04-ep42`.
- The patterns live in `patterns/` — edit `system.md` files to bake in a client's voice, banned words, CTA links, or hashtag sets, and the changes apply on the next run. You can also duplicate a pattern per client (e.g. `create_linkedin_post_acme`).
- Cost per run is just your API usage — typically a few cents per video with a mid-tier model.

## What this deliberately does NOT do (yet)

Auto-*publishing* to TikTok/Instagram/YouTube (what repurpose.io charges for) requires an approved developer app and OAuth review with each platform — not practical for a personal tool. The pragmatic pipeline is:

1. **This toolkit** does the transformation (the time-consuming creative part).
2. **A scheduler you already have access to** does the posting: Buffer, Metricool, Publer, or Later can bulk-import the generated text + clips and publish everywhere on a calendar. Most have free or ~$10/mo tiers.

If you later want direct publishing for one or two platforms (e.g. YouTube uploads via its official API, which is self-serve), that's a reasonable v2 — open an issue or just ask.
