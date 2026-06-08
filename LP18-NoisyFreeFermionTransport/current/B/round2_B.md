# B博士 Round 2：单 shortcut Aharonov-Bohm 环的 holonomy FCS

## 0. 框架声明

本轮不再走分布式共识/纠错码。我的跨学科跳跃改用信息论中的“信道可辨识性”和图上 Aharonov-Bohm 干涉的 full counting statistics。

借来的结构不是“量子环也会干涉”这种表面类比，而是：

> 如果一个观测量只是在 ordinary conductance 中改参数，那么它应当能被一个标量有效电导 `D_eff` 吸收；如果它携带环路 holonomy，则它改变的是输运生成元对非 exact 1-form 的响应，并在 FCS 中留下不能由 `s -> D_eff s` 或 `lambda_SSEP(D_eff)` 重标定吸收的偶函数相位指纹。

最小模型：一条长度 `L` 的 noisy free fermion 链，左右 reservoir 做电荷 FCS；在 bulk 的 `p,q` 两点之间加一条弱 shortcut，`ell=q-p`，hopping 为 `J_l exp(i theta)`。链边 hopping 为 `J`，强退相干率为 `gamma`。shortcut 与链段 `p -> q` 形成单个环；`theta` 是环路 Peierls holonomy，不能由顶点 gauge 全局消去。

## 1. 从 ansatz 到候选最低阶可检验结构

### 1.1 弱 shortcut 的有效速率

强退相干下，off-diagonal coherence 可被绝热消去。普通链边给出经典跳率量级

`r = 2 |J|^2 / gamma`

弱 shortcut 给出

`r_l = 2 |J_l|^2 / gamma`

其中 `r,r_l` 单位均为 `s^-1`。这一步本身只是普通 conductance renormalization：若 shortcut 没有相位可观测性，它只是在经典图上多一条边。

holonomy FCS 的相位项不能无条件地归因于单次 shortcut 跳跃，因为单次跳跃的相位可被局部重定义吸收。真正的 `theta` 依赖至少需要“走 shortcut”和“沿链段走 `p -> q`”两条振幅路径形成闭合比较。因此下面的 `|J_l|^2/gamma` 只能作为候选最低阶：它假设 tilted quantum generator 在强退相干投影后仍保留一个对 holonomy 敏感的二阶残差。A 博士最可能指出的替代是：二阶 Zeno population generator 只留下实跳率 `|J_l|^2/gamma`，Peierls 相位完全消失；真正 holonomy 项必须来自更高阶闭合路径相干，例如含 shortcut 与链段传播的 `J_l^2 J^m/gamma^{m+1}` 型项，或等价的最短闭合相干路径阶数。

在弱 shortcut、强退相干且仅保留候选环路最小干涉的 regime，我把待检修正写成相对误差形式

`Delta lambda_hol(s,theta) = K(s;rho_L,rho_R,L,p,q,r,gamma) * eta_l * W_ell(L,p,q) * [cos(theta)-1] * [1 + O(eta_l/r) + O(J/gamma)]`

或等价地，把所有加到 `lambda` 的余项写成有量纲形式：

`Delta lambda_hol = eta_l W_ell F_hol(s)[cos(theta)-1] + O(eta_l^2/r) + O(eta_l J/gamma)`

这里每一项单位都是 `s^-1`。

`eta_l = |J_l|^2 / gamma`

单位为 `s^-1`，`K` 是无量纲 FCS 形状函数，`W_ell` 是无量纲的环路访问/重合权重。为了让 `Delta lambda_hol(s,0)=0`，我采用 `[cos(theta)-1]`；若报告幅值也可写成正的 `A(s)[1-cos(theta)]`，只是符号吸收到 `A(s)`。

候选最低阶结构的具体可测版本：

`Delta lambda_hol(s,theta) = eta_l * W_ell * F_hol(s;rho_L,rho_R) * [cos(theta)-1]`

其中

`W_ell = (ell/L)(1-ell/L) * L^-1`

是单 shortcut 在 1D diffusive profile 中被电荷传输轨迹访问的候选权重；它给出 bulk 中间最大、靠近边界变小的相对尺度，不把它伪装成定理。若数值发现最佳权重是 Green function `G(p,q)` 或 resistor-network leverage score，应替换 `W_ell`。若二阶 Zeno 投影中相位确实消失，则 `eta_l` 也必须替换成更高阶闭合路径幅度；但 `theta` 偶性、周期性和 `theta=0` 退化判据不变。

