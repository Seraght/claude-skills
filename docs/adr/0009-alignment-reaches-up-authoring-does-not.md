# Alignment reaches up; authoring does not

`make-exam` step 3 read the syllabus for three numbers — the learning outcomes, the grade weighting, the teaching hours — and took all three as given. Nothing checked whether the outcomes were fit to be assessed, and nothing looked at the teaching plan or the programme outcomes at all. The skill owned the third leg of constructive alignment and was blind to the first two.

What that costs is visible in a real practical exam set in the author's own vault. Its outcome reads *"**สร้าง**สื่อดิจิทัลด้วย Generative AI พร้อม**ตรวจสอบ**ความถูกต้อง…"* — two verbs, at two cognitive levels, in one outcome. The exam that serves it has two tasks that share nothing: different levels, different permitted use of AI, different scoring methods, and a mark split that gives sixty per cent to the subordinate clause. The paper is skilfully made and reads wrong, and it reads wrong because no single coherent paper can serve an outcome that is two outcomes. The author felt it without being able to name it. The rule that would have named it was already written down, in that same vault, in a thirty-second checklist: *one verb per outcome*.

**The outcome is an input to be checked, not a given.** Step 3 now reads the outcomes, the teaching plan, and the programme outcomes the course is mapped to, checks each outcome for a single observable verb with teaching hours behind it, and **stops and asks** where one fails. A malformed outcome is cheap to fix before the blueprint and impossible to fix after the paper.

**Reading upward is not the same as authoring upward.** The programme outcomes exist as documents already; reaching them costs a path. Designing them is a committee process with mandated forms, and a skill that generated them would be overridden every time. So the reach goes all the way up and the authoring stays where it is — for now.

**The blueprint cell carries the item format.** A format decided at writing time is decided by what is quickest to write, which is always the selected-response item; a Create-level cell filled with multiple-choice items leaves its outcome unassessed while the totals still reconcile. This is the same argument the skill already made for fixing the blueprint before the items, applied one level down, and it is what gives per-format item guidance something to attach to.

## Considered Options

- **Build the upstream skills now** — one that designs course outcomes and the teaching plan, one that designs programme outcomes — rejected as scope: they are new capability, not repair, and the repair is what the evidence demanded. Queued instead, in order: outcome-and-teaching-plan design next, practical-exam design after it.
- **Leave step 3 as it was and check alignment during review** — rejected: by review the items exist, and the finding is that the blueprint they fill serves a broken outcome. Everything downstream is then rework.
- **Add a third dimension to the blueprint table** for item format, rather than putting format inside the cell — rejected: a three-dimensional table is unreadable on paper and two tables must be reconciled against each other, which is one more place to drift.
- **Narrow `make-exam` to written exams immediately**, since a practical exam's chain differs at five of its eleven steps — its blueprint is an alignment matrix, it has tasks rather than items, its answer key is largely a proctor manual, and its rubric needs marker calibration. Correct, but rejected *as timing*: the replacement does not exist yet, and removing a capability before its successor lands leaves practical exams served by nothing. `make-exam` keeps them until the practical-design skill ships, and narrows then.

## Consequences

- `make-exam` step 3 can now halt the run. It is the first step in the set that stops on the quality of an input rather than on its absence.
- The blueprint's shape moves to the `assessment-layout` skill, where the two skills that read and write it can share one definition — it had been living in `make-exam`'s private reference while `critique-mcq` reconciled against it, the third instance of the drift [ADR 0007](0007-shape-is-shared-process-is-copied.md) was written from.
- [ASSESSMENT-REFERENCE.md](../../skills/make-exam/ASSESSMENT-REFERENCE.md) gains *Outcomes come first*: constructive alignment, and the rules that decide whether an outcome can be assessed at all. It is deliberately thin — the standards a country or an institution imposes belong to the vault, which overrides it.
- Two blocks of work are queued rather than done: **outcome and teaching-plan design**, then **practical-exam design**. The order is deliberate — the practical set that motivated this ADR was well built on a broken outcome, and building the practical skill first would generalise the symptom.
