# INSPECTOR recheck NSF-FCS-1 Round 4: B 修正版

输入：
- `current/B/NSF_FCS_round4_B.md`
- `synthesis/inspector_NSF_FCS_B_round4.md`
- `synthesis/PI_NSF_FCS_round3_synthesis.md`

校对范围：只做量纲、符号/方向、循环论证、数量级、代数/极限校对。

## 复核结论

**原阻断已解除。INSPECTOR 通过，带实现警告。**

上一版阻断为：

`closed reversible bare exchange => G_R=0, lambda_R''=0, S_R undefined`.

B 修正版已把模型从闭合 reservoir-node random walk 改为 open single-particle source-sink sector：

`Omega_L={e,1,...,L}`,

并把计数 observable 改为左端 throughput / two-terminal transport current。该 `g_T` 在保留 left/right channel labels 时不是 occupation coboundary；`G_R=dJ_T/dF|0` 响应的是 transport current，不再是 bare `R<->bulk` exchange。因此上一版的 `0/0` 阻断不再适用于修正版的 transport ledger。

## Q1. 量纲校对

### rates and generator

- `r_L(x), r_R(x)`：单位 `time^-1`。
- `rho0`、`1-rho0`：无量纲。
- `eta_R, eta_L, F=eta_R-eta_L`：无量纲。
- `exp(+eta_nu/2)`、`exp(-eta_nu/2)`：自变量无量纲。
- `k_F(e,x;nu)=rho0 r_nu(x) exp(+eta_nu/2)`：单位 `time^-1`。
- `k_F(x,e;nu)=(1-rho0) r_nu(x) exp(-eta_nu/2)`：单位 `time^-1`。
- `L_F[u,v]=k_F(u,v)`、`L_F[u,u]=-sum k_F(u,v)`：单位 `time^-1`。

量纲匹配。

### transport fields

- `g_T`：count。
- `b_T(u)=sum_edges rate(edge) g_T(edge)`：`count/time`。
- `J_T=<b_T>_pi`：`count/time`。
- `h_T=b_T-J_T`：`count/time`。
- `a_T(u)=sum_edges rate(edge) g_T(edge)^2`：`count^2/time`。
- `-L_0 phi=h_T`：`phi` 单位 `count`。
- `corrector_2hphi=2 sum pi h_T phi`：`count^2/time`。

量纲匹配。

### tilted curvature and S

- `chi` 无量纲。
- `L_chi[u,v] += rate(edge) exp(chi g_transport(edge))`：单位 `time^-1`。
- `lambda_T(chi)`：单位 `time^-1`。
- `lambda_T''(0)` 的中心二阶差分除以无量纲 `eps^2` 后仍为 `time^-1 = count^2/time`。
- `G_R=dJ_T/dF|0`：`count/time`。
- `S_R=lambda_T''/G_R`：单位 count；按 count convention 可作为无量纲诊断比值。

量纲匹配。

## Q2. 符号/方向校对

### two-terminal affinity 方向

B 修正版采用

`eta_R=+F/2`, `eta_L=-F/2`,

并对每个 reservoir 用

`injection: exp(+eta_nu/2)`,

`extraction: exp(-eta_nu/2)`.

因此右端注入到左端抽取的正向两步路径权重含

`exp(+F/4) * exp(+F/4) = exp(+F/2)`,

反向左端注入到右端抽取含

`exp(-F/4) * exp(-F/4) = exp(-F/2)`,

正反 product-rate ratio 为 `exp(F)`。这确实是非保守 two-terminal driving，不是上一版的单节点纯 gauge。

### `J_T` 正方向

B 定义

- `g_T(x,e;L)=+1`：左端抽取，粒子从系统进入左 reservoir；
- `g_T(e,x;L)=-1`：左端注入；
- right 和 bulk increments 为 0。

当 `F>0` 表示右端 chemical potential 高于左端时，右注入、左抽取增强，故 `J_T(F)>0`。用最小 `L=1`、`r_L=r_R=r`、`rho0=1/2` 验算：

`J_T(F)=r/2 sinh(F/4)`,

所以

`dJ_T/dF|0 = r/8 > 0`.

符号方向自洽。

### coboundary

修正版的关键条件是必须保留 channel-resolved edges。对同一状态对 `e<->x`：

- left channel 有 `g_T(e,x)=-1`, `g_T(x,e)=+1`；
- right channel 有 `g_T(e,x)=0`, `g_T(x,e)=0`。