--- INSPECTOR_CHECK ---
[公式] 候选式：`Delta lambda_hol(s,theta)=eta_l W_ell F_hol(s;rho_L,rho_R)[cos(theta)-1][1+O(eta_l/r)+O(J/gamma)]`；等价有量纲余项为 `eta_l W_ell F_hol[cos(theta)-1]+O(eta_l^2/r)+O(eta_l J/gamma)`。`eta_l=|J_l|^2/gamma`、`r=2|J|^2/gamma`，单位均为 `s^-1`；`W_ell,F_hol,theta,s` 无量纲；因此每个加到 `lambda` 的项单位均为 `s^-1`。
[方向] 单 shortcut 的 holonomy 修正必须是相位偶函数；`|J_l|^2/gamma` 只是候选最低阶，需由数值判定。若二阶 Zeno population generator 抹掉 Peierls 相位，真正 holonomy 项应升为更高阶闭合路径项；`theta=0 mod 2pi` 时相对无相位 shortcut 基线消失这一判据保留。
[数据] 使用当前文献库 R1 的强噪声/QSSEP-SSEP 映射边界和 Round 1 的 single-cycle holonomy ansatz；本步未引入外部新数据。
[假设] `J_l` 弱于主链，`gamma` 是最大 bulk 退相干尺度；reservoir Markovian；只有一个独立 cycle；`theta` 是 Peierls holonomy 而不是可局部 gauge 掉的边相位。

### 1.2 奇偶性、阶数和单位

`Delta lambda_hol(s,theta)` 的相位结构：

1. `theta` 偶性：`Delta lambda_hol(s,theta)=Delta lambda_hol(s,-theta)`。理由是两端 reservoir 不显式破坏时间反演时，单环 AB 相位进入闭合路径对比为 `exp(i theta)+exp(-i theta)`。
2. 周期性：`Delta lambda_hol(s,theta+2pi)=Delta lambda_hol(s,theta)`。
3. 零点：以同一 shortcut 的 `theta=0` 为基线，`Delta lambda_hol(s,0)=0`。
4. 小相位：候选二阶式为 `Delta lambda_hol(s,theta) = -0.5 eta_l W_ell F_hol(s) theta^2 + O(eta_l theta^4) + O(eta_l^2/r)`，每个加到 `lambda` 的项单位均为 `s^-1`。
5. 弱耦合阶数：相对“没有 shortcut”的总 CGF，ordinary shortcut conductance 从 `O(|J_l|^2/gamma)` 开始；holonomy 是否同阶是待检假设。若二阶 Zeno population generator 只保留实跳率，则相对“同强度但 `theta=0` 的 shortcut”基线，真正相位残差应升为更高阶闭合路径项。
6. 单位：`lambda` 是长时间极限 `lambda(s)=lim_{t->infty} t^-1 log <exp(s Q_t)>`，单位 `s^-1`；`s` 作为 counting field 无量纲；`J,J_l,gamma` 若按角频率写均为 `s^-1`，所以 `|J_l|^2/gamma` 是 `s^-1`。

`s` 的结构不能只说“乘一个函数”。为了区别均值、噪声和高阶 cumulant，我建议把 `F_hol` 展开：

`F_hol(s;rho_L,rho_R)=a_1 s + a_2 s^2/2 + a_3 s^3/6 + ...`

若左右 reservoir 密度相等，`a_1=0`，但 `a_2` 可非零；若有偏置，`a_1` 可非零。真正值得抓的是比值

`R_n(theta)=Delta C_n(theta)/Delta C_1(theta)`

其中 `C_n=partial_s^n lambda|_{s=0}`。ordinary conductance renormalization 对所有 cumulant 的改变量应近似服从 SSEP 单参数导数关系；holonomy correction 不必服从同一组 `R_n`。

## 2. 数值扫描方案

固定主链和 reservoir 后，扫描这些参数：

1. `theta in [0,2pi]`：检验 `cos theta` 主谐波和偶性。最小判据是拟合 `A0 + A1 cos theta + A2 cos 2theta`，弱 shortcut 的候选最低阶图像预期 `|A2/A1| << 1`。
2. `|J_l|`：判定 `A1` 的幂律。候选最低阶预期 `A1 proportional |J_l|^2`；若出现主导 `|J_l|^4` 或更高幂，说明相位在二阶 Zeno population generator 中消失，holonomy 需要更高阶闭合路径过程。
3. `gamma`：判定 `A1` 的强退相干幂律。候选最低阶预期 `A1 proportional gamma^-1`；若强退相干下转为 `gamma^-2` 或更强压制，说明 shortcut 相位只通过被压制的 coherence 泄漏。
4. `ell/L` 和 `p/L`：检验 holonomy 幅度是否有 bulk 几何形状，而不是只等价于端点 conductance。
5. `s` 或 cumulant order：至少取 `C_1,C_2,C_3`，不要只看平均电流。
6. reservoir 密度 `rho_L,rho_R`：平衡态下看噪声修正，非平衡下看平均流和高阶 cumulants。

