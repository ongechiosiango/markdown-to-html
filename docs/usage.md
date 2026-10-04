# Usage Guide

## Convert a file

    markdown-to-html input.md --output output.html

## Fragment only (no <html> wrapper)

    markdown-to-html input.md -o fragment.html --fragment

## Read from stdin, write to stdout

    cat input.md | markdown-to-html

## Custom title for the full document

    markdown-to-html input.md -o output.html --title "My Document"

## Exit codes

- 0 - success
- 1 - input or output error
