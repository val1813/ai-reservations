# LP23-R2 正式 Round1（B路）

当前北极星：Bridge quotient invariant 生死检验

核心量：

`R_{\beta\beta'}[\gamma] = C_\beta F_\beta(H[\gamma]) - C_{\beta'} F_{\beta'}(H[\gamma])`

问题：是否存在标准 gauge / endpoint calibration / spinoptics / constitutive equivalence 吸收不了的非零 residual？

## §0 框架声明

本轮不用 ABI / 编译器框架。B路选取的外来结构是：

**量子纠错码的 syndrome 网络 + 多路径一致性 holonomy。**

借来的不是“编码”这个比喻，而是一个数学结构：

局部读出边上的变量不直接是物理态；真正可观测的是闭合校验回路上的 syndrome。若所有局部重标定都是 gauge，则每个闭合回路 syndrome 应该为零；若存在非零 syndrome，它不是某条边的属性，而是网络粘合失败的全局 obstruction。

物理翻译：

- `beta` 是 bridge/readout functor：把底层 holonomy `H[\gamma]` 映射到某个实验读出空间。
- `C_beta` 是端点校准和公共 observable 投影。
- 标准 gauge / endpoint calibration 只能改节点势或边的局部基。
- 真 residual 不应定义在单路径上，而应定义在多路径网络的闭合一致性条件上。

所以本轮把 `R_{\beta\beta'}[\gamma]` 从“两个读出差值”提升为：

`S_{\beta\beta'}(\Gamma) = sum_{e in cycle Gamma} s_e R_{\beta\beta'}[e]`

其中 `Gamma` 是多路径干涉网络中的闭合回路；当回路方向与边方向一致时 `s_e=+1`，反向时 `s_e=-1`。若 `R` 只是端点校准差，则它是一个 coboundary，闭合和必为零；若 `S != 0`，它是可落地的 syndrome observable。

## 跨学科结构 -> 物理翻译 -> 最怪可检验预测

跨学科结构：纠错码 parity-check matrix `B`。边 residual 向量 `r` 不直接判死活，真正的 syndrome 是：

`sigma = B r`

若 `r = D a`，即来自节点校准势 `a` 的边差，则 `B D a = 0`。所以所有 endpoint calibration 都自动落在 syndrome 的零空间。

物理翻译：

- 节点 `v_i`：源、像、透镜面、探测端口或中间 caustic chart。
- 有向边 `e: i -> j`：一条几何光学路径、一个 beam branch、或一个 readout bridge。
- 边变量 `h_e`：路径 holonomy 的相位/偏振读出。
- 桥 `beta`：screen/splitting/constitutive/readout 规则。
- 公共 observable 空间 `O`：探测器上同一 Stokes/phase/intensity-interference 向量空间。
- `r_e = C_beta F_beta(h_e) - C_beta' F_beta'(h_e) in O`。
- 标准 gauge：`r_e -> r_e + a_j - a_i`。
- 真 obstruction：`sigma_c = sum_{e in c} s_e r_e`。

最怪可检验预测：

**单条光路上看不见的新物理，只有把三条或更多路径组成闭合干涉网络时才出现；并且该异常对每个端口的重新定标不敏感，却会随网络回路面积、caustic 穿越奇偶性、或介质记忆核的非对易排序而翻转符号。**

这意味着：两个实验若只比较一对像的相位差，可能完全被 endpoint calibration 吸收；但同一系统若有三像闭合回路 `A -> B -> C -> A`，则存在一个三边 syndrome：

`sigma_ABC = r_AB + r_BC + r_CA`

它不能被任何三个端点校准常数同时消掉。

## Toy model：网络 syndrome residual

### 变量

取三节点网络 `V = {0,1,2}`，三条有向边：

- `e01: 0 -> 1`
- `e12: 1 -> 2`
- `e20: 2 -> 0`

每条边对应一条可干涉路径段或一条路径差读出。公共 observable 空间先取 `O = R`，表示标量相位 residual；下一轮可扩展到 `O = R^3` 的 Stokes 向量。

底层 holonomy：

`H_e = exp(i phi_e) U_e`

其中 `phi_e` 是相位，`U_e in SU(2)` 是偏振 Jones transport。

两个 bridge readout：

`F_beta(H_e) = phi_e + eta q_e`

`F_beta'(H_e) = phi_e + eta q'_e`

`q_e, q'_e` 表示两个 bridge 对 caustic chart、screen complement、或记忆核排序的读出修正。共同投影先取 `C_beta = C_beta' = 1`。