推荐数值对象：

`H = sum_i J c_i^\dagger c_{i+1} + J_l e^{i theta} c_p^\dagger c_q + h.c.`

加 bulk dephasing Lindblad `L_i=sqrt(gamma) n_i`，左右注入/抽取 reservoir 设置 `rho_L,rho_R`，在左或右边界加 counting field `s`。对有限 `L=8..64` 可先做 quadratic Lindblad tilted generator；若矩阵过大，先做强退相干投影后的二阶有效 tilted Markov generator，再把 AB correction 当作 coherent perturbation 检验。

## 3. 区分 ordinary conductance renormalization 与 genuine holonomy correction

### 3.1 一参数吸收检验

ordinary conductance renormalization 的假设是：

`lambda(s,theta) = lambda_SSEP(s;D_eff(theta)) + higher finite-size noise`

其中 `D_eff(theta)` 可由平均电流或 `lambda'(0,theta)` 拟合。检验方式：

1. 对每个 `theta` 用 `C_1(theta)` 拟合 `D_eff(theta)`。
2. 用同一个 `D_eff(theta)` 预测 `C_2(theta),C_3(theta)`。
3. 若残差

`E_hol(theta)=C_3(theta)-C_3^SSEP[D_eff(theta)]`

含有稳定的 `cos theta-1` 分量，则不是普通电导重整化。其幅度若随 `|J_l|^2/gamma` 缩放，支持候选最低阶；若随更高阶闭合路径幅度缩放，也仍支持 genuine holonomy correction，只是推翻二阶阶数。

更强的 FCS 判据：

`Q(s,theta)=Delta lambda(s,theta) - (partial_D lambda_SSEP)(s;D_0) Delta D(theta)`

其中 `Delta D(theta)` 由 `partial_s lambda|_{s=0}` 固定。若 `Q(s,theta)` 在多个 `s` 上非零，且为偶周期函数，则是 genuine holonomy correction。

### 3.2 反相位对照

普通 conductance renormalization 只关心等效图连通性。把 `theta=0` 与 `theta=pi` 对比：

`Delta_pi(s)=lambda(s,pi)-lambda(s,0)`

若只是电导重整化，`Delta_pi(s)` 可被 `D_eff(pi)-D_eff(0)` 吸收。若是 holonomy，预期

候选二阶预期为

`Delta_pi(s) = -2 eta_l W_ell F_hol(s) + O(eta_l^2/r) + O(eta_l J/gamma)`

并且在扣除均值拟合的 `D_eff` 后，高阶 cumulant 仍留有同号残差。

### 3.3 位置交换检验

保持 shortcut 长度 `ell` 不变，把 `(p,q)` 沿链平移。普通电导重整化主要由等效电阻变化控制；在长链 bulk 中应较平滑。holonomy correction 则应跟 reservoir 到环的访问 Green function 相关：

`A_hol(p,q) proportional G_L(p,q) G_R(p,q)` 或其简化版 `W_ell`。

因此判据是：同样的 `D_eff` 变化下，如果 `Q(s,theta)` 随环位置有额外 profile，就是 holonomy 而不是电导。

--- INSPECTOR_CHECK ---
[公式] `Q(s,theta)=Delta lambda(s,theta)-(partial_D lambda_SSEP)(s;D_0)Delta D(theta)`；`Delta D` 取扩散常数单位，`partial_D lambda_SSEP * Delta D` 单位为 `s^-1`；`Q` 单位为 `s^-1`。候选二阶式：`Delta_pi(s)=-2 eta_l W_ell F_hol(s)+O(eta_l^2/r)+O(eta_l J/gamma)`，所有项单位为 `s^-1`。
[方向] 若扣除由平均电流确定的 `D_eff(theta)` 后，高阶 cumulant 或完整 `s` 依赖仍含偶周期 `cos theta-1` 分量，则 ordinary conductance renormalization 被排除。
[数据] 数值数据应来自同一有限链在 `theta=0,pi` 和多点 `theta` 扫描下的 tilted generator 主特征值；当前为判据设计，无实测数据。
[假设] SSEP 基线的 `lambda_SSEP(s;D)` 已知或可由 `theta=0` 数值拟合；finite-size correction 在不同 `theta` 间足够平滑，不会伪造精确 AB 周期。

