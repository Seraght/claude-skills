# An unchecked mark names the source it tried

A digest of six lecture decks closed with its claims sorted into checked and unchecked, and its closing report said the unchecked ones were marked in each file — a historical account, repository figures, the year of a paper. The user's next message asked whether the agent could check those itself or whether the user had to. The second run checked nearly all of them with the same tools the first had: paper abstracts, DOI records on Crossref, the repositories, and recomputation from the datasets the slides named. It found seven points to correct or qualify. What it could not settle came to about eight claims, each for a reason it could name: a tool the machine did not have, a page that refused automated fetches, a book.

One of the seven sat in a file an earlier import had written. It gave AlexNet's top-5 error as 18.9%, recorded as checked against the paper's abstract page; the sentence beside it, that the model won its competition by a large margin, carried the vault's unchecked mark. Settling that sentence meant opening the paper itself, whose abstract gives 17.0% on one test set and 15.3% on the competition the sentence was about — so the figure next to the mark was wrong as well, and was corrected only because the mark led to the primary source.

The mechanism is the completion criterion. Step 11 confirmed structure only: staging empty, every new file indexed, no broken links. The host vault's own rules allow a claim to carry an unchecked mark, so marking one satisfied every rule in sight, and the mark cost less than the fetch. Nothing distinguished a mark the run could not clear from one it had not tried to, and the report gave the user no way to tell them apart either. The cost of a mark landed on the user, who had to know to ask.

We decided three things.

**The check opens the primary source.** Before writing an unchecked mark, and for each one already in a file the run edits, the run opens the source the claim rests on — the cited abstract or its DOI record, the repository, the named dataset recomputed — not the document being digested, which is where the claim came from and so always agrees with it. The rule is the attempt, not a forecast of whether it would succeed: the run cannot know a fetch settles a claim until it has made it.

**A settled claim is written as its source gives it.** The check exists to correct, and seven corrections came out of it here; a check that clears the mark but leaves the slide's wording in place has done half its job.

**A mark left standing names the source tried and what stopped it** — the address that refused the fetch, the tool the machine lacks — or, where no source can be reached, the source it would need. Step 11 confirms each remaining mark in the files the run wrote or edited carries this. A reason such as "needs the book" is a verdict, which is what [ADR 0012](0012-a-verdict-is-not-evidence.md) says a check must not write: naming the address that refused is what the run compared, and it is what [ADR 0008](0008-a-check-that-leaves-no-evidence-did-not-run.md) asks a check to leave behind.

## Considered Options

- **Check every claim in the digest** — rejected. A lecture digest carries hundreds of claims, most restating the source faithfully. The AlexNet figure shows the cost of the bound chosen: a claim wrongly recorded as checked is reached only when a mark nearby leads to the same source. Re-checking every claim in every file a run touches would reach it directly, at a cost of every import re-verifying the vault around it.
- **Put the rule in the host vault's constitution** — rejected. It would load on every turn of every task to serve one step of one skill, and a vault adopting this skill would not inherit it.
- **Report the marks to the user and let them choose** — rejected. That is what happened; the user's answer was to ask the agent to do it, and the second run showed the agent could.
- **Name a vault's label (`[ต้องยืนยัน]`) in the step** — rejected by [ADR 0013](0013-true-everywhere-or-true-here.md): labels are the host project's. "Whatever label the host project gives a claim not yet checked against the source it rests on" reaches any of them, and a run cannot dodge the step by choosing another label for the same state.

## Consequences

- `digest` step 10 opens the primary source before writing an unchecked mark, writes a settled claim as its source gives it, and names the source tried on every mark it leaves; step 11 confirms the last.
- `CONTEXT.md` gains **Unchecked mark**, set apart from **Gap marker**: one marks text written but not checked, the other text not yet written.
- A digest run spends more fetches. The second run here took about fifty tool calls; it is the cost of the user not having to ask.
- `_scripts/check.py` checks `digest` by name for both clauses, since a pairing keyed on a trigger phrase stays green once the trigger is reworded away, and pairs `unchecked mark` with `the source tried and what stopped it` for any other skill that adopts the term.
- `new-subject` is unchanged: it digests the subject's own defining document, and every fact in it comes from that document.
