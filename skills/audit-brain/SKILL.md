---
name: audit-brain
description: Score an existing knowledge base against the eleven-component anatomy, report the gaps, then apply only the fixes the user approves. Use when the user asks to health-check a vault (ตรวจสุขภาพคลัง).
---

# audit-brain — score an existing knowledge base

This skill is an ordered checklist: each step opens when the one before it has produced its result. It reports first and changes nothing until the user approves. Scaffolding a vault from scratch is `init-brain`, not this skill.

The component reference is the `brain-anatomy` skill — read it before step 2.

## Steps

1. **Discover the project's conventions** — read the host project's agent instructions file (`AGENTS.md`, or `CLAUDE.md`) and inspect the vault's own shape: which trees exist, where the constitution lives, and the language the vault writes its documents in. A rule the vault states about itself governs the anatomy's default, and the scorecard is written in the vault's language.
2. **Score all 11 components** — walk the `brain-anatomy` skill against the existing vault and mark each component **present / partial / missing**, citing a file path (or its absence) as evidence. Every component accounted for — no skips.
3. **Record the scorecard, then report before touching anything** — write the scorecard to a dated file in the vault (default `docs/brain-audit-<YYYY-MM-DD>.md`; follow the vault's own docs convention if it has one), then present it with a concrete proposal per gap and wait: change nothing else until the user picks which fixes to apply.
4. **Apply approved fixes and verify** — implement only what was approved, and run the project's check script where one exists, then confirm: every approved fix present in the vault, and no link broken by it. Close the loop in the scorecard file: mark each gap as fixed or declined, so the next audit starts from what was already decided rather than re-proposing it.
