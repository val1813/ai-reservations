# INSPECTOR A Round 1

检查对象：`current/A/round1_manual.json`

## 结论

部分通过，但存在阻断级定义域错误。

## 关键检查

- A-F1 `2*m_p/pi`：量纲为 kg，数值 `2*2.176e-8/pi = 1.3853e-8 kg = 13.8528 microgram`，通过。
- A-F2 `q_inv=2*asin(pi*m/(2*m_p))/pi`：在 `m=2*m_p/pi` 时 `q=1`，端点正确。
- 对 `m=1.6e-8 kg, m_p=2.176e-8 kg`，asin 参数为 `1.155>1`，实数域无定义。因此原 numerical_test `[1.0,2.0]` 错误。

## 判定

16 microgram 超过 `13.85 microgram` 边界，只能表述为“实 q 不存在/模型实域越界”，不能表述为 q 在 `[1,2]` 的实数范围。

## 投喂下一轮

阻断级：

1. A-F2 numerical_test 错误：16 microgram 时 asin 参数 >1，实 q 不存在。改为“DGF 实域边界越界/非实 q 判据”。
2. 不得基于 `[1.0,2.0]` 的 q 数值范围继续推导。

警告级：

1. 文献声张改为“不完整检索未命中”，不能说完整支持“未发现直接先发”。
2. q 必须独立定义并可观测，否则是质量重参数化。
3. 落地计算需补实际 16 microgram 数据重分析与 DP/CSL/environmental 对照统计判据。
