---
name: thai-office-files
description: What a Word, PowerPoint, or Excel file carrying Thai text needs, and the rendered check that finishes it. Use when producing or editing one (ไฟล์ Word/สไลด์/Excel ภาษาไทย), or when another skill delivers one.
---

# Thai Office Files

What Thai text needs from an Office file, and the check that decides when such a file is finished. This file is reference only — it carries no steps of its own. The skill or tool that builds the file keeps its own process; this one adds the Thai rules and the check that closes the work.

## A Thai file is finished when its rendered check passes

**Read the file as its reader will see it.** A file whose markup is right line by line can still lay out wrong, and nothing in the file shows it. Word proves the point: with one setting missing it splits Thai words at the right margin, and those split lines reach the margin exactly as well-broken ones do — so measuring line length, or reading the markup, passes a broken page.

1. **Render** the file in the program its reader will open it in, by exporting a PDF from that program. The commands are in each format's file.
2. **Read the line breaks.** Write down, as an evidence table, the last few characters of a line and the first few of the next, for one wrapped line in every paragraph style and every table that holds Thai text, and at least twenty breaks in all — a working figure, not a researched one. Beside each, the reading: *between words* or *inside a word*. A table that holds no breaks did not check anything.
3. **One break inside a word fails the file.** Trace it to its cause with the format's rules, fix the cause rather than the line, and render again.

Some breaks are inside a word by their characters alone: a line that ends on a leading vowel (`เ แ โ ใ ไ`) or on `ั`, and a next line that starts with a following vowel, a tone mark, or `ๆ`. Every other break is read — `สื่|อสาร` and `การวั|ด` pass the character test and are still split.

**PDF text extraction splits `ำ`.** Text pulled from a PDF that Word exported reads `ค าชี้แจง` for `คำชี้แจง`. That space is the extractor's, not the page's: judge it from the page image where it matters.

**Where the machine has no Office program, the check has not run.** Record it as an unticked item in the run's own closing check, naming this skill, and tell the user what to look at once the file is open in the program: line ends of long paragraphs, for a word broken in two; and the first line of each Thai-distributed paragraph, for letters stretched far apart. A rendering from another program — LibreOffice, Google Docs, a browser preview — lays Thai out with its own engine, so it says nothing about what the reader's program will show.

## A rule enters with a rendered test behind it

Every rule in the format files names the test that established it: what was varied, and what the page showed. Something believed about Thai in Office files and not yet tested sits under **Untested** in its format's file until a test moves it — a remembered rule is how a half-true fix gets passed on as a lesson.

## Paragraph alignment

Continuous Thai body text — instructions, stems, passages — is set **Thai distributed** (`thaiDistribute` in Word). Options, table cells, headings, and short lines are set **left**. The host project's template, or the institution's form, governs over both.

Thai distributed shows the Word failure most visibly: the paragraph's first line, cut short at its last space, is stretched letter by letter to the margin. Where that appears, the line-breaking rule in [DOCX.md](./DOCX.md) is the cause, not the alignment.

## Which file to read

| File | Applies to |
|---|---|
| [DOCX.md](./DOCX.md) | Word documents — the line-breaking rule, and how to render |
| [PPTX.md](./PPTX.md) | PowerPoint presentations — how to render; no rules yet |
| [XLSX.md](./XLSX.md) | Excel workbooks — how to render; no rules yet |
