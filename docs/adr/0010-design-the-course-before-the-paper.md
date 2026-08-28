# Design the course before the paper

[ADR 0009](0009-alignment-reaches-up-authoring-does-not.md) gave `make-exam` a gate that stops on a malformed learning outcome, and queued the skill that would author outcomes properly in the first place. This is that skill. The gate can only refuse; something has to be able to write.

**Two skills, because authoring and assessing are different work.** `design-course` runs backwards from the outcomes: what the course owes the programme, then the outcomes, then how each is evidenced, then the timetable that gives learners the chance to perform it. `make-exam` runs forwards from an existing design. Neither contains the other, and the second re-checks what the first produced, because a design and its exam are often written months apart by a person who has changed their mind in between.

**The outcome rules get their own home.** *Outcomes come first* had been living in `make-exam`'s private reference since [ADR 0009](0009-alignment-reaches-up-authoring-does-not.md), which was correct while one skill needed it. A second skill needs it now, which is the trigger [ADR 0007](0007-shape-is-shared-process-is-copied.md) names, so it moves to `learning-outcomes` before it has a chance to become two copies at two levels of detail — the failure [ADR 0008](0008-a-check-that-leaves-no-evidence-did-not-run.md) is written from, avoided this time by acting on the rule instead of rediscovering it.

The reference is deliberately not a standard. It records what the frameworks agree on — an observable verb, alignment in two directions, formats that can reach a level — and says plainly that a programme's or a country's own framework governs where one exists. Where the underlying source is weaker than its reputation, the file says so rather than lending it authority it has not got.

**Four named ways a verb fails**, because "write good outcomes" is not checkable and these are: compound, unobservable, ambiguous, inflated. Each has a fix, and the fix for *inflated* explicitly excludes the move that is always available and always wrong — reading the verb loosely so the paper already written qualifies.

## Considered Options

- **A separate `audit-course` skill** for checking outcomes that already exist, mirroring the `init-brain` / `audit-brain` split in [ADR 0006](0006-how-a-skill-is-reached-and-when-it-is-split.md) — rejected: that invocation is already served. `make-exam` step 3 checks the outcomes it is about to build on, which is when the answer actually matters, and `design-course` step 4 checks the ones it collects. A third skill would be a third place for the same checks to drift.
- **Put outcome design inside `make-exam`** as steps before the blueprint — rejected: it is a different chain, run at a different time of year, and it would give the exam skill the power to rewrite the syllabus it is supposed to be constrained by.
- **Give `design-course` a shared layout reference** for where its artifacts live, as `assessment-layout` does for exam sets — rejected for now under [ADR 0007](0007-shape-is-shared-process-is-copied.md)'s own rule: it is the first skill to write these files, and a first consumer's private default harms nobody. The home gets built when a second skill needs the same shape, which the queued practical-exam skill may well do.
- **Generate the institution's course form directly** (มคอ.3 and its equivalents) — rejected: the form is fixed by an authority and changes on its own schedule. The skill produces the design and the alignment table the form is filled from, which is the part that is actually hard.

## Consequences

- Eleven skills where there were nine. `design-course` is model-invoked, since a user asking for it in their own language must reach it without knowing its name; `learning-outcomes` is reference only.
- `make-exam` no longer carries the outcome rules, only the reach to them. Its private reference is back to being about assessment.
- `_scripts/check.py` gains a fourth literal rule: the outcome vocabulary appears only in `learning-outcomes`.
- One block of work remains queued: **practical-exam design**. `make-exam` keeps practical exams until it ships, per [ADR 0009](0009-alignment-reaches-up-authoring-does-not.md).
- Tested against a real six-outcome course before shipping. The checks found three compound outcomes where one was known and two were not, agreed with a judgement the course's own author had already reached independently about which level a written paper can evidence, and passed the one outcome that looked wrong and is not — an affective outcome correctly assessed by observation rather than by examination.
