# INSPECTOR NSF-FCS-1 Round 4: B

输入：
- `current/B/NSF_FCS_round4_B.md`
- `synthesis/PI_NSF_FCS_round3_synthesis.md`
- 为核对 alpha 记号，另读 `current/A/NSF_FCS_round4_A.md`

校对范围：只做量纲、符号/方向、循环论证、数量级、代数/极限校对。

## Q1. 量纲校对

### generator / stationary

- `k_F(x,y)`：单位 `time^-1`。
- `L_F[x,y]=k_F(x,y)`、`L_F[x,x]=-sum_y k_F(x,y)`：单位 `time^-1`。
- `(L_F f)(x)=sum_y k_F(x,y)[f(y)-f(x)]`：若 `f` 为无量纲，左边单位 `time^-1`。
- `pi_F L_F=0`：`pi_F` 无量纲，右边单位 `time^-1`，作为零向量成立。

量纲匹配。

### Poisson

- `b(x)=sum_y k_0(x,y) g_R(x,y)`：`count/time`。
- `J=<b>_pi`：`count/time`。
- `h=b-J`：`count/time`。
- `-L_0 phi=h`：`L_0` 为 `time^-1`，故 `phi` 单位 `count`。
- `a(x)=sum_y k_0(x,y) g_R(x,y)^2`：`count^2/time`。
- `2<h,phi>=2 sum_x pi_x h_x phi_x`：`count^2/time`。

量纲匹配。

### tilted curvature

- `chi` 无量纲，`exp(chi g_R)` 的自变量无量纲。
- `L_chi` 单位 `time^-1`，主特征值 `lambda_R(chi)` 单位 `time^-1`。
- `[lambda(eps)-2lambda(0)+lambda(-eps)]/eps^2`：`eps` 无量纲，故单位仍为 `time^-1 = count^2/time`，其中 count 为计数约定下的无量纲单位。

量纲匹配。

### conductance and S

- `F_R=beta(mu_R-mu_ref)` 无量纲。
- `J_R(F_R)` 单位 `count/time`。
- `G_R=dJ_R/dF_R|_0` 单位 `count/time`。
- `S_R=lambda_tilt_second/G_R` 单位为 `count`，若 count 按计数 convention 视为无量纲，则 `S_R` 可作为无量纲诊断比值。

量纲匹配，但见 Q2 阻断项：在 B 给定的闭合可逆有限链中，`G_R` 实际退化为 0。

### reservoir tail

B 写

`sum_{z=L+1}^{L+M_tail} c_R |z-x|^(-1-alpha) + c_R (L+M_tail+1-x)^(-alpha)/alpha`.

若 `c_R` 单位为 `time^-1`，距离无量纲，则 `r_R(x)` 单位 `time^-1`。Euler tail 积分

`int_N^infty u^(-1-alpha) du = N^(-alpha)/alpha`

代数正确，要求 `alpha>0`。左库 tail 的 `x+M_tail` 与更自然的 `x+M_tail+1` 有一个格点偏移，不是量纲错误，只是有限 `M_tail` 近似 convention 需在实现中固定。

## Q2. 符号/方向校对

### 阻断：B 的 `G_R>0` 与给定 generator 不自洽

B 的模型在 `F_R` 下仅修改右 reservoir 与 bulk 的双向边：

- `k_F(R,x)=k_0(R,x) exp(+F_R/2)`
- `k_F(x,R)=k_0(x,R) exp(-F_R/2)`
- 其他边不变

同时 `k_0` 是对称 rates，状态空间包含有限 reservoir node `R`、左 node `0` 和 bulk。此时对任意 `F_R`，链仍满足 detailed balance。取非右库状态权重为常数 `c`，右库权重为 `c exp(-F_R)`，则对每条右库边

`pi_F(R) k_F(R,x) = c exp(-F_R) k_0(R,x) exp(F_R/2) = c k_0(R,x) exp(-F_R/2)`

而

`pi_F(x) k_F(x,R) = c k_0(x,R) exp(-F_R/2)`.

由于 `k_0(R,x)=k_0(x,R)`，每条右库边的净流为零。因此

`J_R(F_R)=sum_x pi_F(x) b_F(x)=0` 对所有 `F_R` 成立，

从而

`G_R=dJ_R/dF_R|_0=0`,

不是 B 文中要求的正数。这个问题不是数值精度或符号正负问题，而是 affinity 只形成了对 `R` 节点的纯势变换，没有形成非平衡环流或 transport current。

同一结构还导致右库交换计数为 coboundary。取 `psi(R)=1`、`psi(x)=0` for `x!=R`，则

- `R -> x`: `g_R=+1=psi(R)-psi(x)`
- `x -> R`: `g_R=-1=psi(x)-psi(R)`

所以累计计数 `Q_t=psi(X_0)-psi(X_t)` 有界，长期 SCGF 二阶曲率为

`lambda_R''(0)=lim_{t->infty} t^-1 Var(Q_t)=0`.

这与 A Round 4 的 bare right-reservoir exchange coboundary 结论一致。B 的 `lambda_tilt_second/G_R` 在该 generator 下成为 `0/0` 或质量门失败，无法进入 keep/kill。

建议修正方向：若要得到非零 conductance，需要把 observable 改成真正 transported current，或显式加入左/远端 sink-source 边界并用跨系统 current 定义 `G_R`；不能用当前闭合有限链的 bare `R <-> bulk` 净交换 current 作为正 conductance。

## Q3. 循环论证校对

B 对 `C_from_tilted_residual` 与 `err_balance` 的主要区分是正确的：

