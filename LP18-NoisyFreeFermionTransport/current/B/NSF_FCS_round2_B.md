# B博士 NSF-FCS-1 Round 2

## 0. 本轮框架

本轮继续避开 A 的 `H_-1` 标准路线，不把 `lambda_R''(0)` 直接当作 conductance 的自动副本，也不把 renewal/buffer 当作已证反例。  
我只做一件事：给出一个**能算、能比、能杀假说**的最小判据。

核心对象仍是右 reservoir current `Q_R(t)`，但本轮的重点换成：

`S_R(L)=lambda_R''(0)/G_R(L)`

其中 `G_R(L)` 是先由平均电流/线性响应独立校准得到的边界 conductance，`lambda_R''(0)` 则由小矩阵 Poisson 方程直接算出。  
若 `S_R(L)` 仍收敛到常数，B 假说保留；若 `S_R(L)` 带额外幂律或对 reservoir 实现敏感，则 B 假说被击毙。

---

## 1. 最小数值判据

### 1.1 低密度 / 单粒子判据

优先用低密度极限的单粒子 sector。状态空间取

`Omega_L={1,...,L}`

单粒子在 bulk 做 long-jump random walk，右边界与 reservoir 交换粒子。此时：

- `G_R(L)` 来自稳态净流的线性响应；
- `lambda_R''(0)` 来自右边界净交换数的二阶 cumulant；
- `S_R(L)` 是唯一要看标度的量。

这一层的优点是：generator 规模小，`pi`、Poisson 解、Green 修正都能直接矩阵化。

### 1.2 电网络判据

把同一结构翻译成电网络：

- 节点 = 状态；
- 边权 = 跃迁率；
- 电导 = 线性响应 conductance；
- 噪声 = 右边界电流方差的 Poisson/Green 修正。

在这个翻译里，问题变成：

> 同样的有效电导 `G_R(L)`，是否对应同样的边界噪声标度 `lambda_R''(0)`？

若不对应，则 `lambda_R''` 不是 conductance 的自动继承量。

--- INSPECTOR_CHECK ---
[公式] `S_R(L)=lambda_R''(0)/G_R(L)`；`lambda_R''(0)=A_R(L)+K_R(L)`；`K_R(L)=2<b_R-J_R,phi_R>_pi`；`-L phi_R=b_R-J_R`  
[方向] 只用 `G_R(L)` 先校准平均输运，再独立计算 `A_R,K_R,lambda_R''(0)`，最终只看 `S_R(L)` 的标度是否与 reservoir 实现无关  
[数据] 来自同一 finite-L generator 的 `pi`、边界跃迁图、Poisson 方程数值解、以及两种 reservoir 实现下的 `G_R(L)` 与 `lambda_R''(0)`  
[假设] 单粒子/低密度近似可把问题压缩为有限矩阵；`Q_R(t)` 只计右边界交换；`<.,.>_pi` 只作用在状态函数上；`g_R` 先聚合进 `b_R(x)=sum_y k(x,y)g_R(x,y)`

---

## 2. 可执行的小矩阵算法

### 2.1 Generator

取有限状态空间 `Omega_L`，写 generator 为矩阵 `L`：

`(Lf)(x)=sum_y k(x,y)[f(y)-f(x)]`

右边界 observable 的跳变量写成 `g_R(x,y)`，只对右 reservoir 相关跃迁取 `+1/-1`，其他跃迁取 `0`。  
然后定义

`b_R(x)=sum_y k(x,y)g_R(x,y)`

`a_R(x)=sum_y k(x,y)g_R(x,y)^2`

稳态分布 `pi` 解

`pi L=0,  sum_x pi(x)=1`

### 2.2 Stationary distribution

数值上直接做：

1. 组装稀疏矩阵 `L`；
2. 用约束 `sum pi=1` 替换一条方程；
3. 解线性系统得到 `pi`；
4. 检查 `||pi L||` 是否足够小。

### 2.3 Poisson solve

构造中心化右端：

`h_R(x)=b_R(x)-J_R`

其中

`J_R=<b_R>_pi`

解 Poisson 方程

`-L phi_R=h_R`

并用规范条件固定零模，例如

`<phi_R>_pi=0`

实现时可删去一个状态并解去奇异矩阵，或用最小二乘/伪逆。

### 2.4 提取 `A_R/K_R`

直接算

`A_R(L)=<a_R>_pi`

`K_R(L)=2<h_R,phi_R>_pi`

于是

`lambda_R''(0)=A_R(L)+K_R(L)`

最后再除以独立校准的 `G_R(L)`：

`S_R(L)=lambda_R''(0)/G_R(L)`

### 2.5 最小实现顺序

1. 先算 `pi`；
2. 再算 `G_R(L)`；
3. 再算 `A_R(L),K_R(L)`；
4. 再算 `S_R(L)`；
5. 最后比较不同 reservoir 实现下的 `S_R(L)`。

