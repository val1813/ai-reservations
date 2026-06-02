# A 博士任务书 — Phase 5

**课题：** Hawking-Encoding v1
**Phase：** 5（Petz strict gap / relative entropy 判据）
**日期：** 2026-06-01
**价值分类：** [核心] — 直接检验 M.B 是否存在可量化非平凡信息差

---

## 攻击目标

构造 reference state `ω0` 与 infallen-qubit excited state `ω1`，估计

`Δ_Petz = S_{A_full}(ω1||ω0) - S_{A_bdy}(ω1||ω0)`

并判定是否存在 strict lower bound：

`Δ_Petz > 0`。

若 strict gap 成立，则 M.B 可用 relative entropy gap 表述，不必等待 exact Jones index。

若 strict gap 不成立，尤其在宽 `A_bdy = SYK ∪ bath/radiation` 定义下为 0 或指数小，则 M.B 在物理宽边界代数下失败，island reconstruction 只是 Petz/QEC 等价重构。

---

## 背景

Phase 4 裁决把 CP-009/CP-010 收缩为：

1. canonical setting 下是否存在 strict Petz / relative entropy gap；
2. 是否能构造真正 physical commutant / edge mode。

A 线负责第一个问题。注意 Phase 1 曾经出现 relative entropy 符号笔误，必须使用 K1.6：

`N ⊂ M => S_M(ω1||ω0) >= S_N(ω1||ω0)`。

因此 M.B 非平凡不是 "相对熵下降"，而是更大代数 `A_full` 对态的可区分度严格更高。

---

## 具体推导任务

### 步骤 1：固定三种 `A_bdy`

必须分别计算或估计：

1. **窄边界代数**：`A_bdy^narrow = SYK single-trace`。
2. **宽边界代数**：`A_bdy^wide = SYK ∪ bath/radiation`。
3. **microcanonical crossed-product boundary algebra**：`A_bdy^micro = A_bdy ⋊ R`。

不要把窄代数的 O(1) gap 冒充为物理宽边界代数的 gap。

### 步骤 2：选择态对

建议态对：

- `ω0 = TFD/KMS` 或 Page-time 后的 evaporating black hole reference state；
- `ω1 = U_q ω0 U_q†`，其中 `U_q` 是投掷一个 infallen qubit 的局域 bulk excitation。

要求写清楚 qubit 是否：

- 位于 pre-Page interior；
- 位于 post-Page island；
- 已被 radiation entanglement wedge 包含。

### 步骤 3：用 JLMS / QEC / Petz recovery 估计

对宽代数，检查 EW reconstruction 是否给出 recovery map：

`R_{Petz}: A_bdy^wide -> A_full`

若 recovery 在 code subspace 上误差 `ε(N)`，则相对熵差应受 Fawzi-Renner / approximate sufficiency 型 bound 控制：

`Δ_Petz <= f(ε(N))`。

若 `ε(N) ~ e^{-cN}`，则 strict O(1) gap 不存在。

### 步骤 4：窄代数压力测试

对窄 `A_bdy^narrow`，估计 infallen qubit 的可区分度：

- `S_{A_full} = O(1)`；
- `S_{A_bdy^narrow}` 可能为 `O(e^{-S_BH})` 或 `O(1/N)`。

若成立，这只说明窄代数定义下 M.B 成立，不足以证明岛屿公式给出新动力学机制，因为物理 Page curve 通常使用 radiation/bath 的宽代数。

### 步骤 5：输出判定

必须给出：

- `Δ_Petz^narrow`：[O(1) / 小量 / 不确定]
- `Δ_Petz^wide`：[O(1) / O(ε) / 0 / 不确定]
- `Δ_Petz^micro`：[O(1) / trace-window 小量 / 不确定]
- K1.10 是否升级；
- CP-009 是否关闭。

---

## 禁止

- 不要再写反向的相对熵不等式。
- 不要把 narrow boundary 结论当作 wide boundary 结论。
- 不要只引用 "Petz recovery 存在"；必须说明误差如何控制 relative entropy gap。
- 不要忽略 code subspace / full Hilbert space 区别。

---

## 产出格式

```
⚡ 审核入口（PI 只读）：
  Δ_Petz^narrow：[结论]
  Δ_Petz^wide：[结论]
  Δ_Petz^micro：[结论]
  strict O(1) gap 是否存在：[是/否/仅窄定义/不确定]
  K1.10 升级判定：[可升级 ✅L2 / 维持 ⚠️L1 / 降级]
  最脆弱步骤：[一句话]

然后 §1/§2/§N/§末 完整作业。
```

## 关键文献

- Petz 1986 sufficiency theorem
- JLMS relative entropy equality
- Almheiri-Dong-Harlow 1411.7041
- Harlow 2016 holographic QEC
- Fawzi-Renner approximate recovery
- CPW 2209.10454
- Penington-Witten 2306.03999
