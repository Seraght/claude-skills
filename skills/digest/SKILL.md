---
name: digest
description: Import raw documents (PDFs etc.) from a staging folder into a knowledge base — read the actual content, pass privacy and copyright gates, file to the right destination, write a digest, register it in the index. Use when the user asks to import a document into the knowledge base (นำเข้าเอกสาร, ย่อยเอกสาร), when new files are waiting in the staging folder, or when asked to import a document into the repo.
---

# digest — import raw documents into the knowledge base

This skill is an ordered checklist — do not skip steps. It carries the *process* only: everything project-specific (folder layout, naming rules, templates) is discovered from the host project at runtime, never assumed.

## Steps

1. **Discover the project's conventions** — read the host project's agent instructions file (`AGENTS.md`, `CLAUDE.md`, or its README) and inspect the existing structure: where imported sources live, where digests live, whether an index/registry and a digest template exist. Explicit import rules in the host project override the generic defaults below. If no staging folder is defined, ask the user which folder is the inbox.
2. **Survey the staging area** — list the waiting files (commonly `temp/` or `inbox/`; typically untracked in git).
3. **Read the actual content before any decision** — judge the document by what is inside it, never by its filename. Reading a scanned or image-heavy source puts its pages into the working session, which then carries them for everything that follows; on a long document that can cost more than the rest of the import put together. Take the cheapest path that actually works, in this order:
   - **Read it in an isolated worker if your agent has one** — a sub-agent or equivalent reads the document and returns the summary, so the pages never enter this session at all. Ask it for what steps 4-10 need: subject matter, whether personal data appears, whether it is an original record, copyright status, key content.
   - **Otherwise skim extracted text first** if a text-extraction tool happens to be installed (`pdftotext -raw`), and read pages directly only where extraction comes back empty — which is what scanned documents do.
   - **Otherwise read the document directly** with your own file-reading capability, which handles scanned pages as well as digital text. This path always works; it is simply the expensive one, so it is the fallback rather than the default.
4. **Pass two gates before filing anything:**
   - **Privacy** — does the document contain personal data about identifiable individuals (names, emails, ID numbers)? If yes: stop, notify the user, do not digest.
   - **Original official records** — is this an original organizational record rather than reference material? Originals belong in the organization's system of record, not a knowledge base; file only a digest/summary here, and ask the user where the original should go.
5. **Choose the destination** by what the content *is*, using the structure discovered in step 1 — e.g. a repo split by role might route teaching material, research, and admin work to different trees. If the content fits no discovered destination, or fits more than one, ask the user instead of guessing.
6. **Check for waiting gaps** — before creating a new file, search the destination's README/index for placeholders or "not yet written" markers; a new document often fills a gap that already exists.
7. **Decide copyright before moving the file:**
   - Public/official publications and the user's own writing → the source file may be stored in the knowledge base.
   - Third-party copyrighted material (textbooks, articles) → do not store the file; write a digest with a full citation instead.
   - Unsure → ask the user.
8. **Rename meaningfully** — lowercase, hyphen-separated, with issuing org and year (e.g. `who-ai-ethics-guidance-2024.pdf`), unless the project defines its own naming rule.
9. **Leave nothing behind in staging silently** — when the source file was stored (step 7), move it (don't copy): remove the original from staging once filing succeeds. When only a digest was written (file not stored), ask the user what to do with the original — delete it from staging, or hand it back for them to file elsewhere.
10. **Write the digest and register it** — follow the project's digest template if one exists; update the README/index to point at the new file. If the digest closes a gap found in step 6, update the gap's status in the same edit.
11. **Verify before finishing** — if the project has a status/link check script, run it; otherwise verify manually: staging area empty (or leftovers reported to the user), every new file linked from an index, no broken links introduced.
