# B博士 NSF-FCS-1 Round 5

## 0. 框架声明：市场微观结构 -> FDT 作为无套利 Ward identity

本轮的野路子借用 **经济学/市场微观结构**。表面上这和 free fermion transport 无关，但数学对象是同一个：

`价格冲击函数 + 订单流噪声 + 无套利对称性`

对应到物理里就是：

`线性响应 G_T + 零频二阶 cumulant lambda_T'' + time-reversal/local detailed balance`

Round 4 之后，single-particle 与 finite-density exclusion ledger 都给出

`S_T(L)=lambda_T''(0)/G_R(L) ~= 2`

这不再像一个偶然的 reservoir-capacity 标度命题，而更像 equilibrium two-terminal local detailed balance 下的有限体积 FDT/Einstein 恒等式：

`lambda_T''(0; F=0) = 2 dJ_T/dF |_{F=0}`.

因此本轮的目标不是继续重复 equilibrium symmetric gauge，而是找出这个 identity 的破坏边界。我的判断是：**真正有价值的新方向，是故意破坏 FDT 的前提，而不是换一个等价参数化。**

--- INSPECTOR_CHECK ---
[公式] 在 finite-state open Markov jump process 中，若 `F` 是无量纲 thermodynamic affinity，`J_T` 单位为 `count/time`，则 `G_T=dJ_T/dF|0` 单位为 `count/time`；tilted SCGF `lambda_T(chi)` 单位为 `1/time`，`lambda_T''(0)` 单位为 `count^2/time`。对 dimensionless count，`lambda_T''(0)=2G_T` 两边同为 `1/time`，`S_T` 无量纲。
[方向] Round 5 不再把 `S_T~=2` 当作待解释数值巧合，而把它视为 equilibrium LDB 的候选 Ward identity；新价值来自破坏其前提。
[数据] 使用 PI transport ledger 与 finite-density exclusion ledger 的摘要：两者均 valid，且 `lambda_T''` 与 `G_R` log-slope 一致、`S_T~=2`。
[假设] 当前 ledger 的默认点是 `rho0=1/2`、two-terminal equilibrium、channel-resolved transport current、local detailed balance、零频二阶 cumulant。
---

## 1. 哪些条件会破坏 `lambda_T''=2G_R`

### 1.1 非平衡密度：`rho_L != rho_R`

这是最干净的破坏条件。若基准态已经有 `rho_L != rho_R`，即使外加小 `F` 为 0，系统也处于 NESS：

`J_T(0; rho_L,rho_R) != 0`.

这时 `lambda_T''(0)` 测的是 NESS 背景输运噪声，`G_R=dJ_T/dF|0` 测的是在这个 NESS 上再施加 infinitesimal thermodynamic force 的微分响应。二者没有理由满足 equilibrium Einstein relation。

最小可执行扩展：

```text
rho_left  in {0.35, 0.45, 0.50}
rho_right in {0.50, 0.55, 0.65}
delta_rho = rho_right-rho_left
affinity_mode = two_terminal_symmetric
observable_kind = left_transport_current
report: J0, lambda_T_second_NESS, G_T_NESS, S_T_NESS=lambda_T_second_NESS/G_T_NESS
```

质量门新增：

```text
equilibrium_mode = false if |J0| > tol
FDT_residual_R2 = lambda_T_second_NESS - 2*G_T_NESS
```

会不会让二阶标度重新非平凡：**会**。固定 `delta_rho` 时，`lambda_T''` 可能由背景 shot noise / exclusion traffic 控制，`G_T` 由边界响应控制，二者可出现不同 `L` 标度。若 `delta_rho` 随 `L` 缩小到线性响应窗口，可能回到 FDT crossover，因此要同时跑 fixed `delta_rho` 与 `delta_rho ~ L^{-p}`。

### 1.2 非 symmetric affinity gauge

这里要小心：**纯 gauge 不破坏 identity。**

若仍然满足

`eta_R=aF`, `eta_L=-(1-a)F`, `eta_R-eta_L=F`,

并且每个 reservoir channel 的 rate ratio 仍满足 local detailed balance，那么 `a` 只是把同一个 total affinity 分配到左右端。用同一个 physical current 和同一个 total `F` 求导时，应仍有

`lambda_T''(0)=2 dJ_T/dF|0`.

所以 non-symmetric affinity gauge 本身主要是 **实现验错器**，不是新物理。

真正的破坏版本是把 gauge 改成 time-symmetric activity forcing，例如：

