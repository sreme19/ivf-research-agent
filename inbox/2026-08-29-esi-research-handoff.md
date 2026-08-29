# IVF Research Project — Full Handoff

**Source:** provided by user 29 August 2026, produced by a prior AI session.
**Status:** raw source material. Compiled into `studies/esi-fet/`.
**Note:** the Excel workbook referenced in §56 was NOT provided.

---

## 1. Research objective

The user is planning an IVF research project initially intended for ASPIRE conference submission, with the intention that the work should be sufficiently rigorous to subsequently develop into a full peer-reviewed publication.

The initial exploration covered ovarian stimulation, embryo grading, endometrial thickness, endometrial receptivity and transfer success.

The final selected research direction is: **Endometrial Stability Index (ESI)**

The central idea is to investigate whether the dynamic change in endometrial thickness during progesterone exposure is associated with implantation, pregnancy and, most importantly, live birth following frozen embryo transfer.

The project should not be framed as merely another study of "Endometrial thickness and pregnancy rate." That relationship has already been extensively studied. Instead, the study focuses on the dynamic behavior of the endometrium between progesterone initiation and embryo transfer.

## 2. Proposed publication title

Preferred scientific title:
> Dynamic Endometrial Remodeling During Progesterone Exposure and Live Birth Following Single Blastocyst Frozen Embryo Transfer: Development and Validation of an Endometrial Stability Index

Alternative:
> Endometrial Stability Index During Progesterone Exposure and Its Association With Live Birth Following Single Blastocyst Frozen Embryo Transfer: A Retrospective Cohort Study

Conference-style title:
> Beyond Endometrial Thickness: Does Dynamic Endometrial Change During Progesterone Exposure Predict IVF Success?

## 3. Scientific rationale

Traditionally, endometrial assessment before frozen embryo transfer relies heavily on absolute endometrial thickness. For example: endometrium = 8.5 mm, triple-line → considered acceptable for transfer.

However, two women can both have a 9-mm endometrium before progesterone and subsequently demonstrate very different endometrial behavior.

- Patient A: 9.0 mm before progesterone → 8.9 mm on transfer day. Change = −0.1 mm
- Patient B: 9.0 mm before progesterone → 7.7 mm on transfer day. Change = −1.3 mm

The conventional approach would initially classify both women as having approximately the same endometrial thickness. The hypothesis behind ESI is that the dynamic response to progesterone may contain additional biological/prognostic information.

Previous literature has investigated endometrial compaction/change after progesterone, with conflicting results. Some studies reported associations with improved outcomes, whereas others—including large cohorts and analyses of euploid transfers—have found little or no association.

Therefore, this study must not claim that endometrial thickness change itself has never been studied. The novelty should instead come from:

- standardized measurements
- continuous quantification of endometrial change
- development of ESI
- progesterone timing
- embryo-quality adjustment
- single blastocyst transfer
- live birth as the primary endpoint
- nonlinear/spline analysis
- predictive modeling
- subgroup analysis
- ideally prospective or temporal validation

## 4. Primary research question

Among women undergoing single blastocyst frozen embryo transfer, is the percentage change in endometrial thickness from progesterone initiation to embryo transfer independently associated with live birth?

Secondary question: Does incorporating dynamic endometrial change improve prediction of live birth beyond baseline endometrial thickness, patient characteristics and embryo characteristics?

## 5. Primary hypothesis

The study should remain direction-neutral. Do NOT hypothesize that endometrial compaction is automatically beneficial.

- **Null hypothesis:** Endometrial thickness change following progesterone initiation is not independently associated with live birth.
- **Alternative hypothesis:** The magnitude and/or direction of endometrial thickness change during progesterone exposure is independently associated with live birth after accounting for patient, hormonal, treatment and embryo characteristics.

The analysis should determine whether: compaction is favorable, stability is favorable, expansion is favorable, there is an optimal range, extreme change in either direction is unfavorable, or ESI has no clinically useful association.

## 6. Study design

Initial design: **Retrospective cohort study**, preferably multicentre if sufficiently standardized data are available.

Ideal target: ≥1,500–2,000 eligible single-blastocyst FET cycles. This is a practical target rather than a formal power calculation. A statistician should perform the formal sample-size/power calculation based on expected live-birth rate, expected effect size, number of predictors, anticipated missing data.

If possible, subsequently perform:
- **Phase 1 — Retrospective development cohort.** Develop the ESI model using historical cases.
- **Phase 2 — Prospective/temporal validation cohort.** Standardize ultrasound and hormone measurements and test the findings on subsequent patients.

