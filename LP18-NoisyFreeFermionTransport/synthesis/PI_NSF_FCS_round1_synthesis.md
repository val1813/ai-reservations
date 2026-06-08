# PI NSF-FCS-1 Round 1 综合

## 输入

- A: current/A/NSF_FCS_round1_A.md
- B: current/B/NSF_FCS_round1_B.md
- INSPECTOR A: synthesis/inspector_NSF_FCS_A_round1.md，通过
- INSPECTOR B: synthesis/inspector_NSF_FCS_B_round1_recheck.md，通过

## 汇合判断

**类型：强汇合。**

A 从标准 tilted generator / Poisson 方程出发，写出右 reservoir-current 的 SCGF：

`lambda_R(s)=principal_eigenvalue(L_s^R)`

其中只 tilt 右 reservoir 注入/抽出事件，不 tilt cut-current。A 给出二阶公式：

`lambda_R''(0)=<a_R>_pi+2<b_R-J_R,phi>_pi`，

`L phi=-(b_R-J_R)`。

B 从电网络/renewal/queue 角度独立到达同一结构：`lambda_R''=A_R+K_R`，并指出同标度判据不是 `G_R` 本身，而是

`S_R(L)=lambda_R''(0)/G_R(L)`。

两者共同结论：**目前不能把 `lambda_R''(0)` 与 boundary conductance 同标度当作定理；必须控制 activity 项与 Poisson/Green 项。**

## 本轮推进

1. `L_s^R` 已明确，observable 固定为右 reservoir-current `Q_R(t)`。
2. `lambda_R''(0)` 已转化为有限体积 Poisson/resolvent 问题。
3. 缺口明确为：`<b_R-J_R,(-L)^{-1}(b_R-J_R)>_pi` 的 `L` 标度。
4. B 提供可计算诊断：分别测 `A_R(L)`、`K_R(L)`、`S_R(L)`，并用 buffer reservoir 作为诊断构造，但不能直接当反例。

## 结论等级

- `alpha>3/2: L^-1`：强推断。
- `alpha=3/2: (log L)/L`：待验证。
- `1<alpha<3/2: L^{-(2alpha-2)}`：强推断主候选。

但以上针对 `lambda_R''(0)` 仍未升级为已证；Round 2 必须攻 resolvent / numerical Poisson 方程。

## Round 2 指令

A：查找或建立 fractional long-jump exclusion 的 Poisson/resolvent 标度估计。重点关键词：boundary current variance, additive functional CLT, H_{-1} norm, nonlocal Dirichlet form, reservoir current.

B：设计最小 Poisson 方程数值方案，尤其低密度/单粒子近似，判断 `S_R(L)` 是否常数；buffer reservoir 只作为诊断，不作为主结果。

