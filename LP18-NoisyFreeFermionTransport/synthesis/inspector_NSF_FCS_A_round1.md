# INSPECTOR report - NSF_FCS round1 A

检查对象：`current/A/NSF_FCS_round1_A.md`

限制记录：本次只读取 A 文件与 `ai/INSPECTOR.md`；未读取 B 文件。写入范围仅限本文件。

## Q1. 量纲校对

关键公式 1：

`L_s^R=L_bulk+L_L^res+c_R^+(e^s T_L^+-I)+c_R^-(e^{-s} T_L^--I)`

- 左边 SI 单位：`s^-1`，Markov generator。
- 右边 SI 单位：`L_bulk`、`L_L^res`、`c_R^+(...)`、`c_R^-(...)` 均为 `s^-1`。
- 指数自变量：tilt 参数 `s` 是计数场，无量纲；`e^s`、`e^{-s}` 合法。
- 匹配：通过。

关键公式 2：

`lambda_R''(0)=<a_R>_pi+2<(j_R-J_R),phi>_pi`

其中 `j_R=c_R^+-c_R^-`，`a_R=c_R^++c_R^-`，`L phi=-(j_R-J_R)`。

- `lambda_R(s)=lim_{t->infty} t^{-1} log E exp(s Q_R(t))`，因 `s` 与 `Q_R` 均无量纲，`lambda_R''(0)` 单位为 `s^-1`。
- `<a_R>_pi` 单位：`s^-1`。
- `j_R-J_R` 单位：`s^-1`。
- `L phi=-(j_R-J_R)` 中 `L` 单位为 `s^-1`，所以 `phi` 为无量纲。
- `2<(j_R-J_R),phi>_pi` 单位：`s^-1`。
- 匹配：通过。

关键公式 3：

`lambda_R''(0)=<a_R>_pi+2 integral_0^infty <(j_R(eta_0)-J_R)(j_R(eta_t)-J_R)>_pi dt`

- 相关函数 integrand 单位：`s^-2`。
- `dt` 单位：`s`。
- 积分项单位：`s^-1`。
- 与 `<a_R>_pi` 和 `lambda_R''(0)` 匹配：通过。

关键公式 4：

`r(r)=2 J0^2/(gamma_phi |r|^{2 alpha})`

- 若 `J0` 与 `gamma_phi` 均按物理速率/能量频率单位处理，则 `J0^2/gamma_phi` 为速率，`|r|` 为无量纲格点距离，故 `r(r)` 为跳跃率 `s^-1`。
- `mu=2 alpha - 1` 是尾指数匹配关系，无量纲。
- 匹配：通过。

结论：未发现量纲错误。

## Q2. 符号/方向校对

tilted generator 符号：

- A 定义 `Q_R(t)=N_R^+(t)-N_R^-(t)`，右 reservoir 向系统注入记正，系统向右 reservoir 抽出记负。
- 因此注入事件乘 `e^s`，抽出事件乘 `e^{-s}`。
- A 的 `c_R^+(e^s T_L^+-I)+c_R^-(e^{-s} T_L^--I)` 与该符号约定一致。
- 未把 bulk long jump 跨 cut 事件计入 `Q_R`，与“reservoir-current 而非 cut-current”的定义一致。

Poisson 方程方向：

- 令 `g=j_R-J_R`。
- 对 observables 的 Markov generator `L`，标准 resolvent 写法为 `phi=integral_0^infty P_t g dt`，满足 `L phi=-g`。
- A 写作 `L phi=-(j_R-J_R)`，方向正确。
- 因此 `lambda_R''(0)=<a_R>+2<g,phi>` 的正号与 `phi=(-L)^{-1}g` 的约定一致。

极限检查：

- 若右 reservoir 注入占优，`c_R^+>c_R^-`，则 `J_R>0`，`lambda_R'(0)=J_R` 为正，符合注入为正。
- 若只允许右抽出而无注入，`c_R^+=0`，则 `j_R=-c_R^-`，`J_R<0`，tilt 权重为 `e^{-s}`，`lambda_R'(0)<0`，方向一致。