## 4. 深挖1：同构的更深数学结构

第一层：holonomy correction 不是边权修正，而是非 exact 1-form 的响应。

链加 shortcut 的图有 `b1=1`。普通 conductance 只看图 Laplacian 的实边权；holonomy 看的是 U(1) connection 在唯一 cycle 上的 Wilson loop：

`U_C = exp(i theta)`

如果 `U_C=1`，connection 可退化为 exact sector；如果 `U_C != 1`，它是同一个局部边权图上的不同平坦联络。这个区别不会出现在纯经典电阻网络里，却会出现在 FCS 的 tilted quantum generator 里。

第二层：信息论的“可辨识信道”对应 FCS 的 cumulant 向量。

把 `theta` 看成输入，把长时间电荷计数分布 `P_theta(Q_t)` 看成输出。若所有 `theta` 的影响都能被 `D_eff(theta)` 吸收，则信道只有一维充分统计量 `D_eff`。若扣除 `D_eff` 后仍有

`D_KL(P_theta || P_0)/t > 0`

则 holonomy 是可辨识输入。候选二阶预期：

`I_hol(theta) ~ eta_l W_ell [1-cos theta]^2`

这里 `I_hol` 是单位时间的统计可辨识率，单位 `s^-1`。若二阶相位被 Zeno population generator 抹掉，则把 `eta_l` 替换成实际测得的更高阶闭合路径速率；可辨识率判据本身不依赖候选阶数。这给了比看单个 cumulant 更强的判据：不同 `theta` 的完整电荷分布是否在同一平均电流下仍可区分。

第三层：Fisher information 的零点阶数。

若 `lambda` 的相位依赖从 `[cos theta-1]` 开始，则在 `theta=0`：

`partial_theta lambda|_0=0`

但

候选二阶给出

`partial_theta^2 lambda|_0 = - eta_l W_ell F_hol(s)`

若真实项是更高阶闭合路径速率 `k_loop`，则右边应替换为 `- k_loop W_loop F_loop(s)`。因此 `theta=0` 是一阶不可辨识、二阶可辨识点；数值上不要用很小 `theta` 的线性响应找信号，应拟合二阶曲率，同时扫描该曲率对 `J_l,J,gamma` 的幂律。

## 5. 深挖2：原学科结构的下一层推广

第一层推广：从信道容量到 rate-distortion。

如果实验只能测到有限 cumulants，例如只测 `C_1,C_2,C_3`，那么 holonomy 的可见性不是“有/无”，而是一个失真问题。定义只用前三阶 cumulant 的距离

`d_3(theta,0)=sum_{n=1}^3 w_n [C_n(theta)-C_n(0)]^2`

如果扣除 `D_eff` 后的 `d_3^res` 仍随 `[1-cos theta]^2` 缩放，则有限观测也足以识别 holonomy。若完整 FCS 可辨识但前三阶不可辨识，则需要高阶 cumulants 或 rare-event tail。

第二层推广：从单输入信道到多环 MIMO 信道。

多个 shortcut 给多个 holonomy `theta_alpha`。信息论上这是多输入信道，FCS 输出是电荷计数分布。弱耦合下应有

`Delta lambda = sum_alpha eta_alpha W_alpha F_alpha(s)[cos theta_alpha-1] + sum_{alpha<beta} (eta_alpha eta_beta/r_ref) M_alpha_beta(s) cos(theta_alpha +/- theta_beta) + ...`

其中 `r_ref` 是主链或局部图上的参考跳率，单位 `s^-1`，所以交叉项 `(eta_alpha eta_beta/r_ref)M_alpha_beta` 仍为 `s^-1`。单环 Round 2 的价值在于先测出对角响应的真实阶数：它可能是 `eta_alpha W_alpha F_alpha`，也可能是更高阶闭合路径速率。只有当单环通过后，多环的互信息矩阵或 Fisher matrix 才值得做。

第三层推广：从容量为零到容量亚广延。

R1 的 SSEP 普适性等价于“相干 holonomy 到电荷 FCS 的信道容量在热力学极限为零”。单 shortcut 的命题更尖锐：

`C_hol(L) ~ eta_l W_ell ~ eta_l/L`

