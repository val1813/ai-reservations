# LP23-R2 Round2（A路）：非局域 `K(x,x')` 活口先发覆盖判定

日期：2026-06-03

## §0 框架声明

本轮采用的成熟框架是：线性非局域电动力学与线性响应理论。

核心对象不是新的真空几何量，而是本构型响应

`H^{ab}(x)=1/2 \int K^{abcd}(x,x') F_cd(x') dV_{x'}`。

判定标准：

`K` 若可写成局域极限 `chi^{abcd}(x) delta_V(x,x')`，则归入 premetric/local constitutive electrodynamics；若是平移不变线性介质核，则 Fourier 化为 `chi^{abcd}(omega,k)`；若由加速观测者的测量历史产生，则归入 Mashhoon/Hehl 非局域电动力学；若由探测器、环境消去或 readout 协议产生，则归入开放系统/装置建模。

因此 LP23-R2 的强命题只能是：

`I_K != 0` 且 `I_K` 不等价于 `{local chi, spinoptics O(1/omega), Mashhoon observer kernel, ordinary chi(omega,k), measurement protocol kernel}`。

## §-1 先发文献检索

四组检索结论：

1. Mashhoon/Hehl 非局域电动力学：
   - Muench, Hehl, Mashhoon, "Acceleration-induced nonlocal electrodynamics in Minkowski spacetime", DOI `10.1016/s0375-9601(00)00316-9`.
   - Mashhoon, "Vacuum electrodynamics of accelerated systems: Nonlocal Maxwell's equations", DOI `10.1002/andp.200310028`；OpenAlex 记录含 arXiv `hep-th/0309124`。
   - Mashhoon, "Nonlocal special relativity", DOI `10.1002/andp.200810308`.
   - Mashhoon, "Toward Nonlocal Electrodynamics of Accelerated Systems", DOI `10.3390/universe6120229`.

   先发压力：这些工作已经把“观测者读出的场 = 沿过去世界线的局域场加权积分”作为 Volterra 型 memory kernel 处理，并且指出加速停止后场方程仍可保留非局域记忆。因此任何“历史依赖 readout kernel”若只依赖观测者加速度/转动历史，已经被覆盖。

2. 频散/空间非局域介质：
   - Landau & Lifshitz, *Electrodynamics of Continuous Media*, "Spatial Dispersion", DOI `10.1016/b978-0-08-030275-1.50018-7`.
   - Agranovich & Ginzburg, "Crystal Optics with Spatial Dispersion", DOI `10.1016/s0079-6638(08)70047-7`; book DOI `10.1007/978-3-662-02406-5`.
   - Keller, "Linear Nonlocal Response Theory", DOI `10.1007/978-3-642-17410-0_10`; "Quantum Theory of the Generalized Nonlocal Linear Response", DOI `10.1007/978-3-642-17410-0_12`.

   先发压力：若 `K(x,x')=K(x-x')` 或在局域平衡近似下只依赖相对时空坐标，则

   `H^{ab}(omega,k)=1/2 chi^{abcd}(omega,k) F_cd(omega,k)`，

   这就是标准频散/空间色散响应，不是 LP23 新自由度。

3. 开放系统/测量协议 kernel：
   - Calzetta & Hu, *Nonequilibrium Quantum Field Theory*, DOI `10.1017/cbo9780511535123`; OA reissue DOI `10.1017/9781009290036`.
   - Macroscopic/nonlocal QED 与吸收介质文献把 Green tensor、噪声电流、耗散响应作为有效描述处理，例如 Feist/Fernandez-Dominguez/Garcia-Vidal, DOI `10.1515/nanoph-2020-0451`.

   先发压力：若 `K` 来自 trace-out、探测器响应、采样窗口、锁相/滤波、路径重建或环境噪声，它是影响泛函/开放系统或仪器响应核。此时 R2 离开基础真空物理，变为装置建模。

