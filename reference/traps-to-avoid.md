# Methodological traps to avoid

Compiled from §46–48 of `inbox/2026-08-29-esi-research-handoff.md`. The
`protocol-guard` and `aspire-compliance` skills check drafts against this list.

## Framing

1. **Do not assume compaction is beneficial.** The study is direction-neutral.
   Prior literature conflicts; committing to a direction invites confirmation bias
   in a retrospective dataset full of analytic choices.
2. **Do not claim dynamic endometrial change has never been studied.** It has,
   repeatedly, with conflicting results. Novelty comes from standardised
   measurement, continuous modelling, embryo adjustment, live-birth endpoint and
   validation — not from priority.
3. **Do not call ultrasound thickness "endometrial receptivity."** It is a
   surrogate phenotype, not a molecular measurement.
4. **Do not force a positive result.** A rigorous null challenging the clinical
   utility of transfer-day endometrial measurement is publishable and useful.

## Analysis

5. **Do not choose an ESI cutoff after seeing which gives the best p-value and
   present it as prespecified.** This is the single most damaging thing this
   project could do. Cutoffs come from the locked SAP or from spline modelling,
   with the post-hoc status stated plainly.
6. **Do not overstate what an implantation endpoint shows.** *(Revised 29 August
   2026 — the primary endpoint was changed from live birth to implantation. See
   `SPEC.md` Amendment 1.)* Implantation is an early surrogate. The manuscript must
   state that the association with live birth was not assessed, and must not imply
   it was. A finding about implantation is not a finding about a baby.
7. **Do not let the discussion drift toward live birth.** Phrases like "improved
   outcomes", "better success rates" or "clinical benefit" smuggle in an endpoint
   that was not measured. Say "implantation".
8. **Do not select confounders on univariate p-values alone.** Selection is
   clinically and causally justified. Check collinearity.
9. **Do not infer effect modification from comparing subgroup p-values.** Test the
   interaction term.
10. **Do not treat repeated cycles from one woman as independent.** Either
    first-eligible-transfer-only, or a clustered/mixed/GEE approach — prespecified.
11. **Do not code missing as zero.**

## Population

12. **Do not mix cleavage-stage and blastocyst transfers** indiscriminately.
13. **Do not mix single and double embryo transfers** in the primary analysis.
14. **Do not mix donor and autologous cycles** without justification.

## Measurement and adjustment

15. **Do not ignore embryo morphology.** Retain raw Gardner components.
16. **Do not ignore PGT status.**
17. **Do not ignore FET protocol.** It is a real confounder; do not pool blindly.
18. **Do not ignore progesterone exposure duration.**
19. **Do not let ET1/ET2 measurement timing vary substantially without recording
    it.** Unrecorded timing variation is unfixable at analysis.

## Repo-specific

20. **Do not put a number in a draft that is not traceable to `outputs/`.**
21. **Do not commit patient data.** See `CLAUDE.md` rule 1.
