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
n (%) for categorical. Compared by **implantation vs. no implantation**.

**Unadjusted comparisons are descriptive only** and do not support any conclusion
about ESI.

## 2. Primary analysis

ESI (%) as a **continuous** exposure against **implantation** (primary endpoint,
see `PROTOCOL.md`), by multivariable logistic regression.

Implantation is defined as the presence of at least one intrauterine gestational
sac on transvaginal ultrasound at the centre's standard first scan. **[Definition
pending clinician confirmation — must be fixed before lock.]** Cycles that were
β-hCG negative and therefore never scanned are coded as implantation failures
(`0`), not as missing.

Reported as an adjusted odds ratio per clinically meaningful ESI increment
(increment to be prespecified — **[TBD: propose per 5% or per 10%]**) with 95% CI.

**No categorisation. No cutoffs.** See `../../reference/traps-to-avoid.md` item 5.

## 3. Shape of the relationship

**Restricted cubic splines.** X: ESI %. Y: adjusted predicted probability of
implantation.

Knot number and placement prespecified here: **[TBD — conventionally 3–5 knots at
standard percentiles]**.

Determines whether the relationship is linear, U-shaped, J-shaped, threshold,
plateauing, or absent. Likely the paper's most compelling figure.

## 4. Adjustment set

Selected on clinical and causal grounds, **not on univariate p-values**.
Collinearity checked.

| Domain | Covariates |
|---|---|
| Patient | Age, BMI, infertility diagnosis |
| Endometrium | Baseline ET1, endometrial pattern, FET protocol |
| Hormonal | Progesterone exposure duration, route/dose, serum P4 where available, estrogen exposure duration |
| Embryo | Developmental day (D5/D6/D7), expansion, ICM, TE, PGT-A/ploidy |

Baseline ET1 must be in the model. Without it, ESI is confounded by starting
thickness by construction.

**Note on the endpoint change.** With implantation rather than live birth as the
outcome, the event rate rises substantially — implantation occurs in a larger
fraction of transfers than live birth does. More events per covariate means the
adjustment set can be more generous before overfitting becomes a concern. The
statistician should recalculate events-per-variable on the implantation rate, not
a live-birth rate.

## 5. Repeated cycles — RESOLVED 29 August 2026

**Not applicable by design.** The cohort is restricted to women in their **first IVF
cycle**. Each woman therefore contributes exactly one transfer, and observations are
independent at the patient level. No clustering, mixed-effects or GEE approach is
required for repeated cycles.

**Clustering by centre still applies.** This is a multicentre study; `SITE_ID` is
included as a covariate or random effect (§4). Do not confuse the two — resolving
patient-level clustering does not resolve site-level clustering.

**Consequences for §4.** `PREV_IVF`, `PREV_TRANSFER` and `PREV_IMPLANTATION_FAILURE`
are constant by construction and are removed from the adjustment set. "Previous
failed transfers" is likewise removed. Retaining a constant in a regression model
is not merely redundant, it will fail to estimate.

**Consequence for §7.** The exploratory "previous implantation failure" subgroup is
removed — there is no such subgroup in this cohort.

**Consequence for generalisability.** Findings apply to first-cycle patients only.
They cannot be extrapolated to women with recurrent implantation failure, which is
arguably the population in which endometrial factors matter most. This must appear
in the Limitations, not be left implicit.

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

Note that a model predicting implantation is predicting an earlier, more
endometrium-proximal event than live birth. If ESI has any real signal, this is
where it should be most visible — which cuts both ways: a null result here is
correspondingly harder to attribute to endpoint dilution.

If this section is executed, **TRIPOD applies** — including reporting the full
model coefficients and intercept.

## 7. Prespecified subgroups

Deliberately limited, to avoid data dredging. **These four only:**

1. Single euploid blastocyst transfers *(most important if powered)*
2. FET protocol — HRT/programmed vs natural/modified natural
3. Embryo day — D5 vs D6
4. Baseline ET1 stratum *(continuous modelling preserved in parallel)*

Exploratory, labelled as such: age; adenomyosis; serum P4.
*(Previous implantation failure removed — excluded by design, see §5.)*

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
- [ ] **Implantation definition — gestational sac only, or sac plus fetal pole?**
      *(Primary endpoint. Nothing locks until this does.)*
- [ ] Confirmation that β-hCG-negative, never-scanned cycles are coded `0`, not `NA`
- [ ] Ongoing-pregnancy gestational-age threshold
- [ ] Clinical-pregnancy definition
- [ ] Multiplicity position (§12)
- [ ] Whether the prediction-model comparison (§6) is in scope for this paper

## Amendments

_None. Plan not yet locked._

**Pre-lock revision, 29 August 2026:** primary endpoint changed from live birth to
implantation at the investigator's direction. Made before the lock date, so this is
a revision to a draft rather than a formal amendment. Recorded here for the audit
trail. See `SPEC.md` Amendment 1 for rationale.
