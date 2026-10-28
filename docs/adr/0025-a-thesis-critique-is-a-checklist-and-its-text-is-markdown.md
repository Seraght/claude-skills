# A thesis critique is a checklist, and its text is Markdown

A user who sits on undergraduate thesis committees critiqued six theses in a month, each in its own session. Three of those sessions opened with the same pasted instruction, word for word: critique the whole book "like the earlier group", read it as text rather than images, summarise in the chat before building the Word file with a named template script, save it beside the earlier ones, and put no student's name or ID in it. Each of those runs finished on that one prompt, with no correction from the user.

They finished because the process lived somewhere the agent read: a memory note, grown run by run, holding the output folder, the file name, the template, the report's sections, and a list of checks that had each found a real defect — percentages that did not add up, a standard deviation larger than its scale allows, DOIs that were never registered, references whose journal issues held other articles. The memory was later switched off. The process had no other home, and the pasted instruction carried only the part the user remembered.

The template script carried the first thesis's critique as code. Each later run copied lines 1–55, wrote its own critique as JavaScript calls, and copied lines 210 onward. It also built every Word file without Thai's complex-script flag, and the files went to students that way.

We decided four things.

**Thesis critique is a checklist of its own, `critique-thesis`.** [ADR 0006](0006-how-a-skill-is-reached-and-when-it-is-split.md) splits by how a skill is reached, and this is reached by a thesis arriving, not by a paper or a pool. Its output is a document others are assessed by, so it joins the teaching-and-assessment group. The run that checks a revised thesis against its earlier critique is a branch of the same checklist, not another skill: it reads the same book with the same checks and adds one table.

**The checks travel with the skill; the paths stay with the host.** Under [ADR 0013](0013-true-everywhere-or-true-here.md) the checks are true everywhere — the Bhatia–Davis bound, back-solving n from r and p, the DOI handle and Crossref lookups — and go into `THESIS-CHECKS.md`, generalised from the discipline they were found in. The folder, the file name, the renderer, and the institution's criteria are true here and go into the host project's constitution, which step 1 reads.

**The critique's text is a Markdown file, and the Word file is rendered from it.** A script that carries the text is the failure [ADR 0022](0022-a-contributed-pool-is-adopted-then-critiqued.md) named for exam items: the text is lost with the session, and a correction means another script. The renderer is the host's, since the layout is one institution's form; the skill says where the text lives and that the Word file is rendered from it.

**The summary in the chat is an approval stop, not a grill point.** The user can judge a finding with its page and evidence on its own, which is what [ADR 0016](0016-agreement-is-not-understanding.md) reserves approval for; nothing is built on the summary that a rejected finding would invalidate except the file itself.

## Considered Options

- **Keep the process in the memory note** — rejected: it was switched off, it loads on one machine only, and nothing checked it.
- **A paragraph in the vault's constitution holding the whole process** — rejected: it would load on every session in the vault for a task a few sessions do, and the checks are not the vault's to keep.
- **Fold it into `critique-mcq`** — rejected: that skill measures items against a defect taxonomy; a thesis has no items and its checks are of a different kind.
- **Keep the template and splice its lines** — rejected for the reasons above, and because the splice points moved whenever the template did.
- **Read a scanned page as an image when the text layer is missing** — rejected: the user stopped an image-by-image read for misreading a surname, and a page with no text is usually a certificate the user can check faster than the agent can.

## Consequences

- `critique-thesis` needs `grill-point` and `thai-office-files` beside it when copied alone.
- `check.py` requires the Markdown-and-render sentence of `critique-thesis` by name.
- Testing the renderer showed that docx-js 9.15 writes compatibility mode 15 but not `<w:cs/>`, and that its Thai breaks inside words until the flag is added to the document defaults. `thai-office-files` records the test; the host's renderer adds the flag.
- Critiques already sent were built without the flag. Their text is spaced between phrases, so most lines break at a space: the rendered check of one found no break inside a word in 200 line ends. They are left as sent.
