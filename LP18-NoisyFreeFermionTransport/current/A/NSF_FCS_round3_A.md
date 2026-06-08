# NSF-FCS-1 Round 3 - A博士

角色：A博士（学院派）。本轮只读取 A 侧历史、PI/Inspector 指定文件与公开文献；未读取 `current/B`，未读取 B Round 3 输出。

## §-1 先发文献检索

检索工具：paper-search-mcp。检索时间：2026-06-03。

### 检索组1：nearest-neighbor open SSEP current FCS

命中并使用：

- B. Derrida, B. Doucot, P.-E. Roche, "Current Fluctuations in the One-Dimensional Symmetric Exclusion Process with Open Boundaries", Journal of Statistical Physics 115, 717-748 (2004), DOI `10.1023/B:JOSS.0000022379.95508.B2`.
- B. Derrida, O. Hirschberg, T. Sadhu, "Large Deviations in the Symmetric Simple Exclusion Process with Slow Boundaries", Journal of Statistical Physics 182 (2021), arXiv:`2009.04169`, DOI `10.1007/s10955-020-02680-3`。该文 §3 复述 fast-boundary open SSEP 的 current SCGF：
  `Lambda_L(theta) = L^{-1} R_fast(omega) + o(L^{-1})`,
  `R_fast(omega) = (arsinh sqrt(omega))^2`.

用途：作为 nearest-neighbor open SSEP 的精确 FCS 标尺。它直接显示：即使边界 reservoir jump activity 是 `O(1)`，长时 current variance 只有 `O(L^{-1})`。

### 检索组2：slow-boundary SSEP current FCS

命中并使用：

- B. Derrida, O. Hirschberg, T. Sadhu, arXiv:`2009.04169`, DOI `10.1007/s10955-020-02680-3`。该文给出 slow boundaries 的 current SCGF：
  `Lambda_L(theta) = L^{-1} R_slow(omega) + o(L^{-1})`,
  `R_slow(omega) = min_{t_a,t_b} { sinh^2(t_a)/Gamma_a + (u-t_a-t_b)^2 + sinh^2(t_b)/Gamma_b }`,
  其中 `omega = sinh^2 u`。
- Soumyabrata Saha, Tridib Sadhu, "Large deviations in the symmetric simple exclusion process with slow boundaries: A hydrodynamic perspective", SciPost Physics 17 (2024), DOI `10.21468/SciPostPhys.17.2.033`。新增文献。该文用 MFT 恢复 slow-boundary density/current LDF，并指出 slow coupling 在 MFT action 中引入边界项。

用途：slow-boundary 公式把左边界、bulk、右边界写成串联变分问题；这给出一个对照：当边界 activity 本身已被缩放到 `O(L^{-1})` 时，FCS 小量不再需要 fast-boundary 那种 `O(1)` activity cancellation。

### 检索组3：additivity / MFT 支撑

新增使用：

- T. Bodineau, B. Derrida, "Current Fluctuations in Nonequilibrium Diffusive Systems: An Additivity Principle", Physical Review Letters 92, 180601 (2004), DOI `10.1103/PhysRevLett.92.180601`。
- L. Bertini, A. De Sole, D. Gabrielli, G. Jona-Lasinio, C. Landim, "Macroscopic fluctuation theory", Reviews of Modern Physics 87, 593 (2015), DOI `10.1103/RevModPhys.87.593`。

用途：只作为宏观 current LDF/串联电阻解释的支撑；本轮不把 MFT 当作 microscopic cancellation 的证明。

## §0 框架声明

沿用 Round 2 的 finite-state Markov jump notation。对右 reservoir current 使用 counting field `theta`，避免和 SI 秒 `s` 混淆：

`(L_theta f)(eta) = sum_z c(eta,z) [ exp(theta q_R(eta,z)) f(eta^z) - f(eta) ]`.

定义：