## 7. Preferred study population

Primary cohort: Women undergoing single blastocyst frozen embryo transfer using autologous oocytes.

Preferably use: single embryo transfers; blastocyst transfers; D5/D6, with D7 recorded separately; standardized FET protocols; known embryo morphology; known pregnancy outcome; known live-birth outcome; ET measurements at the required two time points.

If available, create a secondary cohort consisting of single euploid blastocyst transfers. This is scientifically important because embryo aneuploidy is a major confounder when studying endometrial effects.

## 8. Suggested inclusion criteria

- Age approximately 21–45 years
- Frozen blastocyst transfer
- Autologous oocyte cycle
- Single blastocyst transfer for primary analysis
- Endometrial measurement immediately before/around progesterone initiation
- Repeat endometrial measurement on/around embryo-transfer day
- Known progesterone exposure duration
- Known embryo grade
- Known pregnancy outcome
- Known live-birth outcome

Final eligibility definitions must be prespecified before analysis.

## 9. Suggested exclusions

donor-oocyte cycles; gestational carriers; major Müllerian anomalies; untreated hydrosalpinx; untreated significant submucosal fibroid; significant untreated endometrial polyp; severe intrauterine adhesions; cycles without standardized ET measurements; missing embryo information; missing transfer outcome; double embryo transfers from the primary analysis.

Conditions such as adenomyosis, endometriosis and fibroids should generally be recorded rather than automatically excluded, unless there is a strong clinical reason, because they can be adjusted for or studied as subgroups.

## 10. Core exposure: Endometrial Stability Index

Two standardized endometrial measurements are required.

**ET1** — Endometrial thickness immediately before progesterone initiation. Preferably within 24 hours before progesterone initiation. Record in millimeters to one decimal place. Example: `9.4 mm`

## 11. ET2

Endometrial thickness on embryo-transfer day. Ideally measured before transfer, using the same standardized ultrasound methodology, as close to transfer as operationally feasible. Example: `8.6 mm`

## 12. Absolute endometrial change

ΔET = ET2 − ET1

Example: ET1 = 9.4 mm, ET2 = 8.6 mm → ΔET = −0.8 mm

Interpretation: Negative = thickness decreased; Zero = stable; Positive = thickness increased.

## 13. Endometrial Stability Index

Primary exposure:

    ESI (%) = [(ET2 − ET1) / ET1] × 100

Example: ET1 = 9.4 mm, ET2 = 8.6 mm → ESI = −8.5%

Interpretation: ESI < 0 → compaction/reduction; ESI ≈ 0 → stability; ESI > 0 → expansion.

However, these descriptions should not initially be converted into arbitrary clinical categories. ESI should first be analyzed as a **continuous variable**. The data should determine whether clinically relevant thresholds exist.

## 14. Exploratory daily ESI

Because progesterone exposure duration can vary, an exploratory variable can be calculated:

    Daily ESI = ESI / progesterone exposure days

However, Daily ESI should not be the primary exposure. The primary variable remains percentage change between the two standardized measurements.

## 15. Ultrasound standardization

This is critical for publication. Preferably use: transvaginal ultrasound; standardized sagittal midline uterine plane; maximum double-layer endometrial thickness; exclusion of myometrium; measurement to 0.1 mm; same machine/model where possible; standardized bladder conditions; trained sonographers/clinicians; defined measurement protocol.

Record: date of ET1, exact time where possible; date of ET2, exact time; operator/sonographer ID; machine ID/model if multiple machines are used.

If possible, randomly select approximately 100 scans for repeat independent measurement. Calculate the **intraclass correlation coefficient (ICC)** for endometrial thickness. For categorical endometrial pattern, **Cohen's kappa** can assess interobserver agreement.

## 16. Endometrial pattern

Record at both ET1 and ET2. Suggested coding:

1. Triple-line
2. Intermediate
3. Homogeneous/echogenic
4. Other/uncertain

Do not use subjective categories such as "good lining", "bad lining", "satisfactory lining".

## 17. Optional advanced ultrasound variables

If routinely available, collect:

- **3D endometrial volume** at ET1 and ET2
- **Power Doppler**: VI (Vascularization Index), FI (Flow Index), VFI (Vascularization Flow Index) at both time points where available
- **Endometrial/subendometrial blood flow** according to a predefined standardized methodology
- **Endometrial/uterine peristalsis** — if measured, record waves/minute rather than simply "normal/abnormal"

