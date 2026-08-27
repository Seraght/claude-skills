# MCQ Critique Reference

The flaw taxonomy the `critique-mcq` skill applies, the measurements it is judged from, and the discipline that keeps a critique usable. When the host project carries its own assessment reference or item-writing rules, that one governs and this file fills the gaps it leaves — a paper whose regulations require a fixed number of options, or a fixed number of negatively worded items, is not flawed for following them.

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

In Thai, Khmer, Lao, Japanese, and Chinese, a word count is not a measurement — the whole option reads as one token — so length is counted in characters, and several checks need a different marker than their English form. A tokenizer, where one is installed, is a convenience for the length check; it is never a prerequisite.

Working equivalents for Thai:

- **Grammatical cues** — not number agreement, which Thai does not mark. Look at a lead-in ending in a classifier or a connective (`เป็น`, `คือ`, `ที่`, `ซึ่ง`, `เพื่อ`, `ได้แก่`) that only one option continues naturally, and at classifiers that agree with one option's noun only.
- **Clang cues** — a word repeated from the stem into the key, and shared Pali-Sanskrit elements (`โรค-`, `อภิ-`, `-วิทยา`, `-ภาพ`) that tie one option to the stem.
- **Absolute terms** — `เสมอ`, `ทุกครั้ง`, `ทั้งหมด`, `ไม่เคย`, `เท่านั้น`, `ห้ามเด็ดขาด`.
- **Vague frequency terms** — `มักจะ`, `บ่อยครั้ง`, `โดยทั่วไป`, `บางครั้ง`, `ส่วนใหญ่`.
- **Negation in the lead-in** — `ข้อใดไม่ใช่`, `ข้อใดไม่ถูกต้อง`, `ยกเว้น`.
- **"None / all of the above"** — `ถูกทุกข้อ`, `ผิดทุกข้อ`, `ไม่มีข้อใดถูก`.
- **Complex (K-type) options** — `ข้อ ก และ ข ถูก`.

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

## Group A — cues that reward test-wiseness

Flaws that let an examinee who does not know the content pick the key anyway.

- **Correct option stands out.** The key is longer, more qualified, or more detailed than the distractors — it carries the parenthetical gloss, the caveat, the worked example the others lack. It arises because the writer wrote the key first, as a true statement, and teachers writing keys add instructional material to them. *Fix:* move the qualifier into the stem where it applies to all options; strip teaching language from the key; equalize the level of detail across the set.
- **Convergence.** The key is the option sharing the most elements with the others, because the distractors were written as permutations of it — counting which terms recur picks it out without reading the stem. *Fix:* balance the use of terms so no option is the modal combination.
- **Collectively exhaustive options.** A subset of options covers every possibility (increases / decreases / no change), so the key must be inside that subset and the remaining options are visibly filler. *Fix:* replace at least one option in the subset, without creating a matched pair while doing it.
- **Logical cues, odd one out.** One option stands alone on a dimension the stem implies — polarity, direction, tense, scope, grammatical category — and is chosen for standing apart. If the stem asks for a drawback, every option names a drawback. *Fix:* bring the distractors onto the key's dimension.
- **Grammatical cues.** An option does not follow grammatically from the lead-in, and the ones that do not read cleanly are eliminated without knowledge. *Fix:* use a closed lead-in; make every option follow from it.
- **Word repeats (clang cues).** A word from the stem reappears in the key, including at the level of a root. *Fix:* replace the repeated word on one side, or use it in every option.
- **Absolute terms.** Words meaning "always" or "never" appear in some options; examinees reject them on sight, whether or not they are wrong. *Fix:* remove them; put the verb in the lead-in and keep the options short and homogeneous.

## Group B — irrelevant difficulty

Flaws that make the item hard for reasons unrelated to what it is meant to measure. These cost every examinee, not only the ones who do not know the content.