- `b(eta) = L'_0 1 = sum_z c(eta,z) q_R(eta,z)`，单位 `s^-1`；
- `a(eta) = L''_0 1 = sum_z c(eta,z) q_R(eta,z)^2`，单位 `s^-1`；
- `J = <b>_pi`，`h=b-J`；
- `B f = L'_0 f = sum_z c q_R f(eta^z)`；
- `L phi = -h`，`<phi>_pi=0`。

完整二阶 jump-current FCS 公式为

`lambda_R''(0) = <a>_pi + 2 <B phi>_pi`.

写成 martingale-Poisson 分解：

`C(eta) = sum_z c(eta,z) q_R(eta,z) [phi(eta^z)-phi(eta)]`,

则

`lambda_R''(0) = <a>_pi + 2<h,phi>_pi + 2<C>_pi`.

更有用的 cancellation 形式是 carré-du-champ 形式：

`lambda_R''(0) = < sum_z c(eta,z) [ q_R(eta,z) + phi(eta^z)-phi(eta) ]^2 >_pi`.

原因是 stationarity 给出

`<sum_z c [phi(eta^z)-phi(eta)]^2>_pi = -2<phi,L phi>_pi = 2<h,phi>_pi`.

因此 cancellation 的精确含义不是三个数偶然相加变小，而是 Poisson corrector 在被计数的跳跃上近似满足

`phi(eta^z)-phi(eta) ~= -q_R(eta,z)`

使 martingale increment `q_R + Delta phi` 的平均平方变小。

--- INSPECTOR_CHECK ---
[公式] `lambda_R''(0)=<a>_pi+2<B phi>_pi=<a>_pi+2<h,phi>_pi+2<C>_pi=<sum_z c(q_R+Delta_z phi)^2>_pi`，其中 `Delta_z phi=phi(eta^z)-phi(eta)`。所有项单位均为 `s^-1`；`theta` 无量纲。
[方向] 本轮把 cancellation 定义为 corrector 对被计数 jump increment 的 screening：`q_R+Delta phi` 小，而不是把 `2<h,phi>` 单独解释为 FCS 方差。
[数据] Round 2 tilted-generator perturbation；本轮使用 open/slow-boundary SSEP 精确 SCGF 文献。
[假设] 有限体积 tilted generator 主特征值二阶可微；stationary average 存在；`<phi>_pi=0` 固定 Poisson 解常数。

## 1. fast open SSEP：精确 FCS 迫使 O(1) activity cancellation

nearest-neighbor open SSEP 的精确 large-`L` current SCGF 可写为

`Lambda_L(theta) = L^{-1} R_fast(omega(theta,rho_a,rho_b)) + o(L^{-1})`,

其中

`R_fast(omega) = (arsinh sqrt(omega))^2`,

`omega = rho_a(1-rho_b)(e^theta-1) + rho_b(1-rho_a)(e^{-theta}-1)`.

展开得到

`Lambda_L'(0) = (rho_a-rho_b)/L + o(L^{-1})`,

`Lambda_L''(0) = L^{-1} [ rho_a(1-rho_b)+rho_b(1-rho_a) - (2/3)(rho_a-rho_b)^2 ] + o(L^{-1})`.

现在看右 reservoir jump activity。若右边界 injection/removal rates 为

`rho_b(1-eta_L)` 与 `(1-rho_b) eta_L`，

则右 reservoir current 的 instantaneous activity 为

`a_R(eta) = rho_b(1-eta_L) + (1-rho_b) eta_L`.

fast boundary 的 stationary boundary density 满足 `<eta_L> = rho_b + O(L^{-1})`，所以

`<a_R>_pi = 2 rho_b(1-rho_b) + O(L^{-1})`.

这与精确 FCS 的 `Lambda_L''(0)=O(L^{-1})` 只能同时成立，如果

`2<B phi>_pi = -2 rho_b(1-rho_b) + O(L^{-1})`

或等价地

