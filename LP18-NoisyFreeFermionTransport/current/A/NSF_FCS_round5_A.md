# NSF-FCS-1 Round 5 - A博士

角色：A博士（学院派）。本轮只读取了 A 侧历史、PI synthesis/status 指定文件与公开文献；未读取 `current/B`，未读取 B Round 5 输出。

## 0. 本轮结论

在有限状态、不可约 Markov jump process 中，若 two-terminal transport current 是唯一 affinity 的共轭电流，并且 rates 满足 local detailed balance，则在 equilibrium symmetric gauge 下

`lambda_T''(0;A=0) = 2 G_R`

不是 NSF-FCS-1 的新尺度定理，而是有限体积 fluctuation-dissipation / Einstein-Helfand relation。这里 `lambda_T''` 采用普通 SCGF `lambda(chi,A)=lim_{t->infty} t^{-1} log E_A exp[chi Q_T(t)]` 的二阶导数，因此等于长时方差率 `lim t^{-1} Var(Q_T)`；`G_R` 必须定义为对无量纲 entropy affinity `A` 的线性响应 `partial_A J_T|_{A=0}`。在这个规范下，数值台账中 `S_T=lambda_T''/G_R≈2` 正是 FDT 的系数 2。

## 1. 文献定理定位

核心文献链：

1. Schnakenberg, "Network theory of microscopic and macroscopic behavior of master equation systems", Rev. Mod. Phys. 48, 571 (1976), DOI: `10.1103/RevModPhys.48.571`。给出 master equation 网络中的 cycle affinities 与 currents 框架。
2. Lebowitz and Spohn, "A Gallavotti-Cohen-Type Symmetry in the Large Deviation Functional for Stochastic Dynamics", J. Stat. Phys. 95, 333 (1999), DOI: `10.1023/A:1004589714161`。给出 Markov stochastic dynamics 的 GC 型大偏差对称性。
3. Andrieux and Gaspard, "Fluctuation Theorem for Currents and Schnakenberg Network Theory", J. Stat. Phys. 127, 107 (2007), DOI: `10.1007/s10955-006-9233-5`, arXiv/旧号：`cond-mat/0512254`。把 current fluctuation theorem 放到 Schnakenberg network theory 中。
4. Andrieux and Gaspard, "Fluctuation theorem for currents and nonlinear response coefficients", J. Stat. Mech. P02006 (2007), DOI: `10.1088/1742-5468/2007/02/P02006`, arXiv: `0704.3318`。Eq. (7) 写出 current generating function symmetry；Eq. (10)-(13) 从该 symmetry 推出 Onsager 系数与二阶 current cumulant 的关系；Eq. (15) 给出 Green-Kubo / Einstein-Helfand 形式。

其中第 4 篇是本轮需要引用到公式层面的直接来源。它的符号 `Q(lambda;A)` 用 `-log <exp[-lambda G]> / t`，所以文中 `L = -(1/2) Q_{lambda lambda}(0;0)`。换成本项目的普通 SCGF `lambda(chi,A)=log <exp[chi Q_T]>/t` 后，就是

`lambda_{chi chi}(0;0) = 2 L`.

若把 `L` 记为 two-terminal conductance `G_R`，即得到 `lambda_T''(0)=2G_R`。

## 2. counting field 与 affinity 规范

设有限状态空间为 `Omega`，转移 `x -> y` 的 transport increment 为

`d_{xy}=-d_{yx} in Z`,

`Q_T(t)=sum_{jumps x->y up to t} d_{xy}`。

本轮采用普通 SCGF：

`lambda(chi,A)=lim_{t->infty} t^{-1} log E_A exp[chi Q_T(t)]`.

因此

`J_T(A)=partial_chi lambda(0,A) = lim_{t->infty} t^{-1} E_A Q_T(t)`,

`lambda_T''(0;A)=partial_chi^2 lambda(0,A) = lim_{t->infty} t^{-1} Var_A Q_T(t)`.

Local detailed balance / symmetric gauge 写成

`log [k_{xy}(A) pi_x^0 / (k_{yx}(A) pi_y^0)] = A d_{xy}`,

等价的对称分配是

`k_{xy}(A)=k_{xy}^0 exp(A d_{xy}/2)`, `k_{yx}(A)=k_{yx}^0 exp(-A d_{xy}/2)`

在 `A=0` 回到 detailed balance：`pi_x^0 k_{xy}^0 = pi_y^0 k_{yx}^0`。对 exclusion reservoir，`A` 应理解为无量纲化学势/entropy affinity，例如

`A = logit(rho_L)-logit(rho_R)`,

而 symmetric gauge 是 `logit(rho_L)=h0+A/2`, `logit(rho_R)=h0-A/2`。在本项目 equilibrium `rho0=1/2` 时 `h0=0`。如果数值脚本用密度偏置 `delta rho` 做差分，必须先除以 `partial_delta A|_{0}`；只有完成这个换元后，线性响应才是这里的 `G_R=partial_A J_T|_0`。

