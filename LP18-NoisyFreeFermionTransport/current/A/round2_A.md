# LP18 Round 2 - A博士：strong-dephasing projection for power-law/shortcut hopping

角色：A博士（学院派）。本轮只审查 Round 1 提出的长程 hopping 增量：在强退相干/Quantum Zeno 极限下，`J_{jk}` 是否给出有效经典长跳率 `r_eff(j,k) ~ |J_{jk}|^2/gamma`，以及 `J(r)~r^{-alpha}` 是否严格导出 `alpha=3/2` 的扩散-分数扩散边界。

## §-1 先发文献检索

检索工具：paper-search-mcp。检索时间：2026-06-03。

### 检索组1：开放量子系统的 Zeno/绝热消元/Schrieffer-Wolff-Lindblad

命中：
- Azouit, Sarlette, Rouchon, "Adiabatic elimination for open quantum systems with effective Lindblad master equations", CDC 2016, DOI 10.1109/CDC.2016.7798963。
- Albert, Bradlyn, Fraas, Jiang, "Geometry and Response of Lindbladians", Phys. Rev. X 6, 041031 (2016), DOI 10.1103/PhysRevX.6.041031。
- Malekakhlagh, Magesan, Govia, "Time-dependent Schrieffer-Wolff-Lindblad perturbation theory", Phys. Rev. A 106, 052601 (2022), DOI 10.1103/PhysRevA.106.052601。

用途：这些文献支持把强耗散 Liouvillian 的慢子空间投影写成二阶有效生成元

`L_eff = P L_1 P - P L_1 Q (Q L_0 Q)^{-1} Q L_1 P + ...`

其中 `L_0` 是强退相干，`L_1=-i[H_J,.]` 是 hopping 扰动。对于纯退相干问题，`P L_1 P=0`，所以第一非零项是二阶。

### 检索组2：长程 hopping + dephasing 的数值/解析边界

命中：
- Sarkar, Agarwalla, Bhakuni, "Impact of dephasing on nonequilibrium steady-state transport in fermionic chains with long-range hopping", arXiv:2310.01323v2 / Phys. Rev. B 109, 165408 (2024), DOI 10.1103/PhysRevB.109.165408。
- Z̆nidarič, "Superdiffusive magnetization transport in the XX spin chain with nonlocal dephasing", Phys. Rev. B 109, 075105 (2024), DOI 10.1103/PhysRevB.109.075105。

用途：R8 明确报告 `J(r)~1/r^alpha` 的退相干自由费米链在 `alpha_c approx 1.5` 附近从扩散转向超扩散；但该文的 `alpha_c` 是数值/电流算符范数判据，不等同于本轮要给出的严格投影定理。

### 检索组3：长跳排斥过程、分数 Laplacian、边界驱动

命中：
- Jara, "Nonequilibrium scaling limit for a tagged particle in the simple exclusion process with long jumps", Commun. Pure Appl. Math. 62, 198-214 (2009), DOI 10.1002/cpa.20253；相关 arXiv:0805.1326v2。
- Bernardin, Jimenez Oviedo, "Fractional Fick's law for the boundary driven exclusion process with long jumps", ALEA 14, 473 (2017), DOI 10.30757/alea.v14-25 / arXiv:1603.01234v3。
- Jimenez Oviedo, Ramirez Jimenez, "Hydrostatic limit for the symmetric exclusion process with long jumps: super-diffusive case", Revista de Matematica 28, 79-94 (2020), DOI 10.15517/rmta.v28i1.36294。

用途：这些文献给出经典长跳排斥过程的标准参数化：一维跳核 `p(r)~|r|^{-(1+mu)}` 在 `0<mu<2` 时导向分数 Laplacian；若二阶矩有限，则恢复普通 Laplacian 扩散。

## §0 框架声明

采用成熟框架：Lindblad 强耗散绝热消元 + classical long-jump exclusion hydrodynamics。

本轮不重新证明 R1 的 QSSEP gauge trick，而是检查它的前置条件：强退相干后得到的有效经典生成元是否仍是短程 Laplacian 型。若 power-law hopping 投影后产生二阶矩发散的长跳核，则 R1 的 diffusive local MFT/gauge closure 即使在自由费米和 U(1) 守恒下也不应作为 leading large-L FCS 的默认极限。

## 1. Zeno 投影：`r_eff ~ |J|^2/gamma` 的系数、单位、条件

考虑单粒子或自由费米相关矩阵的最小块。Hamiltonian

`H_J = sum_{j != k} J_{jk} c_j^\dagger c_k`

与局域退相干

