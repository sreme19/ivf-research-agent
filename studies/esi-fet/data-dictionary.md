# Data dictionary — ESI

**One row = one FET cycle.** Never one row per patient.

Built from §18–32 of `inbox/2026-08-29-esi-research-handoff.md`. The Excel workbook
described in §56 of that handoff was **not provided**, so this is the authoritative
variable specification.

## Universal coding rules

| Convention | Meaning |
|---|---|
| blank / `NA` | Unavailable — not recorded, not found |
| `0` | Confirmed absent |
| `1` | Confirmed present |

**Missing is never coded as zero.** Store raw values, never derived categories:
`ET1 = 8.7` not "adequate"; `4AB` not "good"; `P4 = 13.8` not "normal". Categories
are generated in analysis; raw data cannot be reconstructed once discarded.

---

## Identifiers

| Variable | Type | Coding / units | Notes |
|---|---|---|---|
| `STUDY_ID` | text | Coded | **The only patient identifier permitted.** Linkage file lives on Indira's systems, outside this repo. |
| `SITE_ID` | text | Coded centre identifier | Required for the multicentre analysis. Covariate or random effect. |

## Demographics

| Variable | Type | Coding / units |
|---|---|---|
| `AGE_FET` | numeric | Years at FET |
| `AGE_OPU` | numeric | Years at oocyte retrieval |
| `BMI` | numeric | kg/m² |

## Reproductive history

| Variable | Type | Coding / units |
|---|---|---|
| `GRAVIDITY` | integer | |
| `PARITY` | integer | |
| `PREV_LIVE_BIRTH` | binary | 0/1 |
| `PREV_MISCARRIAGE` | integer | Count |
| `INFERTILITY_YEARS` | numeric | Years |
| `INFERTILITY_TYPE` | categorical | 1 primary, 2 secondary |
| `PREV_IVF` | integer | Count of previous IVF cycles — **0 for all included cycles** (eligibility check only, not a covariate) |
| `PREV_TRANSFER` | integer | Count of previous transfers — **0 for all included cycles** |
| `PREV_IMPLANTATION_FAILURE` | binary | 0/1 — **0 for all included cycles** |

*First-cycle-only cohort (SPEC.md Amendment 3). These three fields are collected to
verify eligibility, then dropped before modelling — they are constant and cannot be
estimated.*

## Infertility diagnosis — separate binaries, multiple may coexist

`MALE_FACTOR` · `TUBAL_FACTOR` · `PCOS` · `ENDOMETRIOSIS` · `DOR` · `UNEXPLAINED` ·
`UTERINE_FACTOR` · `OTHER_DIAGNOSIS` — each binary 0/1.

**Do not force one diagnosis per woman.**

## Uterine / endometrial history — binaries 0/1

`ADENOMYOSIS` · `FIBROID` · `SUBMUCOSAL_FIBROID` · `POLYP` · `HYDROSALPINX` ·
`CHRONIC_ENDOMETRITIS` · `PREV_HYSTEROSCOPY` · `PREV_ADHESIOLYSIS` ·
`SEPTUM_SURGERY` · `PREV_ENDOMETRIAL_PATHOLOGY`

Recorded, not used for exclusion (except where the protocol specifies).

## Cycle protocol

| Variable | Type | Coding / units |
|---|---|---|
| `FET_PROTOCOL` | categorical | 1 natural, 2 modified natural, 3 HRT/programmed, 4 ovulation induction, 5 other |
| `ESTROGEN_PREP` | text | Preparation name |
| `ESTROGEN_ROUTE` | categorical | 1 oral, 2 transdermal, 3 vaginal, 4 combination |
| `ESTROGEN_DOSE` | numeric | mg/day |
| `ESTROGEN_START_DATE` | date | |
| `ESTROGEN_DAYS_PRE_P` | numeric | Days before progesterone |
| `E2_PRE_TRANSFER` | numeric | pg/mL |
| `E2_AT_P_START` | numeric | pg/mL |

## Progesterone — critical

