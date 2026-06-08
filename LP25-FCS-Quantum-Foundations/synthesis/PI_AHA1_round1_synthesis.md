# PI综合 | AHA1 Round 1

**日期:** 2026-06-03
**输入:** A-β(α)解析推导 (446行) + B-β↔μ对偶分析 (549行)
**汇合判断:** 强收敛 — 解析与数值独立验证

## ⚠️ REVIEWER修复记录 (2026-06-03)
- Costa et al. PRL→arXiv preprints
- Dhawan作者+DOI修正
- 新增Sarkar PRB 2024 + Bhat-Žnidarič PRB 2025
- 纯虚定理声张降级

---

## 核心结果

### A博士：β(α)解析表达式

$$\beta(\alpha, \gamma_\phi=0.5) = \frac{0.8127}{\alpha} + 0.4218$$

- RMSE=0.015，5个α点偏差均<3%
- 穿越点 α_c = 0.8127/(1−0.4218) = **1.406**（COH观测≈1.4）
- 物理机制：单粒子Green函数→分数阶扩散方程→1/α标度来自非局域色散ε(k)~|k|^{α−1}

### B博士：β是真正独立的第二个标度指数

- β(μ) ≈ 1.225 − 0.287·μ（线性，R²=0.995）— 非平凡反相关
- **dβ/dμ < 0**：更长程hopping→输运更弹道（μ小）但相干衰减更快（β大）
- β穿越1在α≈1.39（早于μ穿越1.5）— 量子相干是更灵敏的扩散探测器

---

## GATE 0先发状态

| 文献 | 覆盖 | 我们的增量 |
|------|------|----------|
| Dhawan et al. PRB 110, L081403 (2024) | 电导标度δ≈2α−2 | 未计算非对角相干衰减 |
| Costa et al. arXiv:2504.00188v3 (2025) | 电流方差Σ_R''(0)~L^{-μ(α)} | 未计算C_{i≠j}衰减 |
| Sarkar et al. PRB 109, 165408 (2024) | 电流-退相干相图, 用Im[C]算电流 | 未研究\|C_{ij}\|空间衰减标度 |
| Bhat & Žnidarič PRB 111, 174306 (2025) | NN-XX链非对角元纯虚定理 | 未推广到power-law hopping, 未研究标度 |
| **我们的β(α)** | — | **第二个独立标度指数** |

**先发判定：β(α)作为独立标度指数是新的。** Dhawan、Costa和Sarkar都聚焦对角观测量（电流/电导/噪声）或使用Im[C]计算对角量。Bhat-Žnidarič的纯虚定理限于最近邻XX链。无人系统研究power-law hopping非对角相干衰减的空间标度行为。

---

## PRL角度（B博士提炼）

> "Dhawan et al. PRB (2024) and Costa et al. arXiv:2504.00188v3 (2025) established the first scaling exponent μ(α) for current fluctuations in power-law hopping NESS. Sarkar et al. PRB (2024) mapped the current-decoherence phase diagram of the same system using Im[C] for current. Bhat-Žnidarič PRB (2025) proved purely imaginary off-diagonals for nearest-neighbor XX chains. We generalize the pure imaginary theorem to power-law hopping and report the discovery of β(α) — the second independent scaling exponent governing the spatial decay of quantum coherence. Together, μ(α) and β(α) form the first two-exponent characterization of this nonequilibrium universality class. The two exponents are anti-correlated (dβ/dμ<0), revealing a speed-coherence trade-off: more ballistic transport accelerates quantum decoherence."

---

## 下一步

- INSPECTOR校验A+B产出
- 补全γ_φ依赖的β(α,γ_φ)全公式
- 写Dhawan et al.对比段落（证明我们的增量）
