# NSF-FCS-1 研究计划

## 北极星

fractional long-jump exclusion 的右 reservoir-current FCS：`lambda_R''(0)` 是否继承 boundary conductance 的 `L` 标度？

## 驱动矛盾

命题A：boundary conductance 的 fractional Fick law 标度已经足以推出 reservoir-current variance/CGF 二阶导数同标度。

命题B：平均 current 与 current variance 属于不同层级；fractional hydrodynamics 支持 mean conductance，但 `lambda_R''(0)` 可能受 reservoir 实现、mobility、nonlocal boundary condition 或 finite-size correction 改写。

## 第一轮目标

1. 写出 classical long-jump exclusion 的 tilted generator，只 tilt 右 reservoir 注入/抽出事件。
2. 明确 observable：`Q_R(t)`，不是任意 cut-current。
3. 用文献或 Poisson 方程/Green-Kubo 形式判断 `lambda_R''(0)` 的标度是否应与 `G_R(L)` 一致。
4. 对三段给出等级：
   - `alpha>3/2`: `L^-1`
   - `alpha=3/2`: `(log L)/L`
   - `1<alpha<3/2`: `L^{-(2alpha-2)}`

## 成功标准

- 至少把 `1<alpha<3/2` 的 `lambda_R''(0)` 标度从“强推断”升级为“可验证公式/数值流程”。
- 若不能升级，明确缺口：tilted generator、boundary condition、或 fluctuation-dissipation 不成立。

