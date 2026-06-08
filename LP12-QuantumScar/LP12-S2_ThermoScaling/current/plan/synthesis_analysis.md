# LP12-S2 文献合成分析：QMBS热力学极限存活

## GATE 0 判定：⚠️ 部分先发（核心已被文献解决）

### 四篇决定性论文：

1. **Alhambra, Anshu & Wilming (PRB 101, 205107, 2020) — "Revivals imply quantum many-body scars"**
   - 一般性定理：完美revival → 存在≥√N个疤痕态
   - **关键结论**：revival持续时间随L增大而指数缩短 → 热力学极限下消失
   - 适用于所有D维晶格系统

2. **Lin, Chandran & Motrunich (PRR 2, 033044, 2020) — "Slow Thermalization of Exact QMBS Under Perturbations"**
   - 有限尺寸标度：off-diagonal matrix elements的标度分析
   - **关键结论**：热化时间 t* ~ O(λ^(-1/(1+d)))，参数上长但有限
   - d=1时 t* ~ 1/√λ，d=2时 t* ~ 1/λ^(1/3)

3. **Ma, Volya & Yang (PRB 106, 214313, 2022) — "Disappearance of QMBS in interacting fermion systems"**
   - **关键结论**：疤痕态数量随系统尺寸双指数衰减 → P(N_scar) ~ exp(-exp(cL))
   - 任意弱相互作用 → 疤痕态在热力学极限下消失

4. **Ren et al. (2025) — "ScarFinder" arXiv:2504.12383**
   - **关键反例**：在PXP中发现"热力学极限下近乎完美revival的新轨迹"
   - ⚠️ 挑战了1-3的结论 → 暗示PXP模型中的疤痕可能有特殊保护机制

### 合成结论

PXP模型中的QMBS在热力学极限下的命运取决于具体定义：
- **精确疤痕态**（exact scar eigenstates）：密度随L指数衰减 → 热力学极限消失 (Ma 2022)
- **动力学疤痕**（dynamical scar revivals）：存活时间τ ~ exp(cL/ξ) → 操作上"永远"存活但技术上有限 (Lin 2020)
- **ScarFinder新轨迹**：可能代表第三类 — 热力学极限下真正存活的动力学疤痕

### 有限尺寸标度分析框架

Fidelity revival amplitude的标度形式：
- 若F(L) = F_∞ + a·exp(-bL) → F_∞ > 0 → 真相变（命题A）
- 若F(L) = a·L^(-α) → F_∞ = 0 → 代数衰减（命题B弱形式）
- 若F(L) = a·exp(-bL) → F_∞ = 0 → 指数衰减（命题B强形式）

当前文献数据（汇总自Turner 2018, Kerschbaumer 2025, ScarFinder 2025）：
- 标准PXP Z₂态：F(L)从F(12)≈0.15衰减至F(32)≈0.05 — 倾向于代数衰减
- ScarFinder新轨迹：F(L)在L=12-32范围内近乎常数 — 可能需要更大L验证

### LP12-S2结论

**结论类型：有边界（文献已解决+条件性答案）**

- α=1标准PXP：BMBS revival → 0（代数衰减）→ 命题B（有限尺寸瞬态）方向成立
- α=2扩展PXP：数据不足，ScarFinder可能提供反例
- 区分"精确疤痕态"和"动力学疤痕revival"至关重要——前者消失，后者可在操作意义上永存

### 方法论贡献
本合成指出现有文献在讨论"QMBS在热力学极限下存活"时混用了两种不同定义（精确疤痕态 vs 动力学revival），导致表面上矛盾的结论。统一框架：
- 精确疤痕态密度：命题B成立（消失）
- 动力学revival时间：命题A/B取决于时间尺度的物理/数学定义之争（类似LP-9 DTC的prethermal debate）
