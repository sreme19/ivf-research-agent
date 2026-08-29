# PROTOCOL — Endometrial Stability Index (ESI)

**Status: DRAFT. Not final. Not locked.**
Awaiting clinician review (29 August 2026) and the feasibility pilot.
Target lock date: **30 September 2026**. See `../../ROADMAP.md`.

Compiled from `inbox/2026-08-29-esi-research-handoff.md`.

---

## Working title

> ENDOMETRIAL STABILITY INDEX: DOES DYNAMIC CHANGE IN ENDOMETRIAL THICKNESS DURING
> PROGESTERONE EXPOSURE PREDICT IMPLANTATION FOLLOWING SINGLE BLASTOCYST FROZEN
> EMBRYO TRANSFER

20 words — fits the ASPIRE 25-word limit with 5 words of headroom.

Revised 29 August 2026: "AND LIVE BIRTH" removed. See Endpoints below.

## Objective

To evaluate the association between dynamic changes in endometrial thickness during
progesterone exposure and implantation following single blastocyst frozen embryo
transfer, and to determine whether an Endometrial Stability Index provides
incremental prognostic information beyond baseline endometrial thickness, patient
characteristics and embryo morphology.

## Design

Retrospective cohort study. Multicentre if standardised data permit.

Target: ≥1,500–2,000 eligible single-blastocyst FET cycles. **This is a practical
target, not a power calculation.** A statistician must supply the formal
sample-size calculation based on expected live-birth rate, effect size, number of
predictors and anticipated missingness. STROBE item 10 depends on this.

Ideal two-phase structure:
- Phase 1 — retrospective development cohort
- Phase 2 — prospective or temporal validation cohort

## Population

Women undergoing **single blastocyst frozen embryo transfer using autologous
oocytes**.

Secondary cohort if numbers permit: **single euploid blastocyst transfers**.
Scientifically important, because aneuploidy is the dominant confounder when
studying endometrial effects.

### Inclusion

**Revised 29 August 2026: first IVF cycle only.** Women with previous IVF cycles,
previous embryo transfers, or previous implantation failure are excluded. See
`SPEC.md` Amendment 3.

- Age approximately 21–45 years
- **First IVF cycle** — no previous IVF, no previous embryo transfer
- Frozen blastocyst transfer
- Autologous oocyte cycle
- Single blastocyst transfer (primary analysis)
- Endometrial measurement at/immediately before progesterone initiation
- Repeat endometrial measurement on/around transfer day
- Known progesterone exposure duration
- Known embryo grade
- Known pregnancy outcome
- **Known implantation outcome** (ultrasound performed and documented)

### Exclusion

Donor-oocyte cycles; gestational carriers; major Müllerian anomalies; untreated
hydrosalpinx; untreated significant submucosal fibroid; significant untreated
endometrial polyp; severe intrauterine adhesions; cycles without standardised ET
measurements; missing embryo information; missing transfer outcome; double embryo
transfers (primary analysis); **any previous IVF cycle or embryo transfer**.

Adenomyosis, endometriosis and fibroids are **recorded, not excluded** — they can
be adjusted for or studied as subgroups.

## Exposure

Two standardised transvaginal measurements.

**ET1** — immediately before progesterone initiation, preferably within 24 hours.
Millimetres to 0.1 mm.

**ET2** — on transfer day, before transfer, same methodology, as close to transfer
as feasible.

```
ΔET   = ET2 − ET1                          (mm)
ESI % = [(ET2 − ET1) / ET1] × 100          PRIMARY EXPOSURE
```

Worked example: ET1 9.4, ET2 8.6 → ΔET −0.8 mm, ESI −8.5%.

ESI < 0 compaction · ESI ≈ 0 stability · ESI > 0 expansion.

**These labels are descriptive only. ESI is analysed as a continuous variable.**
No categories at the primary-analysis stage. Thresholds, if any, come from the
data. See `../../reference/traps-to-avoid.md` item 5.

Exploratory only: `Daily ESI = ESI / progesterone exposure days`. Never the
primary exposure.

## Ultrasound standardisation

Transvaginal; standardised sagittal midline uterine plane; maximum double-layer
thickness; myometrium excluded; measured to 0.1 mm; same machine/model where
possible; standardised bladder conditions; trained operators; defined protocol.

Record for both scans: date, exact time where possible, operator ID, machine ID.

**Reproducibility substudy:** ~100 randomly selected scans re-measured
independently. Report **ICC** for thickness and **Cohen's kappa** for pattern.
This is what separates this study from prior compaction work — do not drop it.

Endometrial pattern at both time points: 1 triple-line · 2 intermediate ·
3 homogeneous/echogenic · 4 other/uncertain. Never "good"/"bad"/"satisfactory".

Optional if routinely available: 3D endometrial volume; power Doppler VI/FI/VFI;
subendometrial blood flow; peristalsis in waves/minute. Useful, but not gating.

## Endpoints

**Revised 29 August 2026.** Live birth was the primary endpoint in the original
handoff (§28). It has been replaced by implantation at the investigator's
direction. Rationale and trade-off recorded in `SPEC.md`, Amendment 1.

### Primary: biochemical implantation — positive serum β-hCG (0/1)

**DECIDED 29 August 2026.** See `SPEC.md` Amendment 4.

Positive serum β-hCG measured at the centre's standard post-transfer interval,
indicating trophoblastic secretion and therefore biochemical evidence that
implantation occurred.