These are useful but should not prevent the main ESI study if they are unavailable.

## 18. Patient variables to collect

One row should represent one FET cycle.

**Demographics:** Study ID; coded patient ID if needed; age at FET; age at oocyte retrieval; BMI

**Reproductive history:** gravidity; parity; previous live birth; number of previous miscarriages; duration of infertility; primary vs secondary infertility; number of previous IVF cycles; number of previous embryo transfers; previous implantation failure

## 19. Infertility diagnosis

Prefer separate binary variables, because multiple diagnoses can coexist. Collect 0/1 for: male factor; tubal factor; PCOS; endometriosis; diminished ovarian reserve; unexplained infertility; uterine factor; other.

Do not force each woman into only one diagnosis if multiple factors are present.

## 20. Uterine/endometrial history

Collect: adenomyosis; fibroid; submucosal fibroid; endometrial polyp; hydrosalpinx; chronic endometritis; previous hysteroscopy; previous adhesiolysis; septum surgery; previous endometrial pathology.

Where possible use: 0 = No, 1 = Yes, blank/NA = unavailable. **Do not code missing information as "No."**

## 21. FET protocol

Record: Natural; Modified natural; HRT/programmed; Ovulation induction; Other.

Protocol is a potentially important confounder. Do not simply pool all FET protocols without adjustment. Prespecified subgroup analysis by protocol may be appropriate.

## 22. Estrogen information

For programmed/HRT cycles collect: estrogen preparation; route; dose/day; date started; duration before progesterone; cumulative dose if reliably available.

Possible routes: oral; transdermal; vaginal; combination.

If serum estradiol is routinely measured: E2 at progesterone initiation; E2 before transfer; date/time of sample.

Do not introduce non-routine tests solely to complete a retrospective dataset.

## 23. Progesterone information

Very important. Collect: progesterone initiation date; exact initiation time; route; formulation; dose; frequency; total daily dose.

Routes may include: vaginal; intramuscular; subcutaneous; oral; combination.

Calculate exact progesterone exposure duration before embryo transfer. Where possible, calculate in hours, not only days.

## 24. Serum progesterone

If routinely available, record P4 before transfer in ng/mL. Also record: blood collection date; blood collection time; time since last progesterone dose.

The last point matters because serum concentration varies according to route and timing.

## 25. Embryo variables

These are mandatory for a strong paper.

**Developmental day:** D5, D6, D7

**Gardner components:** expansion grade 1–6; ICM: A/B/C; TE: A/B/C

Also retain the original overall grade. Examples: 4AA, 4AB, 3BB, 5AA.

Do not only collapse embryos into "good" and "poor" during data collection. Always retain the raw morphology. Categories can be generated later.

## 26. PGT-A information

Record PGT-A performed 0/1. If performed: euploid; aneuploid; mosaic; other/indeterminate.

A prespecified single euploid blastocyst subgroup is strongly desirable if the sample is large enough.

## 27. Embryo-transfer variables

Collect: transfer date; exact transfer time; single embryo transfer 0/1; transfer operator; catheter type if available; ultrasound-guided transfer 0/1; difficult transfer 0/1; number of attempts; blood on catheter 0/1; mucus on catheter 0/1; transfer depth if routinely available.

These are secondary variables but can help control for procedural causes of implantation failure.

## 28. Primary outcome

**Live birth per embryo transfer.** Code: `0 = No`, `1 = Yes`

This is preferable to clinical pregnancy because live birth is the clinically meaningful endpoint.

## 29. Secondary outcomes

Positive β-hCG 0/1; Biochemical pregnancy 0/1; Clinical pregnancy 0/1 (predefined definition); Implantation (for single embryo transfer) 0/1; Ongoing pregnancy 0/1 (define gestational-age threshold before analysis); Miscarriage 0/1.

Also collect where available: gestational age at delivery; birth weight.

## 30. Database structure

One row = one FET cycle. Never use one row per patient if a patient has multiple cycles unless the dataset is specifically being transformed for analysis.

Important raw columns include:

