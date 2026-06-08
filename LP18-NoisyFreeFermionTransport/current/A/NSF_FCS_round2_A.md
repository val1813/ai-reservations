# NSF-FCS-1 Round 2 - A博士（学院派，修正版）

角色：A博士（学院派）。本轮只修正 classical long-jump exclusion 的右 reservoir jump-current FCS 二阶公式；不读取、不使用 B 的 Round 2 产出。写入范围仅限本文件。

## §-1 先发文献检索

检索工具：paper-search-mcp。检索时间：2026-06-03。修正依据仍是 Round 2 已检索文献，不新增外部假设。

### 检索组1：additive functional CLT / H_-1 norm

命中：

- C. Kipnis, S. R. S. Varadhan, "Central limit theorem for additive functionals of reversible Markov processes and applications to simple exclusions", Commun. Math. Phys. 104, 1-19 (1986), DOI 10.1007/BF01210789。
- Claude Kipnis, Claudio Landim, "Scaling Limits of Interacting Particle Systems", Springer (1999), DOI 10.1007/978-3-662-03752-2。
- Sunder Sethuraman, "Central limit theorems for additive functionals of the simple exclusion process", Ann. Probab. 28 (2000), DOI 10.1214/aop/1019160120。

用途：这些文献给出 additive functional 的 Poisson equation / `H_-1` 框架。但本项目的 observable 是 jump-current，不是纯时间积分 `int g(eta_t) dt`。因此不能直接把 jump-current FCS 的二阶项写成 `+2<g,(-L)^-1g>`。

### 检索组2：non-gradient method / current replacement

命中：

- Kipnis-Landim, DOI 10.1007/978-3-662-03752-2；nongradient hydrodynamic limit 章节。
- C. Landim, J. Quastel, M. Salmhofer, H.-T. Yau, "Superdiffusivity of Asymmetric Exclusion Process in Dimensions One and Two", DOI 10.1007/s00220-003-1020-4。
- Sunder Sethuraman, S. R. S. Varadhan, Horng-Tzer Yau, "Diffusive limit of a tagged particle in asymmetric simple exclusion processes", DOI 10.1002/1097-0312(200008)53:8<972::AID-CPA2>3.0.CO;2-#。

用途：non-gradient method 仍可用于控制边界 current 的 Poisson 解和误差项，但修正后要控制的是完整 martingale-Poisson 方差，而不是单独的正 `H_-1` 项。

### 检索组3：fractional Dirichlet form / long-jump reservoirs

命中：

- Milton Jara, "Hydrodynamic limit of particle systems with long jumps", arXiv:0805.1326, DOI 10.1002/cpa.20253。
- C. Bernardin, B. Jimenez Oviedo, "Fractional Fick's law for the boundary driven exclusion process with long jumps", arXiv:1603.01234, DOI 10.30757/alea.v14-25。
- Patrícia Gonçalves, "Hydrodynamics for symmetric exclusion in contact with reservoirs", arXiv:1803.11460。
- Cédric Bernardin, Pedro Cardoso, Patrícia Gonçalves, Stefano Scotta, "Hydrodynamic limit for a boundary driven super-diffusive symmetric exclusion", arXiv:2007.01621, DOI 10.1016/j.spa.2023.08.002。

用途：这些文献支撑 mean conductance 的 fractional Dirichlet/capacity 标度，但不直接给出 reservoir jump-current FCS 二阶方差。

### 检索组4：boundary current variance / open exclusion FCS

命中：

- B. Derrida, B. Doucot, P.-E. Roche, "Current Fluctuations in the One-Dimensional Symmetric Exclusion Process with Open Boundaries", DOI 10.1023/B:JOSS.0000022379.95508.B2。
- Dirk Erhard, Tertuliano Franco, Tiecheng Xu, "Nonequilibrium joint fluctuations for current and occupation time in the symmetric exclusion process", DOI 10.1214/24-EJP1137。
- Bernard Derrida, Ori Hirschberg, Tridib Sadhu, "Large deviations in the symmetric simple exclusion process with slow boundaries", arXiv:2009.04169, DOI 10.1007/s10955-020-02680-3。