`L_deph[rho] = gamma sum_l D[n_l][rho]`

其中 `D[A]rho = A rho A^\dagger - (1/2){A^\dagger A,rho}`。在单粒子密度矩阵表示中，人口 `p_j=rho_{jj}` 位于慢子空间，非对角相干 `rho_{jk}` 位于快子空间。对 `j != k`，

`dot rho_{jk} = -i J_{jk}(p_k-p_j) - gamma rho_{jk} + O(J rho_off)`

因为 `D[n_j]` 与 `D[n_k]` 各给相干项 `-gamma/2`，合计相干衰减率为 `gamma`。绝热消元给

`rho_{jk} = -i J_{jk}(p_k-p_j)/gamma + O(J^2/gamma^2)`。

代回人口方程

`dot p_j = sum_{k != j} 2 |J_{jk}|^2/gamma (p_k-p_j) + O(J^3/gamma^2)`。

因此，在本文采用的 Lindblad 规范 `gamma D[n_j]` 下，有效对称长跳率是

`r_{j->k}=r_{k->j}=2 |J_{jk}|^2/gamma`。

这比 Round 1 的 `~ |J|^2/gamma` 多一个可审查的数值因子 2。若某文献把退相干参数定义为相干衰减率 `Gamma_phi=gamma`，则公式为 `2|J|^2/Gamma_phi`；若把 Lindblad 写成 `(gamma/2)D[n_j]` 或把噪声 Hamiltonian 方差改写，因子会随约定移动。稳定结论不是前因子，而是二阶标度 `|J|^2/(coherence decay rate)`。

多体自由费米情形下，由 Pauli 排斥把人口主方程提升为对占据变量的对称排斥过程：

`L_eff f(eta)=sum_{j<k} r_{jk} eta_j(1-eta_k)[f(eta^{j,k})-f(eta)] + r_{jk} eta_k(1-eta_j)[f(eta^{k,j})-f(eta)]`

其中 `r_{jk}=2|J_{jk}|^2/gamma`。这个提升依赖 quadratic/U(1) 守恒结构；若 hopping 带相互作用或噪声不测量局域密度，则不能直接套用。

--- INSPECTOR_CHECK ---
[公式] `r_{jk}=2|J_{jk}|^2/gamma_phi`，SI 单位为 `s^{-1}`；这里 `J_{jk}` 与 `gamma_phi` 都取角频率单位 `s^{-1}`，若 Hamiltonian 写成能量单位则 `J/hbar` 进入公式。
[方向] Round 1 的 `r_eff ~ |J|^2/gamma` 在标度上成立，但严格写法必须注明退相干规范；在 `gamma sum_l D[n_l]` 规范下前因子为 2。
[数据] Azouit/Sarlette/Rouchon 2016 的开放系统绝热消元框架；Albert/Bradlyn/Fraas/Jiang PRX 2016 的 Lindbladian 投影响应；Malekakhlagh/Magesan/Govia PRA 2022 的 Schrieffer-Wolff-Lindblad 扰动；本轮二能级块显式消元。
[假设] `gamma_phi >> sup_j sum_k |J_{jk}|` 或至少 `|J_{jk}|/gamma_phi << 1` 且快子空间存在耗散 gap；Markovian 纯退相干；无能量失谐。若有 onsite detuning `Delta_{jk}`，分母应改成 `gamma_phi^2+Delta_{jk}^2` 型。

## 2. `J(r)~r^{-alpha}` 到长跳核：二阶矩条件与 `alpha=3/2`

取一维平移不变 bulk，

`J(r)=J0/|r|^alpha`。

Zeno 投影后

`r(r)=2 J0^2/(gamma |r|^{2alpha})`。

经典长跳排斥文献通常写

`p(r) ~ |r|^{-(1+mu)}`。

因此一维中

`1+mu = 2alpha`，即 `mu=2alpha-1`。

普通扩散要求跳分布二阶矩有限：

`M_2 = sum_{r in Z} r^2 r(r) ~ sum_{r>=1} r^{2-2alpha} < infinity`。

该级数收敛当且仅当

`2-2alpha < -1`，即 `alpha > 3/2`。

所以在一维、未归一化 power-law hopping、Zeno 二阶投影成立、bulk 平移不变且没有额外 Kac 归一化时，`alpha=3/2` 是二阶矩边界。它不是任意维度的通用数值。若在 `d` 维中 `J(x)~|x|^{-alpha}` 且 shell degeneracy 计入，则

`M_2 ~ int^\infty dr r^{d-1} r^2 r^{-2alpha} = int^\infty dr r^{d+1-2alpha}`

