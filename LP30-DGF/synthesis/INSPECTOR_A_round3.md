# INSPECTOR A Round 3

检查对象：`current/A/round3.json`

## 结论

Round 3 比 Round 2 有明显修正，但仍有阻断级问题。

## 阻断

1. M1 的逐点 `q_i` 自由度会导致过拟合。若每个数据点都有独立 `q_i`，`V_ref*sin(pi*q_i/2)` 可吸收大部分 visibility 残差。必须给出外部 prior、层级约束、平滑动力学约束、Bayes evidence、AIC/BIC 或交叉验证。
2. `single_order_parameter_bridge: q_visibility=q_DGF_mass` 仍是额外桥接假设。若 DGF 质量声称依赖它，当前不可作为物理结论收尾。
3. 最小 LLR 表不完整；当前示例只给 DGF residual/chi2，没有给 M0 residual/chi2、prior penalty、logL_env、logL_DGF、LLR。

## 警告

- M1 prior 缺少 Gaussian 归一化项；若 `sigma_q` 参与比较，必须补。
- 示例表虽然算术正确，但固定 `V_DGF_best=0.7071` 与逐点 profile `q_i` 不一致。
- 替代解释不足，不能只用一个 exponential M0 代表所有 null。
- `sympy_mass` 没有进入 likelihood；若保留 DGF mass 语言，需说明它只是桥接解释层。

## 投喂下一轮/收尾

必须解决过拟合和桥接假设，否则只能收官为“统计化框架草案，核心物理桥接未成立”。
