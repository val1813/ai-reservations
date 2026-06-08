# B博士 NSF-FCS-1 Round 4 修正版

## 0. 阻断后的框架声明

INSPECTOR_B_round4 的阻断是正确的。上一版把右 reservoir 写成有限闭合可逆链中的一个节点，并把 `R <-> bulk` 的 bare exchange 当作 current。这个 observable 是 occupation coboundary：累计计数只等于端点 occupation 差，长期 SCGF 曲率为 0；右 affinity 也只是对 `R` 节点的纯势重标定，不能产生稳态 transport current。因此上一版的 `G_R=0`、`lambda_R''=0`、`S_R=0/0`，不能进入 keep/kill。

本轮修正为真正的 transport ledger：

`排队网络 source-sink -> open single-particle transport -> two-terminal FCS ledger`

借来的结构是 Jackson/open queue 的吞吐量，而不是闭合链里的节点交换。最小模型必须含：

- 一个 empty state `e`；
- 一个 bulk occupied state `x in {1,...,L}`；
- 右端 reservoir/source 对 `e -> x` 注入；
- 左端 reservoir/sink 对 `x -> e` 抽取；
- 计数 current 是穿越到左端的 transport current，或等价的 two-terminal net current；
- `G_R` 必须是右 affinity 或 two-terminal affinity 对 transport current 的响应。

如果脚本只能检测 bare `R <-> bulk` exchange，则必须输出：

`verdict = INVALID_BARE_EXCHANGE_NOT_TRANSPORT`

并且 `S_R=NA`，不得输出 scientific KEEP/KILL。

---

## 1. Transport ledger 的最小矩阵模型

### 1.1 状态空间

取单粒子 open sector：

`Omega_L={e,1,2,...,L}`

其中：

- `e`: empty state，系统中没有粒子；
- `1,...,L`: 单粒子位于 bulk site `x`。

这不是闭合 reservoir-node random walk。Reservoir 不作为可逆节点进入状态空间，而是作为 open Markov jump 的 source/sink rates 进入 generator。

矩阵 convention 仍固定为 row-generator acting on column observables:

`(L_F f)(u)=sum_v k_F(u,v)[f(v)-f(u)]`

即：

- `L_F[u,v]=k_F(u,v)` for `u != v`;
- `L_F[u,u]=-sum_{v != u} k_F(u,v)`;
- stationary distribution 是 row vector `pi_F L_F=0`。

### 1.2 Bulk long jumps

对 occupied states `x,y in {1,...,L}`, `x != y`:

`k_0(x,y)=c_bulk / |x-y|^(1+alpha_kernel)`.

这里 `alpha_kernel` 是外部 long-jump kernel 的指数减 1。与 PI/A 常用的 effective reservoir tail 指数关系为：

`r_nu(d) ~ d^(-alpha_tail)`, `alpha_tail = alpha_kernel`

因为

`sum_{z outside} |z-x|^(-1-alpha_kernel) ~ d^(-alpha_kernel) / alpha_kernel`.

脚本台账必须同时输出：

`alpha_kernel`, `alpha_tail_effective`

避免把 effective tail 错写成 `d^(-1-alpha)`。

### 1.3 Left/right reservoir coupling

定义 effective reservoir tails：

`r_R(x;L)=sum_{z=L+1}^{L+M_tail} c_R |z-x|^(-1-alpha_kernel) + c_R (L+M_tail+1-x)^(-alpha_kernel)/alpha_kernel`

`r_L(x;L)=sum_{z=-M_tail}^{0} c_L |x-z|^(-1-alpha_kernel) + c_L (x+M_tail+1)^(-alpha_kernel)/alpha_kernel`

`r_R(x)` 和 `r_L(x)` 的单位都是 `1/time`。

Reservoir rates 采用 chemical-affinity 参数化。令 two-terminal affinity 为

`F = eta_R - eta_L`

默认 symmetric gauge:

`eta_R=+F/2`, `eta_L=-F/2`.

对每个 reservoir `nu in {L,R}`：

`k_F(e,x;nu)=rho0 * r_nu(x) * exp(+eta_nu/2)`  注入；

`k_F(x,e;nu)=(1-rho0) * r_nu(x) * exp(-eta_nu/2)`  抽取。

默认 `rho0=1/2`。若需要只施加右 affinity，可固定 `eta_L=0`, `eta_R=F_R`，但台账必须写明 `affinity_mode=right_only_transport`。推荐使用 `affinity_mode=two_terminal_symmetric`。

