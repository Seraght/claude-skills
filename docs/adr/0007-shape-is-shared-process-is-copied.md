# Shape is shared, process is copied — and checked

[ADR 0005](0005-duplication-buys-portability.md) said duplicate; [ADR 0006](0006-how-a-skill-is-reached-and-when-it-is-split.md) said share. Neither said which, so every recurrence was argued from scratch — and the argument was lost twice before anyone noticed, in the discovery clause and again in the closing check. The rule that decides it:

**Process is copied. Shape is shared.**

- **Process** is what one skill does, in its own order. It is copied into every skill that performs it and held byte-identical, so a folder copied on its own still runs. The discovery step and the conditional verify are process.
- **Shape** is the structure of an artifact that several skills read and write. It lives in one reference skill, reached by name. The vault anatomy and the exam-set layout are shape.

The trigger to build the shared home is **the second skill that needs the same shape** — not the first, whose private default harms nobody, and not the third, by which time the copies have already disagreed. `assessment/` reached three skills at three levels of detail before it was caught, which is what that clause is written from.

**A rule that cannot be checked will drift.** Every skill in this set is required to close by running the project's check script; this repo had none of its own, and all three drifts above were found by a person running `grep`. `_scripts/check.py` now asserts the invariants: descriptions inside budget, the copied text identical wherever a step carries it, banned wordings absent, layout literals confined to their reference skill, every skill reached by name existing, every relative link resolving. Each rule is there because that exact thing already broke once.

## Considered Options

- **Always duplicate** — rejected: the exam-set layout proved copies of a structured shape drift silently, and the drift lands in the user's vault as misfiled artifacts rather than as odd prose.
- **Always share through reference skills** — rejected: it spends a permanently loaded description on four-line clauses and breaks the promise that one copied folder runs.
- **Decide case by case, as before** — rejected: that is what produced two silent behavioural splits in a set of six files.
- **A shell check script** (PowerShell, matching the author's machine) — rejected: this script serves contributors to this repo, not the non-technical vault users [ADR 0002](0002-external-tools-are-accelerators-not-prerequisites.md) protects, and the repo is public. Python runs everywhere with no dependency to install.

## Consequences

- New shared knowledge is classified before it is written: process or shape. Getting it wrong is now visible rather than arguable.
- `_scripts/check.py` is the repo's own conditional verify, and every future ADR that constrains the skill files is expected to add a rule to it.
- The next candidate is already visible: `digest`, `new-subject`, and `update-portfolio` all write index rows, and nothing defines what an index row looks like. By this rule that is shape, and it reached its second skill some time ago.
