---
name: audit-brain
description: Score an existing knowledge base against the twelve-component anatomy, report the gaps, then apply only the fixes the user decides on. Use when the user asks to health-check a vault (ตรวจสุขภาพคลัง), or after updating the skills (หลังอัปเดต skill).
---

# audit-brain — score an existing knowledge base

This skill is an ordered checklist: each step opens when the one before it has produced its result. It reports first and changes nothing until the user has decided. Scaffolding a vault from scratch is `init-brain`, not this skill.

Whenever a step puts more than one decision to the user, it asks them in the round shape the `grill-point` skill gives in its step 3.

The component reference is the `brain-anatomy` skill — read it before step 2.

## Steps

1. **Discover the project's conventions** — read the host project's agent instructions file (`AGENTS.md`, or `CLAUDE.md`) and inspect the vault's own shape: which trees exist, where the constitution lives, and the language the vault writes its documents in. A rule the vault states about itself governs the anatomy's default, and the scorecard is written in the vault's language. Then show the user the plan for this run — its steps by number with a 🛑 on each one that stops for the user, then one line of what this step found and one of what it could not find, labelled in the user's language — and wait for the user's go-ahead, or take the dispatch as the go-ahead when this run was sent to work without the user, as a sub-agent; name each later step by its number as it starts.
2. **Score all 12 components** — walk the `brain-anatomy` skill against the existing vault and mark each component **present / partial / missing**, citing a file path (or its absence) as evidence. Every component accounted for — no skips. Where an earlier scorecard exists, mark each component it did not score: those rows are what the skill set has added since the last audit, which makes the scorecard the vault's own record of what an update changed. The scorecard is one table, one row per component in the anatomy's order, headers in the vault's language — the same columns every audit, so one scorecard can be read against the last:

   | # | Component | State | Evidence | Outcome |
   |---|---|---|---|---|
   | 3 | Indexes at every level | partial | `index.md` lists 3 of 5 subjects | |

   *State* is present, partial, or missing; *Evidence* is the path, or the path that was looked for and is absent; *Outcome* stays empty until step 4 fills it. A component the earlier scorecard did not score opens its *Evidence* with "new since" and that scorecard's date, so the mark adds no column.
3. **Record the scorecard, then settle the fixes with the user** — write the scorecard to a dated file in the vault (default `docs/brain-audit-<YYYY-MM-DD>.md`; follow the vault's own docs convention if it has one). **This step is a grill point**: run the `grill-point` skill, and build nothing on a decision the grill has not settled. Each gap is one decision, with a concrete proposal as its recommendation — how many trees, where a kind of file lands, what is archived — because those are choices only someone who works in the vault can judge. Change nothing in the vault until the grill has ended.
4. **Apply the decided fixes and verify** — implement only what was decided, and run the project's check script where one exists, then confirm: the scorecard carries the line its grill wrote, every decided fix is present in the vault, and no link broken by it. Close the loop in the scorecard file: mark each gap's *Outcome* as fixed or declined, so the next audit starts from what was already decided rather than re-proposing it.
