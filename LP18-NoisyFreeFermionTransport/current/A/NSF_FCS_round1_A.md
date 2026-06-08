# NSF-FCS-1 Round 1 - A博士（学院派）

角色：A博士（学院派）。本轮只处理 classical long-jump exclusion 的右 reservoir-current FCS，不读取 B 产出，不讨论 cut-current 的任意替代定义。

## §-1 先发文献检索

检索工具：paper-search-mcp。检索时间：2026-06-03。

### 检索组1：long-jump exclusion / fractional Fick law

命中：
- Cedric Bernardin, Byron Jimenez Oviedo, "Fractional Fick's law for the boundary driven exclusion process with long jumps", arXiv:1603.01234v3, ALEA 14, 473 (2017), DOI 10.30757/alea.v14-25。
- Cedric Bernardin, Patricia Goncalves, Byron Oviedo Jimenez, "Slow to fast infinitely extended reservoirs for the symmetric exclusion process with long jumps", arXiv:1702.07216v2。
- Milton Jara, "Hydrodynamic limit of particle systems with long jumps", arXiv:0805.1326v2, Commun. Pure Appl. Math. 62, 198-214 (2009), DOI 10.1002/cpa.20253。

用途：这些文献支撑 long-jump exclusion 的 fractional hydrodynamics 与 boundary-driven fractional Fick law。它们直接支撑的是 stationary mean reservoir current / boundary conductance，不直接给出本轮要问的 nonequilibrium reservoir-current SCGF 二阶导数。

### 检索组2：boundary-driven reservoir current fluctuations / current large deviations

命中：
- Lorenzo Bertini, Alberto De Sole, Davide Gabrielli, Giovanni Jona-Lasinio, Claudio Landim, "Large Deviations for the Boundary Driven Symmetric Simple Exclusion Process", Math. Phys. Anal. Geom. 6, 231-267 (2003), DOI 10.1023/A:1024967818899。
- Lorenzo Bertini, Claudio Landim, Mustapha Mourragui, "Dynamical large deviations for the boundary driven weakly asymmetric exclusion process", Ann. Probab. 37 (2009), DOI 10.1214/09-AOP472。
- Tertuliano Franco, Patricia Goncalves, Claudio Landim, Adriana Neumann, "Dynamical large deviations for the boundary driven symmetric exclusion process with Robin boundary conditions", arXiv:2203.14417v1, ALEA 19 (2022), DOI 10.30757/alea.v19-60。
- Angele Bouley, Claudio Landim, "Dynamical Large Deviations for Boundary Driven Gradient Symmetric Exclusion Processes in Mild Contact with Reservoirs", arXiv:2402.05816v1 / J. Stat. Phys. 191 (2024), DOI 10.1007/s10955-024-03356-y。
- Bernard Derrida, Ori Hirschberg, Tridib Sadhu, "Large deviations in the symmetric simple exclusion process with slow boundaries", arXiv:2009.04169v1, J. Stat. Phys. (2020), DOI 10.1007/s10955-020-02680-3。

用途：这些文献说明 boundary reservoirs、Robin/slow contact 与 current large deviations 可显著改变宏观涨落结构。它们支持“reservoir-current FCS 需要自己的 tilted generator / dynamical LDP”，但不是 long-jump reservoir-current `lambda_R''(0)` 的现成定理。

### 检索组3：tilted generator / conditioned Markov process / Green-Kubo-Poisson

命中：
- Raphael Chetrite, Hugo Touchette, "Nonequilibrium Markov Processes Conditioned on Large Deviations", Ann. Henri Poincare 16 (2015), DOI 10.1007/s00023-014-0375-8。
- Pelerine Tsobgni Nyawo, Hugo Touchette, "Current large deviations for driven periodic diffusions", arXiv:1606.02602v2, Phys. Rev. E 94, 032101 (2016), DOI 10.1103/PhysRevE.94.032101。
- G. A. Pavliotis, "Asymptotic Analysis of the Green-Kubo Formula", arXiv:1002.4103v1。
- Claudio Landim, Aniura Milanes, Stefano Olla, "Stationary and Nonequilibrium Fluctuations in Boundary Driven Exclusion Processes", arXiv:math/0608165v1。
- Lorenzo Bertini, Alberto De Sole, Davide Gabrielli, Giovanni Jona-Lasinio, Claudio Landim, "Macroscopic fluctuation theory", Rev. Mod. Phys. 87, 593 (2015), DOI 10.1103/RevModPhys.87.593。

