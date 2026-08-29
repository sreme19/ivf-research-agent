# Site and governance — ESI

Recorded 29 August 2026 from the investigator.

## Data source

**Indira IVF** — IVF chain, India. The investigator works there.

### What this means for the study

**Advantages, and they are substantial:**

- Large chain volume makes the 1,500–2,000 cycle target realistic, where a single
  clinic would struggle.
- Multicentre by default, which strengthens external validity and is a genuine
  advantage over most published compaction studies (typically single-centre).
- Investigator has internal access — no external data-sharing agreement needed.

**Risks that come with the same fact:**

- **Ultrasound standardisation across centres is now the central methodological
  question.** Different machines, different operators, different local habits. If
  ET1 and ET2 are measured differently across sites, ESI — a *difference* between
  two measurements — absorbs that variation directly. A 0.3 mm inter-operator
  difference is noise on an 8 mm thickness but is meaningful on a −4% ESI.
  This is exactly why the ICC/kappa reproducibility substudy in `PROTOCOL.md`
  is not optional here. It is the study's credibility.
- Site should be included as a covariate or random effect. Add to `SAP.md` §4
  before lock.
- Protocol heterogeneity across sites (FET protocol, progesterone route) must be
  recorded, not assumed uniform.

## Data status

**NOT YET COLLECTED.** As of 29 August 2026, collection has not begun.

This is a more significant constraint than "retrospective extraction pending". The
`ROADMAP.md` timeline assumed data existing in an EMR awaiting extraction. Confirm
which of these is true:

- [ ] Data exists in Indira's systems and needs extraction → timeline holds
- [ ] Data requires manual chart abstraction per cycle → estimate hours/record in
      the pilot and multiply; this is where projects die
- [ ] Data requires prospective collection → **ASPIRE 2027 is not reachable**

## Ethics / IRB

**NOT YET OBTAINED.** To be sought from Indira IVF.

**This is now the critical path item.** Nothing can be extracted before approval.

### What to confirm with Indira's ethics office

- [ ] Does Indira IVF have a registered **Institutional Ethics Committee (IEC)**,
      and what is its meeting schedule? *(Meeting frequency, not review time, is
      usually what determines the delay.)*
- [ ] Does retrospective chart review qualify for **expedited review** or a
      **consent waiver**?
- [ ] Multicentre: does one IEC approval cover all participating sites, or does
      each site need its own?
- [ ] What is the realistic turnaround from submission to approval letter?
- [ ] What de-identification standard does Indira require?

### Indian regulatory context — VERIFY LOCALLY, do not rely on this summary

The following are the frameworks that generally apply to biomedical research and
ART practice in India. Confirm the specifics with Indira's ethics office and, if
needed, legal counsel — this note is orientation, not advice.

- **ICMR National Ethical Guidelines for Biomedical and Health Research Involving
  Human Participants** — the governing ethical framework for IEC review in India.
- **ART (Regulation) Act, 2021** — regulates ART clinics and banks in India and
  establishes a national registry. Relevant to how ART cycle data may be used.
- **Digital Personal Data Protection Act, 2023** — governs personal data handling.
  Health data is sensitive; de-identification standards and any cross-border
  transfer need checking.

None of the above has been verified for this specific study. Treat every line as a
question for the ethics office, not a settled answer.

## Repo consequence

`CLAUDE.md` rule 1 stands unchanged and is now load-bearing rather than theoretical:
no patient data in this repo. The linkage file lives on Indira's systems. Only
`STUDY_ID` crosses over.

## Open

- [ ] Which Indira centres are participating?
- [ ] What study period will the extraction cover?
- [ ] Are ultrasound protocols documented and comparable across those centres?
- [ ] Who is the local PI / responsible investigator for the ethics submission?
