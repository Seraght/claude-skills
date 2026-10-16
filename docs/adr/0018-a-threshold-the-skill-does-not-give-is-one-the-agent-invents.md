# A threshold the skill does not give is one the agent invents

[ADR 0016](0016-agreement-is-not-understanding.md) moved the decisions upstream. This one is about what happened downstream of the blueprint on the same paper — the 2569 networking final — where the check that [ADR 0008](0008-a-check-that-leaves-no-evidence-did-not-run.md) and [ADR 0012](0012-a-verdict-is-not-evidence.md) built *ran*, left its table, and still let the paper through.

Comparing the 60 items `make-exam` wrote with the 60 the user actually set, by character-level similarity of stem and options: 16 were used as written, 9 kept their stem with new options, 15 were reworded, and 20 were replaced. The direction of the edits was the same across the paper. Median stem length fell from 168 characters to 108, median option length from 61 to 32, and the options carrying an explanation — a "because", a dash, a parenthesis — from 123 of 240 to 14. The user had been taking the skill's items to other models to be shortened before they could be used.

The measurement table explains it. The taxonomy said the key "is longer" than the distractors and gave no number, so the run set its own: a key at least 1.5 times the longest distractor and 15 characters longer. Under that bar it flagged 18 items, repaired 9, and passed a paper whose key was the strictly longest option in 39 of 60 items — an examinee who always picks the longest would have scored 65% where guessing scores 25%. The repair it chose was to *add a reason to every distractor* so the lengths evened out, which the taxonomy already named as a repair that creates a defect: "padding distractors to match the key's length makes them implausible — trim the key or move text into the stem instead." The check produced evidence; the criterion inside it was the agent's own, and so was the remedy.

Two more things came out of the same paper. Every item was written before any was measured, so a habit that went wrong went wrong sixty times before anything noticed. And the shared-scenario items each retold their scenario, because the taxonomy's only sentence about such sets — each item "has to be answerable on its own" — was read as *each stem must carry the context*. The user's own 2568 database papers show what was wanted: a table, a schema, or a query with blanks set once, then three to six short items asking different things of it — 17 of 43 items on the final, with a median stem of 60 characters.

We decided five things.

**The skill gives the threshold.** Every item whose key is the strictly longest option is flagged, with no ratio. A flag means *look*, not *change*: fixing every flagged item would leave no key longest anywhere, and a paper where the longest option is never right hands the examinee the opposite rule and a one-in-three guess. So the paper carries the number. The share of items whose key is the longest — what the always-pick-the-longest examinee scores — stays within ten percentage points of one in the number of options, 15–35% on four options. Flagged items whose key is longest because of a qualifier or teaching language are always changed; the rest are changed only as far as the band requires, and the running share is kept while the items are written. The band is our working rule, not a published one; it is about twice the swing a randomly keyed 60-item paper shows anyway. On the networking final it would have required at least 18 of the 39 to change. The table records how each repaired item was repaired, so padding is visible, and a key that no repair keeps true stays flagged rather than padded.

**Items are measured as they are written, not after.** Each item is checked against the style budget and the key's length before the next is started; the whole-set measurement stays as the closing check.

**The user chooses the content before any option is written.** After the blueprint, the run sketches one row per item into a sketches file of its own — the cell, the stem in draft, the correct answer as an idea, why it is worth asking, the session that taught it — and the user keeps, drops, or changes each row. The answer stays an idea because writing the key before its distractors is what makes it the longest. Then one cell is written as a calibration batch and shown with its measurements, so wording, difficulty, and distractors are settled on five items, and the batch's rows and the user's changes go into the measurement table as they happen. At assembly the user chooses the paper's items with the measurements of exactly those items in front of them. All three are approvals rather than grill points: a one-line sketch and a measured item can each be judged on their face.

**Items are written to the user's own papers.** The style budget — stem and option length, explanations in options, the share of items in stimulus sets — is proposed at the blueprint's grill from the papers the subject, or the nearest subject, has actually set. The lengths differ by subject, 60 characters for the database stems against 108 for the networking ones, so they are a subject decision; the rules — explanations in options, material rather than narrative, the share of items in stimulus sets — hold across the vault.

**A stimulus set is a shape, and independence is about answers.** The stimulus is material to work on rather than a story, appears once, and is stored in the bank as a file of its own that its items name, since it outlives every paper. Items in a set share their material and never their answers. A stimulus is part of the version of every item answered from it.

Two smaller rules follow. An item has versions only once it has been sat, so before that the items file holds current text alone: an edit replaces, a dropped item is deleted, a kept item the paper does not take goes to the bank. And where the agent can start a sub-agent with a fresh context, the independent critique runs there on the assembled paper instead of waiting as an unticked line — on the networking final it never ran at all.

## Considered Options

- **Keep the ratio and tighten it** — rejected: any ratio passes the items just under it, and the examinee's strategy has no threshold; it picks the longest.
- **Change every flagged item** — rejected: the share falls to zero and the cue reverses; the user chose the band instead.
- **The band alone, no per-item flag** — rejected: nothing would mark an item while it is being written, which is when it is cheapest to change.
- **Measure only at the end, more strictly** — rejected: it finds sixty instances of one habit after all sixty are written, which is the rework the user described.
- **Show finished items for approval instead of sketches** — rejected: a full item costs the writing before a rejection, and showing a key before its distractors exist means writing it first.
- **A single vault-wide style budget** — rejected: the subjects' own papers differ by nearly half in stem length.
- **Allow a one-item "set"** — rejected: a stimulus serving one item is that item's stem, and calling it a set hides the reading load.

## Consequences

- `make-exam` goes from eleven steps to thirteen: sketches at 6, the calibration batch at 7, the remaining items at 8.
- `item-defects` carries the per-item record and the repair rule in Group A, the paper-level share and the stimulus told once in Group D, and states that a set hinged on another item's answer is a hinged item. `critique-mcq` measures the longest option and the share.
- `assessment-layout` carries the stimulus-set block, the `stimuli/` folder in the bank, `07-sketches.md`, when a version begins, and that a banked item takes its key and rationales with it.
- The reference gains *write to the papers this user has set* and a section on stimulus sets.
- Writing is slower per item. The cost is paid once per item instead of once per rewrite.