## 3. 有限体积推导

有限状态不可约 Markov generator 的 tilted generator 为

`(L_{chi,A})_{xy}=k_{yx}(A) exp(chi d_{yx})` for `x != y`

并保留原 diagonal escape rate。主特征值 `lambda(chi,A)` 在 `chi,A` 近零解析。由 local detailed balance 与 time reversal similarity，有 Gallavotti-Cohen symmetry

`lambda(chi,A)=lambda(-A-chi,A)`.

对该恒等式先对 `chi`、再对 `A` 求导，并在 `(chi,A)=(0,0)` 取值：

`0 = partial_chi partial_A [lambda(chi,A)-lambda(-A-chi,A)]|_0`

`= 2 lambda_{chi A}(0,0) - lambda_{chi chi}(0,0)`.

所以

`lambda_{chi chi}(0,0)=2 lambda_{chi A}(0,0)`.

又 `J_T(A)=lambda_chi(0,A)`，故

`G_R := partial_A J_T(A)|_{A=0}=lambda_{chi A}(0,0)`,

最终得到

`lambda_T''(0)=2G_R`.

这一步不需要 thermodynamic limit，也不依赖 long-jump tail 的具体指数；所有有限体积 correction 都已经包含在有限矩阵的主特征值中。long-jump reservoir 只决定 `G_R(L)` 的大小，不能改变 equilibrium FDT 中的系数 2。

--- INSPECTOR_CHECK ---
[公式] `lambda(chi,A)=lambda(-A-chi,A)`；`G_R=partial_A partial_chi lambda(0,0)`；`lambda_T''(0)=partial_chi^2 lambda(0,0)=2G_R`。`lambda_T''` 与 `G_R` 单位均为 `s^-1`，因为 `A` 与 `chi` 均无量纲。  
[方向] two-terminal transport 版 `S_T≈2` 是 equilibrium FDT/Einstein-Helfand 恒等式，不是新的 NSF-FCS 尺度证据；真正的尺度信息只在 `G_R(L)` 本身。  
[数据] 使用 PI transport/exclusion ledger summary 中 `S_T=lambda_T''/G_R≈2` 的数值结果；文献依据为 Andrieux-Gaspard 2007 Eq. (7), (13), (15), DOI `10.1088/1742-5468/2007/02/P02006`, arXiv `0704.3318`。  
[假设] 有限状态不可约；`d_{xy}` 是与唯一 two-terminal affinity 共轭的 transport current；rates 满足 local detailed balance；`G_R` 是对无量纲 affinity `A` 而非裸 density difference 的导数。

## 4. 为什么 bare exchange 不适用

Round 4 的 bare right-reservoir exchange current 是 occupation coboundary 或非独立 thermodynamic cycle current；它不是 two-terminal entropy affinity 的共轭电流。因此它不满足本节推导中 `A d_{xy}` 这一 conjugacy 条件。对这种 observable，`lambda_R''=0` 或被台账门控为 `INVALID_BARE_EXCHANGE_NOT_TRANSPORT` 并不和 FDT 冲突。

transport ledger 已经改成 two-terminal channel-resolved current；这时 current increment `d_{xy}` 与 reservoir affinity 同一规范，GC symmetry 可用，故 `lambda_T''/G_R` 应稳定在 2。finite-density exclusion ledger 也稳定在 2，说明 occupation-dependent rates 没有破坏 local detailed balance 的 FDT 结构。

--- INSPECTOR_CHECK ---
[公式] 若 `Q_bare(t)=psi(X_0)-psi(X_t)` 为 coboundary，则 `lim_{t->infty} t^{-1} Var Q_bare(t)=0`；若 `Q_T` 为 conjugate transport current，则 `lim t^{-1} Var Q_T(t)=2 partial_A J_T|_0`。单位均为 `s^-1`。  
[方向] bare exchange 的 kill 与 transport current 的 keep 可以同时成立；二者的差别是 current 是否与 terminal affinity 共轭。  
[数据] Round 4 A 的 coboundary 判断；PI transport/exclusion ledger 的 `INVALID_BARE_EXCHANGE_NOT_TRANSPORT` 与 `S_T≈2`。  
[假设] two-terminal ledger 的 `G_R` 已经按 entropy affinity 归一；若用 `rho_L-rho_R` 直接定义 conductance，则系数会被 compressibility/logit Jacobian 改写。

## 5. 对 NSF-FCS-1 的影响

当前二阶 FCS 问题应降级：在 equilibrium two-terminal symmetric gauge 下，证明 `lambda_T''~G_R` 不再是独立目标，因为更强的有限体积恒等式 `lambda_T''=2G_R` 已由 fluctuation theorem 给出。数值台账 `S_T≈2` 的主要价值是校准 counting-field/affinity 规范和排除实现错误，而不是证明新的 transport scaling。

