# LP18 Round 3 - A博士：reservoir-current / boundary conductance scaling

角色：A博士（学院派）。本轮只固定一个 observable：右端 reservoir current 的二阶导数 `lambda_R''(0)`，等价地在小化学势差/小密度差线性响应下的 boundary conductance。本文不把结论泛化到所有 cut-current；长跳模型中 cut-current 与 reservoir current 不再由最近邻连续性自动等价。

## §-1 先发文献检索

检索工具：paper-search-mcp。检索时间：2026-06-03。

### 检索组1：boundary-driven long-jump exclusion / fractional Fick law

命中：
- Cedric Bernardin, Byron Jimenez Oviedo, "Fractional Fick's law for the boundary driven exclusion process with long jumps", arXiv:1603.01234v3 / ALEA 14, 473 (2017), DOI 10.30757/alea.v14-25。
- Cedric Bernardin, Patricia Goncalves, Byron Oviedo Jimenez, "Slow to fast infinitely extended reservoirs for the symmetric exclusion process with long jumps", arXiv:1702.07216v2。

用途：第一篇直接给出一维 boundary-driven long-jump exclusion 在左右 infinite reservoirs 下的 fractional hydrostatics 与 fractional Fick law。它是本轮 reservoir-current/boundary-conductance 标度的主文献，不是 cut-current 的任意定义。第二篇说明 reservoir 强度和边界实现会改变边界条件，因此本轮必须把结论限定在匹配的 boundary-driven reservoir current。

### 检索组2：long-jump exclusion hydrodynamics / fractional Laplacian

命中：
- Milton Jara, "Hydrodynamic limit of particle systems with long jumps", arXiv:0805.1326v2；相关期刊版本：Commun. Pure Appl. Math. 62, 198-214 (2009), DOI 10.1002/cpa.20253。

用途：证明 long-jump exclusion / zero-range 的 hydrodynamic limit 是 fractional heat equation，且 scaling 是 superdiffusive。该文献支撑 `p(r) ~ |r|^{-(1+mu)}` 时 `0<mu<2` 进入 fractional Laplacian，而不是普通 Laplacian。

### 检索组3：fluctuations / current variance 背景

命中：
- Patricia Goncalves, Milton Jara, "Density fluctuations for exclusion processes with long jumps", arXiv:1503.05838v3 / Probab. Theory Relat. Fields 170, 311-362 (2018), DOI 10.1007/s00440-017-0758-0。
- Cedric Bernardin, Patricia Goncalves, Milton Jara, Stefano Scotta, "Equilibrium fluctuations for diffusive symmetric exclusion with long jumps and infinitely extended reservoirs", arXiv:2002.12841v2 / Ann. Inst. Henri Poincare Probab. Stat. 58 (2022), DOI 10.1214/21-AIHP1176。

用途：这些文献支持长跳排斥过程的密度 fluctuation 场会进入非局域/fractional OU 类型；但它们并不直接给出本项目所需的 nonequilibrium reservoir-current `lambda_R''(0)` 全标度定理。因此二阶 current variance 的严格状态要比平均 boundary conductance 更弱。

### 检索组4：量子长程 hopping + dephasing 背景

沿用 Round 2 已定位文献：
- Subhajit Sarkar, Bijay Kumar Agarwalla, Devendra Singh Bhakuni, "Impact of dephasing on non-equilibrium steady-state transport in fermionic chains with long-range hopping", arXiv:2310.01323v2 / Phys. Rev. B 109, 165408 (2024), DOI 10.1103/PhysRevB.109.165408。

用途：该文报告退相干长程自由费米链在 `alpha_c approx 1.5` 附近出现从 diffusive 到 superdiffusive 的数值边界。本文不把该数值结果当作证明，只把它作为与 Zeno-projected long-jump exclusion 标度一致的独立物理证据。

## §0 框架声明

成熟框架：strong-dephasing / Zeno projection + classical boundary-driven long-jump exclusion + fractional Fick law。

本轮继承 Round 2 的有效经典核：

`r_{jk}=2|J_{jk}|^2/gamma_phi`

其中 `J_{jk}` 与 `gamma_phi` 均取角频率单位 `s^{-1}`，所以 `r_{jk}` 单位为 `s^{-1}`。对一维 power-law hopping

`J(r)=J0 |r|^{-alpha}`

得到

`r(r)=2J0^2/(gamma_phi |r|^{2alpha})`。

把经典长跳排斥文献的跳核写成

`p(r) ~ |r|^{-(1+mu)}`，

则本项目参数对应

`mu = 2alpha - 1`。

本轮 observable 固定为右 reservoir 注入/抽出粒子的累计电荷

`Q_R(t) = N_R(t)-N_R(0)`

及其长时 CGF

