# Stage the assessment set, and version what statistics attach to

The set gained a second assessment skill, and the layout the first one had carried as a private default (`assessment/<year>/<exam>/`, files numbered `00-` to `05-`) had to become something several skills could read and write without drifting apart. Watching a real exam cycle answered most of it, and contradicted part of what the skills already claimed.

The observed cycle is: write more items than the paper needs → select from them against the blueprint → edit the selected items for concision and reorder their options → print and administer → receive a per-item statistical report from the institution's analysis program. Two steps in that cycle were invisible to every artifact the set produced. Selection silently breaks the blueprint the marks were balanced against, and editing silently invalidates the item-writing checks that were run before it.

We decided the following.

**`assessment/` hangs under the subject's tree**, not at the vault root. An exam belongs to a subject and travels with it; filing by year first strands the papers when a subject moves.

**File numbers encode the lifecycle stage, not a sequence.** `0x` is authoring, `1x` is review before use, `2x` is after administration. Numbers are left unused inside each stage, so an artifact can be inserted without renumbering across stages, and a missing stage reads as a stage that did not happen rather than as a gap.

**The item bank sits beside the exam sets, not inside one.** A paper is an event that happens once; the bank outlives every paper. Filing items inside the exam that first used them turns reuse into copies with no original.

**The blueprint binds to the assembled paper, not to the pool of written items.** `make-exam` had claimed the finished bank matches the blueprint exactly, which is false whenever more items are written than the paper takes — and writing a surplus to choose from is the practice, not an accident.

**Statistics attach to an item *version*, not to an item.** An item is the question as a reusable thing; a version is one specific wording and option order; a paper is the list of versions administered on one occasion. Difficulty and discrimination are properties of the text people actually answered, so a value carried across an edit is worse than no value at all — it looks authoritative and measures something else.

**The layout's authority is the vault's `AGENTS.md`.** The skills carry the same shape as a skill default, which the vault overrides, per the pattern the whole set already follows.

**IOC is out of scope, permanently.** The observed review process is a committee reading the paper and reporting typos, ambiguity, and cueing — open-ended qualitative critique, which is what `critique-mcq` produces. IOC answers a different and narrower question, is not part of this process, and produces a number with no standing when an agent supplies the ratings itself.

## Considered Options

- **A shared layout file in the plugin** (`skills/_shared/ASSESSMENT-LAYOUT.md`) — rejected on ADR 0001's grounds: it creates a second authority competing with the vault's own rules, and it breaks the property that a skill folder can be copied out on its own and still work.
- **Keep numbering sequential** (`06-critique.md` after `05-rubric.md`) — rejected: adjacent numbers read as "the next step of the same chain", but `00`–`05` are a dependency chain that must not be reordered while a critique is a separate stage that may not exist at all.
- **Put the bank inside the exam folder that first used an item** — rejected: see above; also makes "which paper is this item's home" a question with no good answer once it is reused.
- **Attach statistics to the item and note the edit in prose** — rejected: prose does not stop the next reader from trusting the number.
- **Simulate a three-expert panel to compute an IOC value** — rejected: the arithmetic would be real and the inference worthless, and a fabricated validity index is worse than an absent one because it can be cited.
- **Make the vault the source of truth immediately and generate the Word paper from it** — deferred, not rejected. Import stays one-way (Word to vault) until the bank has enough in it to assemble from; the cost accepted is that the vault lags whenever the Word file is edited, which is why every imported version records the file and date it came from.

## Consequences

- `critique-mcq` runs on the final assembled paper as its binding pass, and reconciles the paper against the pool: items used unchanged, items edited after selection, and items written outside the set entirely. The third group has passed no check at all and is the highest-risk part of any paper.
- `critique-mcq` gains a paper-level pass, because selection and reordering produce defects that are invisible one item at a time: a blueprint that no longer balances, one item's stem answering another, and a key that no longer matches the option it points at.
- `make-exam` stops claiming the item pool matches the blueprint and moves that reconciliation to paper assembly.
- Two skills are deferred with their slots reserved: importing existing papers and their statistics into the bank (`2x` artifacts, `bank/`), and then post-administration analysis. The analysis program already computes and classifies per-option statistics, so the work is ingestion and routing, not calculation.
- Student-level data — names, identifiers, per-person scores — never enters the vault. Only item-level statistics and the number of examinees do. This is a gate in the sense `CONTEXT.md` defines: failing it stops the import rather than warning about it.
- `init-brain` gains one skippable interview question so a vault that does teaching work records this layout, and a vault that does not carries nothing extra.
