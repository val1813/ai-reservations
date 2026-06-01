# A博士 Phase 1 作业：Hawking-Encoding M.B 判据

> 课题：Hawking-Encoding v1（LP6-S3）
> Phase：1（首轮正面构造）
> 角色：A博士（正规军，独立子agent，零项目上下文）
> 日期：2026-06-01

---

## ⚡ PI审核入口

- **M.B 判据选择**：(b) 相对熵判据（按任务建议）
- **M.B 在 SYK/JT+bath 中是否满足**：**有边界**——结论严重依赖于"A_bdy 是否包含 bath"这个定义选择
  - 若 A_bdy = SYK 单迹 + H_bdy（任务字面定义，**不含 bath**）：M.B 平凡满足，Δ_M.B = O(1)，但答案没价值
  - 若 A_bdy = 全部渐近边界数据（SYK 单迹 + bath 单迹）：M.B 在 eternal 设置下**最可能不满足**，Δ_M.B = 0（最多 e^{−S_BH} 量级）
- **Δ_M.B 量级**：O(1)（窄定义） / 0 或 e^{−S_BH}（宽定义）
- **关键技术步骤**：post-Page 阶段，infallen qubit 信息按 PSSY 已转移到 radiation/bath；窄 A_bdy 看不见，岛公式用 island operator 直接读出，故 Δ 大；宽 A_bdy 已含 bath，由 entanglement wedge reconstruction 等价
- **最脆弱假设**：任务的 A_bdy 定义是否合法地把 bath 排除在外——这一定义把 M.B 的"非平凡性"问题悄悄改写成了"任务设定的子算符是否够用"的问题
- **PI需关注**：
  1. 任务"§5 后者严格小→M.B 满足"与 von Neumann 代数单调性方向相反，疑为笔误
  2. ACMP compact 算符论据要求"无 background isometry"，eternal AEMM 设置具 Killing 时间，论据不直接适用
  3. 任务命题 B（trivializing alternative）对应 GKRR completeness，若取宽 A_bdy 它将赢 Phase 1

---

## §0 声张强度声明（不得后改）

任务书目标结论：M.B 在 SYK/JT + bath 标准设置下被满足。

声张强度：☑ **有条件成立**，条件抄录如下（自任务书）：
- "标准设置" = AEMM 2019 双侧 eternal AdS₂ + JT + 左侧非引力 bath
- "boundary algebra" = SYK 单迹算符 O_i + boundary Hamiltonian
- "island reconstruction" = post-Page time, A_island = A_bdy ∨ {island compactly supported gauge-invariant operators}
- "精确模拟" = 算符 norm 判据 ε(N) → 0；本作业用相对熵判据 (b)，等价条件 Δ_M.B = 0

## §0.5 隐含假设清单

| # | 引用 | 原文条件 | 当前是否满足 |
|---|---|---|---|
| 1 | CPW 2209.10454 | 半经典 G→0、microcanonical、boundary Type III 交叉积 | ✓ |
| 2 | PSSY 1911.11977 | 半经典 + replica + JT 鞍点稳定 | ✓ |
| 3 | ACMP 2506.04311 | "**no isometries of the background spacetime**" | **✗ eternal AdS₂ 有 Killing 时间** |
| 4 | GKRR 2602.06543 | "algebra of observables at infinity is complete" | 待核 |
| 5 | JLMS 相对熵公式 | 半经典、bulk 算符在 entanglement wedge | ✓ |
| 6 | 任务 A_bdy 不含 bath | 任务设定 | ✓（按字面） |

**最关键 #6**：bath 是否属于 boundary 是任务设计选择。AEMM/PSSY 文献中通常 bath ⊂ boundary（非引力 QFT 渐近数据）。

## §1 结论预测

- **符号方向**：Δ_M.B ≥ 0（代数单调性必非负）
- **量级**（窄 A_bdy）：S_rel|A_bdy ~ e^{−S_BH/2}（typical state，待核）；S_rel|A_island ~ O(1) → Δ = O(1)
- **量级**（宽 A_bdy）：entanglement wedge reconstruction 给出精确同构 → Δ = 0
- **最易出错的步骤**：post-Page 但 thermalization time 未到时 typical state 估计不适用

## §2 强制撞墙

**反例 1**：t = 0 立即测量（pre-Page）。期望 Δ = 0；检验：pre-Page A_island = A_bdy（island 不出现）✓
**反例 2**：ω₁ 为 bath 侧加 qubit。两边都看不见 → Δ = 0
- 暴露弱点：M.B 满足与否对态选择敏感，单一态不能给出 algebra-level 强声张

## §3 判据精化（修正任务§5 笔误）

**Petz 单调性**：N ⊆ M von Neumann 代数 → S(ω∥ω₀)|_M ≥ S(ω∥ω₀)|_N

故若 A_island ⊋ A_bdy，则 S_rel|A_island ≥ S_rel|A_bdy。
**Δ_M.B := S(ω₁∥ω₀)|_A_island − S(ω₁∥ω₀)|_A_bdy ≥ 0**
M.B nontrivial ⟺ 存在态使 Δ_M.B > 0 严格。

任务§5 "后者严格小→M.B 满足" 疑为笔误，PI 请确认。

## §4 SYK/JT + bath 中的代数显式构造

