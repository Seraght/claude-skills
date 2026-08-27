# How a skill is reached, and when it is split

Every skill in this set was model-invoked, which was never a decision — it was the default nobody questioned. A model-invoked skill's description sits in the agent's context on every turn of every session where the plugin is installed, whether or not the skill ever fires, and the descriptions here had grown to roughly twice the length of the ones they were modelled on: around 62 words each, spending most of them re-listing steps the body already carries.

We decided three things.

**Invocation is a choice with two tiers.** A skill is model-invoked when a user typing a Thai phrase must reach it without knowing its name — which covers the daily-use skills, and is the reason the Thai triggers live in `description` at all. A skill is user-invoked when it *creates* a whole structure, or when the people who run it already know when they want it. `init-brain` scaffolds an entire vault; letting an agent decide on its own to do that is a blast radius out of proportion to saving one line of typing, and the person setting up a vault for the first time is reading the README anyway. `update-portfolio` is run by people who already own the roll-up. Both become user-invoked and cost nothing on the context window.

**A description's job is to get the agent to the right skill, not to describe it.** Budget: about 30 words. Branches named twice with different words ("into the knowledge base" and "into the repo") are one branch, and collapse.

**Splitting is by how a skill is reached, not by hiding its later steps.** `init-brain` carried a second mode that scored an existing vault — a recurring, read-only request that wants exactly the autonomous reach greenfield scaffolding should not have. Two invocations in one file, so it splits: `audit-brain`. The eleven-component anatomy both walk becomes `brain-anatomy`, a model-invoked skill holding reference only, reachable by name from either — which required loosening the set's own rule that a skill never calls another. The loosened rule is narrower than "never": a checklist may reach reference, never another checklist.

## Considered Options

- **Keep `init-brain` whole and user-invoked** — rejected: it takes the audit down with it, and health-checking a vault is the kind of thing a user asks for in a sentence, not by recalling a command name.
- **Keep `init-brain` whole and model-invoked** — rejected: it hands an agent the ability to scaffold a tree on its own initiative.
- **Copy the anatomy into both folders**, per [ADR 0005](0005-duplication-buys-portability.md) — rejected: 964 words is past the size where duplicated text stays identical, and the discovery clause had already proved the point at four lines.
- **Point at the anatomy by relative path** across folders — rejected: it survives copying no better than the copy does, and breaks additionally whenever a folder moves. Name-based reach does not.
- **Split `critique-mcq` at its approval wall** (steps 1–10 critiquing, 11–12 applying), so the agent cannot see the applying steps while it measures — **rejected**. Hiding later steps only works across a real context boundary; an approval wall pauses the clock without clearing context, so the later steps stay visible regardless. `critique-mcq` already defends the same risk better, by publishing the measurement table and a count for every pass including the empty ones: a pass that never ran is visible rather than merely discouraged.

## Consequences

- Eight skills where there were six: `init-brain` and `update-portfolio` user-invoked, `audit-brain` and `brain-anatomy` new and model-invoked.
- `init-brain` and `audit-brain` no longer travel alone — both need `brain-anatomy`. Stated in the README rather than left to be discovered when a copied folder fails.
- Always-loaded description text drops from roughly 375 words across six skills to roughly 190 across six, with two skills paying nothing.
- README pattern 2 is amended, and pattern 5 (the two tiers) is new.
- The prohibition "do not skip steps", present in all six skills and never tested since the first portability pilot, is replaced by a condition an agent can check: a step opens when the one before it has produced its result. It steered by naming the behaviour it forbade, which is the one reliable way to keep that behaviour in mind.
