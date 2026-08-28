# MCQ Critique Reference

The measurements a critique is judged from, and the discipline that keeps it usable. **The defects themselves are not here** — they live in the `item-defects` skill, one file per item format, so that the skill writing items and the skill critiquing them measure against the same taxonomy rather than against two copies of it that drift apart.

When the host project carries its own assessment reference or item-writing rules, that one governs and this file fills the gaps it leaves — a paper whose regulations require a fixed number of options, or a fixed number of negatively worded items, is not flawed for following them.

## Measure before judging

Build this table for each item *before* forming any judgement, and write the findings from the table rather than from an impression of the item:

- **Length of every option**, and which one is the key. Count characters excluding spaces by default; count words only in a language that separates them.
- **Terms appearing in more than one option**, with counts — the input to the convergence check.
- **Words or roots shared between the stem and the key only.**
- **Presence of**: absolute terms, vague frequency terms, "none of the above" and "all of the above", negation in the lead-in, numeric ranges, options that are complete sentences.
- **Whether the options form a collectively exhaustive set** on some dimension.
- **Whether the lead-in is closed** — can the item be answered with the options covered?
- **Which option the key points at, and what is actually in that position.**

This ordering is not ceremony. On this exact task, an LLM applying the same rubric by reading alone detected the longest-key flaw at F1 0.18–0.44, while a script that counted characters reached 0.80–1.00; the same LLM reported 4.2 flaws per item where expert raters using the identical rubric found 1.6, and on some items reported thirteen. Judgement by impression both misses what counting finds and invents what is not there.
### Languages without word spacing

Where the language does not separate words, a word count is not a measurement and several checks need a different marker than their English form. The markers are in the `item-defects` skill, with the taxonomy they belong to.

## Findings discipline

A critique that over-reports is as useless as one that under-reports: the author spends a day on phantom defects and then stops believing the tool.

- **Every finding quotes the span it is about**, from the stem or from a named option **as the rendered paper shows it**, and states the fix. No quote, no finding. Text pulled from a word-processor file is not the paper: what it drops — equations, figures, formatting-carried marks — comes back as a confident report that content is missing, complete with a plausible technical explanation for a defect that does not exist.
- **A measured criterion is reported in full.** Where a check is numeric, list every item that meets it, or give the count and list the worst; naming three of twenty and stopping turns a measurement back into an impression.
- **One rewrite, one finding.** Where a single edit removes several flaws, report it once and name the flaws it resolves.
- **Rank by severity, not by count.** A bank with three real blocks is in worse shape than one with thirty notes.
- **Judge the item against its own outcome.** A Remember-level item is not flawed for being Remember-level unless the blueprint cell it fills calls for something higher.

### Severity

- **Block** — the item cannot be administered as written: the key does not match the option it points at, more than one defensible answer, a keyed answer the course source contradicts, an item that hinges on another item, or a key inferable from the options with the stem covered.
- **Revise** — the item measures something, but a flaw distorts the score: any cue flaw, any irrelevant-difficulty flaw, a level or outcome mismatch.
- **Note** — worth fixing in bulk, with no evidence it moves scores: option ordering, formatting, punctuation.


## Check the fix

Repairs introduce their own flaws, and a critique that stops at the first rewrite hands back a differently broken item. The repairs that create new defects are listed with the defects they follow from, in the `item-defects` skill. Re-run the measurements on any item that was rewritten.

## Provenance

A paper assembled from a larger pool contains items with different histories, and they do not deserve the same treatment:

- **Used unchanged** — carries forward whatever checks it already passed.
- **Edited after selection** — every earlier check is void. Tightening a stem can strip the qualifier that made the key true; reordering options moves the key. Re-measure and re-run all four groups.
- **Written outside the set** — items added by hand to fill a blueprint cell nothing else covered. These have passed nothing, were written last and under time pressure, and are the highest-risk part of any paper. They are also the ones that must reach the item bank, since nothing else holds them.

Report which group each item falls in. The counts alone tell the author where the risk sits.

## Reporting

The report is written in this order:

1. **Three counts** — by severity, by provenance, and **by pass, including the passes that found nothing**, so a pass that never ran cannot hide behind a missing heading.
2. **The measurement table**, exactly as it was built before judging.
3. **Each item in severity order** — the quoted evidence, the flaw named, and a proposed rewrite for every Block and Revise. Items that pass are listed as passing, so the author can see the paper was covered.

Whatever shape the report takes, it answers the questions the institution's own critique paperwork asks, so its fields can be transcribed rather than re-derived:

- Per item: the cognitive level, whether the item is usable as written, and on what point it needs improvement.
- For the paper: the tally of items by cognitive level, the number of items requiring revision, and whether the paper follows its test blueprint — with the reason where it does not.

A report whose numbers were never counted reads exactly like one whose numbers were, until someone counts them; publishing the table is what makes the difference visible without re-doing the work.

Leave the verdict column for a human to fill where the paperwork is signed by people. A form that arrives already ticked gets agreed with rather than read.

## Cognitive level scales

Institutions record levels on their own scale, and the report is written on theirs, not on this file's. Map by meaning, never by position — the original and revised taxonomies swap their top two levels:

| Institution's scale (Thai) | Revised Bloom |
|---|---|
| รู้-จำ | Remember |
| เข้าใจ | Understand |
| นำไปใช้ | Apply |
| วิเคราะห์ | Analyze |
| ประเมินค่า | Evaluate |
| สังเคราะห์ | Create |

Where the institution's form offers fewer columns than the levels its own summary sheet lists, say so and ask which column the item belongs in. Silently folding an unlisted level into a neighbouring one makes the tally on the two sheets disagree.

## Sources

- NBME, *Item-Writing Guide: Constructing Written Test Questions*, 6th ed. — chapter 3, technical item flaws, and the summary table pairing each flaw with its solution.
- Haladyna, Downing & Rodriguez (2002), "A Review of Multiple-Choice Item-Writing Guidelines for Classroom Assessment", *Applied Measurement in Education* 15(3), 309–334 — the 31-guideline taxonomy.
- Moore, Nguyen, Chen & Stamper (2023), "Assessing the Quality of Multiple-Choice Questions Using GPT-4 and Rule-Based Methods" — the 19-item Item-Writing Flaws rubric, and the comparison of rule-based and LLM application of it.
- Rodriguez (2005) on the optimal number of options; Downing (2005) and Tarrant & Ware (2008) on what flawed items do to scores.
