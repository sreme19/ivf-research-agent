---
name: paper-loop
description: Advance the ESI paper by one iteration — read the state board, write every section that is currently writable, run any analysis whose data has arrived, show the updated draft, and state precisely what data or decision is needed next. Use whenever the user says paper-loop, asks to continue or advance the paper, hands over new data or results for the study, asks what data is needed next, asks what analysis to run, or asks to see the current draft. This is the standing workflow for the ESI manuscript across many sessions.
---

# Paper loop

One paper, many days. Each invocation moves it forward by one iteration and ends
with a specific ask.

## State lives in a file, not in memory

**Always read `studies/esi-fet/PAPER-STATE.md` first.** It is the board: section
status, data ledger, analysis queue, open decisions, session log. Sessions end;
the board persists. Never infer where the paper stands from conversation history —
read the board.

Always update it before finishing. A loop that does not update its state is a loop
that restarts from zero next week.

## The six steps

### 1. Orient

Read `PAPER-STATE.md`. Report in three lines: what changed since last iteration,
what is now unblocked, what is still blocked and on what.

### 2. Absorb anything new

If the user supplied data, results, a decision, or a document this session:

- Save raw material to `inbox/YYYY-MM-DD-description.md` if it is reference
  material; patient-level data goes to `studies/esi-fet/data/` (gitignored) and
  **never** into inbox or any tracked file.
- Record it in the **Data ledger** on the board.
- Say what it unblocks. Be specific — "this unblocks Table 1 and the missingness
  report", not "this is helpful".
- If it contradicts something already written, say so and fix the draft.

### 3. Decide what analysis the new data supports

This is the step that carries the loop. For each new data element, state:

- Which analysis it enables, mapped to a numbered section of `SAP.md`
- Whether it is sufficient on its own or needs something else first
- What could go wrong with it — distribution, missingness, coding errors

**Check the data before analysing it.** Row count, missingness per variable,
implausible values, whether β-hCG-negative cycles were coded `0` and not `NA`,
whether ESI was derived in code rather than typed. Report what you found. A
silently accepted bad extract poisons everything downstream.

If the SAP is not yet locked, say so — it changes what any result can claim.

### 4. Write

Write every section that is currently writable, into
`studies/esi-fet/drafts/manuscript/MANUSCRIPT.md`. Update the ASPIRE abstract in
`studies/esi-fet/drafts/abstract/` when results exist to put in it.

**A great deal is writable before any data arrives.** Methods is almost entirely
writable from `PROTOCOL.md` and `SAP.md`. Do not wait for data to write it.

Rules while writing:

- Every number traceable to `studies/esi-fet/outputs/`. No exceptions.
  Unknown values are visible placeholders — `[N=TBD]`, `[aOR TBD (95% CI TBD)]` —
  never plausible-looking guesses. See `CLAUDE.md` rule 2.
- Primary endpoint is **implantation**. Never wording that implies live birth was
  measured. See `SPEC.md` Amendment 1.
- "Dynamic endometrial remodeling", not "stability is good". Never "receptivity"
  for an ultrasound measurement.
- Anything analysed that is not in the locked SAP is labelled **post-hoc** in the
  text.
- Mark each section `<!-- STATUS: DRAFT | NEEDS-DATA | FINAL -->` at its head.

### 5. Show the draft

Show the user what changed — the new or rewritten sections, not the whole
manuscript every time. Full manuscript only when they ask, or at a genuine
milestone.

Run `protocol-guard` on anything substantive before showing it. Run
`aspire-compliance` on any abstract draft.

### 6. Ask — precisely

End every iteration with a short numbered list under **What I need from you next**.

Each ask must be actionable by a busy clinician in one sitting:

- Bad: "I need the endometrial data."
- Good: "For the 40 pilot cycles: `ET1_MM`, `ET2_MM`, `PROG_START_DATE`,
  `TRANSFER_DATE`, `EMBRYO_GRADE`, `IMPLANTATION`. One row per cycle, `STUDY_ID`
  only. CSV or xlsx. This unblocks Table 1, the ESI distribution figure, and the
  missingness report."

Separate **blocking** asks from **nice-to-have**. Rank by what unblocks the most.
Three asks is usually right; more than five means the loop is being run too
infrequently.

Then update `PAPER-STATE.md` and stop.

## Rules for the loop itself

- **One paper.** This loop serves the ESI manuscript. A second study gets its own
  state file.
- **Never idle.** If the user supplied nothing, there is still writing to do, a
  literature gap to fill, or a decision to surface. An iteration that produces
  nothing but a request for data has been run too early — write something first.
- **Never fabricate to keep momentum.** A blocked section stays blocked and
  visible. Momentum is not worth a fabricated number.
- **Surface decisions, do not silently make them.** Where a scientific choice
  belongs to the investigator, put it in the ask list.
- **Say when to stop.** If the data shows the study is not viable, or the deadline
  is no longer reachable, say so plainly in the iteration. That is the loop working
  correctly, not failing.