总 rate 是 reservoir 分量求和：

`k_F(e,x)=k_F(e,x;L)+k_F(e,x;R)`

`k_F(x,e)=k_F(x,e;L)+k_F(x,e;R)`

bulk jumps `x -> y` 不随 `F` 变。

### 1.4 Transport current，不再是 bare exchange

本轮计数 transport current 为左端净输出：

`g_T(x,e;L)=+1`  左端抽取，粒子从系统进入左 reservoir；

`g_T(e,x;L)=-1`  左端注入，粒子从左 reservoir 进入系统；

所有 right reservoir jumps 和 bulk jumps 上 `g_T=0`。

对应 drift:

`b_T(u)=sum_v k_0(u,v) g_T(u,v)`.

在 `F=0` 且左右 reservoir 相同基准下，`J_T=<b_T>_pi=0`。当 `F>0` 表示右端 chemical potential 高于左端时，应有 `J_T(F)>0`。因此：

`G_R := G_T = dJ_T/dF |_{F=0}`

单位 `count/time`。若使用 `right_only_transport` gauge，则：

`G_R=dJ_T/dF_R|_{F_R=0, eta_L=0}`。

`G_R` 的响应对象始终是 transport current `J_T`，不是 bare right exchange current。

### 1.5 Coboundary 检测

脚本必须包含 observable coboundary test。给定 directed-edge increment `g(u,v)`，检查是否存在 potential `psi` 使：

`g(u,v)=psi(v)-psi(u)` for every edge with `k_0(u,v)>0`.

可执行做法：固定 `psi(e)=0`，对所有边建立线性方程，最小二乘残差若

`coboundary_resid <= 1e-12`

则标记：

`observable_status=coboundary`

并强制：

`lambda_tilt_second=0`, `G_R=0`, `S_R=NA`, `verdict=INVALID_COBOUNDARY_OBSERVABLE`.

对 transport `g_T`，由于 right reservoir transitions `e <-> x` 存在但 `g_T=0`，而 left transitions 同一对状态有 `g_T=+-1`，不存在单一 `psi` 同时满足左右通道，因此不是 coboundary。实现时必须保留 channel label `(nu=L/R)`，不能把 left/right 的 `e <-> x` 合并后再丢失计数字段。

---

## 2. 脚本结构规范

建议脚本名：

`scripts/nsf_fcs_transport_ledger.py`

最小 API：

```python
@dataclass
class TransportSpec:
    reservoir_id: str
    alpha_kernel: float
    c_bulk: float = 1.0
    c_left: float = 1.0
    c_right: float = 1.0
    rho0: float = 0.5
    m_tail: int = 20000
    reservoir_kind: str = "tail"
    affinity_mode: str = "two_terminal_symmetric"
    observable_kind: str = "left_transport_current"

@dataclass
class Edge:
    src: int
    dst: int
    channel: str     # "bulk", "left_reservoir", "right_reservoir"
    rate: float
    g_transport: float

def build_edges(L: int, spec: TransportSpec, F: float = 0.0) -> list[Edge]:
    """Build channel-resolved rates. Do not merge L/R reservoir edges before computing g."""

def generator_from_edges(n: int, edges: list[Edge]) -> np.ndarray:
    """Sum rates into L[u,v]; diagonal is minus total escape rate."""

def stationary(Lmat: np.ndarray) -> tuple[np.ndarray, dict]:
    """Solve pi L=0, sum pi=1."""

def additive_fields(edges: list[Edge], pi: np.ndarray) -> dict:
    """Return b_T, a_T, J_T, h_T using channel-resolved g_transport."""

def solve_poisson(L0: np.ndarray, pi: np.ndarray, h: np.ndarray) -> tuple[np.ndarray, dict]:
    """Solve -L0 phi=h, <phi>_pi=0."""

def tilted_generator_from_edges(n: int, edges0: list[Edge], chi: float) -> np.ndarray:
    """Off-diagonal rate * exp(chi*g_transport); diagonal unchanged escape rate."""

def lambda_tilt_second(edges0, eps_grid) -> tuple[float, dict]:
    """Principal-eigenvalue curvature for transport current."""

def transport_conductance(L: int, spec: TransportSpec, delta_grid) -> tuple[float, dict]:
    """Central difference of J_T(F), not bare exchange."""

def coboundary_test(edges0: list[Edge], n: int) -> dict:
    """Return residual for g_transport=psi(dst)-psi(src)."""

def explicit_cross_term_or_none(edges0, pi, phi) -> tuple[float | None, dict]:
    """Optional independent 2*C_explicit; not required for decision."""

def ledger_row(L: int, spec: TransportSpec) -> dict:
    """Build one row and propagate invalid/coboundary statuses."""

def decide(rows: list[dict]) -> dict:
    """Quality gate, then KEEP/KILL using only stable lambda_tilt_second/G_R."""
```

