# B博士 NSF-FCS-1 Round 1：把 reservoir-current variance 看成出口更新过程的电网络噪声

## 0. 框架声明

本轮不走 tilted-generator 标准路线，也不把 `lambda_R''(0)` 直接当作 conductance 的自动副本。我的跨学科入口是：

> 电网络的有效电导只决定平均通量；出口电流噪声还要看“到达右 reservoir 的更新过程”是否近似 Poisson。若出口到达过程有长记忆、批量跳跃或返回相关，平均 current 与 variance 可以拥有不同的有限尺寸标度。

本轮 observable 固定为右 reservoir-current

`Q_R(t)=N_R^{out}(t)-N_R^{in}(t)`

即右 reservoir 边界发生的抽出/注入净计数，不是链内部任意 cut-current。内部 cut-current 在 long-jump 系统中尤其危险，因为一个长跳可以跨越许多 cuts；而 `Q_R(t)` 只数右 reservoir 与系统交换的事件。

## 1. 替代数学结构：Poisson 方程的出口电网络分解

把强退相干后的 population dynamics 看成有限状态连续时间 Markov 链。设未 tilt 的生成元为 `L`，稳态为 `pi`。右 reservoir-current 的瞬时增量为边界跳变函数 `g_R(x,y)`：

- 右 reservoir 抽出粒子：`g_R=+1`
- 右 reservoir 注入粒子：`g_R=-1`
- 其他 bulk 或左边界事件：`g_R=0`

平均右 reservoir-current 是

`j_R = sum_x pi(x) sum_y k(x,y) g_R(x,y)`。

二阶增长率，即本题的目标量，是 additive functional 的 Dirichlet/Poisson 形式：

`lambda_R''(0)= a_R + 2 <b_R-j_R, phi_R>_pi`

其中

`a_R = sum_x pi(x) sum_y k(x,y) g_R(x,y)^2`

是右 reservoir 边界事件的本地 activity，`phi_R` 解

`-L phi_R = b_R - j_R`

而

`b_R(x)=sum_y k(x,y) g_R(x,y)`。

这里所有内积都只在状态函数之间做：

`<f,h>_pi=sum_x pi(x) f(x) h(x)`。

`g_R(x,y)` 只用于定义状态函数 `b_R(x)` 和 activity `a_R`，不直接进入 `pi` 内积。

这给出一个不同于 conductance 的判断结构：

- conductance 标度来自平均通量 `j_R` 对 reservoir 密度差的响应；
- `lambda_R''(0)` 来自“本地 activity `a_R` + Poisson 方程解 `phi_R` 的长程相关修正”；
- 只有当 `a_R` 与相关修正都被同一个有效电阻/电导控制时，variance 才继承 conductance 标度。

电网络翻译是：平均 current 是单位电压下的有效电导；variance 是出口节点的 shot-noise 加上网络中随机游走返回右边界的 Green 函数修正。有效电导 `G_R(L)` 与右边界 Green 函数 `G_{RR}^{kill}(L)` 一般不是同一个量。

--- INSPECTOR_CHECK ---
[公式] `Q_R(t)=N_R^{out}(t)-N_R^{in}(t)`，无量纲计数；`lambda_R''(0)=lim_{t->infty} t^-1 Var Q_R(t)`，单位 `time^-1`；`j_R=lim_{t->infty}t^-1 E Q_R(t)`，单位 `time^-1`；`a_R=sum_x pi(x) sum_y k(x,y)g_R(x,y)^2`，单位 `time^-1`；Poisson 方程 `-L phi_R=b_R-j_R`，若 `L` 单位为 `time^-1`，则 `phi_R` 无量纲。
[方向] `lambda_R''(0)` 不由 conductance 单独决定，而由右 reservoir activity 与 Poisson/Green 相关项共同决定。
[数据] 当前无数值数据；建议数据来自同一 finite-L long-jump exclusion Markov generator 的稳态、右边界 activity、Poisson 方程解。
[假设] 强退相干后可用 classical long-jump exclusion；稳态唯一；`Q_R(t)` 只计右 reservoir 交换事件，不计内部 cut；`<.,.>_pi` 只作用于状态函数，边跳变量 `g_R(x,y)` 先汇总成 `b_R(x)=sum_y k(x,y)g_R(x,y)`。

## 2. 判断 `lambda_R''(0)` 是否继承 conductance 标度的替代判据

定义三个可计算量：

`G_R(L)=partial_{Delta rho} j_R |_{Delta rho=0}`

`A_R(L)=a_R |_{Delta rho=0}`

`K_R(L)=2 <b_R-j_R, phi_R>_pi |_{Delta rho=0}`。

