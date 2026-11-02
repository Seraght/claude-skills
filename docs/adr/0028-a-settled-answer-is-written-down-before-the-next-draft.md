# A settled answer is written down before the next draft

During a grill in a knowledge vault, the user answered the first round of a rubric for a group presentation with an exception: "ยกเว้นหัวข้อ ใช้ Generative AI" — that criterion was not to be scored. About twenty-five minutes and several rounds later the agent rebuilt the forms by editing the existing build script, and the row `ใช้ Generative AI อย่างเหมาะสม + ระบุที่มา | 5` was still in it. The user had to say it again. A retro over 447 session logs ranked it fifth: a decision stated during a grill was lost, and a draft brought back what the user had rejected.

That run used another grilling skill, but `grill-point` had the same gap. Step 5 says back what was settled only at the end of the run, and step 6 writes a decision record only for an answer that outlives the artifact. An answer that shapes this artifact alone — "this rubric does not score GenAI use" — never becomes a record. Between the round that settles it and the step that writes it, the conversation is its only copy, and nothing compares a draft with it. A removal is the easiest to lose: it leaves nothing in the draft to remind anyone, and a file edited rather than written fresh still carries what it held before the grill.

We decided four things.

**Each round's answers are written down as the round closes.** `grill-point` appends every settled answer to a grill log, `GRILL-LOG-<skill>.md`, in the run's folder — where the calling skill writes its artifacts and its handoff — before anything else is drafted or edited. One row each: the step, round, and question; the decision, an exclusion opening with **Not:**; the user's words, quoted; and a last-checked cell. Artifact-local answers, answers that will also become records, and provisional values all go in. Decision records are unchanged: the log is one run's working memory, records are the memory across runs.

**The check lives in `grill-point`, once.** Before any draft built on the grill is presented, and again after every rebuild or edit of an existing file, the log is gone through row by row against the draft: each exclusion absent, each inclusion present, found by searching the draft's text. This is a deliberate exception to [ADR 0007](0007-shape-is-shared-process-is-copied.md), which copies process into each skill that performs it. Every caller already reaches `grill-point` by name at the step that grills, so its text is in context wherever a grill ran; a copy would have to go into seven skills now and every future caller, and the copy that is missing is the one that loses the answer. `check.py` holds that the rule is stated in `grill-point` and nowhere else.

**The check leaves evidence.** Each check rewrites the last-checked cell of every row it covered — date, file, `holds` or `fixed` — and the message presenting the draft carries "checked N logged decisions, fixed M". A check that leaves no evidence did not run ([ADR 0008](0008-a-check-that-leaves-no-evidence-did-not-run.md)).

**The log lives for one run.** Each caller's last step deletes it: in the five that write a handoff, in the sentence that deletes the handoff; in the others, in a sentence of its own. `check.py` finds the callers — a step marked as a grill point, or a decision put to the user "through the `grill-point` skill" mid-step — and holds each sentence identical. A skill that only borrows the round shape of step 3 runs no grill and keeps no log. The handoff clause now points to the log rather than copying settled answers into the handoff, which removes most of what [ADR 0020](0020-a-run-that-outlasts-a-session-leaves-a-handoff.md) called a decision "settled but not yet written anywhere".

## Considered Options

- **Copy the check into every caller** — rejected: seven copies, and one more per future caller, to hold identical for a rule that is already in context through `grill-point`, and a future caller that forgets the copy is the gap this closes.
- **Keep the log beside the artifact** — rejected: one step can write several artifacts, a grill can bind files written later in the run, and a blueprint is rewritten whole, taking anything appended to it along.
- **Keep the log after the run** — rejected: it would be a second copy of decisions that drifts from the artifact, and a later run on the same folder would check its drafts against answers given for another.
- **Log only exclusions** — rejected: an inclusion dropped by a rebuild is the same failure the other way round, and the row costs one line.
- **A check with no evidence** — rejected by ADR 0008.
- **Call it a decision log** — rejected: the name belongs to the decision record; CONTEXT.md defines **Grill log**.

## Consequences

- `grill-point` writes the log as each round closes and states the check the calling step owes; step 5's say-back reads from the log.
- `adopt-pool`, `analyze-results`, `audit-brain`, `critique-mcq`, `design-course`, `make-exam`, and `make-practical` delete the log in their last step; `check.py` fails a skill that gains a grill without that sentence.
- The handoff clause, held identical across five skills, names the grill log "where the run has one", since a critique grills only when a finding asks for a rule over the paper.
- ADR 0007 carries a note pointing to this exception.
- `assessment-layout` names the log, unnumbered, beside the handoff.
- The external grilling skill the incident ran on is not changed by this.