- residual 模式下 `two_C_residual=lambda_tilt_second-a_mean-corrector` 只是定义；
- `err_balance_residual=by_construction`；
- `decision_uses_C=false`；
- 明确禁止把 `lambda_tilt_second=a_mean+corrector+two_C_residual` 当独立验证。

未发现 residual balance 的循环验证。

警告：B 同时写 `decision_uses_C=diagnostic_only`，但 KILL-5 又允许用 `two_C_explicit/lambda_tilt_second` 的跨 reservoir 非普适性触发 kill。这不构成 residual 循环，因为 `C_explicit` 被假设为第三个独立公式；但它和“scientific decision 只依赖稳定的 `lambda_tilt_second` 与独立校准的 `G_R`”这一原则不完全一致。若保留 KILL-5，应把它标为 explicit-C-only 的附加故障判据，而不是说全部 keep/kill 只依赖 `S_R`。

## Q4. 数量级与 alpha 记号校对

### `1+alpha` vs A/PI 的 `alpha`

A/PI 的有效 right-reservoir tail 写作

`r_R(x)=kappa d_R(x)^(-alpha)`.

B 从半无限外部 sites 的 kernel

`|z-x|^(-1-alpha)`

求和到右侧 reservoir，得到有效

`r_R(x) ~ const * d_R(x)^(-alpha)`.

因此 B 的 `1+alpha` 是外部 long-jump kernel exponent，积分后有效 reservoir rate exponent 与 A/PI 的 `alpha` 一致。这里没有代数错误。

需要警告的是记号层级：B 的 `ReservoirSpec.alpha` 同时用于 bulk kernel `|i-j|^(-1-alpha)` 和 reservoir 外部 kernel `|z-x|^(-1-alpha)`，而 A 直接把有效 contact rate 写成 `d^(-alpha)`。实现台账必须明确输出的是 effective tail exponent `r_R(d)~d^(-alpha)`，避免后续把 reservoir rate 误写成 `d^(-1-alpha)`，否则 `A_R(L)=sum_d r_R(d)` 的数量级会错一阶：

- 正确有效 tail：`sum_d d^(-alpha)`；
- 错误误读 tail：`sum_d d^(-1-alpha)=O(1)` 对所有 `alpha>0`，会遮蔽 `alpha<=1` 的增长情形。

## Q5. 代数/极限校对

### stationary solve

用 `L0.T pi_col=0` 加 `sum pi=1` 求 row stationary `pi L0=0`，代数 convention 一致。

### Poisson augmented system

`[-L0, 1; pi, 0] [phi, c]^T = [h,0]^T` 对应 `-L0 phi + c 1=h` 与 `<phi>_pi=0`。因 `h=b-J` 满足 `<h>_pi=0`，可解时 `c` 应为 0。代数 convention 一致。

### tilted second difference

二阶中心差分公式量纲正确，`eps_grid` 为无量纲 `chi` 步长。要求 `lambda(0)` 接近 0 并检查 imaginary part、plateau/Richardson，是合理的数值门。

但在当前 bare right-exchange observable 下，`lambda(chi)` 应因 coboundary 与 `lambda(0)` 同谱主值，主曲率退化为 0。若实现得到非零 `lambda_tilt_second`，应优先检查 `g_R` 符号、tilted diagonal 是否错误改动、或是否隐含加入了 transport sink/source。

### conductance central difference

`[J(+delta_F)-J(-delta_F)]/(2 delta_F)` 的量纲正确。但对 B 当前 rates，极限应为 0。质量门中 `G_R/sigma_G>=5` 与 `G_R>0` 会把所有行判为 `G_uncontrolled` 或 `sign_failed/invalid`，因此不会产生可用 ledger。

### keep/kill criteria

B 明确规定只有 `ledger_valid==true` 后才执行 keep/kill，且 `ledger_valid` 只接受至少两个 `tail`、`l_prefactor=="none"`、每个至少 5 个 valid rows 的台账。这个门控方向正确。

不过由于 Q2 的退化，当前 generator 下 `G_R=0`，`S_R=NA`，所以 `ledger_valid` 实际无法成立。任何 KEEP/KILL 若在这个模型上输出，都是由不合格台账推出。

## 综合判定

**INSPECTOR 阻断。**

阻断原因：B 的 generator/stationary/affinity/current conventions 在量纲上匹配，但方向上不自洽。给定有限闭合可逆链和 bare right-reservoir exchange current，`F_R` 只产生 detailed-balance 权重重标定，不产生 steady current；`J_R(F_R)=0`、`G_R=0`。同一计数也是 occupation coboundary，故 `lambda_R''(0)=0`。因此 `S_R=lambda_tilt_second/G_R` 无定义，台账质量门无法通过，后续 keep/kill 判据不能使用。

附带警告：

1. `1+alpha` 本身不是错误；它积分后给出 A/PI 的有效 `r_R(d)~d^(-alpha)`。但实现必须显式区分 external kernel exponent `1+alpha` 与 effective reservoir tail exponent `alpha`。
2. residual `C` 与 `err_balance` 的循环问题已经基本避免；但 KILL-5 使用 `C_explicit` 作 kill 判据，与“决策只依赖 `lambda_tilt_second/G_R`”的表述有轻微冲突，应改成明确的 explicit-C 附加故障判据。
3. 若要继续 B 的 ledger 路线，需先改定义为真正 transport current 或加入远端 sink/source 后重新定义 `G_R` 与 tilted observable；否则当前 bare exchange ledger 只能给 `INVALID_LEDGER`，不能给科学 KEEP/KILL。
