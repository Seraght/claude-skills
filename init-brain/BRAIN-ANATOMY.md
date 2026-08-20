# Second-Brain Anatomy

Eleven components of a healthy, agent-operated knowledge base, grouped by the four jobs the vault must do: **capture fast, find again, stay trustworthy, don't rot**. Greenfield mode scaffolds each component; audit mode scores each one. A component the user explicitly declines is recorded as declined in the vault's `CLAUDE.md` — never silently skipped.

## Capture

**1. Staging inbox** — a low-friction entry point that separates *capturing* from *filing*, so nothing is lost while filing decisions wait.
- Scaffold: a staging folder (default `temp/`), untracked in git, named in `CLAUDE.md`.
- Audit: does a designated inbox exist, and is it named in the constitution?

**2. Role/area trees** — a clear home for each kind of work the user does, so filing is a decision with a right answer.
- Scaffold: one top-level tree per role from the interview (e.g. teaching / research / admin).
- Audit: does every kind of work the user does have an unambiguous destination?

## Findability

**3. Indexes at every level** — every file reachable from an index, so both human and agent navigate without scanning the whole vault.
- Scaffold: an `INDEX.md` at the root of each tree, a `README.md` per section, each seeded with the tree's initial structure.
- Audit: sample files across trees — is each one linked from an index?

**4. Gap markers** — indexes distinguish *exists* from *planned-but-unwritten*, turning the vault from storage into a worklist.
- Scaffold: a marker convention (e.g. 🔴 not written / 🟢 done) documented in `CLAUDE.md` and used in the seeded indexes.
- Audit: can you tell from an index alone what is still missing?

**5. Retrieval workflow** — the vault is used, not only written to: questions get answers that cite vault files.
- Scaffold: a `CLAUDE.md` rule — answers drawn from this vault must cite the vault files they came from.
- Audit: is there any usage-side workflow, or is the vault write-only?

## Trust

**6. Constitution** — the rules an agent needs (destinations, naming, gates, markers) written where it will look: `CLAUDE.md` per scope.
- Scaffold: a root `CLAUDE.md`, plus a per-tree `CLAUDE.md` (or section) for any tree with rules of its own.
- Audit: could an agent discover every operating rule without asking the user?

**7. Provenance gates** — copyright and privacy policy written down, so what enters the vault is defensible.
- Scaffold: a policy section in `CLAUDE.md` from the interview: what may be stored as source files vs digest-only with citation; what personal data must never enter.
- Audit: do written gates exist for both copyright and PII?

**8. Templates** — repeated document types produce uniform output.
- Scaffold: `_templates/` with at least a digest template; more as the interview reveals repeated outputs.
- Audit: do the vault's repeated document types have templates?

**9. Automated verification** — link and status integrity is checked by machine, not trust.
- Scaffold: a minimal broken-link checker in the user's shell (scan `*.md` for relative links, report targets that don't exist — keep it small), placed in `_scripts/`; wired into a pre-commit hook if the vault uses git.
- Audit: does a check script exist, and does it currently pass?

## Maintenance

**10. Shared knowledge layer** — reusable general knowledge lives once, separate from instance data, so updating it is a one-place edit.
- Scaffold: a `_shared/` folder with a README stating what belongs there (general reference) and what does not (instance-specific data).
- Audit: is the same general reference duplicated across instances?

**11. Review & archive cadence** — dead items leave the active trees, so what remains is alive; the vault is revisited on a rhythm, not only when something breaks.
- Scaffold: an `archive/` convention per tree and a review cadence (what to check, how often) recorded in `CLAUDE.md`.
- Audit: does an archive exist? Is anything visibly stale still sitting in active trees?