则

`lambda_R''(0)=A_R(L)+K_R(L)`

在平衡或近线性响应下应作为第一判据，而不是先假设它等于 `G_R(L)` 的标度。

### 判据 C：activity-Green 同标度测试

若存在常数窗使得

`A_R(L) ~ G_R(L)` 且 `K_R(L) ~ G_R(L)`

并且二者没有 leading-order 抵消，则 `lambda_R''(0)` 继承 conductance 标度。

若出现以下任一情况，则 mean 与 variance 标度可能分离：

1. `A_R(L)` 为 `O(1)` 或边界局域标度，而 `G_R(L)` 是 `L^{-(2alpha-2)}`、`(log L)/L` 或 `L^-1`；
2. `K_R(L)` 由右边界返回 Green 函数控制，指数不同于有效电导；
3. `A_R(L)+K_R(L)` 存在 leading cancellation，留下次阶项；
4. reservoir 实现把右边界事件做成高频注入/抽出对，activity 很大但净 current 很小。

这套判据的价值是把问题拆成两个可直接算的对象：平均 conductance 与出口更新噪声。它允许 `G_R(L)` 正确继承 fractional Fick law，同时 `lambda_R''(0)` 因出口 renewal 结构而改变标度。

## 3. 可计算反例设计：同一平均 current，不同 variance 标度

我建议做一个“reservoir 速率重参数化”的诊断性构造。保持 bulk long-jump kernel 不变，只改变右 reservoir 的实现方式。它不是先验物理反例；必须先独立固定平均 conductance 的同标度，再盲算 variance 比值，不能用目标结论回调参数。

### 3.1 模型族

右边界耦合设为两步机制：

`system boundary site <-> buffer <-> reservoir`

buffer 是一个有限容量中间态，系统与 buffer 的交换速率为 `u_L`，buffer 与 reservoir 的交换速率为 `v_L`。调参步骤只允许使用平均 current/linear-response 数据，使线性响应平均 conductance `G_R(L)` 与原始直接 reservoir 模型同标度；在这一步不得查看 `lambda_R''(0)` 或 `S_R(L)`。

关键是选择两组 `u_L,v_L`：

- 快 buffer 组：`v_L >> u_L`。出口事件近似 Poisson，右 reservoir 看到的更新过程几乎无等待时间记忆。
- 慢 buffer 组：`v_L ~ G_R(L)` 或 `v_L << u_L`。出口事件变成 renewal bottleneck，等待时间方差由 buffer 清空时间控制。

两组都先通过独立平均-current 校准固定 `G_R(L)` 的同标度。校准冻结后，再盲算 `lambda_R''(0)` 与 `S_R(L)`。只有盲算结果显示 `S_R(L)` 不同，才把它记为诊断性分离证据。

### 3.2 预期分离

如果右 reservoir 事件可以粗略近似为稀疏 renewal 过程，

`Q_R(t) approx sum_{n=1}^{N(t)} X_n`

其中 `N(t)` 是更新次数，`X_n` 是单次净转移。则

`j_R ~ E[X]/E[tau]`

`lambda_R''(0) ~ Var(X)/E[tau] + (E[X])^2 Var(tau)/E[tau]^3`。

这个 renewal 公式只作为启发，适用条件是：相邻更新近似独立或只有短程相关；等待时间 `tau` 有有限二阶矩；单次净转移 `X_n` 与等待时间的相关可忽略或可用有限协方差修正；不存在随 `t` 不收敛的 aging。若这些条件失败，应回到上一节的 Markov Poisson 方程，而不是把 renewal 公式当证明。

在这些条件近似成立时，平均 current 只看 `E[tau]` 的一阶；variance 还看 `Var(tau)`。若 long-jump conductance 决定的是 `E[tau] ~ G_R(L)^-1`，但 buffer 或返回过程让

`Var(tau) ~ L^eta E[tau]^2`

则第二项给出额外 `L^eta`，variance 标度与 mean 分离。

### 3.3 最小数值判据

对每个 `alpha` 和 `L`，求四列：

`G_R(L), A_R(L), K_R(L), lambda_R''(0)`

再求两个比值：

`F_R(L)=lambda_R''(0)/|j_R|`

`S_R(L)=lambda_R''(0)/G_R(L)`。

若 `S_R(L)` 收敛到常数，说明 variance 继承 conductance 标度。若 `S_R(L) ~ L^delta` 或出现 `log L` 漂移，则标度不同。若两种 reservoir 实现先经平均-current 盲校准得到相同 `G_R(L)` 标度，然后在未参与调参的 `S_R(L)` 上不同，才算诊断性反例候选。

