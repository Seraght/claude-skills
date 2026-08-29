# A verdict is not evidence

[ADR 0008](0008-a-check-that-leaves-no-evidence-did-not-run.md) established that a step producing no artifact cannot be shown to have run. The loophole it left is a step that produces a *verdict*: a tick, or the sentence "checked, none found". That looks exactly like a check that ran, and it is what a real paper was cleared on.

The evidence is one midterm of fifteen items, measured and then critiqued by this set. Where the check was naturally numeric it worked: option lengths went into a fifteen-row table with `len` per option, a spread, and a flag column, which found the key to be the longest option in nine items and drove nine rewrites. Where the check was a yes/no it collapsed. Nine of the Group A and Group B checks were recorded as one prose bullet each, every one of them reading "checked, none found". At least one was false: the stem of item 7 shares the string `สลับ` with exactly one option, which is the clang cue the taxonomy already names, findable by plain substring matching with no tokenizer. The critique that followed collapsed the whole measurement table into a **single row spanning items 1–15**, with self-containment marked as passing for all fifteen. Two items ended in "ตามที่สอน" and "ที่เรียนมา" verbatim. An independent second pass caught those two and reported the contradiction with the table; nothing caught item 7 at all.

The instruction is what produced this. `MCQ-CRITIQUE-REFERENCE.md` asked for the "**presence of** absolute terms, vague frequency terms…", and *presence* is a request for a yes/no. Its reporting rule bound only part of the work — "where a check is **numeric**, list every item that meets it" — which is precisely the set of checks that were already working. The checks that failed were never covered by the rule written to prevent this.

We decided four things.

**A check writes what it compared, not what it concluded.** The cell holds the matched span and what it was matched against — for item 7, `สลับ · option ข only · 1 of 4`; for self-containment, the phrases searched and where each was found. A cell that can hold a tick can hold a wrong tick, and nothing downstream can tell. A cell that must hold a span cannot be filled without looking.

**One item, one row.** A row spanning a range is a summary, and a summary is where a wrong value hides — the fifteen-item row above is the whole failure in one line.

**A critique measures for itself.** Reading a table built by the run that wrote the items carries that run's errors forward intact, and the saving is one pass over fifteen items. The critique that failed here announced its own defect in its table header: *"cited from `06-measurements.md` — not re-measured"*.

**The independent pass is a numbered stage.** `11-critique-independent.md` joins `10-critique.md` in the review stage. It is what found all three real defects, including the one about the measurement itself, and an artifact no checklist names does not happen twice.

## Considered Options

- **Add a tokenizer-free counting rule for clang cues in Thai** — rejected as the remedy, though kept as a clarification. The defect and its Thai marker were both already in `item-defects`; the check was not attempted at all, and the string that gives item 7 away is found by substring matching. Treating this as a language problem would have left the other eight bullets untouched.
- **Ban the phrase in `_scripts/check.py` and stop there** — rejected. `check.py` reads this repo's skill files and never the artifacts an agent writes into a vault, so it can hold the instruction in place but cannot enforce the output. It is the second half of the fix, not the first.
- **Re-measure only items that were edited after selection** — rejected: provenance already covers that case, and the failure here was a wrong value on items nobody had touched.
- **Leave the independent pass ad hoc** — rejected: it exists in the vault because one session invented it, and the review stage's default file list is what makes a stage recur.
- **Split the measuring step into its own skill** so the critique cannot see the earlier table — rejected for the reason [ADR 0006](0006-how-a-skill-is-reached-and-when-it-is-split.md) rejected splitting `critique-mcq` at its approval wall: hiding later steps needs a real context boundary, and a second numbered artifact achieves the same thing by publishing both tables side by side.

## Consequences

- `_scripts/check.py` gains three banned wordings and one paired instruction. The banned list now carries a phrase in Thai as well as English, since the artifacts these skills produce are written in the vault's language.
- The review stage has two default files, and `critique-mcq` closes with an unticked item naming the pass that has not happened — the same mechanism `make-exam` already uses to hand off to `critique-mcq`.
- `critique-mcq` step 4 loses the option to inherit a measurement table. The cost is one extra pass per critique; the pass it replaces was the one that certified a wrong value.
- ADR 0008 is not superseded. Its rule stands and this one narrows it: the artifact has to be a measurement, and a verdict is not one.
