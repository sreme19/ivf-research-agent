---
name: manuscript-drafter
description: Draft or revise the full manuscript for a study following STROBE and TRIPOD reporting standards. Use when the user asks to write the paper, draft the methods or discussion section, expand the abstract into a manuscript, or prepare a journal submission.
---

# Manuscript drafter

## Before drafting

Read, in order:

1. `studies/<study>/PROTOCOL.md` and `SAP.md` — the manuscript describes what was
   prespecified, and labels anything else as post-hoc.
2. `studies/<study>/outputs/` — every number comes from here.
3. `studies/<study>/literature/evidence-table.md` — the Introduction and Discussion
   are built on this.
4. `reference/strobe-checklist.md` and `reference/tripod-checklist.md`.
5. `venues/aspire-2027/guidelines/journal-fertility-and-reproduction.md` if
   targeting F&R.

## Structure

Follows §51 of the handoff. Introduction establishes eight points in sequence,
ending at the unanswered question. Methods covers design through validation.
Results follow the prespecified table and figure order. Discussion addresses the
eleven points in §52 including, mandatorily, differences from previous compaction
studies and the limitations of retrospective ultrasound data.

## Rules

- Terminology: "dynamic endometrial remodeling", not "stability is desirable".
  Never "receptivity" for an ultrasound measurement.
- A null result is written up with the same care as a positive one.
- Post-hoc analyses are labelled post-hoc, in the text, not only in a footnote.
- Run `protocol-guard` on the draft before circulating it to co-authors.
