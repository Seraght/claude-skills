# A run that outlasts a session leaves a handoff

The 2569 final of a mathematics course was built with `make-exam` in one session. The session reached steps 7 and 8 at 473K tokens of context and stopped at 680K, with the answer key, the paper, and the review still to do; the user asked for a handoff, and the run invented one, `HANDOFF.md`, in the exam set folder. Nothing in the skill told it to, or told the next session to read it.

The growth was not waste that a tighter skill could remove. Of the 680K, 369K was the model's own output — thinking, and the text it wrote into files — and all of it stays in context for every later turn: the turn that wrote the sixty items produced 47,389 output tokens, and the next request's context grew by 47,553. Thai costs several times more tokens per character than English, and the run writes four files of 17K–23K characters each. Steps 1–6 alone took about 250K; writing sixty items with their rationales takes 150K or more. A complete written exam does not fit reliably in one session, whatever the skill says.

What the skill can change is what happens at the boundary. Every planned stop already leaves the whole state of the run in files — the blueprint, the sketches, the items, the measurements — so a stop is a place a session can end at no cost, if the next session knows where to pick up.

We decided four things.

**Every planned stop writes a handoff.** Each of the three checklists whose runs outlast a session — `make-exam`, `make-practical`, `design-course` — carries one clause, held identical by `_scripts/check.py`, after the stop-shape clause: every step the plan marks 🛑 writes `HANDOFF.md` into the run's folder before it stops, and the stop ends with one line telling the user that the session can be closed and giving the line that resumes it. Written at every stop rather than when the user asks, because the user who has to notice that context is running out is the failure this decision is about, and a session that crashes leaves nothing.

**The handoff holds only what no other file does.** The next step by its number, the questions waiting on the user, what the run learned that none of its files records, and the files to read first. Decisions are pointed to rather than copied: the invented handoff copied the blueprint's decisions into a section of its own, and two copies of one answer drift apart — the reason [ADR 0019](0019-every-stop-takes-its-shape-from-one-place.md) kept `init-brain`'s answers out of decision records. It is rewritten whole at each stop.

**Step 1 resumes.** Where the run's folder holds a handoff, the discovery step reads it before the run's other files and starts at the step it names. Where the folder holds the skill's files but no handoff — an older set, or a session that ended before writing one — it infers the step from which files exist and says so. Either way the plan marks the finished steps and waits for the go-ahead, because a resumed run is the moment the user remembers least of what was left ([ADR 0016](0016-agreement-is-not-understanding.md)).

**The last step deletes it.** Once whatever is still open is written into the run's own files — for an exam set, the unticked items of its closing check — the handoff has nothing left to say. Pointing it at the review stage instead would leave a file that `critique-mcq` never updates, saying "next: review" after the review is done.

`assessment-layout` names the file and leaves it unnumbered: the leading number is the lifecycle stage, and a handoff spans stages.

## Considered Options

- **Leave it to the user** — rejected: the user had to notice the context and ask, and each improvised handoff takes a different shape.
- **Rely on the host's context compaction** — rejected: a compaction summary is lossy, the skill cannot trigger it, and it exists in one host; the skills run in any ([ADR 0002](0002-external-tools-are-accelerators-not-prerequisites.md)).
- **Write the items in sub-agents, one cell each** — rejected: it would save perhaps 60K–90K tokens a set, but each writer starts cold, the style drifts across batches — the drift the calibration batch exists to stop — and the running longest-option share has to be stitched across agents. With a session boundary after the sketches, steps 7–13 start near 100K and end near 300K anyway.
- **Have the agent measure its own context and warn at a threshold** — rejected: an agent in another host cannot see its context, and a threshold the skill does not give is one the agent invents ([ADR 0018](0018-a-threshold-the-skill-does-not-give-is-one-the-agent-invents.md)).
- **A section at the end of `01-blueprint.md`** — rejected: the blueprint is the largest file in the set and is rewritten when the paper is reconciled, so the next session would read all of it to learn where it stands, and transient state would sit beside settled decisions.
- **A numbered file such as `08-progress.md`** — rejected: the number would claim a stage the file does not belong to.
- **The clause in all ten checklists** — rejected: `digest`, `new-subject`, and `update-portfolio` end in one session, and would carry a rule they never use.
- **`make-exam` alone** — rejected: `make-practical` is the same chain shape ([ADR 0011](0011-a-practical-is-a-different-chain.md)), and two siblings that diverge on this would diverge further. Its inclusion, and `design-course`'s, rests on the mechanism rather than on a run seen to fail.

## Consequences

- `make-exam`, `make-practical`, and `design-course` carry the handoff clause after the stop-shape clause, and the resume sentence in step 1 just before the plan; `check.py` holds both, and holds that no other skill carries the clause.
- `make-exam` and `make-practical` step-final wording that spoke of "a handoff" to the review stage now speaks of a review passed on, so the word has one meaning; CONTEXT.md defines **Handoff**.
- `assessment-layout` lists `HANDOFF.md` as an unnumbered file in an exam set.
- The thinking a run produces is not touched by any of this; a session's effort level is the only control over it.
- A resumed session still re-reads the files the handoff lists — about 40K–50K tokens for an exam set at step 7 — which is the price of a fresh context.
