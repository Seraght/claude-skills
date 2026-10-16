# The vault keeps its reasons

A grill point ([ADR 0016](0016-agreement-is-not-understanding.md)) settles decisions with the user. Left in the conversation, they end with it: the next run asks again, or decides the other way without knowing the question was ever settled. `make-exam` would put to the user, every term, what `design-course` had already agreed with them about how an outcome is assessed. Nobody could look back and find why a course was built the way it was.

We decided four things.

**A decision record holds one decision, at one of two scopes.** It is the vault's counterpart of this repo's own ADRs, and the two are kept apart on purpose: an ADR records why a *skill* is the way it is, a decision record why the *work in the vault* is. The scope is settled by one question — if this subject were deleted, would the decision still bind another one? A vault-scope record binds every subject, such as how the user writes options; a subject-scope record binds one, including decisions about a single paper of it, and lives inside the subject so the reasons move and archive with it. A third scope for single papers was turned down: every scope is one more place each grill must read before it asks anything.

**Only some answers become records.** One is written when the decision outlives the artifact, had a real alternative, and would leave a later reader asking why — the test this repo applies to its own ADRs. The rest shape the artifact and stop there. A record must name what was turned down and at what cost, because a record exists only where there was an alternative, and writing it down is what shows the decision was a trade-off. One decision is always recorded: assessing an outcome below the level it claims, since the paper does not show that gap and the next review of the outcomes is the reader who needs it. Records are never edited to change their decision; a new one supersedes the old, so the history stays readable. The shape lives with the primitive that writes it, `grill-point`.

**Decision records are the twelfth component of the anatomy.** A vault an agent works in, with nowhere for its reasons to go, asks the same questions again whatever its subject, so the component is true everywhere ([ADR 0013](0013-true-everywhere-or-true-here.md)) and belongs in `brain-anatomy` rather than in the teaching skills alone. It is numbered last instead of by its group, so the numbers in earlier scorecards keep their meaning.

**An update reaches an existing vault through `audit-brain`, not through a setup skill.** The interview this set borrows from configures a repo through a dedicated setup skill. This set already has that job, split in two on purpose — `init-brain` for an empty vault, `audit-brain` for one with content — and a third skill that also knew what a vault needs would be a third copy to drift. So: nothing new has to exist before it is used, since the folders appear with the first record and the teaching constraints are asked the first time a grill needs them; `audit-brain` is reachable by "after updating the skills", and marks the components its previous scorecard did not have, which makes the vault's own scorecards the record of what an update changed.

**Teaching constraints live in the subject's overview.** Equipment, rooms, expertise, staff, and the learners — their programme, their background, what can be expected of them — are facts rather than decisions, so they are not decision records. They decide whether a design can be taught at all, no syllabus holds them, and a grill asks for them when they are missing and writes the answer back, so each one is asked once per subject.

## Considered Options

- **Keep decisions inside the artifact they shaped**, a decisions section of the blueprint — rejected by the user: some decisions bind across subjects, and a section of one subject's blueprint is not where another subject's run would look.
- **One folder with a scope tag on each record** — rejected: a subject's reasons would not move with the subject.
- **Record every answer** — rejected: the records that matter sink beneath the ones that do not.
- **A setup skill run after each update** — rejected for the drift above, and because a prerequisite step contradicts the README's promise that a skill asks for what it needs along the way, which the people least able to run a setup step depend on.
- **A vault-level file for teaching constraints** — rejected: most of them belong to one subject's room, equipment, and cohort.

## Consequences

- `brain-anatomy` has twelve components; `audit-brain` scores twelve and is reachable after an update.
- `new-subject` writes a teaching-constraints section into the overview, with gap markers where the source document is silent.
- `grill-point` reads both scopes of records and the teaching constraints before its first question, lists the records that bind the run, and writes new records after its last.
