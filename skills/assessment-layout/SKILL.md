---
name: assessment-layout
description: Where a vault's exam sets, item bank, and review paperwork live, and what the file numbers mean. Use when reading or writing an exam set, or when another skill needs the assessment layout.
---

# Assessment Layout

The shape every assessment skill in this set reads and writes, and the table those skills put items to the user in. It is reference only — it carries no steps of its own.

**The vault's `AGENTS.md` is the authority.** What follows is the skill default, used only where the vault says nothing. A vault that states its own layout overrides the files and folders below, and an artifact is not misfiled for obeying the vault.

## Where things live

```
<subject>/assessment/
├── bank/                     ← items, reusable, outliving every paper
└── <year>/
    └── <midterm|final|practical|quiz-NN>/    ← one exam set per folder
```

`assessment/` hangs under the subject's own tree, not at the vault root: an exam belongs to a subject and travels with it. The bank sits beside the exam sets rather than inside one — filing an item inside the exam that first used it turns reuse into copies with no original.

## What the file numbers mean

The leading number is the **lifecycle stage**, not a position in a sequence:

| Stage | Meaning | Default files |
|---|---|---|
| `0x` | Authoring — before the paper exists | `00-research.md`, `01-blueprint.md`, `02-items.md`, `03-paper.md`, `04-answer-key.md`, `05-rubric.md`, `06-measurements.md`, `07-sketches.md`, `08-contributed.md` |
| `1x` | Review — after the paper is assembled, before it is used | `10-critique.md`, `11-critique-independent.md` |
| `2x` | After administration | `20-item-analysis.md` |

Every stage has a skill that fills it: `make-exam`, `make-practical`, or — where the items came from another author — `adopt-pool` for `0x`, `critique-mcq` for `1x`, `analyze-results` for `2x`. A stage the layout declares and nothing performs is a gap that reads as a completed step.

`08-contributed.md` holds a contributed pool exactly as it arrived — every item numbered as its author numbered it, with its key as given, under the path of the file it came from — and is never edited after. It sits in the authoring stage because the set is built from it, and it is what a critique matches each item back to when it establishes provenance.

The review stage carries two files rather than one. The second is an independent pass that measures the paper again from scratch rather than reading the first pass's table, because a critique built on a measurement it inherited certifies that measurement rather than checking it. Numbers are left unused inside each stage, so an artifact can be inserted without renumbering across stages. A missing stage reads as a stage that did not happen, rather than as a gap to be filled by the next number in the folder — which is why a review artifact takes the next free `1x` and never the number after the last authoring file.

`HANDOFF.md` carries no number, because it belongs to no stage: it records where an unfinished run stopped, so that a new session can resume it, and the run that wrote it deletes it when it finishes. A set folder holding one is a set still being written. What goes into it is set out by the skills that write it.

## What a blueprint holds

Rows are topics. Columns are cognitive levels. Each cell holds three things, not two:

| | Remember | Understand | Apply | … |
|---|---|---|---|---|
| Topic 1 | 4 items · 4 marks · MCQ | 2 items · 4 marks · MCQ | — | |
| Topic 2 | — | 1 item · 5 marks · short answer | 1 item · 10 marks · essay | |

- **Item count and marks** — what the cell is worth, and how many items carry it.
- **Item format** — selected-response, matching, constructed-response, practical. It belongs in the cell because a format chosen later is chosen by what is quickest to write, and a high-level cell filled with the wrong format leaves its outcome unassessed while the totals still reconcile. **One declaration covering the whole paper does not satisfy this**, even where every cell turns out to use the same format: the check is made cell by cell against the level that cell claims, and a paper-level line gives it nothing to check.

Every cell names the learning outcome it serves, and every outcome the course states appears in at least one cell. Where the exam schedules time per task rather than per paper — a practical, an open-book paper — the cell carries its time budget too, since minutes per mark is what decides which tasks examinees abandon.

### What decides a row's marks

