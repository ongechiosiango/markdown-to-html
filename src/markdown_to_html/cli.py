"""Command-line interface for Markdown to HTML."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rich.console import Console

from . import __version__
from .converter import to_html_document, to_html_fragment

console = Console()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="markdown-to-html",
        description="Convert a Markdown file to HTML.",
    )
    parser.add_argument("input", nargs="?", default="-",
                        help="Input Markdown file (default: stdin).")
    parser.add_argument("--output", "-o", default="-",
                        help="Output HTML file (default: stdout).")
    parser.add_argument("--title", "-t", default="Document",
                        help="Document title used in the full HTML template.")
    parser.add_argument("--fragment", "-f", action="store_true",
                        help="Output only the HTML fragment (no <html> wrapper).")
    parser.add_argument("--version", action="version",
                        version=f"markdown-to-html {__version__}")
    return parser


def _read_input(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    if not p.is_file():
        raise IsADirectoryError(f"Not a file: {path}")
    return p.read_text(encoding="utf-8")


def _write_output(path: str, content: str) -> None:
    if path == "-":
        sys.stdout.write(content)
        if not content.endswith("\n"):
            sys.stdout.write("\n")
        return
    Path(path).write_text(content, encoding="utf-8")


def main() -> int:
    args = build_parser().parse_args()

    try:
        text = _read_input(args.input)
    except (FileNotFoundError, IsADirectoryError, OSError) as exc:
        console.print(f"[bold red]Error:[/bold red] {exc}")
        return 1

    if args.fragment:
        html = to_html_fragment(text)
    else:
        html = to_html_document(text, title=args.title)

    try:
        _write_output(args.output, html)
    except OSError as exc:
        console.print(f"[bold red]Error writing output:[/bold red] {exc}")
        return 1

    if args.output != "-":
        console.print(f"[bold green]Wrote[/bold green] {args.output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