收敛条件变为

`alpha > (d+2)/2`。

等价地，若把 `d` 维稳定过程写成核 `p(x)~|x|^{-(d+mu)}`，则 `mu=2alpha-d`，分数区间 `0<mu<2` 对应

`d/2 < alpha < (d+2)/2`。

还要分出低 `alpha` 的可定义性边界。总跳率

`R=sum_{r !=0} r(r) ~ sum_r |r|^{-2alpha}`

在一维要求 `alpha>1/2` 才有限；在 `d` 维要求 `alpha>d/2`。若 `alpha<=d/2`，无限体 bulk Markov 生成元本身需归一化或截断，不能简单说是分数扩散。

边界与归一化会移动观测标度但不移动未归一化 bulk 二阶矩判据：
- 有限链截断 `r<=L` 时，`M_2(L)~L^{3-2alpha}`，所以 `alpha<3/2` 的扩散常数随系统尺寸发散。
- Kac 归一化若令 `J0=J0(L)` 随 `L` 缩放，可人为恢复有限总能标；这会改变 current variance 的 `L` 标度，必须在命题中排除或单独声明。
- 开边界 reservoir 若允许从 reservoir 到 bulk 的长跳注入，边界算子也会变成非局域；Bernardin-Jimenez 的 fractional Fick law 适合这种边界驱动长跳过程，但具体 conductance 依赖 reservoir 实现。

--- INSPECTOR_CHECK ---
[公式] 一维 `J(r)=J0 r^{-alpha}` 给 `r(r)=2J0^2/(gamma r^{2alpha})`；二阶矩 `sum_r r^2 r(r)<infty` 当且仅当 `alpha>3/2`。`d` 维阈值为 `alpha>(d+2)/2`。
[方向] `alpha=3/2` 是一维未归一化 power-law hopping 的严格二阶矩阈值；它不是维度无关阈值，也不自动覆盖边界长跳和 Kac 归一化模型。
[数据] Sarkar/Agarwalla/Bhakuni PRB 109, 165408 (2024) 的 `alpha_c approx 1.5` 数值边界；Jara CPAM 62, 198 (2009)；Bernardin/Jimenez ALEA 14, 473 (2017) 的长跳排斥/分数 Fick law。
[假设] 平移不变 bulk；`J0` 不随 `L` 缩放；Zeno 投影先于热力学极限有效；计数电流定义为跨 cut 的所有长跳之和，而不是最近邻 bond current。

## 3. 对 R1 universality 的精确影响

若 `alpha>3/2`，`M_2` 有限。Zeno 后的有效排斥过程在长波长极限仍应是普通 Laplacian 扩散，扩散常数重整为

`D_eff = (1/2) sum_r r^2 r(r) = (J0^2/gamma) sum_{r>=1} r^{2-2alpha}`

按对称连续时间随机游走规范。此时 R1 的 SSEP CGF 仍可能作为 leading large-L 结果保留，但扩散时间单位和 conductance 需乘以 `D_eff`；严格等价还要检查 long but finite second-moment jumps 是否破坏 R1 的 local gauge trick。我的判断：leading hydrodynamics 大概率不破坏，但 finite-size correction 会带长尾依赖。

若 `1/2<alpha<3/2`，总跳率有限但二阶矩发散。有效经典过程属于 long-jump exclusion，hydrodynamic generator 应是分数 Laplacian，稳定指数

`mu=2alpha-1 in (0,2)`。

此时 ordinary SSEP 的 `lambda''(0)~L^{-1}` 不应作为 leading 标度。边界驱动分数 Fick law 给出的自然可检验量是 conductance 标度

`lambda''(0) ~ conductance_mu(L)`。

粗略按分数扩散跨长度 `L` 的时间尺度 `t_L~L^mu` 与系统粒子数 `L` 估计，穿越电流标度应从普通扩散的 `L^{-1}` 改为更慢衰减的 `L^{-(mu-1)}` 当 `1<mu<2`，即

`lambda''(0) ~ L^{-(2alpha-2)}` for `1<alpha<3/2`。

这与 Round 1 的候选式一致，但必须标为待验证：当 `mu<=1` (`alpha<=1`) 时，边界到 bulk 的非局域耦合和平均穿越时间可能导致对数或更强异常，R8 也报告 `alpha<=1` 与 `1<alpha<1.5` 有不同 resistance scaling。

若 `alpha<=1/2`，未归一化无限体总跳率发散。该区间不是单纯 fractional-SSEP，而是模型定义需重整化或有限尺寸截断。对发表命题而言，第一篇不应把这个区间作为主战场。

