---
name: new-subject
description: Open a new subject area in a knowledge base — create the folder skeleton, file the defining source document, digest it into a structured summary, write the subject overview from template, register it in the index. Use when the user says /new-subject (เปิดวิชาใหม่), or supplies the defining document for a subject that is not in the index yet.
---

# new-subject — open a new subject area

This skill is an ordered checklist — do not skip steps. It carries the *process* only: the skeleton shape, templates, and naming rules are discovered from the host project at runtime.

## Steps

1. **Discover the project's conventions** — read the host project's `CLAUDE.md` and inspect an existing subject: the folder skeleton it uses, its naming rule, which templates exist, and where the index lives. An existing subject is the specification; match it rather than inventing a shape.
2. **Check the index first** — if the subject is already registered, stop and ask the user whether they meant to extend it instead of creating a duplicate.
3. **Create the skeleton** — one folder per subject, named by the project's rule (default `<id>-<english-slug>`, no spaces), with the same subfolders the existing subjects use.
4. **File the defining source document unmodified** — the original goes in the source folder and stays as received; all later work happens in derived files.
5. **Digest the source into a structured summary** — extract everything downstream work will need, following the project's digest template. Every fact comes from the document; ask the user for anything missing rather than inferring it. *Example — a course syllabus digest needs: subject code and name, credits, program with year and cohort size, term, learning outcomes and their mapping to program outcomes, the weekly schedule, grade weighting with exam weeks, and the teaching team.*
6. **Write the subject overview file** from the project's template.
7. **Register one row in the index.**
8. **Place grouping-level records at the grouping level** — if this subject belongs to a grouping that carries its own records (a program, a client, a domain) and that grouping is not registered yet, create it at the shared level, not inside the subject. One grouping may span many subjects and may have several revisions of its own.
9. **Verify before finishing** — if the project has status or link check scripts, run them; otherwise verify manually: the skeleton matches the existing subjects, the index row resolves to the new folder, and every link in the new files points at a file that exists.
