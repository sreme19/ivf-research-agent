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

## 5. Implantation is the primary endpoint

**SUPERSEDED — see Amendment 1.** Originally recorded as: live birth is primary,
not clinical pregnancy, not implantation.

Current position: **implantation is the sole primary endpoint.** Live birth is
collected where available but is not analysed in this study.

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

### Amendment 1 — 29 August 2026 — primary endpoint changed to implantation

**Changes decision 5.** Primary endpoint changed from live birth to implantation,
at the investigator's direction. Live birth removed from the analysis entirely; it
remains a collected field only.

**Rationale for:**

- **Feasibility, which is the binding constraint.** Live birth requires 9–12 months
  of follow-up after transfer, so a live-birth cohort can only include transfers
  from roughly a year ago or earlier. Implantation is known ~5 weeks post-transfer.
  Against a 6 November 2026 abstract deadline this materially widens the eligible
  cohort.
- **Biological proximity.** Implantation is the event closest to the endometrial
  mechanism ESI is hypothesised to reflect. Live birth adds obstetric and fetal
  causes of failure that have nothing to do with the endometrium at transfer.
  If ESI has real signal, implantation is where it should be most detectable.
- **Statistical power.** A higher event rate yields more events per covariate,
  permitting a more complete adjustment set for the same sample size.

**Rationale against, recorded honestly:**

- The source handoff (§28, §47) explicitly names a softer endpoint in place of live
  birth as a methodological trap. Implantation is softer than clinical pregnancy.
- Live birth is the outcome patients and clinicians care about. Implantation is a
  surrogate.
- The downstream Fertility & Reproduction manuscript will very likely be asked for
  a live-birth analysis. This decision defers that requirement; it does not remove it.

**Mitigations applied:**

- `LIVE_BIRTH`, `GEST_AGE_DELIVERY` and `BIRTH_WEIGHT` are retained as collected but
  unanalysed fields, so the live-birth analysis remains possible later without
  re-extraction.
- The manuscript must state plainly that implantation is an early surrogate and that
  the association with live birth was not assessed. `protocol-guard` enforces this.
- `reference/traps-to-avoid.md` items 6 and 7 rewritten to reflect the change rather
  than being deleted, so the trade-off stays visible.

**Decided by:** investigator. **Recorded by:** Claude, 29 August 2026.

### Amendment 2 — 29 August 2026 — Young Investigator Award not pursued

Award eligibility checks removed from the `aspire-compliance` skill at the
investigator's direction. Best Oral / Best Poster eligibility is unaffected — it is
open to all presenters and requires no action.
