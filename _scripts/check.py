#!/usr/bin/env python3
"""Check the invariants this repo's own conventions depend on.

Run: python _scripts/check.py

Every rule here exists because it already drifted once. A convention that
cannot be checked is a convention that will drift again, so each decision
recorded in docs/adr/ that constrains the skill files gets a rule here.
"""
import io, os, re, sys, glob

# Rules below quote Thai, and this repo's audience runs on Windows consoles
# that default to a legacy codepage. Without this the script dies printing its
# own rule name rather than reporting a result.
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = sorted(glob.glob(os.path.join(ROOT, 'skills', '*', 'SKILL.md')))
NAMES = {os.path.basename(os.path.dirname(p)) for p in SKILLS}
# Every markdown file a skill folder carries, not only its SKILL.md: the drift
# ADR 0008 is written from lived in a sibling reference file, where the rules
# below were not looking.
DOCS = sorted(glob.glob(os.path.join(ROOT, 'skills', '*', '*.md')))

# Text held identical across skills rather than shared from one place,
# because a skill must run when its folder is copied alone (ADR 0005).
# Each entry: label, a regex matching the *step* that must carry the text
# (a mention elsewhere is not a carrier), and the canonical wording.
RUBRIC_CORE = (
    '- **Analytic** (separate criteria, each scored) for diagnostic feedback and multi-marker consistency; **holistic** (one overall judgement) for speed on short responses. Analytic is the default when more than one person marks.' + chr(10) +
    '- **Criteria are observable.** Each level descriptor names what is present or absent in the work, not how good it felt.' + chr(10) +
    '- **Levels are distinguishable.** Adjacent levels differ by something a marker can point at; typically 3–5 levels.' + chr(10) +
    "- **Criterion weights sum to the item's marks**, and reflect what the outcome actually values.")

STOP_CLAUSE = ("Whenever a step puts more than one decision to the user, it asks them in the round "
               "shape the `grill-point` skill gives in its step 3")
APPROVAL_EXCEPTION = (", except that an approval of items is asked in the approval table the "
                      "`assessment-layout` skill gives.")

HANDOFF_CLAUSE = "A run of this skill can outlast one session's context, so every step the plan marks 🛑 writes a handoff named for this skill, `HANDOFF-<skill>.md`, into the run's folder, once that folder exists, before it stops: the step to resume at and where inside it, the questions waiting on the user, what the run has learned that none of its files records, and the files to read first. A decision already written into a file is pointed to rather than copied, because two copies of one answer drift apart; one settled but not yet written anywhere goes into the handoff, or it is lost with the session. The file is rewritten whole at each stop, and the stop ends with one line, in the user's language, saying that the session can be closed here and giving the line, naming the skill and the folder, that resumes the run in a new one. The last step deletes it."
RESUME_CLAUSE = "Where the folder this run writes into already holds this skill's handoff, the run is resuming: read it before the run's other files, read first the files it lists, and take the step it names, checked against the files that exist, since a session can end between stops after its last handoff was written. Another skill's handoff in that folder belongs to that skill's run and is left as it is. Where that folder holds an unfinished run of this skill — one whose last step has not yet written into the folder — but no handoff, infer the step from the files that exist; a finished run's files are read as the steps below direct, not resumed. Where the step was inferred, or the handoff and the files disagree, say so in the line of what could not be found. Either way the plan marks the finished steps ✓. Then show the user the plan for this run"
DELETE_CLAUSE = "Last, delete this skill's handoff from the run's folder, once anything still open in it is written into the run's own files: a handoff left behind makes the next run on this folder resume one that is finished."

# A script a run writes into its session's scratch space is written again by the next
# run, carrying the paper's Thai text each time (ADR 0022).
SCRIPT_CLAUSE = "Where the vault keeps a script for a count or a build this run needs, run it rather than writing another; a script written here is saved where the vault keeps its scripts, not in a session's scratch space, so the next run finds it. An item's text is changed where it lives, in the items file, rather than through a script that regenerates the file: such a script carries the paper's text a second time and is lost with the session."