`2<h,phi>_pi + 2<C>_pi = -<a_R>_pi + O(L^{-1})`.

因此 fast open SSEP 的 cancellation 是强 cancellation：边界上每秒 `O(1)` 次 injection/removal 尝试多数只是局部 rattling；Poisson corrector 把这些局部跳跃吸收到 bounded occupation/corrector martingale 中，只有跨越整个扩散系统的 `O(L^{-1})` 模式留在 FCS 里。

用 carré-du-champ 写，这个结论更干净：

`<sum_z c(q_R+Delta_z phi)^2>_pi = O(L^{-1})`,

但

`<sum_z c q_R^2>_pi = O(1)`.

所以 `Delta_z phi ~= -q_R` 必须在右 reservoir jump 的高 activity 部分成立；残差的 Dirichlet 能量才是 `O(L^{-1})`。

## 2. slow-boundary SSEP：activity 先被缩放，cancellation 变成串联电阻

slow-boundary SSEP 中边界 rates 为 `O(L^{-1})`。Derrida-Hirschberg-Sadhu 的公式是

`Lambda_L(theta) = L^{-1} R_slow(omega(theta,rho_a,rho_b)) + o(L^{-1})`,

`R_slow(omega) = min_{t_a,t_b} { sinh^2(t_a)/Gamma_a + (u-t_a-t_b)^2 + sinh^2(t_b)/Gamma_b }`,

`omega = sinh^2 u`.

这个公式的物理内容是三段串联：

- 左 slow bond 给出 `sinh^2(t_a)/Gamma_a`；
- bulk diffusive SSEP 给出 `(u-t_a-t_b)^2`；
- 右 slow bond 给出 `sinh^2(t_b)/Gamma_b`。

与 fast-boundary 情形不同，slow right reservoir 的 microscopic activity 已经是

`<a_R>_pi = O(L^{-1})`.

于是完整二阶公式

`lambda_R'' = <a_R> + 2<h,phi> + 2<C>`

不需要先消掉一个 `O(1)` activity；三项从起点就是 `O(L^{-1})` 或更小。这里的 cancellation 不是 fast-boundary 的强 screening，而是串联 variational problem 中 counting field 在 left boundary、bulk、right boundary 之间重新分配。

这给 NSF-FCS-1 一个关键分叉：

- 如果 fractional reservoir 的总 jump activity 是 `O(G_R(L))`，它更像 slow-boundary SSEP；
- 如果 fractional reservoir 的总 jump activity 是 `O(1)`，但 conductance `G_R(L)->0`，它更像 fast open SSEP，需要强 `O(1)` cancellation。

## 3. 对 long-jump / fractional reservoir 的迁移判断

设右 reservoir 可以向 bulk site `x=1,...,L` 做长跳，右 reservoir rate tail 记为 `r_R(x)`，右 reservoir current increment 为 injection `+1`、removal `-1`。则

`a_R(eta)=sum_x r_R(x) [ rho_R(1-eta_x)+(1-rho_R) eta_x ]`.

若典型 fractional reservoir tail 满足 `r_R(x) ~ dist(x,R)^{-alpha}` 且 `alpha>1`，则

`A_R(L)=sum_x r_R(x)=O(1)`.

这意味着 microscopic activity 通常不是 `G_R(L)`，而是 `O(1)`。Round 2 的候选 conductance 标度为

| 区间 | 候选 `G_R(L)` | 对 cancellation 的要求 |
|---|---:|---|
| `alpha>3/2` | `L^-1` | 需要 fast-boundary 型 `O(1)` 到 `O(L^-1)` screening |
| `alpha=3/2` | `(log L)/L` | 需要保留临界 log 的 residual Dirichlet 能量 |
| `1<alpha<3/2` | `L^{-(2alpha-2)}` | 需要 nonlocal hitting/capacity 控制 residual |

因此，nearest-neighbor open SSEP 的机制可以迁移的部分是：

