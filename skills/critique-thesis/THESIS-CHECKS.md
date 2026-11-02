# Thesis Checks

The checks a thesis critique runs, and the shape its report takes. Every check here once found a real defect in a submitted thesis or proposal; none is a style preference. A check is run by recomputing or looking something up, never by reading the book and judging that it seems fine, and it is recorded in the evidence table whether or not it finds anything.

When the host project carries its own thesis regulations, format guide, or interpretation criteria, those govern and this file fills the gaps they leave.

## The evidence table

One row per check per place it applies: the check, the page, what was recomputed or looked up, the value the book reports, the value found, and the verdict — *consistent*, *finding*, or *cannot check* with what stopped it. A check that does not apply to this thesis gets one row saying why. The table is kept beside the critique, so a check that did not run is visible rather than silently absent. Personal data found in the book is recorded by page and kind — "a phone number, p. 114" — never by its value, in the table as in the critique.

A finding cites the page it is on. A finding of absence — no ethics number, an objective with no result — cites the page range that was searched.

## A. Numbers the book lets you recompute

**Rounding is not a finding.** Recompute from the values as printed, carry half a unit of each value's last printed digit through the calculation, and report only a difference that falls outside that band. A value back-solved from rounded inputs is a range, and the finding is a reported value outside it.

- **Percentages against counts.** Recompute every percentage in every table from the counts beside it, and every total from its parts.
- **An aspect mean is the mean of its item means** when every respondent answered every item. A reported aspect mean that differs is a calculation or transcription error.
- **A standard deviation cannot exceed its scale's ceiling.** For scores bounded by `min` and `max` with mean `x̄`, the population SD is at most `√((max − x̄)(x̄ − min))` (the Bhatia–Davis inequality); the sample SD statistics software reports is at most that times `√(n / (n − 1))`. Where the book also reports how many scored in each band, find the largest SD those counts and that mean allow; a reported SD above the bound is impossible.
- **A correlation, its p value, and n must agree.** `t = r√(n − 2) / √(1 − r²)` with `n − 2` degrees of freedom: back-solve the range of n the rounded r and p allow, and compare with the sample the book says it analysed.
- **Interpretation labels against the stated cut-offs.** Every mean labelled "high", "moderate" and so on falls in the band the book's own criterion gives that label. Score-band cut-offs give the percentages they claim.
- **Planned sample against achieved sample**, stratum by stratum, and the response rate the book reports against the two.
- **Try-out statistics hang together.** The sum of item difficulties equals the try-out's mean score, within rounding.

## B. The book contains what it claims

- **Every objective and hypothesis has its result in the results chapter**, with the full statistic: test statistic, degrees of freedom, p, and effect where one is claimed. A conclusion or abstract that states a relation the results chapter does not show is a finding against the conclusion.
- **Every table's title matches its content.** A mislabelled table can hide a missing one.
- **Instrument quality is reported, not only planned**: content validity by experts with its index, reliability with its coefficient, and try-out results. A methods chapter that says these will be done is not evidence that they were.
- **Ethics approval is evidenced** by its number and date, and agrees with what the methods describe.
- **For a system, tool, or calculator**: the logic it computes is written out, and any claim that it is faster, more accurate, or easier is measured against the method it replaces.

## C. The design measures what it says

- **Independent-variable items that ask about the dependent variable**, or duplicate its items, make the relation between them partly the same question asked twice.
- **The framework's dimensions against the source it cites.** Open the cited source and compare; a framework attributed to a source that says something else is a finding.
- **A sampling method named as random** is checked against how participants were actually reached.
- **The same test form before and after** an intervention carries a practice effect; a claim of *skill* from a knowledge test claims more than was measured.
- **A system's design diagrams model its data and processes.** An entity-relationship diagram whose entities are screens or pages describes the interface, not the data.
- **Scope, teaching, and test items map onto each other.** Every test item covers something in scope and taught; something dropped from scope in a revision takes its items with it. Answer keys are checked against the discipline's own rules.

## D. Ethics and confidentiality

- **Quotes tagged with a unit, ward, or institution** whose role has only one holder identify their respondent.
- **Personal data printed in the book** — phone numbers, ID numbers, signatures — is a finding to remove before the book is published.
- **What the ethics statement promises against what the methods did** — synthetic data against real records, a sandbox against a production system.

## E. References