## 4. Shortcut hopping 的特例

若只加入有限数量 shortcut，例如 `J_{ab}=J_s` 连接远距两点，Zeno 投影给单条额外经典交换边

`r_s=2|J_s|^2/gamma`。

这不会造成 bulk 二阶矩发散，因为长跳边数不随距离壳层形成幂律尾。它造成的是图 Laplacian 从一维链变成带一条非局域边的网络扩散。对 leading conductance 的影响取决于 shortcut 数量如何随 `L` 缩放：
- 固定一条 shortcut：改变有限尺寸 FCS 和局域 profile，通常不是新的 bulk universality。
- `O(L)` 条 shortcut 或小世界分布：有效维度/图谱 gap 改变，可破坏 `lambda''(0)~L^{-1}`，但阈值不再是 `alpha=3/2`，而是 shortcut 网络的谱维数问题。

本轮 A 侧不进入 B 的 holonomy/FCS 产出；这里只记录学院派结论：Zeno 投影后的 shortcut 是 classical graph-exclusion 的额外边。若边权带 Peierls 相位，人口级二阶 Zeno 率只含 `|J_s|^2`，相位不在 leading population generator 中出现；相位若进入 FCS，应来自更高阶 coherent loops 或 tilted counting 的非交换结构。

## 5. Round 3 可计算对象

我建议 Round 3 选一个最小可算对象，不同时攻 CGF 全函数。

### 对象A：current variance scaling

模型：长度 `L` 开链，bulk `J_{jk}=J0/|j-k|^alpha`，局域退相干 `gamma D[n_j]`，左右 Markovian reservoirs 固定密度 `rho_L,rho_R`，取强退相干 `gamma >> J0`。

计算步骤：
1. 先构造 classical long-jump exclusion rates `r_{jk}=2J0^2/(gamma |j-k|^{2alpha})`。
2. 对单粒子线性问题求稳态 profile 与穿越 cut current；低密度极限已足以给 conductance scaling。
3. 比较 `lambda''(0)` 或零频 current noise 的系统尺寸标度：
   - `alpha>3/2`: `lambda''(0) ~ L^{-1}`。
   - `1<alpha<3/2`: 候选 `lambda''(0) ~ L^{-(2alpha-2)}`。
   - `alpha=3/2`: 候选边界 `lambda''(0) ~ (log L)/L` 或等价对数修正，需由截断二阶矩 `M_2(L)~log L` 验证。

### 对象B：fractional Laplacian conductance

把 Zeno 后的 continuum generator 写成

`L_mu rho(x)=c_mu PV int_0^1 [rho(y)-rho(x)]/|x-y|^{1+mu} dy + reservoir terms`

其中 `mu=2alpha-1`。求解分数 Dirichlet/外部 reservoir 边值问题，提取稳态通量。优点是直接连接 Bernardin-Jimenez 的 fractional Fick law；缺点是边界实现必须严格匹配，不能混用普通 Dirichlet reservoir。

### 对象C：数值最小模型

用二次 Lindblad correlation-matrix 方程直接算原始量子模型，再与 Zeno classical rates 对比：

`dot C = -i[h,C] - gamma( C - diag C ) + L_bath(C)`

扫描 `L=32...1024`、`alpha`、`gamma/J0`。先测平均电流与二阶 cumulant，不求全 CGF。通过 `gamma` 扫描确认 `2|J|^2/gamma` 的 Zeno 率窗口：`J0/gamma` 太大时 coherent long-range effects 会污染 `alpha=3/2` 判据。

## 6. 深挖1：本轮结论的下一层后果

第一层后果：若 `alpha=3/2` 是 Zeno 后长跳核的二阶矩边界，则 R1 universality 的真实前提不是笼统的 "quasi-local hopping"，而是更具体的 "Zeno-projected jump kernel has finite second moment"。这把 quantum free-fermion 问题转化成 classical exclusion 的 domain-of-attraction 分类。

第二层后果：这个分类会改变 FCS 的自然缩放变量。普通 SSEP 使用 diffusive time `t~L^2` 与 CGF `lambda~L^{-1}`；长跳区间应改用 `t~L^mu`。若仍用 R1 的 `tilde lambda=(gamma L/2)lambda`，会把分数区间的 leading term 错判为发散或消失。因此 Round 3 必须先确定 rescaled CGF 的正确 `L` 幂，而不是直接比较 arccosh/arccos 函数形状。

