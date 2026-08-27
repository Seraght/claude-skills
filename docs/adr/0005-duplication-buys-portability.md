`# Duplication buys portability
`
`Every skill in this set opens with the same "Discover the project's conventions" step, and the sentence naming the constitution is repeated word for word in five files. That is a deliberate purchase, not an oversight: the promise this set makes is that a user can copy one folder into `.claude/skills/` and have it run, and a skill whose first step lives in another folder cannot keep it.
`
`We decided that portability outranks single source of truth for *short, stable* text — the discovery clause, the checklist gate, the conditional-verify line — and that the duplicated text is therefore held byte-identical, so a future edit can find every copy with one search. Reference bodies large enough to drift meaningfully are the exception and go to a reference skill instead ([ADR 0006](0006-how-a-skill-is-reached-and-when-it-is-split.md)).
`
`The failure this guards against had already started. `digest` read `AGENTS.md`, `CLAUDE.md`, **or its README**; the other three read only the first two. Nobody chose the discrepancy — it appeared because a later edit landed in one copy. Resolved in favour of the narrower form: a README is written for people, and treating it as binding rules means inferring a project's intent from its marketing. Where no constitution exists, the skills ask.
`
`## Considered Options
`
`- **A shared file the skills point at by relative path** (`../_shared/discovery.md`) — rejected: it breaks single-folder copying and re-breaks whenever a folder moves.
`- **A reference skill holding the discovery step** — rejected for this content specifically: four lines are not worth a permanently loaded description, and unlike the anatomy this text is short enough to keep identical by hand.
`- **Accept the drift** and let each skill word its own discovery step — rejected: the wording decides which files an agent will treat as authoritative, which is exactly the kind of thing that should not vary by accident.
`
`## Consequences
`
- The discovery clause is a single string, identical in all five skills that carry it, so one `grep` finds every copy.
`- `CONTEXT.md`'s **Constitution** entry now states that a README does not qualify.
`- Any future edit to a duplicated line is a five-file edit. That cost is accepted; the alternative was a dependency the copy-one-folder promise cannot survive.
