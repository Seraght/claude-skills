---
name: init-brain
description: Interview, then scaffold a new knowledge base — folder trees, AGENTS.md, indexes, templates, check script.
disable-model-invocation: true
---

# init-brain — scaffold a knowledge base

This skill is an ordered checklist: each step opens when the one before it has produced its result. It is the setup-time counterpart of the other skills in this set — they *discover* a vault's conventions at runtime, and this skill *creates* the conventions they discover. Scoring a vault that already has content is `audit-brain`, not this skill.

The component reference is the `brain-anatomy` skill — read it before step 2.

## Steps

1. **Confirm the target is a greenfield** — inspect the target directory. Effectively empty (no agent instructions file — `AGENTS.md` or `CLAUDE.md` — and no content trees) is what this skill builds on. Existing content belongs to `audit-brain`; say so and stop. Confirm with the user before proceeding.
2. **Interview the variable parts only** — the anatomy carries opinionated defaults; ask only what varies per vault, present the default alongside each question, and let the user override any of them:
   - Which roles/areas of work need their own tree? (e.g. teaching / research / admin)
   - Where each kind of file lands *inside* a tree — are imported source files and their digests
     separate folders (default: `sources/` and `digests/` per subject) or filed together? The other
     skills cannot file anything without this answer, so settle it here rather than at first use.
   - Vault language — the language of the generated `AGENTS.md`, indexes, and templates.
   - Assessment — does this vault hold exam papers? If not, skip this and record nothing. If it
     does, where they hang and how their files are staged (default `<subject>/assessment/<year>/<exam>/`
     with the item bank at `<subject>/assessment/bank/`, and files numbered by lifecycle stage:
     `0x` authoring, `1x` review before use, `2x` after administration), and that per-person data —
     names, identifiers, individual scores — stays out of the vault while item-level statistics come in.
     Record the answer in `AGENTS.md` alongside the other destinations, since the assessment skills
     read it there rather than asking again.
   - Copyright policy — what may be stored as source files vs digest-only with citation.
   - Privacy red lines — what personal data must never enter the vault.
   - Staging folder name (default `temp/`, untracked).
   - Naming convention (default lowercase, hyphen-separated, with issuing org and year).
   - Shell for the check script (PowerShell or bash).
   - Git? If yes, offer a pre-commit hook that runs the check script.
3. **Scaffold every component** — walk the `brain-anatomy` skill top to bottom and create each component's scaffold with the interview answers filled in. Record any component the user declines as declined in the generated `AGENTS.md`.
4. **Verify before finishing** — run the project's check script where one exists, then confirm: the vault is *discoverable* — every operating rule an agent needs (destinations, gates, naming, markers, cadence) is written in `AGENTS.md`, and every folder is reachable from an index. The bar: the `digest` skill's discovery step could run here without asking the user anything the interview already answered — walk that step literally, question by question, and treat any question the constitution cannot answer as an unfinished scaffold rather than a detail to settle on first use.
