"""Tests for the Markdown to HTML converter."""

from markdown_to_html.converter import to_html_document, to_html_fragment


def test_fragment_renders_heading():
    html = to_html_fragment("# Hello")
    assert "<h1" in html
    assert "Hello" in html


def test_fragment_renders_bold_and_italic():
    html = to_html_fragment("**bold** and *italic*")
    assert "<strong>bold</strong>" in html
    assert "<em>italic</em>" in html


def test_fragment_renders_fenced_code():
    html = to_html_fragment("```python\nprint('hi')\n```")
    assert "<pre>" in html
    assert "print" in html


def test_fragment_renders_tables():
    table_md = "| A | B |\n|---|---|\n| 1 | 2 |"
    html = to_html_fragment(table_md)
    assert "<table>" in html
    assert "<th>A</th>" in html
    assert "<td>1</td>" in html


def test_document_wraps_with_html_and_title():
    html = to_html_document("# Hi", title="My Title")
    assert html.startswith("<!DOCTYPE html>")
    assert "<title>My Title</title>" in html
    assert "<h1" in html


def test_document_default_title():
    html = to_html_document("plain text")
    assert "<title>Document</title>" in html


def test_fragment_does_not_wrap_with_html_tag():
    html = to_html_fragment("# Hi")
    assert "<!DOCTYPE html>" not in html
    assert "<html" not in html