边 residual：

`r_e = R_{\beta\beta'}[e] = eta (q_e - q'_e)`

加入端点校准：

`r_e -> r_e + a_{target(e)} - a_{source(e)}`

闭合 syndrome：

`sigma_012 = r_01 + r_12 + r_20`

端点项严格抵消：

`(a_1-a_0) + (a_2-a_1) + (a_0-a_2) = 0`

因此 `sigma_012` 是公共 observable 空间里的 gauge-invariant residual。

### 非局域记忆核版本

给每条边一个沿路径参数 `s in [0,1]` 的局部桥密度 `k_beta,e(s)`。若 bridge 是局域的：

`q_e = integral_0^1 k_beta,e(s) ds`

若 bridge 带记忆：

`q_e = integral_0^1 ds integral_0^s ds' K_beta,e(s,s') X_e(s) X_e(s')`

其中 `X_e(s)` 可取曲率、介质各向异性、或偏振基旋转率。若 `K_beta` 与路径拼接顺序相关，三边闭合和可非零；这不是局域 `chi^{abcd}(x)` 的单点响应能完全吸收的对象，而是网络级历史核。

### 可计算步骤

下一轮本地脚本只需要做最小数值检验：

1. 输入节点数 `n=3`，边表 `[(0,1),(1,2),(2,0)]`。
2. 输入两个 bridge 在每条边上的读出数组 `q_beta[e]` 和 `q_betap[e]`。
3. 计算边 residual `r[e] = eta * (q_beta[e] - q_betap[e])`。
4. 构造 incidence matrix `D` 与 cycle matrix `B`。
5. 检查 `r` 是否可写成 `D a`。等价地，最小化 `||D a - r||`。
6. 输出 `sigma = B r` 与 `projection_residual = ||(I - D D^+) r||`。其中 `B` 若不是左零空间正交归一基，`||B r||` 与正交投影残差不要求数值相等；主判据以后者为准，`B r` 是 syndrome 基坐标。
7. 若 `sigma != 0` 且对随机端点校准 `a_i` 不变，则 R2 toy residual 存活。

最小公式：

`I_bridge = ||B r||^2`

若 `I_bridge > tolerance`，它就是 bridge quotient invariant 的候选。

--- INSPECTOR_CHECK ---
[公式] `S_{\beta\beta'}(\Gamma)=sum_{e in Gamma} s_e R_{\beta\beta'}[e]`；标量相位版本单位为 rad，Stokes 版本为无量纲归一化 Stokes 分量。  
[方向] 单边 residual 可被端点校准污染；闭合网络 syndrome 可剔除 endpoint calibration，并测试是否存在 bridge 粘合 obstruction。  
[数据] 本步未使用外部数据；只构造三节点 toy model。  
[假设] 公共 observable 空间 `O` 已由 `C_beta, C_beta'` 对齐；边 residual 可线性叠加；端点校准以节点 coboundary 形式作用。

## 深挖1：同构的更深层数学结构

第一层：从“闭合回路和”下探到链复形。

边 residual `r` 是一个 1-cochain。端点校准 `a` 是 0-cochain。标准 endpoint gauge 作用是：

`r -> r + d a`

闭合 syndrome 是对 cycle 的配对：

`<z, r>`

若 `r = d a`，则对任何闭合 cycle `z` 有 `<z, d a> = <partial z, a> = 0`。所以可观测 residual 实际落在：

`H^1(network, O) = ker d_1 / im d_0`

这比“多路径差值”更硬：R2 存活条件不是 `R != 0`，而是 `[R] in H^1` 非零。

第二层：从 Abelian syndrome 下探到非交换 holonomy 的群上 2-cocycle。

偏振 transport 不一定可标量化。令每条边有群元素：

`G_beta(e) in U(1) x SU(2)`

两个 bridge 的差不应只写成 `G_beta - G_beta'`，而应写成公共空间里的相对元素：

`Delta_e = C_beta(G_beta(e)) C_beta'(G_beta'(e))^{-1}`

闭合 obstruction 是有序乘积：

`Omega_Gamma = product_{e in Gamma}^{path-order} Delta_e`

若 `Omega_Gamma` 在所有端点共轭变换下只变为共轭类，则 `Tr(Omega_Gamma)` 是 observable。标量 toy model 是其 Abelian 化：

`sigma_Gamma = log Omega_Gamma`

但该 `log` 只在近恒等、固定 log 分支或 Abelian 极限下作为标量 syndrome 使用；一般非交换情形保留 `Omega_Gamma`、`Tr(Omega_Gamma)` 或 eigenphase 作为主对象。

