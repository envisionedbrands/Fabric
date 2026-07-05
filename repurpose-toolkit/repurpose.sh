#!/usr/bin/env bash
# repurpose.sh — turn one piece of long-form content into platform-ready assets.
#
# Usage:
#   ./repurpose.sh -y "https://youtube.com/watch?v=..."   # YouTube video
#   ./repurpose.sh -f transcript.txt                       # existing transcript / article
#   ./repurpose.sh -a episode.mp3                          # local audio/video (transcribed first)
#
# Options:
#   -o DIR      output directory (default: ./output/<name>-<date>)
#   -m MODEL    model to use, passed to fabric (e.g. -m gpt-4o, -m claude-sonnet-5)
#   -s          skip pattern install/refresh
#
# Requires: fabric (https://github.com/danielmiessler/fabric), configured with `fabric --setup`.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PATTERNS_SRC="$SCRIPT_DIR/patterns"
FABRIC_PATTERNS_DIR="${FABRIC_PATTERNS_DIR:-$HOME/.config/fabric/patterns}"

# Custom patterns shipped with this toolkit
CUSTOM_PATTERNS=(
  create_twitter_thread
  create_linkedin_post
  create_instagram_caption
  create_shorts_clips
  create_youtube_metadata
)

# Built-in fabric patterns we also run
BUILTIN_PATTERNS=(
  extract_wisdom
  create_5_sentence_summary
  create_newsletter_entry
  create_video_chapters
)

usage() { sed -n '2,15p' "$0" | sed 's/^# \{0,1\}//'; exit 1; }

err() { printf '\033[31mERROR:\033[0m %s\n' "$*" >&2; exit 1; }
log() { printf '\033[36m▸\033[0m %s\n' "$*"; }

YOUTUBE_URL="" ; INPUT_FILE="" ; MEDIA_FILE="" ; OUT_DIR="" ; MODEL="" ; SKIP_INSTALL=0
while getopts "y:f:a:o:m:sh" opt; do
  case "$opt" in
    y) YOUTUBE_URL="$OPTARG" ;;
    f) INPUT_FILE="$OPTARG" ;;
    a) MEDIA_FILE="$OPTARG" ;;
    o) OUT_DIR="$OPTARG" ;;
    m) MODEL="$OPTARG" ;;
    s) SKIP_INSTALL=1 ;;
    h|*) usage ;;
  esac
done

# The Homebrew formula installs the binary as `fabric-ai`; other installs use `fabric`.
if command -v fabric >/dev/null 2>&1; then
  FABRIC=fabric
elif command -v fabric-ai >/dev/null 2>&1; then
  FABRIC=fabric-ai
else
  err "fabric is not installed (looked for 'fabric' and 'fabric-ai'). See README.md for setup."
fi
[ -n "$YOUTUBE_URL$INPUT_FILE$MEDIA_FILE" ] || usage

MODEL_ARGS=()
[ -n "$MODEL" ] && MODEL_ARGS=(-m "$MODEL")

# --- Install/refresh custom patterns into fabric's patterns dir -------------
if [ "$SKIP_INSTALL" -eq 0 ]; then
  mkdir -p "$FABRIC_PATTERNS_DIR"
  for p in "${CUSTOM_PATTERNS[@]}"; do
    mkdir -p "$FABRIC_PATTERNS_DIR/$p"
    cp "$PATTERNS_SRC/$p/system.md" "$FABRIC_PATTERNS_DIR/$p/system.md"
  done
  log "Installed ${#CUSTOM_PATTERNS[@]} custom patterns into $FABRIC_PATTERNS_DIR"
fi

# --- Get the transcript ------------------------------------------------------
NAME="content"
TRANSCRIPT=""
if [ -n "$YOUTUBE_URL" ]; then
  NAME="$(printf '%s' "$YOUTUBE_URL" | sed -E 's#.*[?&]v=([A-Za-z0-9_-]{6,}).*#\1#; s#.*/##')"
  log "Fetching transcript (with timestamps) from YouTube…"
  TRANSCRIPT="$("$FABRIC" -y "$YOUTUBE_URL" --transcript-with-timestamps)" \
    || err "Could not fetch transcript. Is the video public and captioned?"