用途：open exclusion 的 current FCS 是成熟问题；它们支持本轮修正判断：jump-current variance 必须从 tilted generator 或 martingale-Poisson decomposition 推导，不能把 additive functional 的 `H_-1` 正项直接套用到 jump-current。

## §0 框架声明

使用有限状态 Markov jump process。未倾斜 generator 作用在函数上：

`(L f)(eta)=sum_z c(eta,z)[f(eta^z)-f(eta)]`

右 reservoir current 的单跳增量记为 `q_R(eta,z)`，注入 `+1`，抽出 `-1`，其他跳 `0`。右 reservoir tilted generator 取 Round 1 约定：

`(L_s f)(eta)=sum_z c(eta,z)[exp(s q_R(eta,z)) f(eta^z)-f(eta)]`

定义：

- `b(eta)=L'_0 1=sum_z c(eta,z) q_R(eta,z)`，单位 `s^-1`。
- `a(eta)=L''_0 1=sum_z c(eta,z) q_R(eta,z)^2`，单位 `s^-1`。
- `J=<b>_pi`。
- `h=b-J`。
- `B f=L'_0 f=sum_z c(eta,z) q_R(eta,z) f(eta^z)`。

Poisson equation 采用本文件固定约定：

`L phi = -h`, `<phi>_pi=0`

等价地，若写 `-L phi=h`，同一个 `phi`。注意：`phi` 无量纲，因为 `h` 和 `L` 都有 `s^-1` 单位。

## 1. 完整 tilted-generator 二阶扰动公式

令 `r_s=1+s phi+O(s^2)` 为 principal right eigenvector，`lambda(s)=s J + s^2 lambda''(0)/2+O(s^3)`。代入

`L_s r_s = lambda(s) r_s`

一阶给出：

`L phi + L'_0 1 = J`

即

`L phi = -(b-J)=-h`。

二阶对左稳态 `pi` 取平均，利用 `<L f>_pi=0`：

`lambda''(0)=<L''_0 1>_pi + 2 <L'_0 phi>_pi`

因此 jump-current 的正确公式是

`lambda_R''(0)=<a>_pi + 2 <B phi>_pi`, 其中 `L phi=-h`。

展开成 martingale-Poisson 形式更能看清符号。令

`C(eta)=sum_z c(eta,z) q_R(eta,z)[phi(eta^z)-phi(eta)]`

则 `B phi = b phi + C`，且 `<b phi>_pi=<h phi>_pi`。由于 `L phi=-h`，在可逆情形 `-<phi,L phi>=<phi,h>` 是正 `H_-1` 量。但 jump-current 方差为

`lambda_R''(0)=<a>_pi + 2<h,phi>_pi + 2<C>_pi`

不是 `lambda_R''(0)=<a>_pi+2<h,phi>_pi`。交叉变差 `2<C>_pi` 可以为负，并可与 `<a>`、`2<h,phi>` 发生抵消。

### 1.1 两态交替链校验

取两态链 `0 <-> 1`，两方向 rate 都为 `c`。把 `0->1` 记为 `q=+1`，`1->0` 记为 `q=-1`。则长时净 current `Q(t)` 只等于终态与初态差，故 `lambda''(0)=0`。

直接算：

- `pi(0)=pi(1)=1/2`。
- `b(0)=c`，`b(1)=-c`，`J=0`，`h=b`。
- `a(0)=a(1)=c`，所以 `<a>=c`。
- 解 `L phi=-h` 得 `phi(0)=1/2`，`phi(1)=-1/2`。
- `B phi(0)=c phi(1)=-c/2`，`B phi(1)=(-c) phi(0)=-c/2`，所以 `<B phi>=-c/2`。

于是

`lambda''(0)=c+2(-c/2)=0`

正确。若误写为 `<a>+2<h,phi>`，则 `<h,phi>=c/2`，得到 `2c`，与精确结果矛盾。这正是 INSPECTOR 阻断指出的问题。