第三层后果：在 `alpha>3/2` 侧，若只看 leading `L^{-1}`，R1 可能幸存；但在临界附近 `D_eff(alpha) ~ 1/(2alpha-3)` 发散，有限系统会有很宽 crossover。实验或数值上看到 `alpha_c approx 1.5` 不应被解释为尖锐相变，而应先解释为截断二阶矩控制的 crossover fixed point。

## 7. 深挖2：本轮依赖前提中最可能出错的一项

第一层风险：最可能出错的前提是 "Zeno 投影可在 power-law hopping 的热力学极限前逐项进行"。强退相干小参数不是单个 `J_{jk}/gamma`，而更接近 `sum_k |J_{jk}|/gamma` 或谱范数 `||h||/gamma`。一维 `sum_r r^{-alpha}` 只在 `alpha>1` 收敛；在 `alpha<=1`，即使每条远程边很弱，总 coherent 带宽也可能随 `L` 增长，导致先取 `L->infty` 与先取 `gamma->infty` 不交换。

第二层风险：如果 `||h_L||/gamma` 随 `L` 不小，则二阶 population generator 不是均匀有效近似。这样 `alpha<=1` 区间的异常输运可能不是 classical long-jump exclusion，而是残余 coherent shortcut 网络与退相干竞争的结果。硬边界：本轮推导对 `alpha>1` 最可靠；对 `1/2<alpha<=1` 只作为有限 `L`、固定 `gamma` 下的候选，不应声称严格 hydrodynamic 定理。

第三层风险：reservoir 的建模可能改变边界指数。若 reservoir 只接触端点，而 bulk 允许长跳跨越大部分系统，则 "跨右边界电流" 与 "跨中间 cut 电流" 的等价性弱于最近邻链。Round 3 的数值必须同时报告 reservoir current 与 cut current；若二者 scaling 不同，说明 R1 的 gauge-current equivalence 已经在非局域电流定义处失效。

## §末 产出格式

本轮成果：在 Lindblad 规范 `gamma sum_j D[n_j]` 下，strong-dephasing/Zeno 投影给出有效经典排斥长跳率 `r_{jk}=2|J_{jk}|^2/gamma`；对一维 `J(r)~r^{-alpha}`，有效核 `r(r)~r^{-2alpha}` 的二阶矩有限当且仅当 `alpha>3/2`，因此 `alpha=3/2` 是一维未归一化 power-law hopping 的严格二阶矩阈值，但不具备维度无关性。

新增的引用文献：
- Azouit, Sarlette, Rouchon, DOI 10.1109/CDC.2016.7798963。
- Albert, Bradlyn, Fraas, Jiang, Phys. Rev. X 6, 041031 (2016), DOI 10.1103/PhysRevX.6.041031。
- Malekakhlagh, Magesan, Govia, Phys. Rev. A 106, 052601 (2022), DOI 10.1103/PhysRevA.106.052601。
- Sarkar, Agarwalla, Bhakuni, arXiv:2310.01323v2 / Phys. Rev. B 109, 165408 (2024), DOI 10.1103/PhysRevB.109.165408。
- Jara, Commun. Pure Appl. Math. 62, 198-214 (2009), DOI 10.1002/cpa.20253；相关 arXiv:0805.1326v2。
- Bernardin, Jimenez Oviedo, arXiv:1603.01234v3 / ALEA 14, 473 (2017), DOI 10.30757/alea.v14-25。
- Jimenez Oviedo, Ramirez Jimenez, DOI 10.15517/rmta.v28i1.36294。

最弱的环节：Zeno 投影对 long-range hopping 的热力学极限是否均匀有效，尤其是 `alpha<=1` 时 `sum_r |J(r)|` 或 hopping 谱范数随 `L` 增长，可能使 `gamma->infty` 与 `L->infty` 不可交换。

下一步计划：Round 3 优先计算 current variance/conductance scaling。先用 classical rates `r_{jk}=2J0^2/(gamma |j-k|^{2alpha})` 求边界驱动 long-jump exclusion 的 `lambda''(0)` 标度，验证 `alpha>3/2: L^{-1}`、`1<alpha<3/2: L^{-(2alpha-2)}`、`alpha=3/2: (log L)/L`；再用 correlation-matrix Lindblad 数值检查原始量子模型在有限 `gamma` 下何时偏离 Zeno 预测。

需要PI投喂的文献方向：`fractional macroscopic fluctuation theory current large deviations`, `boundary driven long jump exclusion current variance`, `open quantum systems adiabatic elimination strong dephasing transport`, `long range hopping Lindblad correlation matrix dephasing alpha 3/2`, `fractional Laplacian conductance interval reservoirs`。
