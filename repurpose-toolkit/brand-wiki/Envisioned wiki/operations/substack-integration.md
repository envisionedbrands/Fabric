---
title: Substack Integration — Scheduling & Publishing Options
category: operations
confidence: high
sources:
  - memory/substack-integration.md (research, April 2026)
last_updated: 2026-04-19
---

# Substack Integration — Scheduling & Publishing Options

> Research findings on scheduling/publishing to Substack programmatically. As of April 2026: native scheduling exists with limits, no official write API, unofficial `python-substack` library works.

---

## Current State (April 2026)

### Native Scheduling — YES (with limits)

- **Long-form posts:** web dashboard supports scheduling up to **3 months out**. Sends email + publishes simultaneously.
- **Notes:** scheduling shipped early 2026 — web, iOS, Android.
- **Solves scheduling if she's willing to paste manually.**

### Official API — READ-ONLY

- "Substack Developer API" (updated Apr 3, 2026) exposes only public profile data via LinkedIn lookup.
- No post creation / scheduling / publishing endpoints. No announcements suggest this is changing.

### Unofficial API — WORKS, MAINTAINED

- **`ma2za/python-substack`** (PyPI, v0.1.21, Mar 25 2026) — draft creation, publish, cookie/email+password auth. **Includes a FastMCP server** that Claude can call directly.
- **`JPres-Projects/Substack-API`** — Python client + CLI, multi-account support.
- **Caveat:** Substack can break this any time, likely ToS gray-area.

---

## Tools That Do NOT Publish to Substack (Skip)

- Zapier, Make, Buffer, Publer, Hootsuite — all outbound-only for Substack
- GHL — no Substack connector

---

## Recommended Approach for Maria-Ines

Build a **Claude → Substack draft MCP** using `python-substack` + FastMCP. Pipeline-integrated flow:

1. Approved content hits `02-CONTENT/ready-to-publish/`
2. MCP call: `substack.create_draft(title, subtitle, body_md, cover_image, scheduled_for)`
3. Draft lands in Substack queue (immediate or scheduled ≤ 3 months)
4. **Manual final review in Substack web UI before send** — unofficial API risk warrants human-in-loop

**Effort:** ~1 focused afternoon (4–8 hours total)
- MVP draft creation: 2–4h
- Full MCP integration: 4–6h
- Pipeline hookup: +2h

**Maintenance:** refresh cookies every few weeks, patch when Substack changes internals (2–4× per year).

---

## How to Apply

When Maria-Ines asks about Substack publishing/scheduling in a future session:

- **Scheduling natively:** tell her yes, web dashboard, 3-month cap
- **Programmatic:** recommend the python-substack + FastMCP path, ~1 afternoon build
- **Bridge for NOW (pre-build):** draft in Claude → she copy-pastes to Substack web, uses native scheduling

---

## Sources

- support.substack.com/hc/en-us/articles/360037870412 (native scheduling)
- on.substack.com/p/new-on-substack-post-templates-notes (Notes scheduling)
- github.com/ma2za/python-substack (unofficial library with FastMCP)
- support.substack.com/hc/en-us/articles/45099095296916 (read-only official API)

---

## See Also

- [[../strategy/substack-paid-strategy|substack-paid-strategy]] — The 4-phase paid subscriber roadmap
- [[../content/platform-substack|platform-substack]] — Substack platform playbook (Notes, posting cadence)
- [[content-output-standards]] — HTML / SEO / GEO requirements for Substack articles
