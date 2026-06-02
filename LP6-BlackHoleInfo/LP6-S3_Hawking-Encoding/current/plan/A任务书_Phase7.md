# A 博士任务书 — Phase 7

**课题：** Hawking-Encoding v1
**Phase：** 7（论文骨架 — 正面构造）
**日期：** 2026-06-01
**价值分类：** [核心] — 将 6 Phase 推导整理为可投稿论文骨架

---

## 攻击目标

写出论文的核心命题体系，包含完整的 Definition/Proposition/Proof sketch/Scope limitations。论文的核心主张是：

> 在 SYK/JT post-Page code subspace 中，黑洞信息编码的 "missing bit" (M.B) 是否成立取决于边界代数的定义。窄代数下 O(1) Petz gap 倾向成立；宽辐射/浴代数下 gap 受 QEC/Petz recovery error 控制，岛屿公式不单独给出新的 Lorentzian 信息搬运机制。

---

## 必须输出的论文骨架

### §1 Introduction 主张边界

明确写出论文主张什么、不主张什么：

**主张（Claim）：**
1. 岛屿公式 + 复制虫洞在宽边界代数（SYK∪bath/radiation）中构成 algebraic recovery/bookkeeping——Page 曲线正确，但不等价于 "新的 Lorentzian unitary transport mechanism"
2. M.B 的 O(1) relative entropy gap 是窄边界代数（仅 SYK single-trace）现象
3. canonical Type III₁ vs microcanonical Type II∞ 的 ensemble 依赖是真实的物理维度，不是技术细节

**不主张（Non-claim）：**
1. 不否定岛屿熵公式或 Page 曲线的正确性
2. 不声称黑洞信息悖论 "未被解决"——只说 "机制" 部分的 claims 需要精确化
3. 不声称高维 holographic CFT 或渐近平坦黑洞中结论相同

### §2 Definitions（精确定义）

必须给出以下概念的论文级精确定义，引用文献来源：

1. **Code subspace** `H_code`：post-Page SYK/JT code subspace，含 semiclassical island
2. **A_full**：包含 island bulk effective field operator 的 code algebra
3. **A_bdy^narrow**：单侧 SYK single-trace / simple boundary algebra
4. **A_bdy^wide**：SYK 与 bath/radiation 生成的宽代数
5. **Relative entropy gap**：`Δ(ω₁,ω₀) := S_{A_full}(ω₁‖ω₀) − S_{A_bdy}(ω₁‖ω₀)`
6. **M.B (Missing Bit)**：信息编码的 "新机制"——即是否存在独立于 QEC/Petz recovery 的 Lorentzian information-transport mechanism

### §3 Main Proposition（核心命题）

**Proposition 1（Boundary-algebra separation）：**

假设：
- (H1) post-Page code subspace `H_code` 有 semiclassical island
- (H2) `A_full` 包含 island effective field algebra
- (H3) `A_bdy^wide` 包含 SYK boundary 与 radiation/bath algebra
- (H4) EW reconstruction / Petz recovery 在 `H_code` 上误差为 `ε(N)`，`ε(N)→0` as `N→∞`
- (H5) `ω₀, ω₁` 为 code subspace 内 reference/excited state（infallen qubit）

结论：
- (C1) `0 ≤ Δ_wide ≤ f(ε(N))`，其中 `f(ε)→0` 当 `ε→0`。宽代数下无独立 O(1) mechanism gap。
- (C2) 对 `A_bdy^narrow`（不含 bath/radiation decoder），存在态对使 `Δ_narrow = O(1)`。
- (C3) 因此 M.B 的 "新机制" 叙述是代数定义依赖的：窄代数 → 有 gap；宽代数 → 无独立 O(1) gap。

**Proof sketch（5 步骨架）：**

Step 1: Petz 单调性 → `Δ ≥ 0`

Step 2: 若 `A_bdy^wide` 含 approximate recovery map `R_N: A_full → A_bdy^wide` 且误差 `ε(N)`，则 Petz sufficiency theorem → `Δ_wide ≤ f(ε(N))`

Step 3: JT/SYK post-Page 中 EW reconstruction 正是这种 approximate sufficiency → `Δ_wide` 无 O(1) gap

Step 4: 窄代数不含 decoder → scrambling/typicality 压低 infallen qubit 在 `A_bdy^narrow` 中的可见度 → `Δ_narrow = O(1)`

Step 5: 两种代数定义给出相反的 M.B 判定 → M.B 是代数定义依赖的

### §4 Scope Limitations（适用域限制）

逐条列出定理的适用范围和不适用范围：

1. **只在 code subspace 内成立**，不是全 Hilbert space theorem
2. **只在 post-Page SYK/JT + bath 设置中推导**，高维 holographic CFT、渐近平坦黑洞需独立检验
3. **canonical Type III₁ 设置**：P₀ 不存在，GKRR completeness 不成立，`f(ε)` 受 ensemble 选择影响
4. **microcanonical Type II∞ 设置**：GKRR completeness 可能成立，但 approximate sufficiency 仍控制 gap
5. **doubly non-perturbative 窗口**（~e^{-1/G_N}）：当前推导只在 perturbative-in-1/N + leading replica saddle 精度内有效

### §5 审稿人可能攻击的点（主动列出）

1. "code subspace 限制使定理 trivial——谁会在乎只在 code subspace 成立的命题？"
2. "`A_bdy^wide` 的 EW reconstruction 假设 circular——EW reconstruction 正是需要被机制解释的东西"
3. "`f(ε)` 的具体形式未给出——qualitative statement 不能作为 theorem"
4. "窄代数定义人为——自然界不存在不含 decoder 的 observer"
5. "canonical/microcanonical 差异未在论文中分析——不能声称 ensemble-independence"

---

## 禁止

- 不要声称 L2 theorem——当前最好的结论是 ⚠️L1 proposition
- 不要把 K1.10 升级为 ✅L2——升级条件（GKRR completeness + exact index）未满足
- 不要声称高维或 flat space 推广——只写 SYK/JT
- 不要把 "no mechanism" 写成 "island formula is wrong"——这是不同的声张

---

## 产出格式

```
⚡ 审核入口：
  论文核心主张：[一段话]
  最强命题：[Proposition 1 一句话]
  命题等级：[⚠️L1 / ✅L2]
  不能写的内容：[列表]
  投稿期刊建议：[PRD/JHEP/...]

正文：完整论文骨架（§1-§5）+ 各节待补充标记。
```
