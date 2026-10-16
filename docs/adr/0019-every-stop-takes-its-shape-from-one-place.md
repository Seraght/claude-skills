# Every stop takes its shape from one place

[ADR 0016](0016-agreement-is-not-understanding.md) made the runs stop for the user, and said what each question must carry. It did not say what a stop looks like. The user then found the rounds and the records hard to read, while the interview this set borrows from read clearly. The difference was the template: the upstream skill gives the literal shape of a question and words it so "yes" accepts the recommendation, and `grill-point` gave the content alone. 0.12.1 put a shape into `grill-point` itself.

The same gap sat at every other place a run talks to the user. On the 2569 final of a mathematics course, `make-exam` handed over its sketches — a stop the skill planned as keep, drop, or change on each row — and added five numbered decisions of its own: a notation for the paper, two items to cut, an item that stood only if a rule had been taught, a worksheet question the class may have met unanswered, and how to draw the circuits. Each carried a recommendation and a cost, as a grill round does, and none went through `grill-point`, so none of its shape reached them. A shape attached to the steps that were planned as stops misses the questions a run discovers along the way. The other stops carried no shape either: the plan every checklist shows before it acts, the approvals in `critique-mcq` and `make-exam`, the scorecard of `audit-brain`, and the interview of `init-brain`, which asks ten questions with a default each.

We decided four things.

**One clause in every checklist reaches the shapes.** Each checklist's opening paragraph is followed by one sentence, held identical by `_scripts/check.py`: a step that puts more than one decision to the user asks in the round shape `grill-point` gives, and an approval of items is asked in the approval table `assessment-layout` gives. It sits in the opening rather than at each stopping step because the stops nobody planned are the ones that went wrong. The shapes themselves live once, in the skills that own them, as [ADR 0007](0007-shape-is-shared-process-is-copied.md) allows for shape.

**An approval is a table, not a round.** Approving a rewrite, a calibration batch, or a paper's selection is judged item by item on the item's own numbers, so the user may answer the whole table at once. A grill round's "yes" answers only its own question, because there the user is still finding out what they want. A question a table raises that is about no single item is asked after it, as a round. Where the items already sit in a file built as rows — the sketches — that file is the table.

**The plan and the scorecard get shapes of their own.** The plan is the steps by number with a 🛑 on each one that will stop, then a line of what was found and a line of what was not; it lives in the plan clause, which `check.py` already holds. The scorecard is one table, one row per component, the same columns every audit, so one audit can be read against the last; only `audit-brain` writes it, so the shape lives there.

**`init-brain` takes the round shape, not the grill point.** Its answers go into the vault's `AGENTS.md`. A grill point would write the same answers again as decision records, and two copies of one answer drift.

## Considered Options

- **A shape at each stopping step** — rejected: the sketches' five questions were raised at a step no one planned as a grill.
- **The rule in the vault's `CLAUDE.md`** — rejected: it would bind one vault, and the skills are written to run in any ([ADR 0001](0001-generalize-skills-for-portability.md)).
- **The approval table in `grill-point`** — rejected: it would fold approval into the grill, the distinction CONTEXT.md keeps between the two.
- **The round shape for approvals too** — rejected: sixty items become sixty question blocks.
- **`init-brain` as a full grill point** — rejected for the duplicate answers above.

## Consequences

- All ten checklists carry the stop-shape clause, and the plan clause gains its shape; `check.py` holds both.
- `assessment-layout` carries the approval table; `critique-mcq` step 11 and `make-exam` steps 6, 7, and 12 name what goes in its middle columns.
- `audit-brain` carries the scorecard's table, and step 4 fills its *Outcome* column.
- CONTEXT.md defines **Round** and **Approval table**.
