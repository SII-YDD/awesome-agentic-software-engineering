#!/usr/bin/env python3
"""Validate the curated catalog and deterministically render its README (stdlib only)."""
import argparse
import datetime as dt
import json
import re
from html import escape
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    "coding-agents": "Coding Agents",
    "software-engineering": "AI Software Engineering",
    "vulnerability-discovery": "Vulnerability Discovery",
    "agent-security": "Agent Security",
}


def valid_date(value):
    assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", value), value
    dt.date.fromisoformat(value)


def validate(data):
    assert data["schema_version"] == 1
    valid_date(data["last_updated"])
    seen_ids, seen_urls, seen_papers = set(), set(), set()
    for item in data["entries"]:
        for key in ("id", "title", "institution", "publication_date", "added_date",
                    "updated_date", "type", "category", "canonical_url", "summary",
                    "caveat", "reading_scope", "evidence_status", "links"):
            assert item.get(key), (item.get("id"), key)
        assert re.fullmatch(r"[a-z0-9-]+", item["id"])
        assert item["category"] in CATEGORIES
        assert not any(sep in item["institution"] for sep in (" / ", " · ", ";", "；")), "Credit one institution only"
        assert "\n" not in item["summary"] and len(item["summary"]) <= 100, "Use one concise sentence"
        assert item["evidence_status"] in ("author-reported", "independently-reproduced")
        for field in ("publication_date", "added_date", "updated_date"):
            valid_date(item[field])
        assert item["publication_date"] <= item["added_date"] <= item["updated_date"] <= data["last_updated"]
        if item.get("blog_publication_date"):
            valid_date(item["blog_publication_date"])
        urls = [item["canonical_url"]] + [link["url"] for link in item["links"]]
        for url in urls:
            parsed = urlparse(url)
            assert parsed.scheme == "https" and parsed.netloc and not parsed.username, url
        canonical = item["canonical_url"].rstrip("/")
        assert item["id"] not in seen_ids, item["id"]
        assert canonical not in seen_urls, canonical
        seen_ids.add(item["id"])
        seen_urls.add(canonical)
        if item.get("paper_id"):
            assert re.fullmatch(r"\d{4}\.\d{4,5}", item["paper_id"])
            assert item["paper_id"] not in seen_papers, item["paper_id"]
            assert item["canonical_url"] == "https://arxiv.org/abs/" + item["paper_id"]
            seen_papers.add(item["paper_id"])
        assert "\n" not in item["title"]
        if item.get("display_title"):
            assert "\n" not in item["display_title"] and len(item["display_title"]) <= 80
    assert data["entries"], "Catalog must not be empty"


def compact_links(item):
    """Show only distinct code/artifact and author-blog links on the homepage."""
    output = []
    for link in item["links"]:
        label = link["label"]
        if "报名" in label or "FAQ" in label or link["url"] == item["canonical_url"]:
            continue
        if "博客" in label:
            output.append(f'<a href="{escape(link["url"], quote=True)}">Blog</a>')
        elif "实验材料" in label:
            output.append(f'<a href="{escape(link["url"], quote=True)}">Artifacts</a>')
        elif "代码" in label:
            output.append(f'<a href="{escape(link["url"], quote=True)}">Code</a>')
    return "<br>".join(output)


def table_text(value):
    return escape(value).replace("\n", " ")


def render(data):
    entries = sorted(data["entries"], key=lambda item: (item["publication_date"], item["title"]), reverse=True)
    lines = [
        '<p align="center">',
        '  <picture>',
        '    <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">',
        '    <img src="assets/hero-light.svg" alt="Awesome Coding &amp; Security Agents" width="100%">',
        '  </picture>',
        '</p>',
        "",
        '<p align="center">',
        '  <a href="https://github.com/sindresorhus/awesome"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>',
        f'  <a href="data/entries.json"><img src="https://img.shields.io/badge/papers_%26_blogs-{len(entries)}-6366f1?style=flat-square" alt="Papers and blogs: {len(entries)}"></a>',
        f'  <a href="updates/"><img src="https://img.shields.io/badge/updated-{data["last_updated"].replace("-", "--")}-14b8a6?style=flat-square" alt="Updated: {data["last_updated"]}"></a>',
        '</p>',
        "",
        '<table align="center" width="100%">',
    ]
    categories = list(CATEGORIES.items())
    for row in range(0, len(categories), 2):
        lines.append('  <tr>')
        for index in range(row, min(row + 2, len(categories))):
            slug, name = categories[index]
            count = sum(item["category"] == slug for item in entries)
            quantity = "entry" if count == 1 else "entries"
            lines.append(f'    <td width="50%" align="center" valign="middle"><a href="#{slug}"><b>{index + 1:02d} · {name}</b></a><br><sub>{count} {quantity}</sub></td>')
        lines.append('  </tr>')
    lines.append('</table>')
    for index, (slug, name) in enumerate(categories, 1):
        lines += ["", f'<a id="{slug}"></a>', "", f'<h2 align="center">{index:02d} · {name}</h2>', "",
                  '<table align="center" width="100%">',
                  '  <thead><tr><th width="17%" align="center">Date · Org</th><th width="73%" align="center">Research</th><th width="10%" align="center">Links</th></tr></thead>',
                  '  <tbody>']
        for item in entries:
            if item["category"] != slug:
                continue
            metadata = f"<code>{item['publication_date']}</code><br><sub>{table_text(item['institution'])}</sub>"
            label = table_text(item.get("display_title", item["title"]))
            research = f'<b><a href="{escape(item["canonical_url"], quote=True)}" title="{escape(item["title"], quote=True)}">{label}</a></b><br>{table_text(item["summary"])}'
            lines.append(f'    <tr><td align="center" valign="middle">{metadata}</td><td align="center" valign="middle">{research}</td><td align="center" valign="middle">{compact_links(item) or "—"}</td></tr>')
        lines += ['  </tbody>', '</table>', ""]
    lines += [
        "---",
        "",
        '<p align="center">',
        '  <a href="updates/">Changelog</a> &nbsp;·&nbsp;',
        '  <a href="CONTRIBUTING.md">Contribute</a> &nbsp;·&nbsp;',
        '  <a href="LICENSE">CC0 1.0</a>',
        '</p>',
        "",
        "<!-- Generated from data/entries.json by scripts/render.py. -->",
    ]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate schema and verify README matches catalog")
    args = parser.parse_args()
    data = json.loads((ROOT / "data/entries.json").read_text(encoding="utf-8"))
    validate(data)
    output = render(data)
    target = ROOT / "README.md"
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != output:
            raise SystemExit("README is stale: run python3 scripts/render.py")
    else:
        target.write_text(output, encoding="utf-8")
    print(f"Validated {len(data['entries'])} entries; README {'matches' if args.check else 'rendered'}.")


if __name__ == "__main__":
    main()
