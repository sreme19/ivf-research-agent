# STATISTICAL ANALYSIS PLAN — ESI

**Status: DRAFT. NOT LOCKED.**
**Lock date: [TBD — target 30 September 2026]**
**Locked by: [TBD]**

Once locked, changes are recorded as dated amendments at the foot of this file,
with a stated reason. Never as silent edits. See `CLAUDE.md` rule 4.

---

## Why the lock matters

The most damaging thing this project could do is select an ESI cutoff after seeing
which one produces the best p-value, and present it as prespecified. Reviewers in
this field look for exactly that, because the prior compaction literature is full
of it. The lock date is the defence.

Anything analysed after the lock date that is not in this document is **post-hoc**
and is labelled post-hoc in the manuscript text, not merely in a footnote.

---

## 1. Descriptive analysis

Mean ± SD for approximately normal continuous variables; median (IQR) for skewed;
n (%) for categorical. Compared by live birth vs. no live birth.

**Unadjusted comparisons are descriptive only** and do not support any conclusion
about ESI.

## 2. Primary analysis

ESI (%) as a **continuous** exposure against **live birth**, by multivariable
logistic regression.

Reported as an adjusted odds ratio per clinically meaningful ESI increment
(increment to be prespecified — **[TBD: propose per 5% or per 10%]**) with 95% CI.

**No categorisation. No cutoffs.** See `../../reference/traps-to-avoid.md` item 5.

## 3. Shape of the relationship

**Restricted cubic splines.** X: ESI %. Y: adjusted predicted probability of live
birth.

Knot number and placement prespecified here: **[TBD — conventionally 3–5 knots at
standard percentiles]**.

Determines whether the relationship is linear, U-shaped, J-shaped, threshold,
plateauing, or absent. Likely the paper's most compelling figure.

## 4. Adjustment set

Selected on clinical and causal grounds, **not on univariate p-values**.
Collinearity checked.

| Domain | Covariates |
|---|---|
| Patient | Age, BMI, infertility diagnosis, previous failed transfers |
| Endometrium | Baseline ET1, endometrial pattern, FET protocol |
| Hormonal | Progesterone exposure duration, route/dose, serum P4 where available, estrogen exposure duration |
| Embryo | Developmental day (D5/D6/D7), expansion, ICM, TE, PGT-A/ploidy |

Baseline ET1 must be in the model. Without it, ESI is confounded by starting
thickness by construction.

## 5. Repeated cycles

Women may contribute more than one FET cycle; observations are not independent.

**Prespecified approach: [TBD — DECIDE BEFORE LOCK]**
- Option A: first eligible transfer per woman only (simpler, loses data)
- Option B: all cycles with clustered SEs / mixed effects / GEE (retains data,
  more assumptions)

Recommendation: Option A for the primary analysis, Option B as a sensitivity
analysis. The pilot will show how many women have multiple cycles, which should
inform the choice — decide once that number is known, then lock.

## 6. Incremental prediction

| Model | Contents |
|---|---|
| A | Baseline endometrial thickness alone |
| B | + patient characteristics |
| C | + embryo characteristics |
| D | + ESI |

Compared on: AUC/ROC discrimination; calibration; Brier score; likelihood-based
comparison; decision-curve analysis if a clinical tool is proposed.

**The question is not whether ESI reaches p < 0.05. It is whether knowing ESI adds
clinically meaningful information.** A statistically significant ESI that moves the
AUC from 0.641 to 0.648 is a null result in substance and should be reported as one.

If this section is executed, **TRIPOD applies** — including reporting the full
model coefficients and intercept.

## 7. Prespecified subgroups

Deliberately limited, to avoid data dredging. **These four only:**

1. Single euploid blastocyst transfers *(most important if powered)*
2. FET protocol — HRT/programmed vs natural/modified natural
3. Embryo day — D5 vs D6
4. Baseline ET1 stratum *(continuous modelling preserved in parallel)*

Exploratory, labelled as such: age; adenomyosis; previous implantation failure;
serum P4.

## 8. Interaction

Whether embryo quality modifies the ESI association is tested as a **formal
interaction term**. Never inferred from comparing subgroup p-values.

## 9. Missing data

Percentage missing reported per variable. Mechanism described. Multiple imputation
by chained equations where appropriate, with complete-case analysis as a
sensitivity analysis. **Missing is never coded as zero.**

## 10. Validation

Internal: **bootstrap** preferred over a 70/30 split — it uses the data more
efficiently and yields optimism-corrected performance.

Stronger, if the study period allows: **temporal validation** — earlier years for
development, most recent year(s) for validation. Preferred over random splitting
of one historical population.

Best case: external validation at a different centre.

## 11. Software

R. `rms` (splines, validation), `pROC` (discrimination), `dcurves` (DCA), `mice`
(imputation). Version numbers recorded at lock.

## 12. Significance

Two-sided α = 0.05. Multiplicity handling across subgroups: **[TBD — or state
explicitly that subgroup analyses are exploratory and unadjusted, which is
acceptable if declared]**.

---

## Items that MUST be resolved before locking

- [ ] Formal sample-size / power calculation from a statistician
- [ ] ESI increment for the reported odds ratio
- [ ] Spline knot number and placement
- [ ] Repeated-cycle approach (§5)
- [ ] Ongoing-pregnancy gestational-age threshold
- [ ] Clinical-pregnancy definition
- [ ] Multiplicity position (§12)
- [ ] Whether the prediction-model comparison (§6) is in scope for this paper

## Amendments

_None. Plan not yet locked._
