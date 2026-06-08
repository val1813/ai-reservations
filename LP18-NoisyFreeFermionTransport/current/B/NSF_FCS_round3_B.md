# B博士 NSF-FCS-1 Round 3

## 0. 本轮框架声明

本轮不再把“低密度/最小矩阵”当作口头判据，而把它压成一个可执行的数值验尸台。

跨学科跳跃：`分布式系统日志复制 -> 账本分解 -> 物理 jump-current FCS`。

借来的结构不是表面类比，而是数学对象：一个全局提交量可以被拆成本地提交 activity、状态同步 corrector、以及日志与状态更新之间的 cross term。映射回本问题：

- 日志提交数 = 右 reservoir jump-current `Q_R(t)`;
- 本地提交速率 = `<a>`;
- 状态同步延迟 = `2<h,phi>`;
- 日志/状态交叉项 = `2<C>`;
- 总账本增长率 = `lambda_R''(0)`;
- 独立校准的吞吐响应 = `G_R`;
- 是否继承 conductance 的诊断量 = `S_R=lambda_R''(0)/G_R`。

核心要求：每一个有限 `L`、每一种 reservoir 实现，都必须输出同一张表：

`L, reservoir_id, <a>, 2<h,phi>, 2<C>, lambda_R''(0), G_R, S_R, err_balance, err_tilt, status`

如果 `C` 无法稳定取出，则不能硬凑 decomposition；直接切换到 tilted generator 主特征值二阶有限差分，输出 `lambda_R''(0)`、`G_R`、`S_R`，并把 `<a>,2<h,phi>,2<C>` 标记为 decomposition failed。

---

## 1. 维度与无量纲 affine 定义

### 1.1 计数字段

计数字段 `chi` 无量纲。右 reservoir 计数增量

`g_R(x,y) in {-1,0,+1}`

是粒子数增量，因此也是无量纲 count。

scaled cumulant generating function 定义为

`lambda_R(chi)=lim_{t->infty} t^{-1} log E_pi exp[chi Q_R(t)]`

所以

`lambda_R''(0)` 的单位是 `count^2/time`。

### 1.2 conductance 只对无量纲 affinity 求导

本轮固定 affine convention：

`F_R = beta (mu_R - mu_ref)`

其中 `beta=1/(k_B T)`，`F_R` 无量纲。边界 conductance 定义为

`G_R(L)=d J_R / d F_R |_{F_R=0}`

单位是 `count/time`。因此

`S_R(L)=lambda_R''(0)/G_R(L)`

单位是 `count`，在粒子计数 convention 下作为无量纲噪声/响应比使用。若代码用 `Delta mu` 而不是 `F_R` 做差分，必须转换：

`dJ_R/d(Delta mu)` 不可直接当作本轮的 `G_R`；
正确的是 `G_R=dJ_R/dF_R=(1/beta) dJ_R/d(Delta mu)`。

---

## 2. 最小矩阵模型与 affine 参数化

### 2.1 状态空间

低密度首测使用单粒子或稀疏多粒子有限状态空间 `Omega_L`。单粒子版本可取

`Omega_L={0,1,...,L,L+1}`

其中 `1,...,L` 是 bulk，`0` 是左 reservoir 接触空位/源，`L+1` 是右 reservoir 接触状态。也可以把 reservoir 接触吸收到边界跳率中，此时 `Omega_L={1,...,L}`。

要求不是具体状态编码，而是同一套输出量必须可由 generator 明确产生。

### 2.2 generator

采用行生成元 convention：

`(L_F f)(x)=sum_y k_F(x,y)[f(y)-f(x)]`

`k_F(x,y)` 单位为 `1/time`。右 reservoir 跳迁集合记为 `E_R`，只在这些边上 `g_R(x,y)=+1/-1`，其余边 `g_R=0`。

affine 展开：

`k_F(x,y)=k_0(x,y) exp[alpha_{xy} F_R + O(F_R^2)]`

其中 `alpha_{xy}` 无量纲。局部详细平衡实现可取右边界注入/抽取的 `alpha` 相差 1；非平衡 reservoir 实现也允许，但必须报告所用 `alpha_{xy}`。

### 2.3 独立计算 `G_R`

对每个 `L` 与 reservoir 实现，先在 `F_R=0` 求稳态 `pi_0`，再在小 affine `+delta_F,-delta_F` 求

`J_R(F)=<b_R(F)>_{pi_F}`

