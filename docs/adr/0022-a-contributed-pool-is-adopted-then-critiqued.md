# A contributed pool is adopted, then critiqued in a new session

A course's 2569 final was written by the instructor who taught it, not by the vault's owner: fifty multiple-choice items, no slides, to be cut to forty-five and brought to the vault's standard. Two sessions worked on it.

The first was asked to "assess it against our criteria in order to import it". No skill fired: the request did not read as `critique-mcq`'s "hands over a paper to check", and "import" is the word `digest` answers to. The run improvised an exam set — research, blueprint, items, paper — and inferred the blueprint from the course outcomes, which `critique-mcq` step 2 tells a critique not to do. It stopped at 628K tokens of context when the user said it was full, and wrote its handoff into the session's scratch folder, where no later session would look.

The second ran six jobs in one context: harmonising the wording with another course's paper (150K tokens before any skill was named), `critique-mcq`, writing replacement items for the levels the pool lacked, a Word file for the external reviewer, the user's own review of that file, and a second Word file. It reached 714K tokens and stopped on the plan's usage limit, not the context window. 353 requests averaged about 408K tokens each: 144M tokens read from cache, 5.8M written to it, 0.9M of output. Two cache rewrites of 352K and 627K followed the host dropping old thinking blocks, and typing `resume` after the limit reset rewrote 632K more. The run wrote 28 scripts into its scratch folder, about 250K characters of tool input, many of them carrying the items' Thai text, and the previous session had written its own `measure.py` and document builder the same way.

Three things went wrong, and none of them is a long skill. The work had no skill to enter by. A critique that [ADR 0020](0020-a-run-that-outlasts-a-session-leaves-a-handoff.md) expected to run in a fresh context ran as the fourth job of a long one, with no handoff to end it at. And the cost of every revision was set by the size of the context it ran in, which was set by everything done before it.

We decided seven things.

**A contributed pool has its own checklist, `adopt-pool`.** [ADR 0006](0006-how-a-skill-is-reached-and-when-it-is-split.md) splits skills by how they are reached, and this is reached differently from both neighbours: `make-exam` starts with no items, `critique-mcq` starts with an assembled paper, and this starts with someone else's items and ends with an exam set ready for review. It keeps the pool word for word in `08-contributed.md`, fixes the blueprint, maps and selects the pool against it, writes items for the empty cells, brings the wording to the house style, and stops. A checklist may reach reference, never another checklist, so it ends by recording the review as an unticked item and handing the user the line that starts `critique-mcq` in a new session. Its scope is written papers; a practical stays with `make-practical` ([ADR 0011](0011-a-practical-is-a-different-chain.md)).

**The blueprint comes from the outcomes, even when the items came first.** A table read off the pool certifies the pool's proportions instead of checking them: built that way, the paper that had no item at the application level would have had a blueprint with no such cell. So the blueprint is settled at a grill point from the outcomes' weights and the teaching plan before any contributed item is placed, and the cells left empty are the gaps. CONTEXT.md now says a blueprint precedes the first item *selected or written*.

**Harmonising changes wording, not what is tested.** The vault's owner did not teach the course, and keeps the contributor's content so that nothing on the paper is something the class was never taught. An item whose repair would change what it tests is cut or replaced through the user, not rewritten in place. The house style comes from the vault's decision records and an exemplar paper the user names; a style rule found during the run that should hold for every paper is settled at a grill point and recorded.

**`critique-mcq` joins the checklists that write a handoff.** ADR 0020 left it out because it "already runs as a pass in a fresh context by design", and said it would join once a run was seen to outlast a session. Both sessions here are that run. It now carries the three clauses `check.py` holds identical, and its approval stop at step 11 is where a session ends.

**A reviewer's findings enter `critique-mcq` at triage.** The user's own review of the Word file, and the external reviewer's, are findings like the passes' own: each quotes the span it is about, goes into the same approval table, and every item it changes is re-measured. A finding that asks for a rule over every item — order the options by length — is a decision for the vault, settled at a grill point before it is applied. Where no item has changed since the last pass, its measurement table still stands and the run goes straight to triage.

**Scripts outlive the session that wrote them.** A measuring or building script is run from where the vault keeps its scripts, or saved there when written, and an item's text is changed in the items file rather than in a script that regenerates it. The skills say this in a sentence each; the scripts themselves belong to the vault, since a document builder is one institution's form ([ADR 0013](0013-true-everywhere-or-true-here.md)).

**The rendered check runs in a sub-agent where the host has them.** The page images and the evidence table are written beside the file and only the failing breaks come back, so thirteen page images do not ride in the building run's context for every later turn. The evidence stays on disk, which is what [ADR 0008](0008-a-check-that-leaves-no-evidence-did-not-run.md) asks of it.

## Considered Options

- **Extend `critique-mcq` to build the exam set when none exists** — rejected: a critique changes nothing until the author approves, and building a blueprint and an items file before approval breaks that; step 2's refusal to infer outcomes would have to be reversed for one case.
- **A mode of `make-exam` for items that already exist** — rejected: it would skip the sketches and the writing steps that are most of the chain, and two invocations in one file is what ADR 0006 splits.
- **Widen `critique-mcq`'s description only** — rejected: the harmonising and the blueprint would still have no home, and the first session's job was not a critique.
- **Read the blueprint off the pool and call it a coverage map** — rejected: it cannot show a gap, and every skill downstream reads a blueprint.
- **Call the pool a source paper** — rejected: a paper is a sitting that happened, and this one has not; CONTEXT.md defines **Contributed pool**.
- **A separate skill for reviewer feedback** — rejected: its output is the same findings, approval, and re-measurement as `critique-mcq`.
- **Ship the scripts in the skills** — rejected: what is generic in them is short, and what is long is one institution's document form.
- **Warn on context size from inside the skills** — rejected for the reason in [ADR 0018](0018-a-threshold-the-skill-does-not-give-is-one-the-agent-invents.md). The host-side signals — a hook that lists open handoffs when a session starts, a status line that shows the context size — live in the vault's own configuration, outside this set ([ADR 0002](0002-external-tools-are-accelerators-not-prerequisites.md)).

## Consequences

- `adopt-pool` joins the teaching-and-assessment group; `assessment-layout` names `08-contributed.md` in the authoring stage and `adopt-pool` among the skills that fill it.
- `check.py` adds `critique-mcq` and `adopt-pool` to the checklists that carry the handoff clauses, and `adopt-pool` to those that carry the approval exception.
- ADR 0020's exclusion of `critique-mcq` is superseded; the rest of it stands.
- A resumed critique still re-reads its report and measurement table, about 40K–60K tokens — far less than a revision run at 450K.
- The scripts left in the second session's scratch folder are tied to that exam set's paths; making them general is work for the vault, not for this set.
