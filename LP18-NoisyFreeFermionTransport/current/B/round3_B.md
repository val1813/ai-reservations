# B博士 Round 3：把 long-jump 主线与 holonomy 副线分离的最小判据

## 0. 框架声明

本轮不再扩展新方向。B 线只保留一个可检验、可击毙的副线命题：

> long-jump 标度由强退相干 Zeno 投影后的实跳率核 `r_l=2|J_l|^2/gamma` 决定；holonomy 只有在扣除同一实跳率核导致的 `D_eff` 后，仍在 FCS residual `Q(s,theta)` 中留下稳定的偶周期相位依赖时，才有资格保留。

跨学科借来的结构改为统计实验设计里的“正交化 nuisance parameter”：`D_eff` 是 nuisance parameter，先用 `theta` 平均或 `theta=0` 的数据拟合掉；holonomy 是剩余通道。若剩余通道在强退相干、弱 shortcut、增大系统尺寸后消失得比 long-jump 主线更快，则 B 副线降级或击毙。

## 1. 最小 tilted-Lindblad / Zeno-effective 数值实验

### 1.1 模型

有限链 `i=1,...,L`，左右 reservoir 密度 `rho_L,rho_R` 固定。Hamiltonian

`H = sum_i J(c_i^\dagger c_{i+1}+h.c.) + sum_{l in S} J_l e^{i theta_l} c_p^\dagger c_q + h.c.`

其中 `l=|q-p|`。bulk dephasing

`L_i = sqrt(gamma) n_i`

边界注入/抽取按通常 Markovian reservoir 实现，并在左或右边界加 counting field `s`，取 tilted Liouvillian 最大特征值

`lambda_L(s; alpha,J_l,gamma,theta) = max eig L_s(theta)`。

强退相干对照采用二阶 Zeno-effective population generator：

`w_{ij}=2|J_{ij}|^2/gamma`

它完全不含 `theta`。因此它是 long-jump 主线的干净基线，也是 holonomy 副线的最强击毙对照。

### 1.2 扫描参数

最小扫描不求大而全，只做能分离两条线的矩阵：

1. `L = 16,24,32,48,64`；若 full tilted Lindblad 太大，`L=8,10,12,14` 做量子 Liouvillian，`L=32..256` 做 Zeno-effective。
2. `alpha = 1.25, 1.50, 1.75, 2.00`；主线围绕 `alpha=3/2`。
3. `J_l = J0 l^{-alpha}` 的 power-law 全连接版本，用于主线；另加单 shortcut 版本 `l=L/2`、`J_l in {0.02J,0.05J,0.1J,0.2J}`，用于 holonomy。
4. `gamma/J = 10,20,40,80`，确保能看出强退相干幂律。
5. `theta = 0, pi/2, pi, 3pi/2`；必要时加 `theta=pi/4,3pi/4` 拟合一阶谐波。
6. `s` 取小网格 `{-s0, -s0/2, 0, s0/2, s0}`，或直接用数值导数输出 `C_1,C_2,C_3`。

### 1.3 必须输出的量

每组参数输出：

1. `C_n(theta)=partial_s^n lambda(s,theta)|_{s=0}`，至少 `n=1,2,3`。
2. `D_eff(theta)`：用 `C_1(theta)` 或线性响应 conductance 拟合出来的单参数扩散常数。
3. `Q(s,theta)=Delta lambda(s,theta) - (partial_D lambda_SSEP)(s;D0) Delta D(theta)`。
4. `Q_n(theta)=C_n(theta)-C_n^SSEP[D_eff(theta)]`，至少 `n=2,3`。
5. 谐波分解：`Q_n(theta)=B_{n,0}+B_{n,1} cos theta+B_{n,2} cos 2theta+...`。
6. 幂律拟合指数：
   - long-jump 主线：`C_2(theta=0,L) ~ L^{-beta(alpha)}` 或边界 conductance `G_L ~ L^{-zeta(alpha)}`。
   - holonomy residual：`|B_{n,1}| ~ |J_l|^mu gamma^{-nu} L^{-kappa}`。

### 1.4 最小实现顺序

第一步只跑 Zeno-effective classical long-jump exclusion：`theta` 不出现，验证 `alpha=3/2` 附近的二阶矩阈值。这一步给 A 主线的数值基线。

第二步跑 full tilted quadratic Lindblad 的单 shortcut AB 环：固定 `alpha` 不扫，先只看 `theta=0,pi`，输出 `Q_2,Q_3`。这一步只检验 B 副线是否有非零 residual。

第三步才把 power-law long-jump 和单个带相位 shortcut 合并：先从 `theta=0` 拟合 `D_eff` 和 long-jump 标度，再看 `theta` residual。若第二步已击毙 B 线，第三步不需要做。