elif [ -n "$MEDIA_FILE" ]; then
  [ -f "$MEDIA_FILE" ] || err "File not found: $MEDIA_FILE"
  NAME="$(basename "${MEDIA_FILE%.*}")"
  log "Transcribing $MEDIA_FILE (this can take a while)…"
  TRANSCRIPT="$("$FABRIC" --transcribe-file "$MEDIA_FILE" "${MODEL_ARGS[@]}")" \
    || err "Transcription failed. Check that your fabric transcription model is configured."
else
  [ -f "$INPUT_FILE" ] || err "File not found: $INPUT_FILE"
  NAME="$(basename "${INPUT_FILE%.*}")"
  TRANSCRIPT="$(cat "$INPUT_FILE")"
fi
[ -n "$TRANSCRIPT" ] || err "Got an empty transcript — nothing to repurpose."

OUT_DIR="${OUT_DIR:-$SCRIPT_DIR/output/${NAME}-$(date +%Y%m%d)}"
mkdir -p "$OUT_DIR"
printf '%s\n' "$TRANSCRIPT" > "$OUT_DIR/transcript.txt"
log "Transcript saved to $OUT_DIR/transcript.txt ($(printf '%s' "$TRANSCRIPT" | wc -w | tr -d ' ') words)"

# --- Run every pattern -------------------------------------------------------
run_pattern() {
  local pattern="$1" outfile="$2"
  log "Generating $outfile …"
  if printf '%s' "$TRANSCRIPT" | "$FABRIC" -p "$pattern" "${MODEL_ARGS[@]}" > "$OUT_DIR/$outfile" 2>"$OUT_DIR/.$pattern.err"; then
    rm -f "$OUT_DIR/.$pattern.err"
  else
    printf '\033[33mWARN:\033[0m %s failed — see %s\n' "$pattern" "$OUT_DIR/.$pattern.err" >&2
  fi
}

run_pattern create_twitter_thread    twitter_thread.md
run_pattern create_linkedin_post     linkedin_post.md
run_pattern create_instagram_caption instagram.md
run_pattern create_shorts_clips      shorts_clips.md
run_pattern create_youtube_metadata  youtube_metadata.md
run_pattern extract_wisdom           key_ideas.md
run_pattern create_5_sentence_summary summary.md
run_pattern create_newsletter_entry  newsletter.md
run_pattern create_video_chapters    chapters.md

# --- Extract ffmpeg commands into a runnable clip script ----------------------
# These are ROUGH CUTS ONLY (trim at original framing). The finishing work —
# reframe to vertical, filler/silence removal, karaoke captions — is handed off
# to HyperFrame, which is a far better renderer than a crude ffmpeg crop.
# Set HYPERFRAME_STUDIO to HyperFrame's watch folder to auto-drop the cuts there.
if [ -f "$OUT_DIR/shorts_clips.md" ] && grep -q '^ffmpeg ' "$OUT_DIR/shorts_clips.md"; then
  {
    echo '#!/usr/bin/env bash'
    echo '# Rough-cut the chosen moments from the source, at original framing/quality.'
    echo '# Usage: VIDEO=path/to/video.mp4 [HYPERFRAME_STUDIO=/path/to/hyperframe/studio] ./make_clips.sh'
    echo '# Then HyperFrame reframes to 9:16, removes fillers, and burns captions.'
    echo 'set -euo pipefail'
    echo ': "${VIDEO:?Set VIDEO=path/to/source-video.mp4}"'
    grep '^ffmpeg ' "$OUT_DIR/shorts_clips.md"
    echo 'if [ -n "${HYPERFRAME_STUDIO:-}" ] && [ -d "$HYPERFRAME_STUDIO" ]; then'
    echo '  for c in clip_*.mp4; do [ -f "$c" ] && cp "$c" "$HYPERFRAME_STUDIO/" && echo "→ dropped $c into HyperFrame studio"; done'
    echo 'else'
    echo '  echo "Rough clips ready. Drop clip_*.mp4 into HyperFrame'\''s studio folder to finish them,"'
    echo '  echo "or set HYPERFRAME_STUDIO to auto-drop them next time."'
    echo 'fi'
  } > "$OUT_DIR/make_clips.sh"
  chmod +x "$OUT_DIR/make_clips.sh"
  log "Rough-cut script written to $OUT_DIR/make_clips.sh (verify timestamps, then HyperFrame finishes them)"
fi

echo
log "Done. Your content kit is in: $OUT_DIR"
ls -1 "$OUT_DIR"
