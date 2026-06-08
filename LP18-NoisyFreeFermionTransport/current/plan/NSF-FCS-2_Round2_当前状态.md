# NSF-FCS-2 Round 2 当前状态

**触发原因：** REVIEWER final recommendation = major revision.

**当前北极星：** long-jump open exclusion 的 NESS FDT residual scaling.

**Round 2 定位：** 大修验证轮，不做 theorem claim。目标是消除 REVIEWER 指出的 normalization / circularity / small-L / activity-control 风险。

## REVIEWER 五条约束进展

1. FDT anchor normalization：已完成。见 `synthesis/PI_NSF_FCS2_round2_fdt_normalization.md`。
2. Direct delta test：已完成。raw `R2` 对 `delta` 的指数在 `L=4..7`、`alpha=0.5,1.0,1.5` 上约为 2。见 `synthesis/PI_NSF_FCS2_round2_delta_test.md`。
3. Off-center reverse bias：已完成。`rho_bar=0.4,0.65` 的反向偏置差异为数值误差量级。见 `synthesis/PI_NSF_FCS2_round2_offcenter_reverse.md`。
4. Larger-L/model comparison：已完成当前窗口比较。log drift 在所有可用数据和 alpha 上 AIC 最优；`Qhat~L^{1/2}` 降级为 finite-window effective exponent / unresolved growth。见 `synthesis/PI_NSF_FCS2_round2_qhat_model_compare.md`。
5. Activity controls：已完成实现和 sanity。`reversible_side` 是 LDB sanity control；`nonLDB_site_skew` 是 non-LDB kinetic forcing。见 `synthesis/PI_NSF_FCS2_round2_activity_controls.md`。

## 新增数值结论

- Direct raw `R2~delta^2`：`delta=0.05,0.10,0.15,0.20,0.30` 合并拟合，指数约 `1.99997` 到 `2.00011`。
- Off-center reverse bias：`0.30->0.50` vs `0.50->0.30` 的最大 `|Delta S_T|=4.10e-8`；`0.55->0.75` vs `0.75->0.55` 的最大 `|Delta S_T|=2.96e-8`。
- Activity equilibrium sanity：`reversible_side,A=0.1` 在 `rho_left=rho_right=0.5` 下最大 `|R2|=1.88e-7`，保持 FDT；`nonLDB_site_skew,A=0.1` 最大 `|R2|=4.95e-5`，产生可区分 residual。
- FDT convention：ledger 使用 dimensionless Markov-affinity convention；`lambda_T''`、`G_T`、`R2` 单位均为 inverse time，`S_T` 与 `Qhat` 无量纲。

## 当前判断

NSF-FCS-2 仍为当前主线，但结论必须保守表述：

- 可说：NESS density bias 的 `R2=lambda_T''-2G_T` 在当前 small-L ledger 中稳定非零，raw `delta^2` 与 reverse-bias sanity 已通过。
- 可说：`Qhat` 有 unresolved growth；log drift 当前比 power-law ansatz 更优。
- 不可说：`Qhat~L^{1/2}` 已确立。
- 不可把 `reversible_side` activity 当成 kinetic residual 证据。

## Round 2 A/B re-attack 结果

- A 博士：`KEEP`，但只保留 narrow finite-volume residual program。
- B 博士：`REDIRECT`，建议从 exponent-centered `Qhat` 转向 FDT-manifold curvature/separability diagnostic。
- INSPECTOR-A：`WARNING`，无阻断。
- INSPECTOR-B：`WARNING`，无阻断。

PI 综合：`REDIRECT-within-KEEP`。NSF-FCS-2 数据包继续保留，但当前活动子命题重定向为：

> NSF-FCS-2R: long-jump open exclusion 的 finite-volume FDT-residual curvature/separability diagnostic.

硬约束：

- 不再使用 `Qhat~L^{1/2}` 或 asymptotic power-law wording。
- `R2/G_T` 只能称为 operational curvature-like coordinate，不能称为已证明的 second normal curvature。
- non-LDB activity 必须用 `A=+a,-a` 或多幅度拟合区分 `A` 与 `A^2`。

## 下一步

进入 NSF-FCS-2R coefficient/parity validation：固定 `L,alpha` 提取 `R2=C_L delta^2 + D_L delta^4`，并用 `reversible_side` / `nonLDB_site_skew` 的 `A=+a,-a` 对照验证 perturbation separability。

## NSF-FCS-2R validation update

Completed:

- coefficient extraction: `R2=C_L(alpha) delta^2 + D_L(alpha) delta^4` at `L=4..7`, `alpha=0.5,1.0`, `delta=0.02..0.08`; all `C_L>0`.
- activity parity: equal-density `nonLDB_site_skew` is dominated by an even `A^2` response, not `A`; `reversible_side` remains numerical-floor at equilibrium.
- mixed separability: for `delta=0.04`, `A=±0.10`, nonLDB mixed residual is additive to `1.04e-4` relative error, while reversible traffic changes NESS curvature at about `5.88e-2` relative level.

Current best statement:

> Density bias and nonLDB site skew are separable to current numerical precision in the tested mixed window, with signatures `delta^2` and `A^2`. Reversible-side traffic is an equilibrium LDB sanity control, but in NESS it can renormalize the density-bias curvature coefficient.

Next SOP step: stopping-condition check. If no hard stop, launch next A/B or move to reviewer/closure gate depending on Phase discipline.
