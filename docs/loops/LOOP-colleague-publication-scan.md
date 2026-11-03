# LOOP-colleague-publication-scan

**What it does.** For one clinician, finds what their colleagues have published, where,
and who wrote it, then the same for nearby clinics. The results go to the owner in chat
first, and a short PDF briefing follows only when the owner asks for it.

- First run: 2026-11-03.
- Session: "Wife's IVF publishing: what colleagues published, and a 5-page briefing PDF."
- Output of that run: commit `577a2dd`, `briefings/`.

**Input, by shape:** a clinician's name, often given by voice and misspelled. Their
employer is a multi-center clinic chain. Sometimes a named colleague at one branch, and
the city.

## The owner's rules for this loop

Word for word, from the first run:

- "Don't prepare any reports yet. Paint all the results here first so that I can take a
  look, and then finally a report can be published."
- "I would like to keep the PDF as four or five pages as possible. If not, make it under
  10 pages."

The repo's hard rules apply throughout. Never invent a paper, author, title, PMID or DOI.
Never present a snippet as a fact.

## Steps

### 1. Fix the names

Search the chain's own site for the clinician and the colleague. Try spelling variants of
a name given by voice. Record the exact spelling, the branch, the title and the
qualifications from the profile page.

*Check:* the profile page was opened, not seen in a snippet.

### 2. Search for their papers by name AND by affiliation

Run a PubMed author search. Then run an OpenAlex search on raw affiliation strings for
the chain and the city, and read every author list.

*Check:* the person's own papers are found both ways, or the gap is explained.

### 3. Scan the institution

Run these in parallel, one runner per source group:

- Europe PMC: `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=AFF:"<chain>"&format=json&pageSize=200`
- PubMed: `"<chain>"[ad]`, through E-utilities.
- OpenAlex: `raw_affiliation_strings.search:"<chain>"`. This is the only one of the three that
  catches ESHRE, ASRM and congress abstracts.

Record each count with its query and date. Read every record before ruling it in or out.

*Check:* the count quoted is the count the API returned.

### 4. Scan nearby clinics

Use the same Europe PMC query, with the city and its spelling variants (one paper spelled
it "Banglore") AND reproductive terms, from 2020 onward. Then filter by clinic name in
the affiliation. A clinic counts only when its name and the city appear in the same
affiliation line.

### 5. Re-fetch every item from its source

For PMIDs, use `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=<ids>&retmode=json`.
For DOIs, use `https://api.crossref.org/works/<doi>`. Take titles, journals, years and
author names only from these records. Mark a DOI that does not resolve as unverified and
leave it out of the list.

*Check:* every row in the table has a record behind it. Spot-check some rows by hand as
well.

### 6. Show the results in chat

**Stop point 1.** Show the profiles, the topic clusters with counts, the venues, and a
table of full titles with the people who wrote them. Wait for the owner. Do not build a
report.

### 7. Find each author's current role, if asked

- Pull each author's affiliation from OpenAlex. This is the affiliation at the time of
  the paper.
- Fetch the chain's doctor sitemap and every profile page on it.
- Read a removed profile as a 301 redirect to the directory. A slug that never existed
  returns 404. Test with a nonsense slug as a control.
- Mark LinkedIn facts as snippets, because LinkedIn blocks fetches.
- For an author named by initials only, say so, and match only on name plus branch.

**Stop point 2.** Show the people table in chat.

### 8. Build the briefing, when the owner says to

- Generate the HTML with a script from the stored records (`briefings/source/build.py`
  reads `out.json`). Never type titles by hand.
- Run the gate and the render in one chain, so a failed gate stops the render:
  `check-prose.py <html> && chrome --headless=new --no-pdf-header-footer --print-to-pdf=...`
- Count the pages with `pdfinfo`. Render images of the pages with `pdftoppm` and look at
  every one.

**Stop point 3.** Send the PDF to the owner. The owner sends it on. Commit only when the
owner says so.

## What to read back, not what the step reported

| Step | Proof |
|---|---|
| Names | The profile page text, opened |
| Counts | The API's own `hitCount`, with the query string |
| Paper rows | An E-utilities or Crossref record for each one |
| Current roles | The profile page as fetched, or a 301 with a 404 control beside it |
| PDF | The `pdfinfo` page count, and a look at every page image |
| Commit | `git show --stat HEAD`, then rebuild from a `git archive HEAD` copy and compare with `cmp` |

## Mistakes already made, and the check that now catches each

1. **"No publications" was reported, and it was wrong.** An ESHRE record printed the
   clinician's given and family names swapped, so the name search found nothing. Step 2
   now searches by affiliation too (see trap 22).
2. **A search snippet put a congress in the wrong city.** Venue facts now come only from
   the congress's own page, which is opened before it is quoted.
3. **A CSS width rule for one table broke the columns of a second table.** It was found
   only by looking at the page images. Step 8 requires that look.
4. **A shell variable holding a list of files was passed to `git add` as a single name.**
   zsh does not split words in a variable, so nothing was staged. Name each path in the
   command itself.
5. **Counts quoted from memory drifted** (first-author totals, items per person). Count
   them from the stored records before they go into the report.