IDENTICAL = [
    ("discovery clause",
     r"^\d+\. \*\*Discover the project's conventions\*\*",
     "read the host project's agent instructions file (`AGENTS.md`, or `CLAUDE.md`) and inspect"),
    ("conditional verify",
     r"^\d+\. \*\*[^*]*[Vv]erif[^*]*\*\*",
     "un the project's check script where one exists, then confirm:"),
    ("rubric core",
     r"^## Rubrics$",
     RUBRIC_CORE),
    # The user sees the run before it starts, and which steps will stop for them (ADR 0016),
    # in a shape they can read at a glance (ADR 0019).
    ("plan clause",
     r"^\d+\. \*\*(Discover the project's conventions|Identify the roll-up and its sources|"
     r"Confirm the target is a greenfield)\*\*",
     "Then show the user the plan for this run — its steps by number with a 🛑 on each one "
     "that stops for the user, then one line of what this step found and one of what it "
     "could not find, labelled in the user's language — and wait for the user's go-ahead, or take the "
     "dispatch as the go-ahead when this run was sent to work without the user, as a sub-agent; "
     "name each later step by its number as it starts."),
    # Every stop takes a shape from one place, so a question the run invents mid-step is
    # laid out like the ones the skill planned for (ADR 0019).
    ("stop shape clause",
     r"^This skill is an ordered checklist",
     STOP_CLAUSE),
    # Only the checklists that approve items carry the exception, so a skill copied alone
    # does not point at a reference it never uses (ADR 0019).
    ("approval exception",
     r"except that an approval of items",
     APPROVAL_EXCEPTION),
    # A step that stops to grill the user names the primitive the same way everywhere, so
    # one search finds every grill point in the set (ADR 0016).
    ("grill clause",
     r"\*\*This step is a grill point\*\*",
     "**This step is a grill point**: run the `grill-point` skill, and build nothing on a decision the grill has not settled."),
    ("script clause",
     r"^Where the vault keeps a script",
     SCRIPT_CLAUSE),
]

# Wordings that lost an argument. Each is a real regression, not a style note.
BANNED = [
    (r"do not skip steps",
     "steer by the condition a step opens on, not by forbidding the failure (ADR 0006)"),
    (r"otherwise verify manually|otherwise check the links by hand",
     "a check script does not replace the checklist (ADR 0005)"),
    (r"`AGENTS\.md`, `CLAUDE\.md`, or its README",
     "a README is not a constitution (ADR 0005)"),
    (r"ask which one a|ask yourself",
     "a check that leaves no artifact cannot be shown to have run (ADR 0008)"),
    (r"\*\*Presence of\*\*",
     "asking for presence invites a yes/no; a check answers with the span it compared (ADR 0012)"),
    (r"[Ww]here a check is numeric",
     "the reporting rule bound only the checks that were already working (ADR 0012)"),
    (r"ตรวจแล้ว ไม่พบ|checked, none found",
     "the output shape a verdict takes; never model it in an instruction (ADR 0012)"),
    (r"วทก|KMPHT|รู้-จำ",
     "one institution's scale or paperwork is true where it was written and nowhere else; "
     "it belongs to the host project (ADR 0013)"),
]

# Structure that belongs to the assessment-layout skill and nowhere else (ADR 0007).
LAYOUT_LITERALS = [r"<subject>/assessment", r"assessment/<year>", r"assessment/bank",
                   r"[Rr]ows are topics", r"[Cc]olumns are cognitive levels",
                   r"teaching hours ÷", r"`stimuli/`", r"two per line"]

# The flaw taxonomy belongs to the item-defects skill and nowhere else (ADR 0008).
# It had drifted into two copies at two levels of detail, and the weaker copy is
# what the item-writing skill was held to.
DEFECT_LITERALS = [r"Clang", r"Convergence\.", r"K-type", r"Self-containment"]

# What an outcome must be belongs to the learning-outcomes skill and nowhere
# else (ADR 0010). It reached its second consumer the moment a skill was written
# to author outcomes as well as one to assess against them.
OUTCOME_LITERALS = [r"[Cc]onstructive alignment", r"Mager", r"Unobservable\.", r"Inflated\."]

# Post-administration statistics belong to the analyze-results skill and nowhere
# else (ADR 0014). The authoring and review skills name what a statistic will
# later reveal; they do not carry the thresholds for reading one.
STATS_LITERALS = [r"Ebel", r"Kuder", r"Sijtsma", r"standard error of measurement"]

# The markup Thai text needs in an Office file belongs to the thai-office-files
# skill and nowhere else (ADR 0021). A checklist that copied the Word rule would
# carry the half of it that was remembered.
THAI_OFFICE_LITERALS = [r"compatibilityMode", r"thaiDistribute", r"<w:cs/>"]

# Instructions that are wrong on their own. Each pair is one field test: the first
# phrase turned up without the second, and the run went wrong in exactly the way
# the second prevents.
PAIRED = [
    ("length of every option", "excluding spaces",
     "a step that orders a count carries the counting rule with it; leaving the rule in "
     "the reference produced a measurement table counted in characters including spaces"),
    ("matched span", "One item, one row",
     "the span rule without the row rule still permits one row spanning the whole paper, "
     "which is where the field case hid a wrong value for fifteen items at once"),
    ("binding review runs", "unticked item",
     "a review passed on only as a sentence in the session leaves no evidence, which "
     "is the failure ADR 0008 is about; it is written into the exam set instead"),
]

