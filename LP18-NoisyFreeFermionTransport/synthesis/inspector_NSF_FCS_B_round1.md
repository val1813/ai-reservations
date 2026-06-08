# INSPECTOR report: NSF_FCS_round1_B

输入文件：`current/B/NSF_FCS_round1_B.md`

限制执行记录：未读取 A 文件。只检查 B 的 `INSPECTOR_CHECK` 块与关键公式。

## Q1. 量纲校对

### `Q_R(t)=N_R^{out}(t)-N_R^{in}(t)`

- 左边 SI 单位：无量纲计数。
- 右边 SI 单位：无量纲计数。
- 匹配：通过。

### `lambda_R''(0)=lim_{t->infty} t^-1 Var Q_R(t)`

- 左边 SI 单位：计数二阶累积量增长率，`time^-1`。
- 右边 SI 单位：`time^-1 * dimensionless^2 = time^-1`。
- 匹配：通过。

### `j_R=lim_{t->infty} t^-1 E Q_R(t)`

- 左边 SI 单位：`time^-1`。
- 右边 SI 单位：`time^-1 * dimensionless = time^-1`。
- 匹配：通过。

### `a_R=sum_x pi(x) sum_y k(x,y) g_R(x,y)^2`

- `pi` 无量纲，`k(x,y)` 为 `time^-1`，`g_R^2` 无量纲。
- 左边 SI 单位：`time^-1`。
- 右边 SI 单位：`time^-1`。
- 匹配：通过。

### Poisson 方程 `-L phi_R=b_R-j_R`

- `L` 单位：`time^-1`。
- `b_R(x)=sum_y k(x,y)g_R(x,y)` 单位：`time^-1`。
- `j_R` 单位：`time^-1`。
- 若 `phi_R` 无量纲，则左边单位为 `time^-1`，右边单位为 `time^-1`。
- 匹配：通过。

### `K_R(L)=2 <b_R-j_R, phi_R>_pi |_{Delta rho=0}`

- `b_R-j_R` 单位：`time^-1`。
- `phi_R` 无量纲。
- `pi` 内积无量纲加权。
- `K_R` 单位：`time^-1`。
- 匹配：通过。

### `lambda_R''(0)=A_R(L)+K_R(L)`

- `A_R` 单位：`time^-1`。
- `K_R` 单位：`time^-1`。
- 左边单位：`time^-1`。
- 右边单位：`time^-1`。
- 匹配：通过。

### `S_R(L)=lambda_R''(0)/G_R(L)`

- `lambda_R''(0)` 单位：`time^-1`。
- `G_R=partial_{Delta rho}j_R|_{Delta rho=0}`；若 `Delta rho` 是 occupation/density difference，按无量纲处理，则 `G_R` 单位为 `time^-1`。
- `S_R` 单位：无量纲。
- 匹配：通过，前提是 `Delta rho` 明确为无量纲密度差。若使用有量纲密度，需在 `G_R` 定义中补上密度单位。

### renewal formula

公式：

`j_R ~ E[X]/E[tau]`

`lambda_R''(0) ~ Var(X)/E[tau] + (E[X])^2 Var(tau)/E[tau]^3`

- `X` 无量纲，`tau` 单位为 `time`。
- `j_R` 单位：`time^-1`。
- 第一项 `Var(X)/E[tau]` 单位：`time^-1`。
- 第二项 `(E[X])^2 Var(tau)/E[tau]^3` 单位：`time^2/time^3=time^-1`。
- 匹配：通过。

### 超越函数自变量

- 文中出现 `log L`。若 `L` 表示系统尺寸格点数，则无量纲，通过。
- 未发现 `exp/sin/sinh` 等需额外检查的有量纲自变量。

量纲结论：主体 `INSPECTOR_CHECK` 量纲通过；但正文第 1 节的早期公式写成 `lambda_R''(0)= a_R + 2 <g_R-j_R, phi_R>_pi` 有类型/量纲风险。`g_R(x,y)` 是边跳变函数，无量纲；`j_R` 是态平均流率，`time^-1`；二者不能直接相减，也不能直接与态函数 `phi_R` 做 `pi` 态内积。应改为 `lambda_R''(0)=a_R+2<b_R-j_R,phi_R>_pi` 或显式定义边空间内积和对应的 rate 权重。当前后文 `K_R=2<b_R-j_R,phi_R>_pi` 是一致的。