**A_bdy（窄）**：右 SYK 单迹 {O_i^R(t)} + H_R。不含 bath、不含左 SYK。
类型：N→∞ 后 single-trace algebra 是 Type III₁（Leutheusser-Liu），加 H_R 做交叉积 → Type II_∞。

**A_island**：A_bdy ∨ {island region I 内 gauge-invariant compactly supported bulk fields}
post-Page 时 I 在左 horizon 内侧。"gauge-invariant" 在 JT 中需 dressing 到右 boundary 时间或 ADM 能量。

**关键发现**：eternal AdS₂ 有 Killing 时间 ξ = ∂_t → ACMP "无 isometry" 前提**不成立**。任务§"建议引用 ACMP 支持 M.B 满足"不能直接执行。

可用变体：(i) 一侧 collapse → ACMP 可能适用，待核；(ii) dress 到 bath 时间 → 模糊 A_bdy/A_bath 边界。本作业承认 island 算符通过 *non-compact* boundary-time dressing 构造。

## §5 ω₀, ω₁ 与相对熵计算

**态**：ω₀ = TFD；ω₁ = U_qubit|TFD⟩，t_inj < 0 且 |t_inj| > t_Page 使信息已部分外泄

**计算 1：S(ω₁∥ω₀)|_A_bdy^R（窄）**

post-Page + Hayden-Preskill scrambling → typical state 论据：
S(ω₁∥ω₀)|_A_bdy^R ≲ O(e^{−S_BH/2})

**计算 2：S(ω₁∥ω₀)|_A_island**

A_island 含 island 内 bulk field φ(x_qubit) → 直接局域可分辨度 O(1)：
S(ω₁∥ω₀)|_A_island ≈ S_bulk_semiclassical = O(1) ~ log 2

**Δ_M.B = O(1) − O(e^{−S/2}) = O(1)**（窄 A_bdy）

## §6 ACMP 2025 在 eternal+bath 中是否适用？

ACMP 摘要原文要点：
- "general arguments... compactly supported... whenever **no isometries of the background spacetime exist**"
- 例子："**massless gravitons and no external reservoir**"

**两条不利对照**：
1. eternal AEMM 双侧设置存在 Killing 时间 → ACMP 前提违反
2. AEMM 用 non-grav bath（external reservoir）→ ACMP 例子明确"no external reservoir"

故：**ACMP 2025 的 compactly supported 论据不直接覆盖任务设定的 SYK/JT + bath 标准 setup**。任务§3 问题1 答案：在任务设定下，ACMP 显式构造不可用；island 算符仍依赖 dressing 到 boundary 时间的 non-compact 重构。

## §7 GKRR 2026 完备性反驳与宽 A_bdy

GKRR 摘要主张：boundary algebra 在 AdS（含 JT/SYK）和渐近平直情形下都是 complete。

若取宽 A_bdy = SYK + bath：
- post-Page 时 entanglement wedge of (SYK ∪ bath) 包含整个 spacetime（含 island）
- entanglement wedge reconstruction → island 算符 = (SYK ∪ bath) 中某高度 nonlocal 算符的*精确* dual
- ⟹ A_island ⊆ A_bdy_wide
- ⟹ **Δ_M.B = 0（宽定义）**

这正是任务命题 B（trivializing alternative）。在宽 A_bdy 下 **Phase 1 倾向于命题 B 赢**。

## §8 必须回答的三个问题

**Q1：ACMP 算符在 SYK/JT 中显式形式？**
答：**在任务设定（eternal + bath）下不直接存在**。需变体（一侧 collapse、纯引力无 bath）才能引用，但偏离任务设定。

**Q2：这些算符是否真不在 A_bdy 中？**
答：取决于 A_bdy 定义。窄定义 → Δ = O(1) 但人为；宽定义 → GKRR completeness 给 Δ = 0。

**Q3：若 boundary completeness 成立，A_island = A_bdy？**
答：**是**——GKRR 核心声明。M.B 在宽定义下不满足。

## §末 声张强度对比与新增卡点

**§0 目标 vs 实际**：

| 维度 | 目标 | 实际 |
|---|---|---|
| M.B 满足？ | 期望 yes | yes（窄）/ no（宽） |
| Δ_M.B 量级 | 期望 O(1) | O(1) 窄 / 0 宽 |
| 论据强度 | 引 ACMP 2025 | ACMP **不适用** eternal+bath |

**结论：不一致，不写入 ✅**。开立卡点：

**[CP-001-Phase1] A_bdy 定义争议**：窄 A_bdy 排除 bath 是人为选择。物理合理的宽 A_bdy 下 M.B 不满足。需 PI 裁定。

**[CP-002-Phase1] ACMP 不适用 eternal+bath**：原"建议引用 ACMP"行不通。需要变体设置（无 Killing + 无 bath）。

**[CP-003-Phase1] GKRR completeness 真实强度未核**：仅读摘要。Phase 2 必读 GKRR 正文。

**[CP-004-Phase1] 相对熵单调性方向**：任务§5 "后者严格小→M.B 满足" 疑为笔误。

**[CP-005-Phase1] 量级估计 e^{−S_BH/2} 待核**：依赖典态/HP 一般论据，需 SYK 具体参数下数值核。

**Phase 1 收官认定**：本 Phase **未能给出 M.B 在标准 setup 下被严格满足的无条件证明**。Phase 1 净结果：**M.B 满足性仍开放**，需 Phase 2 同时攻 GKRR completeness 真实强度 + 寻找 setup 变体使 ACMP 直接适用。
