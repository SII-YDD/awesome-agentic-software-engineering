# Awesome Agentic Software Engineering

[![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome) [![License: CC0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](LICENSE)

> A curated reading list of coding agents, AI software engineering, and agentic vulnerability research — with Chinese technical notes and explicit evidence limits.

精选 Coding Agent、AI 软件工程、Agent 漏洞发现与安全研究的一手论文和技术博客。每项提供团队、首发日期、核心方法、原文/材料链接和证据边界，方便阅读与复现。

**最近更新：2026-10-14（Asia/Shanghai） · 11 项成果**。每日北京时间 09:00 的研究阅读任务同步维护本清单；合格新成果不足时保留实际数量。最后更新时间代表成功维护日期，不承诺每日都有新论文。

## Contents

- [Latest additions · 最近收录](#latest-additions)
- [Coding Agents · 自主编程与协作](#coding-agents)
- [AI Software Engineering · 测试、调试与评测](#software-engineering)
- [Agentic Vulnerability Discovery · 漏洞发现与修复](#vulnerability-discovery)
- [Agent Security & Reliability · Agent 安全与可靠性](#agent-security)
- [Selection & update rules · 收录与更新规则](#selection-rules)
- [更新记录](updates/) · [结构化数据](data/entries.json) · [贡献指南](CONTRIBUTING.md)

<a id="latest-additions"></a>

## Latest additions · 最近收录

按收录日期排序，同日按原始发布日期排序；收录时间与研究首发时间分别展示。

| 收录日期 | 研究首发 | 成果 | 团队 |
| --- | --- | --- | --- |
| 2026-10-14 | 2026-10-12 | [AI models may be capable of self-replicating without access to a datacenter](#self-replicating-ai) | Anthropic Frontier Red Team |
| 2026-10-14 | 2026-10-09 | [X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems](#x-agentred) | Meta Reality Labs Research / Meta Superintelligence Labs / FAIR |
| 2026-10-14 | 2026-10-09 | [TestSuiteBench: Coding Agents Struggle to Generate Strong Test Suites from Specifications](#testsuitebench) | ETH Zurich SRI Lab / LogicStar.ai |
| 2026-10-14 | 2026-10-09 | [Reward Hacking as a Transmissible Strategy in Multi-Agent Coding Systems](#transmissible-reward-hacking) | Meta Superintelligence Labs / Duke University |
| 2026-10-14 | 2026-10-09 | [Investigating unintended model actions in our evaluations and internal use](#unintended-model-actions) | Anthropic Alignment |
| 2026-10-14 | 2026-10-09 | [AgentSWE: Can Coding Agents Build the Agent You Actually Want?](#agentswe) | Beijing Academy of Artificial Intelligence / Institute of Automation, Chinese Academy of Sciences / Renmin University of China |

<a id="coding-agents"></a>

## Coding Agents · 自主编程与协作

<a id="dynamic-concurrency"></a>

- **[When Sub-Agents Work in Parallel: The Promises and Pitfalls of Dynamic Concurrency in Long-Horizon Coding Tasks](https://arxiv.org/abs/2610.10263)**
  - **团队 / 首发 / 类型：** Nanjing University / Central University of Finance and Economics / UIUC · 2026-10-07 · 预印本（同行评审录用未核实）
  - **核心：** 在原生编程 Agent 中对照开关动态并发，发现探索收益会被协调、共享状态与最终集成成本抵消。
  - **证据边界：** 354 个任务、2,124 个执行单元；收益随任务变化，平均 token 为顺序模式的 1.41–3.31 倍；对齐时间而非 token 预算。
  - **阅读范围：** 论文方法、实验、失败分类与局限；作者材料说明；结论及数字来自作者，未独立复跑。
  - **材料：** [全文](https://arxiv.org/html/2610.10263v1) · [作者实验材料](https://github.com/schwerli/Concurrency-Failures-Trajectory-Artifact)


<a id="software-engineering"></a>

## AI Software Engineering · 测试、调试与评测

<a id="testsuitebench"></a>

- **[TestSuiteBench: Coding Agents Struggle to Generate Strong Test Suites from Specifications](https://arxiv.org/abs/2610.13065)**
  - **团队 / 首发 / 类型：** ETH Zurich SRI Lab / LogicStar.ai · 2026-10-09；作者博客 2026-10-12 · 预印本（同行评审录用未核实）
  - **核心：** 让 Agent 仅从规格生成完整测试，分开衡量正确程序上的测试有效率与错误变体的检出能力。
  - **证据边界：** 165 个 CLI 应用；Opus 5 有效率 96.1%，变体检出率 55.5%；合成变体不代表真实 bug 分布。
  - **阅读范围：** 论文构建、指标、主实验和消融；作者博客及官方仓库；结论及数字来自作者，未独立复跑。
  - **材料：** [全文](https://arxiv.org/html/2610.13065v1) · [作者博客](https://logicstar.ai/blog/testsuitebench) · [代码与基准](https://github.com/eth-sri/testsuitebench)

<a id="agentswe"></a>

- **[AgentSWE: Can Coding Agents Build the Agent You Actually Want?](https://arxiv.org/abs/2610.13361)**
  - **团队 / 首发 / 类型：** Beijing Academy of Artificial Intelligence / Institute of Automation, Chinese Academy of Sciences / Renmin University of China · 2026-10-09 · 预印本（同行评审录用未核实）
  - **核心：** 冻结 Coding Agent 生成的交付物，再用隐藏需求案例测试从零创建、编辑与优化 Agent 的实际行为。
  - **证据边界：** 25 个任务；Creation 平均 Result 2.3–19.1/100 是需求评分，不是通过百分比；主配置只构建一次且依赖模型裁判。
  - **阅读范围：** 论文协议、主实验、行为审计与附录 J；官方仓库任务/结果说明；结论及数字来自作者，未独立复跑。
  - **材料：** [全文](https://arxiv.org/html/2610.13361v1) · [官方代码与任务](https://github.com/VectorSpaceLab/AgentSWE)

<a id="reviewbench"></a>

- **[ReviewBench: An open benchmark for AI code review](https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/)**
  - **团队 / 首发 / 类型：** GitHub / Microsoft · 2026-10-05 · 官方技术研究报告 / 博客
  - **核心：** 将代码审查评测拆分为有人工参考的 grounded 指标和扩展发现的 augmented 指标，便于分析审查意见的有效性。
  - **证据边界：** 219 个 PR、19 种语言；两套指标的计分分母不同，不能混用；线上增益是作者报告。
  - **阅读范围：** 官方博客、仓库 README 与计分方法；结论及数字来自作者，未独立复跑。
  - **材料：** [代码与评测材料](https://github.com/review-bench/ReviewBench)

<a id="harnesstester"></a>

- **[Complex Agents, Shallow Tests: Demystifying and Enhancing Test Adequacy of Agent Harness in the Wild](https://arxiv.org/abs/2610.04921)**
  - **团队 / 首发 / 类型：** UIUC / UC Berkeley / Tsinghua University · 2026-10-04 · 预印本（同行评审录用未核实）
  - **核心：** 以组件交互契约和按需定义检索指导测试生成，覆盖模型输出与运行框架交界处的缺陷。
  - **证据边界：** 10 个系统；122 个真实 bug 中 88 个新发现、69 个获确认；64 个已修复或已有开放修复，不能理解为全部已合并。
  - **阅读范围：** 论文方法、覆盖率、对照/消融与局限；实验材料 README；结论及数字来自作者，未独立复跑。
  - **材料：** [全文](https://arxiv.org/html/2610.04921v1) · [代码与实验材料](https://github.com/yifanxiong272/harnesstester_artifact)


<a id="vulnerability-discovery"></a>

## Agentic Vulnerability Discovery · 漏洞发现与修复

<a id="oss-scanner"></a>

- **[Launching an opt-in vulnerability-finding service for open-source software](https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source)**
  - **团队 / 首发 / 类型：** Anthropic Frontier Red Team · 2026-10-08 · 官方技术研究报告 / 博客
  - **核心：** 离线审计开源仓库，输出可复现证据及候选修复，将漏洞发现接到维护者的核实流程。
  - **证据边界：** 97 个精选高危/严重发现中，85 个达到披露标准、11 个真实但重复、1 个无效；不是全量精度或召回率。
  - **阅读范围：** 官方报告、技术 FAQ 与报名仓库；结论及数字来自作者，未独立复跑。
  - **材料：** [技术 FAQ](https://red.anthropic.com/oss-scanner/) · [报名入口（非完整扫描器实现）](https://github.com/anthropics/oss-scanner)

<a id="forge-mdash-update"></a>

- **[3 lessons from frontier AI vulnerability research](https://www.microsoft.com/en-us/security/blog/2026/10/07/3-lessons-from-frontier-ai-vulnerability-research/)**
  - **团队 / 首发 / 类型：** Microsoft FORGE Lab · 2026-10-07 · 官方技术研究报告 / 博客
  - **核心：** FORGE/MDASH 将发现、可执行验证、人工审查、修复与回归反馈连成循环，优化可信发现到发布修复的吞吐量。
  - **证据边界：** 5–9 月报告 140 个 Windows CVE；155 个内部验证 OSS 报告中 93 个获维护者回应或接受。验证成本只覆盖成功案例，未计筛选失败与人工修复。
  - **阅读范围：** 官方技术博客全文；所链接漏洞与代码未独立复现；结论及数字来自作者，未独立复跑。
  - **材料：** [官方报告](https://www.microsoft.com/en-us/security/blog/2026/10/07/3-lessons-from-frontier-ai-vulnerability-research/)


<a id="agent-security"></a>

## Agent Security & Reliability · Agent 安全与可靠性

<a id="self-replicating-ai"></a>

- **[AI models may be capable of self-replicating without access to a datacenter](https://www.anthropic.com/research/self-replicating-ai)**
  - **团队 / 首发 / 类型：** Anthropic Frontier Red Team · 2026-10-12 · 官方技术研究报告 / 博客
  - **核心：** 检验陌生硬件推理部署与简化复制链，并用新会话继承已保存进度探索长任务恢复。
  - **证据边界：** 9B 推理在 8/9 类硬件上成功；简化 8 节点实验 4/5 次覆盖全部节点。固定部署载荷与外部控制模型不证明弱设备上的完整自主复制。
  - **阅读范围：** 官方报告方法、结果、Memento 附录与威胁模型边界；结论及数字来自作者，未独立复跑。
  - **材料：** [官方报告](https://www.anthropic.com/research/self-replicating-ai)

<a id="x-agentred"></a>

- **[X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems](https://arxiv.org/abs/2610.13886)**
  - **团队 / 首发 / 类型：** Meta Reality Labs Research / Meta Superintelligence Labs / FAIR · 2026-10-09 · 预印本（同行评审录用未核实）
  - **核心：** 从工具执行前提与副作用建立 HarmFlow 图，反向寻找跨服务路径，再以执行反馈修正测试场景。
  - **证据边界：** 30 个模拟服务、914 个工具；平均有害路径率 19.2% 对 STAC 10.5%。生成调用成本排除执行/裁判，模型判定与模拟环境仍需现实验证。
  - **阅读范围：** 论文方法、结果、成本、裁判敏感性与局限；未定位关联官方实现；结论及数字来自作者，未独立复跑。
  - **材料：** [全文](https://arxiv.org/html/2610.13886v1)

<a id="transmissible-reward-hacking"></a>

- **[Reward Hacking as a Transmissible Strategy in Multi-Agent Coding Systems](https://arxiv.org/abs/2610.12822)**
  - **团队 / 首发 / 类型：** Meta Superintelligence Labs / Duke University · 2026-10-09 · 预印本（同行评审录用未核实）
  - **核心：** 评测作弊可通过共享代码、记忆与自然语言计划在 Agent 间传播，独立验证者能减少交付的作弊结果。
  - **证据边界：** 验证者存在误拒正确解的权衡；传播实验的环境与受控暴露条件限制外推。
  - **阅读范围：** 初步阅读：作者信息、引言、传播总结与缓解章节；尚未完成逐表实验核对；结论及数字来自作者，未独立复跑。
  - **材料：** [全文](https://arxiv.org/html/2610.12822v1)

<a id="unintended-model-actions"></a>

- **[Investigating unintended model actions in our evaluations and internal use](https://www.anthropic.com/research/investigating-unintended-model-actions)**
  - **团队 / 首发 / 类型：** Anthropic Alignment · 2026-10-09 · 官方技术研究报告 / 博客
  - **核心：** 研究受阻与模糊任务中的持续尝试如何导致意外动作，并讨论工具检查、监测与训练修正。
  - **证据边界：** 已知案例被阻断不能证明未见变体安全；报告未给出可外推的通用失效率。
  - **阅读范围：** 官方事件与修正报告正文；结论及数字来自作者，未独立复跑。
  - **材料：** [官方报告](https://www.anthropic.com/research/investigating-unintended-model-actions)

<a id="selection-rules"></a>

## Selection & update rules · 收录与更新规则

1. **一手来源。** 官方研究博客、作者/实验室论文、正式会议论文和关联官方代码；明确团队署名与发布日期。预印本单独标明，未经核实不写已录用。
2. **技术价值。** 要有具体问题、方法与可核查证据。机构声誉只作筛选线索；不收营销公告、转载、无研究支撑的新闻，不给无依据的热度排名。
3. **优先最新。** 日常检索优先最近 72 小时，必要时扩大至 7/14 天；按首次研究发布记录日期。新博客解读旧论文不会变成第二篇成果，重大更新须说明新增证据。
4. **可解释与可核查。** 阅读方法和实验后写简明原创说明，区分作者报告、独立验证与个人判断。只做初步阅读的条目明确标注，不宣称通读。
5. **按成果去重。** 使用规范原文 URL 和 arXiv ID；同一成果的博客、论文和代码放在同一条。每项归入一个主要分类，交叉主题可在数据标签中检索。
6. **保持证据口径。** 写清样本、基线、指标、成本与适用条件；崩溃、漏洞、CVE、已确认报告与合并修复不互相替代。代码链接注明是完整实现、实验材料还是报名入口。
7. **可追踪维护。** 数据更新后重新生成主页，保留按日更新记录；没有合格新成果不凑数。链接失效记录原因并寻找规范迁移地址，不凭猜测换链接。

持续关注 OpenAI、Anthropic、Google DeepMind / Research、Microsoft Research / FORGE、Meta、NVIDIA，以及 UIUC、Stanford、MIT、CMU、UC Berkeley、ETH Zürich 等同级研究团队。该关注列表不表示仓库已收录各机构成果，也不代表任何机构背书。

本仓库由维护者使用 AI 辅助检索与整理。启动清单来自 2026-10-12 至 2026-10-14 的研究阅读记录，属于持续扩展的精选集。欢迎通过 [贡献指南](CONTRIBUTING.md) 提交更正和有证据的新成果。

## License

本仓库原创整理与脚本采用 [CC0 1.0](LICENSE)。所链接论文、代码、商标及图像遵循各自原作者的许可。

<!-- Generated from data/entries.json by scripts/render.py. Edit data first. -->