所以它可能不是 leading universality breaker，而是亚广延的可测修正。若 shortcut 密度随 `L` 增长到 `O(L)`，总容量可变成 `O(1)`，这时才可能升级为新的 leading universality class。

## 6. 失败记录

失败跳跃：纯 Shannon channel capacity 上界。

我试图直接说“噪声强则信道容量为零，所以 SSEP；容量非零，所以 holonomy FCS”。失败原因是容量需要先指定输入分布和输出观测族，太抽象，无法直接给出 `Delta lambda(s,theta)` 的阶数。可保留的是 Fisher/KL 可辨识率，它能落到 FCS 主特征值和 cumulants 上。

另一个暂缓方向：图上 AB 环的持久电流。

闭合量子环的 persistent current 对 `theta` 是标准物理，但当前系统是开放 reservoir 驱动的 noisy transport，直接搬 persistent current 会偏题。这里我只借 Wilson loop/AB 偶周期结构，不把平衡持久电流当作目标观测量。

## 7. 本轮判断

单 shortcut ring 的 holonomy FCS 最小可检验命题是：

> 在强退相干 noisy free fermion 链中，带 Peierls 相位的弱 shortcut 对电荷 FCS 的相位依赖必须表现为 `theta` 的偶周期函数，并在 `theta=0 mod 2pi` 退化到无 holonomy 基线。候选二阶形式为 `Delta lambda_hol(s,theta)=eta_l W_ell F_hol(s)[cos(theta)-1]`，其中 `eta_l=|J_l|^2/gamma`，`lambda` 单位为 `s^-1`；但该阶数需数值判定，真正项也可能是更高阶闭合路径速率。关键不是先验阶数，而是扣除由平均电流拟合的 ordinary conductance renormalization 后，残差是否仍存在于高阶 cumulants 或完整 `s` 依赖中。

这个命题比 Round 1 的 ansatz 更可检查：只需做 `theta`、`J_l`、`gamma`、`ell/L` 和 `s` 的有限链扫描。若 `Q(s,theta)` 为零，则 B 路线退化为普通电导修正；若非零，R1 的 SSEP 等价边界就多了一个“非 exact holonomy sector”的亚领先例外。

## 末格式

本轮的跨学科跳跃：信息论/AB 图环路 -> 可辨识信道与 Wilson loop -> 单 shortcut noisy free fermion 的 holonomy FCS 不能被单参数 conductance renormalization 完全吸收。

这个结构的数学对象：图 `G` 上的 U(1) flat connection、单环 Wilson loop `U_C=exp(i theta)`、tilted generator 主特征值 `lambda(s,theta)`、扣除电导重整化后的残差 `Q(s,theta)`、KL/Fisher 可辨识率。

如果这个同构成立，最奇怪的可检验预测是：同一条 shortcut 在 `theta=0` 与 `theta=pi` 之间，即使平均电流差异被 `D_eff` 吸收，高阶 cumulants 仍留下 `cos theta-1` 残差。该残差若按 `|J_l|^2/gamma` 缩放，支持候选二阶图像；若按更高阶闭合路径速率缩放，则支持 holonomy 但否定二阶阶数。

A博士最可能反对的点：A 会说强退相干投影后只剩经典跳率，Peierls 相位在 `|J_l|^2/gamma` 中消失，所以我写的候选二阶 holonomy 可能过早；真正相位依赖也许要到 `k_loop ~ J_l^2 J^m/gamma^{m+1}` 或其他更高阶闭环相干速率才出现，其中 `k_loop` 单位仍为 `s^-1`。我的回应是：这正是本轮数值扫描要判定的核心；若 `|J_l|^2/gamma` 不成立，应把阶数修正为最短闭合相干路径阶数，但偶性、周期性和 conductance-residual 判据仍保留。

本轮失败记录（如有）：纯 Shannon capacity 过抽象，不能直接给 `Delta lambda` 阶数；平衡 AB persistent current 也不适合作为开放 noisy FCS 的直接类比。

下一步计划：让 PI 或 INSPECTOR 优先检查强退相干投影中相位是否真的能在候选二阶速率 `|J_l|^2/gamma` 留下，还是必须提升到包含链段相干传播的更高阶闭合路径；同时建议数值组先做 `theta=0,pi`、`J_l` 幂律和 `gamma` 幂律扫描。

需要PI投喂的文献方向：full counting statistics Aharonov-Bohm interferometer dephasing；counting statistics quantum ring Lindblad reservoirs；tilted Lindbladian free fermion transport Peierls phase；SSEP on graph with chord conductance cumulants；Fisher information full counting statistics transport。
