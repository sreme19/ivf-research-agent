---
name: aspire-compliance
description: Check a draft abstract or manuscript against the ASPIRE congress submission rules — title and body word limits, the mandatory Background and Aims / Methods / Results / Conclusions structure, topic category, table and figure limits, prior-presentation policy, and award eligibility. Use whenever the user asks whether a draft complies, is within the word limit, is formatted correctly for ASPIRE, is ready to submit, or asks to check, review, audit or validate an abstract or paper against conference rules. Also use before any ASPIRE submission.
---

# ASPIRE compliance check

Audits a draft against the venue's actual rules and returns a pass/fail report
with exact word counts and the specific edits needed.

## Rule source — read this first, every time

**Read `venues/aspire-2027/guidelines/abstract-rules.md` before checking anything.**

Never check against remembered limits. The rules live in that file so they can be
corrected in one place when the official 2027 document arrives. If that file
disagrees with anything in this skill, the file wins.

Current rules are **inherited from ASPIRE 2026 and not yet officially confirmed
for 2027**. Say so in every report. A draft that passes today can fail if 2027
tightens the limits.

## Procedure

### 1. Identify what is being checked

Congress abstract → the rules in `abstract-rules.md`.
Full manuscript → `journal-fertility-and-reproduction.md` plus
`reference/strobe-checklist.md` and `reference/tripod-checklist.md`.

These are different documents with different rules. Do not apply congress limits
to a manuscript.

### 2. Count words mechanically, not by eye

Do not estimate. Count.

```bash
# Title — must be <= 25 words
# Body — must be <= 300 words, INCLUDING acknowledgements
wc -w <file>
```

Strip the section headings themselves before counting the body only if the
official rules say headings are excluded. They do not say so. **Assume headings
count** until confirmed, and report the count both ways so the user knows the
margin.

Report the count as `287 / 300 — 13 words of headroom`, never as "within limit".

### 3. Run the checklist

**Title**
- [ ] ≤ 25 words
- [ ] Rendered in UPPER CASE
- [ ] Describes the study without overclaiming

**Body**
- [ ] ≤ 300 words including acknowledgements
- [ ] Contains all four sections, in order: Background and Aims, Methods,
      Results, Conclusions
- [ ] Each section is actually present in substance, not a heading with one clause
- [ ] Results contain actual numbers, not "results will be presented"

**Submission metadata**
- [ ] A topic category is chosen from the list of 20
- [ ] ≤ 2 abstracts total from this author across the congress
- [ ] Tables ≤ 3, each ≤ 10 rows × 10 columns
- [ ] Images ≤ 2, ≤ 500 KB, 600 × 800 px, JPG/PNG/GIF

**Eligibility**
- [ ] Prior presentation status established. National/regional prior presentation
      is eligible with disclosure; **international** prior presentation may
      preclude acceptance
- [ ] Presenting author identified and able to register by the deadline

*Young Investigator Award eligibility is NOT checked — the investigator has
declined to pursue it (SPEC.md Amendment 2). Do not raise it.*

### 4. Check scientific compliance too

A rule-compliant abstract can still be a bad abstract. Also run the checks in
`reference/traps-to-avoid.md` — in particular:

- No claim that dynamic endometrial change has never been studied
- No description of ultrasound thickness as "receptivity"
- No ESI cutoff presented as prespecified unless it is in the locked SAP
- **Implantation** reported as the primary endpoint, with its definition stated
  (SPEC.md Amendment 1 changed this from live birth — do not flag its absence as
  an error, but DO flag any wording that implies live birth was measured)
- No number in the draft that is not traceable to a file in `outputs/`

Flag any fabricated or unsourced number as a **blocking** failure. This outranks
every formatting rule in the list.

### 5. Report

```
ASPIRE COMPLIANCE — <draft>, <date>
Rules: ASPIRE 2026 inherited. NOT confirmed for 2027.

TITLE      23 / 25 words        PASS   (not yet upper case — FIX)
BODY      318 / 300 words       FAIL   (cut 18)
STRUCTURE  4 / 4 sections       PASS
CATEGORY   not selected         FAIL

BLOCKING
  1. Body over limit by 18 words. Methods para 2 is the compressible part.
  2. "aOR 1.34" in Results has no source in outputs/. Confirm or remove.

FIX
  3. Title needs UPPER CASE rendering.
  4. Choose a topic category. Suggest "ART, Clinical".

UNVERIFIED FOR 2027
  Word limits, category list, and whether results are mandatory at submission.
```

Order findings by severity. Blocking failures first. Be specific about which
sentence to cut — "trim the methods" is not an actionable finding.

## When rules are unknown

If the official 2027 guidelines have arrived and are in `guidelines/`, use them
and say so. If a needed rule is in neither the official nor the inherited file,
say the rule is unknown. Do not infer a plausible value.