4. 代数结构：
   - toy script 已验证：三边环上 `r=[0.10,-0.04,0.08]` 不是 endpoint calibration coboundary，`cycle syndrome B r=0.14`，`I_bridge=0.00653333`。
   - 但该结果只证明图上商空间非空，不证明物理 `K` 非标准。

## 1. Mashhoon/Hehl 是否已覆盖 `K` memory residual？

结论：覆盖一大类，足以杀死“观测者历史记忆就是新物理”的版本。

Mashhoon 类形式可抽象为

`F_obs(lambda)=F_inst(lambda)+\int_{lambda0}^{lambda} M(lambda,lambda') F_inst(lambda') d lambda'`。

其中 `M` 由加速度/转动历史决定，满足因果 Volterra 支持。把它提升到本构语言，就是沿世界线支持的非局域核：

`K_M^{abcd}(x,x') ~ int d tau' delta_V(x',z(tau')) M^{abcd}(tau,tau') Theta(tau-tau')`。

因此若 LP23 的 `K` 只是“沿探测器世界线读出的历史加权场”，则

`I_K = I_{Mashhoon}`，

不是新命题。

未被 Mashhoon 自动覆盖的余地很窄：`K` 必须不是单个加速观测者的局域历史读出，而是多路径/多边网络上的传播-响应核，并且 cycle residual 不能归约为每个节点的 tetrad/readout 历史。

--- INSPECTOR_CHECK ---
[公式] `F_obs(lambda)=F_inst(lambda)+\int_{lambda0}^{lambda} M(lambda,lambda')F_inst(lambda')d lambda'`；`K_M^{abcd}(x,x') ~ int d tau' delta_V(x',z(tau')) M^{abcd}(tau,tau') Theta(tau-tau')`。`lambda,tau` 单位 s；`M d tau'` 无量纲或与本构映射单位匹配；`delta_V` 按 `dV` 归一化，使 `K dV` 与 `chi` 同量纲。
[方向] 单世界线历史 kernel 被 Mashhoon/Hehl 覆盖；多路径 cycle kernel 尚需额外判别。
[数据] DOI `10.1016/s0375-9601(00)00316-9`, `10.1002/andp.200310028`, `10.1002/andp.200810308`, `10.3390/universe6120229`。
[假设] 线性响应、因果支持、观测者历史可参数化为世界线加速度/转动。
---

## 2. `chi(omega,k)` 是否能吸收 toy `K`？

结论：若 toy `K` 是平移不变或统计均匀的线性介质核，则被吸收。

一般非局域线性介质：

`H^{ab}(x)=1/2 \int K^{abcd}(x-x')F_cd(x')d^4x'`。

Fourier 变换给出：

`H^{ab}(omega,k)=1/2 chi^{abcd}(omega,k)F_cd(omega,k)`，

其中

`chi^{abcd}(omega,k)=\int d^4xi exp[i(omega xi^0-k·xi)] K^{abcd}(xi)`。

所以 Round1 toy 中的边残差 `r_e` 若只是不同边的 `chi_e(omega,k)` 取值差，或者每条边局部可赋一个 dispersive transfer matrix `T_e(omega,k)`，则 cycle syndrome

`sigma = B r`

只是网络中不同介质段的频散失配，不是基础物理 residual。

未被吸收的必要条件：

`K_e(x,x')` 不能同时满足所有边的共同平移不变/局部平衡假设；并且 `sigma` 不能由边介质参数的普通不均匀性解释。换言之，R2 必须证明：

`r notin im D + im L_chi(omega,k)`。

这里 `D` 是 endpoint calibration coboundary，`L_chi` 是所有允许频散/空间色散本构模板生成的边响应空间。

## 3. 开放系统/测量协议 kernel 是否把 R2 推成装置建模？

结论：是。若 `K` 来自 readout、滤波、环境消去或 detector backaction，R2 不再是基础真空几何命题。

开放系统中常见形式：

`S_eff[F]=S_EM[F]+1/2 \int F(x) Pi_ret(x,x') F(x') dV_x dV_{x'} + noise`。

