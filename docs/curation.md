# Curation

维护 Coding Agent、AI 软件工程、Agent 漏洞挖掘与安全领域的一手研究。

## 主页格式

- 条目只展示标题、首发日期、一个机构、一句话简介和必要的 Code / Artifacts / Blog 链接。
- 主页始终显示 `title` 中的完整原文标题，不以缩写、项目简称或悬停提示代替。
- `publication_kind` 为 `paper` 或 `blog`；每个关联链接填写 `kind`（`paper`、`code`、`blog`、`artifacts`、`project`、`enrollment`、`faq`）和可核实 URL。资源列先列原文 Paper / Blog，再列实际公开的 Code / Artifacts 与作者 Blog；同一 URL 去重，报名与 FAQ 不冒充代码或博客。
- 论文机构取一作在原文中的首个署名单位；共同一作取作者列表首位，多重署名只取第一个。博客取首位作者单位，无个人单位时取发布机构。
- `institution` 使用常用简称（如 UIUC、ETH Zürich、BAAI），核对链接保存在 `institution_source`。不拼接合作单位，不凭机构声誉选择署名。
- 一句话直接说清研究做了什么，通常 25–60 个中文字；证据边界与阅读范围保存在数据中。
- 主页保持适配明暗主题的居中横幅、轻量徽章、两列分类索引与分栏清单；标题、导航、表格本体与单元格均居中，单元格垂直居中。左列日期和一作单位，中列标题和一句话，右列统一显示 Paper / Blog 与已核实的 Code / Artifacts / 作者 Blog 链接。不添加收录规则、运行说明、声明或重复的最近收录表。

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

主页不展示贡献入口；本文件作为维护规则保留，不使用 GitHub 自动识别的 CONTRIBUTING 文件名。原始文章、代码和作者博客按实际公开情况记录，不填入无关仓库或转载链接。
