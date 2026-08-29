# The chain does not end when the paper is used

The `assessment-layout` skill has declared three lifecycle stages since [ADR 0004](0004-stage-the-assessment-set-and-version-its-items.md): authoring, review, and *after administration — item statistics, post-hoc analysis*. Two of them had skills. The third was a row in a table and nothing else, for four ADRs, while [ADR 0011](0011-a-practical-is-a-different-chain.md) closed by naming the one remaining gap as a review pass for practical examinations. That count was short. Nothing performed the last stage either.

A declared stage with nothing behind it is worse than an undeclared one. [ADR 0004](0004-stage-the-assessment-set-and-version-its-items.md) fixed the meaning of a missing stage as *a stage that did not happen*, and a stage nobody can perform is indistinguishable from one nobody got around to.

`analyze-results` fills it. Its reference distils the operative rules out of the 61 KB the vault held — the difficulty and discrimination bands, the arithmetic ceiling discrimination has at each difficulty, the diagnostic table for the options, the reliability bands and what the coefficient does not mean, the standard error at a pass mark, and the intervals for a class-sized cohort — to about 10 KB, per [ADR 0013](0013-true-everywhere-or-true-here.md).

**Three things shape the skill rather than decorate it.**

*It is model-invoked, and its second step is a gate.* Post-examination analysis is asked for in a sentence, not by recalling a command name, which is [ADR 0006](0006-how-a-skill-is-reached-and-when-it-is-split.md)'s test for the model-invoked tier. Against that: it is the only skill here whose input is a list of named people with their marks. The blast radius [ADR 0006](0006-how-a-skill-is-reached-and-when-it-is-split.md) protected `init-brain` from was *writing* — scaffolding a tree unasked. Here it is *reading*, and a gate placed before anything is opened defends reading better than making the skill harder to reach; `digest` already carries a privacy gate and stays model-invoked. So the gate goes at step 2, before the data is located, and it covers intermediate files as well as the report, since a working file inside an exam set is inside the vault.

*Statistics attach to the item version.* [ADR 0004](0004-stage-the-assessment-set-and-version-its-items.md) settled this and the skill is where it finally has a consumer: a value carried across an edit describes a wording nobody answered.

*The cohort-size step cannot be skipped.* This is not a caveat, it is the finding. The same 32 items across 22 small cohorts had 91% of them classified as both poor and excellent by the same bands, and one fixed difficulty rule cut between 1 and 22 items depending only on who sat it. With thirty to sixty examinees — the size every cohort this set was written for actually is — the thresholds do not survive being read as thresholds. The step reports the interval beside every judgement, so that a value near a boundary is reported as near a boundary rather than as the side it happened to fall on.

## Considered Options

- **A reference skill only**, holding the statistics for others to read — rejected: nothing would have read it. The stage's work is an ordered sequence with a gate in it, which is a checklist by this set's own definition.
- **A step on the end of `critique-mcq`** — rejected on [ADR 0011](0011-a-practical-is-a-different-chain.md)'s test. The two share no step: one measures a paper nobody has sat from the text alone, the other computes from responses and cannot start until marking is done. They also differ in what they may open, which is the difference a gate exists for.
- **User-invoked, because of the personal data** — rejected as argued above, and it would have split the tier on a different axis from the one [ADR 0006](0006-how-a-skill-is-reached-and-when-it-is-split.md) uses, leaving two rules for which tier a skill belongs to.
- **Name it `item-analysis`** — rejected: the set names checklists with a verb and references with a noun, and the noun form is also the vault's filename for the knowledge this skill consumes.
- **Include a post-hoc grade-adjustment procedure** — rejected. Deciding what a borderline mark means is a standard-setting decision that belongs before the examination, and the reference says so plainly: the standard error is a reason to look for more evidence, never a reason to move the cut.

## Consequences

- Fourteen skills where there were thirteen. `plugin.json` goes to 0.9.0.
- `assessment-layout` names a default file for `2x` and states which skill fills each stage, so a stage without a performer is visible in the place the stages are declared.
- `_scripts/check.py` gains a fourth ownership rule: the discrimination bands, the reliability coefficient, and the standard error appear only in `analyze-results`. The authoring and review skills may name what a statistic will later reveal — `item-defects` already does, for the distractor nobody picks — but they do not carry the thresholds for reading one.
- The assessment side is now closed end to end: design the course, build the paper, review it before use, review the review, analyse it after. The gap [ADR 0011](0011-a-practical-is-a-different-chain.md) named is still open — nothing reviews a practical examination before it is used.
