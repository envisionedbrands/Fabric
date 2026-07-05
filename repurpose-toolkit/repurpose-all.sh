#!/usr/bin/env bash
# repurpose-all.sh — ONE command that does BOTH halves:
#   1. writes all your platform text (posts, threads, captions, titles, clip picks) in your voice
#   2. rough-cuts the best moments and drops them into HyperFrame's watch folder,
#      which auto-finishes them into vertical, captioned short-form videos.
#
# Usage:
#   ./repurpose-all.sh -y "https://youtube.com/watch?v=..."      # YouTube video
#   ./repurpose-all.sh -a "/path/to/episode.mp4"                  # local video/podcast
#   ./repurpose-all.sh -f transcript.txt                          # existing transcript (text only)
#
# Options: same as repurpose.sh (-o output dir, -m model, -s skip pattern refresh).

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# ─────────────────────────────────────────────────────────────────────────────
# CONFIG — set this ONCE to the folder HyperFrame watches (where you drop videos).
# Override any time with:  HYPERFRAME_STUDIO="/path" ./repurpose-all.sh ...
: "${HYPERFRAME_STUDIO:=/Volumes/Maria-Ines New SSD T7/maria-ines/envisioned-os-april-2026/VIdeos HyperFrame}"
# ─────────────────────────────────────────────────────────────────────────────

log() { printf '\033[36m▸\033[0m %s\n' "$*"; }
warn() { printf '\033[33m⚠\033[0m  %s\n' "$*" >&2; }

# We need the source video path to cut clips from. Capture -a (local file); for -y
# (YouTube) there's no local file, so we can only produce text + clip picks, not cut.
SOURCE_VIDEO=""
for ((i=1; i<=$#; i++)); do
  if [ "${!i}" = "-a" ]; then j=$((i+1)); SOURCE_VIDEO="${!j:-}"; fi
done

# 1) TEXT + CLIP PICKS ─────────────────────────────────────────────────────────
log "Step 1/2 — writing your content kit (text + clip picks)…"
# Pass everything straight through to repurpose.sh and capture its output folder.
"$SCRIPT_DIR/repurpose.sh" "$@" | tee /tmp/repurpose-all.log
OUT_DIR="$(grep -oE '/[^ ]+' /tmp/repurpose-all.log | grep -E 'output|/' | tail -1 || true)"
# More robust: read the "content kit is in:" line.
OUT_DIR="$(grep 'content kit is in' /tmp/repurpose-all.log | sed 's/.*content kit is in: //' | tail -1)"
[ -n "$OUT_DIR" ] && [ -d "$OUT_DIR" ] || { warn "Couldn't locate the output folder; text is done, skipping video step."; exit 0; }

# 2) CUT CLIPS → HAND TO HYPERFRAME ──────────────────────────────────────────────
CLIP_SCRIPT="$OUT_DIR/make_clips.sh"
if [ ! -f "$CLIP_SCRIPT" ]; then
  log "No timestamped clips were produced (transcript had no timestamps). Text kit is ready in: $OUT_DIR"
  exit 0
fi
if [ -z "$SOURCE_VIDEO" ]; then
  warn "Clip picks are in $OUT_DIR/shorts_clips.md, but I need the SOURCE VIDEO FILE to cut them."
  warn "Re-run with -a \"/path/to/video.mp4\" (a local file), or cut manually per shorts_clips.md."
  exit 0
fi
if [ ! -e "$HYPERFRAME_STUDIO" ]; then
  warn "HyperFrame watch folder not found:"
  warn "  $HYPERFRAME_STUDIO"
  warn "Fix the HYPERFRAME_STUDIO path at the top of this script, then re-run. Rough clips left in $OUT_DIR."
  ( cd "$OUT_DIR" && VIDEO="$SOURCE_VIDEO" bash make_clips.sh ) || true
  exit 0
fi

log "Step 2/2 — cutting clips and dropping them into HyperFrame to finish…"
( cd "$OUT_DIR" && VIDEO="$SOURCE_VIDEO" HYPERFRAME_STUDIO="$HYPERFRAME_STUDIO" bash make_clips.sh )

echo
log "All done."
log "  • Text content:  $OUT_DIR   (open linkedin_post.md first)"
log "  • Short videos:  HyperFrame is now finishing them into vertical captioned clips."
log "                   Look in its output folder in a few minutes for the FINAL.mp4s."
