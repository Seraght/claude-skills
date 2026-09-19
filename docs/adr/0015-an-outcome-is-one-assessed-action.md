# An outcome is one assessed action, and its check is a table

A course's outcomes were checked by `design-course` against `learning-outcomes` and passed with a paragraph of ticks. Three defects were in them. Two outcomes carried two verbs each — *converse and present*, *analyse and identify the main idea* — and one used *produce*, a Create verb, under a programme outcome the course only introduces. The host project's own rules would have caught all three: it holds one verb per outcome, and it holds that a course introducing an outcome should not write Evaluate or Create verbs for it. Nothing in the skills sent the agent to those rules, and nothing in the skills would have caught the defects without them.

Three mechanisms produced this, and each has its own fix.

**The compound rule counted levels, not actions.** It described a compound outcome as two verbs "usually at two different cognitive levels". *Converse* and *present* are both Apply, so the run read the pair as one level and passed it. What makes an outcome compound is not a gap between levels. It is that one outcome's marks are paying for two separately scored performances. The rule now counts **assessed actions** and decides them with a **deletion test**: delete the phrase, and see whether a rubric criterion or a block of marks has to go with it. The test also settles the two cases a surface rule gets wrong. A channel phrase ("through conversation and presentation") is a condition, because deleting it changes only the task. A method phrase ("by researching the topic") is a condition only while nothing scores it, because it names something the learner does rather than something supplied.

**Level against the map was nobody's step.** The skill checked each verb for failure and each outcome for an upward mapping, but never compared the two levels. The comparison now exists with **no threshold in the skill**. Curriculum maps use introduce/reinforce/master, one-to-three weights, or filled and hollow marks, and a rule like "introduce excludes levels 5–6" means nothing under the second. The host project's own vault states that rule without a source, so by [ADR 0013](0013-true-everywhere-or-true-here.md) it is true here, not everywhere. The skill carries the comparison and the **intentional exception**, which is true everywhere: an outcome kept above its map level passes only with evidence that teaching and assessment reach it, its cost, its fallback verb, and who confirmed it.

**The host project's standard was never looked for.** `design-course` step 1 looked for layout, naming, templates, language, and form. `make-exam` step 1 already looks for "whether the project carries its own assessment reference", and the outcome skills had no counterpart. Both outcome skills now name what they look for and where it usually sits, and the check table records which files governed, so a check made without them is visible.

**The check is a table.** [ADR 0008](0008-a-check-that-leaves-no-evidence-did-not-run.md) and [ADR 0012](0012-a-verdict-is-not-evidence.md) already settled that a verdict is not a check. The outcome check was the remaining place where a verdict was the whole output. It is now one row per outcome, with each cell quoting the outcome or citing a line, and a result that is pass, fail, or exception.

## Considered Options

- **Count levels, as before, and add "or the same level" to the example list.** Rejected: it keeps counting words. A rule based on the surface of the text flags every *and*, including channel phrases that the deletion test correctly passes, and it still has no way to decide a method phrase.
- **Carry the host project's threshold in the skill.** Rejected under ADR 0013, and by `check.py`'s ban on institution markers. It would be wrong the moment the skill ran on a map that is not introduce/reinforce/master.
- **Make the level rule a hard fail.** Rejected. The case that prompted this is an open project where learners choose their topic and tools. It is taught over the course's largest block of hours and marked with a product rubric. Lowering the verb to Apply would make the outcome claim less than the course teaches and assesses. That is the inflated defect in reverse, and the skills have no name for it.
- **Leave discovery to the host project's signposts.** Rejected as the only fix. A signpost helps only an agent that is already looking. The vault this came from now has one as well, and the two are meant to work together.

## Consequences

- `learning-outcomes` gains two sections, *The level the programme assigns* and *The check table*, and its set checklist gains the level comparison.
- `design-course` step 4 is done only when the table is written into the outcomes file. Step 9 confirms that it is there.
- Outcomes that passed before can now fail. The version moves to 0.10.0, not a patch.
- The affective and psychomotor columns in the table defer to the host project's taxonomy. The skill does not yet carry one. That waits on primary-source research in the host vault.
