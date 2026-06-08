# PI NSF-FCS-1 Round 3 综合

## 输入

- A: `current/A/NSF_FCS_round3_A.md`
- B: `current/B/NSF_FCS_round3_B.md`
- INSPECTOR A: `synthesis/inspector_NSF_FCS_A_round3.md`，通过，带条件警告
- INSPECTOR B: `synthesis/inspector_NSF_FCS_B_round3.md`，警告可继续

## 汇合判断

**类型：命题精确化 + 可证伪路径收敛。**

Round 3 的核心进展是把 NSF-FCS-1 从模糊的

`lambda_R''(0) 是否继承 G_R(L) 标度`

改写成一个更可检验的 microscopic corrector residual 命题：

`D_R(L)=<sum_{z in R} c_z(q_R(z)+Delta_z phi)^2>_pi = O(G_R(L))`.

这里 `L phi=-h`，`h=b_R-<b_R>_pi`，`q_R` 是右 reservoir jump-current increment。A 的分析显示 fast open SSEP 中 `<a_R>=O(1)` 但 `lambda_R''=O(L^-1)`，所以必须存在强 cancellation；slow-boundary SSEP 则是 activity 本身已缩放，机制不同。对未额外缩放的 long-jump reservoir，若 `sum_x r_R(x)=O(1)`，NSF-FCS-1 应归入 fast-boundary 型强 cancellation 问题，而不是 slow-boundary 型串联电阻问题。

B 的贡献是把这个命题压成台账判据：每个 `L` 和 reservoir 实现必须输出

`<a>, 2<h,phi>, 2<C>, lambda_R'', G_R, S_R=lambda_R''/G_R`

并且当显式 `C` 不稳定时，用 tilted generator 主特征值二阶有限差分给出 `lambda_R''`。INSPECTOR B 的警告必须保留：若 `2<C>` 是由 `lambda_tilt''-<a>-2<h,phi>` 反推得到，它只能作为 residual 报告，不能再反过来作为 decomposition balance 的独立验证。

## 当前结论

1. `lambda_R''~G_R` 仍未证明，但待证对象已经明确：不是单纯 `H_-1` 小，而是 `q_R+Delta phi` 在 reservoir jump 集合上的 carré-du-champ residual 小。
2. 对未缩放 tail `r_R(x)~x^{-alpha}` 且 `alpha>1`，`A_R(L)=sum_x r_R(x)=O(1)`，因此若 `G_R(L)->0`，必须出现 fast-boundary 型强 cancellation。
3. 若后续模型把 reservoir rates 额外乘上 `L` 依赖 prefactor，使 `A_R(L)=O(G_R(L))`，则当前命题必须改判为 slow-boundary 型，不得继续使用 fast-boundary cancellation 解释。
4. 下一步最有价值的工作不是继续扩展北极星，而是做单粒子 long-jump reservoir 的最小台账测试：它可以在低成本下直接 kill 或保留 NSF-FCS-1。

## Round 4 指令

A：做单粒子 long-jump random walk with right reservoir 的解析 Poisson/capacity test。明确 `r_R(x)`、`A_R(L)`、`G_R(L)`，解 `L phi=-h`，判断 `D_R(L)=<sum_R c(q_R+Delta phi)^2>` 是否同标度于 fractional capacity / `G_R(L)`。优先给出可手算或可渐近估计的 lemma；如果单粒子层面失败，直接建议 kill 当前强命题。

B：实现或写出最小矩阵台账算法的伪代码/脚本规范。必须区分 `C_explicit` 与 `C_from_tilted_residual` 两种状态；keep/kill 只能依赖已校准的 `G_R` 与稳定的 `lambda_tilt''`。目标是给 PI 一个二值判据，而不是趋势图叙述。

## 轮次状态

N=3 for NSF-FCS-1。已满足最低三轮探索要求；未触发硬停止。按 SOP 下一步应进入北极星收尾前检查，但由于 Round 3 产生了更高价值且更可证伪的单粒子台账测试，PI 判断继续一轮定向推进比立即收尾更有意义。
