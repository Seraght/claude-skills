# Item Statistics Reference

The formulas, thresholds, and diagnostic tables a post-examination analysis is read from. **The defects themselves are not here** — a statistic points back at the item, and what is wrong with the item is in the `item-defects` skill.

Where the host project or the institution fixes its own thresholds or its own reporting form, those govern and this file fills the gaps they leave.

**Every threshold below is a convention, not a finding.** The bands are widely used and none of them come from a standards body: *Standards for Educational and Psychological Testing* (AERA/APA/NCME, 2014) requires that reliability evidence be reported with the conditions of use, and sets no universal minimum. A report that hides which convention it applied cannot be argued with later, so name the thresholds in the report and use one set throughout.

## Difficulty

The proportion of examinees answering correctly, correct divided by the number who sat it. It measures *ease*: a high value is an easy item.

| Difficulty | Reading |
|---|---|
| Above 0.90 | Almost nobody misses it. Legitimate for content everyone must hold, at roughly one item in eight; beyond that the paper spends marks without separating anyone |
| 0.70 – 0.90 | Easy and useful, especially early in a paper |
| **0.40 – 0.70** | **Where an item separates examinees best** — most of the paper belongs here |
| 0.30 – 0.40 | Hard, and fine while discrimination holds |
| Below 0.30 | Go back and read the item: check the key, check the stem for ambiguity, check that the topic was taught |
| Below the guessing rate — under 0.25 on four options | Something is wrong. Usually the key, or a distractor more defensible than the key |

An item's variance is the difficulty multiplied by one minus itself, which peaks at 0.50 — an item everyone gets right, or everyone gets wrong, separates nobody at all. A paper's useful average sits midway between guessing and certainty: about 0.63 on four options, 0.67 on three.

**This reverses where the paper was scored against a standard everyone was expected to reach.** There a high value is the teaching having worked, not a defect. Which kind of paper it is has to have been settled when the blueprint was drawn, not decided once the marks are in and one answer is convenient.

## Discrimination

Whether examinees who did well overall did better on this item. Two forms are in use: the difference in success between the top and bottom groups, and the correlation between getting the item right and the total score. The correlation is the better instrument, since it uses everybody rather than the extremes. The bands below are applied to both by convention, though they were set for the group-difference form and borrowed for the correlation.

| Value | Reading |
|---|---|
| 0.40 and above | Strong; bank it |
| 0.30 – 0.39 | Good |
| 0.20 – 0.29 | Marginal; read the item again |
| 0.00 – 0.19 | Weak — ask whether this item measures something the rest of the paper does not |
| Negative | The stronger examinees did worse. Check the key **first**; this is where a wrong key surfaces |

**Discrimination is capped by difficulty, arithmetically.** An item nearly everyone answers correctly cannot discriminate, however well written it is:

| Difficulty | Highest discrimination possible |
|---|---|
| 0.50 | 1.00 |
| 0.70 or 0.30 | 0.60 |
| 0.90 or 0.10 | 0.20 |
| 0.95 or 0.05 | 0.10 |

An item at 0.95 will never exceed 0.10, and cutting it for that is cutting it for being the item it was written to be. **Never judge discrimination without the difficulty beside it.**

## Options

Run this only on items the two measures above flagged. For each option: how many chose it, and how those who chose it scored overall.

A distractor is not working when almost nobody takes it — under about 5% — or when it correlates positively with the total score. In a study of 514 items and 1,542 distractors, only 52% were working, 10% were chosen by nobody at all, and just 14% of items had all three distractors working. Items with more working distractors discriminated better, and items with none were significantly easier. **A four-option item with two dead distractors is a two-option item**, with a one-in-two guess rather than one in four — which is the case for writing three options that all draw takers instead of four where one is furniture.

| Pattern | Reading | Action |
|---|---|---|
| A distractor takes under 5%, or none at all | Implausible enough that nobody was tempted; the item is easier than it looks | Rewrite it from a misconception examinees actually hold, or drop to three options |
| A distractor is taken more by strong examinees than weak ones | There is a defensible reading of it, or the stem is ambiguous enough that careful examinees go elsewhere | Check the content now. If it is defensible, accept both answers or void the item |
| A distractor outdraws the key | The key is wrong, or the cohort was taught it wrong | Check the key. If it stands, this is a teaching finding, not an item defect |
| Every option draws about equally in both groups | Everyone guessed — too hard, or not taught | Check against the blueprint that the topic was actually covered |
| Unusually many left it blank, especially late in the paper | They ran out of time | Statistics for items near the end cannot be interpreted; what to revisit is the item count against the duration |

