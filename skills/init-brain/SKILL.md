---
name: init-brain
description: Scaffold a new second-brain knowledge base, or audit an existing one against an 11-component anatomy — interview the user, then generate the folder skeleton, AGENTS.md constitution, indexes, templates, and check script that the other skills in this set discover at runtime. Use when the user wants to start a new knowledge base (สร้าง second brain, เปิดคลังใหม่), or asks to health-check an existing vault (ตรวจสุขภาพคลัง).
---

# init-brain — scaffold or audit a second-brain

This skill is an ordered checklist — do not skip steps. It is the setup-time counterpart of the other skills in this set: they *discover* a vault's conventions at runtime; this skill *creates* (or health-checks) the conventions they discover. The component reference is [BRAIN-ANATOMY.md](./BRAIN-ANATOMY.md) — read it before proceeding past step 1.

## Steps

1. **Choose the mode** — inspect the target directory. Effectively empty (no agent instructions file — `AGENTS.md` or `CLAUDE.md` — and no content trees) → **Greenfield**. Existing content → **Audit**. Confirm the chosen mode with the user before proceeding.

## Greenfield: interview → scaffold → verify

2. **Interview the variable parts only** — the anatomy carries opinionated defaults; ask only what varies per vault, present the default alongside each question, and let the user override any of them:
   - Which roles/areas of work need their own tree? (e.g. teaching / research / admin)
   - Vault language — the language of the generated `AGENTS.md`, indexes, and templates.
   - Copyright policy — what may be stored as source files vs digest-only with citation.
   - Privacy red lines — what personal data must never enter the vault.
   - Staging folder name (default `temp/`, untracked).
   - Naming convention (default lowercase, hyphen-separated, with issuing org and year).
   - Shell for the check script (PowerShell or bash).
   - Git? If yes, offer a pre-commit hook that runs the check script.
3. **Scaffold every component** — walk [BRAIN-ANATOMY.md](./BRAIN-ANATOMY.md) top to bottom and create each component's scaffold with the interview answers filled in. Record any component the user declines as declined in the generated `AGENTS.md`.
4. **Verify before finishing** — run the generated check script on the fresh vault, then confirm the vault is *discoverable*: every operating rule an agent needs (destinations, gates, naming, markers, cadence) is written in `AGENTS.md`, and every folder is reachable from an index. The bar: the `digest` skill's discovery step could run here without asking the user anything the interview already answered.

## Audit: score → report → fix on approval

5. **Score all 11 components** — walk [BRAIN-ANATOMY.md](./BRAIN-ANATOMY.md) against the existing vault and mark each component **present / partial / missing**, citing a file path (or its absence) as evidence. Every component accounted for — no skips.
6. **Record the scorecard, then report before touching anything** — write the scorecard to a dated file in the vault (default `docs/brain-audit-<YYYY-MM-DD>.md`; follow the vault's own docs convention if it has one), then present it with a concrete proposal per gap and wait: change nothing else until the user picks which fixes to apply.
7. **Apply approved fixes and verify** — implement only what was approved, then run the vault's check script (or, if it has none, the discoverability check from step 4) over the changed parts. Close the loop in the scorecard file: mark each gap as fixed or declined, so the next audit starts from what was already decided rather than re-proposing it.