`k(e,x;nu) -> k(e,x;nu) exp(theta_nu F)`

并同时保留 thermodynamic part。`theta_nu` 改变 escape traffic，不改变正反跳的 entropy ratio；它对应市场里的“流动性/挂单深度变化”，不是价格差。此时响应含 frenetic term，`G_T` 不再只由 entropy production 生成，`lambda_T''=2G_T` 可破。

最小可执行扩展：

```text
affinity_split_a in {0.0, 0.25, 0.5, 0.75, 1.0}
activity_theta_left/right in {(0,0), (0.25,0), (0,0.25), (0.25,-0.25)}
report separately:
  thermodynamic_F = eta_R-eta_L
  activity_forcing = theta_R-theta_L or theta_R+theta_L
  FDT_residual_R2
```

会不会让二阶标度重新非平凡：纯 `affinity_split_a` **不会**，应作为 regression test；`activity_theta != 0` **会**，尤其当 activity perturbation 作用在 reservoir tails 上并带有 `L` 依赖权重时。

### 1.3 非 local detailed balance

这是比非平衡密度更硬的破坏。当前恒等式若成立，核心依赖是 channel-wise ratio：

`log[k_F(e,x;nu)/k_F(x,e;nu)] = chemical_potential_nu + constant`.

若改成

`k_F(e,x;nu)=rho_nu r_nu(x) exp(+a_nu eta_nu)`

`k_F(x,e;nu)=(1-rho_nu) r_nu(x) exp(-b_nu eta_nu)`

且 `a_nu+b_nu != 1`，或者让 `a_nu,b_nu` 随 `x` 变，则外加参数不再是纯 entropy affinity。Gallavotti-Cohen / FDT 的符号对称性被破坏。

最小可执行扩展：

```text
ldb_mode in {"local_detailed_balance", "asymmetric_kinetics", "site_dependent_kinetics"}
kappa_in_nu = a_nu
kappa_out_nu = b_nu
ldb_mismatch_nu(x)=log(k(e,x;nu)/k(x,e;nu)) - [log(rho_nu/(1-rho_nu)) + eta_nu]
report max_abs_ldb_mismatch, mean_abs_ldb_mismatch
```

会不会让二阶标度重新非平凡：**会，而且是最明确的 kill/keep 后续。** 如果 `ldb_mismatch` 是 `O(1)` 且 `FDT_residual_R2` 也有稳定非零标度，说明 Round 4/ledger 的 `S_T~=2` 不是 reservoir universality，而是 LDB identity。

### 1.4 有限频二阶噪声与高阶 cumulants

`lambda_T''` 是零频、长时间二阶 cumulant。FDT 在 equilibrium 下保护的是零频二阶噪声与 DC conductance。若改问有限频：

`S_T(omega)=<a_T>_pi + 2 Re <h_T, (i omega - L_0)^{-1} h_T>_pi`

则它应与 dynamic admittance `G_T(omega)` 配对，而不是与 `G_T(0)` 配对。因此若仍用

`S_T(omega)/G_T(0)`

就会显露 relaxation spectrum 与 long-jump reservoir 的尺度。

高阶 cumulants 更有价值。Equilibrium 二阶 FDT 不会固定：

`lambda_T'''(0)`, `lambda_T''''(0)`,

以及 nonlinear conductance：

`d^2 J_T/dF^2|0`, `d^3 J_T/dF^3|0`.

在 time reversal 对称点，某些奇阶量可能因 current 反对称而为 0；真正要看的不是单个 `lambda'''(0)`，而是 nonlinear FDT 组合是否存在新的 cancellation。

最小可执行扩展：

```text
chi_grid = {-2e-2,-1e-2,-5e-3,0,5e-3,1e-2,2e-2}
fit lambda(chi) to order 4 or 6
report lambda_3, lambda_4, rel_fit_spread
omega_grid = c / tau_mix(L), with c in {0.1,1,10}
report S_T(omega), G_T(omega) if implemented, else S_T(omega)/G_T(0) as diagnostic only
```

会不会让二阶标度重新非平凡：有限频二阶 **会**，但只有当比较对象仍是 DC `G_T(0)` 时；若同步计算 dynamic `G_T(omega)`，equilibrium FDT 可能再次平凡化。高阶 cumulants **会开新问题**，但严格说不是“二阶标度”本身，而是 NSF-FCS-1 的下一代 observable。

### 1.5 Reservoir realization dependence

