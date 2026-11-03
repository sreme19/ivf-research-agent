# IVF Research Agent

A research and publication workbench for reproductive-medicine studies.

Zero-API and skill-driven, following the same pattern as `job-hunt-agent`,
`finance-controls-agent` and `ad-management-agent`: the thinking happens live in
a Claude Code session running one of the skills in `.claude/skills/`; the repo
itself only stores evidence, guidelines, protocols and drafts.

**Current work:** the Endometrial Stability Index (ESI) study — does dynamic change
in endometrial thickness during progesterone exposure predict **implantation** after
single blastocyst FET? Data from **Indira IVF** (India). Targeted at the ASPIRE 2027
congress in Yokohama (abstract deadline **6 November 2026**), then at Fertility &
Reproduction.

---

## The two axes

The repo separates two things that most research repos conflate:

| Axis | Lives in | Reusable because |
|---|---|---|
| **Venue** — a congress or journal, its rules, its history | `venues/` | The same study can go to a congress *and* a journal |
| **Study** — a research question, its protocol, data, analysis | `studies/` | The same venue will host your next study too |

They are paired only at submission time, in `venues/<venue>/submissions/`.

Adding a second publication means adding `studies/<name>/`.
Adding a second conference means adding `venues/<name>/`.
Neither touches the other.

---

## Layout

```
inbox/            Raw material you hand over, unprocessed and dated.
                  Nothing here is authoritative until it is compiled out.

venues/
  aspire-2027/
    venue.md      Confirmed facts: dates, theme, contacts, portal.
    guidelines/   OFFICIAL submission rules, verbatim and sourced.
    history/      Past congresses, accepted-topic patterns, award criteria.
    submissions/  What was actually submitted, and what happened.

studies/
  esi-fet/
    PROTOCOL.md         Design, population, definitions, endpoints.
    SAP.md              Statistical analysis plan. Locked before analysis.
    data-dictionary.md  Every variable, its type, coding and source.
    feasibility/        The pilot that decides whether this study is possible.
    literature/         Prior work + the evidence table that scopes novelty.
    data/               GITIGNORED. De-identified extracts only.
    analysis/           R scripts. Regenerate everything in outputs/.
    outputs/            Tables and figures. Disposable by design.
    drafts/abstract/    The ASPIRE version.
    drafts/manuscript/  The full paper.

reference/        STROBE, TRIPOD, and the methodological traps list.
```

---

## Start here

1. `ROADMAP.md` — the 69-day countdown to the abstract deadline and what gates what.
2. `studies/esi-fet/feasibility/pilot-questions.md` — the ten questions that decide
   whether the retrospective study is viable at all.
3. `venues/aspire-2027/guidelines/README.md` — what we still do not know about the
   submission rules, and how to get it.

## Skills

| Skill | Use it to |
|---|---|
| `literature-scan` | Build the evidence table of prior compaction/remodeling work |
| `abstract-builder` | Draft to a venue's real word limit and structure |
| `protocol-guard` | Audit a draft against the methodological traps list |
| `manuscript-drafter` | Produce the STROBE/TRIPOD-structured full paper |

## Conventions

- Analysis in **R** (`rms` for splines, `pROC`, `dcurves` for decision curves).
  Nothing is written yet — this is swappable.
- Local git only. No remote until the gitignore has been proven against a real extract.
- Dates written in full (`6 November 2026`), never relative.