```text
STUDY_ID
AGE_FET
BMI
GRAVIDITY
PARITY
PREV_LIVE_BIRTH
PREV_MISCARRIAGE
INFERTILITY_YEARS
PREV_IVF
PREV_TRANSFER
PREV_IMPLANTATION_FAILURE

MALE_FACTOR
TUBAL_FACTOR
PCOS
ENDOMETRIOSIS
DOR
UNEXPLAINED
UTERINE_FACTOR
ADENOMYOSIS
FIBROID
POLYP
HYDROSALPINX
CHRONIC_ENDOMETRITIS

FET_PROTOCOL

ESTROGEN_ROUTE
ESTROGEN_DOSE
ESTROGEN_START_DATE

PROG_START_DATE
PROG_ROUTE
PROG_DOSE
P_DAYS
P4_PRE_TRANSFER
P4_SAMPLE_TIME
E2_PRE_TRANSFER

ET1_DATE
ET1_MM
PATTERN_E1
ET1_VOLUME
ET1_VI
ET1_FI
ET1_VFI
ET1_PERISTALSIS

ET2_DATE
ET2_MM
PATTERN_E2
ET2_VOLUME
ET2_VI
ET2_FI
ET2_VFI
ET2_PERISTALSIS

DELTA_ET_MM
ESI_PERCENT
ESI_DAILY_PERCENT

EMBRYO_DAY
EMBRYO_EXPANSION
ICM_GRADE
TE_GRADE
EMBRYO_GRADE
PGT_STATUS
PLOIDY

SINGLE_EMBRYO_TRANSFER
TRANSFER_DATE_TIME
TRANSFER_OPERATOR
US_GUIDED_TRANSFER
DIFFICULT_TRANSFER
BLOOD_CATHETER
MUCUS_CATHETER

BETA_HCG
CLINICAL_PREGNANCY
ONGOING_PREGNANCY
IMPLANTATION
MISCARRIAGE
LIVE_BIRTH
GEST_AGE_DELIVERY
BIRTH_WEIGHT
```

## 31. Data-entry principles

Store raw data, not derived categories.

- Record `ET1 = 8.7`, not `ET1 = adequate`
- Record `Embryo = 4AB`, not only `Embryo = good`
- Record `P4 = 13.8 ng/mL`, not `P4 = normal`

Derived categories can always be created later. Raw information cannot be reconstructed once discarded.

## 32. Missing data

Use a consistent approach: blank/NA = unavailable; 0 = confirmed absence; 1 = confirmed presence. **Never treat missing information as zero.**

The eventual statistical analysis should describe: percentage missing per variable; missing-data mechanism; complete-case analysis and/or multiple imputation where appropriate.

## 33. Do not manually calculate ESI

Keep ET1 and ET2 as raw values. Then calculate ESI automatically using Excel/R/Python/SPSS/Stata. This reduces transcription errors.

## 34. Primary statistical analysis

First describe the cohort using: mean ± SD for approximately normally distributed continuous variables; median and IQR for skewed variables; n (%) for categorical variables.

Compare live birth versus no live birth. But unadjusted comparisons are only descriptive.

## 35. Primary ESI analysis

ESI should initially be modeled as a **continuous exposure** against live birth using multivariable logistic regression. Report an interpretable effect size, such as adjusted odds ratio per clinically meaningful ESI increment, with 95% confidence intervals.

## 36. Do not initially impose arbitrary cutoffs

Avoid starting with: 10% compaction = good; ±5% = stable; 5% expansion = poor.

Those thresholds would be arbitrary unless justified independently. Instead, allow the data to reveal the relationship.

## 37. Restricted cubic spline analysis

Strongly recommended. X-axis: ESI %. Y-axis: adjusted predicted probability/odds of live birth.

This can determine whether the relationship is linear, U-shaped, J-shaped, threshold-based, plateauing, or absent. This may be one of the most visually compelling figures in the paper.

## 38. Multivariable adjustment

Important candidate confounders include:

- **Patient:** age; BMI; infertility diagnosis; previous failed transfers
- **Endometrium:** baseline ET1; endometrial pattern; FET protocol
- **Hormonal:** progesterone exposure duration; progesterone route/dose; serum progesterone where available; estrogen exposure duration
- **Embryo:** D5/D6/D7; expansion; ICM; TE; PGT-A/euploid status

Variable selection should be clinically and causally justified rather than based only on univariate P values. Check for collinearity.

## 39. Important repeated-cycle issue

If the same woman contributes more than one FET cycle, observations are not fully independent. Therefore either use only the first eligible transfer per woman for the primary analysis, or use an appropriate clustered/mixed-effects/GEE approach. This decision should be prespecified.

## 40. Prediction-model comparison

A potentially strong component of the paper is to determine whether ESI provides incremental predictive information.

