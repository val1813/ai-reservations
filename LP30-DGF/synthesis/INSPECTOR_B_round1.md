# INSPECTOR B Round 1

检查对象：`current/B/round1.json`

## 结论

警告通过，但存在接近阻断的循环风险。

## 关键检查

- B-F1 `theta - pi*q/2`：量纲通过，但不是完整公式。应写为 `theta = pi*q/2` 或约束残差 `theta - pi*q/2 = 0`。
- B-F2 `m_star*sin(pi*q/2)`：量纲通过；若 `m_star=2*m_p/pi`，则小 q 极限恢复 `m≈m_p*q`。
- B-F3 `2*m_p_ug/pi`：使用 `m_p_ug=21.76` 得 `13.853 microgram`，正确。
- B-F4 `q_inv=2*asin(pi*m_ug/(2*m_p_ug))/pi`：代数正确，但对 `m_ug>13.85` 非实。

## 判定

“q_inv 非实”本身不是可观测现象，只是反演公式定义域失败。要成为物理预言，下一轮必须给出从非实定义域到 fringe visibility 异常、模型失配残差、相变式衰减或其他可观测的机制。

## 投喂下一轮

阻断级：

1. B-F4 的 `q_inv` 在 `m_ug > 2*m_p_ug/pi` 非实，目前只能说明反演定义失败，不能直接声称为可观测边界。
2. Fisher-Rao / Hellinger 角 q 的质量独立性未建立。下一轮必须提供 q 的独立 readout / fluctuation 定义；若 q 仍由质量反推，则 B-C1/B-C2 构成循环重参数化。

警告级：

1. B-F1 应改成 `theta = pi*q/2` 或 `theta - pi*q/2 = 0`。
2. DGF-N4 特定边界依赖 `m_star=2*m_p/pi` 的模型定标。
3. 14 microgram 仅比边界高约 1.1%，实验声张必须处理质量校准和系统误差。
4. 当前落地计算仍缺 visibility 函数、背景扣除模型、q 独立测量方案和误差预算。
