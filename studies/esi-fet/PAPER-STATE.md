# PAPER STATE — ESI

**The board.** Read this first in every `paper-loop` iteration. Update it before
finishing. Sessions end; this file persists.

**Iteration: 4** · Last updated: 29 August 2026

> ⚠️ **READ `literature/REPORT.md` BEFORE WRITING ANY FRAMING.** The phenomenon is
> published as "endometrial compaction": ~25 studies, 4 meta-analyses, up to 27,857
> patients. Pan 2025 (n=16,453) used the identical ESI formula. The novelty claim as
> originally framed is NOT defensible. Positioning decision Q7 is now the most
> important open item in this project.

---

## The paper

**Title (20 words, fits ASPIRE's 25-word limit):**

> ENDOMETRIAL STABILITY INDEX: DOES DYNAMIC CHANGE IN ENDOMETRIAL THICKNESS DURING
> PROGESTERONE EXPOSURE PREDICT IMPLANTATION FOLLOWING SINGLE BLASTOCYST FROZEN
> EMBRYO TRANSFER

**Primary endpoint:** implantation (SPEC.md Amendment 1)
**Data source:** Indira IVF, India — multicentre
**Targets:** ASPIRE 2027 abstract (deadline 6 November 2026) → Fertility & Reproduction

---

## Section board

| Section | Status | Blocked on |
|---|---|---|
| Title | **DRAFT** | Implantation definition may alter wording |
| Abstract — ASPIRE | BLOCKED | Results |
| Abstract — journal | BLOCKED | Results |
| Introduction | **DRAFTABLE NOW** | Positioning decision Q7 first |
| Methods — Study design | **DRAFTABLE NOW** | — |
| Methods — Setting | **NEEDS-DATA** | Which Indira centres; study period |
| Methods — Data sources | **DRAFTABLE NOW** | — |
| Methods — Participants | **DRAFTABLE NOW** | — |
| Methods — Variables | **DRAFTABLE NOW** | — |
| Methods — Exposure (ESI) | **DRAFTABLE NOW** | — |
| Methods — Ultrasound | **DRAFTABLE NOW** | Site protocol detail improves it |
| Methods — Outcomes | **NEEDS-DECISION** | Implantation definition |
| Methods — Statistical | **DRAFTABLE NOW** | SAP [TBD] items |
| Methods — Ethics | **NEEDS-DATA** | IEC approval reference |
| Results — all | BLOCKED | No data collected |
| Discussion | BLOCKED | Results + literature |
| Limitations | **DRAFTABLE NOW** | Several are already known |
| References | **DRAFTABLE NOW** | Evidence table populated |

**Roughly half the paper is writable before a single data point arrives.** Methods
is the bulk of it, and it is the section reviewers scrutinise hardest.

---

## Data ledger

### Received

| Date | What | Unblocked |
|---|---|---|
| 29 Aug 2026 | ESI research handoff (design, variables, analysis plan) | Protocol, SAP, data dictionary |
| 29 Aug 2026 | Data source = Indira IVF; ethics not yet sought | Governance file, roadmap revision |
| 29 Aug 2026 | **Data confirmed to exist** in clinic systems — retrospective retrieval | D2 resolved; timeline holds |
| 29 Aug 2026 | Endpoint decision: implantation only | Endpoint rewrite across repo |
| 29 Aug 2026 | Cohort decision: first IVF cycle only | SAP §5 resolved; adjustment set reduced; new limitation |

### Outstanding — blocking

| # | Need | Unblocks | Priority |
|---|---|---|---|
| D1 | **Implantation definition** — gestational sac only, or sac + fetal pole? At what gestational age is the first scan? | Methods-Outcomes, SAP lock, entire analysis | **Critical** |
| D3 | **Ethics/IEC submission status and expected approval date** | All data work | **Critical** |
| D10 | **Decision on Q7 positioning** | Introduction, Discussion, abstract — everything | **Critical** |
| D11 | Is ultrasound transvaginal at BOTH timepoints across all sites? | Whether the study is credible at all — see REPORT §"Where the evidence conflicts" | **Critical** |
| D4 | Participating Indira centres + study period | Methods-Setting, `SITE_ID` design | High |
| D5 | Pilot data, 30–50 consecutive cycles | Feasibility answers, missingness report | High |

### Outstanding — improves the paper, not blocking

| # | Need | Unblocks |
|---|---|---|
| D6 | Ultrasound protocol documentation per centre | Methods-Ultrasound; strengthens the exposure's credibility |
| D7 | Official ASPIRE 2027 abstract guidelines | Confirms the 300-word / 25-word limits |
| D8 | F&R Instructions to Authors | Journal manuscript formatting |
| D9 | Co-author list, affiliations, contributions | Title page |

---

## Analysis queue

Nothing runnable — no data. Mapped to `SAP.md` sections.

| # | Analysis | SAP § | Needs | Status |
|---|---|---|---|---|
| A1 | Data quality check — row counts, missingness, implausible values, β-hCG-negative coding | — | Any extract | Waiting |
| A2 | Derive ΔET, ESI %, daily ESI **in code** | — | `ET1_MM`, `ET2_MM`, `P_DAYS` | Waiting |
| A3 | Table 1 — baseline by implantation | §1 | Full extract | Waiting |
| A4 | Figure 2 — ESI distribution | §1 | A2 | Waiting |
| A5 | Primary model — ESI continuous vs implantation | §2 | Full extract, SAP locked | Waiting |
| A6 | Figure 3 — restricted cubic spline | §3 | A5 | Waiting |
| A7 | Model A/B/C/D comparison | §6 | A5 | Waiting |
| A8 | Prespecified subgroups + interaction | §7,§8 | A5 | Waiting |
| A9 | ICC / Cohen's kappa reproducibility | — | ~100 re-measured scans | Waiting |
| A10 | Bootstrap internal validation | §10 | A7 | Waiting |

---

## Open decisions — investigator's to make

| # | Decision | Consequence | Status |
|---|---|---|---|
| Q1 | Implantation: sac, or sac + fetal pole? | Defines the primary endpoint | **Open — options presented, awaiting choice** |
| Q2 | Repeated cycles: first-only or clustered? | SAP §5 | **RESOLVED 29 Aug 2026 — first IVF cycle only** |
| Q6 | Does "first IVF cycle" exclude a woman whose fresh transfer in that same cycle failed before this FET? | Eligibility; potentially a large share of the cohort | **Open — new** |
| Q3 | Is the prediction-model comparison in scope, or association only? | Determines whether TRIPOD applies | Open |
| Q4 | ESI increment for the reported OR — per 5% or per 10%? | SAP §2 | Open |
| Q5 | Prior international presentation of this work? | ASPIRE eligibility | Open |
| **Q7** | **How is the study positioned given 4 meta-analyses already sit on the null?** Replication/refutation vs. novel index | The entire Introduction, Discussion and abstract framing | **Open — most important decision in the project** |
| Q8 | Keep the name "Endometrial Stability Index"? It is compaction expressed as % change, already published under that formula | Title, reviewer credibility | Open |
| Q9 | Restrict to euploid-only? Would occupy the strongest remaining gap but cuts N | Cohort definition, power | Open |
| Q10 | ASPIRE 2027 closes 6 November 2026. This study cannot make it: no ethics approval, no data. Submit a different abstract, or skip ASPIRE 2027? | Next realistic venue for ESI becomes a later congress; Q5 still governs eligibility | **Open — raised 3 Nov 2026** |

---

## Background work running

| Started | What | Status |
|---|---|---|
| 29 Aug 2026 | Literature review of prior endometrial compaction studies | **COMPLETE.** See `literature/REPORT.md`. |

### Outstanding literature action — before submission

- [ ] **Re-check De la Torre Perez 2023** (Front Endocrinol, PMID 38027116) — registered
      prospective euploid modified-natural-cycle compaction protocol, n=206, ~30 months.
      May have reported by now. If it has, it directly occupies part of the intended space.
- [ ] **Re-check ClinicalTrials.gov NCT04330066** — "Impact of Endometrial Compaction in
      Euploid Frozen Embryo Transfers". Status unverified.

---

## Session log

| Iteration | Date | Done | Asked for |
|---|---|---|---|
| 1 | 29 Aug 2026 | Repo created; ASPIRE rules captured; endpoint changed to implantation; Indira governance recorded; loop established; Methods drafted | D1, D2, D3 |
| 2 | 29 Aug 2026 | First-cycle-only applied across protocol, SAP, dictionary, manuscript; SAP §5 resolved; implantation definition options presented | Q1 choice, Q6, D2, D3 |
| 3 | 29 Aug 2026 | Primary endpoint set to β-hCG positivity (Amendment 4); raw-value + harmonised-threshold mitigations added; 6-week scan anchor recorded; data confirmed to exist | Q6, D3 |
| 4 | 29 Aug 2026 | **Literature review complete — novelty claim not defensible as framed.** Positioning decision Q7 raised | **Q7, Q8, Q9, D11** |
| — | 3 Nov 2026 | Side session, not a loop iteration: publication-landscape briefing for the investigator (`briefings/`). Title-level check of 61 Indira IVF items (2023–26, PubMed/Crossref) and 143 OpenAlex Indira records found **none on endometrial thickness change** — supports positioning ESI as new *within the network*, not new to the field. Investigator's one prior item: ESHRE 2025 poster P-493 (co-author, name printed "I Mekhala") | Q10 |
