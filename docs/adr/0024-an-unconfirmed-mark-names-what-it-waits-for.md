# An unconfirmed mark names what it waits for

A digest of six lecture decks closed with its claims sorted into checked and unconfirmed, and its closing report said the unconfirmed ones were marked in each file — a historical account, repository figures, the year of a paper. The user's next message asked whether the agent could check those itself or whether the user had to. The second run checked nearly all of them with the same tools the first had: paper abstracts, Crossref, the repositories, and recomputation from the datasets the slides named. It found seven points to correct or qualify. One was a figure already in the vault from an earlier import: a top-5 error of 18.9% that the paper's own abstract gives as 17.0% on one test set and 15.3% on the competition the sentence was about. What it could not settle came to about eight claims, each for a reason it could name — a tool the machine did not have, a page that refused automated fetches, a book.

The mechanism is the completion criterion. Step 11 confirmed structure only: staging empty, every new file indexed, no broken links. The host vault's own rules allow a claim to be marked unconfirmed, so marking one satisfied every rule in sight, and the mark cost less than the fetch. Nothing distinguished a mark the run could not clear from one it had not tried to, and the report gave the user no way to tell them apart either: both read "unconfirmed". The cost of a mark landed on the user, who had to know to ask, and the earlier import's wrong figure would have stayed until someone did.

We decided two things.

**A mark is cleared where one fetch or one recomputation clears it.** Step 10 checks each claim the digest would mark unconfirmed against its source before writing the mark, in every file the run writes or edits, so marks earlier imports left in a file being edited are reached too. The bound is one fetch or one recomputation: the cited abstract, the repository, the dataset the source names. That is the class the second run cleared.

**A mark left standing names what it waits for.** The reason is written beside the mark — a tool to run, a page that refuses fetches, a book to open — and step 11 confirms every remaining mark carries one. This follows [ADR 0008](0008-a-check-that-leaves-no-evidence-did-not-run.md): a bare mark is the shape a check that never ran leaves, and a mark with its reason is evidence the check was attempted and what stopped it.

## Considered Options

- **Check every claim in the digest** — rejected. A lecture digest carries hundreds of claims, most restating the source faithfully; the defect was in the claims the run already suspected, which is the set it marks.
- **Put the rule in the host vault's constitution** — rejected. It would load on every turn of every task to serve one step of one skill, and a vault adopting this skill would not inherit it.
- **Report the marks to the user and let them choose** — rejected. That is what happened; the user's answer was to ask the agent to do it, and the second run showed the agent could.
- **Name a vault's label (`[ต้องยืนยัน]`) in the step** — rejected by [ADR 0013](0013-true-everywhere-or-true-here.md): labels are the host project's; "a claim the digest would mark unconfirmed" reaches any of them.

## Consequences

- `digest` step 10 checks before it marks, and step 11 confirms each remaining mark names what it waits for.
- A digest run spends more fetches. The second run here took about fifty tool calls; it is the cost of the user not having to ask.
- `_scripts/check.py` pairs `would mark unconfirmed` with `this run lacks`, so a reworded step keeps its reason requirement.
- `new-subject` is unchanged: it digests the subject's own defining document, whose claims are about the subject itself and have no further source to check against.