- **Long or complex options.** Reading load shifts the item toward measuring reading speed. *Fix:* move text common to all options into the stem; shorten what remains.
- **Nonparallel options.** Each option is built differently, so the set has to be parsed one at a time. *Fix:* edit all options to one grammatical shape, usually by rewording the lead-in first.
- **Negatively structured stem.** Examinees miss the negation even in bold, and the item measures attention. *Fix:* rewrite positively; where the content genuinely calls for exclusion, build a scenario from the correct statements instead.
- **Vague terms.** Frequency words in the options — different readers assign them different probabilities, so the item has no single defensible answer. *Fix:* state the condition precisely or drop the frequency word.
- **Inconsistent or overlapping numeric data.** Overlapping ranges, or units and precision that vary across options, produce more than one correct answer. *Fix:* make the ranges disjoint and the format uniform; ask for a minimum or maximum where a boundary is at stake.
- **Tricky or padded stems.** Window dressing, teaching statements, or detail included only to mislead. *Fix:* keep what is needed to answer the item or to make a distractor attractive; cut the rest.
- **"None of the above" and "all of the above".** "None of the above" turns a best-answer item into a set of true-false judgements against everything unlisted; "all of the above" is answerable from partial knowledge. *Fix:* replace "none of the above" with the specific action it stands for; remove "all of the above".
- **Complex (K-type) options.** Knowing one component eliminates half the set. *Fix:* convert to single best answer.
- **Unfocused stem.** The stem cannot be answered with the options covered, so the examinee reads the options to discover what is being asked. *Fix:* put the central idea in the stem and close the lead-in.
- **Mid-sentence blanks.** A gap inside the stem that the options fill turns reading into reassembly. *Fix:* ask the question as a question.
- **More than one defensible answer.** Another option can be argued correct under a reading the stem does not exclude. *Fix:* tighten the stem, or rewrite the competing option.
- **Implausible distractors.** An option no informed examinee would ever choose does no work; at administration it shows up as a non-functioning distractor, one selected by fewer than 5% of examinees. Three working options discriminate better than five with two dead ones. *Fix:* replace it with a named misconception, or drop it where the paper's rules allow a shorter option set.
- **Hinged items.** Answering this item requires having answered another one correctly, so one lapse is scored twice. *Fix:* make the items independent.
- **True-false series.** The options are unrelated statements to be judged one by one rather than compared. *Fix:* rebuild as one best-answer item, or split into separate items.

## Group C — congruence, level, and correctness

Surface flaws are the visible half. An item can pass every check above and still be the wrong item, or a wrong answer.

- **The keyed answer is defensible against the course's own sources.** Check it against the syllabus, the teaching material, or the references the vault holds — not against the model's own knowledge, which is what produced the error in an AI-written item in the first place. Where no source is available to check against, the report says the item's content was not verified rather than passing over it in silence. This check finds what no structural check can: roughly a fifth of AI-written items in the research record carry a factual or conceptual error while looking perfectly well formed.
- **Outcome congruence.** The item measures the learning outcome it is tagged with — not a neighbouring one, and not a prerequisite skill that happens to be needed to read it.
- **Blueprint fit.** The item fills the cell it was written for, and that cell exists. An item serving no cell is cut, not filed.
- **Actual cognitive level.** Judge by what the examinee must do, not by the verb in the stem: an "analyze" item whose answer appeared verbatim in the notes tests Remember. Recall items dominate real papers — in one study 91% of the control-group items tested factual recall — so an item claiming a higher level earns the check rather than the benefit of the doubt.
- **Novel material.** Language paraphrased from the slides tests recognition of the slides. A higher-level item needs a situation the examinee has not already seen resolved.
- **Content worth asking.** Not trivia, not opinion, not a trick. If nobody would be worse off for not knowing it, the item is spending marks a real outcome needs.
- **Distractor accountability.** Every distractor names a misconception a real examinee holds. A distractor whose misconception cannot be stated is filler, and filler is why option sets get padded.

### Cognitive level scales

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

## Group D — the paper as a whole

Defects that are invisible one item at a time, and that selecting and reordering items create after every per-item check has passed.