这一层给出一个更强预测：即使每条边的标量相位 residual 可调零，非交换偏振闭合乘积仍可能留下 `Tr(Omega_Gamma) != dim`。

## 深挖2：原学科结构的下一层推广

第一层：从普通纠错 syndrome 推广到 subsystem code。

在 subsystem code 中，不是所有 gauge 自由度都需要修正；部分局部自由度属于 gauge subsystem，只有 logical operator 可观测。物理翻译是：

- screen rotation、endpoint tetrad、局域 constitutive reparametrization 是 gauge subsystem；
- 多路径闭合 syndrome 是 logical observable；
- R2 要找的不是边上的“错误”，而是 logical residual。

这避免了一个陷阱：如果某条边 `r_e != 0`，它可能仍是 gauge；只有投影到 logical subspace 的分量才有物理生命。

第二层：从静态 syndrome 推广到带记忆的 convolutional code。

卷积码的校验不仅看当前 bit，还看过去窗口。物理翻译是非局域介质或 caustic chart history：

`sigma_t = sum_{ell=0}^L B_ell r_{t-ell}`

若介质/路径历史核有有限记忆深度 `L`，则单一时刻的 constitutive equivalence 不足以吸收 residual；可观测的是时序 syndrome 的谱：

`I_memory(omega) = ||B(e^{-i omega}) r(omega)||^2`

最怪版本：R2 residual 可能不在平均相位里，而在多路径干涉信号的频域 syndrome 峰中；峰位由记忆核延迟决定，不由单条光线的 Berry/Rytov 相位决定。

## A博士最可能反对的点

A 路可能会说：只要 `q_e - q'_e` 来自某个有效局域 constitutive tensor 或 spinoptics 修正，`sigma` 仍是标准物理，不是 R2 新自由度。

B 路回应：同意单边 residual 不算新自由度。因此生死线改成：

`r notin im(D) + im(spinoptics) + im(local constitutive equivalence)`

脚本上不是问 `r` 是否非零，而是问把这些标准子空间投影掉后：

`I_bridge = ||P_perp r||^2`

是否仍非零。网络 syndrome 只是第一道最小过滤器；下一轮应把 spinoptics 与局域 constitutive 模板也加入设计矩阵。

## 本轮失败记录

失败跳跃：把 residual 类比成“单条路径上的错误位”。

失败原因：单边错误可被端点校准、screen gauge、或桥定义重写吸收；这会重复标准路线，不能给 R2 生死检验。必须升到闭合网络 syndrome，才有可能避开 endpoint calibration。

## R2 是否存活

B路判断：**弱存活，但生死线变窄。**

存活的不是“任意 bridge residual”，而是：

`[R_{\beta\beta'}] != 0 in H^1(network, O) / standard_model_subspace`

也就是在多路径闭合网络中，经过 endpoint calibration、screen gauge、spinoptics 模板、局域/等效 constitutive 模板投影后仍非零的 logical syndrome。

若下一轮脚本在三节点或四节点 toy network 上找到 `I_bridge > 0`，R2 值得继续。若所有可构造的 `r` 都落入标准子空间，则 R2 应降级为“标准商空间分类 no-go”，不再声称新 observable。

## 下一轮计算脚本需要的输入

最小输入：

- `nodes`: 节点列表，例如 `[0,1,2]`
- `edges`: 有向边列表，例如 `[(0,1),(1,2),(2,0)]`
- `cycles`: 闭合回路矩阵或由脚本自动求 cycle basis
- `q_beta`: 每条边的 bridge-beta 读出数组
- `q_betap`: 每条边的 bridge-beta-prime 读出数组
- `C_beta, C_betap`: 公共 observable 投影矩阵；标量模型可设为 `1`
- `standard_templates`: 端点校准、spinoptics、局域 constitutive 等可吸收模板组成的设计矩阵
- `tolerance`: 判定非零 syndrome 的数值阈值

输出：

- `r`
- `B r`
- `||P_perp r||`
- 随机 endpoint calibration 下的 invariance check
- 若使用非交换版本，则输出 `Tr(Omega_Gamma)` 或其 eigenphase

本轮的跨学科跳跃：

纠错码 syndrome / subsystem logical operator / convolutional memory code -> 多路径 bridge residual 的闭合 holonomy obstruction -> 只有网络级 syndrome 非零才算 R2 活口。

建议保存路径：`current/B/R2_round1.md`