`lambda_R'' = <sum_z c(q_R+Delta_z phi)^2>`

这个 exact martingale-Poisson identity。只要能证明 fractional Poisson corrector 对右 reservoir jump 满足

`<sum_{z in R} c_z (q_R(z)+Delta_z phi)^2>_pi = O(G_R(L))`,

就能得到同标度 FCS。

不能直接迁移的部分是 nearest-neighbor 的 cut-current cohomology。nearest-neighbor SSEP 中任意两个 bond currents 的差只等于 bounded occupation change，所以所有截面 current 有同一长时 SCGF。long-jump exclusion 中一次 jump 可以跨过多个 cut，右 reservoir current 不再等同于单个 nearest-neighbor cut current；它只通过非局域 continuity equation 与 fractional divergence 相连。换言之，迁移需要一个 nonlocal harmonic/capacity lemma，而不是把 open SSEP 公式照搬。

本轮判断：

1. 对未缩放的 long-jump reservoir，`lambda_R''~G_R(L)` 若成立，必须来自 fast-boundary 型强 cancellation。
2. 这个 cancellation 的正确 microscopic 表达是 `q_R+Delta phi` 的 Dirichlet 残差小，而不是 `H_-1` 项小。
3. 现有 fractional Fick law / hydrodynamic conductance 文献只支撑 mean conductance 与非局域 Dirichlet form；尚未直接给出 `q_R+Delta phi` residual bound。
4. 因此迁移是 plausible but unproved：需要证明 right-reservoir jump 的 Poisson corrector 等价于 fractional harmonic measure/capacity 的 equilibrium potential。

--- INSPECTOR_CHECK ---
[公式] 对 long-jump reservoir，待证核心应写成 `D_R(L)=<sum_{z in R} c_z(q_R(z)+Delta_z phi)^2>_pi=O(G_R(L))`，而非 `||h||_{-1}^2=O(G_R(L))`。其中 `D_R(L)`、`G_R(L)` 在 microscopic time normalization 下单位均为 `s^-1`。
[方向] nearest-neighbor open SSEP 支持强 cancellation 机制；slow-boundary SSEP 支持 activity 先缩放的串联机制。标准 fractional reservoir 更可能落入前者，而非后者。
[数据] Derrida-Doucot-Roche open SSEP FCS；Derrida-Hirschberg-Sadhu slow-boundary FCS；Saha-Sadhu MFT slow-boundary 复核。
[假设] fractional reservoir 总 activity `A_R(L)=O(1)`；若模型实际把 reservoir rates 额外缩放到 `O(G_R(L))`，则本判断需改为 slow-boundary 型。

## 4. 深化1：本轮结论的下一层后果

第一层后果：NSF-FCS-1 的理论目标应改写为一个 nonlocal corrector screening 定理：

`q_R + Delta phi` 在 reservoir jump 集合上的 Dirichlet 均方残差由 fractional capacity 控制。

这比证明 mean fractional Fick law 更强，因为 mean 只看一阶 harmonic profile，而 FCS 二阶要控制 tilted corrector 的 jump-level residual。

第二层后果：数值实验必须输出的不只是

`lambda_R''` 与 `G_R(L)`，

而是至少五个量：

- `<a_R>`;
- `2<h,phi>`;
- `2<C>`;
- `<sum_z c(q_R+Delta_z phi)^2>`;
- `G_R(L)`。

如果 `<a_R>=O(1)` 而总和是 `O(G_R)`，则 cancellation 真实存在；如果 `<a_R>` 本身已经 `O(G_R)`，则只是 slow-boundary 型缩放，不能作为 fast-boundary fractional cancellation 的证据。

第三层后果：对 `alpha>3/2` 的 `L^-1` 区间，nearest-neighbor open SSEP 提供了最清晰的类比；对 `1<alpha<3/2`，残差可能由 deep landing jumps 的 hitting probability 控制，证明对象应接近 fractional equilibrium potential，而不是 local boundary layer。