用途：给出 Markov jump process tilted generator、Poisson 方程和 Green-Kubo 表达式的标准框架。它们允许把 `lambda_R''(0)` 写成可验证公式；但要从公式推出 long-jump boundary conductance 的同一 `L` 标度，还需要 resolvent / spectral gap / boundary observable 范数估计。

## §0 框架声明

成熟框架：有限体积 classical boundary-driven symmetric exclusion with long jumps + Feynman-Kac tilted generator + Poisson equation / Green-Kubo for additive functionals。

本轮固定跳跃核：

`c_{ij}(\eta)=p(j-i) eta_i (1-eta_j)`, `p(r)=p(-r) >= 0`, `p(r) ~ a_alpha |r|^{-(1+mu)}`。

从强退相干自由费米映射继承：

`r(r)=2 J0^2/(gamma_phi |r|^{2 alpha})`, 因而 `mu=2 alpha - 1`。

只讨论 `alpha>1`，即 `mu>1`，总长跳率有限。`1<alpha<3/2` 对应 `1<mu<2` 的 fractional 区间；`alpha=3/2` 对应临界 `mu=2`；`alpha>3/2` 对应有限二阶矩扩散区间。

## 1. 右 reservoir-current tilted generator

令系统为 `{1,...,L}` 上的排斥过程。bulk generator 为

`(L_bulk f)(eta)= sum_{1<=i,j<=L, i!=j} p(j-i) eta_i(1-eta_j) [f(eta^{i,j})-f(eta)]`。

右 reservoir 只作用在边界站点 `L`。取右 reservoir 密度 `rho_R`、接触强度 `kappa_R`。右端注入和抽出率为

`c_R^+(eta)=kappa_R rho_R (1-eta_L)`,

`c_R^-(eta)=kappa_R (1-rho_R) eta_L`。

左 reservoir 可类似定义，但本轮不 tilt 左端：

`L_L^res f = c_L^+(eta)[f(eta^{1,+})-f(eta)] + c_L^-(eta)[f(eta^{1,-})-f(eta)]`。

右 reservoir-current 定义为

`Q_R(t)=N_R^+(t)-N_R^-(t)`，

其中 `N_R^+` 计右 reservoir 向系统注入粒子的事件数，`N_R^-` 计系统向右 reservoir 抽出的事件数。注意：这不是穿过某个空间 cut 的 current；bulk 中任何跨 cut long jump 都不计入 `Q_R`。

于是只 tilt 右 reservoir 注入/抽出事件的 tilted generator 是

`(L_s^R f)(eta)=L_bulk f(eta)+L_L^res f(eta)+c_R^+(eta)[e^s f(eta^{L,+})-f(eta)]+c_R^-(eta)[e^{-s} f(eta^{L,-})-f(eta)]`。

长时 SCGF 为最大特征值

`lambda_R(s)=lim_{t->infty} t^{-1} log E_eta[exp(s Q_R(t))] = principal_eigenvalue(L_s^R)`。

其一阶、二阶导数满足有限状态 Markov 链的标准扰动公式。令 `pi` 为 `s=0` 的 NESS，`j_R(eta)=c_R^+(eta)-c_R^-(eta)`，`a_R(eta)=c_R^+(eta)+c_R^-(eta)`，`J_R=<j_R>_pi`。Poisson 方程取

`L phi = -(j_R-J_R)`, `<phi>_pi=0`。

则候选 Green-Kubo / Poisson 表达式为

`lambda_R''(0)=<a_R>_pi + 2 <(j_R-J_R), phi>_pi`

