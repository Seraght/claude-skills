# Generalize skills for portability instead of copy-and-edit reuse

This repo began as an archive of skills extracted verbatim from the `second-brain` repo, reusable only by copying a folder and hand-editing its hardcoded paths (`.Subject/`, `_shared/assessment/`, check scripts). We decided to rewrite each skill as a **generalized, portable checklist**: the skill carries only the recurring *process*, discovers project-specific structure (folder layout, naming rules, templates) from the host project's `CLAUDE.md` and file tree at runtime, and asks the user when the discovered structure is ambiguous. Skill prose is English by default; hardcoded second-brain rules are stripped, surviving only as brief examples explicitly marked as examples.

## Considered Options

- **Keep copy-and-edit reuse** (the original README's stance) — rejected: every deployment needs manual path surgery, and the intended target includes projects with no second-brain structure at all.
- **Embed second-brain reference content into each skill** (e.g. copy `_shared/assessment/*` into `make-exam/`) — rejected: creates a second source of truth that silently drifts from the original repo, the exact failure the original design guarded against. A skill may still carry *its own* general reference (`make-exam/ASSESSMENT-REFERENCE.md`, `init-brain/BRAIN-ANATOMY.md`) written for the generic case, because the skill states that the host project's equivalent governs where one exists — so the two never compete to be authoritative.
- **Placeholder/config sections filled in per project** — rejected in favor of runtime discovery: still manual editing, and the environment is the source of truth that cannot go stale.

## Consequences

- Each skill must end with a conditional verification step (run the project's check script if one exists, otherwise a manual checklist), since project scripts can no longer be assumed.
- The README's identity statement ("not plug-and-play") became wrong and was rewritten once the `digest` and `init-brain` pilots had been validated in real use.
- A setup-time skill (`init-brain`) is required: runtime discovery needs conventions to discover, which a fresh vault does not have.
- The original second-brain-specific versions remain available in git history (commit `1de9306`).
