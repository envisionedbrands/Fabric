#!/usr/bin/env bash
# Double-click to turn on the drop-folder watcher.
# After this, dropping any video into ~/Desktop/Drop Videos Here runs the
# whole repurpose pipeline automatically. You'll get a notification when done.
cd "$(dirname "$0")"
PIDFILE="$HOME/.repurpose-watcher.pid"

if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
  echo "✓ Watcher is already ON."
  echo "  Drop videos into:  ~/Desktop/Drop Videos Here"
  sleep 4
  exit 0
fi

nohup bash watch.sh >/dev/null 2>&1 &
echo $! > "$PIDFILE"
osascript -e 'display notification "Drop videos into ~/Desktop/Drop Videos Here" with title "Repurpose watcher is ON"' >/dev/null 2>&1 || true
echo "✓ Watcher is ON."
echo "  Drop videos into:  ~/Desktop/Drop Videos Here"
echo "  You can close this window — it keeps running in the background."
echo "  To turn it off:    kill \$(cat ~/.repurpose-watcher.pid)"
sleep 5