**This must be named precisely in the manuscript.** ICMART/WHO defines *implantation
rate* as gestational sacs divided by embryos transferred. This study uses a
different, earlier definition. The Methods must say so explicitly — "biochemical
implantation, defined as positive serum β-hCG" — and must not present it as the
ICMART implantation rate. Naming it plainly converts a reviewer objection into a
stated design choice.

**Rationale.** β-hCG positivity is the earliest detectable evidence that an embryo
implanted and trophoblast began secreting. It is biologically the most proximate
marker of the event ESI is hypothesised to influence; later endpoints add causes of
failure that have nothing to do with the endometrium at transfer. It also carries
the highest event rate, and — decisively for a retrospective study — near-complete
ascertainment: every patient has a β-hCG result, whereas only β-hCG-positive patients
proceed to ultrasound.

**Mitigation 1 — record the value, not just the flag.** The raw β-hCG concentration,
the assay's positivity threshold, the assay platform, and the number of days
post-transfer at which the sample was taken are recorded for every cycle. A binary
alone is not sufficient in a multicentre study.

**Mitigation 2 — gestational sac is a prespecified key secondary.** This provides
comparability with the prior compaction literature, which is almost entirely
sac-based, and serves as a sensitivity analysis. Concordant results across both
endpoints strengthen the finding; divergence is itself informative.

### Key secondary — gestational sac

Presence of at least one intrauterine gestational sac on transvaginal ultrasound at
the centre's standard first scan, performed at **6 weeks' gestation** (confirmed
29 August 2026). Because all transfers are single blastocyst transfers, this is
equivalent to both the ICMART implantation rate and the clinical pregnancy rate — a
point the manuscript should state rather than leave for a reviewer to notice.

**Note on 6 weeks.** At this gestational age fetal cardiac activity is frequently
already visible. This is an advantage — the same scan can yield both a sac-level and
a cardiac-activity-level endpoint at no extra cost — but it means the scan record
must be checked for what was actually documented. If the record routinely notes
cardiac activity, capture it as a separate field rather than collapsing everything
into "sac present".

### Other secondary

Biochemical pregnancy (β-hCG positive without subsequent gestational sac); ongoing
pregnancy (gestational-age threshold predefined); miscarriage.

### Multicentre threat to this endpoint

If participating Indira centres use different assay platforms or different positivity
thresholds, a cycle classified positive at one site could be classified negative at
another. This is measurement error **in the outcome**, which is more damaging than
measurement error in a covariate. Confirm the thresholds in use across sites; if they
differ, apply a single harmonised threshold to the recorded raw values.

### Collected but NOT analysed in this study

`LIVE_BIRTH`, `GEST_AGE_DELIVERY`, `BIRTH_WEIGHT` are collected where available and
retained in the dataset, but form no part of this study's analysis. They are kept
because a column costs nothing to carry and cannot be reconstructed later — and
because the downstream Fertility & Reproduction manuscript will very likely be
asked for a live-birth endpoint.

### Known trade-off

The original handoff (§47) lists using a softer endpoint instead of live birth as a
methodological trap, and implantation is softer than clinical pregnancy. This is a
deliberate, recorded decision, not an oversight. The manuscript must state plainly
that implantation is an early surrogate and that the association with live birth
was not assessed. Do not let a discussion section drift into implying it was.

## Hypotheses — direction-neutral

- **H0:** ESI is not independently associated with implantation.
- **H1:** The magnitude and/or direction of ESI is independently associated with
  implantation after adjustment.

The analysis determines whether compaction, stability or expansion is favourable,
whether an optimal range exists, whether extremes in either direction are
unfavourable, or whether ESI has no clinically useful association. **No direction
is assumed.**

## Ethics and governance

Required before any extraction:

- [ ] Institutional ethics/IRB approval or exemption
- [ ] Retrospective consent-waiver determination
- [ ] De-identification procedure agreed with the clinic
- [ ] Linkage file held on clinic storage, **outside this repo**

Analysis uses `STUDY_ID` only.

**Start this now.** Institutional turnaround of 4–6 weeks is common and is the
most underestimated risk to the timeline.

## Reporting

STROBE for the observational component. TRIPOD additionally if the prediction-model
comparison is presented. See `../../reference/`.

---

## Open items for clinician review

1. Is ET2 routinely and consistently recorded on transfer day? *(This determines
   whether the study is possible retrospectively at all.)*
2. Confirm the age range — 21–45, or the centre's actual practice?
3. Single-centre or multicentre? Which centres, and are their ultrasound protocols
   comparable?
4. What study period should the extraction cover?
5. Is D7 blastocyst transfer performed? Include, or exclude?
6. Is PGT-A common enough to power a euploid subgroup?
7. Is serum P4 measured routinely before transfer?
8. Which FET protocols are in use, and in what proportions?
9. **What β-hCG positivity threshold is used, and is it the same at every
   participating centre?** Is the raw value retrievable, or only a positive/negative
   flag? *(Primary endpoint depends on this.)*
10. How many days after transfer is β-hCG measured, and is that interval consistent?
11. ~~At what gestational age is the first scan performed?~~ **Answered: 6 weeks.**
12. Does the 6-week scan record routinely document fetal cardiac activity as well as
    the sac? *(If yes, a third endpoint level is available at no extra collection
    cost.)*