`G_R(L;delta_F)=[J_R(delta_F)-J_R(-delta_F)]/(2 delta_F)`

默认至少用三组 `delta_F`，例如 `delta_F in {1e-2,5e-3,2.5e-3}`，并做二次外推。`G_R` 不许用 `lambda_R''` 调参。

---

## 3. 完整二阶分解：必须输出的六个量

### 3.1 activity 与 drift

在 `F_R=0`：

`b(x)=sum_y k_0(x,y) g_R(x,y)`

`a(x)=sum_y k_0(x,y) g_R(x,y)^2`

`J=<b>_pi`

`h(x)=b(x)-J`

`<a>=sum_x pi(x) a(x)`

### 3.2 corrector

解 Poisson 方程

`-L_0 phi = h`

规范条件

`<phi>_pi=0`

输出

`2<h,phi> = 2 sum_x pi(x) h(x) phi(x)`

这一项只代表 resolvent/corrector 部分，不能把它误报为完整 `lambda_R''(0)`。

### 3.3 cross term `2<C>`

PI 综合要求把 jump-current martingale cross term 单独列出。数值上本轮采用守恒定义：

`2<C> = lambda_R''(0) - <a> - 2<h,phi>`

但这里的 `lambda_R''(0)` 必须来自独立的 tilted generator 主特征值，或者来自一个已经通过 Inspector 可校对的显式 cross-term 公式。若没有显式公式，就用 tilted 值反推 `2<C>`；这比伪造一个不稳定的边求和公式更干净。

输出总量：

`lambda_R''(0)=<a>+2<h,phi>+2<C>`

`S_R(L)=lambda_R''(0)/G_R(L)`

---

## 4. tilted generator 后备方案

当 `C` 不可稳定取出时，进入主特征值方案。

### 4.1 tilted generator

定义

`(L_chi f)(x)=sum_y k_0(x,y)[exp(chi g_R(x,y)) f(y)-f(x)]`

等价矩阵写法：非对角元

`L_chi[x,y]=k_0(x,y) exp(chi g_R(x,y))`

对角元

`L_chi[x,x]=-sum_y k_0(x,y)`

`lambda_R(chi)` 是 `L_chi` 最大实部特征值，且 `lambda_R(0)=0`。

### 4.2 二阶有限差分

取对称差分：

`lambda_R''(0;epsilon)=[lambda_R(epsilon)-2 lambda_R(0)+lambda_R(-epsilon)]/epsilon^2`

实际 `lambda_R(0)` 应小于容差，可保留实测值，不手动设零。默认

`epsilon in {1e-2,5e-3,2.5e-3,1.25e-3}`

用 plateau 或 Richardson 外推得到 `lambda_R''(0)`。若特征值求解给出小虚部，要求

`|Im lambda_R(epsilon)| <= 100 eps_machine max(1,|Re lambda_R(epsilon)|)`

否则该 `epsilon` 标记失败。

### 4.3 何时判定 `C` 不稳定

任一条件成立，放弃显式 `C`：

1. `2<C>` 随线性求解容差变化的相对漂移超过 `5%`；
2. `lambda_decomp=<a>+2<h,phi>+2<C_explicit>` 与 tilted `lambda_tilt''` 的相对差超过 `3%`；
3. `C` 的显式边求和依赖 row/column convention 转置，无法给出唯一符号；
4. Poisson 残差合格但 `2<C>` 的符号或量级在相邻 `L` 间出现非物理跳变，且 tilted 值平滑。

后备输出不再声称知道 `C` 的机制，只报告：

`<a>, 2<h,phi>, 2<C>=lambda_tilt''-<a>-2<h,phi>, lambda_tilt'', G_R, S_R`

并把 `status=C_from_tilted_residual`。

