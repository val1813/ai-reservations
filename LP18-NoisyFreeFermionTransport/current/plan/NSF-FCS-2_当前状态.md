# NSF-FCS-2 当前状态

**当前北极星：** long-jump open exclusion 的 NESS FDT residual scaling。

**一句话：** equilibrium two-terminal second cumulant 已降级为有限体积 FDT corollary；真正有价值的问题是 NESS 中 `R2(L)=lambda_T''(L)-2G_T(L)` 是否携带 reservoir-tail / fractional conductance 的新标度。

**优先级分数：** 9.0/10。

**切换依据：**
- NSF-FCS-1 bare reservoir-exchange 版本已 kill：bare exchange 是 occupation coboundary，长期二阶 FCS 为 0。
- NSF-FCS-1 two-terminal equilibrium 二阶版本已降级：local detailed balance + equilibrium two-terminal affinity 下 `lambda_T''=2G_T`。
- Tier 1 NESS bias scan 显示 `R2` 稳定非零，并且在 `L=8` 对 `delta=|rho_R-rho_L|` 近乎精确二次增长。

## 当前数值证据

- `current/plan/nsf_fcs_tier1_ness_0p45_0p55.csv`
- `current/plan/nsf_fcs_tier1_ness_0p40_0p60.csv`
- `current/plan/nsf_fcs_tier1_ness_0p35_0p65.csv`

45 行全部 `ROW_VALID`。

关键斜率：
- `alpha=0.5`: `slope(log |R2|) ~= 1.009`
- `alpha=1.0`: `slope(log |R2|) ~= 0.621`
- `alpha=1.5`: `slope(log |R2|) ~= 0.279`

偏置幅度：
- 固定 `L=8` 时，`R2 ~ delta^2`，三个 alpha 的 delta 斜率分别约 `2.000030`, `2.000000`, `1.999998`。

## 前置检查

- [x] equilibrium affinity split sanity 通过。
- [x] NESS density-bias residual 非零。
- [x] residual 对 density bias 的二次幅度通过。
- [x] NSF-FCS-2 已高于 NSF-FCS-1 equilibrium 二阶分支。
- [ ] NSF-FCS-2 AB Round 1 尚未启动。

下一步：启动 NSF-FCS-2 AB Round 1。A 侧做 near-equilibrium/NESS response 推导；B 侧做数值 stress test 与 non-LDB/activity forcing 设计。

## 反向偏置 sanity check

- 已新增：`current/plan/nsf_fcs_tier1_ness_reverse_0p60_0p40.csv`
- 15 行全部 `ROW_VALID`。
- 与 `rho_left=0.4,rho_right=0.6` 对照：
  - `max |Delta S_T| = 6.03e-8`
  - `max |Delta R2| = 8.46e-9`

判定：二阶 NESS residual 对偏置反向为偶函数到数值精度，不是电流符号约定造成的假残差。

## Round 1 A/B 结果

- A 输出：`current/A/NSF-FCS-2_round1.md`
- B 输出：`current/B/NSF-FCS-2_round1.md`
- A INSPECTOR：`synthesis/inspector_NSF_FCS2_A_round1.md`，结论 `WARNING`，可继续，但 `Q_L~L^{1/2}` 与 `3/2-alpha` 必须保留为 ansatz。
- B INSPECTOR：初检 `BLOCKED`，修正后 `synthesis/inspector_NSF_FCS2_B_round1_recheck.md` 结论 `PASS`。
- PI 综合：`synthesis/PI_NSF_FCS2_round1_synthesis.md`

当前 sharpened claim:

`Qhat(L,alpha)=R2/(delta^2 G_T)=(S_T-2)/delta^2`

现有三组 centered-bias ledger 显示 `Qhat` 的 `L` 斜率约 `0.47..0.54`，比 raw `R2` 更稳定、更接近 bias-independent。下一步应围绕 `Qhat` 做大 L、off-center density 与 non-LDB site-skew falsifier。

## Off-center density falsifier

- 新增：`current/plan/nsf_fcs_tier1_ness_offcenter_0p30_0p50_L4_7.csv`
- 新增：`current/plan/nsf_fcs_tier1_ness_offcenter_0p55_0p75_L4_7.csv`
- 两个文件均为 12 行、全部 `ROW_VALID`。

与 centered `0.40 -> 0.60` 在同一 `L=4..7, delta=0.2` 比较：
- `alpha=0.5`: `Qhat` 斜率 `0.496859 / 0.496877 / 0.496907`
- `alpha=1.0`: `Qhat` 斜率 `0.542479 / 0.542582 / 0.542727`
- `alpha=1.5`: `Qhat` 斜率 `0.564290 / 0.564527 / 0.564847`

判定：off-center density 改变 `Qhat` 幅度，但不改变当前 `L` 指数窗口；`Qhat~L^{1/2}` 不是简单的 particle-hole 中心假象。
