# A proposal is a branch of the thesis critique, and a finding says what to change

`critique-thesis` was run on a research proposal — chapters 1–3, 24 pages, critiqued on 2569-10-29 — with checks built for a finished book. Group A had nothing to recompute, and the findings that mattered were about the design: a sample that had already studied what the intervention teaches, a sample size with no method behind it, interpretation bands that did not fit the instrument's item count, hypotheses the sample could not test, objectives with no analysis method, and a chain from objective to analysis plan that broke along the way. None of these had a check to run.

We decided three things.

**A proposal run is a branch of the same checklist**, for the reason [ADR 0025](0025-a-thesis-critique-is-a-checklist-and-its-text-is-markdown.md) gave the revision run: the same book, earlier, read with the same checks. Step 2 tells it apart by the book itself — no results chapter — rather than by what the user calls it. Group A, and each check that reads results, records *cannot apply: no results yet*, so the evidence table still shows every check. When the full thesis arrives, its proposal's critique is the earlier critique of a revision run.

**Group F holds the proposal's design checks, and only the ones a real proposal failed.** The research for this change (`docs/research/thesis-critique-and-rubric-standards.md`) lists further candidates from the reporting standards; they wait until a critique finds the defect, as every other check in the file did. The sample-size check entered through the proposal's own finding, and cites the standards that ask for it. Group F also runs on a finished thesis, whose methods chapter makes the same commitments.

**The report puts a table of what to change after the summary, and each finding under *evidence / effect / change to*.** Every examiner form read leads with the verdict in the institution's outcome words; Bristol's regulations require a rationale beside it and merged guidance that names the parts to improve; Holbrook et al. found that a comment without a direction is the one a student sets aside. The table replaces the closing list of what to submit, which carried the same rows at the end, where the students found them last.

## Considered Options

- **A separate `critique-proposal` skill** — rejected: it would copy every check in groups B to E, and the two copies would drift ([ADR 0006](0006-how-a-skill-is-reached-and-when-it-is-split.md) splits by how a skill is reached, and both are reached by a book arriving).
- **Adding every research candidate to group F** — rejected: the file's promise is that each check once found a real defect; a check from a standard alone is a style preference until a book fails it.
- **Keeping the list of what to submit at the end** — rejected: the students act on it first, and it repeated the findings without their codes.

## Consequences

- `check.py` requires step 2 to name the proposal run, `THESIS-CHECKS.md` to carry group F, and *Reporting* to put the table of what to change after the summary and to name the three sub-heads.
- The host's example critique was written in the old layout; it is updated in the host's own session.