## Reliability and the standard error

Internal-consistency reliability for right or wrong items, on a scale of zero to one.

| Value | Fit for |
|---|---|
| 0.90 and above | Licensure, and other decisions that fall heavily on one person |
| 0.80 – 0.89 | A final paper carrying much of a grade |
| **0.70 – 0.79** | **An ordinary classroom paper — acceptable** |
| 0.60 – 0.69 | A quiz, read alongside other evidence |
| Below 0.60 | Not sound enough to decide anything about an individual |

**A high coefficient is not evidence the paper measures one thing.** It is unrelated to the paper's internal structure: two clearly different topics produce a high value whenever they correlate with each other. It also rises with length on its own, so a short, excellent paper can score under 0.70 — and a value above 0.95 usually means the paper asks the same thing repeatedly, buying consistency with coverage.

When it comes out low, look for items with weak or negative discrimination, check whether the paper is simply short, and check whether the marks are bunched. **Do not delete items to raise it**: that produces a repetitive paper and spends the blueprint's coverage to buy a number.

The **standard error of measurement** is what says how precise one person's mark is, and it is the figure to use whenever a mark decides something. Where the paper carries a pass mark, the band of one standard error either side of the cut holds the examinees whose marks cannot be told apart from it. For those examinees: look at other evidence, re-check the marking of their papers by hand, and **fix the rule in advance and apply it to everyone**, before any names are visible.

The standard error is a reason to **look for more evidence, not to move the cut**. Whatever argument raises the examinees a hair below is equally an argument about the ones a hair above; the honest fix is to set the cut by a standard-setting method when the paper is designed.

## Cohorts of thirty to sixty — the step that is never skipped

Every threshold above was developed on cohorts in the hundreds. On a class-sized group the values swing far enough to reverse a decision, so each is reported with its interval, and a value near a boundary is reported as near a boundary rather than as the category it happened to land in.

The evidence is direct. The same 32 items were given to 22 cohorts of 10–15 examinees: **91% of the items were classified both "poor" and "excellent"** by the same discrimination bands in different cohorts, 59% appeared in all five bands, and one fixed difficulty rule cut anywhere from 1 to 22 items depending only on which cohort sat it. Same items, same content — the difference is which people turned up. A later simulation found the proportion cut rises as the cohort shrinks, to the point of doing more harm than good.

Difficulty has a standard error of the square root of the difficulty times one minus itself, divided by the number who sat it. The 95% interval is about twice that either side:

| Examinees | At difficulty 0.50 | At difficulty 0.80 |
|---|---|---|
| 30 | ± 0.18 | ± 0.14 |
| 40 | ± 0.16 | ± 0.12 |
| 50 | ± 0.14 | ± 0.11 |
| 60 | ± 0.13 | ± 0.10 |
| 100 | ± 0.10 | ± 0.08 |
| 200 | ± 0.07 | ± 0.06 |

A class of 40 measuring 0.50 has a true value somewhere between 0.35 and 0.65 — spanning hard through easy entirely.

Discrimination is worse, because the group-difference form uses only the top and bottom 27%: about 11 examinees each way in a class of 40, where **one examinee answering differently moves the value by 0.09** against bands that are 0.10 wide. One person can move an item a whole category.

None of this makes the statistics useless. It means one cohort is not enough to retire an item, that the numbers are read alongside whether the item covers something the paper needs, and that an item is retired on a pattern across cohorts rather than on a single run.

## Sources

- AERA, APA & NCME, *Standards for Educational and Psychological Testing* (2014) — reliability evidence is reported with the conditions of use; no universal minimum is set.
- Tarrant, Ware & Mohammed (2009) on non-functioning distractors across 514 items, using the under-5% definition from Haladyna & Downing (1993).
- Sijtsma (2009), *Psychometrika* — coefficient alpha is unrelated to the test's internal structure, and single-administration statistics say little about the accuracy of an individual's score.
- Young, Cummings & St-Onge (2017), *Perspectives on Medical Education* — the same 32 items across 22 small cohorts, and the classification instability that follows.
- Aubin et al. (2020), *Academic Medicine* — Monte Carlo simulation of item removal as cohort size falls.
- Ebel & Frisbie for the discrimination bands, borrowed by convention for the correlation form; Kuder & Richardson (1937) for the reliability coefficient used on right or wrong items.
