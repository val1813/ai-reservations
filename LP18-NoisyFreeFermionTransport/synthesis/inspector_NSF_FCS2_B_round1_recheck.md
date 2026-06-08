# INSPECTOR recheck：NSF-FCS-2 B Round 1 修正版

结论：PASS

范围：核查 `current/B/NSF-FCS-2_round1.md` 对上一轮 `synthesis/inspector_NSF_FCS2_B_round1.md` 的 BLOCKED 点是否逐条修复。未读取 A 文件或 `current/A`。

## 1. 单位问题

判定：PASS。

上一轮阻断点是 `R2`、`B2=R2/delta^2`、`a2/a3`、`M`、`c20/c02/c11` 被写成无量纲。修正版已明确：

- `R2`、`B2`、`a2/a3`、`M_R`、`c20/c02/c11` 单位均为 `1/time`。
- `delta,A,eta,phi_x` 无量纲。
- 无量纲比较改用 `B2/G_T`、`a2/G_T`、`R2/G_T`、`M_Y`。

这修复了量纲自洽性问题。

## 2. `Q_J`

判定：PASS。

上一轮阻断点是 `R2/J0^2` 被当作无量纲量。修正版已改为：

- `tau_J=R2/J0^2`，单位 `time`，只作时间尺度诊断。
- `Q_JG=R2*G_T/J0^2`，无量纲。
- 显式要求 `J0 != 0` 且远离数值噪声。

该修正量纲正确，且避免了近零 `J0` 的方向误用。

## 3. pure activity / LDB

判定：PASS。

上一轮阻断点是把 `delta=0,A!=0` 的同侧 in/out 同乘 activity 解释成可能的 kinetic residual。修正版已改为：

- `reversible_side` activity 是 equilibrium/FDT sanity control。
- 在 `delta=0,A!=0` 且同侧 in/out ratio 不变时，预期 `R2≈0`、`S_T≈2`。
- 若出现非零 `R2`，优先解释为 implementation/FDT-response mismatch、tilt pairing 错误、finite-difference instability，或 multiplier 实际破坏 LDB。

这修复了方向错误。

## 4. non-LDB forcing

判定：PASS with retained implementation check。

修正版新增 `nonLDB_site_skew`，通过 site-dependent forward/backward ratio：

`left_in/left_out = [rho_left/(1-rho_left)] exp(eta_left + A phi_x)`

`right_in/right_out = [rho_right/(1-rho_right)] exp(eta_right - A phi_x)`

并指出该 ratio 不能由单个 reservoir chemical potential 吸收，需通过闭合环 log-rate circulation 确认。

这满足上一轮“必须定义真正破坏 detailed balance 的 non-LDB forcing，并写清 rate ratios”的要求。后续实现时仍需显式计算至少一个 cycle affinity，确认该 forcing 没有被代码中的状态势或 reservoir 重参数化吸收。

## 5. KL / traffic / Fisher / curvature

判定：PASS。

修正版已补全可测量与单位：

- `J0`、`Traffic_left/right`、`KL_rate`：`1/time`。
- `Traffic_asym`、`R2/G_T`、`D_rate/G_T`、`Escape_cv2`：无量纲。
- `Escape_var`：`1/time^2`。
- `I_ab` 定义为 path KL rate 的二阶导，单位 `1/time`，无量纲比较用 `I_ab/G_T` 或 `I_ab/(mean_pi a_i)`。
- response observable 明确定义为 `Y=R2/G_T`。
- `Omega_deltaA` 被降级为导数一致性检查；真正可测对象改为 `M_R` 与 `M_Y`。

这修复了上一轮“Fisher/curvature 类比未落到可测物理量”的阻断点。

## 6. 残留弱点

可继续，但后续 ledger 必须保留以下检查：

1. `G_T != 0`、`J0 != 0` 且误差传播受控，否则 `R2/G_T`、`Q_JG`、`C3/J0` 不可用。
2. `nonLDB_site_skew` 需要用 cycle affinity 或等价 detailed-balance 检查确认确实 non-LDB。
3. `KL_rate` 的 reverse edge pairing 对 reservoir injection/extraction 必须使用 same-site empty/occupied flip 配对。
4. `Omega_deltaA` 不能被当作已证明的物理曲率；目前只允许使用 `M_R/M_Y` 作为 mixed response non-additivity。

## 综合判定

PASS。上一轮 BLOCKED 的四类问题已经逐条修复；剩余内容属于后续数值实现时必须显式保留的 sanity checks，不再阻断 B Round 1 kill ledger 继续推进。