仍然有价值的 NSF-FCS-1 风险点转移为三类：

1. 非平衡：`A != 0` 时二阶 cumulant 的 affinity sensitivity 与 nonlinear response，需使用 Andrieux-Gaspard 的 higher-order relations，而不再有简单常数 2。
2. 非对称或错误 gauge：若 left/right reservoir 的 driving 不是同一 entropy affinity 的对称分配，`G_R` 的定义可能夹入 Jacobian 或额外 frenetic terms。
3. 高阶 cumulants：三阶、四阶 FCS 不由 equilibrium `2G` 固定，才可能承载 NSF-FCS-1 的新信息。

## 6. 深化1：本轮结论的下一层后果

第一层后果：PI 后续不应再把 `S_T≈2` 当作 long-jump reservoir 的特殊发现。它是对 finite-state LDB generator 的 sanity check。真正需要分析的是 `G_R(L)` 的有限体积 scaling：single-particle 情况可与 capacity/Dirichlet principle 比较；exclusion 情况则是 many-particle Green-Kubo conductance。

第二层后果：如果 `G_R(L)` 已经由 capacity 或数值 ledger 给出同一斜率，那么 `lambda_T''` 的同斜率自动跟随。任何 `lambda_T''` 与 `G_R` 的斜率分叉，优先说明 counting current、affinity normalization、tilted generator sign、或 finite-difference derivative 定义出错，而不是说明 FDT 失效。

第三层后果：NSF-FCS-1 若要保持新意，应把问题转向 `A=0` 以外或 `n>=3` cumulants。例如检查 `partial_A lambda_{chi chi}(0,0)`、`lambda_{chi chi chi}(0,0)` 是否携带 long-jump tail 的额外尺度；这些量在 Andrieux-Gaspard 框架中受 nonlinear response identities 约束，但不被 `2G` 完全固定。

## 7. 深化2：最可能出错的前提

第一层风险：`G_R` 的单位规范。文献里的 affinity 是 entropy affinity，无量纲。若台账中的 `G_R` 实际是 `partial_delta_rho J`，则在 `rho0=1/2` symmetric density gauge 下 `A=logit(rho_L)-logit(rho_R)`，小偏置的 Jacobian 需要显式处理。未处理时，理论系数不是 2。

第二层风险：current increment 的 conjugacy。FT symmetry 要求被计数的 `Q_T` 正是 entropy production 中 `A Q_T` 的那一项。若计数的是 reservoir 内部交换、单端 source/sink exchange、或加了任意 gradient/coboundary 的 observable，则 `lambda''=2G` 可被改写或退化为零。

第三层风险：finite-state 条件。当前 finite ledger 满足有限矩阵假设；若以后取无限体积、连续谱、非遍历极限、或 reservoir tail 造成 escape rate 非有限，则需要先证明主特征值解析性和极限交换。Round 5 只证明每个固定 `L` 的恒等式，不自动证明 `L->infty` 后的 uniformity。

硬边界：本轮没有证明 `G_R(L)~Cap(R,0)` 的 long-jump capacity lemma，也没有证明 nonlinear/high-order FCS 的新尺度。它只把 equilibrium two-terminal 二阶关系定位为已有 FDT 定理，并解释 `S_T≈2`。

## 本轮输出格式

本轮成果：定位并证明了 `lambda_T''(0)=2G_R` 在 finite-state Markov jump process、local detailed balance、equilibrium two-terminal symmetric gauge 下是有限体积 FDT/Einstein-Helfand relation。数值台账 `S_T≈2` 是该恒等式的表现；`lambda_T''` 的 scaling 跟随 `G_R`，不构成独立 NSF-FCS 新证据。

新增引用文献：Schnakenberg 1976 DOI `10.1103/RevModPhys.48.571`；Lebowitz-Spohn 1999 DOI `10.1023/A:1004589714161`；Andrieux-Gaspard 2007 J. Stat. Phys. DOI `10.1007/s10955-006-9233-5`, arXiv/旧号 `cond-mat/0512254`；Andrieux-Gaspard 2007 J. Stat. Mech. DOI `10.1088/1742-5468/2007/02/P02006`, arXiv `0704.3318`。

最弱的环节：台账中的 `G_R` 是否严格按 entropy affinity `A` 归一。若它使用裸密度差或其它 perturbation parameter，必须补一行 Jacobian 校准。

下一步计划：让 PI/Inspector 检查 transport/exclusion ledger 中 `G_R` 的定义是否为 `partial_A J_T|_0`；若确认，则 equilibrium 二阶 FCS 分支收束，转向非平衡 affinity sensitivity 或三阶/四阶 cumulants。

需要 PI 投喂的文献方向：`finite-state Markov jump current fluctuation theorem nonlinear response`, `Einstein-Helfand formula Markov jump process`, `full counting statistics fluctuation theorem nonlinear conductance`。