- **Citations against the bibliography, in both directions**: count each, and list every in-text citation with no entry and every entry never cited.
- **A DOI exists.** `https://doi.org/api/handles/<doi>` answers `responseCode` 1 for a registered DOI and 100 for none; run one known-good DOI alongside as a control.
- **A DOI's metadata matches the citation.** `https://api.crossref.org/works/<doi>/agency` names the agency that registered it; for Crossref, `https://api.crossref.org/works/<doi>` gives authors, year, journal, volume, and pages to compare, and for any agency, `https://doi.org/<doi>` requested with `Accept: application/vnd.citationstyles.csl+json` gives the same fields. Percent-encode a DOI that holds `<`, `>`, `#`, or `;`.
- **A citation with no DOI is matched to its journal issue.** List the issue's articles — Crossref `https://api.crossref.org/journals/<issn>/works` filtered by publication date, or the `citation_*` meta tags on a Thai journal's article page — and confirm the cited pages hold the cited article rather than another one.
- **Signs of generated references**: a real title under an invented journal, volume, or page range; co-authors who do not appear on the paper; the same surnames recurring across unrelated entries; and conversational residue in the text around them. One confirmed fabrication means every entry is looked up by identifier or journal issue before the critique treats it as sound.
- **An entry with too little to find** — a surname alone, no title — is a finding of its own, not a reference that passed.
- **An annual report's or ranking's title year** may be the year it was released, the year its data covers, or the year after release, depending on the publisher. Find the edition the figure came from before calling it wrong.

## F. The design a proposal commits to

A proposal is judged on its design, since it has no results to check; a finished thesis is held to the same checks against its methods chapter.

- **The sample has not already learned what the intervention teaches.** Compare the sample's description — year, courses passed, training received — with the intervention's content. A sample that has already studied it measures review, not learning, and leaves the effect little room to show.
- **The sample size comes from a method that can be recomputed**: the Krejcie–Morgan table, Yamane's `n = N / (1 + Ne²)`, or a power analysis (G*Power) stating its test, effect size, α, and power. Recompute it from the stated inputs; a size with no method, or one its inputs do not give, is a finding. Reporting standards ask for the same: APA JARS on sample size, power, and precision; STROBE item 10.
- **The instrument's item count agrees with its interpretation bands.** With `k` items scored `min` to `max`, a total runs from `k × min` to `k × max`; the bands cover that range with no gap and no overlap. Bands built for another item count — copied from the source instrument before items were added or dropped — are a finding.
- **Each hypothesis can be tested on the stated sample.** A comparison needs the groups it compares, measured as the design says; a hypothesis against a control group in a one-group design, or a test the sample's size and level of measurement cannot carry, is a finding.
- **Each objective has its analysis method**: the analysis plan names the statistic that answers it.
- **Objective, hypothesis, framework, variable, instrument, and analysis plan hang together.** Trace every objective along that chain, one evidence-table row per objective; a variable in the framework that no instrument measures, an instrument part no objective uses, or a hypothesis about a variable outside the framework is a break, and each break is a finding.

## A proposal

On a proposal, run groups B to F; group A, and each check elsewhere that reads a results chapter, gets one row, *cannot apply: no results yet*. A check that a proposal states as a plan — instrument quality, ethics approval — is checked as a plan: what will be done, with what, and against which criterion.

## A revised thesis

When the thesis comes back after an earlier critique, or the full thesis arrives after its proposal's, build a **status table** for each section of it: one row per earlier finding, its location in the revised book, and its status — *fixed*, *partly fixed*, *not fixed*, or *worse* — with the evidence. Then run every check above on the whole revised book: reading only what changed misses what the revision broke elsewhere, such as scope trimmed while the items testing it stayed, or a specific safeguard replaced by vaguer wording. New text added in the revision, references above all, is checked as if it were a first submission.

## Reporting

The critique is written in the host project's language, in this order:

1. **Summary**: title, the version checked — proposal, thesis, or revision — the date, the overall verdict in the host institution's own outcome words with its rationale in two or three sentences, and the few findings that decide it.
2. **What to change**: one table the students act on, one row per finding — its code (the section's letter and the finding's number, as ก.1), its page, what to change, and whether it *must* be fixed before the exam or *should* be.
3. **Critical — must be fixed before the exam**: each finding under its code, with the fixed sub-heads *evidence* (page, and the quoted text or the recomputed number), *effect* (what it does to the thesis's conclusions), and *change to* (what the text, table, or design becomes).
4. **Methodology — should be fixed**: the same sub-heads.
5. **Formatting and typing**: a table of page, what was found, and what it should be, after the substance. Where they are many, the summary says so, since enough of them together count against the book.
6. **Strengths**: what the thesis does well, specific enough to keep through revision.
7. **Sources used to check**: every external source a finding rests on, with its link.

A revision run's critique leads each section with its status table.

A finding without its page and its evidence is dropped, however sure it feels. People are named by role — advisor, committee, the student group — never by name or ID.
