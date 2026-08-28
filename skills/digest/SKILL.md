---
name: digest
description: Import a raw document from staging into a knowledge base — privacy and copyright gates, filing, digest, index entry. Use when the user asks to import a document (นำเข้าเอกสาร, ย่อยเอกสาร), or files are waiting in staging.
---

# digest — import raw documents into the knowledge base

This skill is an ordered checklist: each step opens when the one before it has produced its result. It carries the *process* only — everything project-specific (folder layout, naming rules, templates) is discovered from the host project at runtime.

## Steps

1. **Discover the project's conventions** — read the host project's agent instructions file (`AGENTS.md`, or `CLAUDE.md`) and inspect the existing structure: where imported sources live, where digests live, whether an index/registry and a digest template exist. Explicit import rules in the host project override the generic defaults below. If no staging folder is defined, ask the user which folder is the inbox.
2. **Survey the staging area** — list the waiting files (commonly `temp/` or `inbox/`; typically untracked in git).
3. **Read the actual content before any decision** — judge the document by what is inside it, never by its filename. Reading a scanned or image-heavy source puts its pages into the working session, which then carries them for everything that follows; on a long document that can cost more than the rest of the import put together. Take the cheapest path that actually works, in this order:
   - **Read it in an isolated worker if your agent has one** — a sub-agent or equivalent reads the document and returns the summary, so the pages never enter this session at all. Ask it for what steps 4-10 need: subject matter, whether personal data appears, whether it is an original record, copyright status, key content.
   - **Otherwise skim extracted text first** if a text-extraction tool happens to be installed (`pdftotext -raw`), and read pages directly only where extraction comes back empty — which is what scanned documents do.
   - **Otherwise read the document directly** with your own file-reading capability, which handles scanned pages as well as digital text. This path always works; it is simply the expensive one, so it is the fallback rather than the default.
4. **Pass two gates before filing anything:**
   - **Privacy** — does the document hold personal data *as its content*: records about identifiable people who did not publish them — students, patients, clients, research participants, staff — such as names on a roster, ID numbers, individual scores, contact details, or case notes? If yes: stop, notify the user, do not digest. The people a published work names as its own authors, editors, or cited sources are its byline, not its content; a paper is not blocked for carrying an author list, an affiliation, or a corresponding-author email. Where a document holds both, the gate fires on the personal data it holds, whatever its byline says.
   - **Original official records** — is this an original organizational record rather than reference material? Originals belong in the organization's system of record, not a knowledge base; file only a digest/summary here, and ask the user where the original should go.
5. **Choose the destination** by what the content *is*, using the structure discovered in step 1 — e.g. a repo split by role might route teaching material, research, and admin work to different trees. If the content fits no discovered destination, or fits more than one, ask the user instead of guessing.
6. **Check for waiting gaps** — before creating a new file, search the destination's README/index for placeholders or "not yet written" markers; a new document often fills a gap that already exists.
7. **Decide copyright before moving the file:**
   - The user's own writing, public and official publications → the source file may be stored.
   - Someone else's work carrying a licence that permits redistribution — Creative Commons, an open-access statement, a public-domain dedication, an open-source licence → the source file may be stored, and the licence is recorded beside it, so a later reader can tell why it was allowed to stay.
   - Everything else a third party holds rights over — textbooks, paywalled articles, purchased material → write a digest with a full citation; the source file is not stored.
   - Unsure, or a licence you cannot read off the document → ask the user.
8. **Rename meaningfully** — lowercase, hyphen-separated, with issuing org and year (e.g. `who-ai-ethics-guidance-2024.pdf`), unless the project defines its own naming rule.
9. **Leave nothing behind in staging silently** — when the source file was stored (step 7), move it (don't copy): remove the original from staging once filing succeeds. When only a digest was written (file not stored), ask the user what to do with the original — delete it from staging, or hand it back for them to file elsewhere.
10. **Write the digest and register it** — follow the project's digest template if one exists; update the README/index to point at the new file. If the digest closes a gap found in step 6, update the gap's status in the same edit.
11. **Verify before finishing** — run the project's check script where one exists, then confirm: staging area empty (or leftovers reported to the user), every new file linked from an index, no broken links introduced.
