#!/usr/bin/env python3
"""Repurpose Studio dashboard — a local web UI for the repurpose-toolkit.

Zero dependencies (Python 3 stdlib only). Run:

    python3 dashboard.py            # opens http://127.0.0.1:8787

What it does:
  • Run a repurpose job (YouTube URL, local video/audio path, or transcript path)
  • Watch the live log while it runs
  • Browse every content kit ever generated; read posts with copy buttons
  • Preview any cut clips (mp4) found in a kit folder

Binds to 127.0.0.1 only — never exposed to the network.
"""
import html.parser
import json
import os
import re
import shutil
import subprocess
import threading
import time
import urllib.parse
import urllib.request
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = Path(os.environ.get("REPURPOSE_OUTPUT", ROOT / "output"))
PORT = int(os.environ.get("REPURPOSE_PORT", "8787"))
FABRIC = shutil.which("fabric") or shutil.which("fabric-ai")

TEXT_EXT = {".md", ".txt", ".sh", ".json"}
VIDEO_EXT = {".mp4", ".mov"}

# Friendly labels + display order for kit files
FILE_META = [
    ("script.md", "Short Script"),
    ("linkedin_post.md", "LinkedIn Post"),
    ("twitter_thread.md", "X / Twitter Thread"),
    ("instagram.md", "Instagram"),
    ("shorts_clips.md", "Clip Picks"),
    ("youtube_metadata.md", "YouTube Metadata"),
    ("newsletter.md", "Newsletter"),
    ("summary.md", "Summary"),
    ("key_ideas.md", "Key Ideas"),
    ("chapters.md", "Chapters"),
    ("transcript.txt", "Transcript"),
]

_state = {"proc": None, "log": None, "label": ""}
_lock = threading.Lock()


def kit_list():
    kits = []
    if OUT.is_dir():
        for d in sorted(OUT.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True):
            if not d.is_dir() or d.name.startswith("."):
                continue
            files = [f.name for f in sorted(d.iterdir())
                     if f.suffix in TEXT_EXT | VIDEO_EXT and not f.name.startswith(".")]
            ordered = [n for n, _ in FILE_META if n in files]
            extras = [f for f in files if f not in ordered]
            kits.append({
                "name": d.name,
                "mtime": int(d.stat().st_mtime),
                "files": ordered + extras,
                "clips": [f for f in files if Path(f).suffix in VIDEO_EXT],
            })
    return kits


def safe_kit_path(kit, name):
    p = (OUT / kit / name).resolve()
    if not str(p).startswith(str(OUT.resolve()) + os.sep) or not p.is_file():
        return None
    return p


def start_run(source, model):
    with _lock:
        if _state["proc"] and _state["proc"].poll() is None:
            return False, "A run is already in progress."
        src = source.strip()
        if not src:
            return False, "Give me a YouTube URL or a file path."
        if src.startswith("http"):
            flag = "-y"
        elif Path(src).suffix.lower() in {".txt", ".md", ".srt"}:
            flag = "-f"
        else:
            flag = "-a"
        OUT.mkdir(parents=True, exist_ok=True)
        log_path = OUT / ".dashboard-run.log"
        log = open(log_path, "w")
        cmd = ["bash", str(ROOT / "repurpose.sh"), flag, src]
        if model.strip():
            cmd += ["-m", model.strip()]
        try:
            proc = subprocess.Popen(cmd, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT)
        except OSError as e:
            return False, f"Could not start: {e}"
        _state.update(proc=proc, log=log_path, label=src)
        return True, "started"


def run_status():
    with _lock:
        proc, log_path = _state["proc"], _state["log"]
        running = bool(proc and proc.poll() is None)
        tail = ""
        if log_path and Path(log_path).exists():
            text = Path(log_path).read_text(errors="replace")
            tail = text[-6000:]
        exit_code = proc.poll() if proc else None
        return {"running": running, "log": tail, "label": _state["label"],
                "exit_code": exit_code}


class _TextExtractor(html.parser.HTMLParser):
    """Crude article-text extractor: keeps text, drops script/style/nav."""
    SKIP = {"script", "style", "nav", "header", "footer", "aside", "form"}

    def __init__(self):
        super().__init__()
        self.parts, self._skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in self.SKIP and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip and data.strip():
            self.parts.append(data.strip())


