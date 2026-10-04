"""Convert Markdown text to HTML."""

from __future__ import annotations

import markdown as md


DEFAULT_EXTENSIONS = [
    "fenced_code",
    "tables",
    "toc",
    "sane_lists",
]


DEFAULT_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      max-width: 720px;
      margin: 2rem auto;
      padding: 0 1rem;
      line-height: 1.65;
      color: #222;
      background: #fff;
    }}
    @media (prefers-color-scheme: dark) {{
      body {{ color: #e6e6e6; background: #121212; }}
      a {{ color: #6cb6ff; }}
      pre, code {{ background: #1e1e1e; }}
    }}
    pre, code {{
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      background: #f4f4f4;
      border-radius: 4px;
    }}
    code {{ padding: 0.15em 0.35em; }}
    pre {{ padding: 0.9em 1em; overflow-x: auto; }}
    pre code {{ padding: 0; background: transparent; }}
    table {{ border-collapse: collapse; }}
    th, td {{ border: 1px solid #ccc; padding: 0.4em 0.8em; }}
  </style>
</head>
<body>
{body}
</body>
</html>
"""


def to_html_fragment(text: str) -> str:
    """Convert Markdown text to an HTML fragment (no <html> wrapper)."""
    return md.markdown(text, extensions=DEFAULT_EXTENSIONS, output_format="html5")


def to_html_document(text: str, title: str = "Document") -> str:
    """Convert Markdown text to a full HTML document with embedded CSS."""
    fragment = to_html_fragment(text)
    return DEFAULT_TEMPLATE.format(title=title, body=fragment)