--- INSPECTOR_CHECK ---
[公式] `lambda(s)=lim_{t->infty}t^-1 log <e^{sQ_t}>`，单位 `s^-1`；`w_{ij}=2|J_{ij}|^2/gamma`，单位 `s^-1`；`Q(s,theta)=Delta lambda-(partial_D lambda_SSEP)Delta D`，单位 `s^-1`；`C_n=partial_s^n lambda|_{0}`，单位 `s^-1`，counting field `s` 无量纲。
[方向] Zeno-effective generator 不含 `theta`，因此能独立验证 long-jump 主线；full tilted Lindblad 中只有扣除 `D_eff` 后仍非零的偶周期 residual 才能支持 holonomy。
[数据] 当前为数值实验设计，无实测数据；数据来源应为同一有限链的 tilted Liouvillian 主特征值或 Zeno-effective tilted Markov generator 主特征值。
[假设] reservoir 设置固定且可重复；`gamma` 是最大快尺度；SSEP 基线 `lambda_SSEP(s;D)` 可由 `theta=0` 或纯 Zeno 模型拟合。

## 2. holonomy 副线保留/击毙判据

### 2.1 保留条件

holonomy 只能在同时满足以下条件时保留：

1. `Q_n(theta)` 在 `n>=2` 中非零，且不是由 `C_1` 拟合出的 `D_eff(theta)` 可吸收。
2. `Q_n(theta)` 是偶周期函数，主谐波满足 `cos theta-1` 或 `1-cos theta`，并在 `theta=0 mod 2pi` 退化。
3. `|B_{n,1}|` 对 `J_l` 和 `gamma` 有稳定幂律。候选二阶是 `mu=2, nu=1`；若实际是更高阶，只要幂律清楚且 residual 非零，副线可降级保留。
4. 在同一 `alpha,L,gamma` 下，改变 `theta` 不改变 long-jump 主线指数 `beta(alpha)`，只改变 residual 振幅。

### 2.2 击毙条件

满足任一条即可击毙或至少冻结 B 副线：

1. full tilted Lindblad 与 Zeno-effective 在 `Q_n(theta)` 上一致为零到数值精度，且误差界小于 long-jump 主线信号的 `1%`。
2. 扣除 `D_eff(theta)` 后，`Q(s,theta)` 随 `gamma` 比任何可发表有限阶闭环项更快消失，例如拟合 `nu>=3` 且随 `L` 还额外快速衰减，导致在 `gamma/J>=40,L>=32` 时低于数值误差。
3. `Q_n(theta)` 的相位依赖不是偶周期 `cos m theta`，而是随 gauge choice 或 counting-field 放置改变；这说明它是实现伪影，不是 Wilson loop。
4. residual 只出现在 `C_1`，并可完全由 `D_eff(theta)` 吸收；`C_2,C_3` 无独立残差。
5. `theta=0` 与 `theta=pi` 的差异在增大 `L` 后按比主线更高阶的有限尺寸误差消失，例如 `|Q_3(pi)|/|C_3(0)| -> 0` 且无可稳定拟合的幂律窗口。

### 2.3 降级条件

若 `Q(s,theta)` 非零，但只按更高阶闭环路径出现，例如

`|B_{n,1}| ~ J_l^2 J^m gamma^{-(m+1)} L^{-kappa_loop}`

则 B 线不再声称改变 universality，只作为 finite-size coherent correction 附录方向。只有当 `O(L)` 个 loops 累加后 residual 变成 `O(1)`，才允许重新升级。

## 3. 如何验证 A 的 `alpha=3/2` 主线且不混入 holonomy

关键隔离原则：验证 `alpha=3/2` 时必须设 `theta=0`，或直接使用不含相位的 Zeno-effective generator。此时所有 Peierls holonomy 被关闭，只剩实跳率

`r(l)=2|J_l|^2/gamma ~ l^{-2alpha}`。

主线判据：

1. 计算跳核二阶矩 `M_2(L)=sum_{l=1}^L l^2 r(l)`。
2. 若 `alpha>3/2`，`M_2(L)` 有限，预期普通 diffusive/SSEP 标度。
3. 若 `alpha=3/2`，`M_2(L) ~ log L`，预期边界 conductance 或 `C_2` 出现对数修正。
4. 若 `alpha<3/2`，`M_2(L)` 发散，进入 fractional long-jump 标度。

数值上先拟合 `theta=0` 的

`C_2(L,alpha,theta=0)`、`G_L(alpha,theta=0)`、`D_eff(L,alpha,theta=0)`。

只有完成这一步后，才允许打开 `theta` 并研究

`Q_n(theta)=C_n(theta)-C_n^SSEP[D_eff(theta)]`。

因此 A 主线的判据不使用 `Q`，B 副线的判据不使用 `C_2` 的裸标度。两者观测量正交。

## 4. 深挖1：同构的更深数学结构

第一层：nuisance-orthogonal decomposition。

把 tilted CGF 看成两部分：

`lambda(s,theta)=lambda_main(s;D_eff(alpha,L,gamma,J_l)) + lambda_res(s,theta)`。

`D_eff` 是可由 `C_1` 或 `theta=0` 数据识别的实参数；`lambda_res` 是与 `D_eff` 正交的剩余方向。数学对象不是“有无 AB 相位”，而是参数流形上对 `D_eff` 方向投影后的正交分量。

第二层：Fisher metric 下的残差判据。

