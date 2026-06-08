# B博士 round1：从分布式共识/纠错码攻击 Q-SSEP 普适性边界

## §0 框架声明

我的框架：计算机科学，具体取两个看似远离输运物理的结构：

1. 分布式共识中的拜占庭一致性/leader election：局域节点只看邻居消息，但全局一致性可能被网络环路、延迟和少数坏边破坏。
2. 纠错码中的 syndrome 与 stabilizer：局域误差可被局域校验吸收，但环绕非平凡 cycle 的误差不一定是局域 syndrome，可能成为 logical error。

我借来的数学结构不是“计算机也有噪声”这种表面类比，而是：

> 局域 gauge 消去等价于把每条测量边的 counting field 视为 exact 1-cochain；只要网络没有非平凡环路，或所有环路 holonomy 为零，局域 gauge trick 就能把输运统计约化为 SSEP。若存在非局域跳跃、多路径网络或带相位的长程边，则 counting/gauge field 的 curl 可能不为零，留下无法局域消去的 cycle syndrome。

这条路避开标准 MFT/Gauge trick 正路，不问“leading hydrodynamics 是否扩散”，而问“把 counting field 当作局域规范自由时，是否隐含了 cohomology triviality”。

## 1. 跨学科跳跃：共识协议里的环路故障

动作1 - 跨学科跳跃：

分布式共识中，树状通信图上的一致性很容易被局域消息传递建立；但在含环网络上，若沿不同路径传回的消息存在不可协调的相位/版本号差异，就会出现全局不一致。局部看每条边都像合法消息，全局绕一圈才暴露矛盾。

动作2 - 物理翻译：

把 noisy free fermion 网络写成图 G=(V,E)，边 e=(ij) 上有 hopping J_e、噪声/退相干强度 gamma_e 和 counting/gauge field a_e。Gauge trick 能否把 a_e 推到边界，取决于 a 是否是某个顶点势 phi 的差分：

a_e = phi_i - phi_j。

若存在 cycle C，使得

Phi_C = sum_{e in C} a_e mod 2pi != 0，

则 a 不是 exact 1-cochain，而是带有非平凡 holonomy 的 1-cochain。此时“所有 counting field 都可局域 gauge 掉”的共识条件失败。

动作3 - 落地：

物理上可落到一个最小模型：一维链加一条长程 shortcut，形成一个单环图。reservoir 仍接在左右端，bulk 是 U(1) 守恒自由费米子和强噪声。若 shortcut 形成的环承载非零 Phi_C，则 CGF 不应只由左右端化学势和链长决定，还应出现对 cycle holonomy 或图的第一 Betti 数 b1(G) 的依赖。

--- INSPECTOR_CHECK ---
[公式] Phi_C = sum_{e in C} a_e mod 2pi；预测 Delta lambda(s) = lambda_G(s, Phi_C) - lambda_SSEP(s) = A(G,gamma,J) [1 - cos(Phi_C)] F(s) + o(A)，lambda 与 A(G,gamma,J) 单位均为 s^-1，Phi_C 与 F(s) 无量纲；若改用归一化 CGF tilde lambda=lambda/A，则 tilde lambda 无量纲。
[方向] 若图存在非平凡 cycle 且 counting/gauge field 在 cycle 上有非零 holonomy，则 gauge trick 的 SSEP 等价只在 exact sector 成立；non-exact sector 留下可测 CGF 修正。
[数据] 使用当前项目文献库 R1 的 gauge trick/SSEP 等价边界、C2 的 long-range hopping 边界；本轮未引入新外部数据。
[假设] 自由费米子、U(1) 守恒、强噪声仍成立；新增假设是几何图含 shortcut/cycle，且 counting field 或 hopping phase 沿 cycle 的总和不可由顶点重定义消去。

## 2. 攻击路径：Gauge trick = 测量边的共识选择

标准路线会说：counting field 可以通过 gauge transformation 移动，最后只剩边界差。我的野路子翻译是：