硬边界：本轮没有证明 `D_R(L)=O(G_R(L))`；只把待证命题从模糊的 `lambda''~G` 精确化为 corrector residual/capacity bound。

## 5. 深化2：本轮前提中最可能出错的一项

第一层风险：最可能出错的前提是 `A_R(L)=sum_x r_R(x)=O(1)`。如果项目采用的 fractional reservoir 已经把每个 reservoir jump rate 乘了额外 `L` 依赖系数，使 `A_R(L)=O(G_R(L))`，则 fast-boundary cancellation 问题会退化为 slow-boundary SSEP 的串联问题。

第二层风险：即使 `A_R(L)=O(1)`，也不能假设 nearest-neighbor 的 current cohomology 自动成立。long-jump current 的 conservation law 是非局域的；一次 reservoir jump 到深处 bulk 不是一个局部边界 rattling event。对这些 jumps，`Delta phi ~= -q_R` 是否成立取决于从 landing site 回到右 reservoir 的 harmonic probability，而不是局部边界密度。

第三层风险：fractional hydrodynamic Dirichlet form 控制的是宏观 profile 能量；jump-current FCS 需要 microscopic tilted-generator corrector。宏观 MFT 若没有边界 noise/action 的 microscopic matching，可能给出正确指数但给不出 activity/cross-term cancellation 的项级分解。

硬边界：下一轮若继续 A 路线，优先补一个可检验 lemma：对单粒子 long-jump random walk with right reservoir，显式求解 Poisson corrector，检查 `sum_{z in R} c_z(q_R+Delta phi)^2` 是否等于或同标度于 fractional capacity。若单粒子都失败，多粒子 exclusion 不应继续声称同标度。

## §本轮输出格式

本轮成果：用 open/slow-boundary SSEP 的精确 current FCS 重新解释 Round 2 的完整二阶公式。fast open SSEP 显示 `<a_R>=O(1)` 但 `lambda_R''=O(L^{-1})`，因此必须有 `2<B phi>=-<a_R>+O(L^{-1})` 的强 cancellation；slow-boundary SSEP 则显示当 boundary activity 已缩放为 `O(L^{-1})` 时，FCS 小量来自串联变分而非强 `O(1)` 抵消。对未缩放 long-jump/fractional reservoir，若总 reservoir activity 为 `O(1)`，则 NSF-FCS-1 必须证明 `q_R+Delta phi` residual 由 fractional capacity 控制。

新增的引用文献：Saha-Sadhu DOI `10.21468/SciPostPhys.17.2.033`；Bodineau-Derrida DOI `10.1103/PhysRevLett.92.180601`；Bertini-De Sole-Gabrielli-Jona-Lasinio-Landim DOI `10.1103/RevModPhys.87.593`。本轮继续使用 Derrida-Doucot-Roche DOI `10.1023/B:JOSS.0000022379.95508.B2` 与 Derrida-Hirschberg-Sadhu arXiv:`2009.04169` / DOI `10.1007/s10955-020-02680-3`。

最弱的环节：从 fractional hydrodynamic capacity 推出 microscopic corrector residual `D_R(L)=<sum_{z in R} c_z(q_R+Delta phi)^2>=O(G_R(L))`。这一步目前只有类比和公式定位，没有证明。

下一步计划：做单粒子 long-jump reservoir 的 Poisson corrector test。明确 `r_R(x)`、`A_R(L)`、`G_R(L)`，解 `L phi=-h` 后输出 `<a_R>`、`2<h,phi>`、`2<C>`、`D_R(L)`，判断 cancellation 是否已经在单粒子层面等于 fractional capacity。

需要 PI 投喂的文献方向：`fractional reservoir exclusion harmonic measure capacity`；`long jump random walk reservoir Poisson equation current variance`；`nonlocal MFT boundary current noise`；`open SSEP current cohomology Poisson corrector`。
