---
status: NEEDS_INVESTIGATION
flagged_on: 2026-05-18
flagged_by: SOP audit Phase 2B (see 00-STRATEGY/sop-audit/)
canonical_location: /Volumes/Maria-Ines New SSD T7/maria-ines/envisioned-os-april-2026/02-CONTENT/Obsidian Envisioned Content DB/Envisioned wiki/
---

# ⚠️ NEEDS INVESTIGATION — do not edit until reconciled

This `wiki/` folder (lowercase) sits side-by-side with `../Envisioned wiki/` (the canonical one CLAUDE.md points to). They are different wikis, not a symlink. 21 files differ between them. Both were edited recently (this one as recently as 2026-04-30; canonical is being actively maintained).

This wasn't part of the 2026-05-18 wiki reconciliation because the audit focused on the `Obsidian Envisioned Content DB 26/` split, which is now resolved. This fourth wiki copy surfaced at the end of that session and was left for a future cleanup pass.

## What to do (next session)

1. Diff `wiki/` (this folder) vs `../Envisioned wiki/` (canonical) the same way Phase 2B did — file-by-file, pick winners by date + content, merge.
2. After merge: mark this folder DEPRECATED and remove from any tool that references it (Obsidian, etc.).
3. Update MEMORY.md to confirm the canonical path is `Envisioned wiki/` (with the space and the "Envisioned" prefix) — MEMORY.md previously pointed here.

## Do NOT do

- Do not edit any files in this folder until reconciliation is complete. Edits here will diverge from canonical.
- Do not delete or rename this folder before merge — content might be unique to here.
- Do not assume the file dates alone tell the truth (the Phase 2B audit found cases where older files were the right ones to keep).
