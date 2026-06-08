# INSPECTOR 强制挽救轮

Agent：Descartes (`019e9514-0178-75e0-96df-b191a425965a`)

## 机械检查

未运行。输入为强制挽救摘要，不含 `roundN_claims.json`、完整公式行号或 `validation/` 路径；本轮按 SOP 降级为独立 Agent 语义 INSPECTOR 检查。

## 检查对象

- A 挽救：把逐点自由 `q_i` 改为少参数共享潜变量
  `q_i=sigmoid(logit(q_star)+beta_M log(M_i/M_star)+beta_t g(t_i;tau)+beta_env z_env_i)`；
  用 `delta_bridge` 检验 `q_visibility` 与 `q_DGF_mass` 的桥接残差。
- B 挽救：交换低秩/图拉普拉斯/跨表征一致性模型，修复 `log(M_cal)` 为
  `log(M_cal/13.85 microgram)`，用投影和残差判据检验质量边界。

## 判定

挽救失败，按“当前北极星存活”标准不通过；只能保留为待验证统计模型。

已解除或部分解除：

- 逐点自由 `q_i` 直接过拟合：A 方案基本解除；B 方案仅部分解除。
- `log(M/13.85 microgram)` 量纲错误：已解除。
- `q_visibility=q_DGF_mass` 硬等号：形式上改为 residual / `delta_bridge` 检验。

仍保留为阻断：

- 外部 `q_DGF_mass` observable 未证明可获得；若由同一 visibility 数据反推，则桥接检验循环。
- B 的低秩/图模型若图、秩、正则强度、特征字典未预注册，仍可能等价于高灵活后验拟合。
- `K`、`h(x,q)`、`P_m`、`W`、`X_m/X_q` 与图拉普拉斯 penalty 的量纲和归一化未闭合。
- `M_star=13.85 microgram` 尚无独立校准来源、不确定度和尺度敏感性检验；目前只能作为参考尺度，不能作为 DGF 核心物理常数。
- LLR 表仍是模板，缺真实数值、惩罚项、bootstrap/null 和预注册 acceptance thresholds。

## PI 结论

强制挽救轮没有恢复 DGF-N4 的强物理命题。按 PI.md §2 条件B，允许执行降级动作：

1. DGF-N4 标记为“证伪-降级”；
2. 分数降为 `max(1, old*0.3)`；
3. 从失败过程强制分叉并注册不少于两个新方向。