定义由 cumulant 向量 `C=(C_1,C_2,C_3,...)` 张成的局部度量。`D_eff` 方向是

`v_D = partial_D C^SSEP(D)`。

holonomy 方向是

`v_theta = partial_{cos theta} C(theta)|_{theta=0}`。

若投影后

`v_theta^\perp = v_theta - v_D (v_D·v_theta)/(v_D·v_D)`

为零，则 holonomy 不可辨识，应击毙；若非零，则副线保留。这个形式比单看某个 cumulant 更稳，因为它明确扣除了 ordinary conductance renormalization。

第三层：强退相干极限中的商空间。

Zeno 投影把量子连接压到 population graph 的实跳率空间。holonomy 若存在，必须活在被 Zeno 投影杀掉后的高阶商空间中：

`ker(P_Zeno at second order) / im(D_eff renormalization)`。

若这个商空间在数值上为空，B 线被击毙；若非空，也只是高阶 residual，不得混入 leading long-jump 标度。

## 5. 深挖2：原学科结构的下一层推广

第一层推广：从正交实验设计到 sequential test。

先做主线测试 `H0_main: alpha>3/2 diffusive` vs `H1_main: alpha<=3/2 long-jump/fractional`，使用 `theta=0` 数据。只有主线指数固定后，才做副线测试 `H0_hol: Q=0` vs `H1_hol: Q!=0`。这避免把 `theta` residual 错当成 long-jump 指数漂移。

第二层推广：从单 shortcut 到稀疏 loops 的多输入检测。

若单 loop residual 已被击毙，多 loop 不应继续投入。若单 loop residual 非零，再定义 Fisher matrix

`I_ab = <v_a^\perp, v_b^\perp>`

其中 `a,b` 标记不同 loops 的 `theta_a,theta_b`。只有当 `I_ab` 有稳定非零特征值，才说明多 loop holonomy 有累积信息容量。否则多 loop 只是多个不可辨识伪参数。

第三层推广：从可检测副线到 universality breaker。

单 loop 即使保留，多数情况下也只是 `O(1/L)` 或更小的 finite-size correction。升级为 universality breaker 的必要条件是 loop 数随 `L` 增长，且

`sum_a |B_{n,1}^{(a)}| = O(C_n^{main})`

在热力学极限不消失。若该条件不成立，B 线只能作为附录或数值 caution。

## 6. 本轮收敛判断

本轮不主张 holonomy 是主结果。真正主结果应是强退相干下 power-law hopping 的二阶矩阈值 `alpha=3/2`。B 线的贡献是给 PI 一个最小防混淆协议：

1. `theta=0` 或 Zeno-effective 验证 long-jump 主线。
2. full tilted Lindblad 只用于检查 `Q(s,theta)`。
3. 若 `Q` 在扣除 `D_eff` 后消失，B 线当场击毙。
4. 若 `Q` 非零但高阶小量，B 线降级为 finite-size coherent correction。
5. 只有 `Q` 与主线同阶并随 loop density 累积时，才允许重新讨论 universality。

## 末格式

本轮的跨学科跳跃：统计实验设计/信息几何 -> nuisance parameter 正交化与 Fisher residual -> 把 long-jump `D_eff` 主线和 holonomy `Q(s,theta)` 副线拆成正交可检验通道。

这个结构的数学对象：tilted CGF `lambda(s,theta)`、Zeno 实跳率核 `w_{ij}=2|J_{ij}|^2/gamma`、单参数扩散投影 `D_eff`、conductance-residual `Q(s,theta)`、cumulant residual `Q_n(theta)`、Fisher 正交分量 `v_theta^\perp`。

如果这个同构成立，最奇怪的可检验预测是：同一 long-jump 标度指数 `beta(alpha)` 不随 `theta` 改变，但扣除 `D_eff` 后的高阶 cumulant residual 仍出现稳定 `cos theta-1` 谐波；若该 residual 不存在，holonomy 副线应被击毙。

A博士最可能反对的点：强退相干二阶 Zeno generator 只保留实跳率，Peierls 相位在主阶完全消失，因此 B 的 holonomy 不应进入主线。我的回应是：同意；Round 3 的设计正是把 B 线降为 residual test，主线验证必须在 `theta=0` 或 Zeno-effective 中完成。

本轮失败记录（如有）：放弃把 holonomy 作为 leading universality breaker 的表述；除非 `Q(s,theta)` 与主线同阶且可随 loop density 累积，否则它只是有限尺寸/高阶相干修正。

下一步计划：请 PI 或数值组先跑两张表：一张是 `theta=0` 的 `alpha,L` 标度表，验证 `alpha=3/2`；另一张是单 shortcut full tilted Lindblad 的 `theta,J_l,gamma` residual 表，判定 `Q` 是否非零。若第二张表为零，B 副线终止。

需要PI投喂的文献方向：long-range exclusion fractional hydrodynamics boundary current variance；Zeno projection dephasing free fermion transport；full counting statistics tilted Lindblad quadratic fermions；Aharonov-Bohm interferometer dephasing counting statistics；Fisher information nuisance parameter orthogonalization。