### 2.1 Stationary solve

Use `L0.T pi_col=0`, replace one equation by `sum pi=1`。Accept only if:

`||pi L0||_1 <= 1e-10 max(1,||L0||_1)`

`|sum pi - 1| <= 1e-12`

`min_x pi_x >= -1e-12`.

### 2.2 Transport fields

At `F=0`:

`b_T(u)=sum_edges_from_u rate(edge) * g_transport(edge)`

`a_T(u)=sum_edges_from_u rate(edge) * g_transport(edge)^2`

`J_T=<b_T>_pi`

`h_T=b_T-J_T`.

At symmetric equilibrium `J_T` should be numerically zero:

`|J_T(0)| <= 1e-10 max(1,<a_T>)`.

If not, mark `equilibrium_current_failed`。

### 2.3 Poisson corrector

Solve:

`-L_0 phi=h_T`, `<phi>_pi=0`.

Report:

`a_mean=<a_T>`

`corrector_2hphi=2 sum_u pi_u h_T(u) phi(u)`.

Accept:

`||-L0 phi-h_T||_{pi,2} <= 1e-9 max(1,||h_T||_{pi,2})`

`|<phi>_pi| <= 1e-10 max(1,||phi||_{pi,2})`.

### 2.4 Tilted generator for transport current

Use channel-resolved transport increments:

`L_chi[u,v] += rate(edge u->v) exp(chi g_transport(edge))`

for off-diagonal entries; diagonal remains:

`L_chi[u,u] = -sum_edges_from_u rate(edge)`.

`lambda_T(chi)` is the principal eigenvalue. Compute:

`lambda_tilt_second(eps)=[lambda(eps)-2lambda(0)+lambda(-eps)]/eps^2`.

Default:

`eps_grid={1e-2,5e-3,2.5e-3,1.25e-3}`.

Accept if:

`rel_spread(lambda_tilt_second(eps)) <= 3%`

and imaginary parts are below numerical tolerance.

### 2.5 Independent transport conductance

For `delta_F in {1e-2,5e-3,2.5e-3}`:

`G(delta_F)=[J_T(+delta_F)-J_T(-delta_F)]/(2 delta_F)`.

Use quadratic extrapolation in `delta_F^2`。Accept:

`rel_spread(G(delta_F)) <= 2%`

`G_R > 0`

`G_R/sigma_G >= 5`.

If the implementation instead computes:

`J_bare_R=sum_x pi(R)k(R,x)-pi(x)k(x,R)`

or any closed-node `R <-> bulk` exchange, mark:

`status=bare_exchange_not_transport`

and force:

`S_R=NA`, `verdict=INVALID_BARE_EXCHANGE_NOT_TRANSPORT`.

---

## 3. C_explicit 与 C_from_tilted_residual

本轮保留 Round 3 的区分，但决策只看 `lambda_tilt_second/G_R`。`C` 只用于诊断 decomposition 缺口。

每行字段：

```text
two_C_explicit
two_C_residual
C_status
err_balance_explicit
err_balance_residual
decision_uses_C
```

规则：

1. 无独立 cross-term 公式：
   - `two_C_explicit=NA`
   - `two_C_residual=lambda_tilt_second-a_mean-corrector_2hphi`
   - `C_status=C_from_tilted_residual`
   - `err_balance_residual=by_construction`
   - `decision_uses_C=false`

2. 有独立 cross-term 公式：
   - compute `lambda_decomp=a_mean+corrector_2hphi+two_C_explicit`
   - compute `err_balance_explicit=|lambda_decomp-lambda_tilt_second|/max(1,|lambda_tilt_second|)`

   若通过 `3%`：
   - `C_status=C_explicit`
   - `decision_uses_C=false`
   - `C_diagnostic=explicit_formula_consistent`

   若不通过：
   - `C_status=C_explicit_failed_use_residual`
   - `two_C_residual=lambda_tilt_second-a_mean-corrector_2hphi`
   - `decision_uses_C=false`
   - `C_diagnostic=explicit_formula_failed`

