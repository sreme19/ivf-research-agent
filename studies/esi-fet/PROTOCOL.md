# PROTOCOL — Endometrial Stability Index (ESI)

**Status: DRAFT. Not final. Not locked.**
Awaiting clinician review (29 August 2026) and the feasibility pilot.
Target lock date: **30 September 2026**. See `../../ROADMAP.md`.

Compiled from `inbox/2026-08-29-esi-research-handoff.md`.

---

## Working title

> ENDOMETRIAL STABILITY INDEX: DOES DYNAMIC CHANGE IN ENDOMETRIAL THICKNESS DURING
> PROGESTERONE EXPOSURE PREDICT IMPLANTATION AND LIVE BIRTH FOLLOWING SINGLE
> BLASTOCYST FROZEN EMBRYO TRANSFER

23 words — fits the ASPIRE 25-word limit with 2 words of headroom.

Manuscript alternatives (both also ≤25 words) in §2 of the handoff.

## Objective

To evaluate the association between dynamic changes in endometrial thickness during
progesterone exposure and live birth following single blastocyst frozen embryo
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

- Age approximately 21–45 years
- Frozen blastocyst transfer
- Autologous oocyte cycle
- Single blastocyst transfer (primary analysis)
- Endometrial measurement at/immediately before progesterone initiation
- Repeat endometrial measurement on/around transfer day
- Known progesterone exposure duration
- Known embryo grade
- Known pregnancy outcome
- Known live-birth outcome

### Exclusion

Donor-oocyte cycles; gestational carriers; major Müllerian anomalies; untreated
hydrosalpinx; untreated significant submucosal fibroid; significant untreated
endometrial polyp; severe intrauterine adhesions; cycles without standardised ET
measurements; missing embryo information; missing transfer outcome; double embryo
transfers (primary analysis).

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

**Primary: live birth per embryo transfer** (0/1).

Secondary: positive β-hCG; biochemical pregnancy; clinical pregnancy (predefined);
implantation; ongoing pregnancy (gestational-age threshold predefined);
miscarriage. Also gestational age at delivery and birth weight where available.

## Hypotheses — direction-neutral

- **H0:** ESI is not independently associated with live birth.
- **H1:** The magnitude and/or direction of ESI is independently associated with
  live birth after adjustment.

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
9. Is live-birth follow-up complete, or are some patients delivered elsewhere?
10. Who are the co-authors, and is any of them under 40 and Asia-Pacific resident
    (Young Investigator Award eligibility)?
