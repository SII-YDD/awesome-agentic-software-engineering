#!/usr/bin/env python3
"""Validate the curated catalog and deterministically render its README (stdlib only)."""
import argparse
import datetime as dt
import json
import re
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
    assert data["entries"], "Catalog must not be empty"


def compact_links(item):
    """Show only distinct code/artifact and author-blog links on the homepage."""
    output = []
    for link in item["links"]:
        label = link["label"]
        if "报名" in label or "FAQ" in label or link["url"] == item["canonical_url"]:
            continue
        if "博客" in label:
            output.append(f"[Blog]({link['url']})")
        elif "实验材料" in label:
            output.append(f"[Artifacts]({link['url']})")
        elif "代码" in label:
            output.append(f"[Code]({link['url']})")
    return " · ".join(output)


def render(data):
    entries = sorted(data["entries"], key=lambda item: (item["publication_date"], item["title"]), reverse=True)
    lines = [
        '<h1 align="center">Awesome Agentic Software Engineering</h1>',
        "",
        '<p align="center">Coding Agents · AI Software Engineering · Agent Security</p>',
        "",
        '<p align="center">',
        '  <a href="https://github.com/sindresorhus/awesome"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>',
        f'  <a href="data/entries.json"><img src="https://img.shields.io/badge/papers_%26_blogs-{len(entries)}-6366f1?style=flat-square" alt="Papers and blogs: {len(entries)}"></a>',
        f'  <a href="updates/"><img src="https://img.shields.io/badge/updated-{data["last_updated"].replace("-", "--")}-14b8a6?style=flat-square" alt="Updated: {data["last_updated"]}"></a>',
        '</p>',
        "",
        '<p align="center">',
        '  <a href="#coding-agents">Coding Agents</a> &nbsp;·&nbsp;',
        '  <a href="#software-engineering">Software Engineering</a> &nbsp;·&nbsp;',
        '  <a href="#vulnerability-discovery">Vulnerability Discovery</a> &nbsp;·&nbsp;',
        '  <a href="#agent-security">Agent Security</a>',
        '</p>',
    ]
    for slug, name in CATEGORIES.items():
        lines += ["", f'<a id="{slug}"></a>', "", f"## {name}", ""]
        for item in entries:
            if item["category"] != slug:
                continue
            metadata = f"`{item['publication_date']}` · {item['institution']}"
            links = compact_links(item)
            if links:
                metadata += " · " + links
            lines += [
                f"- **[{item['title']}]({item['canonical_url']})** · {metadata}<br>{item['summary']}",
                "",
            ]
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
