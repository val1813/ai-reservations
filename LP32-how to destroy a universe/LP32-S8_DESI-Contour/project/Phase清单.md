# LP32-S8 Phase清单 — DESI DR2 Contour Comparison

**课题:** DGF w₀-w_a 预测与 DESI DR2 完整等高线对比
**北极星:** ¬H: DGF对(w₀,w_a)的预测不仅与DESI DR2最佳拟合一致(Δχ²=-15.5≈3.9σ)，而且完整理论等高线与DESI DR2的观测等高线在形状、方向、紧缩度上匹配
**父项目:** LP32 DGF框架
**创建日期:** 2026-06-08
**贡献者:** 匿名

---

## Phase 0: 奠基 (GATE -1 → GATE 0)

| # | 任务 | 状态 | 产出 |
|---|------|:--:|------|
| 0.1 | DESI DR2协方差矩阵精确提取 | ⬜ | Σ矩阵+等高线数据 |
| 0.2 | DGF telegraph+Friedmann自洽方程定稿 | ⬜ | 方程体系(含n参数) |
| 0.3 | GATE -1: 核心矛盾结构验证 | ⬜ | 矛盾对列表 |
| 0.4 | 先发拦截(R1文献搜索) | ⬜ | 竞争者清单 |

## Phase 1: 数值实现 (GATE 0 → GATE 1)

| # | 任务 | 状态 | 产出 |
|---|------|:--:|------|
| 1.1 | 自洽DGF+Friedmann RK4求解器 | ⬜ | Python solver |
| 1.2 | (η/γ₀, n)参数空间扫描 | ⬜ | 参数网格×w(z) |
| 1.3 | CPL投影(w₀, w_a)计算 | ⬜ | 投影映射 |
| 1.4 | χ²(w₀,w_a)等高线生成 | ⬜ | Δχ²网格 |
| 1.5 | 与DESI DR2观测等高线叠加对比 | ⬜ | 对比图 |
| 1.6 | SFR不确定性传播 | ⬜ | 理论误差棒 |

## Phase 2: AB博士独立推导 (GATE 1 → GATE 1.5)

| # | 任务 | 状态 | 产出 |
|---|------|:--:|------|
| 2.1 | A博士: telegraph方程严格推导 | ⬜ | A_round1.md |
| 2.2 | B博士: 跨学科交叉验证 | ⬜ | B_round1.md |
| 2.3 | PI综合 | ⬜ | PI_synthesis_R1.md |
| 2.4 | 最低3轮AB迭代 | ⬜ | R1-R3 |

## Phase 3: 验证与攻击 (GATE 1.5 → GATE 2)

| # | 任务 | 状态 | 产出 |
|---|------|:--:|------|
| 3.1 | 自我攻击: n敏感性分析 | ⬜ | n∈[0.5,2.0]扫描 |
| 3.2 | 自我攻击: SFR不确定性影响 | ⬜ | Madau+Driver误差 |
| 3.3 | 自我攻击: 记忆修正量级 | ⬜ | R₀边界 |
| 3.4 | 自我攻击: CPL投影偏差 | ⬜ | 非参数w(z)直接对比 |
| 3.5 | 与竞争者定量对比 | ⬜ | QMM/Quintessence/CreSS |
| 3.6 | INSPECTOR审查 | ⬜ | inspector_report.md |

## Phase 4: 论文准备 (GATE 2 → GATE 3)

| # | 任务 | 状态 | 产出 |
|---|------|:--:|------|
| 4.1 | 主图: DGF vs DESI DR2等高线 | ⬜ | Fig1: contour overlay |
| 4.2 | 补充图: w(z)形状预测 | ⬜ | Fig2: w(z) for various n |
| 4.3 | 补充图: SFR敏感性 | ⬜ | Fig3: error band |
| 4.4 | 可证伪预言清单 | ⬜ | 预言表 |
| 4.5 | 论文草稿(Nature Physics格式) | ⬜ | main.tex |
| 4.6 | 补充材料 | ⬜ | supplement.tex |

## Phase 5: 收官 (GATE 4 → GATE 7)

| # | 任务 | 状态 | 产出 |
|---|------|:--:|------|
| 5.1 | 知识库汇总 | ⬜ | knowledge_base.md |
| 5.2 | 知识图谱备份 | ⬜ | knowledge_graph.json |
| 5.3 | 诚实局限清单 | ⬜ | limitations.md |
| 5.4 | 最终结案报告 | ⬜ | FINAL_CLOSURE.md |

---

## 北极星优先级矩阵

| # | 北极星 | Score | 依赖 |
|---|--------|:-----:|------|
| **N1** | DGF (w₀,w_a)等高线与DESI DR2在1σ内重叠 | 9.5 | Phase 1-3 |
| N2 | n=1自然基准的数据驱动确认 | 8.5 | Phase 1 |
| N3 | w(z)非单调峰结构的模型独立检验方案 | 8.0 | Phase 3 |
| N4 | 可投Nature Physics的完整论文包 | 9.0 | Phase 4-5 |
