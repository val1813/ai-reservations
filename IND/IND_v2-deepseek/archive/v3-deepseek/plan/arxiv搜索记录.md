# arXiv搜索记录 — v3-deepseek

> Phase 0 初始化搜索（2026-05-29）

## 竞争者搜索（全面，新课题初始化）

### 搜索1：核心概念精确搜索
**关键词**：`quantum thermodynamics strong coupling entropy production sign freedom cumulant expansion 2025 2026`
**来源**：WebSearch
**结果**：
- Rahbar & Stein (2025, arXiv:2505.00188): HMF框架+T>0下的Jensen不等式+方差条件。最接近本课题——用HMF的cumulant展开推导自由能不等式。**差异**：他们关注HMF定义下的自由能/内能的概率表示，不涉及ρ̇_S符号自由度分析，也未追踪κ₂对角性到κ₄符号的失效传递。
- Pathania et al. (2024, arXiv:2407.21584): HMF+熵产生+两qubit+JC模型。**差异**：计算具体模型而非代数结构，不分析cumulant展开的对角性/非对易性。
- **判断**：无直接竞争 ✓

### 搜索2：方法论精确搜索
**关键词**：`"entropy production" "sign" "lower bound" impossibility quantum thermodynamics 2025 2026`
**来源**：WebSearch
**结果**：
- Honma & Vu (2025, arXiv:2510.04866): 量子TKUR，多体系统负局部熵产生通过信息流补偿。**差异**：关注精度-耗散trade-off，不是κ₂对角子空间结构。
- Pernambuco & Céleri (2026, arXiv:2602.06716): 规范不变熵产生+涨落定理。**差异**：几何框架，关注信息约束而非代数结构，互补但非竞争。
- **判断**：无直接竞争 ✓

### 搜索3：否定性/反例搜索
**关键词组1**：`"Jensen inequality" "entropy production lower bound" "strong coupling" limitation counterexample`
**结果**：Jensen bound for entropy production rate in stochastic thermodynamics (2023)——经典随机热力学，非量子。**判断**：不影响本课题。

**关键词组2**：`"no-go theorem" "strong coupling" "second law" "quantum thermodynamics" limitation 2025`
**结果**：
- Hokkyo et al. (PRL 2025): ETH禁止能量本征态功提取——是关于量子热化的no-go，非关于强耦合熵产生。**判断**：领域相邻但不竞争。
- Xu (Physica A 2025): 强耦合下热力学定律成立+效率降低——**结论方向相反**（Xu说强耦合下定律仍成立，本课题从K24说负方向路径被排除了）。**差异**：Xu关注Carnot引擎效率，不涉及HMF cumulant展开的代数对角性。**判断**：不竞争，但应记入文献库作为不同视角的参照。

**关键词组3**：`"entropy production" "lower bound" impossibility quantum thermodynamics 2025 2026`
**结果**：Gu (2026, arXiv:2601.04039) — WTD bound vs TUR bound无通用排序，反例存在。**判断**：经典随机热力学结论，不涉及量子同调代数结构。不影响本课题。

## 结论
**赛道有效** ✓ — 未发现直接竞争。
- 最接近的工作（Rahbar & Stein 2025）关注HMF的概率表示而非κ₂对角子空间的代数结构
- 跨版本悬留问题中记录的K13→K24失效传递问题未被任何竞争者正面分析
- 2026年量子热力学社区集中在TUR/精度-耗散/涨落定理，无人从cumulant展开的代数对角性角度切入
- Xu (2025)的"强耦合下热力学定律仍成立"结论与本课题K24的否定性视角构成外部声张冲突——不自动降级K24，标记为外部声张冲突，交由后续审稿人处理
