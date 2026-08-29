---
name: abstract-builder
description: Draft a congress abstract to a venue's exact word limit and required structure. Use when the user asks to write, draft, compose, tighten, cut down or rewrite an abstract for ASPIRE or another conference, or asks to fit an abstract within a word limit.
---

# Abstract builder

## Refuse to start without rules

Read `venues/<venue>/guidelines/`. If it contains no rules — official or
inherited — stop and say the limits are unknown. Drafting to a guessed word limit
means drafting twice. See `CLAUDE.md` rule 3.

For ASPIRE 2027 the working rules are in
`venues/aspire-2027/guidelines/abstract-rules.md`: 25-word UPPER CASE title,
300-word body including acknowledgements, mandatory Background and Aims / Methods /
Results / Conclusions.

## Refuse to invent results

Every number comes from `studies/<study>/outputs/`. If the analysis has not run,
draft with visible placeholders — `[aOR TBD (95% CI TBD)]`, `[N=TBD]` — never with
plausible-looking values. See `CLAUDE.md` rule 2.

## Budget the words before writing

At 300 words with four mandatory sections, allocation matters more than prose:

| Section | Target | Why |
|---|---|---|
| Background and Aims | 50–60 | Enough to establish the gap and state the question. No literature review. |
| Methods | 70–90 | Design, population, exposure definition, endpoint, analysis. The ESI formula earns its space. |
| Results | 110–130 | **The largest share.** N, the primary effect estimate with CI, the shape of the relationship, the model comparison. |
| Conclusions | 30–40 | What it means. One sentence of caveat. |

If Methods is crowding Results, cut Methods. Reviewers score on findings.

## Then

Hand the draft to `aspire-compliance` for the mechanical check before it goes
anywhere. Record the submitted version in `venues/<venue>/submissions/`.
