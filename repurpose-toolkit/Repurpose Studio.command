#!/usr/bin/env bash
# Double-click to open the Repurpose Studio dashboard.
# Keep this window open while you use it; close it (or press Ctrl+C) to stop.
cd "$(dirname "$0")"
echo "Starting Repurpose Studio…"
exec python3 dashboard.py
