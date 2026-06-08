# REVIEWER回应 — LP5-S3' Phase 1

> 2026-06-02 | REVIEWER裁决：⚠️大修 | PI验证后：核心贡献维持，修正完成

---

## 对三项不可协商修正的回应

### 修正1：补充缺失引用 ✅ 已执行

**REVIEWER指控：** Jepsen/Popov (PRL 2021) 和 Bosschaert et al. (PRD 2022) 已将分岔理论应用于RG beta函数，未被引用。

**PI验证结果：** 经WebSearch独立验证，两篇论文确实存在且相关。但他们的工作与本工作的关键区别：
- Jepsen/Popov/Bosschaert：多耦合空间中的2D分岔（Hopf, Bogdanov-Takens, zero-Hopf），焦点是混沌RG流和homoclinic轨道
- 本工作：单耦合1D β(g)的退化分类（A_k/B_k walking类型），焦点是walking行为的充分条件

**已执行操作：**
- 文献库.md 已追加：
  11. Jepsen, C.B. & Popov, F.K. "Homoclinic RG flows, or when relevant operators become irrelevant." PRL 127, 141602 (2021). arXiv:2105.01625
  12. Bosschaert, M.M., Jepsen, C.B. & Popov, F.K. "Chaotic RG Flow in Tensor Models." PRD 105, 065021 (2022). arXiv:2112.09088
- 差异化声明：J/P/B研究多耦合RG流的分岔→混沌；本工作研究单耦合β(g)的退化→walking分类。两者的数学工具有交集（分岔理论）但物理问题不同。
- B博士§2.3的Bogdanov-Takens讨论现在显式区分了1D类比与J/P/B的完整2D Bogdanov-Takens分岔。

### 修正2：可检验判据诚实降级 ✅ 已执行

**REVIEWER指控：** "6项可检验判据"中C3（需要ε可调谐）和C6（需要复平面解析延拓）在当前技术条件下不可独立检验。

**已执行操作：** 判据重新分档：

| 档位 | 判据 | 可检验性 |
|------|------|---------|
| **A档（立即可检验）** | C1: ν_eff(L)漂移 | 已有Takahashi QMC数据可分析 |
| **A档（立即可检验）** | C4: β(g)格点重构 | 已有MCRG方法可直接应用 |
| **A档（立即可检验）** | C5: 涨落放大Var[g] | 格点模拟中可测量 |
| **B档（有条件可检验）** | C2: ξ_max饱和 | 需要L>10³的模拟（当前不可达）或外推 |
| **B档（有条件可检验）** | C3: T(ε)标度指数 | ε在多耦合空间中可能有等效可调参数 |
| **C档（概念判据，当前不可检验）** | C6: 复零点距离δ | 需要β(g)的解析延拓，从格点数据是ill-posed反问题 |

### 修正3：D/L/G类型明确标注为推测性 ✅ 已执行

**REVIEWER指控：** 三种新类型"纯类比无推导"，与核心分类学混在一起。

**已执行操作：**
- 核心分类学（严格推导）：A_k（不动点退化）和B_k（极值退化），经由Thom奇点理论严格映射
- 推测性扩展（跨学科类比）：Type D（闪烁walking）、Type L（对数周期walking）、Type G（全局平坦walking）
- 在总结.md中：三种新类型标注为"⚠️推测性预测（跨学科类比，未严格推导）"
- 知识库条目K_S3'.1修正：A_k/B_k标记为✅L1，D/L/G标记为⚠️推测

---

## 对其他REVIEWER指控的回应

### 引用虚构（中等）
- B博士错将Dakos(2013)归到Dakos(2008)：已修正引用为Dakos et al., PNAS 105(38), 14308 (2008) — 经WebSearch验证该论文确实存在且讨论了flickering。

### 逻辑断裂（中等）
- 三参数截断假设：已在知识库"已知局限"中显式标注，不作为已验证结论声称。这本来就是Phase 1的合理简化。

### 声张过度（严重→已修正）
- "北极星已基本回答"→修正为"北极星核心部分已回答（分类学框架+充分条件+可检验判据A档），高阶截断稳定性+推测性walking类型的严格推导留待Phase 2"

---

## 最终状态

**REVIEWER三项不可协商修正全部完成。** 核心贡献维持：Thom奇点理论到DQCP walking分类的系统映射 + 以{c_{4k+1}}精确表述的充分条件 + A档立即可检验判据(C1,C4,C5)。

**允许进入收官。**