--- INSPECTOR_CHECK ---
[公式] `F_R=beta(mu_R-mu_ref)` 无量纲；`G_R=dJ_R/dF_R|_0`，单位 `count/time`；`lambda_R''(0)` 单位 `count^2/time`；`S_R=lambda_R''/G_R` 为 count convention 下无量纲比值。完整分解写作 `lambda_R''(0)=<a>+2<h,phi>+2<C>`，其中 `-L_0 phi=h=b-<b>_pi`。若 `C` 不稳定，则用 `lambda_R''(0)=[lambda(epsilon)-2lambda(0)+lambda(-epsilon)]/epsilon^2`。
[方向] `G_R` 由无量纲 affine 的平均流响应独立校准；`lambda_R''` 由完整 decomposition 或 tilted 主特征值给出；不得用 `lambda_R''` 调 `G_R`。Poisson 方程采用行生成元 `L f=sum k(f_y-f_x)`，因此 centered subspace 上解 `-L phi=h`。
[数据] 有限 `L` generator、右 reservoir jump set `E_R`、`g_R`、affine 参数 `alpha_xy`、稳态 `pi`、Poisson 残差、tilted eigenvalue 扫描、`G_R` affine 差分扫描。
[假设] 有限矩阵 irreducible；`F_R` 足够小使线性响应成立；`chi` 与 `F_R` 均无量纲；主特征值孤立；低密度 sector 是 full problem 的最小 falsification test，不是最终定理。

---

## 5. 误差控制与台账标准

### 5.1 稳态误差

稳态 `pi` 必须满足：

`||pi L_0||_1 <= 1e-10 max(1,||L_0||_1)`

`|sum_x pi(x)-1| <= 1e-12`

`min_x pi(x) >= -1e-12`

若存在小负数，允许投影回 simplex 后重算残差；若残差不合格，整行数据 `status=pi_failed`。

### 5.2 Poisson 误差

定义

`r_phi=-L_0 phi-h`

要求

`||r_phi||_{pi,2} <= 1e-9 max(1,||h||_{pi,2})`

`|<phi>_pi| <= 1e-10 max(1,||phi||_{pi,2})`

同时报告 condition number 或最小非零奇异值估计。若 Poisson 解病态但 tilted eigenvalue 稳定，优先信 tilted。

### 5.3 `G_R` 误差

三组 `delta_F` 的 central difference 外推后要求：

`rel_spread(G_R) <= 2%`

且 `G_R>0`。若 `G_R` 小到相对误差失控，报告绝对误差，并暂停 `S_R` 判据；不能用噪声比除以近零数制造结论。

### 5.4 tilted 误差

要求：

`rel_spread(lambda_R''(epsilon)) <= 3%`

若 Richardson 外推与最小两个 `epsilon` plateau 差异超过 `3%`，标记 `lambda_tilt_unstable`。若 double precision 不够，使用高精度 arithmetic 或 shift-invert 验证。

### 5.5 balance 误差

若同时有显式 `C` 与 tilted 值，必须输出

`err_balance=|(<a>+2<h,phi>+2<C>)-lambda_tilt''|/max(1,|lambda_tilt''|)`

通过阈值：

`err_balance <= 3%`

超过阈值时，不允许把显式 decomposition 用作 keep/kill 判据。

---

## 6. keep / kill criteria

### 6.1 keep B 假说的最低条件

对至少两种 reservoir 实现 `r=1,2`，在 `G_R` 独立校准后，如果存在常数 `S_*` 与指数 `p>=0` 使

`S_R^{(r)}(L)=S_*+O(L^{-p})`

且两个实现的外推极限在误差条内一致，则 B 的“variance 可能继承 conductance 标度”继续保留。

更弱但仍可保留的条件：

- `<a>`、`2<h,phi>`、`2<C>` 各自随 reservoir 实现变化；
- 但总和 `lambda_R''` 与 `G_R` 同阶；
- `S_R` 对 `L` 无系统性漂移，对 reservoir 实现无稳定分裂。

### 6.2 kill B 假说的条件

任一条成立即可 kill 本轮 B 假说：

1. 两种 reservoir 实现有相同 `G_R(L)` 标度，但 `S_R(L)` 的极限不同，且差异超过合并误差 `3 sigma`；
2. `S_R(L)` 出现稳定幂律漂移 `S_R~L^q`，`|q|>0.1`，而 `G_R` 的标度已经校准；
3. `S_R(L)` 出现稳定对数漂移，拟合 `S_R=A+B log L` 中 `B` 显著非零；
4. `lambda_R''` 的主要贡献来自 `2<C>` 的 reservoir-specific cancellation，而该 cancellation 不随 `G_R` 重标定消失；
5. tilted eigenvalue 与 decomposition 长期不一致，且不一致只在 jump-current reservoir 边界项出现。

### 6.3 暂存而非 kill

下面情况不能 kill，只能暂停：

- `G_R` 自身没有线性响应 plateau；
- `L` 太小，`S_R` 拟合指数在不同窗口间翻转；
- `C` 不稳定，但 tilted eigenvalue 也不稳定；
- 单一 reservoir 实现给出常数 `S_R`，但没有第二实现对照。