## 4. 对三段 alpha 的野路子预测

这里不是给最终结论，而是给可击毙预测。

### `alpha>3/2`

bulk 二阶矩有限，平均 conductance 预期 `G_R(L)~L^-1`。若右 reservoir activity 没有随 `L` 降低，`A_R(L)` 可能先给出 `O(1)` 的平衡交换噪声；但对净 current 的平衡 FCS，注入与抽出相关项可能抵消到 `L^-1`。因此本段关键不是算 `G_R`，而是检查 `A_R+K_R` 的抵消精度。

可计算击毙条件：

`A_R(L)=O(1)`, `K_R(L)=-A_R(L)+O(L^-1)`。

若该抵消成立，`lambda_R''(0)~L^-1`。若慢 buffer 在平均 conductance 已盲校准同标度后仍破坏抵消，则出现 `O(1)` 或非 `L^-1` 噪声的诊断信号。

### `alpha=3/2`

平均 conductance 候选为 `(log L)/L`。这里最脆弱，因为 Green 函数通常也有对数，但未必同一个对数。需要直接测试

`S_R(L)=lambda_R''(0)/[(log L)/L]`。

若 `S_R(L)` 仍带 `log L`，例如 `S_R(L)~log L` 或 `1/log L`，就说明 variance 没有简单继承 conductance。

### `1<alpha<3/2`

平均 conductance 候选为

`G_R(L)~L^{-(2alpha-2)}`。

我最怀疑本段存在分离，因为 long jumps 让“到达右 reservoir 的时间”与“在 bulk 中跨越距离的能力”脱钩。平均通量由跨尺度跳跃的有效电阻决定；variance 可能由右边界局域 occupation 的更新频率和返回相关决定。

可击毙预测：

`lambda_R''(0) ~ L^{-beta_2(alpha)}`

其中 `beta_2(alpha)` 不必等于 `2alpha-2`。数值上若

`beta_2(alpha) = 2alpha-2`

且 `S_R(L)` 在不同 reservoir 实现下稳定，B 的分离假说被击毙；若 `beta_2` 随 reservoir 实现改变，则 conductance 不能单独推出 FCS 二阶。

## 5. 深挖1：本轮同构的更深数学结构

第一层：电网络 effective conductance vs local time。

随机游走电网络里，有效电导刻画从左到右的逃逸概率/通量；但某个边界节点的 local time、返回次数和 hitting-time 方差由 Green 函数控制。把它翻译回来：

`G_R(L)` 是平均跨系统传输能力；

`lambda_R''(0)` 是右 reservoir 边界 local time 的波动。

二者同标度需要额外定理，不是定义。

第二层：Poisson 方程的 Hodge 分解。

current observable 可以拆成梯度部分与循环/散度自由部分。conductance 只看能由 reservoir 密度势差驱动的梯度通道；variance 通过 Poisson 方程会看到 non-gradient residual。若 long-jump kernel 引入大量非局域边，这些 residual 的 Green 权重可能改变 `lambda_R''(0)`。

第三层：从 local time 到 renewal aging。

右 reservoir 事件序列不是自动 Poisson。它是由 hitting/return cycles 诱导的点过程。若 hitting-time 分布有重尾或随 `L` 改变的变异系数，则

`Var Q_R(t)` 的标度由 renewal 方差控制，而不是只由平均 hitting time 控制。

## 6. 深挖2：原学科结构的下一层推广

第一层推广：从电网络到有源边界的 Norton/Thevenin 等效。

平均 transport 可以被压缩成一个等效 conductance；但噪声还需要一个等效 noise source。两个网络有相同 Thevenin conductance，却可以有不同 Norton noise。物理翻译：同一个 `G_R(L)` 不唯一决定 `lambda_R''(0)`，除非证明 fluctuation-dissipation 把 noise source 锁定。

第二层推广：从 renewal process 到排队论的服务时间分布。

右 reservoir 可以看作 server，bulk 到达右边界是 arrival process，reservoir 抽出/注入是 service。平均吞吐量在稳定队列中可由瓶颈服务率决定；输出方差还取决于 inter-arrival 和 service-time 的平方变异系数。于是一个可检验反例是：固定吞吐量，改变服务时间分布，让输出 Fano factor 随 `L` 改变。

第三层推广：从单 server 到 Jackson network 的准可积例外。

若 long-jump exclusion 的右边界在某些 reservoir 选择下恰好形成 product-form/Jackson-like network，则输出过程可能因 Burke-type theorem 变成 Poisson，variance 才被 conductance 锁住。也就是说，同标度可能不是普适物理，而是某类 reservoir 实现的准可积性质。

