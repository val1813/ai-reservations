# INSPECTOR A Round2

输入文件：`current/A/round2_A.md`

限制：未读取 B 文件；本报告只校对 A Round2 的 INSPECTOR_CHECK 块及其相关公式/方向结论。

## Q1. 量纲校对

### 1. Zeno 投影速率

公式：

`r_{jk}=2|J_{jk}|^2/gamma_phi`

约定：`J_{jk}` 与 `gamma_phi` 均取角频率单位 `s^{-1}`；若 Hamiltonian 用能量单位，则应以 `J_{jk}/hbar` 进入公式。

左边 SI 单位：`s^{-1}`。

右边 SI 单位：`(s^{-1})^2 / s^{-1} = s^{-1}`。

匹配：通过。

说明：A 文中先用 `gamma sum_l D[n_l]`，后在 INSPECTOR_CHECK 中写 `gamma_phi`。只要 `gamma_phi` 明确定义为相干衰减率，公式量纲和系数写法自洽；若 `gamma_phi` 改指 Lindblad 单站强度以外的参数，必须同步重写前因子。

### 2. 长跳核与二阶矩

公式：

`J(r)=J0 r^{-alpha}`

`r(r)=2J0^2/(gamma r^{2alpha})`

若晶格距离 `r` 以 lattice spacing 为单位，则 `r^{-alpha}` 无量纲，`J0` 为 `s^{-1}`，`r(r)` 为 `s^{-1}`。若物理距离 `x=ra` 进入幂律，则应写 `J(x)=J_* (a/|x|)^alpha` 或给 `J_*` 相应单位，避免 `J0 |x|^{-alpha}` 的量纲缺口。

二阶矩：

`M_2=sum_r r^2 r(r)`

若 `r` 是格点距离，`M_2` 单位为 `s^{-1}`，对应格点单位下的扩散常数；若换成物理长度，需乘 `a^2`，单位为 `m^2 s^{-1}`。

匹配：通过，前提是 A 文默认晶格距离无量纲。

### 3. d 维二阶矩阈值

公式：

`M_2 ~ int dr r^{d-1} r^2 r^{-2alpha} = int dr r^{d+1-2alpha}`

积分变量若为无量纲径向格点距离，则量纲无误。收敛条件为 `d+1-2alpha < -1`，即

`alpha > (d+2)/2`

匹配：通过。

### 4. `lambda''` 标度候选

A 文候选：

`lambda''(0) ~ L^{-(2alpha-2)}` for `1<alpha<3/2`

`lambda''(0) ~ (log L)/L` at `alpha=3/2`

若 `lambda` 是单位时间 CGF，`lambda''(0)` 单位应为 `s^{-1}`；右边只写了 `L` 幂，缺少速率前因子。作为 scaling 语句可以接受，但严格公式应写成

`lambda''(0) ~ C(alpha, reservoirs) (2J0^2/gamma) L^{-(2alpha-2)}`

以及临界处

`lambda''(0) ~ C_c (2J0^2/gamma) (log L)/L`

匹配：量纲上仅作为比例标度通过；作为完整公式不通过。建议在 Round3 前把 `~` 明确为只声明 `L` 标度。

超越函数自变量检查：未发现 `exp/sin/log/sinh` 等带量纲自变量问题；`log L` 应理解为 `log(L/a)` 或格点长度下的 `log L`。

## Q2. 符号/方向校对

### 1. `r_{jk}=2|J|^2/gamma` 的方向

极限 `gamma -> infinity`：`r_{jk}->0`，强退相干抑制 hopping，符合 Zeno 方向。

极限 `|J| -> 0`：`r_{jk}->0`，符合二阶扰动方向。

极限 `|J|` 增大：`r_{jk}` 增大，但仅在 `|J|/gamma << 1` 的窗口内可信。

方向：通过。

系数：在 `gamma sum_l D[n_l]` 且 `gamma_phi` 为 `rho_{jk}` 相干衰减率的约定下，单粒子二能级消元给出前因子 2。A 文对 Round1 的 `~|J|^2/gamma` 方向保留、严格前因子改为 2 的结论正确。

### 2. `alpha=3/2` 阈值方向

一维：

`M_2 ~ sum_{r>=1} r^{2-2alpha}`

级数收敛当且仅当 `2-2alpha < -1`，即 `alpha>3/2`。

极限检验：

`alpha -> infinity`：长跳尾快速衰减，二阶矩有限，普通扩散方向正确。

`alpha=1`：`sum_r r^0` 发散，不能是普通二阶矩扩散，方向正确。

`alpha=3/2`：`sum_r 1/r` 对数发散，临界 `log L` 修正方向正确。

方向：通过。

### 3. d 维阈值方向

`alpha>(d+2)/2` 随维度升高而变严格。shell degeneracy `r^{d-1}` 增大远距离权重，因此阈值右移，方向正确。

`mu=2alpha-d` 与 kernel `p(x)~|x|^{-(d+mu)}` 一致；分数区间 `0<mu<2` 对应 `d/2<alpha<(d+2)/2`，方向正确。