阻断项：有。原因是同一核心公式在正文早期版本存在类型错误，虽然后文定义修正了它。

## Q2. 符号/方向校对

### `lambda_R''=A_R+K_R`

- 若 `A_R=O(1)` 且 `K_R=-A_R+O(G_R)`，则 `lambda_R''=O(G_R)`，方向正确。
- 若 cancellation 被破坏，`lambda_R''` 可保留 `O(1)` 或其他标度，方向正确。
- 需要注意：`K_R` 可为负，但总 variance growth `lambda_R''` 必须非负。文中没有违反该约束，但数值流程应检查 `A_R+K_R>=0`。

### `S_R=lambda_R''/G_R`

- 若 `lambda_R''~G_R`，则 `S_R` 收敛常数，方向正确。
- 若 `lambda_R''/G_R~L^delta` 或带额外 `log L`，则标度不同，方向正确。
- 高危比值检查：分子分母未放反。若目的是判断 variance 是否继承 conductance，`lambda/G` 比 `G/lambda` 更自然，因为继承时为常数。

### renewal direction

- 增大 `Var(tau)` 会增大 renewal 公式第二项，方向正确。
- 但该方向只在 `E[X]` 不为零时直接影响第二项。对平衡净 current 或严格线性响应零偏压极限，通常 `E[X]` 可能为 0 或一阶小量，此时 `(E[X])^2 Var(tau)/E[tau]^3` 是二阶偏压量，不能单独解释平衡二阶 FCS 的 leading scaling。
- 若 B 要用该式解释 `Delta rho=0` 下的 `lambda_R''`，应改用带符号 reward renewal 的完整方差率，或说明此 renewal 判据只用于有限偏压/非零平均 reward 的诊断层。

方向结论：`S_R` 与 cancellation 判据方向通过；renewal formula 的“等待时间方差导致 variance 标度分离”方向需要附加非零 `E[X]` 或更完整的 signed-reward 条件。

## Q3. 循环论证校对

### Poisson 方程四列表

数据生成方式：同一 finite-L long-jump exclusion Markov generator 的稳态、activity、Poisson 方程解。

输入假设：给定 generator、observable `Q_R`、boundary rates。

检查数据是否由结论假设生成：不是。`G_R,A_R,K_R,lambda_R''` 可由 generator 直接计算，不需要预设 `lambda_R''` 是否继承 `G_R`。

循环结论：未发现循环。

### buffer reservoir 反例

数据生成方式：改变右 reservoir 实现为 `system boundary site <-> buffer <-> reservoir`，调 `u_L,v_L`，再计算同样的 `G_R,A_R,K_R,lambda_R''`。

输入假设：允许 buffer reservoir 作为同一问题域内的 reservoir 实现；允许调参保持平均 conductance 同标度。

检查数据是否由结论假设生成：部分风险。文中说“两组都可以通过调整 `u_L` 让平均 current 同标度，但 `lambda_R''` 可能不同”。这不是严格循环论证，因为最终仍要求直接计算 `lambda_R''`；但“可调到同一 `G_R` 且不同 `S_R`”目前是设计目标，不是已证明事实。

循环风险判定：警告，不阻断。避免循环的最低要求是先独立给出 `G_R(u_L,v_L)` 的线性响应计算或数值拟合，再在不使用目标 `lambda_R''` 的情况下选定两组 `u_L,v_L`，最后盲算 `S_R`。若用“想要不同 variance”来反向选择 `v_L` 的 L 标度，则会变成诊断性构造而非反例证明。

### 模型内反例资格

文中已承认：若 SOP 或物理问题固定为标准 Markovian Bernoulli bath，buffer reservoir 可能被判定为改变模型。

循环结论：这不是循环论证，而是反例外推范围问题。报告中应显式标注：buffer reservoir 至少是“conductance 不足以决定 FCS 的实现依赖诊断”，是否为原模型内反例需 PI 判定 reservoir class。

## Q4. 量级鸿沟标记

出现的量级比较：

- `A_R(L)=O(1)` vs `G_R(L)~L^-1`，随 `L` 增长有任意大尺度差。
- `A_R(L)=O(1)` vs `G_R(L)~(log L)/L`，随 `L` 增长有任意大尺度差。
- `A_R(L)=O(1)` vs `G_R(L)~L^{-(2alpha-2)}`，`1<alpha<3/2` 时随 `L` 增长有幂律差。
- `Var(tau)~L^eta E[tau]^2` 会给 `lambda` 额外 `L^eta`，若 `eta` 大且 L 足够大，可形成数量级鸿沟。

