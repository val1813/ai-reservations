# LP7-S3 任务书：经典-量子混合动力学 no-go 边界

生成时间：2026-06-01

## 题目

经典-量子混合动力学 no-go 边界。

## 目标

找出哪些 hybrid classical-quantum dynamics 真正矛盾，哪些只是模型受限。

## 北极星

不是证明“所有经典-量子混合理论都不成立”，而是压缩为一个可判别命题：

> 若经典自由度要与量子系统一致耦合，则它必须付出随机噪声、扩散、退相干或非局域假设的成本；deterministic / naive hybrid closure 不能同时保住完全正性、局域性、无超光速信号与低噪声可观测输出。

## 已知锚点

| 编号 | 文献 | 作用 |
|---|---|---|
| LP7-S3-1 | Hall, Reginatto, Savage 2012, *Nonlocal signaling in the configuration space model of quantum-classical interactions* | 经典-量子混合模型存在非局域信号风险，说明适用域受限 |
| LP7-S3-2 | Hall & Reginatto 2021 comment | 说明“经典介质可生成纠缠”争论中存在多类混合模型，no-go 通常依赖额外假设 |
| LP7-S3-3 | Bermúdez Manjarres, Reginatto, Ulbricht 2024 | 识别两类不等价 hybrid 模型，尤其在 entanglement 预测上不同 |
| LP7-S3-4 | Oppenheim et al. 2020/2023, *Objective trajectories in hybrid classical-quantum dynamics* | 存在一致的 stochastic hybrid dynamics，但需随机性与扩散，且“测量公设”被替换 |
| LP7-S3-5 | Oppenheim et al. 2022/2023, *Gravitationally induced decoherence vs space-time diffusion* | classical gravity 路线的可检验代价：decoherence 与 metric diffusion 贸易 |
| LP7-S3-6 | Oppenheim 2023, *A Postquantum Theory of Classical Gravity?* | 经典引力并非立刻自毁，但必须是后量子/随机/混合动力学 |

## 反例栏

| 反例/风险 | 影响 |
|---|---|
| Hall-Reginatto / Oppenheim 类模型存在存活分支 | 不能把结论写成全局 no-go |
| 一些 hybrid 构造可以生成纠缠 | 不能把“经典介质”与“不能生成纠缠”直接等同 |
| 随机完全正混合动力学可自洽 | 只能攻击 deterministic 或 naive closure |
| 引力相关混合理论常需要噪声-扩散代价 | 结论应写成边界条件，而非最终排除 |

## 判定标准

1. 若模型要求确定性且同时保持量子与经典自由度的闭合，则优先检查是否触发非局域信号或正性破坏。
2. 若模型允许 stochasticity，则检查其代价是否转化为 decoherence / diffusion trade-off。
3. 若模型仍能生成纠缠，则必须显式列出“经典”假设被保留到什么程度。
4. 若模型只在特定耦合常开、特定配置或特定 ensemble 下成立，则应降级为受限 proposition。

## 下一步

▶️ 下一步：执行 LP7-S3 的 A 正规推导，先建立 hybrid 模型分类表与 no-go/escape 边界。