| Variable | Type | Coding / units |
|---|---|---|
| `PROG_START_DATE` | date | |
| `PROG_START_TIME` | time | **Exact time where available** |
| `PROG_ROUTE` | categorical | 1 vaginal, 2 IM, 3 subcutaneous, 4 oral, 5 combination |
| `PROG_FORMULATION` | text | |
| `PROG_DOSE` | numeric | Total daily dose, mg |
| `PROG_FREQUENCY` | text | e.g. BD, TDS |
| `P_DAYS` | numeric | Exposure days before transfer — **derived** |
| `P_HOURS` | numeric | Exposure hours — **derived**, preferred |
| `P4_PRE_TRANSFER` | numeric | ng/mL |
| `P4_SAMPLE_DATE` | date | |
| `P4_SAMPLE_TIME` | time | |
| `P4_HOURS_SINCE_DOSE` | numeric | Serum level depends on route and timing |

## Endometrium — the exposure

| Variable | Type | Coding / units |
|---|---|---|
| `ET1_DATE` | date | Preferably ≤24 h before progesterone start |
| `ET1_TIME` | time | |
| `ET1_MM` | numeric | **mm to 0.1** |
| `PATTERN_ET1` | categorical | 1 triple-line, 2 intermediate, 3 homogeneous/echogenic, 4 other/uncertain |
| `ET1_OPERATOR` | text | Sonographer ID |
| `ET1_MACHINE` | text | Machine ID/model |
| `ET2_DATE` | date | Transfer day, before transfer |
| `ET2_TIME` | time | |
| `ET2_MM` | numeric | **mm to 0.1** |
| `PATTERN_ET2` | categorical | As above |
| `ET2_OPERATOR` | text | |
| `ET2_MACHINE` | text | |

### Optional advanced ultrasound

`ET1_VOLUME` / `ET2_VOLUME` (mL, 3D) · `ET1_VI` `ET1_FI` `ET1_VFI` /
`ET2_VI` `ET2_FI` `ET2_VFI` (power Doppler) ·
`ET1_PERISTALSIS` / `ET2_PERISTALSIS` (**waves/minute**, never "normal/abnormal")

Useful but not gating. Do not delay the study for these.

### Derived — computed in code, never typed

| Variable | Formula |
|---|---|
| `DELTA_ET_MM` | `ET2_MM − ET1_MM` |
| `ESI_PERCENT` | `((ET2_MM − ET1_MM) / ET1_MM) × 100` — **PRIMARY EXPOSURE** |
| `ESI_DAILY_PERCENT` | `ESI_PERCENT / P_DAYS` — exploratory only |

See handoff §33: never hand-calculate these.

## Embryo — mandatory

| Variable | Type | Coding / units |
|---|---|---|
| `EMBRYO_DAY` | categorical | 5, 6, 7 |
| `EMBRYO_EXPANSION` | integer | Gardner 1–6 |
| `ICM_GRADE` | categorical | A / B / C |
| `TE_GRADE` | categorical | A / B / C |
| `EMBRYO_GRADE` | text | **Raw overall grade, e.g. 4AA, 4AB, 3BB, 5AA** |
| `PGT_PERFORMED` | binary | 0/1 |
| `PLOIDY` | categorical | 1 euploid, 2 aneuploid, 3 mosaic, 4 other/indeterminate |

**Retain raw morphology. Do not collapse to good/poor at entry.**

## Transfer

| Variable | Type | Coding / units |
|---|---|---|
| `SINGLE_EMBRYO_TRANSFER` | binary | 0/1 |
| `TRANSFER_DATE` | date | |
| `TRANSFER_TIME` | time | |
| `TRANSFER_OPERATOR` | text | |
| `CATHETER_TYPE` | text | |
| `US_GUIDED_TRANSFER` | binary | 0/1 |
| `DIFFICULT_TRANSFER` | binary | 0/1 |
| `TRANSFER_ATTEMPTS` | integer | |
| `BLOOD_CATHETER` | binary | 0/1 |
| `MUCUS_CATHETER` | binary | 0/1 |
| `TRANSFER_DEPTH` | numeric | mm, if routine |

## Outcomes

### Primary — biochemical implantation

