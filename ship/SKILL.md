---
name: ship
description: Close out pending work as clean, topic-grouped commits — group changes by subject, screen the diff for sensitive data and stray files, regenerate derived artifacts, write the message through a file, verify the tree is clean. Use when the user says /ship (ปิดงาน, commit งานค้าง), or asks to commit or save the work in progress.
---

# ship — close out work as clean commits

This skill is an ordered checklist — do not skip steps. It carries the *process* only: the project's own message format, check scripts, and hooks are discovered at runtime.

## Steps

1. **Discover the project's commit conventions** — read `CLAUDE.md` / `CONTRIBUTING.md` for message format and language, and look for check scripts (`_scripts/`, `scripts/`, `package.json`) and git hooks. Project rules override the defaults below.
2. **Survey and group** — run `git status --short` and group the changed files by subject. One commit = one subject: content changes and rule/documentation changes ship as separate commits.
3. **Account for every file** — anything you cannot attribute to the work at hand goes to the user before staging: sync-service conflict copies (`name (1).md`), stray build output, editor scratch files.
4. **Screen the diff before staging** — read the actual diff for personal data (names, emails, ID numbers) and secrets. Backup hooks and mirrors make history effectively permanent, so treat "commit now, remove later" as unavailable.
5. **Run the checks that apply** — if the changes touch an area covered by a status or link script, run it and reconcile what it reports with the files as they actually are.
6. **Regenerate derived artifacts** — if the project generates a map, index, or table of contents from content that this change invalidates, regenerate it and include it in the last commit of the batch.
7. **Write the message through a file** — write it to a scratch file and use `git commit -F <file>`. Shells mangle multi-line and non-ASCII messages passed inline, quietly and differently on each platform (PowerShell 5.1 splits arguments on embedded quotes), so a file keeps the message you wrote. Follow the project's format; default to `type: summary` on line one plus detail bullets.
8. **Let the hooks do their job** — when a hook rejects a commit, fix the cause it names (a broken link, a failing check) so the next attempt passes on merit.
9. **Verify before finishing** — `git status` comes back clean. If files report as modified while their content is unchanged (a stat-cache artifact of sync-mounted drives), confirm with `git hash-object` against HEAD before clearing them with `git add -u`.
