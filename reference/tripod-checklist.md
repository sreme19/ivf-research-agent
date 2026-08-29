# TRIPOD — reporting standard for prediction models

Applies if the study develops the Model A/B/C/D comparison described in §40 of the
handoff — i.e. if ESI is presented as adding predictive value, not merely as being
associated with live birth.

Official: https://www.tripod-statement.org/

## When TRIPOD applies here

If the paper only reports an adjusted odds ratio for ESI, STROBE suffices. The
moment it claims ESI **improves prediction** — AUC comparison, calibration, Brier
score, decision-curve analysis — TRIPOD applies and reviewers will expect it.

Decide which paper this is before drafting. Both are legitimate; mixing them
produces a paper that satisfies neither checklist.

## Core requirements

**Title and abstract** — identify the study as developing and/or validating a
prediction model; state the outcome and the population.

**Methods**
- Source of data, separately for development and any validation set
- Participants, eligibility, setting, dates
- Outcome definition, and whether outcome assessment was blinded to predictors
- All predictors, with how and when they were measured
- Sample size rationale
- Missing data handling — **multiple imputation, not complete-case, unless
  justified**
- How predictors were handled in the analysis, including any selection
- Model type, building procedure, and internal validation method
- Measures of model performance

**Results**
- Flow of participants, with a diagram
- Characteristics, including number of outcome events and missingness
- **The full model presented — all regression coefficients and the intercept.**
  This is the item most commonly omitted and it is what makes a model usable.
- Performance measures with confidence intervals
- Any model updating

**Discussion** — limitations, interpretation with reference to validation
performance, and how the model could be used in practice.

## Items this study is most likely to fail

- **Full model presentation.** Report the coefficients, not just the AUC.
- **Internal validation.** Bootstrap is preferred over a 70/30 split (§43).
- **Calibration.** Discrimination alone is insufficient. A model with AUC 0.65 and
  good calibration may be more useful than one with AUC 0.68 and poor calibration.
- **Optimism correction.** An apparent AUC from the development sample is
  optimistic and must be corrected.