`lambda_R(s)=lim_{t->infty} t^{-1} log E[exp(s Q_R(t))]`。

`lambda_R''(0)` 是单位时间 reservoir-current variance，SI 单位为 `s^{-1}`。在线性响应和排斥迁移率有限的假设下，它与 boundary conductance 同标度；但这一步对 nonequilibrium current noise 仍需要单独验证。

## 1. 从 fractional Fick law 提取 reservoir conductance 标度

Bernardin-Jimenez 的模型是左右 reservoirs 直接驱动的一维 long-jump exclusion。该模型的主结论可以用于 reservoir current/boundary conductance，而不是任意 cut-current。对 `p(r) ~ |r|^{-(1+mu)}` 且 `1<mu<2` 的 superdiffusive 区间，fractional Fick law 给出的 stationary current 标度是

`J_R(L) ~ const(mu, reservoirs) (rho_L-rho_R) L^{-(mu-1)}`。

把 `mu=2alpha-1` 代入，得到

`J_R(L)/(rho_L-rho_R) ~ C_alpha (2J0^2/gamma_phi) L^{-(2alpha-2)}`,  `1<alpha<3/2`。

这里 `C_alpha` 是无量纲常数，依赖长跳核归一化、reservoir 实现和边界条件；`2J0^2/gamma_phi` 给出速率前因子。

因此，对本轮固定的 boundary conductance：

`G_R(L) := partial J_R / partial(rho_L-rho_R)`

有强文献支撑的标度

`G_R(L) ~ C_alpha (2J0^2/gamma_phi) L^{-(2alpha-2)}`, `1<alpha<3/2`。

若进一步假设 Einstein/Green-Kubo 型关系在该 boundary-driven long-jump exclusion 的稳态二阶 reservoir current fluctuation 中保持同一 `L` 标度，则

`lambda_R''(0) ~ C_alpha^noise (2J0^2/gamma_phi) L^{-(2alpha-2)}`。

但最后这句是对 `lambda_R''(0)` 的强推断，不是 Bernardin-Jimenez 论文已经逐字证明的 full counting statistics 结论。

--- INSPECTOR_CHECK ---
[公式] `G_R(L) ~ C_alpha (2J0^2/gamma_phi) L^{-(2alpha-2)}` for `1<alpha<3/2`；`G_R` 与 `lambda_R''(0)` 的单位均按单位时间计，为 `s^{-1}`，`L` 以晶格间距为单位无量纲。
[方向] fractional Fick law 支持 reservoir boundary conductance 的超扩散增强：`alpha` 从 `3/2` 降到 `1` 时，conductance 衰减指数从 `1` 降到 `0`。
[数据] Bernardin-Jimenez arXiv:1603.01234v3 / DOI 10.30757/alea.v14-25；Jara arXiv:0805.1326v2 / DOI 10.1002/cpa.20253；Round 2 的 Zeno projection `r_{jk}=2|J_{jk}|^2/gamma_phi`。
[假设] reservoir 实现匹配 boundary-driven long-jump exclusion；`alpha>1` 使 `sum_r |J(r)|` 收敛，Zeno projection 在热力学极限前后可控；`lambda_R''(0)` 与 conductance 同标度是 fluctuation 层面的附加假设。

## 2. 三个候选标度的判定

### 2.1 `alpha>3/2: L^-1`

已知链条：

`alpha>3/2` 等价于 Zeno-projected jump kernel 的二阶矩有限：

`sum_r r^2 r(r) ~ sum_r r^{2-2alpha} < infinity`。

有限二阶矩意味着 hydrodynamic generator 回到普通 Laplacian 的 domain of attraction。有效扩散常数为

`D_eff(alpha) = (1/2) sum_r r^2 r(r) = (J0^2/gamma_phi) sum_{r>=1} r^{2-2alpha}`。

因此 classical boundary conductance 的自然标度为

`G_R(L) ~ C_D D_eff(alpha) L^{-1}`。

判定：
- 对经典 long-jump exclusion 的 boundary conductance：强推断，接近已证。有限二阶矩长跳核的 hydrodynamics 是普通扩散，且 boundary-driven exclusion 的 Fick law 框架成熟；但本轮检索到的主 fractional Fick law 文献重点是 `1<mu<2` 的分数区间。
- 对原始强退相干自由费米链：强推断。它还依赖 Zeno projection 的均匀有效性。
- 对 `lambda_R''(0)`：强推断。平均 current/conductance 的 `L^-1` 比二阶 FCS 更稳固。

注意临界靠近 `alpha=3/2+` 时

`D_eff(alpha) ~ 1/(2alpha-3)`，

所以有限 `L` 会有很宽 crossover；数值上不应把这误判为真正偏离 `L^-1` 的新相。