### 1.2 Poisson process 极限校验

若只有单态 Poisson 计数过程，rate `c`，每跳 `q=+1`。则 `b=J=c`，`h=0`，`phi=0`，`a=c`。公式给出

`lambda''(0)=<a>+2<B phi>=c`

与 Poisson SCGF `lambda(s)=c(e^s-1)` 的二阶导数一致。

--- INSPECTOR_CHECK ---
[公式] 固定约定 `L phi=-h`、`h=b-J`、`B=L'_0`。正确二阶式为 `lambda_R''(0)=<a>_pi+2<B phi>_pi`，等价于 `<a>_pi+2<h,phi>_pi+2<C>_pi`，其中 `C=sum_z c q_R[phi(eta^z)-phi(eta)]`。`lambda_R''`、`<a>`、`<B phi>`、`<h,phi>`、`<C>` 单位均为 `s^-1`。
[方向] 修正了 Round 2 阻断：jump-current FCS 的二阶项不是单纯正 `H_-1` 二次型；若出现与 activity 的 `O(1)` cancellation，来源是完整公式中的 `2<B phi>` 或 martingale 交叉变差项。
[数据] tilted-generator perturbation；两态交替链校验给 `lambda''=0`；单态 Poisson 校验给 `lambda''=c`。
[假设] finite-state principal eigenvalue 可二阶扰动；`pi` 是 `s=0` 稳态；`phi` 以 `<phi>_pi=0` 固定常数。

## 2. 对 H_-1 说法的修正

纯 additive functional `int_0^t h(eta_s) ds` 的渐近方差二阶项是

`2<h,phi>_pi = 2<h,(-L)^-1 h>_pi`

在 reversible 情形为正 `H_-1` norm。但 reservoir jump-current 是

`Q_R(t)-Jt = M_Q(t) + int_0^t h(eta_s) ds`

用 `L phi=-h` 后，

`int_0^t h(eta_s) ds = phi(eta_0)-phi(eta_t)+M_phi(t)`

所以长期方差来自 martingale `M_Q+M_phi` 的 quadratic variation：

`lambda_R''(0)=lim t^-1 E[<M_Q+M_phi>_t]`

即

`<a> + <Gamma phi> + 2<C>`

其中 `<Gamma phi>=2<h,phi>` 在稳态下成立，而 `2<C>` 是 jump-current martingale 与 Poisson martingale 的交叉项。这个交叉项正是抵消机制的合法来源。

因此本文件修正如下：

1. 不再声称 `lambda_R''` 有正的 `+2||h||_{-1}^2` 上界。
2. `||h||_{-1}^2` 只控制 Poisson 解 `phi` 的能量和 martingale correction 的大小。
3. 若要证明 `lambda_R''=O(G_R(L))`，必须控制完整表达式 `<a>+2<B phi>`，特别是 `O(1)` activity 与交叉项的 cancellation。

## 3. 可证上界的正确版本

从非负方差只能得

`lambda_R''(0)>=0`。

对上界，可用 martingale-Poisson 分解与 Cauchy-Schwarz，而不是把 `2<h,phi>` 当成 `lambda''` 的正加项。设 jump rates 有界，`|q_R|<=1`。有

`|<B phi>| <= <a>_pi^{1/2} <sum_z c q_R^2 phi(eta^z)^2>_pi^{1/2}`

这类 bound 仍需要控制边界跳后 `phi` 的二阶矩。更实用的粗上界来自

`lambda_R'' <= 2 lim t^-1 E[M_Q(t)^2] + 2 lim t^-1 E[M_phi(t)^2]`

即

`lambda_R'' <= 2<a>_pi + 2<Gamma phi>_pi`

而 `<Gamma phi>_pi=2<h,phi>_pi`。若可用 sector condition 把非可逆解与 symmetric part 比较，则

`<h,phi>_pi <= C_sec <h,(-S)^-1h>_pi`。

因此保守上界是

`lambda_R''(0) <= 2<a>_pi + 4 C_sec ||h||_{-1,S,L}^2`

而不是旧稿中的