修正上一版冲突：不再设置 KILL-5。`C_explicit` 的跨 reservoir 非普适性只能输出 diagnostic warning，不能覆盖基于 `S_R=lambda_tilt_second/G_R` 的 scientific KEEP/KILL。若 PI 想让 explicit `C` 进入决策，必须另立一个非 `lambda/G` 命题。

---

## 4. 台账输出格式

每行必须包含：

```text
L
reservoir_id
alpha_kernel
alpha_tail_effective
reservoir_kind
affinity_mode
observable_kind
n_state
n_edges
coboundary_resid
observable_status
pi_resid
equilibrium_J_T
phi_resid
phi_gauge
a_mean
corrector_2hphi
two_C_explicit
two_C_residual
C_status
C_diagnostic
lambda_tilt_second
lambda_tilt_rel_spread
G_R
G_rel_spread
S_R
err_balance_explicit
err_balance_residual
status
verdict_hint
```

Compatibility convention:

`G_R` in this table means `G_transport=dJ_T/dF|0`，not bare right exchange conductance。

`S_R=lambda_tilt_second/G_R` only if:

- `observable_status=transport_non_coboundary`;
- `status=ok`;
- `G_R>0`;
- `lambda_tilt_second` stable.

Otherwise:

`S_R=NA`.

推荐最小扫描：

```text
L_grid = [16, 24, 32, 48, 64, 96]
transport_specs = [
  tail_alpha_0p5_two_terminal,
  tail_alpha_1p0_two_terminal,
  tail_alpha_1p5_two_terminal
]
```

少于两个 valid tail transport specs 只能输出 `INVALID_LEDGER`，不能输出 scientific KEEP。

--- INSPECTOR_CHECK ---
[公式] `Omega_L={e,1,...,L}`；`k_F(e,x;nu)=rho0 r_nu(x) exp(+eta_nu/2)`；`k_F(x,e;nu)=(1-rho0) r_nu(x) exp(-eta_nu/2)`；`F=eta_R-eta_L`；`g_T(x,e;L)=+1`, `g_T(e,x;L)=-1`, right/bulk increments 0；`J_T=<sum k g_T>_pi`；`G_R=dJ_T/dF|0`；`-L0 phi=h_T`；`lambda_T''=[lambda(eps)-2lambda(0)+lambda(-eps)]/eps^2`；`S_R=lambda_T''/G_R`。
[方向] `G_R` 是 two-terminal/right-affinity 对左端 transport current 的响应；不再是闭合有限链中 bare `R<->bulk` exchange。Bare exchange 若为 coboundary，强制 `S_R=NA` 与 `INVALID_BARE_EXCHANGE_NOT_TRANSPORT`。
[数据] 输入为 channel-resolved edges，必须保留 `left_reservoir/right_reservoir/bulk` channel label；否则 left/right 的 `e<->x` 边合并后会误判 current。
[假设] finite open Markov chain irreducible；`F=0` 左右 reservoir 基准相同，`J_T(0)=0`；count convention 下 `S_R` 可作为无量纲诊断比值，否则单位为 count。
---

## 5. 可执行质量门

单行有效条件：

```python
row_valid = (
    status == "ok"
    and observable_kind in {"left_transport_current", "two_terminal_transport_current"}
    and observable_status == "transport_non_coboundary"
    and coboundary_resid > 1e-8
    and abs(equilibrium_J_T) <= 1e-10 * max(1.0, a_mean)
    and pi_resid <= 1e-10
    and phi_resid <= 1e-9
    and phi_gauge <= 1e-10
    and lambda_tilt_rel_spread <= 0.03
    and G_rel_spread <= 0.02
    and G_R > 0
    and G_R / sigma_G >= 5
    and lambda_tilt_second >= -tol_abs
)
```

Bare exchange hard gate:

```python
if observable_kind == "bare_right_exchange" or observable_status == "coboundary":
    return {
        "quality": "INVALID_LEDGER",
        "verdict": "INVALID_BARE_EXCHANGE_NOT_TRANSPORT",
        "S_R": None,
    }
```

Ledger 有效：

```python
valid_specs = [
    spec for spec in transport_specs
    if spec.reservoir_kind == "tail"
    and number_of_valid_rows(spec) >= 5
]
ledger_valid = len(valid_specs) >= 2
```