def fetch_article(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read(1_500_000).decode("utf-8", errors="replace")
    p = _TextExtractor()
    p.feed(raw)
    return "\n".join(p.parts)


def make_short(source, directions, length, model):
    """Blocking: build input, run the create_shorts_script pattern, save a kit."""
    if not FABRIC:
        return None, "fabric is not installed (looked for 'fabric' and 'fabric-ai')."
    # make sure the pattern is installed
    pat_dir = Path.home() / ".config/fabric/patterns/create_shorts_script"
    pat_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(ROOT / "patterns/create_shorts_script/system.md", pat_dir / "system.md")

    material = source.strip()
    if material.startswith("http"):
        try:
            material = fetch_article(material)
        except OSError as e:
            return None, f"Could not fetch that URL: {e}"
    if not material:
        return None, "Paste an article URL, article text, or an idea brief."

    payload = ""
    if directions.strip():
        payload += f"DIRECTIONS: {directions.strip()}\n"
    if length.strip():
        payload += f"TARGET LENGTH: {length.strip()}\n"
    payload += "\nSOURCE MATERIAL:\n" + material

    cmd = [FABRIC, "-p", "create_shorts_script"]
    if model.strip():
        cmd += ["-m", model.strip()]
    try:
        res = subprocess.run(cmd, input=payload.encode(), capture_output=True, timeout=600)
    except subprocess.TimeoutExpired:
        return None, "The model took too long (10 min timeout)."
    if res.returncode != 0:
        return None, (res.stderr or b"fabric failed").decode(errors="replace")[-500:]

    slug = re.sub(r"[^a-z0-9]+", "-", (directions or material)[:40].lower()).strip("-") or "short"
    kit = OUT / f"short-{slug}-{time.strftime('%Y%m%d-%H%M%S')}"
    kit.mkdir(parents=True, exist_ok=True)
    (kit / "script.md").write_bytes(res.stdout)
    (kit / "source_material.txt").write_text(material)
    return kit.name, "ok"


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):  # quiet
        pass

    def _send(self, code, body, ctype="application/json"):
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        q = urllib.parse.parse_qs(url.query)
        if url.path == "/":
            self._send(200, INDEX_HTML.encode(), "text/html; charset=utf-8")
        elif url.path == "/api/kits":
            self._send(200, {"kits": kit_list()})
        elif url.path == "/api/status":
            self._send(200, run_status())
        elif url.path == "/api/file":
            p = safe_kit_path(q.get("kit", [""])[0], q.get("name", [""])[0])
            if p and p.suffix in TEXT_EXT:
                self._send(200, {"content": p.read_text(errors="replace")})
            else:
                self._send(404, {"error": "not found"})
        elif url.path == "/clip":
            p = safe_kit_path(q.get("kit", [""])[0], q.get("name", [""])[0])
            if p and p.suffix in VIDEO_EXT:
                self._send(200, p.read_bytes(), "video/mp4")
            else:
                self._send(404, {"error": "not found"})
        else:
            self._send(404, {"error": "not found"})

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        try:
            body = json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            return self._send(400, {"error": "bad json"})
        if self.path == "/api/run":
            ok, msg = start_run(body.get("source", ""), body.get("model", ""))
            self._send(200 if ok else 409, {"ok": ok, "message": msg})
        elif self.path == "/api/short":
            kit, msg = make_short(body.get("source", ""), body.get("directions", ""),
                                  body.get("length", ""), body.get("model", ""))
            self._send(200 if kit else 500, {"ok": bool(kit), "kit": kit, "message": msg})
        else:
            self._send(404, {"error": "not found"})