方向：通过。

### 4. `lambda''` 标度方向

将 `mu=2alpha-1` 代入 A 文候选：

`lambda''(0) ~ L^{-(mu-1)}` for `1<mu<2`

`alpha -> 3/2` 即 `mu -> 2`：得到 `L^{-1}`，临界二阶矩发散给出增强为 `(log L)/L`，方向与截断扩散常数 `D(L)~log L` 一致。

`alpha -> 1+` 即 `mu -> 1+`：指数趋近 0，衰减慢于普通 `L^{-1}`，方向与超扩散增强 conductance 一致。

方向：作为 boundary conductance/reservoir-current 标度候选通过。

警告：A 文同时提到“跨 cut 的所有长跳之和”。对非局域跳跃，cut current、reservoir current、以及端点 reservoir 注入流的噪声标度不必自动相同。`lambda'' ~ L^{-(2alpha-2)}` 不能仅凭二阶矩阈值推出为所有 current 定义的 FCS 标度；必须在 Round3 明确 current observable 和 boundary implementation。

## Q3. 循环论证校对

Zeno 速率部分：A 文用二能级相干消元显式生成 `rho_{jk}` 并代回 `dot p_j`，不是只重复输入假设。通过。

`alpha=3/2` 部分：由 `r(r)~|J(r)|^2/gamma` 与经典长跳二阶矩条件推出，不是把文献数值 `alpha_c approx 1.5` 当作证明。通过。

d 维阈值部分：由 shell degeneracy 和二阶矩积分推出。通过。

`lambda''` 部分：A 文承认是 Round3 候选和待验证对象；但目前从 fractional time scale 到 FCS 二阶导的推断较粗，且依赖 current/boundary 定义。标记为警告，不作为已证明结论使用。

## Q4. 数量级鸿沟标记

未发现 `10^N` vs `10^M` 且 `|N-M|>10` 的数量级比较。

存在临界发散标记：

`D_eff(alpha) ~ 1/(2alpha-3)` 在 `alpha -> 3/2+` 发散；有限系统 crossover 可能很宽。A 文已显式标出，不构成错误。

## Q5. 代数验算

### 5a. Zeno 二阶消元

给定

`dot rho_{jk} = -i J_{jk}(p_k-p_j) - gamma_phi rho_{jk}`

绝热消元：

`rho_{jk} = -i J_{jk}(p_k-p_j)/gamma_phi`

人口方程：

`dot p_j = -i sum_k (J_{jk} rho_{kj} - rho_{jk} J_{kj})`

使用 `J_{kj}=J_{jk}^*` 与 `rho_{kj}=rho_{jk}^*`，得到

`dot p_j = sum_k 2|J_{jk}|^2/gamma_phi (p_k-p_j)`

系数、符号、指数：通过。

### 5b. 二阶矩阈值

一维：

`sum_r r^2 r(r) ~ sum_r r^{2-2alpha}`

p-series 收敛条件：

`2-2alpha < -1`

`alpha > 3/2`

通过。

d 维：

`int dr r^{d+1-2alpha}`

无穷远收敛条件：

`d+1-2alpha < -1`

`alpha > (d+2)/2`

通过。

总跳率：

`R ~ int dr r^{d-1-2alpha}`

收敛条件：

`d-1-2alpha < -1`

`alpha > d/2`

通过。

### 5c. 临界对数

一维 `alpha=3/2`：

`M_2(L) ~ sum_{r<=L} r^{-1} ~ log L`

若 ordinary conductance `~D(L)/L`，候选为 `(log L)/L`。代数方向通过；是否等于 `lambda''` 仍依赖 current observable。

### 5d. 数值来源级别

文献数值 `alpha_c approx 1.5` 来源于 Sarkar/Agarwalla/Bhakuni PRB 2024，被 A 文作为支持背景而非严格推导输入。可接受。

`lambda''` 标度没有全文级推导来源，A 文标为候选。必须维持“待验证”标记。

## Q6. 综合判定

结论：INSPECTOR 警告通过。

通过项：

- `r_{jk}=2|J_{jk}|^2/gamma_phi` 在 A 文 Lindblad 约定下量纲、系数和方向均正确。
- 一维 `alpha=3/2` 是未归一化 bulk power-law hopping 经 Zeno 二阶投影后的二阶矩阈值，方向正确。
- d 维阈值 `alpha>(d+2)/2` 与分数区间 `d/2<alpha<(d+2)/2` 正确。

警告项：

- `lambda''(0) ~ L^{-(2alpha-2)}` 与临界 `(log L)/L` 只能作为 boundary conductance/reservoir-current 的 `L` 标度候选继续使用。它缺少速率前因子 `2J0^2/gamma`，且不能自动推广到所有 cut-current FCS 定义。
- Round3 必须同时固定：current observable、reservoir coupling、是否统计所有跨 cut 长跳、以及 `lambda` 是否为单位时间 CGF。否则 `lambda''` 的量纲和方向可能被错误复用。

阻断项：无。

