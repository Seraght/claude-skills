# claude-skills

## Agent skills

### Issue tracker

Issues live in GitHub Issues for `Seraght/claude-skills`, worked with the `gh` CLI. See `docs/agents/issue-tracker.md`.

### Triage labels

The five default triage labels, each string equal to its role name. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: the glossary is `CONTEXT.md` at the root, and ADRs are in `docs/adr/`. See `docs/agents/domain.md`.

## Working in this repo

- **Open the PR, then hand the merge to the user.** The auto-mode classifier refuses a self-merge here as "Merge Without Review", even after a `reviewer` pass. Put the review summary in the PR body, wait for the `check.py` job (branch protection requires it), and give the user the link. Merge only when the user says to. Allowing self-merge with a permission rule is the user's call; do not change settings to get around it.
- **Prove a new `check.py` rule fires.** Insert a real violation, confirm the run FAILs, then revert. A rule never seen to fail may be matching nothing.
- **Test a skill by walking the next skill's first step literally.** Checking that files exist misses defects in the handoff. For example, a greenfield `init-brain` test scaffolded every component but left questions `digest` opens with unanswered. Those questions only surfaced when `digest`'s discovery step was walked against the output.
- **Measure always-on cost with `claude plugin details`.** It reports the per-turn description cost ADR 0006 was written without. Model-invoked skills cost about twice what user-invoked ones do.