INDEX_HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Repurpose Studio</title>
<style>
  :root {
    --sage: #516b62; --sage-soft: #6e857c; --sage-tint: #eef2f0;
    --ink: #26312d; --muted: #75817c; --bg: #faf9f6; --card: #ffffff;
    --line: #e4e1da; --accent: #b08d57;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: 'Inter', -apple-system, sans-serif; background: var(--bg); color: var(--ink); }
  h1, h2, h3 { font-family: 'Cormorant Garamond', Georgia, serif; font-weight: 600; }
  header { padding: 26px 34px; border-bottom: 1px solid var(--line); display: flex; align-items: baseline; gap: 14px; }
  header h1 { font-size: 30px; color: var(--sage); }
  header span { color: var(--muted); font-size: 13.5px; }
  .layout { display: grid; grid-template-columns: 290px 1fr; min-height: calc(100vh - 81px); }
  aside { border-right: 1px solid var(--line); padding: 22px; }
  main { padding: 28px 34px; max-width: 900px; }

  .runbox { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 18px; margin-bottom: 26px; }
  .runbox h3 { color: var(--sage); font-size: 20px; margin-bottom: 10px; }
  .runbox input, .runbox textarea { width: 100%; padding: 10px 12px; border: 1px solid var(--line); border-radius: 8px; font-size: 13.5px; margin-bottom: 8px; background: var(--bg); font-family: inherit; resize: vertical; }
  .tabs { display: flex; gap: 6px; margin-bottom: 14px; }
  .tab { background: transparent; color: var(--muted); border: 1px solid var(--line); padding: 8px 14px; font-size: 13px; }
  .tab.active { background: var(--sage); color: #fff; border-color: var(--sage); }
  #prompter { display: none; position: fixed; inset: 0; background: #0d1210; z-index: 50; }
  #prompter .ptext { max-width: 780px; margin: 0 auto; padding: 45vh 40px 60vh; color: #f2f5f3; font-size: 44px; line-height: 1.55; font-family: 'Cormorant Garamond', Georgia, serif; white-space: pre-wrap; }
  #prompter .pbar { position: fixed; top: 0; left: 0; right: 0; display: flex; gap: 10px; justify-content: center; padding: 14px; background: rgba(13,18,16,.9); z-index: 51; }
  #prompter .pbar button { background: #2a3833; font-size: 13px; padding: 8px 14px; }
  #prompter .midline { position: fixed; top: 45vh; left: 0; right: 0; border-top: 2px solid rgba(176,141,87,.5); pointer-events: none; }
  .runrow { display: flex; gap: 8px; }
  .runrow input { flex: 1; margin-bottom: 0; }
  button { background: var(--sage); color: #fff; border: none; border-radius: 8px; padding: 10px 18px; font-size: 13.5px; font-weight: 600; cursor: pointer; }
  button:hover { background: var(--sage-soft); }
  button:disabled { opacity: .5; cursor: default; }
  #log { display: none; margin-top: 12px; background: var(--ink); color: #d7e2dd; border-radius: 8px; padding: 12px 14px; font: 11.5px/1.6 ui-monospace, monospace; white-space: pre-wrap; max-height: 220px; overflow-y: auto; }

  .kit-item { padding: 10px 12px; border-radius: 8px; cursor: pointer; margin-bottom: 4px; font-size: 13.5px; }
  .kit-item:hover { background: var(--sage-tint); }
  .kit-item.active { background: var(--sage); color: #fff; }
  .kit-item .d { font-size: 11px; opacity: .65; }
  aside h3 { color: var(--sage); font-size: 19px; margin-bottom: 12px; }
  .empty { color: var(--muted); font-size: 13px; line-height: 1.6; }

  .card { background: var(--card); border: 1px solid var(--line); border-left: 3px solid var(--sage); border-radius: 10px; margin-bottom: 18px; overflow: hidden; }
  .card .head { display: flex; justify-content: space-between; align-items: center; padding: 12px 18px; border-bottom: 1px solid var(--line); }
  .card .head h3 { font-size: 19px; color: var(--sage); }
  .copy { background: transparent; color: var(--sage); border: 1px solid var(--sage); padding: 5px 12px; font-size: 12px; }
  .copy:hover { background: var(--sage-tint); }
  .card .body { padding: 16px 18px; white-space: pre-wrap; font-size: 13.8px; line-height: 1.65; max-height: 420px; overflow-y: auto; }
  video { width: 240px; border-radius: 10px; display: block; }
  .clips { display: flex; gap: 14px; flex-wrap: wrap; padding: 16px 18px; }
  @media (max-width: 800px) { .layout { grid-template-columns: 1fr; } aside { border-right: none; border-bottom: 1px solid var(--line); } }
</style>
</head>
<body>
<header><h1>Repurpose Studio</h1><span>one video in — everything out, in your voice</span></header>
<div class="layout">
  <aside>
    <h3>Content kits</h3>
    <div id="kits"><div class="empty">No kits yet. Run your first video →</div></div>
  </aside>
  <main>
    <div class="runbox">
      <div class="tabs">
        <button class="tab active" id="tab-rep" onclick="setTab('rep')">Repurpose a video</button>
        <button class="tab" id="tab-short" onclick="setTab('short')">New short (from idea/article)</button>
      </div>
      <div id="pane-rep">
        <input id="source" placeholder="YouTube URL, or /path/to/video.mp4, or /path/to/transcript.txt">
        <div class="runrow">
          <input id="model" placeholder="model override (optional, e.g. claude-opus-4-8)">
          <button id="runbtn" onclick="run()">Run</button>
        </div>
      </div>
      <div id="pane-short" style="display:none">
        <textarea id="short-source" rows="4" placeholder="Paste an article URL, article text, or describe your idea"></textarea>
        <input id="short-directions" placeholder="Directions — angle, what to emphasize, CTA (optional)">
        <div class="runrow">
          <input id="short-length" placeholder="target length (e.g. 45 seconds)" style="max-width:200px">
          <input id="short-model" placeholder="model override (optional)">
          <button id="shortbtn" onclick="makeShort()">Write script</button>
        </div>
      </div>
      <div id="log"></div>
    </div>
    <div id="kitview"><div class="empty">Select a kit on the left to review its content — or start a new run.</div></div>
  </main>
</div>
<div id="prompter">
  <div class="pbar">
    <button onclick="pPlay()" id="pplay">Play</button>
    <button onclick="pSpeed(-0.2)">Slower</button>
    <button onclick="pSpeed(0.2)">Faster</button>
    <button onclick="pFont(-4)">A−</button>
    <button onclick="pFont(4)">A+</button>
    <button onclick="pClose()">Close (Esc)</button>
  </div>
  <div class="midline"></div>
  <div class="ptext" id="ptext"></div>
</div>
<script>
let kits = [], current = null, polling = null;
let pTimer = null, pV = 1.0;

function setTab(t) {
  document.getElementById('tab-rep').classList.toggle('active', t === 'rep');
  document.getElementById('tab-short').classList.toggle('active', t === 'short');
  document.getElementById('pane-rep').style.display = t === 'rep' ? '' : 'none';
  document.getElementById('pane-short').style.display = t === 'short' ? '' : 'none';
}

async function makeShort() {
  const btn = document.getElementById('shortbtn');
  const log = document.getElementById('log');
  btn.disabled = true; log.style.display = 'block';
  log.textContent = 'Writing your script (30–90 seconds)…';
  try {
    const r = await fetch('/api/short', { method: 'POST', headers: {'Content-Type':'application/json'},
      body: JSON.stringify({
        source: document.getElementById('short-source').value,
        directions: document.getElementById('short-directions').value,
        length: document.getElementById('short-length').value,
        model: document.getElementById('short-model').value }) });
    const j = await r.json();
    if (j.ok) { log.textContent = '✓ Script ready.'; current = j.kit; await loadKits(true); openKit(j.kit); }
    else log.textContent = '✗ ' + j.message;
  } catch (e) { log.textContent = '✗ ' + e; }
  btn.disabled = false;
}

// ---- Teleprompter ----
function openPrompter(text) {
  // strip B-ROLL notes and section headers that shouldn't be read aloud
  const spoken = text.split('\n').filter(l =>
    !/^\[B-ROLL/i.test(l.trim()) && !/^(FACT CHECK|ON-SCREEN TEXT|ALT HOOKS|METADATA)\b/i.test(l.trim())
  ).join('\n');
  const cut = spoken.split(/\nFACT CHECK/i)[0];
  document.getElementById('ptext').textContent = cut.trim();
  document.getElementById('prompter').style.display = 'block';
  window.scrollTo(0, 0); document.getElementById('prompter').scrollTop = 0;
}
function pPlay() {
  const box = document.getElementById('prompter');
  if (pTimer) { clearInterval(pTimer); pTimer = null; document.getElementById('pplay').textContent = 'Play'; return; }
  document.getElementById('pplay').textContent = 'Pause';
  pTimer = setInterval(() => { box.scrollTop += pV; }, 16);
}
function pSpeed(d) { pV = Math.max(0.2, pV + d); }
function pFont(d) {
  const el = document.getElementById('ptext');
  el.style.fontSize = (parseFloat(getComputedStyle(el).fontSize) + d) + 'px';
}
function pClose() {
  if (pTimer) { clearInterval(pTimer); pTimer = null; }
  document.getElementById('pplay').textContent = 'Play';
  document.getElementById('prompter').style.display = 'none';
}
document.addEventListener('keydown', e => { if (e.key === 'Escape') pClose(); });
document.getElementById('prompter').style.overflowY = 'auto';

async function loadKits(keepSel) {
  kits = (await (await fetch('/api/kits')).json()).kits;
  const el = document.getElementById('kits');
  if (!kits.length) { el.innerHTML = '<div class="empty">No kits yet. Run your first video →</div>'; return; }
  el.innerHTML = kits.map(k =>
    `<div class="kit-item ${current===k.name?'active':''}" onclick="openKit('${k.name}')">${k.name}
     <div class="d">${new Date(k.mtime*1000).toLocaleString()}</div></div>`).join('');
  if (!keepSel && !current && kits.length) openKit(kits[0].name);
}

async function openKit(name) {
  current = name;
  const kit = kits.find(k => k.name === name);
  const view = document.getElementById('kitview');
  view.innerHTML = '<div class="empty">Loading…</div>';
  let html = '';
  if (kit.clips.length) {
    html += `<div class="card"><div class="head"><h3>Clips</h3></div><div class="clips">` +
      kit.clips.map(c => `<div><video src="/clip?kit=${encodeURIComponent(name)}&name=${encodeURIComponent(c)}" controls></video></div>`).join('') + `</div></div>`;
  }
  for (const f of kit.files) {
    if (kit.clips.includes(f)) continue;
    const r = await fetch(`/api/file?kit=${encodeURIComponent(name)}&name=${encodeURIComponent(f)}`);
    if (!r.ok) continue;
    const { content } = await r.json();
    const label = f.replace(/[_.]/g, ' ').replace(/ (md|txt|sh|json)$/, '');
    const prompterBtn = f === 'script.md'
      ? `<button class="copy" onclick="openPrompter(this.closest('.card').querySelector('.body').innerText)">Teleprompter</button>` : '';
    html += `<div class="card"><div class="head"><h3>${label}</h3><div style="display:flex;gap:8px">${prompterBtn}
      <button class="copy" onclick="copyText(this)">Copy</button></div></div>
      <div class="body">${content.replace(/&/g,'&amp;').replace(/</g,'&lt;')}</div></div>`;
  }
  view.innerHTML = html || '<div class="empty">Empty kit.</div>';
  loadKits(true);
}

function copyText(btn) {
  navigator.clipboard.writeText(btn.closest('.card').querySelector('.body').innerText);
  btn.textContent = 'Copied ✓'; setTimeout(() => btn.textContent = 'Copy', 1500);
}

async function run() {
  const source = document.getElementById('source').value;
  const model = document.getElementById('model').value;
  const r = await fetch('/api/run', { method: 'POST', headers: {'Content-Type':'application/json'},
    body: JSON.stringify({ source, model }) });
  const j = await r.json();
  if (!j.ok) { alert(j.message); return; }
  document.getElementById('runbtn').disabled = true;
  const log = document.getElementById('log'); log.style.display = 'block'; log.textContent = 'Starting…';
  polling = setInterval(poll, 1500);
}

async function poll() {
  const s = await (await fetch('/api/status')).json();
  const log = document.getElementById('log');
  log.textContent = s.log || '…'; log.scrollTop = log.scrollHeight;
  if (!s.running) {
    clearInterval(polling);
    document.getElementById('runbtn').disabled = false;
    log.textContent += s.exit_code === 0 ? '\n✓ Done.' : '\n✗ Run ended with an error — read the log above.';
    current = null; loadKits();
  }
}

loadKits();
</script>
</body>
</html>"""


if __name__ == "__main__":
    url = f"http://127.0.0.1:{PORT}"
    try:
        server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    except OSError as e:
        if e.errno == 48 or "in use" in str(e).lower():
            # Already running from an earlier launch — just open the page.
            print(f"Repurpose Studio is already running → {url}")
            webbrowser.open(url)
            raise SystemExit(0)
        raise
    print(f"Repurpose Studio dashboard → {url}   (Ctrl+C to stop)")
    try:
        webbrowser.open(url)
    except Exception:
        pass
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nbye")
