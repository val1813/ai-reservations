# PI Round 1 综合

## 输入

- A: current/A/round1_A.md
- B: current/B/round1_B.md
- INSPECTOR A: synthesis/inspector_A_round1.md，警告通过
- INSPECTOR B: synthesis/inspector_B_round1_recheck.md，通过

## 汇合判断

**类型：互补汇合。**

A 从标准开放量子系统 + MFT 重建 R1 链条，确认 R1 在一维、free、U(1)、unitary noise、Markovian reservoirs、quasi-local hopping、large-L diffusive scaling 下闭合。A 给出的最小增量是 long-range hopping 破坏 quasi-locality，导致 Zeno 投影后的有效长跳排斥过程从 Laplacian 扩散转向 fractional generator。

B 从分布式共识/纠错码出发，把 gauge trick 解释为 counting 1-form 的全局一致性。B 的有效增量不是重复“长程跳跃”，而是指出 shortcut/cycle 产生的 non-exact holonomy sector 可能在 FCS 中留下拓扑亚领先项。

两者共同指向一个更高价值命题：

> R1 的 Q-SSEP -> SSEP 普适性边界不是简单的“是否自由费米子”，而是“输运图上的 counting field 是否可被全局写成 exact 1-form，且 hydrodynamic generator 是否仍为局域 Laplacian”。

## Round 2 北极星收窄

**新工作命题：** 带 shortcut/长程 hopping 的 noisy free fermion 链是否出现两类 SSEP 等价破坏：

1. **分数扩散破坏：** `J(r)~r^-alpha` 在强噪声下诱导 `r_eff(r)~|J(r)|^2/gamma`。当 `alpha<3/2` 时二阶矩发散，普通 SSEP 的 `lambda''(0)~L^-1` 标度应被 fractional conductance 标度替代。
2. **环路 holonomy 修正：** 即使主导扩散仍存在，单 shortcut 形成的 cycle 在 Peierls/counting holonomy `theta` 非零时，应产生 `Delta lambda ~ K(theta,s)[1-cos theta]` 的有限尺寸 FCS 修正。

## 已杀死/降级的方向

- 纯有限尺寸修正：降级。A 查到 arXiv:2601.16883v1 已系统推进 QSSEP/QSSIP 的 finite-size quantum correction。
- 高维普通几何：降级。R1 Supplement K 已给 `tilde lambda_d=C_Lambda tilde lambda_1d` 的 harmonic conductance 约化，除非引入 cycle/holonomy 或非局域边。
- 泛泛相互作用：暂存。价值高但第一轮可控性低，待 long-range/cycle 方向若失败再切换。

## Round 2 任务书

A: 做 strong-dephasing projection for power-law/shortcut hopping。目标是证明或反驳 `r_eff(j,k) ~ |J_jk|^2/gamma`，并给出 `alpha=3/2` 阈值是否严谨。

B: 聚焦单 shortcut ring 的 holonomy FCS。目标是把 `Delta lambda(s,theta)` 的最低阶结构从 ansatz 推到可检查公式，至少给出偶性、单位、弱耦合阶数和如何数值验证。

## 当前结论

Round 1 不收官。N=1<3，且未触发硬停止。按 SOP 继续 Round 2。

