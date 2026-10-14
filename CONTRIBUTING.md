# Contributing

欢迎提交 Coding Agent、AI 软件工程、Agent 漏洞挖掘与安全领域的一手研究，或纠正已收录内容。

## 收录要求

- 提供规范原文、明确作者/团队和首次发布日期。优先有实质技术新意与实验证据的成果。
- 同一研究的博客、论文与代码作为一个条目；arXiv 版本号不能当作新的论文 ID。
- 技术说明用自己的话解释问题与方法，并给出结果的适用范围；不要复制整段摘要。
- 标明预印本/已评审、阅读范围、作者报告/独立复现。宣称独立复现需要公开记录。
- 区分已确认漏洞、待核实报告、CVE、候选补丁与已合并修复。不要把报名入口误标为完整实现。
- 不接受转载、营销介绍、无证据排名和未核实机构归属。缺少实验全文应明确说明。

## 修改流程

1. 在 `data/entries.json` 增加或更正条目，沿用现有字段结构。`added_date` 是首次收录日期，`publication_date` 是首次研究公开日期。
2. 主分类使用 `coding-agents`、`software-engineering`、`vulnerability-discovery` 或 `agent-security`；交叉领域使用 `tags`。
3. 实质更新时修改 `updated_date`，保留原始发布日期并记录新增证据；同步更新顶层 `last_updated`。
4. 在 `updates/YYYY-MM-DD.md` 写当日新增/更正和原文链接。初始收录与新研究发布分别描述。
5. 运行以下命令再提交 PR：

```sh
python3 scripts/render.py
python3 scripts/render.py --check
```

维护者每日北京时间 09:00 的研究阅读任务会检索新成果并更新这个仓库。运行任务需已有执行环境与 GitHub 授权；克隆本仓库本身不会自动触发定时更新。没有合格新成果时不添加占位条目。