`<a>+2 C_sec ||h||_{-1,S,L}^2`。

在有 spectral gap 下界 `gap_L` 时，

`||h||_{-1,S,L}^2 <= Var_pi(h)/gap_L`

所以

`lambda_R''(0) <= 2<a>_pi + 4 C_sec Var_pi(h)/gap_L`。

重要标注：这里的 `gap_L` 标度

- `alpha>3/2`: 预期 `gap_L >= c L^-2`。
- `alpha=3/2`: 预期 `gap_L >= c (log L) L^-2`。
- `1<alpha<3/2`: 预期 `gap_L >= c L^{-(2alpha-1)}`。

这些 gap 下界在本文件中未证明；需要引用或另证 long-jump exclusion with reservoirs 的有限体积 spectral gap。没有该引用/证明时，spectral-gap 上界只能作为 conditional bound。

## 4. continuous trace 变分式与单位修正

fractional hydrodynamic Dirichlet form 的连续版本可写为

`E_mu(u,u)=D_mu int_0^1 int_0^1 (u(x)-u(y))^2/|x-y|^{1+mu} dx dy + E_bd(u,u)`

若 `x` 是无量纲宏观坐标，则 `D_mu` 带有宏观时间标度下的速率单位。若回到 microscopic time，前面还要乘相应的 `L` 标度因子。旧稿写

`sup_f {2 f(1)-E_mu(f,f)-boundary_mass(f)}`

单位不完整。正确写法必须先指定与边界 observable 配对的有单位线性泛函 `ell_R(u)`，例如线性响应下的 boundary density trace：

`ell_R(u)=kappa_R [u(1)-rho_R]`

其单位为 `s^-1`。对应的连续 `H_-1` 型控制应写成

`||ell_R||_{E_mu,*}^2 = sup_u { 2 ell_R(u) - E_mu(u,u) }`

其中 `E_mu(u,u)` 必须与 `ell_R(u)` 同为 `s^-1`，这要求已固定 microscopic-to-macroscopic time normalization。若没有这个 normalization，只能比较 `L` 指数，不能比较 prefactor 或 SI 单位。

## 5. 与 boundary conductance 的绑定状态

修正后，boundary conductance 绑定问题变成：

能否证明完整 jump-current 方差

`<a>_pi + 2<B phi>_pi`

与 fractional conductance `G_R(L)` 同标度，而不是证明正 `H_-1` norm 与 `G_R(L)` 同标度。

目前可说：

1. `||h||_{-1}` 的 fractional trace bound 仍然有用，因为它控制 Poisson corrector `phi`。
2. 但 `||h||_{-1}=O(G_R)` 本身既不是必要条件，也不是充分条件；真正需要的是 activity 与 cross term 的组合估计。
3. 若数值发现 `<a>=O(1)`、`2<B phi>=-O(1)+O(G_R)`，则 `lambda''=O(G_R)` 的 cancellation 是真实 jump-current 机制。
4. 若 `2<B phi>` 不抵消 `<a>`，则 endpoint reservoir jump-current variance 可能是 `O(1)`，不与 conductance 同标度。

因此三段标度仍降级为待验证候选：

| 区间 | `G_R(L)` | `lambda_R''(0)` 修正后状态 |
|---|---:|---|
| `alpha>3/2` | `L^-1` | 需证明 `<a>+2<B phi>` 的 cancellation 到 `L^-1` |
| `alpha=3/2` | `(log L)/L` | 需证明 cancellation 后保留临界 log |
| `1<alpha<3/2` | `L^{-(2alpha-2)}` | 需 fractional trace + martingale cross-term 组合估计 |

## 6. 深挖1：本轮修正的下一层后果

第一层后果：NSF-FCS-1 的主命题必须从“`H_-1` 正二次型同标度”改成“jump-current martingale-Poisson 方差同标度”。这把目标从单个正变分问题改成带符号的组合恒等式。

第二层后果：数值验证必须输出四项，而不是两项：

- `<a>_pi`
- `2<h,phi>_pi`
- `2<C>_pi`
- `<a>_pi+2<h,phi>_pi+2<C>_pi`

