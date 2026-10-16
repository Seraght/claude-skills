---
name: grill-point
description: Interview the user round by round at a skill's grill point until the decision is theirs and understood, then record what outlives the run. Use when another skill reaches a grill point.
---

# grill-point — interview before writing

A grill point is where a skill stops before writing an artifact that later work is built on, or one that needs facts only the user holds. It stops every time, even when every check has passed, because the decision belongs to the user. What the grill produces is **understanding**, not approval: a whole draft handed to someone who does not yet know what they want becomes the answer by default, and the "ok" that comes back is a verdict rather than evidence that anyone understood it.

This skill is a primitive. It runs from inside a step of another skill, it carries no discovery or closing check of its own, and when it ends, control returns to the calling step, which writes its artifact from what the grill settled. What the grill writes itself is only its own by-products: decision records, answers written back to the teaching constraints, the line that shows it ran, and the questions file of a grill nobody was there to answer. The shape of a decision record, where records live, and when one is written are in [DECISION-RECORD.md](./DECISION-RECORD.md) — read it before step 1.

**Facts are the agent's job; decisions are the user's.** Whatever the vault's documents answer — the syllabus, the programme outcomes, the teaching plan, the records below — is looked up and cited. What remains is put to the user, and the grill waits for the answer.

## Steps

1. **Read what is already decided** — the decision records at every scope the step reaches, and, where the step belongs to a subject, the teaching constraints in its overview: equipment, expertise, staff, and the learners — their programme, their background, what can realistically be expected of that cohort. Open the first round by listing the records that bind this step, one line each ("0003 still applies: CLO3 is assessed by a project"), so the user sees which past decisions are shaping this run. These are settled, so they are listed rather than asked; the user may reopen one, and a reopened decision becomes a new record that supersedes the old.
2. **Map the open decisions** — what this step must settle before its artifact can be written, less what step 1 settled and what the documents answer. A decision whose answer depends on another still open waits for a later round.
3. **Ask the frontier, one round at a time** — every ready decision in one round, numbered, each with a recommended answer, in the shape below. The first round opens with the records step 1 lists; after them, a round holds questions and nothing else. An assumption the agent would otherwise make goes in as a question whose "yes" accepts it, and a fact the agent checked that no question rests on goes into the artifact rather than the round, because every line set in front of the questions is one the user reads before reaching what they are asked. Each question:

   ```
   ❓ **Q1** - **<the decision, as a title>**: <the question, worded so "yes" takes the recommendation, the other options named where there are several>

   ➡️ <the recommended answer, in one line>
      Rests on: <the fit>
      Reason: <the reason>
      Alternatives: <option> — <what it would cost>, one line per option it beat
      Feasible?: <the feasibility question>

   ---
   ```

   The labels are written in the user's language. Word each question, its feasibility line included, so that "yes" accepts the recommendation and says it can be carried out: one word then answers both, and anything else the user writes is their own answer. A "yes" answers the question it is given to, never the round: where a round holds more than one question, a reply that does not say which it accepts is put back as the same round, asking for an answer against each number, because a go-ahead to the whole round says only that nobody objected. Ask the round as text in the conversation, never through a multiple-choice question tool: such a tool holds only a few questions a round and gives each option a single line, so the parts below run together into one sentence nobody can take apart. Every recommendation carries three things, the alternatives of its reason on a line of their own:
   - **Fit** — what it rests on, quoted or cited: the syllabus line or programme outcome for a course artifact, the anatomy component for a vault's layout, the statistics and the blueprint for an item decision.
   - **Reason** — the mechanism that makes it the better choice, and the options it beat with what each would cost.
   - **Feasibility** — a question to the user: can the people who will carry this out actually do it? For anything taught or assessed, that is this course's equipment, expertise, staff, and learners. Where the teaching constraints bear on it, cite them and ask whether they still hold and whether they settle it; write new answers back to them.

   Fit and feasibility are separate questions, even where one "yes" answers both: the feasibility line is always put to the user, never concluded. An outcome's level justifies a recommendation; whether these learners can reach it is something only the user can say. Wait for the answers, then recompute the frontier: settled decisions unblock the ones that depended on them.
4. **Turn "I don't know" into a choice** — offer two or three concrete options, each with what choosing it leads to ("a project → four studio sessions and a five-criterion rubric"). Where the user still cannot choose, take the recommendation as a provisional value and write it into the artifact as an open item carrying the vault's gap marker, where it stays visible until someone decides it.
5. **End when nothing is left open** — every decision the step needs is answered by the user, settled by a record, or written down as an open item — which later work may build on, since it is a decision made visible rather than one left unmade. Say back what was settled in a few lines and wait for the user to confirm it is what they meant. Then write one line into the artifact the calling step produces — the date, who was grilled, how many decisions, and the numbers of any records written — so a grill that ran can be told apart from one that was skipped. With nobody there to answer — a sub-agent, a scheduled run — write the round's questions into the work folder and stop there, so that nothing downstream is built on an artifact nobody decided.
6. **Record what outlives the run** — write a decision record for each answer that meets the tests in DECISION-RECORD.md. Every other answer shapes the artifact itself and is recorded there.
