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
| `0x` | Authoring — before the paper exists | `00-research.md`, `01-blueprint.md`, `02-items.md`, `03-paper.md`, `04-answer-key.md`, `05-rubric.md` |
| `1x` | Review — after the paper is assembled, before it is used | `10-critique.md` |
| `2x` | After administration | item statistics, post-hoc analysis |

Numbers are left unused inside each stage, so an artifact can be inserted without renumbering across stages. A missing stage reads as a stage that did not happen, rather than as a gap to be filled by the next number in the folder — which is why a review artifact takes the next free `1x` and never the number after the last authoring file.

## What binds to what

- **The blueprint binds to the assembled paper**, not to the pool of items written. Writing a surplus to choose from is the practice; the reconciliation happens at assembly.
- **Statistics attach to an item *version*** — one specific wording and option order — not to the item. A value carried across an edit measures something other than what it claims to.
- **Per-person data stays out of the vault.** Names, identifiers, and individual scores do not enter; item-level statistics do.

The reasoning behind each of these is in [ADR 0004](../../docs/adr/0004-stage-the-assessment-set-and-version-its-items.md).
