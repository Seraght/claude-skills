# Options are laid out by rendered width

Two 2569 finals went out as Word files, and on both the user had to send the paper back for its option layout. On the mathematics final the first build knew only two layouts — all four options on one line, or one per line — and two per line was added after the user asked for it, its threshold tuned by trial from 26 characters to 34. On the GE 25301 final the build had all three layouts, under thresholds the run set for itself: at most 12 characters for one line, at most 26 for two per line. Applied to the 45 items of the paper as finally set, that rule put 17 items on four lines that two per line held, and 5 on two lines that one line held. The rebuild the user accepted measured each option's rendered width in TH Sarabun at 16 pt against the columns of the form: 2113 twips each with four to a line, 4279 with two, from an option indent of 1021 on an A4 page with 1134 margins.

The mechanism is the unit. Thai marks above and below a letter — `ไม่`, `ใช้`, `ผู้` — are characters to a count and take no width on the line, so a character threshold reads Thai options as wider than they print. No skill said how options are set out, so each run invented its threshold, which is the failure [ADR 0018](0018-a-threshold-the-skill-does-not-give-is-one-the-agent-invents.md) names. The builds lived in an exam set's `_build/` and in a session's scratch space, so the next paper could not find the last one's widths.

We decided four things.

**The rule is fit by rendered width.** Each item takes the most options per line that leave every option, with its letter, on one line inside its column, the columns dividing the line equally from the option indent. An institution's form that fixes the layout governs.

**The rule is shape, and lives in `assessment-layout`.** `make-exam`, `adopt-pool`, and `critique-mcq` all produce or change the paper, so by [ADR 0007](0007-shape-is-shared-process-is-copied.md) it lives once and they point to it.

**The skill gives the rule; the vault's one paper builder gives the numbers.** The column widths and the gap depend on the vault's form, so they belong in a script the vault keeps for every subject, in its scripts folder. Where the vault has no form, the widths are put to the user before that script is written.

**The page confirms it in both directions.** An option wrapping inside its column fails, and so does an item set on more lines than it needs — the second is the defect the user kept catching. It is read in the pass the `thai-office-files` check already makes, so the page images are opened once.

## Considered Options

- **A character threshold in the skill** — rejected: the unit is what failed.
- **Numeric widths in the skill** — rejected: they belong to one institution's form, margins, and font size.
- **The rule in `make-exam` alone** — rejected: two other skills rebuild the paper, and copies drift.
- **The rule in `thai-office-files`** — rejected: that skill holds tested Thai rendering rules; option layout is the paper's shape, whatever its language.
- **Ask the user per item** — rejected: forty-five to sixty decisions that a measurement settles.

## Consequences

- `assessment-layout` gains *Options on the printed paper*; its description names it.
- `make-exam` step 12 assembles the paper only once its options pass that check; `adopt-pool` step 8 and `critique-mcq` step 12 point to it.
- `_scripts/check.py` keeps `two per line` inside `assessment-layout`.
- The vault's paper builder is to be merged into one script under its scripts folder — vault work, outside this repo.
