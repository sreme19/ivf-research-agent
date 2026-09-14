# CLAUDE.md — repro-research-agent

Guidance for Claude Code working in this repository.

## What this repo is

A research and publication workbench for reproductive-medicine studies. It holds
evidence, venue rules, protocols, analysis and drafts. It holds **no API key** and
runs no model calls of its own — the reasoning happens in whichever Claude Code
session is running one of the skills in `.claude/skills/`.

Active work: the Endometrial Stability Index (ESI) study for ASPIRE 2027.

---

## Hard rules

### 1. No patient data in git. Ever.

`studies/*/data/` is gitignored, as are all common data-file extensions repo-wide.

- Only `STUDY_ID` may appear in any analysis dataset.
- Never write a patient name, MRN, hospital ID, date of birth, phone number or
  address into any file in this repo — including examples, test fixtures and
  documentation.
- A linkage file mapping `STUDY_ID` back to patients must live **outside this
  repo entirely**, on the clinic's own secured storage.
- If a file is handed over that contains identifiers, stop, say so, and do not
  commit it. Do not attempt to de-identify it in place inside the repo.
- Before any `git add -A`, check what is actually staged.

### 2. Never fabricate a number, a citation, or a result.

This is a repo whose entire output is a scientific claim. Invented content here
does not produce a bug — it produces research misconduct.

- No invented sample sizes, effect sizes, p-values, confidence intervals or AUCs.
- No invented citations. Every reference needs a real, verifiable source; if it
  cannot be verified, mark it `[UNVERIFIED]` rather than presenting it.
- In drafts, unknown values stay as visible placeholders — `[N=TBD]`,
  `[aOR TBD (95% CI TBD)]` — never as plausible-looking guesses.
- Numbers in a draft must be traceable to a file in `outputs/`.

### 3. Venue rules are quoted, never remembered.

Do not write an abstract to a word limit from memory or inference. If
`venues/<venue>/guidelines/` does not contain the official rules with a source
and a retrieval date, the correct action is to say the rules are unknown and
get them — not to assume a plausible limit.

### 4. The SAP is locked before the data is analysed.

`studies/*/SAP.md` carries a lock date. After that date, changes are recorded as
dated amendments with a stated reason, appended to the file — never silent edits.
Choosing an ESI cutoff after seeing which one gives the best p-value, and then
presenting it as prespecified, is the single most damaging thing this project
could do to itself.

### 5. Direction neutrality.

The study does not assume endometrial compaction is beneficial. Drafts must not
drift into advocacy for a hypothesis. A rigorous null result is a publishable
result and must be written up as willingly as a positive one.

---

## Session discipline

This repo's memory already exists and `CLAUDE.md` never named it, so a session not running
`paper-loop` had no way to know it was there. It is:

| File | Holds |
|---|---|
| `studies/<study>/PAPER-STATE.md` | The board — section status, data ledger, analysis queue, **Open decisions**, and the **Session log** |
| `HANDOFF.md` | Cold start. Read first when you have no memory of the project |
| `reference/traps-to-avoid.md` | Durable methodological findings, checked by `protocol-guard` and `aspire-compliance` |
| `venues/` | Venue rules, quoted (hard rule 3) |

### Write into the board as the work happens, not before finishing

`PAPER-STATE.md` says "Update it before finishing." Do better than that: open it at the start
and add to it as each thread closes.

A session that saves the whole write-up for the end loses everything it never wrote down the
moment it runs out of context — and the long sessions, the ones that learned the most, are
exactly the ones that run out. Iteration 4 is the shape of the risk: a literature review that
found the novelty claim indefensible is one paragraph in the session log, and it changes the
whole paper. Written at the close, it exists only if the close arrives.

### Wrap up unprompted, and never write a rule into this file unasked

At the end of a session, without being asked, sort what was learned and say where each piece
goes:

- **a durable methodological finding** → `reference/traps-to-avoid.md`, or `venues/` if it is
  a venue rule (quoted, never remembered);
- **a fact about the study** → the board, the protocol, the SAP or the data dictionary,
  whichever owns it — and note in the **Session log** row that you changed it;
- **a decision that is the investigator's to make** → **Open decisions** on the board, with
  its consequence, the way Q7 and Q9 are already written;
- **a rule this repo should follow from now on** → this file.

Say so explicitly when something belongs nowhere. That is a finding too.

**Stop at the last one and ask.** Propose the rule, say what produced it, and wait. Recording
what was *found* — a trap, an open decision, a session-log row — needs no permission. A rule
in this file is a standing instruction to every future session here, written by the one party
that will never have to live with it being wrong. That matters more than usual in a repo whose
hard rules govern what may be claimed in a paper submitted under someone's name.

---

## Working conventions

- **Dates**: written in full — `6 November 2026`. Never "next month" or "in 10 weeks".
- **Raw over derived**: store `ET1 = 8.7`, never `ET1 = adequate`. Store `4AB`, never
  `good`. Categories are generated in analysis, never at data entry.
- **Missingness**: blank/`NA` = unavailable, `0` = confirmed absent, `1` = confirmed
  present. Missing is never coded as zero.
- **Regenerable outputs**: everything in `outputs/` must be reproducible by rerunning
  `analysis/`. Never hand-edit a table or figure.
- **inbox/ is not authoritative.** Files there are raw source material. Facts become
  authoritative only when compiled into `venues/` or `studies/`, with provenance.

## Terminology

- Prefer **"dynamic endometrial remodeling"** over "stability" in scientific prose —
  ESI is the index name, not a claim that no change is desirable.
- Never describe ultrasound thickness as measuring **"endometrial receptivity."**
  It is a surrogate phenotype, not a molecular measurement.
- Never claim dynamic endometrial change has not previously been studied. It has,
  with conflicting results. Novelty comes from method and endpoint, not from
  being first.

## Commands

There is no build. Analysis, once written, runs as:

```bash
Rscript studies/esi-fet/analysis/00_run_all.R
```