等价于

`lambda_R''(0)=<a_R>_pi + 2 integral_0^infty <(j_R(eta_0)-J_R)(j_R(eta_t)-J_R)>_pi dt`

在非可逆 NESS 情况下需用 generator resolvent 解释，不能简单换成平衡自伴随 Dirichlet form。

--- INSPECTOR_CHECK ---
[公式] `L_s^R=L_bulk+L_L^res+c_R^+(e^s T_L^+-I)+c_R^-(e^{-s} T_L^--I)`；`lambda_R''(0)=<a_R>_pi+2<(j_R-J_R),phi>_pi`，其中 `L phi=-(j_R-J_R)`。`lambda_R''(0)` 单位为 `s^-1`；`L` 为无量纲格点长度。
[方向] 本步只 tilt 右 reservoir 注入/抽出，明确排除了 cut-current；二阶 FCS 被化为有限体积 Poisson/resolvent 问题。
[数据] Chetrite-Touchette DOI 10.1007/s00023-014-0375-8；Pavliotis arXiv:1002.4103；Bertini-Landim 系列 boundary-driven LDP 文献；本项目 Round 3 的 long-jump kernel 映射。
[假设] 有限体积 Markov 链不可约；`alpha>1` 保证总跳率有限；右 reservoir 只接触站点 `L`；符号约定为注入系统记正、抽出系统记负。

## 2. `lambda_R''(0)` 能否直接与 `G_R(L)` 同标度？

结论：本轮不能把 `lambda_R''(0) ~ G_R(L)` 标为已证；只能给出可验证公式和三段候选等级。缺口不在 tilted generator，而在从 Poisson 方程 / Green-Kubo 公式到 `L` 标度的 resolvent 控制。

原因分三层：

1. 均值电导 `G_R(L)=partial J_R / partial(rho_L-rho_R)` 来自 stationary hydrostatics / fractional Fick law。它只需要平均 profile 和平均 current。
2. `lambda_R''(0)` 包含瞬时活动项 `<a_R>_pi` 与时间积分相关项 `2 integral C_R(t) dt`。这两个量可能有相消、边界层或 contact-rate 依赖。
3. 对 nearest-neighbor diffusive SSEP，MFT/Einstein relation 常把 mobility 与 conductance 绑定；但 long-jump reservoir problem 有非局域边界条件，Dirichlet exterior、regional fractional Laplacian、endpoint-only reservoirs 不是自动等价。

因此，Poisson 方程给出了正确的计算路线，但还缺以下任一项：

- 严格谱/resolvent 估计：证明 `<(j_R-J_R),(-L)^{-1}(j_R-J_R)>_pi` 与 fractional resistance 同阶。
- fractional MFT 边界版本：证明 reservoir-current mobility 的二次型与 fractional conductance 同阶。
- 数值闭环：对 `L_s^R` 直接求 principal eigenvalue 或用 cloning/Gillespie 估计 `lambda_R''(0)`，验证三段指数。

若采用小密度差、局部平衡、mobility 非奇异并且 boundary observable 不引入额外标度的附加假设，则可以提出强推断：

`lambda_R''(0) asymp G_R(L)`。

但这是假设，不是本轮由文献和公式推出的定理。

## 3. 三段等级判定

### 3.1 `alpha>3/2: L^-1`

此时 `mu=2alpha-1>2`，Zeno classical jump kernel 有有限二阶矩：

`sum_r r^2 r(r) = (2J0^2/gamma_phi) sum_r r^{2-2alpha} < infinity`。

bulk hydrodynamics 回到普通扩散 domain of attraction，有效扩散常数

`D_eff(alpha)=(1/2) sum_r r^2 r(r)`。

对 mean boundary conductance：

`G_R(L) ~ C_> D_eff(alpha) L^-1`。

对 `lambda_R''(0)` 的等级：强推断 / 可数值检验，尚非已证。若 Poisson resolvent 的边界 current 二次型受普通扩散电阻控制，则 `lambda_R''(0) ~ L^-1`。缺口是 NESS reservoir-current Green-Kubo 到电导的严格同阶证明。

