# INSPECTOR NSF-FCS-1 Round 3 - A

输入文件：
- `current/A/NSF_FCS_round3_A.md`
- `synthesis/PI_NSF_FCS_round2_synthesis.md` 作为背景

检查范围：仅做量纲、符号/方向、循环论证、数量级、代数/极限校对；不评价发表价值。

## 1. 完整二阶公式与 carré-du-champ 符号

A 文采用

`(L_theta f)(eta)=sum_z c(eta,z)[exp(theta q_R(eta,z)) f(eta^z)-f(eta)]`

因此

- `b=L'_0 1=sum_z c q_R`，单位 `s^-1`；
- `a=L''_0 1=sum_z c q_R^2`，单位 `s^-1`；
- `L phi=-h`，`h=b-J`，所以 `phi` 无量纲；
- `B phi=L'_0 phi=sum_z c q_R phi(eta^z)`，单位 `s^-1`；
- `C=sum_z c q_R[phi(eta^z)-phi(eta)]`，单位 `s^-1`。

代数核算：

`B phi=sum_z c q_R[phi(eta)+Delta_z phi]`

取平稳平均并用 `<phi>_pi=0`：

`<B phi>_pi=<phi b>_pi+<C>_pi=<h,phi>_pi+<C>_pi`.

所以

`lambda_R''(0)=<a>_pi+2<B phi>_pi=<a>_pi+2<h,phi>_pi+2<C>_pi`

这一行符号一致。

carré-du-champ 核算：

`<sum_z c(q_R+Delta_z phi)^2>_pi`

`=<a>_pi+2<C>_pi+<sum_z c(Delta_z phi)^2>_pi`.

由 stationarity：

`0=<L phi^2>_pi=<2 phi L phi>_pi+<sum_z c(Delta_z phi)^2>_pi`

故

`<sum_z c(Delta_z phi)^2>_pi=-2<phi,L phi>_pi=2<h,phi>_pi`.

在 A 文给定的生成元号约定 `L f=sum c(f(eta^z)-f(eta))` 和 Poisson 方程 `L phi=-h` 下，A 的正号是正确的；不差负号。若改用正算子 `-L` 作为生成元记号，才会看到相反写法，但那不是本文约定。

量纲：`theta` 与 `q_R` 无量纲，所有二阶项均为 `s^-1`。通过。

## 2. fast open SSEP 二阶展开与 cancellation 方向

A 文使用

`R_fast(omega)=(arsinh sqrt(omega))^2`,

`omega=rho_a(1-rho_b)(e^theta-1)+rho_b(1-rho_a)(e^{-theta}-1)`.

小 `theta` 展开：

`R_fast(omega)=omega-(1/3)omega^2+O(omega^3)`,

`omega'(0)=rho_a-rho_b`,

`omega''(0)=rho_a(1-rho_b)+rho_b(1-rho_a)`.

因此

`Lambda_L''(0)=L^{-1}[rho_a(1-rho_b)+rho_b(1-rho_a)-(2/3)(rho_a-rho_b)^2]+o(L^{-1})`

与 A 文一致。

右 reservoir activity：

`a_R(eta)=rho_b(1-eta_L)+(1-rho_b)eta_L`,

`<eta_L>=rho_b+O(L^-1)` 给出

`<a_R>_pi=2 rho_b(1-rho_b)+O(L^-1)=O(1)`.

于是 `lambda_R''=O(L^-1)` 与 `<a_R>=O(1)` 同时成立，确实要求

`2<B phi>_pi=-<a_R>_pi+O(L^-1)`

或等价地

`2<h,phi>_pi+2<C>_pi=-<a_R>_pi+O(L^-1)`.

方向正确：这是从 `O(1)` activity 到 `O(L^-1)` SCGF 的强 cancellation，不是 activity 本身小。

## 3. slow-boundary SSEP 方向

若 boundary rates 已缩放为 `O(L^-1)`，则右 reservoir 的 `a_R` 从定义上就是 `O(L^-1)`。此时 `lambda_R''=<a_R>+2<h,phi>+2<C>` 不需要先抵消一个 `O(1)` 项；A 文把该情形解释为 slow-boundary/串联变分机制，方向与 fast-boundary 对照一致。

未发现符号反向或数量级反向。

## 4. long-jump `A_R(L)=O(1)` 与 `alpha>1` tail

若右 reservoir 到 bulk site 的未缩放 tail 为

`r_R(x) ~ dist(x,R)^(-alpha)`,

且右边界距离可写成 `d=1,...,L`，则

`A_R(L)=sum_x r_R(x) ~ sum_{d=1}^L d^(-alpha)`.

当 `alpha>1` 时该和有界并收敛到常数量级，所以 `A_R(L)=O(1)` 与 tail 假设一致。

条件警告：该结论只适用于未额外乘上 `L` 依赖 prefactor 的 reservoir rates。A 文已经显式标注：若模型实际把 rates 缩放到 `O(G_R(L))`，则应改判为 slow-boundary 型。这是必要条件标注，不构成代数阻断。

## 5. 循环论证与待证命题

A 文没有把 `D_R(L)=O(G_R(L))` 当作已证结论；它明确写为待证核心：

`D_R(L)=<sum_{z in R} c_z(q_R(z)+Delta_z phi)^2>_pi=O(G_R(L))`.

这避免了把 hydrodynamic conductance 或 `H_-1` 小量直接循环替代为 jump-current FCS 小量。未发现循环论证。

## 最终判定

通过。

附带条件警告：`A_R(L)=O(1)` 依赖未缩放的 `alpha>1` reservoir tail；若后续模型定义含额外 `L` 依赖缩放，fast-boundary cancellation 结论必须改写为 slow-boundary 型检查。