## 7. 本轮落地：最小计算流程

不需要先做全 FCS。只要解一个稳态和一个 Poisson 方程：

1. 固定 observable 为 `Q_R(t)`，列出所有右 reservoir 注入/抽出事件并赋 `g_R=±1`。
2. 对 finite `L` 的 long-jump exclusion generator 求稳态 `pi`。
3. 计算 `j_R` 与线性响应 `G_R(L)`。
4. 在 `Delta rho=0` 或小偏压下计算 `A_R(L)`。
5. 解 `-L phi_R=b_R-j_R`，在零均值子空间中求 `K_R(L)`。
6. 第一阶段只用 `j_R` 和 `G_R(L)` 校准直接 reservoir 与 buffer reservoir，使二者平均 conductance 同标度；校准时冻结所有后续 `S_R` 相关输出。
7. 第二阶段在固定参数上盲算 `A_R,K_R,lambda_R''(0)`，拟合 `S_R(L)=lambda_R''(0)/G_R(L)`。
8. 若 `G_R` 同标度但盲算得到的 `S_R` 不同，得到诊断性反例候选。

这条路线的好处是：它甚至可以在没有 tilted generator 的情况下先判断同标度是否是定理、巧合还是 reservoir 细节。

## 8. 本轮失败记录

首达时间直接套单粒子随机游走会漏掉 exclusion 的 occupancy covariance；所以我不把 hitting-time 公式当最终证明，只把它作为 Poisson 方程数值判据的解释层。

排队论构造也不是自动物理反例：如果 SOP 要求 reservoir 必须是标准 Markovian Bernoulli bath，那么 buffer reservoir 可能被认为改变了模型。但它仍是一个诊断实验：先只用平均-current 数据把 `G_R(L)` 同标度固定住，再盲算 variance；若冻结参数后 variance 变了，就说明 `G_R(L)` 本身不足以推出 `lambda_R''(0)`。

## 末格式

本轮的跨学科跳跃：电网络/renewal process/排队论 -> effective conductance 与出口 noise source 分离 -> 把右 reservoir-current `Q_R(t)` 的 variance 写成 activity + Poisson-Green 相关项。

这个结构的数学对象：右 reservoir-current `Q_R(t)`；边界跳变函数 `g_R(x,y)`；平均 current `j_R`；右边界 activity `A_R(L)`；Poisson 方程 `-L phi_R=b_R-j_R`；Green 相关项 `K_R(L)`；标度比值 `S_R(L)=lambda_R''(0)/G_R(L)`；renewal Fano 判据 `F_R(L)=lambda_R''(0)/|j_R|`。

如果这个同构成立，最奇怪的可检验预测是：存在两种右 reservoir 实现先经平均-current 盲校准后拥有相同 conductance 标度 `G_R(L)`，但冻结参数后盲算出的 `S_R(L)` 随 `L` 或 reservoir 服务机制改变；尤其在 `1<alpha<3/2`，`lambda_R''(0)` 的指数 `beta_2(alpha)` 可能不等于 `2alpha-2`。

A博士最可能反对的点：标准 Markovian reservoir 与 fluctuation-dissipation 可能强迫 `lambda_R''(0)` 与 conductance 同标度，buffer/queue 反例改变了模型。我的回应是：这正是本轮判据要检查的东西；若标准 reservoir 中 `A_R+K_R` 精确抵消并给出 `S_R(L)->const`，B 分离假说被击毙；若仅在特定 reservoir 中成立，则同标度不是 conductance 的逻辑后果，而是实现依赖定理。

本轮失败记录（如有）：单粒子首达时间类比不能直接替代 exclusion 的 Poisson 方程；renewal 公式只在近似独立、有限二阶等待时间、弱相关条件下作为启发；buffer reservoir 不能直接声称为模型内反例，只能先作为“同一 conductance 盲校准、不同 FCS 盲算”的诊断实验。

下一步计划：请数值组先做 Poisson 方程四列表 `G_R,A_R,K_R,lambda_R''(0)`；对 buffer 构造先只用 `j_R,G_R` 做独立校准并冻结参数，再盲算直接 reservoir vs buffer reservoir 的 `S_R(L)` 比较；若 `S_R(L)` 在三段 alpha 都收敛到常数且与 reservoir 实现无关，则 B 路线终止。

需要PI投喂的文献方向：Markov additive functional Poisson equation current variance；electrical network Green function local time variance；renewal process Fano factor first passage current；exclusion process non-gradient method current fluctuations；queueing output process Burke theorem finite buffer reservoir。
