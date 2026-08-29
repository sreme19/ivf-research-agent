# Feasibility pilot — 30–50 cases

**Run this before extracting hundreds of records.** Target completion:
**15 September 2026**.

The pilot is not a formality. It decides whether the ASPIRE 2027 submission is
possible at all, and it is cheap compared to discovering the answer in October.

---

## The gate

> **Question 2 below is the gate. Answer it first.**
>
> If transfer-day endometrial thickness (ET2) was not routinely and consistently
> recorded, the retrospective study cannot be done, and ESI must become a
> prospective project — which cannot make the 6 November 2026 deadline.

Answer it from actual chart review of consecutive cases, not from recollection of
what is usually recorded.

---

## The ten questions

| # | Question | Answer | n/N | % missing |
|---|---|---|---|---|
| 1 | Is ET measured at **both** required time points? | | | |
| 2 | **How consistently is transfer-day ET (ET2) recorded?** | | | |
| 3 | Is progesterone start **time** available, not just date? | | | |
| 4 | Are D5/D6 and Gardner grades reliably available? | | | |
| 5 | Is live-birth follow-up complete? | | | |
| 6 | Are PGT-A data available? | | | |
| 7 | Is serum P4 measured routinely before transfer? | | | |
| 8 | Are endometrial patterns recorded at both scans? | | | |
| 9 | How many women have multiple FETs? | | | |
| 10 | How much missingness exists per field? | | | |

## Method

1. Select 30–50 **consecutive** eligible cycles — not a convenience sample of
   complete-looking records. Consecutive selection is what makes the missingness
   estimate honest.
2. Attempt to populate every field in `../data-dictionary.md`.
3. Record what could not be found, and why.
4. Time how long one record takes. Multiply by the target N. If a full extraction
   would take 300 hours, that is a finding.

## What each answer changes

| Finding | Consequence |
|---|---|
| ET2 missing in >30% of cycles | Retrospective study not viable. Go to the ROADMAP fallbacks. |
| Progesterone **time** unavailable | Exposure duration in days only. Acceptable; state as a limitation. |
| Live-birth follow-up incomplete | Primary endpoint at risk. Quantify before deciding. |
| PGT-A rare | Euploid subgroup unpowered. Drop it from the SAP rather than run it underpowered. |
| Serum P4 not routine | Drop from the adjustment set. Do not order non-routine tests to fill a retrospective dataset. |
| Many women with multiple FETs | Decides SAP §5 — first-cycle-only vs clustered. |
| Pattern missing at ET1 or ET2 | Drop pattern from adjustment, or accept imputation. |

## Output

Write findings to `pilot-results.md` in this directory, then update:

- `../PROTOCOL.md` — eligibility and variables that survive
- `../SAP.md` — the [TBD] items the pilot resolves, then **lock it**
- `../../../ROADMAP.md` — the status log and the go/no-go decision

## Reminder

Pilot data is patient data. It goes in `../data/`, which is gitignored. Not here.