DESCRIPTION_BUDGET = 40

fails = []
def check(ok, msg):
    print(("  ok   " if ok else "  FAIL ") + msg)
    if not ok:
        fails.append(msg)

def body_of(text):
    parts = text.split('---', 2)
    return parts[2] if len(parts) > 2 else text

print("skills\n")
for path in SKILLS:
    name = os.path.basename(os.path.dirname(path))
    text = io.open(path, encoding='utf-8').read()
    m = re.search(r"^name:\s*(\S+)\s*$", text, re.M)
    check(bool(m) and m.group(1) == name, "%s: frontmatter name matches its folder" % name)
    d = re.search(r"^description:\s*(.+)$", text, re.M)
    check(bool(d), "%s: has a description" % name)
    if d and 'disable-model-invocation: true' not in text:
        n = len(d.group(1).split())
        check(n <= DESCRIPTION_BUDGET,
              "%s: description is %d words, budget %d" % (name, n, DESCRIPTION_BUDGET))

print("\ntext held identical\n")
for label, carries, canonical in IDENTICAL:
    carriers = [p for p in DOCS
                if re.search(carries, io.open(p, encoding='utf-8').read(), re.M)]
    check(len(carriers) > 1, "%s: carried by more than one skill (%d)" % (label, len(carriers)))
    for p in carriers:
        name = os.path.relpath(p, ROOT)
        text = io.open(p, encoding='utf-8').read()
        # Once per carrier, not once per file: a file holding three grill points with one
        # of them reworded still contains the canonical text twice.
        anchors, copies = len(re.findall(carries, text, re.M)), text.count(canonical)
        check(copies >= anchors,
              "%s: %s is the canonical wording (%d of %d)" % (name, label, copies, anchors))

# The stop-shape clause follows the opening paragraph rather than sitting anywhere: it
# governs every step, the ones nobody planned as stops included (ADR 0019).
# It ends either at its full stop or with the approval exception, and only the checklists
# that approve items carry the exception, so neither half grows a tail nobody checks.
APPROVERS = {'adopt-pool', 'critique-mcq', 'make-exam'}
for p in SKILLS:
    text = io.open(p, encoding='utf-8').read()
    if re.search(r"^This skill is an ordered checklist", text, re.M):
        name = os.path.basename(os.path.dirname(p))
        ending = re.escape(APPROVAL_EXCEPTION) if name in APPROVERS else r"\."
        check(re.search(r"^This skill is an ordered checklist[^\n]*\n\n" + re.escape(STOP_CLAUSE)
                        + ending + r"\n", text, re.M) is not None,
              "%s: stop shape clause follows the opening paragraph and ends as %s"
              % (os.path.relpath(p, ROOT), "the approval exception" if name in APPROVERS else "a full stop"))

# The checklists whose runs outlast a session write a handoff at every planned stop and
# resume from it in step 1 (ADR 0020). The clause follows the stop-shape clause, and the
# resume sentence sits in the discovery step just before the plan is shown, and the
# deletion closes the verify step, where it is acted on. Only these carry them: a run that
# always ends in one session would carry a rule it never uses. Any file may still name
# the handoff; what stays out is the clauses, in SKILL.md and sibling references alike.
# critique-mcq joined once a critique was seen to outlast a session (ADR 0022).
RESUMABLE = {'adopt-pool', 'critique-mcq', 'make-exam', 'make-practical', 'design-course'}
for p in DOCS:
    name = os.path.basename(os.path.dirname(p))
    text = io.open(p, encoding='utf-8').read()
    if name in RESUMABLE and os.path.basename(p) == 'SKILL.md':
        check(re.search(re.escape(STOP_CLAUSE) + r"[^\n]*\n\n" + re.escape(HANDOFF_CLAUSE) + r"\n",
                        text) is not None,
              "%s: handoff clause follows the stop shape clause" % os.path.relpath(p, ROOT))
        check(re.search(r"^\d+\. \*\*Discover the project's conventions\*\*[^\n]*"
                        + re.escape(RESUME_CLAUSE), text, re.M) is not None,
              "%s: resume clause leads into the plan in the discovery step" % os.path.relpath(p, ROOT))
        check(re.search(r"^\d+\. \*\*[^*]*[Vv]erif[^*]*\*\*[^\n]*" + re.escape(DELETE_CLAUSE) + r"\n",
                        text, re.M) is not None,
              "%s: delete clause closes the verify step" % os.path.relpath(p, ROOT))
    else:
        stray = [label for label, clause in (("handoff", HANDOFF_CLAUSE), ("resume", RESUME_CLAUSE),
                                             ("delete", DELETE_CLAUSE)) if clause in text]
        check(not stray, "%s: carries no handoff clauses%s"
              % (os.path.relpath(p, ROOT), (" [found %s]" % ", ".join(stray)) if stray else ""))

