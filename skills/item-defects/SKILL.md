---
name: item-defects
description: The defects an exam item can carry, one file per item format, each defect with its fix. Use when writing or critiquing items, or when another skill needs the defect taxonomy.
---

# Item Defects

The flaw taxonomy every assessment skill in this set judges an item against. The `make-exam` skill measures items against it while writing them; `critique-mcq` measures an assembled paper against it. This file is reference only — it carries no steps of its own.

**Measure, then judge.** Every defect here is read off a count, not off an impression of the item. On this exact task, an LLM applying a rubric by reading alone detected the longest-key flaw at F1 0.18–0.44, while a script that counted characters reached 0.80–1.00; the same LLM reported 4.2 flaws per item where expert raters using the identical rubric found 1.6. Judgement by impression both misses what counting finds and invents what is not there — so a pass that produced no table did not run.

**A verdict is not a measurement.** Where a check answers yes or no rather than producing a number, the cell holds **the matched span** — the string found, which option carries it, and in how many options it appears — never a tick, and never the words "none found". A cell that can hold a tick can hold a wrong tick, and nothing downstream can tell one from the other. **One item, one row:** a row spanning a range of items is a summary, and a summary is where a wrong value hides.

**The host project governs.** Where a project or an institution fixes an item rule — a required number of options, a mandated response form, a fixed critique taxonomy — an item is not flawed for following it, and the project's own rules override every file here.

## Which file to read

| File | Applies to |
|---|---|
| [COMMON-DEFECTS.md](./COMMON-DEFECTS.md) | **Every item, of every format** — congruence with the outcome, the correctness of the keyed answer, self-containment, and the defects that appear only across a whole paper |
| [MCQ-DEFECTS.md](./MCQ-DEFECTS.md) | Selected-response items with a single best answer |
| [CONSTRUCTED-RESPONSE-DEFECTS.md](./CONSTRUCTED-RESPONSE-DEFECTS.md) | Essay, short-answer, and problem items, together with their rubrics |
| [MATCHING-DEFECTS.md](./MATCHING-DEFECTS.md) | Matching sets |
| [PRACTICAL-DEFECTS.md](./PRACTICAL-DEFECTS.md) | Practical and performance tasks, with their conditions, scoring instruments, and markers |

An item is judged against **COMMON-DEFECTS.md and the file for its own format** — never one alone. A format with no file here is reported as not reviewed rather than judged against a taxonomy written for another format.

## How the groups are used

Each file divides its defects into the same four groups, so a skill can run them as passes and report a count for each, including the passes that found nothing:

- **Group A** — flaws that let an examinee who does not know the content earn the mark anyway.
- **Group B** — flaws that make the item hard for reasons unrelated to what it measures.
- **Group C** — flaws in congruence, cognitive level, and correctness, judged against the course's own outcomes and sources.
- **Group D** — flaws that appear only once the paper is assembled, and that no per-item pass can find.

Severity is the same everywhere: **Block** where the item cannot be administered as written, **Revise** where a flaw distorts the score, **Note** where there is no evidence it moves scores.

## Languages without word spacing

In Thai, Khmer, Lao, Japanese, and Chinese, a word count is not a measurement — the whole option reads as one token — so length is counted in characters, and several checks need a different marker than their English form. A tokenizer, where one is installed, is a convenience for the length check; it is never a prerequisite.

Working equivalents for Thai:

- **Grammatical cues** — not number agreement, which Thai does not mark. Look at a lead-in ending in a classifier or a connective (`เป็น`, `คือ`, `ที่`, `ซึ่ง`, `เพื่อ`, `ได้แก่`) that only one option continues naturally, and at classifiers that agree with one option's noun only.
- **Clang cues** — a word repeated from the stem into the key, and shared Pali-Sanskrit elements (`โรค-`, `อภิ-`, `-วิทยา`, `-ภาพ`) that tie one option to the stem.
- **Absolute terms** — `เสมอ`, `ทุกครั้ง`, `ทั้งหมด`, `ไม่เคย`, `เท่านั้น`, `ห้ามเด็ดขาด`.
- **Vague frequency terms** — `มักจะ`, `บ่อยครั้ง`, `โดยทั่วไป`, `บางครั้ง`, `ส่วนใหญ่`.
- **Negation in the lead-in** — `ข้อใดไม่ใช่`, `ข้อใดไม่ถูกต้อง`, `ยกเว้น`.
- **"None / all of the above"** — `ถูกทุกข้อ`, `ผิดทุกข้อ`, `ไม่มีข้อใดถูก`.
- **Complex (K-type) options** — `ข้อ ก และ ข ถูก`.
