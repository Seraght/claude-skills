# External tools are accelerators, not prerequisites

These skills are intended for non-technical staff as well as their author, so a step that names a specific CLI tool turns a missing install into a dead end the user cannot diagnose. We decided that every step states its *goal* and offers a path the agent can take with its own built-in capabilities; an external tool may be used when present, as a shortcut. Where a tool is genuinely unavoidable, the skill checks for it first and gives a one-line install instruction rather than failing on a raw command-not-found.

## Considered Options

- **Require the tools and document the install** (e.g. poppler for `pdftotext`) — rejected: the install is the first thing a non-IT user meets, and it would not even solve the motivating case, since text extraction returns nothing on the scanned PDFs common in Thai government documents.
- **Detect and degrade silently** without saying anything — rejected for genuinely-required tools: a silent downgrade hides that the run was weaker than it looked.

## Consequences

- `digest` now reads documents with the agent's own PDF-reading capability (which covers scanned pages), treating `pdftotext` as an optional skim shortcut for long documents rather than step one.
- `ship`'s rationale for writing commit messages through a file is stated platform-neutrally; the PowerShell 5.1 behaviour remains as one example rather than the whole reason.
- Reading a long document visually costs meaningfully more tokens than extracting its text. That cost is accepted as the price of a skill that runs anywhere without setup.
