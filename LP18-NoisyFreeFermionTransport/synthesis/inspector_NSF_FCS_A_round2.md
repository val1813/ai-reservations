# INSPECTOR - NSF_FCS Round2 A

输入文件：`current/A/NSF_FCS_round2_A.md`

未读取 B 文件。

## Q1. 量纲校对

### 1. `lambda_R''(0)=<a_R>_pi+2<g_R,(-L)^-1g_R>_pi`

- 左边 SI 单位：若 `lambda_R(theta)` 是未缩放时间的 SCGF，则 `lambda_R''(0)` 单位为 `s^-1`。
- `<a_R>_pi`：`a_R=c_R^+ + c_R^-`，rate 和，单位 `s^-1`。
- `g_R=b_R-J_R`：signed rate，单位 `s^-1`。
- `(-L)^-1`：generator inverse，单位 `s`。
- `<g_R,(-L)^-1g_R>_pi`：`s^-1 * s * s^-1 = s^-1`。
- 匹配：通过。

### 2. `D_L(f)=<-f,Sf>_pi`

- 若 `f` 取无量纲测试函数，`S f` 单位为 `s^-1`，所以 `D_L(f)` 单位为 `s^-1`。
- 变分项 `2<g_R,f>_pi-D_L(f)` 中 `2<g_R,f>_pi` 单位也是 `s^-1`。
- 匹配：在 `f` 无量纲且 `g_R` 为 rate observable 的约定下通过。

### 3. `sup_f {2 f(1)-E_mu(f,f)-boundary_mass(f)} <= C G_R(L)`

- 左边第一项 `2 f(1)` 若 `f` 无量纲，则无单位；`E_mu(f,f)` 在 conductance/Dirichlet 约定下通常带 rate 或 conductance 单位；右边 `G_R(L)` 是 conductance/rate 标度。
- 匹配：不充分。该连续 trace 公式缺少与边界源强度同量纲的线性泛函，例如 `2 q f(1)`，或需要显式声明 `E_mu` 已归一化为无量纲且 `G_R` 也为无量纲。
- 建议修正：把该式改成尺度判断式，例如
  `sup_f {2 ell_R(f)-E_mu(f,f)-boundary_mass(f)} <= C G_R(L)`,
  并声明 `ell_R` 的单位使线性项与 Dirichlet form 同量纲。

### 超越函数自变量

未发现 `exp()`、`sin()`、`log()`、`sinh()` 等带量纲自变量的关键公式。`log L` 中的 `L` 应理解为无量纲系统尺寸；若写成物理长度，应改为 `log(L/L0)`。

## Q2. 符号/方向校对

### 阻断项：jump-current FCS 的 resolvent 公式符号/算子不成立

A 的 INSPECTOR_CHECK 写为：

`lambda_R''(0)=<a_R>_pi+2<g_R,(-L)^-1g_R>_pi`

并随后多次要求 `<a_R>` 与 resolvent 项发生 `O(1)` cancellation，使 `lambda_R''(0)` 可能降到 `G_R(L)` 标度。

方向检验：

- 在 reversible 或 sector-reduced 的状态型 additive functional 公式中，`<g_R,(-S)^-1g_R>_pi >= 0`。
- 因而若二阶项真是 `+2<g_R,(-L)^-1g_R>` 或被正的 `H_-1` 二次型上界替代，它只能增加 `<a_R>`，不能抵消 `<a_R>` 的 `O(1)` 主部。
- 但 open exclusion 的边界 current variance 已知可低于 endpoint activity 标度，真正的抵消来自 jump-current martingale 与 Poisson corrector 的交叉变差/tilted-generator 一阶算子项，而不是简单的正 `H_-1` 二次型。

结论：`<a_R>` 与 resolvent cancellation 的说法和当前正号二次型公式互相冲突。对 jump current，二阶扰动公式应从 tilted generator 写成

`lambda''(0)=<L_0'' 1>_pi + 2 <L_0' h>_pi`

其中 `L h = -(L_0'1-<L_0'1>)`。这里 `L_0' h` 一般不是乘法内积 `<g_R,h>`。若要得到 cancellation，必须保留 jump increment 对 corrector 的交叉项；不能把它替换为 `+2<g_R,(-L)^-1g_R>`。

判定：阻断。A 的主公式需要重写，否则后续关于 cancellation、`lambda_R''(0) asymp G_R(L)` 的讨论建立在错误/不完整的二阶公式上。

### spectral gap 上界方向

A 写：

`<g_R,(-S)^-1g_R>_pi <= Var_pi(g_R)/gap_L <= C kappa_R^2/gap_L`

方向检验：

- 若 `gap_L` 是 `-S` 在中心化函数空间上的最小正谱值，则 `(-S)^-1 <= gap_L^-1`，所以上界方向正确。
- 代入 `gap_L ~ L^-2`、`(log L)L^-2`、`L^{-(2alpha-1)}` 得到 `O(L^2)`、`O(L^2/log L)`、`O(L^{2alpha-1})` 的粗上界，方向正确。