这一步顺序不能倒。若把 `lambda_R''(0)` 先拿去调参，就会把诊断变成自证。

---

## 3. 何时保留 / 何时击毙 B 假说

### 3.1 保留 B 假说的结果

满足下面任一条，都只能算“B 还活着”：

1. `G_R(L)` 的标度相同，但 `S_R(L)` 也在不同 reservoir 实现下收敛到同一常数；
2. `A_R(L)` 与 `K_R(L)` 各自会变，但总和 `lambda_R''(0)` 仍跟着 `G_R(L)` 同阶；
3. 低密度/单粒子 sector 与电网络翻译给出同一 `S_R(L)` 极限。

### 3.2 击毙 B 假说的结果

下面任一条都足够击毙：

1. `G_R(L)` 已被校准成同阶，但 `S_R(L)` 仍出现幂律漂移或对数漂移；
2. 两种 reservoir 实现给出相同 `G_R(L)`，却给出不同的 `S_R(L)` 极限；
3. `A_R(L)` 只剩边界局域项，而 `K_R(L)` 带出额外长程 Green 修正，导致 `lambda_R''(0)` 的标度不同于 `G_R(L)`；
4. 单粒子网络中已经能复现“同电导，不同噪声”。

### 3.3 我现在更看重的击毙方式

最强的击毙不是“某个点算错了”，而是：

`S_R(L)` 在 `L` 变大时不收敛，或者不同边界实现给出不同极限。

这说明 variance 不是 conductance 的自动继承量，而是额外的边界动力学对象。

---

## 4. 深挖1：电网络 -> Poisson -> Green

### 4.1 第一层

把边界电流噪声写成 Poisson 方程修正：

`lambda_R''(0)=<a_R>_pi+2<b_R-J_R,phi_R>_pi`

这里 `a_R` 是边界活动，`phi_R` 是 Poisson 解。  
这一步说明：二阶量不是只看平均流，而是看“活动 + Green 修正”。

### 4.2 第二层

若 `b_R-J_R` 在边界附近是局域的，则 `phi_R` 的传播长度由网络 Green 函数决定。  
于是可能出现：

- `G_R(L)` 已经是一个标度；
- 但 `K_R(L)` 通过 Green 函数带出不同标度；
- 最后 `S_R(L)` 不再跟 conductance 同阶。

这就是本轮最想抓的“非继承”机制。

---

## 5. 深挖2：单粒子 / 低密度 -> renewal 只作启发，不作结论

### 5.1 第一层

单粒子极限下，右边界交换可以近似成“到达-服务”过程。  
但我这里只把它当作数值启发：它告诉我怎样设计最小矩阵模型，而不是证明 renewal 公式。

### 5.2 第二层

若等待时间方差或返回时间尾部改变了 `lambda_R''(0)`，那说明噪声由服务时间分布主导，而不是由平均电导主导。  
这类结果若在单粒子模型里已经出现，就足以提示：在 many-particle 模型里，variance 可能继承的是 boundary memory，而不是 `G_R(L)`。

反过来，若单粒子模型里 `S_R(L)` 仍是常数，那就更像“B 假说只在特殊实现里成立”，而不是普遍定理。

---

## 6. 本轮失败记录

1. 我没有把 `lambda_R''(0)` 直接降成 `G_R(L)` 的同义词；
2. 我没有把 renewal 当成最终证明；
3. 我没有把 buffer reservoir 当成已证内反例。

这三点都保住了，所以本轮没有逻辑性自毁。

---

## 7. 下一步计划

1. 先做一个 `O(L)` 或更小的单粒子矩阵例子；
2. 先独立算 `G_R(L)`，再算 `A_R,K_R,lambda_R''(0)`；
3. 比较两种右边界实现的 `S_R(L)`；
4. 若 `S_R(L)` 稳定，B 假说暂存活；若不稳定，直接击毙。

需要的最小文献方向：

`boundary current variance, additive functional CLT, Poisson equation, electrical network Green function, single-particle transport, nonlocal conductance, reservoir noise`

---

## 8. 本轮收尾格式

本轮的跨学科跳跃：`[电网络/单粒子] -> [Poisson/Green 修正] -> [边界噪声是否继承 conductance]`

这个结构的数学对象：`[generator, pi, Poisson solve, A_R, K_R, S_R]`

如果这个同构成立，最奇怪的可检验预测是：`[同样的 G_R(L) 也可能对应不同的 S_R(L)]`

A博士最可能反对的点：`[你把单粒子/电网络的边界噪声推广得太快]`

本轮失败记录（如有）：`[未做多粒子 full FCS；renewal 仍只是启发层]`

下一步计划：`[先算最小矩阵例子，再比较两种 reservoir 实现的 S_R(L)]`

需要PI检索的文献方向：`[boundary current variance, Poisson equation CLT, electrical network noise, single-particle reservoir transport]`
