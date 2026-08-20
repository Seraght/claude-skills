---
name: make-exam
description: Build an exam set in dependency order — blueprint mapped to learning outcomes and teaching hours, then items, answer key, and rubric. Use when the user says /make-exam (ออกข้อสอบ), or asks to write midterm, final, practical, or quiz items for a course.
---

# make-exam — build an exam set

This skill is an ordered checklist — do not skip steps, and do not start a document before the one it depends on is finished. Each artifact is derived from the previous one: items that precede a blueprint end up weighted by what was easy to write. The assessment principles behind each step are in [ASSESSMENT-REFERENCE.md](./ASSESSMENT-REFERENCE.md) — read it before step 5.

## Steps

1. **Discover the project's conventions** — read the host project's `CLAUDE.md` and inspect an existing exam set: folder layout, file naming, available templates, and whether the project carries its own assessment reference. A project's own assessment rules override [ASSESSMENT-REFERENCE.md](./ASSESSMENT-REFERENCE.md); its templates override the document shapes below.
2. **Open the exam set folder** — one folder per exam, named by the project's rule (default `assessment/<year>/<midterm|final|practical|quiz-NN>/`).
3. **Read the course definition** — the syllabus or its digest: learning outcomes, grade weighting, and teaching hours per topic. These are the facts the blueprint is built from; take them from the document rather than estimating, and ask the user if the document is missing any of them.
4. **Research only what is missing** — if the exam needs subject knowledge neither the course documents nor the assessment reference supply, gather it and record it in `00-research.md` with sources.
5. **Write the blueprint** (`01-blueprint.md`) — every cell mapped to a learning outcome, marks per topic tracking that topic's teaching hours, totals reconciling with the course's grade weighting.
6. **Write the items** (`02-items.md`) — each item tagged with its learning outcome and cognitive level, filling the blueprint cell by cell. The blueprint is the specification: the finished bank matches it exactly.
7. **Write the answer key** (`04-answer-key.md`) — every item, with the rationale for each distractor on selected-response items.
8. **Write the rubric** (`05-rubric.md`) — for every constructed-response and practical item, with observable criteria whose weights sum to the item's marks.
9. **Write the paper** (`03-paper.md`) — only when the project separates the examinee-facing paper from the item bank.
10. **Verify before finishing** — if the project has a link or status check script, run it; then confirm: blueprint marks total to the course's grade weighting, every item traces to a learning outcome, every item appears in the answer key, and every constructed-response item has rubric criteria.