- **Model A:** Baseline endometrial thickness alone
- **Model B:** Thickness + patient characteristics
- **Model C:** Thickness + patient + embryo characteristics
- **Model D:** Thickness + patient + embryo characteristics + ESI

Compare: AUC/ROC discrimination; calibration; Brier score where appropriate; likelihood-based model comparison; potentially decision-curve analysis if developing a clinical prediction tool.

The key question is not merely whether ESI has P < 0.05. It is: does knowing ESI actually add clinically meaningful information?

## 41. Important subgroup analyses

Prespecify only a limited number to avoid data dredging. Most useful:

- **Single euploid blastocyst transfers** — very important if sample size permits
- **FET protocol** — HRT/programmed vs natural/modified natural
- **Embryo day** — D5 vs D6
- **Baseline endometrial thickness** — thin / conventional-adequate / thicker, but preferably preserve continuous modeling

Potential exploratory analyses: age; adenomyosis; previous implantation failure; progesterone level.

## 42. Endometrial–embryo interaction

A particularly interesting secondary question: does the importance of ESI depend on embryo quality?

For example: excellent embryo + favorable ESI; excellent embryo + unfavorable ESI; lower-grade embryo + favorable ESI; lower-grade embryo + unfavorable ESI.

Statistically, this should be tested as an **interaction**, not inferred simply by comparing subgroup P values.

## 43. Internal validation

If developing a prediction model, use bootstrap validation preferably, or cross-validation. A simple 70/30 random split can be used with a sufficiently large dataset, but bootstrap validation often uses data more efficiently.

## 44. Stronger validation strategy

If historical data are available: development on earlier years, temporal validation on more recent year(s). Conceptually: 2023–2025 → development, 2026 → validation.

Temporal validation is stronger than randomly splitting the same historical population. Best case: external validation at a different IVF centre.

## 45. Prospective validation

An excellent follow-up study would prospectively standardize: ET1 timing; ET2 timing; ultrasound machine; measurement technique; operator training; progesterone initiation; serum P4 timing; embryo morphology; transfer procedure. Then test whether the retrospective ESI finding replicates.

## 46. What would make the study genuinely valuable?

A positive result alone is not enough. The study becomes compelling if it can demonstrate something like:

> Endometrial thickness alone had poor discrimination for live birth, whereas dynamic endometrial remodeling provided independent prognostic information after adjustment for embryo quality and treatment characteristics.

Alternatively, a rigorous negative result is also valuable:

> Endometrial thickness changes substantially after progesterone, but this dynamic change does not independently predict live birth once embryo and patient characteristics are considered.

That would challenge the clinical usefulness of measuring transfer-day endometrial change. **Do not force a positive result.**

## 47. Major methodological traps to avoid

Do not:

- assume compaction is beneficial
- choose ESI cutoffs after seeing which gives the best P value and present them as prespecified
- use clinical pregnancy as the only endpoint
- ignore live birth
- mix cleavage-stage and blastocyst transfers indiscriminately
- mix single and double embryo transfers in the primary analysis
- mix donor and autologous cycles without justification
- ignore embryo morphology
- ignore PGT status
- ignore FET protocol
- ignore progesterone exposure duration
- allow ET1/ET2 measurement timing to vary substantially without recording it
- label ultrasound measurements as direct biological "receptivity"
- claim that dynamic endometrial change has never previously been studied

## 48. Terminology

The project uses the term Endometrial Stability Index (ESI). However, "stability" should not imply that no change is necessarily desirable. Scientifically, the manuscript should frequently describe the phenomenon as **dynamic endometrial remodeling**. This is more neutral.

Likewise, avoid claiming that ESI directly measures "endometrial receptivity." Ultrasound thickness is a surrogate phenotype, not a direct molecular measurement of receptivity.

## 49. Proposed manuscript objective

> To evaluate the association between dynamic changes in endometrial thickness during progesterone exposure and live birth following single blastocyst frozen embryo transfer, and to determine whether an Endometrial Stability Index provides incremental prognostic information beyond baseline endometrial thickness, patient characteristics, and embryo morphology.

## 50. Proposed primary endpoint

Live birth per single blastocyst frozen embryo transfer.

Secondary endpoints: positive β-hCG; implantation; clinical pregnancy; ongoing pregnancy; miscarriage.

## 51. Proposed manuscript structure

**Introduction** — establish:

1. Endometrial assessment is central to FET preparation.
2. Thickness is commonly used clinically.
3. Absolute ET has limited ability to predict implantation/live birth.
4. Progesterone causes structural and functional endometrial transformation.
5. Endometrial thickness can change after progesterone exposure.
6. Previous studies of compaction/remodeling have reported conflicting findings.
7. The clinical significance of the magnitude and direction of dynamic ET change, particularly after controlling for embryo characteristics, remains uncertain.
8. Therefore, evaluate ESI against live birth.

**Methods** — include: study design; setting/centres; study period; ethics approval; inclusion/exclusion criteria; FET preparation; progesterone protocol; ultrasound methodology; ET1 definition; ET2 definition; ESI formula; embryo grading; PGT methodology if relevant; transfer procedure; outcome definitions; statistical plan; missing-data handling; sensitivity analyses; validation.

**Results** — suggested sequence:

- Table 1: Baseline characteristics by live-birth outcome
- Table 2: Endometrial and embryo characteristics
- Figure 1: Patient flow diagram
- Figure 2: Distribution of ESI
- Figure 3: Restricted cubic spline — ESI → adjusted live-birth probability
- Table 3: Multivariable logistic regression
- Figure 4: ROC/model comparison with and without ESI
- Table 4: Prespecified subgroup/sensitivity analyses
- If euploid numbers are adequate — Figure/Table 5: Single euploid blastocyst cohort

## 52. Discussion

Should address: whether ESI is independently associated with live birth; whether the relationship is linear/nonlinear; whether an optimal range exists; whether baseline ET remains important; whether ESI adds predictive value; whether embryo quality modifies the association; whether results persist in euploid embryos; differences from previous compaction studies; measurement reproducibility; clinical utility; limitations of retrospective ultrasound data.

## 53. Potential final conclusion — only if supported

If positive:
> Dynamic endometrial remodeling during progesterone exposure is independently associated with live birth following single blastocyst FET and provides prognostic information beyond baseline endometrial thickness.

If negative:
> Dynamic endometrial thickness change during progesterone exposure does not provide clinically meaningful prediction of live birth beyond established patient and embryo characteristics.

Both can be scientifically valuable.

## 54. Ethics and governance

Before extracting identifiable clinical data: obtain appropriate institutional ethics/IRB approval or exemption; determine whether retrospective consent waiver applies; de-identify patient data; maintain a secure linkage file separately if necessary; avoid patient names, phone numbers, addresses, hospital IDs or other direct identifiers in the research dataset.

Use a coded `STUDY_ID` for analysis.

## 55. Reporting standard

For the observational component, plan the manuscript around **STROBE**. If a formal multivariable prediction model is developed, also follow the relevant **TRIPOD** reporting framework.

The statistical analysis plan should ideally be finalized before looking for optimal ESI cutoffs.

## 56. Current Excel data-collection tool

An Excel workbook was described as already created for this project, containing: FET Data sheet; Data Dictionary; Coding Guide; Analysis Notes; standardized variable names; dropdowns; ET1/ET2 fields; embryo data; hormonal data; pregnancy outcomes; automatic ΔET calculation; automatic ESI calculation; capacity for approximately 5,000 records.

**NOT PROVIDED.** The user confirmed on 29 August 2026 that no workbook was available. `studies/esi-fet/data-dictionary.md` was built from §30 and §18–29 of this handoff instead.

## 57. Recommended immediate next steps

Before collecting hundreds of records, run a pilot of approximately 30–50 cases through the spreadsheet. The pilot should answer:

1. Is ET actually measured at both required time points?
2. How consistently is transfer-day ET recorded?
3. Is the progesterone start time, not just date, available?
4. Are D5/D6 and Gardner grades reliably available?
5. Is live-birth follow-up complete?
6. Are PGT-A data available?
7. Is serum P4 routinely measured?
8. Are endometrial patterns available at both scans?
9. How many women have multiple FETs?
10. How much missingness exists for each field?

Only after that pilot should the final protocol and statistical analysis plan be locked.

The single biggest feasibility issue is likely to be whether ET2 (transfer-day endometrial thickness) was routinely and consistently measured. If it was not, the project may need to become prospective rather than relying on retrospective records.

## Core concept in one sentence

This study will test whether the dynamic percentage change in endometrial thickness between progesterone initiation and single blastocyst transfer—the Endometrial Stability Index—provides independent and clinically useful information about live-birth probability beyond the conventional single measurement of endometrial thickness and embryo quality.