只看 `2<h,phi>` 会误判 FCS variance；两态交替链已经说明正 `H_-1` 项可以非零，而真实 net current variance 为零。

第三层后果：若同标度最终成立，它不是普通 fluctuation-dissipation 的直接结果，而是一个更强的 boundary current cancellation statement。它可能比 fractional Fick law 更难，也更有研究价值。

硬边界：在证明或数值确认 `<a>+2<B phi>` 的组合标度前，不能写 `lambda_R'' ~ G_R`。

## 7. 深挖2：本轮前提中最可能出错的一项

第一层风险：最可能出错的是把 reservoir jump-current 当作纯 additive functional。纯 additive functional 的 `H_-1` 正项和 jump-current 的 tilted-generator 二阶项只在特殊情形重合；一般不重合。

第二层风险：endpoint reservoir 的 activity `<a>` 是本地翻转尝试率，通常 `O(1)`；conductance 是跨系统响应，通常随 `L` 衰减。若要同标度，必须有精确负交叉项。这个事实使 endpoint reservoir FCS 对边界实现极其敏感。

第三层风险：fractional trace estimate 即便成立，也只控制 `phi` 的大小；它不自动控制 `B phi` 与 `<a>` 的符号匹配。符号匹配来自 microscopic jump orientation 与 Poisson corrector 的边界值，必须单独校验。

硬边界：Round 3 若继续 A 路线，应优先做两态/小系统 exact diagonalization 与 Poisson decomposition，确认 `B phi` 的符号、单位和 scaling 后，再谈 fractional conductance。

## §末 输出格式

本轮成果：修正了 NSF-FCS-1 Round 2 的阻断公式。采用 `L phi=-h`、`h=b-J` 时，reservoir jump-current 的正确二阶扰动公式是 `lambda_R''(0)=<a>_pi+2<L'_0 phi>_pi=<a>_pi+2<h,phi>_pi+2<C>_pi`，不是 `<a>_pi+2<h,(-L)^-1h>_pi`。两态交替链校验显示旧公式会给出错误的非零方差；完整公式给出正确的零方差。

新增的引用文献：本次修正未新增文献；沿用 Kipnis-Varadhan DOI 10.1007/BF01210789；Kipnis-Landim DOI 10.1007/978-3-662-03752-2；Sethuraman DOI 10.1214/aop/1019160120；Landim-Quastel-Salmhofer-Yau DOI 10.1007/s00220-003-1020-4；Jara arXiv:0805.1326 / DOI 10.1002/cpa.20253；Bernardin-Jimenez Oviedo arXiv:1603.01234 / DOI 10.30757/alea.v14-25；Bernardin-Cardoso-Goncalves-Scotta arXiv:2007.01621 / DOI 10.1016/j.spa.2023.08.002；Derrida-Doucot-Roche DOI 10.1023/B:JOSS.0000022379.95508.B2；Erhard-Franco-Xu DOI 10.1214/24-EJP1137。

最弱的环节：从 fractional trace estimate 控制 `phi`，进一步推出完整组合 `<a>+2<L'_0 phi>` 与 `G_R(L)` 同标度；尤其是 `O(1)` activity 与 martingale cross term 的 cancellation。

下一步计划：Round 3 先做 exact Poisson decomposition：解 `L phi=-h`，分别输出 `<a>`、`2<h,phi>`、`2<C>`、`2<L'_0 phi>` 和总和 `lambda''`；再拟合这些项相对 `G_R(L)` 的标度。理论上补 long-jump exclusion with reservoirs 的 spectral gap 下界引用/证明，并寻找 endpoint boundary Dirichlet-to-Neumann/capacity 与 jump-current cross term 的组合估计。

需要PI投喂的文献方向：`tilted generator perturbation Markov additive current`；`martingale decomposition current additive functional exclusion`；`boundary current variance open exclusion Poisson equation`；`sector condition nonreversible Markov current CLT`；`fractional boundary capacity endpoint reservoir exclusion spectral gap`。
