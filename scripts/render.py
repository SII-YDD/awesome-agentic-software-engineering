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
    "coding-agents": "Coding Agents · 自主编程与协作",
    "software-engineering": "AI Software Engineering · 测试、调试与评测",
    "vulnerability-discovery": "Agentic Vulnerability Discovery · 漏洞发现与修复",
    "agent-security": "Agent Security & Reliability · Agent 安全与可靠性",
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


def cell(value):
    return value.replace("|", "\\|").replace("\n", " ")


def render(data):
    entries = sorted(data["entries"], key=lambda item: (item["publication_date"], item["title"]), reverse=True)
    lines = [
        "# Awesome Agentic Software Engineering",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome) [![License: CC0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](LICENSE)",
        "",
        "> A curated reading list of coding agents, AI software engineering, and agentic vulnerability research — with Chinese technical notes and explicit evidence limits.",
        "",
        "精选 Coding Agent、AI 软件工程、Agent 漏洞发现与安全研究的一手论文和技术博客。每项提供团队、首发日期、核心方法、原文/材料链接和证据边界，方便阅读与复现。",
        "",
        f"**最近更新：{data['last_updated']}（Asia/Shanghai） · {len(entries)} 项成果**。每日北京时间 09:00 的研究阅读任务同步维护本清单；合格新成果不足时保留实际数量。最后更新时间代表成功维护日期，不承诺每日都有新论文。",
        "",
        "## Contents",
        "",
        "- [Latest additions · 最近收录](#latest-additions)",
    ]
    lines += [f"- [{name}](#{slug})" for slug, name in CATEGORIES.items()]
    lines += [
        "- [Selection & update rules · 收录与更新规则](#selection-rules)",
        "- [更新记录](updates/) · [结构化数据](data/entries.json) · [贡献指南](CONTRIBUTING.md)",
        "",
        '<a id="latest-additions"></a>',
        "",
        "## Latest additions · 最近收录",
        "",
        "按收录日期排序，同日按原始发布日期排序；收录时间与研究首发时间分别展示。",
        "",
        "| 收录日期 | 研究首发 | 成果 | 团队 |",
        "| --- | --- | --- | --- |",
    ]
    latest = sorted(entries, key=lambda item: (item["added_date"], item["publication_date"], item["title"]), reverse=True)[:6]
    for item in latest:
        lines.append(f"| {item['added_date']} | {item['publication_date']} | [{cell(item['title'])}](#{item['id']}) | {cell(item['institution'])} |")
    for slug, name in CATEGORIES.items():
        lines += ["", f'<a id="{slug}"></a>', "", f"## {name}", ""]
        for item in entries:
            if item["category"] != slug:
                continue
            links = " · ".join(f"[{link['label']}]({link['url']})" for link in item["links"])
            dates = item["publication_date"]
            if item.get("blog_publication_date"):
                dates += f"；作者博客 {item['blog_publication_date']}"
            lines += [
                f'<a id="{item["id"]}"></a>',
                "",
                f"- **[{item['title']}]({item['canonical_url']})**",
                f"  - **团队 / 首发 / 类型：** {item['institution']} · {dates} · {item['type']}",
                f"  - **核心：** {item['summary']}",
                f"  - **证据边界：** {item['caveat']}",
                f"  - **阅读范围：** {item['reading_scope']}；" + ("独立复现（见所附记录）。" if item['evidence_status'] == 'independently-reproduced' else "结论及数字来自作者，未独立复跑。"),
                f"  - **材料：** {links}",
                "",
            ]
    lines += [
        '<a id="selection-rules"></a>',
        "",
        "## Selection & update rules · 收录与更新规则",
        "",
        "1. **一手来源。** 官方研究博客、作者/实验室论文、正式会议论文和关联官方代码；明确团队署名与发布日期。预印本单独标明，未经核实不写已录用。",
        "2. **技术价值。** 要有具体问题、方法与可核查证据。机构声誉只作筛选线索；不收营销公告、转载、无研究支撑的新闻，不给无依据的热度排名。",
        "3. **优先最新。** 日常检索优先最近 72 小时，必要时扩大至 7/14 天；按首次研究发布记录日期。新博客解读旧论文不会变成第二篇成果，重大更新须说明新增证据。",
        "4. **可解释与可核查。** 阅读方法和实验后写简明原创说明，区分作者报告、独立验证与个人判断。只做初步阅读的条目明确标注，不宣称通读。",
        "5. **按成果去重。** 使用规范原文 URL 和 arXiv ID；同一成果的博客、论文和代码放在同一条。每项归入一个主要分类，交叉主题可在数据标签中检索。",
        "6. **保持证据口径。** 写清样本、基线、指标、成本与适用条件；崩溃、漏洞、CVE、已确认报告与合并修复不互相替代。代码链接注明是完整实现、实验材料还是报名入口。",
        "7. **可追踪维护。** 数据更新后重新生成主页，保留按日更新记录；没有合格新成果不凑数。链接失效记录原因并寻找规范迁移地址，不凭猜测换链接。",
        "",
        "持续关注 OpenAI、Anthropic、Google DeepMind / Research、Microsoft Research / FORGE、Meta、NVIDIA，以及 UIUC、Stanford、MIT、CMU、UC Berkeley、ETH Zürich 等同级研究团队。该关注列表不表示仓库已收录各机构成果，也不代表任何机构背书。",
        "",
        "本仓库由维护者使用 AI 辅助检索与整理。启动清单来自 2026-10-12 至 2026-10-14 的研究阅读记录，属于持续扩展的精选集。欢迎通过 [贡献指南](CONTRIBUTING.md) 提交更正和有证据的新成果。",
        "",
        "## License",
        "",
        "本仓库原创整理与脚本采用 [CC0 1.0](LICENSE)。所链接论文、代码、商标及图像遵循各自原作者的许可。",
        "",
        "<!-- Generated from data/entries.json by scripts/render.py. Edit data first. -->",
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