---

## 7. 深化1：账本分解 -> cohomology obstruction

第一层同构：分布式账本里的 commit log 不等于状态变量本身；它包含本地提交、状态追赶、以及同步协议带来的交叉项。物理翻译是：

`Q_R(t)=martingale activity + phi(X_t)-phi(X_0) + cross protocol residue`

这解释了为什么 `2<h,phi>` 不是完整答案。它只描述“状态追赶”的 Green correction，不能吞掉 martingale cross term。

更深一层：若 `2<C>` 可以被写成一个 coboundary 的平均，它会随 `phi` 的规范选择抵消；若不能，它就是 jump-current 的 cohomology obstruction。对应数值信号是：

- `<a>` 与 `2<h,phi>` 单独大；
- `2<C>` 也大且符号相反；
- 但总 `lambda_R''` 小并与 `G_R` 同阶。

这类 cancellation 若对 reservoir 实现敏感，就是 kill 信号；若对实现不敏感，则可能是隐藏的 universal structure。

---

## 8. 深化2：协议延迟 -> tilted spectrum

分布式系统里，当 cross term 无法通过本地日志稳定审计，最终审计方法不是继续拆账，而是读取全系统共识日志的增长率。物理翻译就是 tilted generator 主特征值。

第一层：`L_chi` 把每一次右边界跳迁直接写进谱问题，避免人为选择 `C` 的边界 convention。

第二层：若 `lambda_R(chi)` 的二阶曲率稳定，而 `<a>+2<h,phi>` 不足以重建它，则缺失部分必然是 cross/cancellation 结构；这时 B 的任务从“给出漂亮分解”变成“判断缺失结构是否继承 `G_R` 标度”。

最怪的可检验预测：

> 两个 reservoir 可以有相同的 `G_R(L)`，也有相近的 `<a>` 与 `2<h,phi>`，但 tilted curvature 给出不同的 `2<C>`，从而导致不同的 `S_R` 极限。

这就是本轮要抓的非继承证据。

---

## 9. 本轮失败记录

1. Round 2 的 `lambda_R''=<a>+2<h,phi>` 写法已经不够完整；Round 3 明确加入 `2<C>`。
2. 显式 `C` 公式若没有稳定 convention，不再硬写成定理；直接由 tilted eigenvalue 审计。
3. 单粒子/低密度测试仍只是 falsification test；通过它不等于证明 many-particle fractional reservoir 的普遍定理。

---

## 10. 下一步计划

1. 先做 `Omega_L={1,...,L}` 的单粒子 long-jump generator；
2. 对两个右 reservoir 实现分别输出完整台账；
3. 先验收 `pi`、Poisson、`G_R`、tilted 四个误差；
4. 若 `C` 稳定，比较 decomposition 与 tilted；
5. 若 `C` 不稳定，直接用 tilted `lambda_R''` 做 `S_R` scaling；
6. 用 keep/kill criteria 给 PI 一个二值判断，而不是只给趋势图。

需要 PI 投喂的文献方向：

`tilted generator current cumulants, Markov additive functional cross term, martingale decomposition jump current, full counting statistics open exclusion process, boundary reservoir noise cancellation`

---

## 11. 本轮收尾格式

本轮的跨学科跳跃：`[分布式系统日志复制] -> [账本分解/共识审计] -> [jump-current FCS 的 activity/corrector/cross-term 分解]`

这个结构的数学对象：`[finite generator, dimensionless affinity, Poisson corrector, martingale cross term, tilted generator principal eigenvalue, S_R scaling]`

如果这个同构成立，最奇怪的可检验预测是：`[相同 G_R 标度不保证相同 S_R；差异会集中在 2<C> 或 tilted curvature residual 中]`

A博士最可能反对的点：`[tilted eigenvalue 得到的是总二阶曲率，不解释 cross term 的微观 cancellation]`

本轮失败记录：`[显式 C 不稳定时不强行分解；单粒子测试不作为最终证明；G_R 必须对无量纲 affine 求导]`

下一步计划：`[生成最小矩阵台账，若 C 稳定则 decomposition 审计，若不稳定则 tilted 主特征值二阶差分审计]`

需要 PI 检索的文献方向：`[Markov additive process CLT, tilted generator FCS, jump-current martingale cross term, open SSEP current variance cancellation]`
