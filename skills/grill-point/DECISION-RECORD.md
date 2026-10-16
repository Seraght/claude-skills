# Decision records

A decision record holds one decision the user made at a grill point: the question, what was chosen, why, and what was turned down at what cost. It records why the *work in the vault* is the way it is, so a later run reads the reason instead of asking again — or, worse, quietly deciding the other way.

## Where they live

Two scopes, told apart by one question: *if this subject were deleted, would the decision still bind another one?*

- **Vault scope** — binds every subject: how the user writes options, how much of a paper sits in stimulus sets. Default `docs/decisions/`.
- **Subject scope** — binds one subject, including decisions about a single paper of it. Default `decisions/` inside the subject's own folder, so the reasons travel with the subject when it moves or is archived.

A rule in the vault's constitution overrides both defaults. Create a folder when its first record is written.

## When to write one

All three must hold:

1. **It outlives this artifact** — a later paper, a later term, or another subject will need it.
2. **There was a real alternative** — something was turned down for a reason.
3. **A later reader would ask why** — without the record the choice looks arbitrary, or wrong.

An answer that fails any of them shapes the artifact and stops there: "this midterm has 40 items" changes next year without anyone needing the reason.

One decision is recorded whatever the tests say: **assessing an outcome below the level it claims.** The paper does not show the gap, and the next review of the outcomes is exactly the reader who needs to find it. The options that lead there, and the order they are offered in, are in the `learning-outcomes` skill.

An intentional exception — an outcome kept *above* its map level — keeps its record beside the outcome, where the `learning-outcomes` skill puts it, rather than here.

## Shape

Numbered by scanning the folder for the highest number and adding one: `0004-short-slug.md`. Written in the vault's language; the frontmatter keys stay as below.

```md
---
status: accepted          # or: superseded by 0007
date: YYYY-MM-DD
decided-by: <who decided>
supersedes: 0003          # only when it replaces an earlier record
---

# <the decision, as one short sentence>

<One to three sentences: the question, what was chosen, and why.>

**Rests on:** <the syllabus line, programme outcome, teaching constraint, or record it was checked against>

**Turned down:**
- <option> — <what it would have cost>
```

**Turned down** is required: a record exists only where there was a real alternative, and writing the alternative down with its cost is what lets a later reader see the decision was a trade-off rather than a default.

An accepted record keeps its decision for good. A change of mind is a new record naming the one it supersedes, and the old record's status becomes `superseded by NNNN` — the only edit it ever receives — so the history of what was decided, and when, stays readable.
