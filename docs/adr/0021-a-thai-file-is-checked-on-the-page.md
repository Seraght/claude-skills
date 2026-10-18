# A Thai file is checked on the page

The 2569 final of a mathematics course was built into a Word file by a script the run wrote for itself. Under Thai distributed alignment the instructions came out with their first lines stretched letter by letter. The run traced it to a missing complex-script flag, added `<w:cs/>` to every run, saw the lines now reach the margin, and moved the paper to left alignment. The fix held, but not for the reason given: the script already wrote `compatibilityMode` 15 into its settings, and the flag only works alongside that. A second script carrying the same "lesson" without the setting fails again. And the check it used — lines reaching the margin — passes a broken page too, because Word's forced breaks inside a word reach the margin as well.

Bisecting against a file Word made itself showed the real rule: Word breaks Thai into words only with `<w:cs/>` on the text **and** a `<w:compat>` holding a compatibility mode of 14 or 15 (or `applyBreakingRules`). The evidence is in `skills/thai-office-files/DOCX.md`.

We decided four things.

**The knowledge is a reference skill in this plugin**, `thai-office-files`, reached by name from the checklists whose papers leave as Office files and model-invoked for everything else. It sits beside the Anthropic `docx`, `pptx`, and `xlsx` skills rather than replacing them: they build the file, this adds what Thai needs. It is true everywhere — Word behaves the same at every institution — so it travels with the skills ([ADR 0013](0013-true-everywhere-or-true-here.md)), and it lives in this plugin because its first readers, `make-exam` and `make-practical`, must not depend on a second install.

**A Thai file is finished when its rendered check passes**: the file is exported from the program its reader will use, and the line breaks are read and written down, one per paragraph style and table, twenty at least. Markup inspection checks only the causes already known, and Word's failure is an absence that reads as nothing until the rule is known. Where no Office program is present, the check is recorded as not run ([ADR 0008](0008-a-check-that-leaves-no-evidence-did-not-run.md)).

**A rule enters the skill only with a rendered test behind it.** The run's own lesson was half true and would have been written down whole. Other things believed about Thai in Office files — the complex-script font slot, bold and size twins, clipped marks under exact spacing — sit under *Untested* until a test moves them.

**PowerPoint and Excel are covered with the check and no rules.** Both broke Thai between words from default library output with nothing added; that is recorded there as tested on the default package, and whether either has conditions of its own is left untested.

## Considered Options

- **A memory note or a line in `CLAUDE.md`** — rejected: it stays on one machine, and the people this set is written for would never receive it.
- **A script that builds Thai `.docx` files** — rejected: it makes a runtime a prerequisite ([ADR 0002](0002-external-tools-are-accelerators-not-prerequisites.md)) and fixes every document's look for every user.
- **A separate plugin in the `seraght` marketplace** — rejected: a checklist that names a skill another install may lack fails without a word.
- **Rendering in LibreOffice where Word is absent** — rejected: it lays Thai out with its own engine, so a pass there says nothing about Word.
- **Word only** — rejected at the user's word: similar problems had been met in other formats, though none was recorded.

## Consequences

- `make-exam` and `make-practical` travel with a fifth skill, and each gained one sentence at the step that produces the paper. Where no Office program is present, that step closes with the check recorded as not run rather than waiting on it.
- `_scripts/check.py` holds the Word markup — `compatibilityMode`, `thaiDistribute`, `<w:cs/>` — to `thai-office-files`, so the rule has one home.
- The final already built stays left-aligned; it breaks correctly, and moving it to Thai distributed waits for its next build.
