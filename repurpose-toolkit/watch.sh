#!/usr/bin/env bash
# Drop-folder watcher: drop a video into ~/Desktop/Drop Videos Here and the
# full repurpose pipeline runs automatically. No terminal interaction.
#
# Started by "Start Video Watcher.command" (or run directly). macOS bash 3.2 safe.
#
# Behavior per video:
#   1. waits until the file finishes copying (size stable)
#   2. runs the FULL studio pipeline headlessly via Claude Code if available
#      (tighten -> text kit -> on-brand clips -> 9:16 captions -> motion
#      graphics per motion-style.md, self-approving the graphics plan);
#      falls back to repurpose.sh (text kit + rough clips) if claude is absent
#   3. moves the video to done/ (or failed/) and fires a macOS notification
#
# Results appear in the dashboard (Repurpose Studio.command) as usual.

set -u

DROP="${DROP_DIR:-$HOME/Desktop/Drop Videos Here}"
TOOLKIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOGS="$TOOLKIT/watch-logs"
STABLE_WAIT="${STABLE_WAIT:-8}"
POLL="${POLL:-15}"

mkdir -p "$DROP" "$DROP/done" "$DROP/failed" "$DROP/.processing" "$LOGS"

notify() { osascript -e "display notification \"$2\" with title \"$1\"" >/dev/null 2>&1 || true; }
fsize() { stat -f%z "$1" 2>/dev/null || stat -c%s "$1" 2>/dev/null || echo 0; }
log_line() { printf '%s %s\n' "$(date '+%F %T')" "$*" >> "$LOGS/watcher.log"; }

process() {
  base="$(basename "$1")"
  work="$DROP/.processing/$base"
  mv "$1" "$work" || return
  runlog="$LOGS/${base%.*}-$(date +%Y%m%d-%H%M%S).log"
  log_line "processing: $base"
  notify "Repurpose Studio" "Started: $base — you'll get a ping when it's done."

  if command -v claude >/dev/null 2>&1; then
    claude -p "Use the repurpose-studio skill on the video at '$work'. Run the FULL pipeline autonomously: tighten the master (silences, fillers, retakes), generate the complete text content kit, select on-brand clip moments, cut them to 9:16 with karaoke captions, and render motion graphics following ~/fabric/repurpose-toolkit/motion-style.md. Do NOT ask any questions — build and approve your own graphics plan strictly by the rules in motion-style.md (beat table, density limits, no graphics on emotional story peaks). When finished, print every output path." \
      --dangerously-skip-permissions > "$runlog" 2>&1
    status=$?
  else
    bash "$TOOLKIT/repurpose.sh" -a "$work" > "$runlog" 2>&1
    status=$?
  fi

  if [ "$status" -eq 0 ]; then
    mv "$work" "$DROP/done/$base"
    log_line "done: $base"
    notify "Repurpose Studio ✓" "Finished: $base — open the dashboard to review."
  else
    mv "$work" "$DROP/failed/$base"
    log_line "FAILED ($status): $base — see $runlog"
    notify "Repurpose Studio ✗" "Failed: $base — check watch-logs."
  fi
}

log_line "watcher started (drop folder: $DROP)"
while :; do
  for f in "$DROP"/*.mp4 "$DROP"/*.MP4 "$DROP"/*.mov "$DROP"/*.MOV "$DROP"/*.m4v "$DROP"/*.mts "$DROP"/*.MTS; do
    [ -f "$f" ] || continue
    s1="$(fsize "$f")"
    sleep "$STABLE_WAIT"
    s2="$(fsize "$f")"
    if [ "$s1" = "$s2" ] && [ "$s1" -gt 0 ] 2>/dev/null; then
      process "$f"
    fi
  done
  [ "${WATCH_ONCE:-0}" = "1" ] && break
  sleep "$POLL"
done
