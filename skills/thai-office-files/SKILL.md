---
name: thai-office-files
description: What a Word, PowerPoint, or Excel file carrying Thai text needs, and the rendered check that finishes it. Use when producing or editing one (ไฟล์ Word/สไลด์/Excel ภาษาไทย), or when another skill delivers one.
---

# Thai Office Files

What Thai text needs from an Office file, and the check that decides when such a file is finished. This file is reference only — it carries no steps of its own. The skill or tool that builds the file keeps its own process; this one adds the Thai rules and the check that closes the work.

## A Thai file is finished when its rendered check passes

**Read the file as its reader will see it.** Reading the markup checks only the causes already known. Word's failure is an absence — a flag and a setting that are simply not there — which reads as nothing until the rule is known, and the lines it splits reach the margin exactly as well-broken ones do. Neither the markup nor line length shows it; the page does.

1. **Render** the file in the program its reader will open it in, by exporting a PDF from that program. The commands are in each format's file.
2. **Read the line breaks.** Write down, as an evidence table, the last few characters of a line and the first few of the next, for one wrapped line in every paragraph style and every table that holds Thai text, and at least twenty breaks in all, or every break where the file has fewer — a working figure, not a researched one. Beside each, the reading: *between words* or *inside a word*. A table that holds no breaks did not check anything.
3. **One break inside a word fails the file.** Trace it to its cause with the format's rules, fix the cause rather than the line, and render again.

Some breaks are inside a word by their characters alone: a line that ends on a leading vowel (`เ แ โ ใ ไ`) or on `ั`, and a next line that starts with a following vowel, a tone mark, or `ๆ`. Every other break is read — `สื่|อสาร` and `เด็|ดขาด` pass the character test and are still split.

**Where the agent can start a sub-agent with a fresh context, the render and the reading run there.** It writes the page images and the evidence table beside the file and reports back only the breaks inside a word, each with its page. Page images read in the run that builds the file stay in that run's context for every turn after; the evidence on disk is what shows the check ran.

**Extracted text can misreport `ำ`.** PyMuPDF, reading a PDF that Word exported, gives `ค าชี้แจง` for `คำชี้แจง`. That space is the extractor's, not the page's: judge a suspect break from the page image.

**Where the machine has no Office program, the check has not run.** Record it as an unticked item in the run's own closing check, naming this skill, and tell the user what to look at once the file is open in the program: line ends of long paragraphs, for a word broken in two; and any line of a Thai-distributed paragraph — often the first — whose letters are stretched far apart. A rendering from another program — LibreOffice, Google Docs, a browser preview — lays Thai out with its own engine, so it says nothing about what the reader's program will show.

## A rule enters with a rendered test behind it

Every rule in the format files names the test that established it: what was varied, and what the page showed. Something believed about Thai in Office files and not yet tested is listed under **Untested** in its format's file, as a question rather than a rule — a remembered rule is how a half-true fix gets passed on as a lesson. When a run meets a Thai problem the files do not cover, tell the user, with the file it was seen in, so it can be tested and added here.

## Paragraph alignment

In Word documents, continuous Thai body text — instructions, stems, passages — is set **Thai distributed** (`thaiDistribute`). Options, table cells, headings, and short lines are set **left**. The host project's template, or the institution's form, governs over both.

Thai distributed shows the Word failure most visibly: the paragraph's first line, cut short at its last space, is stretched letter by letter to the margin. Where that appears, the line-breaking rule in [DOCX.md](./DOCX.md) is the cause, not the alignment.

## Which file to read

| File | Applies to |
|---|---|
| [DOCX.md](./DOCX.md) | Word documents — the line-breaking rule, and how to render |
| [PPTX.md](./PPTX.md) | PowerPoint presentations — how to render; no rules yet |
| [XLSX.md](./XLSX.md) | Excel workbooks — how to render; no rules yet |