若 `ledger_valid == false`：

`verdict=NO_SCIENTIFIC_DECISION_INVALID_LEDGER`.

---

## 6. 二值 keep/kill 判据

以下 scientific decision 只在 `ledger_valid==true` 后执行，并且只依赖：

`S_R(L)=lambda_tilt_second(L)/G_R(L)`.

不再含 KILL-5。

### 6.1 拟合对象

对每个 valid tail transport spec `r`：

`S_r(L)=lambda_tilt_second(L,r)/G_R(L,r)`.

拟合三类模型：

1. 常数修正：

`S_r(L)=S_inf_r + A_r L^(-p_r)`, `p_r in [0.25,3]`.

2. 幂漂移：

`log S_r = q_r log L + c_r`.

3. 对数漂移：

`S_r = A_r + B_r log L`.

无 bootstrap 时取保守误差：

`sigma_S/S = sqrt(0.03^2 + 0.02^2)`.

### 6.2 KILL 条件

任一成立：

`verdict=KILL_NSF_FCS_1_TRANSPORT_LEDGER`.

KILL-1: 两个 tail transport specs 的 `S_inf` 分裂：

`|S_inf_r-S_inf_s| > 3 sqrt(sigma_r^2+sigma_s^2)`.

KILL-2: 任一 spec 有稳定幂漂移：

`|q_r| > 0.1` and `|q_r|/sigma_q > 3`.

KILL-3: 任一 spec 有稳定对数漂移：

`|B_r|/sigma_B > 3` 且对数模型优于常数修正模型。

KILL-4: `G_R(L)` 同标度而 `lambda_tilt_second(L)` 标度分裂：

`|slope_logG_r-slope_logG_s| <= 0.1`

and

`|slope_loglambda_r-slope_loglambda_s| > 0.1`

with `3 sigma` significance.

### 6.3 KEEP 条件

若没有任何 KILL 条件成立，并且所有 valid specs 满足：

- `S_inf` 有限正；
- `S_inf` 跨 specs 在 `3 sigma` 内一致；
- 无显著幂漂移；
- 无显著对数漂移；
- `G_R` 不是 near-zero 除法造成的假稳定；

则：

`verdict=KEEP_NSF_FCS_1_FOR_NEXT_STAGE`.

KEEP 仍不是定理证明，只表示最小 two-terminal transport ledger 没有 falsify NSF-FCS-1。

### 6.4 决策伪代码

```python
def decide(rows):
    invalid_bare = any(
        r["observable_kind"] == "bare_right_exchange"
        or r["observable_status"] == "coboundary"
        for r in rows
    )
    if invalid_bare:
        return {
            "quality": "INVALID_LEDGER",
            "verdict": "INVALID_BARE_EXCHANGE_NOT_TRANSPORT",
            "reason": "current is coboundary or not a transport observable",
        }

    valid = quality_gate(rows)
    if not valid.ledger_valid:
        return {
            "quality": "INVALID_LEDGER",
            "verdict": "NO_SCIENTIFIC_DECISION_INVALID_LEDGER",
        }

    fits = fit_S_scaling(valid.rows)
    kill_reasons = []

    if cross_reservoir_Sinf_split(fits, sigma=3):
        kill_reasons.append("KILL-1: S_inf split")
    if any_power_drift(fits, q_threshold=0.1, sigma=3):
        kill_reasons.append("KILL-2: power drift in S_R")
    if any_log_drift(fits, sigma=3):
        kill_reasons.append("KILL-3: log drift in S_R")
    if same_G_scaling_but_lambda_split(fits, slope_tol=0.1, sigma=3):
        kill_reasons.append("KILL-4: G and lambda scaling mismatch")

    c_warnings = explicit_C_diagnostics(valid.rows)

    if kill_reasons:
        return {
            "quality": "VALID_LEDGER",
            "verdict": "KILL_NSF_FCS_1_TRANSPORT_LEDGER",
            "reasons": kill_reasons,
            "diagnostics": c_warnings,
        }

    return {
        "quality": "VALID_LEDGER",
        "verdict": "KEEP_NSF_FCS_1_FOR_NEXT_STAGE",
        "reasons": ["stable lambda_tilt_second/G_R for transport current"],
        "diagnostics": c_warnings,
    }
```

---

## 7. 深化1：闭合节点交换 -> 网络吞吐 cohomology

