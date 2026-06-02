# LP7-S1 — B 独立检查

## 0. 独立性声明
我只依据本任务书与指定文献锚点作判断，不读取 `current/A/LP7-S1_phase1.md`，也不使用任何 A 输出。

## 1. 最小模型
取二分支质量态

`|\psi> = (|L> + |R>)/sqrt(2)`

naive expectation-source 的牛顿势写成

`Phi_naive(x) = -G \int d^3x' <rho(x')> / |x-x'|`

在两分支近似正交、交叉项可忽略时，

`<rho> ≈ (rho_L + rho_R)/2`

所以

`Phi_naive ≈ (Phi_L + Phi_R)/2`

其中 `Phi_L` 与 `Phi_R` 分别是单次分支 `|L>`、`|R>` 的经典牛顿势。  
单次分支势就是

`Phi_L(x) = -G \int d^3x' rho_L(x') / |x-x'|`,  
`Phi_R(x) = -G \int d^3x' rho_R(x') / |x-x'|`.

可观测差异在于：naive expectation-source 预测的是“平均场”或中间场，而分支势预测的是与实际分支一致的定向力矩/加速度。对 Page-Geilker 型装置，这意味着指针应偏向与当前分支质量配置对应的方向，而不是停在两个分支的平均响应附近。

## 2. Page-Geilker 可推出什么/不能推出什么
Page & Geilker 1981 明确写的是：实验结果与“最简单的替代方案”即 semiclassical Einstein equations 不一致，并且“支持但不证明”引力量子化。

因此它能推出的是：

- 反对朴素的 `G=<T>`/期望值源项半经典方程作为直接模型。
- 反对“宏观分支质量配置的引力响应等于分支平均”的 naive expectation-source 版本。

它不能推出的是：

- 不能推出“引力必须量子化”作为唯一结论。
- 不能推出“所有 classical/semi-classical gravity 都失败”。
- 不能推出“任何以经典场描述的引力理论都被排除”。

核心边界在于：Page-Geilker 打到的是“期望值当源且不额外补偿”的那一支，不是整个经典/半经典家族。

## 3. 逃逸路线表

| 路线 | 是否被 Page-Geilker 排除 | 理由 |
|---|---|---|
| stochastic gravity / Einstein-Langevin | 否 | 它把应力能涨落作为噪声核纳入方程，不等同于纯 `G=<T>` 的无噪声期望值源模型。 |
| classical-channel / measurement-feedback gravity | 否 | 这类模型把引力解释为经典信道或测量反馈，可产生退相干并压制纠缠判据，但不必退回 naive expectation-source。 |
| Kafri-Taylor-Milburn 类 | 否 | 它们是经典信道重建方案，目标就是在保留经典媒介的同时加入必要退相干。 |
| Oppenheim 2023 postquantum classical gravity | 否 | 该方案明确构造了一个与半经典期望值方程不同的、仍为经典时空的自洽框架。 |
| 纯粹 expectation-value semiclassical Einstein equation | 是 | 这是 Page-Geilker 直接针对的最简单版本。 |

## 4. 对预期 A 结论的攻击
- “Page-Geilker 只边界化 naive expectation-source。” 这句基本成立，但必须把“只”理解为“只针对该最简单源项规则”，而不是“只对某个模糊的半经典词汇边界化”。
- “stochastic gravity 是否足以逃逸仍未定。” 从本任务给定锚点看，这不应写成悬而未决；stochastic gravity 本身就是已知的存活逃逸路线之一，Page-Geilker 没有把它打掉。
- “classical channel gravity 转入 BMV 纠缠判据。” 这更像后续判据迁移，而不是 Page-Geilker 的直接否定对象。Page-Geilker 不能单独排除这种路线。
- “postquantum classical gravity 是 LP7-S1 的重要反例栏。” 这成立；Oppenheim 2023 明确给出经典引力与量子物质耦合的自洽方案，并声称避开半经典期望值方程的病态。

## 5. B 结论类型
**有边界。**

理由：Page-Geilker 足以排除 naive expectation-source semiclassical gravity，但不足以排除全部 classical/semi-classical gravity；stochastic gravity、classical-channel/measurement-feedback 以及 postquantum classical gravity 都仍是存活路线。

## 6. 待 PI 仲裁问题
1. LP7-S1 的最终表述是否应固定为“反驳最朴素半经典源项”，而不是泛称“反驳半经典引力”。
2. stochastic gravity 在本项目里应被列为“已存活模型”还是“有效理论入口”。
3. classical-channel 与 postquantum classical gravity 是否需要分成两条独立反例栏。