# The checklists that measure or write items carry the script clause, each by name: the
# identical-text rule alone stays green while any two copies survive (ADR 0022).
SCRIPT_CARRIERS = {'adopt-pool', 'critique-mcq', 'make-exam'}
for name in sorted(SCRIPT_CARRIERS):
    p = os.path.join(ROOT, 'skills', name, 'SKILL.md')
    check(SCRIPT_CLAUSE in io.open(p, encoding='utf-8').read(),
          "%s: carries the script clause" % os.path.relpath(p, ROOT))

print("\nwordings that lost an argument\n")
for pattern, why in BANNED:
    hits = [os.path.relpath(p, ROOT) for p in DOCS
            if re.search(pattern, io.open(p, encoding='utf-8').read())]
    check(not hits, "absent: %s — %s%s" % (pattern, why, (" [in %s]" % ", ".join(hits)) if hits else ""))

print("\ninstructions that need their companion\n")
for trigger, needs, why in PAIRED:
    for path in DOCS:
        body = io.open(path, encoding='utf-8').read()
        if trigger in body:
            check(needs in body, "%s says %r, so it must also say %r%s"
                  % (os.path.relpath(path, ROOT), trigger, needs,
                     "" if needs in body else " -- " + " ".join(why.split())))

print("\nshape lives in one place\n")
for pattern in LAYOUT_LITERALS:
    hits = sorted({os.path.basename(os.path.dirname(p)) for p in DOCS
                   if os.path.basename(os.path.dirname(p)) != 'assessment-layout'
                   and re.search(pattern, io.open(p, encoding='utf-8').read())})
    check(not hits, "%s appears only in assessment-layout%s" % (pattern, (" [also in %s]" % ", ".join(hits)) if hits else ""))
for pattern in DEFECT_LITERALS:
    hits = sorted({os.path.basename(os.path.dirname(p)) for p in DOCS
                   if os.path.basename(os.path.dirname(p)) != 'item-defects'
                   and re.search(pattern, io.open(p, encoding='utf-8').read())})
    check(not hits, "%s appears only in item-defects%s" % (pattern, (" [also in %s]" % ", ".join(hits)) if hits else ""))
for pattern in OUTCOME_LITERALS:
    hits = sorted({os.path.basename(os.path.dirname(p)) for p in DOCS
                   if os.path.basename(os.path.dirname(p)) != 'learning-outcomes'
                   and re.search(pattern, io.open(p, encoding='utf-8').read())})
    check(not hits, "%s appears only in learning-outcomes%s" % (pattern, (" [also in %s]" % ", ".join(hits)) if hits else ""))

for pattern in STATS_LITERALS:
    hits = sorted({os.path.basename(os.path.dirname(p)) for p in DOCS
                   if os.path.basename(os.path.dirname(p)) != 'analyze-results'
                   and re.search(pattern, io.open(p, encoding='utf-8').read())})
    check(not hits, "%s appears only in analyze-results%s" % (pattern, (" [also in %s]" % ", ".join(hits)) if hits else ""))

for pattern in THAI_OFFICE_LITERALS:
    hits = sorted({os.path.basename(os.path.dirname(p)) for p in DOCS
                   if os.path.basename(os.path.dirname(p)) != 'thai-office-files'
                   and re.search(pattern, io.open(p, encoding='utf-8').read())})
    check(not hits, "%s appears only in thai-office-files%s" % (pattern, (" [also in %s]" % ", ".join(hits)) if hits else ""))

print("\nskills reached by name exist\n")
for path in DOCS:
    name = os.path.relpath(path, ROOT)
    for ref in set(re.findall(r"`([a-z][a-z0-9-]+)` skill", io.open(path, encoding='utf-8').read())):
        check(ref in NAMES, "%s reaches `%s`, which is a skill in this set" % (name, ref))

print("\nlinks resolve\n")
broken = []
for f in glob.glob(os.path.join(ROOT, '**', '*.md'), recursive=True):
    if os.sep + '.git' + os.sep in f:
        continue
    for m in re.finditer(r"\]\(([^)#][^)]*)\)", io.open(f, encoding='utf-8').read()):
        t = m.group(1).split('#')[0]
        if t.startswith(('http', 'mailto')) or not t:
            continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), t))):
            broken.append("%s -> %s" % (os.path.relpath(f, ROOT), t))
check(not broken, "every relative link resolves" + (" [%s]" % "; ".join(broken) if broken else ""))

print("\n%d checks failed" % len(fails) if fails else "\nall checks passed")
sys.exit(1 if fails else 0)
