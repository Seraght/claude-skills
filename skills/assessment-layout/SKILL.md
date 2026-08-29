---
name: assessment-layout
description: Where a vault's exam sets, item bank, and review paperwork live, and what the file numbers mean. Use when reading or writing an exam set, or when another skill needs the assessment layout.
---

# Assessment Layout

The shape every assessment skill in this set reads and writes. It is reference only — it carries no steps of its own.

**The vault's `AGENTS.md` is the authority.** What follows is the skill default, used only where the vault says nothing. A vault that states its own layout overrides all of it, and an artifact is not misfiled for obeying the vault.

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
| `0x` | Authoring — before the paper exists | `00-research.md`, `01-blueprint.md`, `02-items.md`, `03-paper.md`, `04-answer-key.md`, `05-rubric.md`, `06-measurements.md` |
| `1x` | Review — after the paper is assembled, before it is used | `10-critique.md`, `11-critique-independent.md` |
| `2x` | After administration | `20-item-analysis.md` |

Every stage has a skill that fills it: `make-exam` or `make-practical` for `0x`, `critique-mcq` for `1x`, `analyze-results` for `2x`. A stage the layout declares and nothing performs is a gap that reads as a completed step.

The review stage carries two files rather than one. The second is an independent pass that measures the paper again from scratch rather than reading the first pass's table, because a critique built on a measurement it inherited certifies that measurement rather than checking it. Numbers are left unused inside each stage, so an artifact can be inserted without renumbering across stages. A missing stage reads as a stage that did not happen, rather than as a gap to be filled by the next number in the folder — which is why a review artifact takes the next free `1x` and never the number after the last authoring file.

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

## What binds to what

- **The blueprint binds to the assembled paper**, not to the pool of items written. Writing a surplus to choose from is the practice; the reconciliation happens at assembly.
- **Statistics attach to an item *version*** — one specific wording and option order — not to the item. A value carried across an edit measures something other than what it claims to.
- **Per-person data stays out of the vault.** Names, identifiers, and individual scores do not enter; item-level statistics do.

The reasoning behind each of these is in [ADR 0004](../../docs/adr/0004-stage-the-assessment-set-and-version-its-items.md).
