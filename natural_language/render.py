#!/usr/bin/env python3
"""Update this static page's content from its Markdown source using Pandoc."""

from pathlib import Path
import re
import subprocess


def main():
    directory = Path(__file__).resolve().parent
    markdown = (directory / "draft.md").read_text(encoding="utf-8")
    # The surrounding site template owns the visible page title.
    body = markdown.split("\n", 1)[1]
    rendered = subprocess.run(
        ["pandoc", "--from=markdown-implicit_figures", "--to=html5", "--wrap=auto"],
        input=body,
        text=True,
        capture_output=True,
        check=True,
    ).stdout
    # Markdown wraps for editing; the prompt wraps to the reader's screen.
    rendered = re.sub(
        r'(<pre id="starting-prompt"[^>]*><code>)(.*?)(</code></pre>)',
        lambda match: match[1]
        + "\n\n".join(
            " ".join(paragraph.splitlines())
            for paragraph in match[2].strip().split("\n\n")
        )
        + match[3],
        rendered,
        flags=re.S,
    )
    rendered = rendered.replace(
        '<p><strong>Your starting prompt</strong></p>',
        '<div class="prompt-toolbar"><span id="prompt-label">'
        'Your starting prompt</span>'
        '<button type="button" class="copy-prompt" '
        'aria-label="Copy prompt" aria-controls="starting-prompt" hidden>'
        'Copy</button></div>'
        '<span class="screen-reader-text" id="copy-status" '
        'role="status" aria-live="polite"></span>',
    )
    rendered = rendered.replace(
        '<pre id="starting-prompt"',
        '<pre tabindex="0" aria-labelledby="prompt-label" id="starting-prompt"',
    )
    # The notebook route is a plain link card: same header, no copy button.
    rendered = rendered.replace(
        '<p><strong>Prefer a notebook?</strong></p>',
        '<div class="prompt-toolbar"><span>Prefer a notebook?</span></div>',
    )
    rendered = rendered.replace(
        'src="../assets/images/cosmos_web_ring_rgb.png"',
        'src="../assets/images/cosmos_web_ring_rgb.png" '
        'width="840" height="840" decoding="async"',
    )
    page = directory / "index.html"
    updated, count = re.subn(
        r'(<div class="entry-content">).*?(</div><!-- .entry-content -->)',
        lambda match: match[1] + "\n" + rendered + "\n\t" + match[2],
        page.read_text(encoding="utf-8"),
        count=1,
        flags=re.S,
    )
    if count != 1:
        raise SystemExit("Expected one entry-content section in index.html")
    page.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