- **The key matches the option it points at.** Verify against the final option order, item by item, rather than trusting that the key was updated when options were reordered. Where the options carry no visible labels — as with an automatically numbered list in a word processor — position is the only anchor there is. **Block.**
- **The blueprint reconciles against the items actually selected.** Marks per topic and the level distribution are recomputed for the assembled paper. A blueprint balanced over a larger pool says nothing about the subset drawn from it.
- **No item answers another.** A stem that supplies a fact, a definition, or a worked value that another item asks for gives that item away. This is not the same as a hinged item: nothing here depends on answering correctly, only on having read.
- **No option set is reused between items.** Options copied from a neighbouring item and not recomputed give a set that cannot contain the right answer, and the defect then reads as a typo in the stem rather than as what it is. The giveaway is two items offering exactly the same options. Numeric sets are where copying hides best, since nothing looks out of place. *Fix:* compute the option set for the item at hand.
- **No duplicated coverage.** Two items testing the same point at the same level spend two items' worth of marks on one thing, and usually mean some other cell went short.
- **Key positions spread, and do not run.** Two separate checks: the distribution across positions, and the longest run of consecutive items keyed to the same position. A paper can be perfectly balanced overall and still hand out four or five in a row, which is the pattern an examinee notices while sitting the exam. *Fix:* re-scramble option order — then re-verify every key against the new order.
- **The paper is answerable in the time allowed.** Item count and reading load against the scheduled duration.
- **Format is consistent across the paper.** Option count, labelling, and instructions do not vary between sections without a stated reason.

## Provenance

A paper assembled from a larger pool contains items with different histories, and they do not deserve the same treatment:

- **Used unchanged** — carries forward whatever checks it already passed.
- **Edited after selection** — every earlier check is void. Tightening a stem can strip the qualifier that made the key true; reordering options moves the key. Re-measure and re-run all four groups.
- **Written outside the set** — items added by hand to fill a blueprint cell nothing else covered. These have passed nothing, were written last and under time pressure, and are the highest-risk part of any paper. They are also the ones that must reach the item bank, since nothing else holds them.

Report which group each item falls in. The counts alone tell the author where the risk sits.

## Number of options

Three well-made options — a key and two working distractors — measure as well as four or five in the research record, and forcing a fixed count is what produces filler distractors and collectively exhaustive sets. Where the host project or the institution fixes the number, that rule governs, and the flaw to report is the filler distractor itself rather than the count.

## Check the fix

Repairs introduce their own flaws, and a critique that stops at the first rewrite hands back a differently broken item:

- Padding distractors to match the key's length makes them implausible — trim the key or move text into the stem instead.
- Trimming the key for length parity can leave it no longer strictly true.
- Adding an option to reach a required count is how filler distractors and collectively exhaustive sets appear.
- Replacing a repeated word with a synonym can change what the item asks.
- Re-scrambling option order to spread the keys moves every key.

Re-run the measurements on any item that was rewritten.

## Reporting

Whatever shape the report takes, it answers the questions the institution's own critique paperwork asks, so its fields can be transcribed rather than re-derived:

- Per item: the cognitive level, whether the item is usable as written, and on what point it needs improvement.
- For the paper: the tally of items by cognitive level, the number of items requiring revision, and whether the paper follows its test blueprint — with the reason where it does not.

It also carries the measurement table and a finding count for every pass, zeros included. A report whose numbers were never counted reads exactly like one whose numbers were, until someone counts them; publishing the table is what makes the difference visible without re-doing the work.

Leave the verdict column for a human to fill where the paperwork is signed by people. A form that arrives already ticked gets agreed with rather than read.

## Sources

- NBME, *Item-Writing Guide: Constructing Written Test Questions*, 6th ed. — chapter 3, technical item flaws, and the summary table pairing each flaw with its solution.
- Haladyna, Downing & Rodriguez (2002), "A Review of Multiple-Choice Item-Writing Guidelines for Classroom Assessment", *Applied Measurement in Education* 15(3), 309–334 — the 31-guideline taxonomy.
- Moore, Nguyen, Chen & Stamper (2023), "Assessing the Quality of Multiple-Choice Questions Using GPT-4 and Rule-Based Methods" — the 19-item Item-Writing Flaws rubric, and the comparison of rule-based and LLM application of it.
- Rodriguez (2005) on the optimal number of options; Downing (2005) and Tarrant & Ware (2008) on what flawed items do to scores.
