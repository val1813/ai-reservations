# INSPECTOR B Round 3

检查对象：`current/B/round3.json`

## 结论

警告通过，但有阻断级问题，不能直接作为收尾版公式。

## 阻断

1. `x_i=log(M_cal_i)` 量纲错误。应改为 `x_i=log(M_cal_i/M_ref)`，并补充 `M_cal_i>0`、`1+s_cal>0`。
2. `q` 独立性仍是统计检验计划，不是已解决结论。必须定义 `X_m, X_q, W, P_m, h(x,q)`、样本维度、rank 阈值和 bootstrap/null。

## 警告

- `projection_score` 需明确矩阵乘法、W-范数、投影矩阵公式和分母非零条件。
- `rank` 判据需补样本数、矩阵维度和数值 rank 容差。
- `Delta_14_22` 中 `sigma_cal^2*beta_m^2` 仅当 `sigma_cal` 是 log-mass 不确定度时成立；若是质量误差需 Jacobian 传播。
- `T_14_22` 与 A 的 LLR 正负方向相反，需改名并显式标注正值支持哪一模型。
- caustic-like 降级合格，但仍缺 `J_phi`、`Sigma_y`、投影密度和阈值。

## 投喂下一轮/收尾

B 路线已提供可检验计划，但不能声称 `q` 独立性已解决。