若要求 `g(u,v)=psi(v)-psi(u)`，left channel 要求 `psi(x)-psi(e)=-1`，right channel 要求 `psi(x)-psi(e)=0`，矛盾。因此 channel-resolved `g_T` 非 coboundary，`lambda_T''` 不被端点势差强制为 0。

该点解除上一轮阻断。

## Q3. 循环论证校对

修正版保留：

- 无独立 cross-term 时，`two_C_residual=lambda_tilt_second-a_mean-corrector_2hphi` 只作为 residual；
- `err_balance_residual=by_construction`；
- `decision_uses_C=false`；
- 有 `C_explicit` 时也只输出 diagnostic，不进入 scientific KEEP/KILL；
- 明确删除上一版 KILL-5。

未发现 residual `C` 反向验证 decomposition 的循环论证。

## Q4. 数量级与 alpha 记号校对

B 修正版把记号拆成：

- `alpha_kernel`：外部 kernel `|z-x|^(-1-alpha_kernel)` 的稳定指数；
- `alpha_tail_effective`：积分后 effective tail `r_nu(d)~d^(-alpha_tail_effective)`；
- 并声明 `alpha_tail_effective=alpha_kernel`。

Euler tail：

`int_N^infty u^(-1-alpha_kernel) du = N^(-alpha_kernel)/alpha_kernel`

要求 `alpha_kernel>0`，代数正确。此修正消除了上一轮关于 `1+alpha` 与 A/PI effective `alpha` 可能错位的主要风险。

## Q5. 代数/极限校对

### stationary / Poisson

`pi L=0`、`sum pi=1`、`-L0 phi=h_T`、`<phi>_pi=0` 的 convention 与上一版相同，量纲和代数一致。

### tilted generator

修正版要求：

`L_chi[u,v] += rate(edge u->v) exp(chi g_transport(edge))`,

且 diagonal 保持 untilted escape rate。对于 Markov additive current 的 SCGF，这是正确的 tilted-backward-generator convention。关键实现要求是：不能先把 left/right reservoir edges 合并成单个 `K[u,v]` 后再 tilt；必须先按 channel 加权 `exp(chi g)` 后求和。

### conductance central difference

修正版用：

`G(delta_F)=[J_T(+delta_F)-J_T(-delta_F)]/(2 delta_F)`,

并明确不是 bare exchange。`delta_F` 无量纲，故 `G_R` 单位 `count/time`。方向由上面的 `L=1` 极限验算给出正号。

## Bare exchange gate

修正版明确：

```python
if observable_kind == "bare_right_exchange" or observable_status == "coboundary":
    return {
        "quality": "INVALID_LEDGER",
        "verdict": "INVALID_BARE_EXCHANGE_NOT_TRANSPORT",
        "S_R": None,
    }
```

这满足 recheck 要求：bare exchange 被判为 INVALID，而不是进入 scientific KEEP/KILL。

## Keep/Kill gate

修正版规定 scientific decision 只在 `ledger_valid==true` 后执行，并且只依赖

`S_R(L)=lambda_tilt_second(L)/G_R(L)`.

KILL-1 到 KILL-4 都是 `S_R`、`G_R`、`lambda_tilt_second` 的稳定性/标度判据；KILL-5 已删除；`C` 只作为 diagnostics 返回。因此 keep/kill criteria 已回到合格 transport ledger 上。

## 实现警告

1. `invalid_bare = any(...)` 会让混入 bare/coboundary 测试行的整批 rows 返回 `INVALID_BARE_EXCHANGE_NOT_TRANSPORT`。这在“同一 ledger 不应混合 observables”的前提下没问题；实现时最好按 `observable_kind` 分账，避免一个 sanity-check row 污染 transport ledger。
2. `coboundary_resid > 1e-8` 是绝对阈值，最小二乘 residual 可能随边数或归一化 convention 变化。建议实际脚本输出 normalized residual，例如除以 `max(1, ||g||_2)`，但当前绝对阈值不是量纲错误，也不构成阻断。

## 综合判定

**INSPECTOR 通过，带警告。**

原阻断 `closed reversible bare exchange => G=0, lambda''=0, S undefined` 已由 open two-terminal transport current 修正解除。`G_R=dJ_T/dF`、`lambda_T''`、`S_T=lambda_T''/G_R` 的量纲与符号方向自洽；bare exchange/coboundary observable 已被硬门控为 `INVALID_BARE_EXCHANGE_NOT_TRANSPORT`，不能 keep/kill。

当前未发现仍需阻断的量纲、符号、循环论证、数量级或代数/极限错误。
