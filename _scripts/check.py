#!/usr/bin/env python3
"""Check the invariants this repo's own conventions depend on.

Run: python _scripts/check.py

Every rule here exists because it already drifted once. A convention that
cannot be checked is a convention that will drift again, so each decision
recorded in docs/adr/ that constrains the skill files gets a rule here.
"""
import io, os, re, sys, glob

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
]

# Structure that belongs to the assessment-layout skill and nowhere else (ADR 0007).
LAYOUT_LITERALS = [r"<subject>/assessment", r"assessment/<year>", r"assessment/bank",
                   r"[Rr]ows are topics", r"[Cc]olumns are cognitive levels"]

# The flaw taxonomy belongs to the item-defects skill and nowhere else (ADR 0008).
# It had drifted into two copies at two levels of detail, and the weaker copy is
# what the item-writing skill was held to.
DEFECT_LITERALS = [r"Clang", r"Convergence\.", r"K-type", r"Self-containment"]

# What an outcome must be belongs to the learning-outcomes skill and nowhere
# else (ADR 0010). It reached its second consumer the moment a skill was written
# to author outcomes as well as one to assess against them.
OUTCOME_LITERALS = [r"[Cc]onstructive alignment", r"Mager", r"Unobservable\.", r"Inflated\."]

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
        check(canonical in io.open(p, encoding='utf-8').read(),
              "%s: %s is the canonical wording" % (name, label))

print("\nwordings that lost an argument\n")
for pattern, why in BANNED:
    hits = [os.path.relpath(p, ROOT) for p in DOCS
            if re.search(pattern, io.open(p, encoding='utf-8').read())]
    check(not hits, "absent: %s — %s%s" % (pattern, why, (" [in %s]" % ", ".join(hits)) if hits else ""))

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
