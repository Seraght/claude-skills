# Group by output, and defer the folders

The set had grown past the "second brain" framing it was extracted under: two of its six skills produced nothing that lived in a knowledge base. We first fixed the definition — `claude-skills` is a set of ordered checklists for repeatable knowledge work, where the steps cannot be reordered, skipping one fails silently, and the result is a document that has to land in the right place. A knowledge base is one destination those results land in, not what the set is about.

With that in hand, grouping became answerable. Skills are grouped by **what they change when they finish**, not by topic: a topic is a feeling, an output can be pointed at. That yields *vault work* (`init-brain`, `digest`, `new-subject`, `update-portfolio`) and *teaching and assessment* (`make-exam`). The criterion is written down in `README.md`; the folders under `skills/` stay flat.

`ship` was moved out of the set to its author's personal skills. It is a git tool whose output is repository state, not a document, and the audience this set is written for (see ADR 0002) does not necessarily use git at all. That left its group with no members, so the group is not documented either — the criterion's last clause covers the case where a future skill fits neither group.

## Considered Options

- **Split into category folders now** (`skills/vault/`, `skills/teaching/`) — rejected: plugin skill auto-discovery only looks one level deep, so nested categories force every skill's path into `plugin.json` and keep it there forever. Six skills, two of them alone in their group, is not enough evidence to lock an axis in exchange for that.
- **Split into one plugin per group** so installers could take half the set — rejected: several manifests, several marketplace entries, and several version streams to bump, for a set nobody yet wants half of.
- **Group by lifecycle stage** (set up → take in → maintain → close out) — rejected: a skill's stage changes with how the vault is being used that day, while its output does not.
- **Keep `ship` and accept a one-member group** — rejected on audience, not on definition: the definition covers `ship` fine, but a git skill in the list makes the set read as a developer's toolkit.

## Consequences

- The five remaining skills moved from the repository root into `skills/`, which is what plugin auto-discovery reads. `plugin.json` therefore carries no skill list, and adding a skill means adding a folder and nothing else.
- The set is published as a single Claude Code plugin, `knowledge-keeper`, from a marketplace hosted in this same repository.
- ADR 0002 cites `ship` as evidence for stating rationale platform-neutrally. That skill no longer lives here; the ADR is left as written, since it records what was true when the decision was made.
- Splitting into folders later costs one `git mv` and one `skills` array in `plugin.json` — deferred, not foreclosed. The trigger is a third group with real members, decided by the criterion in `README.md`.