结论：未发现 tilted generator 符号或 Poisson 方程方向错误。

## Q3. 循环论证校对

检查项：从 `lambda_R''(0)` 推到 `G_R(L)` 同标度。

- A 明确说 tilted generator 与 Poisson/Green-Kubo 只给出可计算公式。
- A 明确说缺口在 resolvent / spectral gap / boundary observable 范数估计。
- A 未把 `lambda_R''(0) asymp G_R(L)` 写成已证定理，而写成“小密度差、局部平衡、mobility 非奇异、boundary observable 不引入额外标度”等附加假设下的强推断。

结论：未发现把输入假设当作验证结论的循环论证。A 对同标度缺口的标注是合格的。

## Q4. 数量级鸿沟标记

三段候选标度：

- `alpha>3/2`：`G_R(L) ~ L^-1`；A 将 `lambda_R''(0) ~ L^-1` 标为强推断/尚非已证。
- `alpha=3/2`：`G_R(L) ~ (log L)/L`；A 将 `lambda_R''(0)` 标为待验证，并强调 log 最脆弱。
- `1<alpha<3/2`：`G_R(L) ~ L^{-(2alpha-2)}`；A 将 `lambda_R''(0)` 标为强推断/主候选/非已证。

检查结果：

- 没有出现 `10^N` vs `10^M` 的具体数值跨越估算，因此无可执行的数量级差异报警。
- 关键标度跃迁均被明确放在假设或待验证层级，没有被误标为已证结论。

结论：无阻断；同标度假设的显式标注通过。

## Q5. 代数验算

tilt 扰动展开：

- `L_s^R` 对常数函数的一级导数给出 `L'_0 1=c_R^+-c_R^-=j_R`。
- 二级导数给出 `L''_0 1=c_R^++c_R^-=a_R`。
- 因而 `lambda_R'(0)=<j_R>_pi=J_R`，`lambda_R''(0)` 的瞬时活动项为 `<a_R>_pi`。

Poisson/resolvent：

- `g=j_R-J_R`。
- `L phi=-g` 且 `<phi>_pi=0` 固定常数自由度。
- `phi=(-L)^{-1}g`，所以 `2<g,phi>` 与 Green-Kubo 积分项 `2 integral_0^infty <g(eta_0)g(eta_t)> dt` 同向。
- 非可逆 NESS 下 A 已提醒不能简单改写成平衡自伴随 Dirichlet form；这是正确限制。

long-jump 指数：

- `r(r) ~ |r|^{-2alpha}` 与 classical long-jump kernel `p(r) ~ |r|^{-(1+mu)}` 比较，得 `1+mu=2alpha`，即 `mu=2alpha-1`。
- 总跳率 `sum_r r(r)` 收敛条件为 `2alpha>1`；A 采用更强的 `alpha>1`，对应 `mu>1`，用于有限平均跨越尺度/文献 fractional Fick 区间，未构成代数错误。
- 二阶矩 `sum_r r^2 r(r) ~ sum_r r^{2-2alpha}`，收敛条件为 `2-2alpha<-1`，即 `alpha>3/2`。
- 临界 `alpha=3/2` 时 `sum_{r<=L} r^{-1} ~ log L`，A 的 log 判定正确。
- `1<alpha<3/2` 时 `mu-1=2alpha-2`，A 的 `L^{-(2alpha-2)}` 与 fractional Fick 候选标度一致。

结论：未发现代数展开、指数或临界条件错误。

## Q6. 综合判定

结论：`INSPECTOR 通过，可继续，但保留一条非阻断警告。`

非阻断警告：

- `lambda_R''(0) asymp G_R(L)` 仍依赖未证明的 resolvent / Green-Kubo 同标度控制，尤其是 endpoint-only reservoir 与 exterior/infinite reservoir 边界实现的等价性，以及 `alpha=3/2` 的 log 因子。
- A 已将此点正确标为假设、强推断或待验证，而非已证定理。因此该警告不阻断后续推进，但后续文本必须继续保留“未证同标度假设”的标签。

阻断错误：无。

