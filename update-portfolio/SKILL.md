---
name: update-portfolio
description: Sync a roll-up document against the sources it summarizes — reconcile every section with its source tree, append to the decision log, refresh the dates, verify the cross-tree links. Use when the user says /update-portfolio (อัปเดตพอร์ตโฟลิโอ), or asks to review or sync a summary document that spans several parts of the repo.
---

# update-portfolio — sync a roll-up document with its sources

This skill is an ordered checklist — do not skip steps. A **roll-up document** is a single file whose content is a summary of state that lives elsewhere: it goes stale the moment a source changes, and its value is that a reader can trust it without opening the sources.

## Steps

1. **Work from the root that can see every source** — open the session at the repository root, not inside one of the trees being summarized. A session rooted in a single tree cannot read the other trees' rules, and will reconcile against a partial picture without noticing.
2. **Identify the roll-up and its sources** — read the host project's `CLAUDE.md` for which document rolls up what; the document's own frontmatter and section links usually name the sources feeding each section.
3. **Read the roll-up in full** — read the whole file, not a sampled range. A summary document's sections constrain each other, and editing one against a partial read produces contradictions inside the same file.
4. **Reconcile section by section** — for each section, open the source it summarizes (that tree's index, status file, or project records) and compare claim by claim. Every section accounted for; where the source and the roll-up disagree, the source wins unless the user says otherwise.
5. **Apply the changes and log the decision** — update the affected tables and checklists, then append one row to the document's decision history: date, what changed, and the effect. History rows are append-only — superseded entries stay as the record of what was believed when.
6. **Refresh the frontmatter dates** — set the verified and updated fields to today.
7. **Verify before finishing** — if the project has a link check script, run it; otherwise check the links by hand. Cross-tree links break more often than any others in the repo, and this document holds more of them than any other.
