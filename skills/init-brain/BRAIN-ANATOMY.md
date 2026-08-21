# Second-Brain Anatomy

Eleven components of a healthy, agent-operated knowledge base, grouped by the four jobs the vault must do: **capture fast, find again, stay trustworthy, don't rot**. Greenfield mode scaffolds each component; audit mode scores each one. A component the user explicitly declines is recorded as declined in the vault's constitution — never silently skipped.

## Capture

**1. Staging inbox** — a low-friction entry point that separates *capturing* from *filing*, so nothing is lost while filing decisions wait.
- Scaffold: a staging folder (default `temp/`), untracked in git, named in the constitution.
- Audit: does a designated inbox exist, and is it named in the constitution?

**2. Role/area trees** — a clear home for each kind of work the user does, so filing is a decision with a right answer.
- Scaffold: one top-level tree per role from the interview (e.g. teaching / research / admin).
- Scaffold: the destination rule *inside* a tree as well — which folder an imported source file lands in, and which folder its digest lands in (default: `sources/` and `digests/` per subject) — written into the constitution as a rule, not merely implied by whichever folders happen to exist. A tree whose internal layout is only visible by example forces every later skill to guess or ask.
- Audit: does every kind of work have an unambiguous destination — and could an agent tell from the constitution alone where a new source file and its digest belong?

## Findability

**3. Indexes at every level** — every file reachable from an index, so both human and agent navigate without scanning the whole vault.
- Scaffold: an `INDEX.md` at the root of each tree, a `README.md` per section, each seeded with the tree's initial structure.
- Scaffold: the registration rule in the constitution — which index a newly filed document is registered in, and that registering is part of filing rather than a later tidy-up. Skills that file documents carry a "register it in the index" step; without the rule written down, each one has to ask.
- Audit: sample files across trees — is each one linked from an index? Does the constitution say where a new document gets registered?

**4. Gap markers** — indexes distinguish *exists* from *planned-but-unwritten*, turning the vault from storage into a worklist.
- Scaffold: a marker convention (e.g. 🔴 not written / 🟢 done) documented in the constitution and used in the seeded indexes.
- Audit: can you tell from an index alone what is still missing?

**5. Retrieval workflow** — the vault is used, not only written to: questions get answers that cite vault files.
- Scaffold: a constitution rule — answers drawn from this vault must cite the vault files they came from.
- Audit: is there any usage-side workflow, or is the vault write-only?

## Trust

**6. Constitution** — the rules an agent needs (destinations, naming, gates, markers) written where it will look, in a file every agent reads.
- Scaffold: a root `AGENTS.md` holding the rules, plus a one-line `CLAUDE.md` beside it that says to read `AGENTS.md` — `AGENTS.md` is the cross-agent name, and the pointer costs one line rather than a second copy that can drift. Mirror the pair in any tree with rules of its own (or keep the tree's rules as a section of the root file).
- Audit: could an agent discover every operating rule without asking the user? An existing vault whose rules live in `CLAUDE.md` alone is *present*, not partial — only propose the split if the user works with more than one agent.
- Audit: is it still a rules file, or has it become a manual? The constitution is loaded before the user types anything and re-sent on every turn afterwards, so length here is a tax on every session in the vault, including the ones that never touch what the long section describes. Flag any section that walks through a task step by step: procedure belongs in a skill, or in a side file the agent opens when it is doing that task. What stays is what an agent must know *before* it can act — destinations, naming, gates, markers, cadence.

**7. Provenance gates** — copyright and privacy policy written down, so what enters the vault is defensible.
- Scaffold: a policy section in the constitution from the interview: what may be stored as source files vs digest-only with citation; what personal data must never enter.
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
- Scaffold: an `archive/` convention per tree and a review cadence (what to check, how often) recorded in the constitution.
- Audit: does an archive exist? Is anything visibly stale still sitting in active trees?
