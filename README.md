<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img src="assets/hero-light.svg" alt="Awesome Agentic Software Engineering — Code · Build · Secure" width="100%">
</picture>

<p align="center">
  <a href="https://github.com/sindresorhus/awesome"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <a href="data/entries.json"><img src="https://img.shields.io/badge/papers_%26_blogs-11-6366f1?style=flat-square" alt="Papers and blogs: 11"></a>
  <a href="updates/"><img src="https://img.shields.io/badge/updated-2026--10--14-14b8a6?style=flat-square" alt="Updated: 2026-10-14"></a>
</p>

<table width="100%">
  <tr>
    <td width="50%"><a href="#coding-agents"><b>01 · Coding Agents</b></a><br><sub>1 entry</sub></td>
    <td width="50%"><a href="#software-engineering"><b>02 · AI Software Engineering</b></a><br><sub>4 entries</sub></td>
  </tr>
  <tr>
    <td width="50%"><a href="#vulnerability-discovery"><b>03 · Vulnerability Discovery</b></a><br><sub>2 entries</sub></td>
    <td width="50%"><a href="#agent-security"><b>04 · Agent Security</b></a><br><sub>4 entries</sub></td>
  </tr>
</table>

<a id="coding-agents"></a>

## 01 · Coding Agents

<table width="100%">
  <thead><tr><th width="17%">Date · Org</th><th width="73%">Research</th><th width="10%" align="center">Links</th></tr></thead>
  <tbody>
    <tr><td valign="top"><code>2026-10-07</code><br><sub>Nanjing University</sub></td><td><b><a href="https://arxiv.org/abs/2610.10263" title="When Sub-Agents Work in Parallel: The Promises and Pitfalls of Dynamic Concurrency in Long-Horizon Coding Tasks">When Sub-Agents Work in Parallel</a></b><br>对照编程 Agent 的串行与并发执行，揭示协作收益、协调失败与资源代价。</td><td align="center"><a href="https://github.com/schwerli/Concurrency-Failures-Trajectory-Artifact">Artifacts</a></td></tr>
  </tbody>
</table>


<a id="software-engineering"></a>

## 02 · AI Software Engineering

<table width="100%">
  <thead><tr><th width="17%">Date · Org</th><th width="73%">Research</th><th width="10%" align="center">Links</th></tr></thead>
  <tbody>
    <tr><td valign="top"><code>2026-10-09</code><br><sub>ETH Zürich</sub></td><td><b><a href="https://arxiv.org/abs/2610.13065" title="TestSuiteBench: Coding Agents Struggle to Generate Strong Test Suites from Specifications">TestSuiteBench</a></b><br>评测 Agent 从需求生成完整测试套件的能力，区分测试有效性与错误检出能力。</td><td align="center"><a href="https://logicstar.ai/blog/testsuitebench">Blog</a><br><a href="https://github.com/eth-sri/testsuitebench">Code</a></td></tr>
    <tr><td valign="top"><code>2026-10-09</code><br><sub>BAAI</sub></td><td><b><a href="https://arxiv.org/abs/2610.13361" title="AgentSWE: Can Coding Agents Build the Agent You Actually Want?">AgentSWE</a></b><br>用隐藏需求案例验收 Coding Agent 创建、修改和优化的 Agent 交付物。</td><td align="center"><a href="https://github.com/VectorSpaceLab/AgentSWE">Code</a></td></tr>
    <tr><td valign="top"><code>2026-10-05</code><br><sub>GitHub</sub></td><td><b><a href="https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/" title="ReviewBench: An open benchmark for AI code review">ReviewBench</a></b><br>构建真实 PR 的代码审查基准，评估 Agent 发现问题的准确性与覆盖能力。</td><td align="center"><a href="https://github.com/review-bench/ReviewBench">Code</a></td></tr>
    <tr><td valign="top"><code>2026-10-04</code><br><sub>UIUC</sub></td><td><b><a href="https://arxiv.org/abs/2610.04921" title="Complex Agents, Shallow Tests: Demystifying and Enhancing Test Adequacy of Agent Harness in the Wild">HarnessTester</a></b><br>依据组件交互契约生成测试，发现 Agent 运行框架中的隐藏缺陷。</td><td align="center"><a href="https://github.com/yifanxiong272/harnesstester_artifact">Artifacts</a></td></tr>
  </tbody>
</table>


<a id="vulnerability-discovery"></a>

## 03 · Vulnerability Discovery

<table width="100%">
  <thead><tr><th width="17%">Date · Org</th><th width="73%">Research</th><th width="10%" align="center">Links</th></tr></thead>
  <tbody>
    <tr><td valign="top"><code>2026-10-08</code><br><sub>Anthropic</sub></td><td><b><a href="https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source" title="Launching an opt-in vulnerability-finding service for open-source software">OSS Scanner</a></b><br>离线审计开源仓库，生成漏洞复现证据和候选修复方案。</td><td align="center">—</td></tr>
    <tr><td valign="top"><code>2026-10-07</code><br><sub>Microsoft</sub></td><td><b><a href="https://www.microsoft.com/en-us/security/blog/2026/10/07/3-lessons-from-frontier-ai-vulnerability-research/" title="3 lessons from frontier AI vulnerability research">FORGE / MDASH</a></b><br>将漏洞发现、可执行验证与修复反馈串成闭环，提升安全研究的有效产出。</td><td align="center">—</td></tr>
  </tbody>
</table>


<a id="agent-security"></a>

## 04 · Agent Security

<table width="100%">
  <thead><tr><th width="17%">Date · Org</th><th width="73%">Research</th><th width="10%" align="center">Links</th></tr></thead>
  <tbody>
    <tr><td valign="top"><code>2026-10-12</code><br><sub>Anthropic</sub></td><td><b><a href="https://www.anthropic.com/research/self-replicating-ai" title="AI models may be capable of self-replicating without access to a datacenter">Self-Replicating AI</a></b><br>在陌生硬件与简化集群中测试模型部署、复制和长任务恢复能力。</td><td align="center">—</td></tr>
    <tr><td valign="top"><code>2026-10-09</code><br><sub>Meta Reality Labs Research</sub></td><td><b><a href="https://arxiv.org/abs/2610.13886" title="X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems">X-AgentRed</a></b><br>利用工具依赖图与执行反馈，发现跨服务组合导致的 Agent 安全失效。</td><td align="center">—</td></tr>
    <tr><td valign="top"><code>2026-10-09</code><br><sub>Meta Superintelligence Labs</sub></td><td><b><a href="https://arxiv.org/abs/2610.12822" title="Reward Hacking as a Transmissible Strategy in Multi-Agent Coding Systems">Transmissible Reward Hacking</a></b><br>研究评测作弊如何通过代码、记忆和计划在多 Agent 系统中传播。</td><td align="center">—</td></tr>
    <tr><td valign="top"><code>2026-10-09</code><br><sub>Anthropic</sub></td><td><b><a href="https://www.anthropic.com/research/investigating-unintended-model-actions" title="Investigating unintended model actions in our evaluations and internal use">Unintended Model Actions</a></b><br>分析 Agent 在受阻任务中采取意外动作的原因，并评估防护措施。</td><td align="center">—</td></tr>
  </tbody>
</table>

---

<p align="center">
  <a href="updates/">Changelog</a> &nbsp;·&nbsp;
  <a href="CONTRIBUTING.md">Contribute</a> &nbsp;·&nbsp;
  <a href="LICENSE">CC0 1.0</a>
</p>

<!-- Generated from data/entries.json by scripts/render.py. -->