| Variable | Type | Coding / units |
|---|---|---|
| **`BETA_HCG_POSITIVE`** | binary | **0/1 — PRIMARY ENDPOINT.** Derived in code by applying the harmonised threshold to `BETA_HCG_VALUE` |
| `BETA_HCG_VALUE` | numeric | **mIU/mL — raw value. Collect this, not just the flag.** |
| `BETA_HCG_UNITS` | text | Confirm units per site |
| `BETA_HCG_THRESHOLD_SITE` | numeric | The positivity threshold that site uses |
| `BETA_HCG_ASSAY` | text | Assay platform |
| `BETA_HCG_DAYS_POST_TRANSFER` | numeric | Days from transfer to sample |
| `BETA_HCG_DATE` | date | |

**Why the raw value matters.** This is a multicentre study. If sites use different
positivity thresholds, a binary flag means the outcome is defined differently at
different sites — measurement error in the outcome, which is worse than measurement
error in a covariate. Collect the number; derive the flag in code with one
harmonised threshold.

### Key secondary — gestational sac (6-week scan)

| Variable | Type | Coding / units |
|---|---|---|
| `GESTATIONAL_SAC` | binary | 0/1 — ≥1 intrauterine sac |
| `SAC_NUMBER` | integer | Count |
| `FETAL_CARDIAC_ACTIVITY` | binary | 0/1 — often visible at 6 weeks; capture separately |
| `FIRST_SCAN_DATE` | date | |
| `GEST_AGE_AT_SCAN` | numeric | Weeks — expected ~6 |

**Coding rule that matters:** a cycle that was β-hCG negative and therefore never
scanned is `GESTATIONAL_SAC = 0`, **not** `NA`. It is a confirmed failure, not a
missing observation. Coding it `NA` drops it from the analysis and inflates the rate.

Because all transfers are single blastocyst transfers, `GESTATIONAL_SAC` is
equivalent to both the ICMART implantation rate and the clinical pregnancy rate.

### Other secondary

| Variable | Type | Coding / units |
|---|---|---|
| `BIOCHEMICAL_PREGNANCY` | binary | 0/1 — β-hCG positive, no subsequent sac |
| `ONGOING_PREGNANCY` | binary | 0/1 — predefined GA threshold |
| `MISCARRIAGE` | binary | 0/1 |

### Collected but NOT analysed in this study

| Variable | Type | Coding / units |
|---|---|---|
| `LIVE_BIRTH` | binary | 0/1 |
| `GEST_AGE_DELIVERY` | numeric | Weeks |
| `BIRTH_WEIGHT` | numeric | Grams |

Retained because a column costs nothing to carry and cannot be reconstructed later.
The downstream Fertility & Reproduction manuscript will very likely be asked for a
live-birth endpoint. Collect where available; leave `NA` where not. **Do not analyse
these in the ESI study.** See `SPEC.md` Amendment 1.

---

## Reproducibility substudy

Separate file. ~100 randomly selected scans, independently re-measured.

| Variable | Type |
|---|---|
| `STUDY_ID` | text |
| `SCAN_POINT` | categorical — ET1 / ET2 |
| `MEASURE_1_MM` | numeric |
| `MEASURE_2_MM` | numeric |
| `PATTERN_1` | categorical |
| `PATTERN_2` | categorical |

Yields **ICC** for thickness and **Cohen's kappa** for pattern.

---

## Open questions for the clinician

1. Which optional advanced ultrasound variables are actually recorded routinely?
2. Are ultrasound operator and machine IDs retrievable retrospectively?
3. Is progesterone start **time** in the record, or only the date?
4. What units are used locally for P4 (ng/mL vs nmol/L) and E2 (pg/mL vs pmol/L)?
5. Is `TRANSFER_DEPTH` routinely recorded?
6. What is the local clinical-pregnancy definition?
7. **At what gestational age is the first scan performed, and what is recorded —
   gestational sac, fetal pole, or cardiac activity?** This defines the primary
   endpoint.
8. Do ultrasound protocols differ across the participating Indira centres, and is
   `ET1_MACHINE` / `ET1_OPERATOR` retrievable? *(Multicentre measurement variation
   propagates directly into ESI — see `SITE-AND-GOVERNANCE.md`.)*
9. Add `SITE_ID` — required as a covariate or random effect for a multicentre
   analysis.
10. **What β-hCG positivity threshold does each participating centre use, and is
    the raw value retrievable?** *(Primary endpoint depends on this.)*
11. Is the days-post-transfer interval for β-hCG consistent across sites?
12. Does the 6-week scan record routinely document cardiac activity as well as sac?
