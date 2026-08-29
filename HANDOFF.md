# HANDOFF — pick this up cold

Written 29 August 2026, end of session 1. Read this first if you have no memory of
this project. Then read `studies/esi-fet/PAPER-STATE.md` for live status.

---

## In one paragraph

An IVF research project heading for the **ASPIRE 2027** congress (Yokohama, 6–9 May
2027; abstract deadline **6 November 2026**) and then the journal **Fertility &
Reproduction**. The study asks whether the percentage change in endometrial thickness
between progesterone initiation and embryo transfer — an "Endometrial Stability Index"
— predicts implantation after single blastocyst frozen embryo transfer. Data comes from
**Indira IVF**, a multicentre IVF chain in India, where the investigator works. The data
exists and needs retrieval; ethics approval has not yet been sought and is the critical
path. A literature review completed this session found the phenomenon is already
extensively published as **"endometrial compaction"** and that the original novelty claim
is not defensible — this is the single most important thing to know.

---

## The finding that reframes the project

**Read `studies/esi-fet/literature/REPORT.md` before writing any framing.**

- ~25 primary cohort studies, **four independent meta-analyses** (2023–24), up to
  27,857 patients pooled.
- **Pan 2025** (*Hum Reprod Open*, n=16,453) uses the **identical ESI formula**.
- **Zilberberg 2020** (*Fertil Steril*, n=234) is essentially this study's cohort,
  done six years ago, and positive.
- All four meta-analyses: compaction helps clinical/ongoing pregnancy in crude
  analyses; **the signal dies before live birth** (pooled OR 0.95–0.97). Euploid
  cohorts flat (RR 0.99, 0.86–1.13).
- **The positive signal tracks a measurement artefact.** Positive studies measured
  transvaginally at baseline, **transabdominally** at transfer. Chen 2023: mixed-route
  studies RR 1.69 (1.26–2.26); transvaginal-throughout studies, nothing.

**Consequences already applied:**
- Transvaginal at both timepoints is now an **eligibility criterion**, not a methods
  note. Any transabdominal measurement excludes the cycle.
- A **null result should be expected** and is publishable.
- The hypothesis must be **two-sided** — Bu 2019, Jin Z 2021, Hou 2025 and Pan 2025 all
  found *expansion* favourable.

**The one gap that survives:** implantation as a *prespecified primary endpoint* is
genuinely rare in this literature. The investigator chose β-hCG positivity as the
primary endpoint before the review came back — an accidental landing on the real gap.

**Citation corrections:** Haas 2019 is *Fertility and Sterility*, not RBMO (common
mis-citation). The 2020 euploid follow-up is first-authored by **Zilberberg**, not Haas.

---

## Decisions made (all recorded in `SPEC.md` with rationale)

| # | Decision | Where |
|---|---|---|
| 1 | Repo separates `venues/` from `studies/` so both are reusable | SPEC §1 |
| 2 | Zero API key; skills do the thinking in-session | SPEC §2 |
| 3 | Analysis in R (`rms`, `pROC`, `dcurves`, `mice`) — provisional, no code yet | SPEC §3 |
| 4 | Local git only, no remote | SPEC §4 |
| 5 | **Primary endpoint: β-hCG positivity** ("biochemical implantation") | Amendment 1, 4 |
| 6 | Gestational sac (6-week scan) = prespecified key secondary | Amendment 4 |
| 7 | Live birth collected but NOT analysed | Amendment 1 |
| 8 | **First IVF cycle only** — no previous IVF, transfer or implantation failure | Amendment 3 |
| 9 | ESI modelled continuously; no a priori cutoffs | SPEC §6 |
| 10 | Direction-neutral, two-sided hypothesis | SPEC §7 |
| 11 | Young Investigator Award not pursued | Amendment 2 |
| 12 | Transvaginal at both timepoints = eligibility criterion | PROTOCOL |

---

## ASPIRE 2027 rules (inherited from 2026/2025/2024 — NOT officially confirmed for 2027)

- Title **25 words, UPPER CASE**
- Abstract **300 words including acknowledgements**
- Mandatory structure: **Background and Aims / Methods / Results / Conclusions**
- 20 topic categories — this study is **"ART, Clinical"**
- Max 2 abstracts per author; 3 tables; 2 images
- **International** prior presentation may preclude acceptance; national/regional is fine
- Notification expected ~January 2027

Full detail and the still-unknown items: `venues/aspire-2027/guidelines/`.

---

## Open questions — investigator's to answer

| # | Question | Why it matters |
|---|---|---|
| **Q7** | **How is the study positioned given four meta-analyses sit on the null?** Replication/refutation vs. novel index | The entire Introduction, Discussion and abstract |
| Q8 | Keep the name "Endometrial Stability Index"? It is compaction under a new name | Reviewer credibility |
| Q9 | Euploid-only, all blastocysts, or both (full cohort primary + euploid subgroup)? | Cohort, power, which gap is occupied |
| Q3 | Is the prediction-model comparison in scope, or association only? | Whether TRIPOD applies |
| Q4 | ESI increment for the reported OR — per 5% or per 10%? | SAP §2 |
| Q5 | Any prior international presentation of this work? | ASPIRE eligibility |
| Q6 | Does "first IVF cycle" exclude a woman whose fresh transfer in that cycle failed? | Eligibility; possibly a large share of the cohort |

## Blocking data needs

| # | Need | Status |
|---|---|---|
| D3 | **Ethics / Indira IEC approval** | Not yet sought. **Critical path.** Nothing extracts before it. |
| D10 | Q7 positioning decision | Open |
| D11 | **Is ultrasound transvaginal at BOTH timepoints across all sites?** | Unverified. Study is uninterpretable without this. |
| — | β-hCG positivity threshold per site; is the raw value retrievable? | Unknown. Primary endpoint depends on it. |
| — | Participating Indira centres and study period | Unknown |
| D5 | Pilot: 30–50 consecutive cycles | Not started |

## Before submission

- [ ] Re-check **De la Torre Perez 2023** (Front Endocrinol, PMID 38027116) — registered
      prospective euploid compaction study, n=206. May have reported; would occupy part
      of the intended space.
- [ ] Re-check **ClinicalTrials.gov NCT04330066** — euploid FET compaction. Status unverified.
- [ ] Obtain official ASPIRE 2027 abstract guidelines (`abstract@aspire2027.com`)
- [ ] Obtain F&R Instructions to Authors

---

## How to work here

Say **`/paper-loop`** — the standing workflow. It reads `studies/esi-fet/PAPER-STATE.md`,
writes whatever is writable, runs whatever analysis the available data supports, shows the
draft, and ends with a specific list of what is needed next. It updates the board before
finishing.

Other skills: `aspire-compliance` (word counts and venue rules), `protocol-guard` (the 21
methodological traps), `literature-scan`, `abstract-builder`, `manuscript-drafter`.

**Two rules that are load-bearing:**
1. No patient data in this repo, ever. `studies/*/data/` is gitignored.
2. No number in any draft that is not traceable to `studies/esi-fet/outputs/`.

## What exists now

- Methods drafted (~2,000 words): design, participants, ESI exposure, ultrasound,
  covariates, statistical analysis, plus six known limitations
- Introduction, Results, Discussion blocked — Introduction is unblocked pending Q7
- No data, no analysis, no outputs
