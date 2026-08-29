# SPEC.md — locked design decisions

Decisions recorded here are settled. Reopening one requires a stated reason and a
dated amendment at the bottom of this file. Written 29 August 2026.

---

## 1. Repo separates venue from study

`venues/` holds congresses and journals with their rules and history. `studies/`
holds research questions with their protocols and data. They are paired only in
`venues/<venue>/submissions/`.

**Why:** the ESI study is going to two places (ASPIRE 2027 abstract, then a
journal manuscript), and ASPIRE will host future studies. Any structure that nests
one inside the other has to be rebuilt the first time either is reused. This was
stated as an explicit requirement — the repo is for future publications too.

## 2. Zero API key

No model calls originate from this package. Reasoning happens in-session via
`.claude/skills/`; the repo persists results deterministically.

**Why:** matches the established pattern in `job-hunt-agent`,
`finance-controls-agent` and `ad-management-agent`. It also keeps a repo that will
sit adjacent to clinical data free of any outbound network path.

## 3. Analysis in R

`rms` for restricted cubic splines, `pROC` for discrimination, `dcurves` for
decision-curve analysis, `mice` for multiple imputation.

**Why:** the SAP calls for spline modeling, calibration assessment and DCA. R's
tooling for these is the de facto standard in clinical prediction research and
reviewers recognise it. Python is the portfolio norm elsewhere, but here the
methods tooling wins.

**Status:** provisional — no analysis code exists yet, so this is cheap to change.

## 4. Local git only, no remote

**Why:** the repo sits next to PHI. A remote gets added only after the gitignore
has been proven against a real extract without leaking. Not before.

## 5. Live birth is the primary endpoint

Not clinical pregnancy. Not implantation.

**Why:** it is the clinically meaningful outcome, and using anything softer is a
known reviewer objection in this literature. Secondary endpoints are collected
but do not become the headline if the primary is null.

## 6. ESI is modeled continuously first

No categories, no cutoffs, at the primary-analysis stage. Thresholds — if any —
emerge from spline modeling, not from the analyst.

**Why:** post-hoc cutoff selection presented as prespecified is the failure mode
that would sink this paper in review. See `reference/traps-to-avoid.md`.

## 7. Direction-neutral hypothesis

The study does not assume compaction is beneficial. A rigorous null is a
publishable result.

**Why:** prior compaction literature is genuinely conflicting. Committing to a
direction in advance invites confirmation bias in a retrospective dataset where
analytic choices are plentiful.

## 8. inbox/ is non-authoritative

Raw handoffs, PDFs and notes land there dated and untouched. Facts become
authoritative only when compiled into `venues/` or `studies/` with provenance.

**Why:** so that a fact's source is always recoverable, and so revisions to source
material don't silently overwrite reasoning that was built on the earlier version.

---

## Open decisions

| # | Decision | Blocked on |
|---|---|---|
| A | Whether the study is retrospective or must become prospective | ET2 feasibility pilot |
| B | Abstract word limit and structure | Official ASPIRE 2027 guidelines |
| C | Single-centre vs multicentre | Data access confirmation |
| D | First-transfer-only vs clustered analysis for repeated cycles | Pilot: how many women have >1 FET |
| E | Whether a euploid-only subgroup is powered | Pilot: PGT-A availability |

---

## Amendments

_None yet._