> gauge trick 不是纯代数技巧，而是一次“测量边 leader election”：系统选择哪条边承载计数相位。如果图是树，leader election 无冲突；如果图有多个路径，leader election 需要所有回路给出同一版本号。

于是边界命题改写为：

### 边界命题 B1：SSEP 等价需要 counting 1-form 的零曲率条件

设图 G 的边 counting field 为 a。若 H^1(G) = 0，或 a 在所有 cycle 上的积分为零，则可期待 R1 的 gauge trick 延续。若 H^1(G) != 0 且存在 cycle C 满足 Phi_C != 0，则 leading SSEP CGF 之外允许出现拓扑扇区修正：

lambda_G(s) = lambda_SSEP(s; G_eff) + sum_{alpha=1}^{b1(G)} K_alpha(L,gamma,J) [1 - cos Phi_alpha] F_alpha(s) + ...

其中 b1(G)=|E|-|V|+c 是图的第一 Betti 数，c 是连通分支数；本轮最小模型是连通图，所以退化为 b1(G)=|E|-|V|+1。K_alpha 是由 shortcut 权重、噪声强度和环长控制的速率幅度，单位 s^-1；F_alpha(s) 无量纲。

这不是说主导扩散一定被推翻；更尖锐的说法是：即使主导扩散仍是 SSEP，FCS 的亚领先项会携带“共识失败 syndrome”。这正好落在项目成功标准的“可测亚领先量”。

### 最小可检验模型

取 N 个点的一维链，边 (i,i+1) 的 hopping 为 J，另加 shortcut 边 (p,q) 的 hopping 为 J_l，q-p = ell。shortcut 与链段形成单个 cycle。对 shortcut 或链段施加 Peierls 相位 theta，并在左右端做电荷 FCS。

预测：

1. 当 J_l = 0 或 theta = 0 mod 2pi 时，lambda(s) 回到 SSEP 基线。
2. 当 J_l != 0 且 theta != 0 mod 2pi 时，Delta lambda(s,theta) 的最低阶角依赖是偶函数 1-cos theta，而不是线性 theta。
3. 若 shortcut 是弱边，幅度应满足 K ~ (|J_l|^2/gamma) times P_hit(p,q; reservoirs)，其中 P_hit 是环路被输运轨迹访问的网络因子；它不是单纯局域边界项。
4. 有限尺寸 scaling 可能不是 R1 的纯 1/L 亚领先，而是

Delta lambda_top(s) ~ L^{-1} (ell/L)(1-ell/L) (|J_l|^2/gamma) [1-cos theta] F(s)

或在弱耦合、稀疏 cycle、不同 shortcut 共享边很少的条件下，近似独立累加为 b1(G)/L 控制的修正；交叉项按 J_l^4/gamma^2 或 cycle 重叠度进一步压低。若 b1(G) 随 L 增长，修正可能从“亚领先”升为可见的 leading renormalization。

--- INSPECTOR_CHECK ---
[公式] 一般图 b1(G)=|E|-|V|+c，连通图 c=1 时 b1(G)=|E|-|V|+1；Delta lambda_top(s) ~ L^-1 (ell/L)(1-ell/L)(|J_l|^2/gamma)[1-cos theta]F(s)。lambda 单位 s^-1；|J_l|^2/gamma 单位 s^-1；L、ell、theta、F(s) 无量纲。
[方向] 单个 shortcut 预言 CGF 对环路相位 theta 有偶函数修正；多 shortcut 只在弱耦合、稀疏 cycle、cycle 重叠交叉项可忽略时，才可按独立 cycle 数或 cycle basis 近似加权。
[数据] 仅使用项目计划中的 long-range hopping、finite-size correction 攻击面；公式为本轮提出的可检验 ansatz。
[假设] shortcut 弱耦合，强噪声下可把 shortcut 访问率估为 |J_l|^2/gamma；F(s) 是与具体 reservoir 密度和 counting parameter 有关的无量纲函数；多个 shortcut 的线性叠加仅用于稀疏、弱耦合、低 cycle 重叠 regime。

