# INSPECTOR A Round 2

检查对象：`current/A/round2.json`

## 结论

警告通过。Round 2 基本解决了 Round 1 的两个阻断方向，但尚不能作为可落地强结论。

## 关键判定

- `q_readout=(2/pi)*asin(V/V_ref)` 量纲正确，但不能在统计模型中使用 `clip(V/V_ref,0,1)`；clip 会吞掉异常和越界信息。
- 正确做法：设潜变量 `q∈[0,1]`，令 `V_model=V_ref sin(pi*q/2)`，用 `V_obs` likelihood 处理越界观测。
- `q_readout` 当前是“相干可见度坐标”，不是自动等同于 DGF 质量映射坐标。若要把同一个 q 代入 `m=(2m_p/pi)sin(pi q/2)`，必须新增桥接假设。
- `fisher_visibility` 是 Fisher information 模板，但缺少具体 `P_i(q)` 或连续 likelihood。
- LLR 量纲正确；建议固定符号约定：`LLR=2(logL_env-logL_DGF)`，正值支持环境/null。

## 投喂下一轮

阻断级：

1. 不得在统计模型中使用 `clip(V/V_ref,0,1)` 作为 q 定义。改为潜变量 `q in [0,1]` + `V_model=V_ref sin(pi*q/2)` + `V_obs` likelihood。
2. 明确区分 `q_visibility` 与 `q_DGF_mass`。若要令二者相同，必须写出桥接假设或机制。
3. 给出至少一个具体 `P_i(q)` 或连续读出 likelihood，使 Fisher 信息可计算。

警告级：

1. 明确 LLR 符号和判别阈值。
2. 只能写“与环境/null model 比较”，不能写“排除环境退相干”。
3. 下一轮至少补一张最小表：`t, V_obs, sigma_V, V_env_best, V_DGF_best, residual, chi2 contribution`。