如果每个 realization 仍处于 equilibrium LDB，那么 `lambda_T''=2G_T` 应对每个 realization 逐个成立，而不只是 ensemble average 成立。因此随机 reservoir tail、稀疏 reservoir、随机 couplings 本身不会破坏二阶比值；它只会让 `lambda_T''` 和 `G_T` 的共同标度同时变乱。

真正有价值的是：

```text
random reservoir realization + NESS density bias
random reservoir realization + LDB mismatch
random reservoir realization + finite-frequency noise
random reservoir realization + higher cumulants
```

最小可执行扩展：

```text
reservoir_kind = random_tail
seed in 0..Nseed-1
c_left(x), c_right(x) iid lognormal with normalized mean
report sample mean/std of G_T, lambda_T_second, S_T, FDT_residual_R2
```

会不会让二阶标度重新非平凡：equilibrium LDB 下 **不会**；与 `rho_L != rho_R` 或 `ldb_mismatch != 0` 组合后 **会**，并且可能暴露 non-self-averaging 的 rare-contact 标度。

--- INSPECTOR_CHECK ---
[公式] `FDT_residual_R2(L)=lambda_T''(0;state)-2G_T(state)`；`ldb_mismatch_nu(x)=log(k(e,x;nu)/k(x,e;nu))-[log(rho_nu/(1-rho_nu))+eta_nu]`；`S_T(omega)=<a_T>+2 Re <h_T,(i omega-L_0)^{-1}h_T>_pi`。
[方向] 非平衡基准、非 LDB、activity forcing、有限频/高阶 cumulants 是真实破坏方向；纯 affinity split 与 equilibrium random reservoir 不是破坏方向，只能做验错或与破坏项组合。
[数据] 依据当前 ledger 的 channel-resolved Markov generator 与 tilted SCGF 结构；未使用 A Round 5 文件。
[假设] `chi` 与 `F` 均无量纲；count increment 为 dimensionless；有限频公式采用 row-generator convention 的等价 resolvent 表达，实际实现需与现有 `L_0` 左/右本征向量 convention 对齐。
---

## 2. 最小可执行扩展建议

我建议 PI 不要一次性扩脚本成大机器，而是做三个层级的最小台账。

### Tier 0：FDT identity sanity ledger

目的：证明 `S_T~=2` 不是数值偶然。

新增字段：

```text
affinity_split_a
FDT_residual_R2
FDT_residual_rel = |lambda_T_second-2G_T|/max(1,|lambda_T_second|,|2G_T|)
```

扫描：

```text
rho_left=rho_right=0.5
ldb_mode=local_detailed_balance
activity_theta_left=activity_theta_right=0
affinity_split_a in {0,0.25,0.5,0.75,1}
```

预期：`FDT_residual_R2` 全部为数值零。若这里失败，说明脚本的 `F`、current convention 或 derivative 对象错了。

### Tier 1：二阶重新非平凡 ledger

目的：直接打破 equilibrium/LDB 前提。

最小扫描：

```text
case A: rho_left=0.4, rho_right=0.6, ldb_mode=local_detailed_balance
case B: rho_left=rho_right=0.5, ldb_mode=asymmetric_kinetics, a+b in {0.7,1.3}
case C: rho_left=rho_right=0.5, activity_theta_left/right != 0
L_grid same as feasible
alpha in {0.5,1.0,1.5}
```

判据：

```text
R2_slope = slope_log_abs(FDT_residual_R2)
G_slope
lambda2_slope
S_T_slope
```

若 `S_T` 出现稳定幂漂移/对数漂移，或 `lambda2_slope` 与 `G_slope` 分裂，就说明二阶问题在该扩展下重新非平凡。

### Tier 2：新 observable ledger

目的：不再执着二阶 DC FDT。

新增：

```text
lambda_3
lambda_4
finite_frequency_S_T(omega)
mixing_gap_or_tau_mix
disorder_seed if random reservoir
```

优先顺序：

1. `lambda_4/G_T` 或 `lambda_4/lambda_2` 的 `L` 标度；
2. `S_T(omega~tau_mix^{-1})/G_T(0)`；
3. random reservoir 下的 sample-to-sample variance；
4. nonlinear FDT residual，例如 `d lambda_T''/dF|0 - 2 d^2J_T/dF^2|0`，具体系数需 INSPECTOR 再校准。

## 3. 哪些方向最值得投资源

优先级排序：

