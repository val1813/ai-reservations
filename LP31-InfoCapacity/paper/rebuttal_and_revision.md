# 审稿回应与论文修正

## 致命1: 标量GW极化已被LIGO排除 → **接受, 撤掉此声称**

**审稿人是对的。** GW170814张量vs纯标量=1000:1, GW170817=10¹⁰:1。标量极化已排除。

**修正:** 
- 摘要和Section V中移除"标量引力波极化"作为预测
- 替换为: "DGF的引力波是q场密度波。当γ→0时波速=c(与GW170817一致)。DGF的波-扩散交叉(k_cross=γ/2c)可能在低频(<k_cross)产生与GR不同的色散——这是可检验的。"
- 诚实标注: "DGF目前不预测引力波极化。波方程□q=0在真空成立,但q↔h_μν的完整映射尚待建立。"

## 致命2: "推导引力"实为校准 → **接受, 修改语言**

**审稿人是对的。** G是外部校准, d=3是输入。

**修正:**
- 全文"derive"→"reproduce"/"recover"/"is consistent with"
- 摘要加入: "The framework accepts c, ℏ, G, and d=3 as empirically determined inputs"
- Section IV明确: "The integration constant is identified as GM/c² by matching to the observed Newtonian force law. The 1/r functional form is derived from the static equation; the coupling strength G is calibrated, not predicted."

## 致命3: 优先系未指定 → **接受, 诚实讨论**

**审稿人是对的。** γ∂_t q在γ>0时破缺Lorentz。

**修正:**
- Section VI加入: "The damping term γ∂_t q selects a preferred frame—the rest frame of the information medium. When γ>0, Lorentz invariance is broken. This is physically expected: decoherence requires a time arrow. In vacuum (γ→0), Lorentz invariance is restored."
- "The preferred frame is naturally identified with the cosmic rest frame (CMB). Lorentz-violating signatures are controlled by γ and must satisfy existing constraints. We estimate γ < H₀ ≈ 10⁻¹⁸ s⁻¹ from cosmological consistency, placing LV effects below current experimental sensitivity."

---

## 修正后的核心声张

**论文真正证明了什么:**

1. ✅ **静态q场满足∇²(ln 1/q)=0** → 球对称解q(r)=e^{-GM/rc²} → 弱场恢复Newton
2. ✅ **扩散+自组织统一在同一个方程** → 两个项来自∇²(ln q)的展开
3. ✅ **J-电流耦合产生有限传播速度** → 波方程□q=0(γ→0), 扩散方程∂_t q=D₀∇²q(γ大)
4. ⚠️ **波-扩散交叉可检验** (k_cross=γ/2c处行为改变)
5. ⚠️ **软边界可检验** (EHT—需定量化)

**论文不能声称的:**

1. ❌ 推导了G的值 — G是外部校准
2. ❌ 推导了d=3 — d=3是输入
3. ❌ 标量GW极化 — 已被排除
4. ❌ 完整的Einstein方程 — 只恢复了静态Newton极限
5. ❌ 从纯信息论"推导"引力 — 框架需要c, ℏ, G, d=3, γ, a作为输入

---

## 修正后的摘要

We show that the static limit of information capacity dynamics on a discrete graph yields the Laplace equation ∇²(ln 1/q)=0 for the free-capacity fraction q. Building on Zilly's (2026) derivation of quantum mechanics from finite capacity, we introduce information cells with bounded capacity evolving under causal, finite-speed dynamics. The q-field obeys a telegraph equation that interpolates between wave propagation (□q=0, speed c) and diffusion (∂_t q=D₀∇²q) as the damping parameter γ varies. In the static limit, the spherically symmetric solution q(r)=e^{-GM/rc²} reproduces the Newtonian gravitational potential at large r, with the coupling constant G identified empirically. The same equation's nonlinear expansion ∇²q/q = |∇q|²/q² unifies diffusive decoherence (q≈1) with self-organizing gravitational collapse (q≈0). The framework accepts c, ℏ, G, d=3, and γ as empirically determined inputs; it predicts a frequency-dependent crossover from wave to diffusive behavior at k=γ/(2c) and a soft boundary replacing the classical event horizon—both原则上testable by gravitational wave and black hole shadow observations, respectively.

---

## 投稿策略调整

| 原计划 | 修正后 |
|--------|--------|
| PRD,声称"推导引力" | PRD,声称"引力势方程的静态起源" |
| 卖点: 标量GW | 卖点: ∇²(ln 1/q)=0 + 扩散/自组织统一 + 软边界 |
| 对标GR竞争 | 与GR兼容, 在强场/低频有新预言 |
| G, c, d=3是输入 | 诚实标注在摘要中 |

**关键改变:** 从"我们推导了引力"→"我们展示了引力势方程如何从信息容量动力学的静态极限涌现"。声张缩小了，但更诚实、更难被拒。
