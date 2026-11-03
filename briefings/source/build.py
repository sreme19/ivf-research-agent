"""Build the briefing HTML from the verified paper records (out.json) plus hand-written sections."""
import html, json, re, sys

recs = {r["n"]: r for r in json.load(open(sys.argv[1]))}
OUT = sys.argv[2]

CLUSTERS = [
    ("Ovarian stimulation, trigger and poor responders", [1, 3, 7, 14, 17, 19, 25, 26, 30, 31, 37, 39, 52, 61]),
    ("Luteal support, frozen embryo transfer and endometrium", [8, 15, 18, 20, 21, 33, 43, 48, 58, 59, 60]),
    ("Male factor and sperm DNA damage", [4, 5, 11, 28, 32, 34, 42, 45, 46, 55]),
    ("Embryology lab quality and transfer media", [6, 9, 10, 27, 40, 53, 57]),
    ("Genetic testing of embryos (PGT-A) and AI embryo grading", [13, 16, 29, 41, 47]),
    ("Repeated miscarriage and immune therapy", [22, 24, 54, 56]),
    ("Patient factors, psychology and quality of life", [2, 12, 23, 36, 44]),
    ("Case reports and other topics", [35, 38, 51, 49, 50]),
]

HR = "Human Reproduction (ESHRE {} poster)"
FR23 = "Fertility &amp; Reproduction (2023 congress abstract)"
VENUE = {
    1: "J Reprod Healthc Med", 2: "J Clin Basic Psychosomatics", 3: "Int J Clin Obstet Gynaecol",
    4: "Frontiers in Urology", 5: "Frontiers in Reprod Health", 6: "RBMO", 7: "Int J Reprod Res",
    8: HR.format(2026), 9: "RBMO", 10: "RBMO", 11: HR.format(2026), 12: HR.format(2026),
    13: "Scientific Reports", 14: HR.format(2026), 15: HR.format(2026), 16: "Research Square (preprint)",
    17: "Research Square (preprint)", 18: HR.format(2026), 19: "Minerva Obstet Gynecol", 20: "RBMO",
    21: "SSRN (preprint)", 22: "SSRN (preprint)", 23: "J Reprod Healthc Med", 24: HR.format(2025),
    25: "Fertility and Sterility", 26: "Reproduction and Fertility",
    27: "Fertility and Sterility (ASRM 2025 abstract)", 28: "Fertility and Sterility (ASRM 2025 abstract)",
    29: HR.format(2025), 30: HR.format(2025), 31: "Cureus", 32: "J Hum Reprod Sci", 33: "Clin Exp Reprod Med",
    34: "J Hum Reprod Sci", 35: "J Obstet Gynecol India", 36: "Int J Infertil Fetal Med",
    37: "Springer book chapter", 38: "J Clin Images Med Case Rep", 39: "Reproduction &amp; Fertility",
    40: "Cureus", 41: "RBMO", 42: "RBMO", 43: "Fertility &amp; Reproduction", 44: "Int J Nutr Pharmacol Neurol Dis",
    45: "Int J Nurs Health Care Res", 46: HR.format(2024), 47: HR.format(2024), 48: HR.format(2024),
    49: "J Clin Exp Hepatol", 50: "JCO Global Oncology", 51: "J Clin Images Med Case Rep",
    52: "Fertility and Sterility (ASRM 2023 abstract)", 53: HR.format(2023), 54: HR.format(2023),
    55: FR23, 56: FR23, 57: FR23, 58: FR23, 59: FR23, 60: FR23, 61: "J IVF-Worldwide",
}

TITLE_FIX = {
    27: "Does Total Oocyte Exposure Time to HEPES During Processing and ICSI Correlate with Laboratory and Clinical Outcomes When Temperature Based IVF Chamber Is Used?",
    28: "Impact of High DNA Fragmentation Index on Fertilization and Blastocyst Development Rates: A Comparative Analysis Using Ejaculatory Sperm and Testicular Biopsy in Sibling Oocytes",
    52: "IVF Stimulation Optimized, Personalized, and Simplified Using an Advanced Decision-Support Tool",
}

B = " <b>(Bengaluru)</b>"
WHO = {
    7: "Shashank Sanagoudar",
    8: "S. Gupta" + B + "; S. Bhandari" + B,
    10: "Naval Shah; Kshitiz Murdia (with Jishnu PS" + B + ")",
    11: "N. Aggarwal; S. Gupta" + B,
    16: "Anil Kumar; Arvind Vaid",
    17: "Alessandro Conforti; Carlo Alviggi (Indira: V. Chandra, K. Murdia and team)",
    20: "Georg Griesinger (Indira: Kshitiz Murdia)",
    21: "Vipin Chandra", 22: "Vipin Chandra",
    24: "Vasanthi Palanivel (Seragen); C Srinivas (Seragen), with Shyam Gupta and <b>Mekhala Iyengar</b>" + B,
    26: "Urmila Diwekar; Sanjay Joag (with Shyam Nandan Gupta" + B + ")",
    34: "Sonali Bhan; Audesh Bhat (Indira: Manisha Bhagat)",
    39: "Urmila Diwekar; Sanjay Joag (with Shyam Gupta" + B + ")",
    43: "Peter Humaidan; Ritu Punhani",
    45: "Authors missing from the record",
    49: "Amar Mukund; Shiv Kumar Sarin (Indira: Yasha Pandey)",
    50: "Sharada Mailankody; Shripad Banavali (Indira: Rinoy Sreedharan)",
    51: "Indira IVF Pune team; Nihar Ranjan Bhoi",
    54: "Vasanthi Palanivel (Seragen); G Shyam N" + B,
    55: "Shyam Nandan Gupta" + B + "; Deepak Pandey" + B,
    56: "Shyam Nandan Gupta" + B + "; Jishnu PS" + B,
}


def title(n):
    t = TITLE_FIX.get(n) or html.unescape(recs[str(n)]["title"])
    t = re.sub(r"^(L26/)?P-\d+\s+|^#\d+\s*:\s*", "", t).rstrip(".")
    return html.escape(t)


def who(n):
    if n in WHO:
        return WHO[n]
    a = recs[str(n)]["authors"]
    s = html.escape(a[0])
    if len(a) > 1 and a[-1] != a[0]:
        s += "; " + html.escape(a[-1])
    return s


rows = []
assert sorted(sum((c[1] for c in CLUSTERS), [])) == list(range(1, 62)), "cluster map must cover 61 items once"
for name, ns in CLUSTERS:
    rows.append(f'<tr class="grp"><td colspan="3">{name} ({len(ns)})</td></tr>')
    for n in sorted(ns, key=lambda n: -int(str(recs[str(n)]["year"])[:4])):
        y = str(recs[str(n)]["year"])[:4]
        rows.append(f"<tr><td>{title(n)}</td><td>{VENUE[n]}, {y}</td><td>{who(n)}</td></tr>")
papers = "\n".join(rows)

tpl = open(sys.argv[3]).read()
open(OUT, "w").write(tpl.replace("<!--PAPERS-->", papers))
print("rows", len(rows) - len(CLUSTERS))