### 2.2 `alpha=3/2: (log L)/L`

临界点对应 `mu=2`，截断二阶矩为

`M_2(L) ~ sum_{r<=L} r^{-1} ~ log L`。

如果把 finite-size 截断的扩散常数写成 `D_eff(L) ~ (2J0^2/gamma_phi) log L`，则普通 Fick conductance 给出候选

`G_R(L) ~ C_c (2J0^2/gamma_phi) (log L)/L`。

判定：
- 对 classical boundary conductance：强推断，但不是本轮可称的已证。它由临界二阶矩截断和 Fick law 拼接得到；需要查找或证明 `mu=2` 边界情形的 reservoir Fick law。
- 对原始强退相干自由费米链：待验证到强推断之间；我建议标为待验证，因为这里最容易受有限 `gamma`、finite-size cutoff、reservoir 实现影响。
- 对 `lambda_R''(0)`：待验证。二阶 current noise 是否继承同一临界 log，需要专门 tilted generator 或 Green-Kubo 估计。

### 2.3 `1<alpha<3/2: L^{-(2alpha-2)}`

此时 `mu=2alpha-1 in (1,2)`，总跳率有限、二阶矩发散，且 `sum_r |J(r)|` 对 `alpha>1` 收敛。该区间正好避开 Round 2 指出的最大 Zeno 风险 `alpha<=1`。

fractional Fick law 文献直接支持 boundary-driven long-jump exclusion 的平均 current / conductance 标度

`G_R(L) ~ C_alpha (2J0^2/gamma_phi) L^{-(mu-1)} = C_alpha (2J0^2/gamma_phi) L^{-(2alpha-2)}`。

判定：
- 对匹配的 classical boundary-driven long-jump exclusion 的 reservoir conductance：已证/强文献支撑。若严格说“已证”，限定词必须包括模型的 reservoir 实现和 `p(r)~|r|^{-(1+mu)}` 的正规假设。
- 对原始强退相干自由费米链的 reservoir conductance：强推断。缺口是 Zeno projection 与 thermodynamic limit 的均匀交换。
- 对 `lambda_R''(0)`：强推断，不是已证。density fluctuations 文献支持非局域 fluctuation 场，但还没有直接替代 `lambda_R''(0)` 的 nonequilibrium FCS 定理。

## 3. 最小可判定命题

我建议把 LP18 的 Round 3 后命题写成以下可检验形式：

给定一维开链、端点 Markovian reservoirs、局域退相干 `gamma_phi sum_j D[n_j]`，以及未 Kac 归一化的 power-law hopping `J_{jk}=J0 |j-k|^{-alpha}`。在 `gamma_phi >> ||h_L||` 的 Zeno 窗口内，右 reservoir current 的 boundary conductance 标度为

`G_R(L) = partial_s lambda_R'(s)|_{s=0, rho_L-rho_R small}`

并满足候选分段：

`G_R(L) ~ (2J0^2/gamma_phi) x`

其中

`x = C_> L^{-1}` for `alpha>3/2`,

`x = C_c (log L)/L` for `alpha=3/2`,

`x = C_< L^{-(2alpha-2)}` for `1<alpha<3/2`。

若在稳态 current FCS 中 mobility 与 conductance 同标度，则

`lambda_R''(0)` obeys the same `L` powers。

这就是本轮的核心：conductance 标度比 full FCS 标度更有文献支撑；`lambda_R''(0)` 应作为下一步数值/解析验证对象，而不是在本轮直接宣称已证。

## 4. 与 R1 universality 的关系

R1 的普通 SSEP/QSSEP leading CGF 对应 `lambda_R''(0) ~ const/L`。Round 3 的结果表明它的真正适用条件不应只写成“free fermion + dephasing + large L”，而应加入：

`Zeno-projected exclusion jump kernel has finite second moment`。

对 `J(r)~r^{-alpha}`，这等价于 `alpha>3/2`。当 `1<alpha<3/2` 时，强退相干投影并没有把模型送回普通 SSEP，而是送到 fractional long-jump exclusion；普通 SSEP 的 `L^-1` conductance 不是 leading 标度。

这也是为什么本轮坚持 reservoir current：R1 的 reservoir counting field 是明确定义的；长跳模型中局部 cut-current 的定义可能涉及跨 cut 的所有 jump，与 reservoir current 的 FCS 不必相同。

## 5. 深挖1：本轮结论的下一层后果

第一层后果：若 `1<alpha<3/2` 的 reservoir conductance 确为 `L^{-(2alpha-2)}`，则 R1 的 rescaled CGF 变量 `tilde lambda ~ L lambda` 在 fractional 区间不是自然归一化。自然归一化应随 `L^{2alpha-2}` 或 `L^{mu-1}` 改变。

