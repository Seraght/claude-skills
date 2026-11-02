# Every score has a source, and the examinee sees where it comes from

The GE25301 practical (2569) had a rubric whose every score could be traced to a descriptor, and an examinee-facing paper that showed only a total per criterion — "C1 … 8" — with a pointer to `05-rubric.md`, a file inside the vault the examinee could not open. Other rubrics the authoring skills accepted awarded a criterion's 8 from descriptors at 8, 4 and 0, leaving the marker to choose a 7 with nothing to choose it by. The rubric rules in `make-exam` and `make-practical` — observable criteria, distinguishable levels, weights that sum — passed both.

We decided two rules, and one exception to the first.

**Every score a criterion can award is traceable**: it is a described level, or it is computed by a stated rule from described parts — a sum of sub-parts that each have a descriptor, or a weight times a described level. Brookhart (2018) tells rubrics, checklists, and rating scales apart by their scale: a rating scale asks for decisions across a scale that does not describe the performance, so an unsourced 7 out of 8 is a rating scale labelled a rubric. The sourced position is an inference from that definition (`docs/research/thesis-critique-and-rubric-standards.md`, section 3), not a rule any source states.

**Where a rating scale is the deliberate choice, it is called one and its points are anchored.** `make-practical` prescribes rating scales for judgement, so a rule that every unsourced score is a defect would condemn what the skill tells the author to build. The defect is the label, not the scale.

**The examinee sees where the marks come from**: any criteria summary the examinee receives gives at least one line per criterion on how its marks are reached, or points to a document the examinee actually receives. Dawson (2017) names a rubric's *scoring strategy* and its *secrecy* among its design elements; totals alone keep the strategy secret.

Both rules sit in the rubric core the two authoring references copy, in the step that builds the rubric, and as defects with their fixes in the two `item-defects` files that carry rubrics, worded alike so a critique of a written item and of a practical task names the same failure the same way.

## Considered Options

- **A range of points inside one described level, chosen by the marker** — rejected: no source read gives a procedure for it, and the score inside the range has no descriptor of its own, which is the rating-scale case.
- **Banning rating scales from rubric files outright** — rejected: `make-practical` deliberately prescribes them for judgement, and an expert marker on an anchored scale is a sound instrument when it is called what it is.
- **Publishing the full rubric to the examinee as the only remedy** — rejected: some institutions keep the marker's copy back, and one line per criterion on how its marks are reached is enough to stop the strategy being secret.
- **Holding only the defect names identical across the two defect files** — rejected: the bodies drifted apart in the first draft, and only one of them kept the rating-scale exception.

## Consequences

- `check.py` holds the rubric core identical across the two authoring references, the two defect entries identical, whole, across the two defect files, and requires the rubric-building step of `make-exam` and `make-practical` to name both rules.
- The GE25301 paper's criteria summary is fixed in the host's own session, before its next sitting.