### 3.2 `alpha=3/2: (log L)/L`

此时 `mu=2`，二阶矩临界发散：

`sum_{r<=L} r^2 r(r) ~ (2J0^2/gamma_phi) log L`。

有限尺度有效扩散常数候选为

`D_eff(L) ~ (J0^2/gamma_phi) log L`，

因此 mean conductance 的候选等级是

`G_R(L) ~ C_c (2J0^2/gamma_phi) (log L)/L`。

对 `lambda_R''(0)` 的等级：待验证。临界 log 最容易被 boundary contact、有限尺寸 cutoff、reservoir 实现和 subleading jump-tail 修正污染。若 Green-Kubo resolvent 捕捉同一临界二阶矩，则 `lambda_R''(0)` 也应为 `(log L)/L`；但本轮不能排除 `L^-1` 带慢 crossover 或非通用 log prefactor。

### 3.3 `1<alpha<3/2: L^{-(2alpha-2)}`

此时 `mu=2alpha-1 in (1,2)`，总跳率有限而二阶矩发散。Bernardin-Jimenez 的 boundary-driven long-jump exclusion fractional Fick law 支撑 mean reservoir conductance：

`G_R(L) ~ C_< (2J0^2/gamma_phi) L^{-(mu-1)}`

即

`G_R(L) ~ C_< (2J0^2/gamma_phi) L^{-(2alpha-2)}`。

对 `lambda_R''(0)` 的等级：强推断 / 主候选，但仍需 FCS 层验证。支持理由是 fractional hydrodynamic resistance 的主尺度已经改变；反对理由是 `lambda_R''(0)` 是 reservoir activity 与长期相关的和，不只等于 mean current 的线性响应。

本轮最终等级表：

| 区间 | mean `G_R(L)` | `lambda_R''(0)` 本轮等级 |
|---|---:|---|
| `alpha>3/2` | `L^-1` | 强推断，缺 Poisson/Green-Kubo 同阶定理 |
| `alpha=3/2` | `(log L)/L` | 待验证，临界 log 最脆弱 |
| `1<alpha<3/2` | `L^{-(2alpha-2)}` | 强推断，主候选，但非已证 |

## 4. 可执行验证路线

最小解析路线：

1. 固定有限 `L` 的 `L_s^R`。
2. 求 NESS `pi` 与 `J_R=<j_R>_pi`。
3. 解 Poisson 方程 `L phi=-(j_R-J_R)`、`<phi>_pi=0`。
4. 计算 `lambda_R''(0)=<a_R>_pi+2<(j_R-J_R),phi>_pi`。
5. 对 `alpha>3/2`、`alpha=3/2`、`1<alpha<3/2` 分别拟合 `L lambda_R''(0)`、`L lambda_R''(0)/log L`、`L^{2alpha-2} lambda_R''(0)`。

硬边界：全状态空间精确对角化只能到小 `L`。大 `L` 需要 matrix-product-like closure、linear fluctuating hydrodynamics 或 cloning/Gillespie。若没有这些数值或解析估计，不应把 `lambda_R''(0)` 与 `G_R(L)` 同标度写成定理。

## 5. 深挖1：本轮结论的下一层后果

第一层后果：若 `lambda_R''(0)` 最终确认为与 `G_R(L)` 同标度，则 R1 的 diffusive FCS 归一化 `L lambda_R(s)` 只在 `alpha>3/2` 保持自然；在 `1<alpha<3/2` 应改为 `L^{2alpha-2} lambda_R(s)`。

第二层后果：这会把 noisy free fermion 的 universality statement 从“强退相干后就是 SSEP”改成“强退相干后是由 Zeno jump kernel 二阶矩决定的 exclusion universality class”。真正的边界不在量子/经典，而在 `sum_r r^2 r(r)` 是否有限。

