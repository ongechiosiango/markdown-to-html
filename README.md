# Markdown to HTML

[![CI](https://github.com/ongechiosiango/markdown-to-html/actions/workflows/ci.yml/badge.svg)](https://github.com/ongechiosiango/markdown-to-html/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)

Convert Markdown files to HTML with a simple CLI.

## Features

- Convert a Markdown file (or stdin) to HTML.
- Full HTML document output with embedded CSS and dark-mode support.
- Fragment mode (--fragment) for embedding in other pages.
- Support for fenced code blocks, tables, and TOC.
- Reads from stdin, writes to stdout when no paths are given.

## Installation

From source:

    git clone git@github.com:ongechiosiango/markdown-to-html.git
    cd markdown-to-html
    python3 -m venv venv
    source venv/bin/activate
    pip install -e ".[dev]"

## Usage

    markdown-to-html input.md --output output.html

Or with stdin/stdout:

    cat input.md | markdown-to-html

See docs/usage.md for more.

## Development

    pip install -e ".[dev]"
    pytest -v

## Contributing

See CONTRIBUTING.md.

## License

MIT - see LICENSE.