警告：这里需要的是 gap 的下界 `gap_L >= c * scale(L)` 才能推出严格上界。A 写“预期 gap ~ ...”可以作为启发，但若作为定理需补充引用或证明。

### conductance 方向

A 明确说 `||g_R||_{-1,S,L}^2 <= C G_R(L)` 不是 KV 自动给出，而是额外 fractional trace inequality；该方向是保守的上界方向，没有冒进成定理。通过。

## Q3. 循环论证校对

发现一处潜在循环/偷换：

- A 用 fractional Fick law 的 mean conductance `G_R(L)` 启发 `H_-1` trace bound。
- 随后又把 `||g_R||_{-1}^2=O(G_R(L))` 作为“最小有用目标”，并明确说没有证明。
- 因此正文没有直接循环证明，但若后续把该 trace bound 当成已由 mean conductance 推出，就会循环。

判定：当前文本对该风险有标注，可继续；但必须把 `H_-1 trace bound` 保持为独立待证命题，不能由 Fick law 直接引用。

## Q4. 数量级鸿沟标记

### `G_R(L)` vs spectral-gap 粗上界

对比：

- `alpha>3/2`：`G_R(L)~L^-1`，gap 粗上界给 `O(L^2)`，相差 `L^3`。
- `alpha=3/2`：`G_R(L)~(log L)/L`，gap 粗上界给 `O(L^2/log L)`，相差 `L^3/(log L)^2`。
- `1<alpha<3/2`：`G_R(L)~L^{-(2alpha-2)}`，gap 粗上界给 `O(L^{2alpha-1})`，相差 `L^{4alpha-3}`。

这是多项式级鸿沟，不是 10^N 数值鸿沟，但足以说明 spectral-gap bound 与 conductance 标度相距很远。A 已明确标注“很粗”“远弱于 conductance 标度”，通过。

### `<a_R>` vs `G_R(L)`

`<a_R>_pi=O(1)` 而 `G_R(L)->0`。若声称 `lambda_R''(0)=O(G_R(L))`，需要 `O(1)` cancellation。A 已把这一点列为硬边界，但由于 Q2 的二阶公式写错/不完整，当前 cancellation 讨论不能作为有效推导。

## Q5. 代数验算

### 5a. 变分公式展开

对正自伴算子 `A=-S`：

`sup_f {2<g,f>-<f,A f>} = <g,A^-1 g>`

因为变分一阶条件为 `A f = g`，代回得 `2<g,A^-1g>-<A^-1g,g>=<g,A^-1g>`。

因此 A 的 `H_-1` 变分公式本身在状态型 additive functional / symmetric Dirichlet form 语境下系数正确，没有缺少 `1/2`。

问题不在这个代数恒等式，而在把 reservoir jump current 的 SCGF 二阶项等同于该正二次型。

### 5b. 极限退化

- 自由/无相互作用极限：单个 Poisson 边界活动的 FCS 二阶项应含 activity；若 transport current 被系统约束，低频 variance 可以低于 bare activity，需要 corrector 交叉项。当前正二次型公式不能产生降低。
- 平衡小密度差极限：Einstein relation 预期给出 mobility-conductance 型标度；这同样要求跳跃电流公式中的 martingale-corrector cancellation，而不是正 `H_-1` 加法。

### 5c. 数值量级验算

未提供具体数值参数，无法执行数值代入。可验算的符号量级见 Q4。

### 5d. 数值来源

A 中具体数值主要是文献 DOI、指数标度和 `O(...)` 级别判断。未发现无来源的具体实数常量被用于计算结论。

## Q6. 综合判定

阻断：INSPECTOR 阻断，原因是 jump-current FCS 二阶公式写成了 `+2<g_R,(-L)^-1g_R>` 的正 `H_-1` 二次型；这与后文要求 `<a_R>` 和 resolvent 项发生 `O(1)` cancellation 的结论不相容。修正后需要重新提交。

警告：

1. 连续 trace 变分式 `sup_f {2 f(1)-E_mu(f,f)-boundary_mass(f)} <= C G_R(L)` 量纲未写清，需要把边界线性泛函和归一化显式化。
2. spectral-gap 上界方向正确，但作为严格上界时需要 gap 下界证明/引用，而不仅是“预期 gap ~ ...”。
3. A 对 `<a_R>` 与 resolvent cancellation 的谨慎结论方向是对的，但当前公式无法承载该 cancellation；必须改用 tilted-generator 二阶扰动或 martingale-Poisson decomposition 的完整 jump-current 公式。

最终结论：A Round2 的保守科学判断大体没有冒进，尤其是没有把 `lambda_R''(0) asymp G_R(L)` 升格为定理；但 INSPECTOR_CHECK 的关键公式本身对 reservoir jump current 不合格，属于阻断级问题。