第三层后果：若 `lambda_R''(0)` 不同标度而 mean `G_R(L)` 仍按 fractional Fick law 标度，则 current mean 与 current variance 分属不同 universality 层级。这会产生更强的新命题：long-jump reservoirs 的 FCS mobility 不是 conductance 的简单 fluctuation-dissipation partner。

## 6. 深挖2：本轮前提中最可能出错的一项

第一层风险：最可能出错的是 endpoint-only Markovian reservoir 与 Bernardin-Jimenez infinite/exterior reservoir 的等价性。前者只在站点 `L` 注入/抽出；后者的数学边界实现可能等效于整个外部半线的 reservoir 耦合。

第二层风险：fractional Laplacian 的边界问题对实现极敏感。Dirichlet exterior condition、regional fractional Laplacian、censored jump process 与 endpoint contact 给出的边界通量可以同 bulk exponent 但不同 prefactor，也可能在临界 `alpha=3/2` 改变 log 修正。

第三层风险：即便 mean current exponent 稳定，FCS 二阶导数还依赖 reservoir activity `<a_R>_pi` 与时间相关积分的相消结构。若瞬时 activity 是 `O(1)` 而长期相关项抵消到 `G_R(L)`，则同标度证明必须控制一个精细 cancellation；这正是目前 Green-Kubo 路线的主要缺口。

硬边界：没有针对本模型 `L_s^R` 的二阶特征值扰动估计或数值谱证据前，`lambda_R''(0)` 的三段标度只能标为强候选，不可标为已证。

## §末 输出格式

本轮成果：写出了 classical long-jump exclusion 的右 reservoir-current tilted generator `L_s^R`，只 tilt 右 reservoir 注入/抽出事件，不 tilt cut-current；给出 `lambda_R''(0)` 的 Poisson/Green-Kubo 表达式，并判定其与 `G_R(L)` 同标度目前是附加假设而非已证结论。三段候选等级为 `alpha>3/2: L^-1`，`alpha=3/2: (log L)/L`，`1<alpha<3/2: L^{-(2alpha-2)}`。

新增的引用文献：Bernardin-Jimenez Oviedo arXiv:1603.01234v3 / DOI 10.30757/alea.v14-25；Bernardin-Goncalves-Oviedo Jimenez arXiv:1702.07216v2；Jara arXiv:0805.1326v2 / DOI 10.1002/cpa.20253；Bertini-De Sole-Gabrielli-Jona-Lasinio-Landim DOI 10.1023/A:1024967818899；Bertini-Landim-Mourragui DOI 10.1214/09-AOP472；Franco-Goncalves-Landim-Neumann arXiv:2203.14417v1 / DOI 10.30757/alea.v19-60；Bouley-Landim arXiv:2402.05816v1 / DOI 10.1007/s10955-024-03356-y；Derrida-Hirschberg-Sadhu arXiv:2009.04169v1 / DOI 10.1007/s10955-020-02680-3；Chetrite-Touchette DOI 10.1007/s00023-014-0375-8；Pavliotis arXiv:1002.4103；Bertini et al. MFT review DOI 10.1103/RevModPhys.87.593。

最弱的环节：从 `lambda_R''(0)=<a_R>_pi+2<(j_R-J_R),phi>_pi` 到 `G_R(L)` 同标度的 resolvent / Green-Kubo 估计；特别是临界 `alpha=3/2` 的 log 因子和 endpoint reservoir 边界实现。

下一步计划：对有限 `L` 构造 `L_s^R` 或直接解 Poisson 方程，数值比较 `lambda_R''(0)` 的三种 rescaling：`L lambda_R''(0)`、`L lambda_R''(0)/log L`、`L^{2alpha-2} lambda_R''(0)`；同时检索 fractional MFT with reservoirs / nonlocal boundary mobility 是否已有可引用定理。

需要PI投喂的文献方向：`fractional macroscopic fluctuation theory boundary reservoirs`，`long range exclusion current fluctuations reservoirs`，`tilted generator boundary driven exclusion reservoir current`，`Poisson equation additive functional exclusion process current`，`nonlocal fractional Laplacian reservoir mobility Green-Kubo`。