第二层后果：这会改变 finite-size quantum correction 的相对阶数。R7/QSSEP 中的 quantum correction 在普通 diffusive 标度下是 subleading `O(1/L)`；若 leading conductance 本身变成 `L^{-(2alpha-2)}`，则某些 coherence-loop correction 相对 leading 的阶数可能从 `L^{-1}` 改成 `L^{-(?)} / L^{-(2alpha-2)}`，在 `alpha` 接近 `1` 时可能被放大。

第三层后果：因此真正可发表的后续问题不是“长程 hopping 是否破坏 universality”这个宽泛说法，而是“finite-size quantum correction 在 fractional conductance scaling 下是否仍 subleading”。这可以用原始 correlation-matrix tilted Lindblad 数值直接测 `lambda_R''(0)` 和 Zeno classical prediction 的比值。

## 6. 深挖2：本轮前提中最可能出错的一项

第一层风险：最可能出错的是把 Bernardin-Jimenez 的 infinite-reservoir boundary-driven long-jump exclusion 直接等同于原始量子链的端点 Markovian reservoirs。长跳 bulk 允许远距离跨越，但端点 reservoir 只在边界站点注入/抽出；这可能和数学文献中的外部 reservoir 耦合不完全相同。

第二层风险：如果 reservoir 实现不同，mean profile 和 reservoir current 的 prefactor 甚至边界指数可能改变，尤其在 fractional Laplacian 的非局域边界问题中，Dirichlet exterior condition、regional fractional Laplacian、censored process 的边界通量定义并不等价。

第三层风险与硬边界：在 `1<alpha<3/2` 区间，bulk fractional exponent `2alpha-2` 很稳，但 reservoir current 的严格 FCS 需要 microscopic tilted generator 明确写出。硬边界是：没有这个 tilted generator 或直接数值验证前，`lambda_R''(0)` 只能标为强推断；只有 boundary conductance/平均 reservoir current 可以借 fractional Fick law 作为已证或强文献支撑。

## §末 输出格式

本轮成果：固定 observable 为右 reservoir current / boundary conductance；由 Zeno-projected `J(r)~r^{-alpha}` 得到 classical long-jump kernel `r(r)=2J0^2/(gamma_phi r^{2alpha})`，对应 `mu=2alpha-1`。对 boundary conductance，`1<alpha<3/2` 的 `L^{-(2alpha-2)}` 有 fractional Fick law 强文献支撑；`alpha>3/2` 的 `L^-1` 是有限二阶矩普通扩散强推断；`alpha=3/2` 的 `(log L)/L` 是临界二阶矩截断给出的待验证/强推断候选。对 `lambda_R''(0)`，三者均需额外 FCS 或 Green-Kubo 验证，其中 `1<alpha<3/2` 和 `alpha>3/2` 可作为强推断，临界 log 标为待验证。

新增的引用文献：
- Bernardin, Jimenez Oviedo, arXiv:1603.01234v3 / ALEA 14, 473 (2017), DOI 10.30757/alea.v14-25。
- Bernardin, Goncalves, Oviedo Jimenez, arXiv:1702.07216v2。
- Jara, arXiv:0805.1326v2 / Commun. Pure Appl. Math. 62, 198-214 (2009), DOI 10.1002/cpa.20253。
- Goncalves, Jara, arXiv:1503.05838v3 / Probab. Theory Relat. Fields 170, 311-362 (2018), DOI 10.1007/s00440-017-0758-0。
- Bernardin, Goncalves, Jara, Scotta, arXiv:2002.12841v2 / Ann. Inst. Henri Poincare Probab. Stat. 58 (2022), DOI 10.1214/21-AIHP1176。
- Sarkar, Agarwalla, Bhakuni, arXiv:2310.01323v2 / Phys. Rev. B 109, 165408 (2024), DOI 10.1103/PhysRevB.109.165408。

最弱的环节：从 classical boundary conductance 的 fractional Fick law 推到 nonequilibrium reservoir-current variance `lambda_R''(0)` 的同标度；该步目前是强推断而非已证，尤其 `alpha=3/2` 的 `(log L)/L` 需要单独验证。

下一步计划：写出 Zeno classical long-jump exclusion 的右 reservoir tilted generator，只 tilt reservoir 注入/抽出事件，不 tilt cut-current；用线性响应或 Poisson 方程计算 `lambda_R''(0)` 的 `L` 标度，并数值比较 `alpha>3/2`、`alpha=3/2`、`1<alpha<3/2` 三段。

需要PI投喂的文献方向：`boundary driven long jump exclusion current fluctuations`, `fractional Fick law current variance`, `fractional macroscopic fluctuation theory reservoirs`, `tilted generator long jump exclusion reservoirs`, `Green-Kubo fractional exclusion boundary current`。
