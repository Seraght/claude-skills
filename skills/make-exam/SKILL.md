---
name: make-exam
description: Build an exam set in dependency order — blueprint, items, answer key, rubric. Use when the user asks to build an exam (ออกข้อสอบ), or to write midterm, final, practical, or quiz items.
---

# make-exam — build an exam set

This skill is an ordered checklist: each step opens when the one before it has produced its result. Each artifact is derived from the one before it: items that precede a blueprint end up weighted by what was easy to write. The folder shape and what the file numbers mean are in the `assessment-layout` skill; the assessment principles behind each step are in [ASSESSMENT-REFERENCE.md](./ASSESSMENT-REFERENCE.md) — read it before step 5.

## Steps

1. **Discover the project's conventions** — read the host project's agent instructions file (`AGENTS.md`, or `CLAUDE.md`) and inspect an existing exam set: folder layout, file naming, available templates, and whether the project carries its own assessment reference. A project's own assessment rules override [ASSESSMENT-REFERENCE.md](./ASSESSMENT-REFERENCE.md); its templates override the document shapes below.
2. **Open the exam set folder** — one folder per exam, in the place and under the name the `assessment-layout` skill gives, unless the vault's own rule says otherwise.
3. **Read the course definition** — the syllabus or its digest: learning outcomes, grade weighting, and teaching hours per topic. These are the facts the blueprint is built from; take them from the document rather than estimating, and ask the user if the document is missing any of them.
4. **Research only what is missing** — if the exam needs subject knowledge neither the course documents nor the assessment reference supply, gather it and record it in `00-research.md` with sources.
5. **Write the blueprint** (`01-blueprint.md`) — every cell mapped to a learning outcome, marks per topic tracking that topic's teaching hours, totals reconciling with the course's grade weighting.
6. **Write the items** (`02-items.md`) — each item tagged with its learning outcome and cognitive level, filling the blueprint cell by cell. The blueprint is the specification. Writing more items than a cell needs is fine — a surplus to choose from is normal practice — but every item belongs to a cell, and the reconciliation happens when the paper is assembled, not here. On selected-response items write the stem first, then the distractors, then the correct option — writing the correct option first is what makes it the longest and the most qualified of the four.
7. **Audit the items for cues** — before writing the key, read each item's options with the stem and the correct option covered, and ask which one a test-wise examinee would pick knowing nothing about the subject. Any item whose answer is predictable from the options alone is rewritten. The checks to run are in [ASSESSMENT-REFERENCE.md](./ASSESSMENT-REFERENCE.md).
8. **Write the answer key** (`04-answer-key.md`) — every item, with the rationale for each distractor on selected-response items.
9. **Write the rubric** (`05-rubric.md`) — for every constructed-response and practical item, with observable criteria whose weights sum to the item's marks.
10. **Assemble the paper** (`03-paper.md` where the project separates the examinee-facing paper from the item bank) — decide which items the exam takes, then reconcile the blueprint against exactly those: marks per topic and the level distribution are recomputed for the selected set. A blueprint balanced over a larger pool says nothing about the subset drawn from it.
11. **Verify before finishing** — run the project's check script where one exists, then confirm: the assembled paper's marks total to the course's grade weighting, every item traces to a learning outcome, every item appears in the answer key, every constructed-response item has rubric criteria, and no selected-response item is answerable from its options alone.