## 3. 深挖1：同构的更深数学结构

第一层：共识失败 -> 1-cochain 非 exact

共识协议里“每个节点版本号 phi_i 是否存在”对应数学条件 a=d phi。若存在 a 但不存在全局 phi，就是第一上同调 H^1(G) 的非平凡类。物理翻译是：局域 gauge choice 存在，但全局 gauge patch 不能拼起来。

第二层：纠错 syndrome -> logical error

纠错码里，局域 stabilizer syndrome 可以定位局域误差；但绕过非平凡 cycle 的误差可能不触发局域 syndrome，却改变 logical state。物理翻译是：局域噪声平均可能把局域相干消掉，但绕 cycle 的 Peierls/counting holonomy 是 logical observable。它不一定改变平均电流，却改变高阶 cumulants 或 CGF 的非高斯尾部。

第三层：cohomology class -> CGF sector decomposition

如果上述翻译成立，CGF 不应是单一 SSEP 函数，而应分解为拓扑扇区：

lambda(s) = max_{[a] in H^1(G,U(1))} lambda_{[a]}(s)

或在弱 holonomy 下表现为各扇区的解析修正。这里最危险也最有价值的预测是：某些 s 区间可能出现不同 holonomy sector 的竞争，导致 lambda(s) 的亚领先非解析点。这会比“有限尺寸修正”更像一条新议题。

## 4. 深挖2：原学科结构的下一层推广

第一层推广：拜占庭共识 -> 带坏边的鲁棒共识

在共识理论中，不只是环路会出问题；少数拜占庭边可以在局域一致性检查下持续注入矛盾。物理翻译：不是所有边都同一类噪声。若某些边的噪声强度 gamma_e 或 hopping phase 随时间慢变/准静态，系统可能出现 quenched gauge disorder。预测是样本间 CGF 方差不再按普通自平均下降，而与 cycle disorder 的方差相关：

Var_sample[lambda(s)] ~ K0(s)^2 b1(G) Var(Phi_C) / L^2

这里 K0(s) 是单个弱 cycle 对 CGF 的速率幅度，单位 s^-1；例如弱 shortcut 极限可取 K0(s) ~ (|J_l|^2/gamma) F_var(s)，其中 F_var(s) 无量纲。若 b1(G) ~ L，则 Var_sample[lambda] ~ K0(s)^2/L，而不是更快的树状自平均。

第二层推广：纠错码 -> LDPC 阈值/渗流阈值

LDPC 码有局域稀疏校验，但是否能纠错取决于全局 Tanner graph 的 expansion 和短环分布。物理翻译：Q-SSEP 普适性边界也许不是“有没有长程边”这么粗，而是网络是否越过一个 cycle percolation 阈值。若 shortcut 密度 rho_l 低于阈值，只出现稀疏亚领先 holonomy 修正；若 rho_l 超过阈值，cycle space 广延，SSEP CGF 的单参数 conductance 约化失效。

第三层推广：consensus number -> universality capacity

不同同步原语有不同 consensus number，表示它们能解决多少进程的一致性。物理翻译：不同噪声/边界机制有一个“普适性容量”：最多能消去多少独立 cycle 的 counting holonomy。若噪声只局域退相干，它的容量可能随局域约束增长不足以覆盖 b1(G)。这给出一个定性但可计算的判据：

chi = b1(G) / N_noise_constraints。

当 chi -> 0，SSEP 等价稳；当 chi = O(1)，FCS 出现网络拓扑修正；当 chi > chi_c，可能切换到新 universality class。

