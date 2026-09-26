#!/usr/bin/env python3
"""Refresh the full Euclid paper list on this page from the arXiv API."""

from datetime import date
from html import escape, unescape
from pathlib import Path
import re
import subprocess
import time

AUTHOR_QUERIES = [
    "au:Nightingale_J",
    'au:"James Nightingale"',
    'au:"J. W. Nightingale"',
    'au:"James W. Nightingale"',
]
START = "<!-- euclid-papers:start -->"
END = "<!-- euclid-papers:end -->"

# arXiv titles keep LaTeX markup; these are the readable forms.
TITLE_FIXES = {
    "$Λ$CDM": "ΛCDM",
    "\\Euclid Flagship simulation\\": "Euclid Flagship simulation",
    "$z>$ 1.3": "z > 1.3",
    "$z=0.25$ and $z=1$": "z = 0.25 and z = 1",
    "$z<1$": "z < 1",
    "$r_{\\rm b}$-$M_\\ast$": "r<sub>b</sub>–M<sub>∗</sub>",
    "$5 \\times 10^9 M_\\odot$": "5 × 10<sup>9</sup> M<sub>⊙</sub>",
    "$Euclid$": "Euclid",
    " -- ": " – ",
}


def fetch(query):
    # arXiv rejects Python's HTTP client here (HTTP 406), so use curl.
    return subprocess.run(
        [
            "curl", "--silent", "--show-error", "--fail", "--get",
            "--max-time", "120",
            "--data-urlencode", f"search_query={query}",
            "--data-urlencode", "max_results=1000",
            "https://export.arxiv.org/api/query",
        ],
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def euclid_papers():
    papers = {}
    for query in AUTHOR_QUERIES:
        for entry in re.findall(r"<entry>(.*?)</entry>", fetch(query), re.S):
            arxiv_id = re.search(
                r"<id>http://arxiv.org/abs/(.*?)(?:v\d+)?</id>", entry
            )[1]
            title = " ".join(re.search(r"<title>(.*?)</title>", entry, re.S)[1].split())
            if "Euclid" in title:
                published = re.search(r"<published>(.*?)</published>", entry)[1]
                papers[arxiv_id] = (published[:10], unescape(title))
        time.sleep(3)
    return sorted(papers.items(), key=lambda item: item[1][0], reverse=True)


def readable(title):
    title = escape(title, quote=False)
    for latex, text in TITLE_FIXES.items():
        title = title.replace(escape(latex, quote=False), text)
    return title


def main():
    papers = euclid_papers()
    items = "\n".join(
        f'<li><a href="https://arxiv.org/abs/{arxiv_id}">{readable(title)}</a>'
        f' <span class="euclid-paper-year">({published[:4]})</span></li>'
        for arxiv_id, (published, title) in papers
    )
    block = f"""{START}
<h2 id="every-euclid-paper">Every Euclid Paper (So Far)</h2>
<p class="wp-block-paragraph">Large collaborations make for long author lists.
As a member of the Euclid Consortium, my name appears on every one of the
<strong>{len(papers)} papers</strong> below, as of {date.today():%B %Y} and
rising quickly. They are listed in full, newest first, partly for completeness
and partly because it is quite satisfying to scroll through.</p>
<div class="euclid-papers" tabindex="0" role="region" aria-label="All Euclid papers">
<ol reversed>
{items}
</ol>
</div>
<p class="euclid-papers-note">Compiled from arXiv author metadata; each title
links to its arXiv entry.</p>
{END}"""
    page = Path(__file__).resolve().parent / "index.html"
    html = page.read_text(encoding="utf-8")
    if START in html:
        html = re.sub(
            re.escape(START) + ".*?" + re.escape(END),
            lambda _: block,
            html,
            flags=re.S,
        )
    else:
        anchor = "https://pyautocti.readthedocs.io/en/latest/</a></p>"
        html = html.replace(anchor, anchor + "\n\n" + block, 1)
    page.write_text(html, encoding="utf-8")
    print(f"Wrote {len(papers)} Euclid papers to {page}")


if __name__ == "__main__":
    main()