标记：警告。文中已经把这些作为需检查的 cancellation/分离机制，不是直接错误；但如果后续推导把 `A_R=O(1)` 与 `lambda_R''~G_R` 同时使用，必须显式依赖 `K_R=-A_R+O(G_R)` 的高精度抵消。

## Q5. 代数验算

### Poisson/Dirichlet 方差分解

从定义：

- `b_R(x)=sum_y k(x,y)g_R(x,y)`，单位 `time^-1`。
- `j_R=sum_x pi(x)b_R(x)`，单位 `time^-1`。
- `-L phi_R=b_R-j_R`。
- `a_R=sum_x pi(x)sum_y k(x,y)g_R(x,y)^2`。

代入标准 CTMC Markov additive functional 方差率结构，若采用 `-L phi=f=b-j` 约定，则：

`lambda_R''=a_R+2<f,phi_R>_pi`

即：

`lambda_R''=a_R+2<b_R-j_R,phi_R>_pi`

所以后文定义：

`A_R=a_R|_{Delta rho=0}`

`K_R=2<b_R-j_R,phi_R>_pi|_{Delta rho=0}`

推出：

`lambda_R''=A_R+K_R`

代数通过。早期 `2<g_R-j_R,phi_R>_pi` 不通过，需统一为 `b_R-j_R`。

### renewal formula 代数

对 compound renewal reward process：

`Q(t)=sum_{n=1}^{N(t)}X_n`

在 i.i.d. reward 与 waiting、有限二阶矩、长时极限存在的条件下，方差率常见形式为：

`sigma^2 = Var(X - j tau)/E[tau]`

其中 `j=E[X]/E[tau]`。若 `X` 与 `tau` 独立，则展开为：

`sigma^2 = Var(X)/E[tau] + (E[X])^2 Var(tau)/E[tau]^3`

因此 B 文中的 renewal formula 在独立或忽略协方差条件下代数通过。若 `X` 与 `tau` 相关，缺少交叉项：

`-2 E[X] Cov(X,tau)/E[tau]^2`

所以该式应标注为近似式/独立 reward-waiting 特例。对于 exclusion/hitting-return cycles，相关性不应默认忽略。

### 极限退化

- Poisson waiting：`Var(tau)=E[tau]^2`，固定 `X=1` 时公式给 `lambda=1/E[tau]`，退化正确。
- 零平均 reward：`E[X]=0` 时第二项消失，`lambda=Var(X)/E[tau]`。因此“waiting variance 改变净流 variance leading scaling”的说法不适用于零平均 reward 的该简化公式。
- conductance 继承：若 `lambda~G`，`S=lambda/G->const`，退化正确。

## Q6. 综合判定

INSPECTOR 阻断：核心公式需修正后重提。

具体阻断错误：

`lambda_R''(0)= a_R + 2 <g_R-j_R, phi_R>_pi` 中 `g_R` 是边函数且无量纲，`j_R` 是态平均流率且单位 `time^-1`，不能相减，也不能直接进入 `pi` 态内积。建议修正为：

`lambda_R''(0)=a_R+2<b_R-j_R,phi_R>_pi`

并与后文 `K_R=2<b_R-j_R,phi_R>_pi` 保持一致。

INSPECTOR 警告：

1. `S_R=lambda_R''/G_R` 量纲和方向通过，但需声明 `Delta rho` 是无量纲密度差。
2. renewal formula 量纲通过，方向在非零 `E[X]` 或有限偏压诊断中通过；若用于平衡/线性响应 leading variance，需要完整 signed-reward renewal 方差率，并检查 `X-tau` 相关项。
3. buffer reservoir 反例不是严格循环论证，但目前只是诊断性构造。要成为反例，必须先独立固定两组具有同标度 `G_R` 的 `u_L,v_L`，再计算 `lambda_R''`/`S_R`，不能用目标 variance 差异反向选参。

最终结论：

`INSPECTOR 阻断`。B 的路线可继续作为诊断框架，但当前交付稿中关键方差分解公式有类型/量纲错误；修正该公式并补充 renewal 适用条件后，`A_R+K_R`、`S_R` 与 buffer 诊断部分可重新提交检查。