A topic's share of the marks tracks its share of the teaching hours, because a paper spending two marks on the six hours it taught is not a sample of the course:

    topic's share of marks (%) = topic's teaching hours ÷ hours the paper covers × 100

Departing from that share is ordinary and has to be written down. Raise it where the topic is core to the ones built on it, where it carries an outcome nothing else assesses, or where getting it wrong is a safety or ethics failure. Lower it where the topic is an overview, where a report or a practical already assesses it, or where most of its hours were practice assessed elsewhere. **Past about five percentage points either way, the blueprint states its reason** in its own design notes: the band exists so that a departure is a decision on the record rather than an accident nobody can date. The proportional principle is the standards literature's; the five-point band is a working rule with no published threshold behind it.

### How many items fit

An item count is decided by the time available, not by a round number. Working figures, scaled from the 1.5 minutes per item that large-scale health-science testing allows:

| Item | Time |
|---|---|
| Short selected-response — Remember or Understand, stem of two lines or less | 45–60 s |
| Scenario-based selected-response — Apply and above | 90–120 s |
| One matching set of five pairs | 2–3 min |
| Restricted-response written item | 5–10 min |
| Extended-response written item | 20–30 min |
| Reading the instructions and checking back | add 10% of the total |

A paper that does not fit its own duration measures reading speed, and it does so hardest on the examinees the outcome was written for. These are working figures for classroom papers rather than researched values; a cohort new to the format needs more.

**The vault's own blueprint form wins.** Where an institution fixes the shape — a mandated form with its own columns — that shape governs, and the three things above are recorded wherever it has room for them.

## Stimulus sets

A stimulus set is one stimulus — a table, a query, a log, a diagram, a form — and every item answered from it. In the items file it is one block: a heading naming the set and the items it serves (`Set S1 · items 28–33`), the stimulus once, then the items, each tagged with its own cell, since one set routinely spans several levels. The stems do not retell the stimulus.

In the bank the stimulus is a file of its own under `stimuli/`, named by an id, and each of its items names that id. A stimulus outlives every paper that uses it: a table set this year carries new items next year.

## Approval table

Where a step puts items to the user to approve — rewrites, a calibration batch, the selection for a paper, sketches to keep or drop — it shows them as one table, one row per item:

| Item | Proposed | Measured | Your answer |
|---|---|---|---|
| 12 | rewrite of option C | longest option 41 characters, key B | |

- The two middle columns are the calling step's to fill: what it proposes for the item, and the numbers it was judged on. The headers are written in the user's language.
- The user may answer row by row or the whole table at once. Each row carries what it is judged on, so an answer to the table is still an answer about evidence on the page — unlike a grill round, where a "yes" answers only its own question.
- A question the table raises that is not about one item — a notation for the whole paper, a slide that contradicts a key — is not a row. It is asked after the table, in the round shape the `grill-point` skill gives. An answer to the whole table covers its rows only; the round after it is answered against each number, as that skill's step 3 says.
- Where the items already sit in a file built as rows, such as the sketches file, that file is the table, and the conversation points to it rather than repeating it.

## What binds to what

- **The blueprint binds to the assembled paper**, not to the pool of items written. Writing a surplus to choose from is the practice; the reconciliation happens at assembly.
- **Statistics attach to an item *version*** — one specific wording and option order, and the stimulus it is answered from — not to the item. A value carried across an edit measures something other than what it claims to, so editing a stimulus after it was sat gives every item in its set a new version.
- **A version begins when the item is first sat.** Before that there are no statistics to protect, so the items file holds only the current text of each item: an edit replaces the old wording, an item the user drops is deleted, and an item kept but not chosen for the paper moves to the bank at assembly, carrying its key and its distractor rationales. A trail of earlier drafts in the file is what makes it unreadable, and it protects nothing.
- **Per-person data stays out of the vault.** Names, identifiers, and individual scores do not enter; item-level statistics do.

The reasoning behind each of these is in [ADR 0004](../../docs/adr/0004-stage-the-assessment-set-and-version-its-items.md).
