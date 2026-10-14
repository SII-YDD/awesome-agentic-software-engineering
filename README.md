<h1 align="center">Awesome Agentic Software Engineering</h1>

<p align="center">Coding Agents · AI Software Engineering · Agent Security</p>

<p align="center">
  <a href="https://github.com/sindresorhus/awesome"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <a href="data/entries.json"><img src="https://img.shields.io/badge/papers_%26_blogs-11-6366f1?style=flat-square" alt="Papers and blogs: 11"></a>
  <a href="updates/"><img src="https://img.shields.io/badge/updated-2026--10--14-14b8a6?style=flat-square" alt="Updated: 2026-10-14"></a>
</p>

<p align="center">
  <a href="#coding-agents">Coding Agents</a> &nbsp;·&nbsp;
  <a href="#software-engineering">Software Engineering</a> &nbsp;·&nbsp;
  <a href="#vulnerability-discovery">Vulnerability Discovery</a> &nbsp;·&nbsp;
  <a href="#agent-security">Agent Security</a>
</p>

<a id="coding-agents"></a>

## Coding Agents

- **[When Sub-Agents Work in Parallel: The Promises and Pitfalls of Dynamic Concurrency in Long-Horizon Coding Tasks](https://arxiv.org/abs/2610.10263)** · `2026-10-07` · Nanjing University · [Artifacts](https://github.com/schwerli/Concurrency-Failures-Trajectory-Artifact)<br>对照编程 Agent 的串行与并发执行，揭示协作收益、协调失败与资源代价。


<a id="software-engineering"></a>

## AI Software Engineering

- **[TestSuiteBench: Coding Agents Struggle to Generate Strong Test Suites from Specifications](https://arxiv.org/abs/2610.13065)** · `2026-10-09` · ETH Zürich · [Blog](https://logicstar.ai/blog/testsuitebench) · [Code](https://github.com/eth-sri/testsuitebench)<br>评测 Agent 从需求生成完整测试套件的能力，区分测试有效性与错误检出能力。

- **[AgentSWE: Can Coding Agents Build the Agent You Actually Want?](https://arxiv.org/abs/2610.13361)** · `2026-10-09` · BAAI · [Code](https://github.com/VectorSpaceLab/AgentSWE)<br>用隐藏需求案例验收 Coding Agent 创建、修改和优化的 Agent 交付物。

- **[ReviewBench: An open benchmark for AI code review](https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/)** · `2026-10-05` · GitHub · [Code](https://github.com/review-bench/ReviewBench)<br>构建真实 PR 的代码审查基准，评估 Agent 发现问题的准确性与覆盖能力。

- **[Complex Agents, Shallow Tests: Demystifying and Enhancing Test Adequacy of Agent Harness in the Wild](https://arxiv.org/abs/2610.04921)** · `2026-10-04` · UIUC · [Artifacts](https://github.com/yifanxiong272/harnesstester_artifact)<br>依据组件交互契约生成测试，发现 Agent 运行框架中的隐藏缺陷。


<a id="vulnerability-discovery"></a>

## Vulnerability Discovery

- **[Launching an opt-in vulnerability-finding service for open-source software](https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source)** · `2026-10-08` · Anthropic<br>离线审计开源仓库，生成漏洞复现证据和候选修复方案。

- **[3 lessons from frontier AI vulnerability research](https://www.microsoft.com/en-us/security/blog/2026/10/07/3-lessons-from-frontier-ai-vulnerability-research/)** · `2026-10-07` · Microsoft<br>将漏洞发现、可执行验证与修复反馈串成闭环，提升安全研究的有效产出。


<a id="agent-security"></a>

## Agent Security

- **[AI models may be capable of self-replicating without access to a datacenter](https://www.anthropic.com/research/self-replicating-ai)** · `2026-10-12` · Anthropic<br>在陌生硬件与简化集群中测试模型部署、复制和长任务恢复能力。

- **[X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems](https://arxiv.org/abs/2610.13886)** · `2026-10-09` · Meta Reality Labs Research<br>利用工具依赖图与执行反馈，发现跨服务组合导致的 Agent 安全失效。

- **[Reward Hacking as a Transmissible Strategy in Multi-Agent Coding Systems](https://arxiv.org/abs/2610.12822)** · `2026-10-09` · Meta Superintelligence Labs<br>研究评测作弊如何通过代码、记忆和计划在多 Agent 系统中传播。

- **[Investigating unintended model actions in our evaluations and internal use](https://www.anthropic.com/research/investigating-unintended-model-actions)** · `2026-10-09` · Anthropic<br>分析 Agent 在受阻任务中采取意外动作的原因，并评估防护措施。

---

<p align="center">
  <a href="updates/">Changelog</a> &nbsp;·&nbsp;
  <a href="CONTRIBUTING.md">Contribute</a> &nbsp;·&nbsp;
  <a href="LICENSE">CC0 1.0</a>
</p>

<!-- Generated from data/entries.json by scripts/render.py. -->