1. **非平衡 `rho_L != rho_R`**：最小改动，最可能立刻让 `lambda_T''/G_T` 脱离 2，并产生新的 `L` 标度。
2. **非 local detailed balance**：最干净的反证方向，能把“FDT corollary”与“reservoir universality”分开。
3. **有限频二阶噪声**：仍是二阶，但避开 DC FDT；需要动态导纳或至少明确这是 diagnostic ratio。
4. **高阶 cumulants**：最可能成为 NSF-FCS-1 后续新命题，但不应伪装成原二阶问题。
5. **reservoir realization dependence**：单独做价值有限；必须和 NESS、非 LDB、有限频或高阶 cumulants 绑定。
6. **非 symmetric affinity gauge**：纯 gauge 不是物理破坏；只适合作为 sanity check。若加入 activity/barrier forcing，则升级为有价值方向。

## 4. 深化1：FDT identity -> cohomological Ward identity

第一层同构：市场无套利约束说，若价格冲击由同一个对称订单流生成，线性冲击和二阶波动不能独立调节。物理翻译是 equilibrium time reversal 把 response 与 current-current fluctuation 绑在一起：

`lambda_T'' = 2G_T`.

更深层结构：这不是某个 reservoir tail 的解析性质，而是 generator 上的 involution symmetry。只要 tilted generator 与 force-perturbed generator 由同一个 entropy cocycle 生成，二阶标度就被 Ward identity 锁死。此时 `D_R~Cap` 若只服务于二阶 DC ratio，价值下降；它解释 `G_T` 自身标度，而不是解释 `lambda_T''/G_T`。

再深一层：破坏 identity 的最小方式不是换 tail，而是让 perturbation 不再是 entropy cocycle：NESS density bias、LDB mismatch、activity forcing 都是在 cocycle 外加入 time-symmetric 或 nonconservative 成分。这样 `lambda_T''` 才从 Ward identity 的影子里逃出来。

## 5. 深化2：均衡市场 -> 信息不对称市场 -> 随机流动性市场

第一层推广：从均衡市场到信息不对称市场。对应物理是 `rho_L != rho_R` 的 NESS：系统已有背景流，噪声包含真实交易量，响应只是再加一小撮价格差的 marginal effect。此时 noise/response 不必同标度。

第二层推广：从信息不对称市场到随机流动性市场。对应物理是 random reservoir realization：如果仍 equilibrium LDB，每个 realization 的二阶 FDT 逐个成立；但在 NESS 或非 LDB 下，随机 contact geometry 会选择不同 bottleneck，`FDT_residual_R2` 可能非自平均。

第三层推广失败记录：若只做 random reservoir 但保持 `rho_L=rho_R`、LDB、zero-frequency second cumulant，则映射回物理后仍被 FDT 锁死，不能产生新二阶命题。因此 reservoir realization dependence 不能单独作为 Round 6 主线。

## 6. 本轮收尾格式

本轮的跨学科跳跃：`经济学/市场微观结构 -> 无套利价格冲击 identity -> equilibrium FDT/Einstein identity`

这个结构的数学对象：`time-reversal involution, entropy cocycle, local detailed balance, tilted SCGF Ward identity, frenetic/activity perturbation`

如果这个同构成立，最奇怪的可检验预测是：`在 equilibrium LDB 下，非 symmetric affinity split 与 random reservoir realization 都不能破坏 lambda_T''/G_T=2；只有 NESS、非 LDB、activity forcing、有限频或高阶 cumulants 才能开新问题。`

A博士最可能反对的点：`这已经是标准 FDT 语言，不够野。B 的回答是：野路子价值不在重证 FDT，而在明确哪些看似新方向其实被 FDT 锁死，从而逼 PI 把资源投到破坏条件上。`

本轮失败记录：`纯 non-symmetric affinity gauge 不是破坏条件；equilibrium random reservoir 不是破坏条件；zero-frequency second cumulant 在 LDB equilibrium 下大概率已降级为 FDT corollary。`

下一步计划：`先做 Tier 0 affinity split sanity，再做 Tier 1 rho_L!=rho_R 与 non-LDB ledger；若 R2=lambda_T''-2G_T 出现稳定标度，再把该扩展升为 NSF-FCS-1 的新版本。`

需要PI投喂的文献方向：`nonequilibrium fluctuation-dissipation Markov jump process`, `frenetic contribution linear response`, `local detailed balance violation current noise`, `finite frequency noise exclusion process`, `nonlinear fluctuation-dissipation higher cumulants`