`Pi_ret` 是 action 二次核；只有经过变分并换算到本构响应后，才能与 `K` 比较。若 LP23 的 `K` 等价于这类 retarded response、detector response function、Green tensor reconstruction kernel 或采样窗口核，则可观测 `I_K` 依赖装置选择：

`I_K = I_K[detector, filter, environment, reconstruction]`。

这不是“真空螺旋世界线/bridge quotient”的基础命题，而是“给定装置网络的系统辨识”。

因此开放系统方向不是活口，而是降级条件：它可用于构造可测 toy，但会牺牲基础物理声称。

## 4. 最小可发表命题是否存在？

强命题判死：

“非局域 `K(x,x')` memory residual 是标准理论之外的新基础物理”当前判死。

死因：

1. 单世界线历史依赖被 Mashhoon/Hehl 覆盖。
2. 平移不变/局域平衡非局域介质被 `chi(omega,k)` 覆盖。
3. 局域极限被 `chi^{abcd}` 覆盖。
4. helicity/frequency `O(1/omega)` 残差被 spinoptics 覆盖。
5. 协议诱导 kernel 属于开放系统/装置建模，不是基础真空 residual。

窄命题存活，但必须降级为“非局域响应网络的 endpoint-calibration quotient diagnostic”：

给定有向图 `G=(V,E)`，每条边是一条传播路径或路径束。边响应

`r_e = P_e [ \int K_e(x,x') F(x') dV_{x'} ] - P_e [ \int K_e^0(x,x') F(x') dV_{x'} ]`。

endpoint calibration 为节点 0-cochain `a_v`，边上作用为

`(Da)_e = a_{t(e)} - a_{s(e)}`。

最小不变量：

`I_K = || (I - D(D^T D)^+D^T) r ||^2`

其单位为 `[r]^2`；若 `r` 是偏振角/Jones phase，则为 `rad^2`。跨实验比较时应使用噪声协方差白化版本 `||C_noise^{-1/2} r_perp||^2`。

或等价的 cycle syndrome

`sigma_c = \sum_{e in c} r_e`。

存活判据：

`I_K != 0` 且 `r notin im D + im L_local_chi + im L_spinoptics + im L_Mashhoon + im L_chi(omega,k)`。

这不是“发现新 `K` 理论”，而是一个分类/排除定理：在给定候选模板族后，cycle residual 可以判定某个网络响应不能被 endpoint calibration 与标准本构模板同时吸收。

## 最小 `K` 形式、可观测量、下一轮必须计算

若 PI 选择保留窄命题，最小 `K` 应避免被 `chi(omega,k)` 立即吸收，因此不能取全局平移不变卷积核。建议取三边环：

`K_e^{abcd}(x,x') = chi_0^{abcd} delta_V(x,x') + epsilon P_e^{abcd} Theta(t-t') exp[-(t-t')/T_e] delta_{tube(e)}(x,x')`。

约束：

1. `P_e^{abcd}` 不是所有边共享的同一张量。
2. `T_e` 随边或历史窗口变化，破坏单一 `chi(omega,k)` 描述。
3. `K_e` 不沿单个探测器世界线支持，避免退化成 Mashhoon kernel。
4. `P_e,T_e` 必须来自传播段物理，而不是 detector filter；否则降级为装置模型。

可观测量：

`r_e = theta_e[K_e] - theta_e[K_e^0]`，

其中 `theta_e` 是同一入射 Stokes 数据下的偏振角或 Jones phase shift。对三边环：

`I_K = (1/3)(r_1+r_2+r_3)^2`

在欧氏边内积规范下等价于 toy script 的正交投影范数平方。当前 toy 数值：

`r=[0.10,-0.04,0.08]`，`sigma=0.14`，`I_K=0.00653333`。

下一轮必须计算的公式：

1. 对上述指数核求一阶响应：

   `delta theta_e = epsilon Im <s_out| J_0^{-1} delta J_e |s_in> / <s_out|s_out>`

   其中

   `delta J_e(omega) proportional P_e / (1/T_e - i omega)`。

