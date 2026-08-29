---
name: protocol-guard
description: Audit an ESI study draft, protocol, analysis plan or results section for methodological problems — post-hoc cutoffs presented as prespecified, overclaimed novelty, clinical pregnancy substituted for live birth, unadjusted confounding, repeated-cycle non-independence, missing-as-zero coding, or numbers not traceable to analysis outputs. Use when the user asks to sanity-check the science, review the methods, check for reviewer objections, or asks whether the study or draft is methodologically sound.
---

# Protocol guard

Checks the science, not the formatting. For venue formatting use `aspire-compliance`.

## Procedure

1. Read `reference/traps-to-avoid.md` — the 21-item list.
2. Read `studies/esi-fet/PROTOCOL.md` and `SAP.md`. Note the SAP lock date.
3. Read the draft under review.
4. Check each trap against the draft. For each, either confirm compliance or quote
   the offending sentence.

## Severity

**Blocking** — would constitute misconduct or would sink the paper in review:
- A cutoff, subgroup or endpoint that appears in results but not in the SAP,
  presented as prespecified
- **Any wording implying live birth was measured.** It was not — the primary
  endpoint is implantation (SPEC.md Amendment 1). Watch for "improved outcomes",
  "success rates", "clinical benefit", "take-home baby". Each of these smuggles in
  an unmeasured endpoint.
- Any number not traceable to `outputs/`
- Any claim of priority over prior compaction literature
- Patient identifiers anywhere in the repo

**Serious** — a reviewer will raise it:
- Confounder omitted from adjustment without justification
- Repeated cycles unaddressed
- Interaction inferred from subgroup p-values
- Direction-of-effect assumed rather than tested
- Implantation presented without acknowledging it is an early surrogate

**Advisory** — improves the paper:
- Terminology drift toward "stability is good" or "receptivity"
- Missing sensitivity analysis
- Unstated limitation

## Rules

- Quote the specific sentence. Never say "the methods section has issues".
- If the SAP is not yet locked, say so — it changes what "prespecified" can mean.
- If a check cannot be run because the input does not exist, say the check was not
  run. Do not report it as passing.