--- INSPECTOR_CHECK ---
[公式] Var_sample[lambda(s)] ~ K0(s)^2 b1(G) Var(Phi_C)/L^2，K0(s) ~ (|J_l|^2/gamma)F_var(s)；chi=b1(G)/N_noise_constraints。lambda 方差与 K0(s)^2 单位均为 s^-2；Phi_C、F_var(s)、chi 无量纲。若改用 tilde lambda=lambda/K0，则 Var_sample[tilde lambda] ~ b1(G)Var(Phi_C)/L^2 为无量纲式。
[方向] 普适性边界可能由 cycle-space 密度控制，而非仅由局域 hopping 是否存在控制。
[数据] 无新增实验数据；来自计算机科学共识/纠错码结构向当前 QSSEP 网络边界的映射。
[假设] 不同 cycle 的 holonomy disorder 在弱耦合、稀疏 cycle、交叉项可忽略的近似下可加；N_noise_constraints 可用独立局域退相干/校验约束数量估算。

## 5. 本轮失败记录

失败跳跃：建筑学张拉整体。

借来的结构本来是“局域杆件压缩、整体张力闭合决定稳定形态”。我试图把它翻译成“边界 reservoir 是支座，bulk hopping 是杆件，噪声是预应力”。问题是它能自然给出边界几何量和刚度矩阵，但落到 CGF 时只得到“有效 conductance 由网络刚度决定”，这太接近普通网络扩散/电阻网络，不能清楚地产生非 SSEP 的 FCS 签名。暂时放弃，除非后续需要研究高维边界形状的 harmonic conductance。

## 6. 本轮判断

最值得继续的不是“长程 hopping 一定破坏 SSEP”，而是更窄的命题：

> Q-SSEP/SSEP 等价可能只对 counting field 的 exact sector 成立；含非平凡 cycle holonomy 的网络会在有限尺寸或多路径几何中留下拓扑 CGF 修正。

这比泛泛讲相互作用或长程跳跃更可检验，因为它给出明确旋钮：shortcut 强度 J_l、cycle 长度 ell、holonomy theta、cycle 数 b1(G)。数值上可以先做单 shortcut noisy free fermion，把 lambda(s,theta)-lambda(s,0) 抽出来，看是否有 1-cos theta 和 |J_l|^2/gamma scaling。

## §末 产出格式

本轮的跨学科跳跃：计算机科学 -> 分布式共识/纠错码的 cycle syndrome 与 logical error -> Gauge trick 只消去 exact counting 1-form，非平凡 cycle holonomy 留下 FCS 修正。

这个结构的数学对象：图 G 上的 U(1) 1-cochain a、上同调类 [a] in H^1(G,U(1))、第一 Betti 数 b1(G)=|E|-|V|+c（连通图 c=1 时为 |E|-|V|+1）、cycle holonomy Phi_C=sum_{e in C}a_e mod 2pi。

如果这个同构成立，最奇怪的可检验预测是：一维 noisy free fermion 链只要加一条带 Peierls 相位的弱 shortcut，CGF 就出现 Delta lambda(s,theta) proportional to (|J_l|^2/gamma)[1-cos theta] 的拓扑亚领先修正，且幅度随 cycle 位置和 b1(G) 而非仅随边界 reservoir 改变。

A博士最可能反对的点：A 会说 R1 的 gauge trick 已经允许把 counting field 任意移动，且强噪声热力学极限只保留扩散模式；我的回应是，这个说法默认 counting field 是 exact sector，单环/多环网络的 holonomy sector 不是边界势差，不能由顶点 gauge 全局消去。

本轮失败记录（如有）：建筑学张拉整体 -> 可映射到网络 conductance/刚度，但没有自然给出 CGF 非经典项，暂不作为主攻。

下一步计划：下一轮跳信息论，针对“噪声平均是否真的丢失全部量子 FCS 信息”建立 channel capacity/rate-distortion 版本；若容量为零才有完全 SSEP，若容量亚广延但非零，则解释 finite-size quantum cumulants。

需要PI投喂的文献方向：graph cohomology gauge field transport、full counting statistics Aharonov-Bohm ring dephasing、QSSEP on graphs、long-range hopping noisy fermions、cycle space random walks large deviations、LDPC Tanner graph cycle expansion。