第一层同构：闭合链中的 reservoir node exchange 像在 Git 仓库里数“文件打开/关闭次数”。它可以是局部状态势的差，累计量有界，不能代表提交吞吐。真正 transport ledger 必须数“从 source 进入、从 sink 完成”的跨端事务。

物理翻译：bare `R<->bulk` exchange 满足 `g=Delta psi`，所以 `Q_t=psi(X_t)-psi(X_0)`，长期方差率为零。Transport `g_T` 只数左端穿越，而右端 source 仍改变 empty/occupied state；这个 current 不能被单一 occupation potential 消去。

更深一层：`C_from_tilted_residual` 在 transport ledger 中才有意义。若 observable 是 coboundary，`lambda_tilt_second` 本身退化，所有 decomposition 缺口都是伪问题；若 observable 是 non-coboundary transport current，`C` 才是在 true throughput FCS 中定位 cancellation 的 residual。

---

## 8. 深化2：two-terminal affinity -> 非保守循环

第一层同构：电路里单端节点电压若只改一个孤立节点的平衡权重，不会产生环流；必须有 source-sink 和闭合回路的非保守电势差。上一版右库 affinity 是纯 gauge。本版 two-terminal affinity 在路径

`right injection -> bulk motion -> left extraction`

与反向路径之间产生 product-rate ratio `exp(F)`，因此能产生非零线性响应。

第二层推广：如果 two-terminal single-particle ledger 仍给出 `S_R` 稳定，它只是最小 transport falsifier 通过；下一步应把同一台账搬到 many-particle exclusion generator，或证明 PI 关心的

`D_R(L)=<sum_R c(q_R+Delta phi)^2>_pi=O(G_R(L))`

其中 `q_R` 必须属于 transport/capacity problem，而不是 closed-node exchange coboundary。

---

## 9. 本轮失败记录

1. 上一版 finite closed reversible reservoir-node chain 被 INSPECTOR 正确阻断。
2. Bare `R<->bulk` exchange 是 coboundary，不能定义可用的 `S_R`。
3. `G_R` 必须响应 transport current；单纯右节点势重标定给出 `G_R=0`。
4. KILL-5 已删除；explicit `C` 只作为 diagnostic warning，不进入 scientific keep/kill。

---

## 10. 下一步计划

1. 若 PI 落地脚本，优先实现 channel-resolved `Edge`，禁止先合并 left/right reservoir edges。
2. 先跑 `two_terminal_symmetric`，`observable_kind=left_transport_current`。
3. 首行必须先输出 `coboundary_resid`；若为 coboundary，直接 `INVALID_BARE_EXCHANGE_NOT_TRANSPORT`。
4. 只有 `transport_non_coboundary` 且 `G_R>0` 后，才计算 `S_R` scaling。
5. 如果 `KEEP_NSF_FCS_1_FOR_NEXT_STAGE`，再进入 many-particle 或 analytic capacity test；如果 `KILL_NSF_FCS_1_TRANSPORT_LEDGER`，建议停止当前强命题。

需要 PI 投喂的文献/关键词方向：

`open Markov process current FCS`, `two-terminal conductance Markov jump process`, `single-particle exclusion source sink`, `tilted generator transport current`, `fractional reservoir capacity`

---

## 11. 本轮收尾格式

本轮的跨学科跳跃：`[open queue throughput] -> [source-sink transport ledger] -> [two-terminal Markov FCS]`

这个结构的数学对象：`[channel-resolved finite generator, non-coboundary additive current, two-terminal affinity, Poisson corrector, tilted principal eigenvalue, transport conductance]`

如果这个同构成立，最奇怪的可检验预测是：`[bare exchange ledger 必须 INVALID；只有 left transport current 的 lambda_tilt_second/G_R 才能给 NSF-FCS-1 的 keep/kill]`

A博士最可能反对的点：`[single-particle open sector 仍不是 many-particle theorem；B 的回答是它只作为 minimal transport falsifier]`

本轮失败记录：`[闭合可逆 reservoir node 已废弃；KILL-5 已降级为 C diagnostic；S_R 只在 non-coboundary transport current 上定义]`

下一步计划：`[实现 nsf_fcs_transport_ledger.py 的 channel-resolved 台账，先 coboundary test，再 G/lambda/S scaling]`

需要 PI 检索的文献方向：`[Markov additive current CLT, open exclusion process conductance, tilted generator transport FCS, fractional reservoir capacity]`