2. 构造模板投影：

   `Pi_standard = Pi_span(D, L_chi, L_spin, L_M, L_disp)`，即对联合模板列空间的一次正交投影；然后

   `r_perp = (I - Pi_standard) r`。

3. 生死判据：

   `I_K = ||r_perp||^2`，单位为 `[r]^2`；若需无量纲比较，使用白化范数 `||C_noise^{-1/2} r_perp||^2`。

   若 `I_K=0`，R2 全部判死；若 `I_K>0`，只能声称“该网络响应不在指定标准模板张成空间内”，不能声称发现基础真空新自由度。

## 深挖1：本轮结论的下一层后果

第一层后果：LP23-R2 不能再用“非局域 `K`”本身作为新颖性。`K` 是标准线性响应语言，必须把新颖性移到商空间判据：

`response / {endpoint calibration + standard response templates}`。

第二层后果：论文结构若继续推进，应写成 no-go + diagnostic，而不是 discovery paper。核心定理应是：

若 `r in im D + im L_standard`，任何 bridge residual 都是假阳性；只有 `r_perp != 0` 才值得进入物理解释。

第三层后果：即便 `r_perp != 0`，它也首先说明模板族不完备，而不是说明基础物理被突破。需要额外实验/模型排除装置 filter、环境、介质不均匀、频散张量拟合。

## 深挖2：本轮依赖前提中最可能错的是哪一个？

第一层可疑前提：`L_standard` 可以被有限模板张成。真实介质/仪器的响应空间可能太大，导致任何有限维 `r_perp` 都只是模板不足。

第二层可疑前提：边响应 `r_e` 可以定义成同一可观测空间中的标量。若不同路径的 Jones/Stokes 基底、相干性、带宽、噪声模型不同，则把它们放入同一图 cochain 已经引入额外校准选择。

第三层可疑前提：`K_e` 能被归因于传播段而非探测协议。实际测量中最容易产生 memory residual 的正是锁相、积分窗口、重建算法和 detector response；若不能独立标定这些项，`I_K` 会变成仪器系统误差指标。

硬边界：下一轮若不能显式构造联合模板空间 `span(D,L_chi,L_spin,L_M,L_disp)` 并证明 toy 的 `r_perp=(I-Pi_standard)r` 非零，则 R2 应完全判死。

## 本轮成果

本轮成果：非局域 `K(x,x')` 作为基础新物理活口判死；作为 endpoint-calibration quotient diagnostic 的窄命题条件存活。

新增引用文献：Muench/Hehl/Mashhoon DOI `10.1016/s0375-9601(00)00316-9`；Mashhoon DOI `10.1002/andp.200310028`, `10.1002/andp.200810308`, `10.3390/universe6120229`；Landau-Lifshitz DOI `10.1016/b978-0-08-030275-1.50018-7`；Agranovich-Ginzburg DOI `10.1016/s0079-6638(08)70047-7`, `10.1007/978-3-662-02406-5`；Keller DOI `10.1007/978-3-642-17410-0_10`, `10.1007/978-3-642-17410-0_12`；Calzetta-Hu DOI `10.1017/cbo9780511535123`, `10.1017/9781009290036`；Feist/Fernandez-Dominguez/Garcia-Vidal DOI `10.1515/nanoph-2020-0451`。

最弱环节：`L_standard` 的模板投影尚未计算；当前 toy 只证明图代数 residual，不证明物理 residual。

下一步计划：计算 `r_perp=(1-Pi_standard)r`，其中 `Pi_standard` 至少包含 endpoint coboundary、local `chi`、spinoptics、Mashhoon worldline kernel、`chi(omega,k)` dispersion kernel。

需要 PI 投喂的文献方向：`Volterra nonlocal electrodynamics kernel equivalence`, `spatial dispersion inverse problem chi omega k`, `polarization network calibration cohomology`。
