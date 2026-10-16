---
name: new-subject
description: Open a new subject area in a knowledge base — skeleton, defining document, digest, overview, index row. Use when the user opens a new subject (เปิดวิชาใหม่), or supplies the defining document for one not yet registered.
---

# new-subject — open a new subject area

This skill is an ordered checklist: each step opens when the one before it has produced its result. It carries the *process* only — the skeleton shape, templates, and naming rules are discovered from the host project at runtime.

Whenever a step puts more than one decision to the user, it asks them in the round shape the `grill-point` skill gives in its step 3; an approval of items is asked in the approval table the `assessment-layout` skill gives.

## Steps

1. **Discover the project's conventions** — read the host project's agent instructions file (`AGENTS.md`, or `CLAUDE.md`) and inspect an existing subject: the folder skeleton it uses, its naming rule, which templates exist, and where the index lives. An existing subject is the specification; match it rather than inventing a shape. Then show the user the plan for this run — its steps by number with a 🛑 on each one that stops for the user, then one line of what this step found and one of what it could not find, labelled in the user's language — and wait for the user's go-ahead, or take the dispatch as the go-ahead when this run was sent to work without the user, as a sub-agent; name each later step by its number as it starts.
2. **Check the index first** — if the subject is already registered, stop and ask the user whether they meant to extend it instead of creating a duplicate.
3. **Create the skeleton** — one folder per subject, named by the project's rule (default `<id>-<english-slug>`, no spaces), with the same subfolders the existing subjects use.
4. **File the defining source document unmodified** — the original goes in the source folder and stays as received; all later work happens in derived files.
5. **Digest the source into a structured summary** — extract everything downstream work will need, following the project's digest template. Every fact comes from the document; ask the user for anything missing rather than inferring it. *Example — a course syllabus digest needs: subject code and name, credits, program with year and cohort size, term, learning outcomes and their mapping to program outcomes, the weekly schedule, grade weighting with exam weeks, and the teaching team.*
6. **Write the subject overview file** from the project's template, with a section for the subject's teaching constraints: the equipment and rooms, the expertise and staff behind it, and the learners — their programme, their background, what can realistically be expected of the cohort. Fill what the source document states; give every other line the vault's gap marker, so the first grill point that needs it asks once and writes the answer back here.
7. **Register one row in the index.**
8. **Place grouping-level records at the grouping level** — if this subject belongs to a grouping that carries its own records (a program, a client, a domain) and that grouping is not registered yet, create it at the shared level, not inside the subject. One grouping may span many subjects and may have several revisions of its own.
9. **Verify before finishing** — run the project's check script where one exists, then confirm: the skeleton matches the existing subjects, the index row resolves to the new folder, and every link in the new files points at a file that exists.
