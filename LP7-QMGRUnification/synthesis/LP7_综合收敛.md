# LP7 综合收敛：证否统一公式，确认中间层

日期：2026-06-01

## 总结论

LP7 目前没有得到一个可宣布成立的“量子力学-广义相对论统一公式”。

更强、更稳妥的结论是：

```text
J_unify as a single fundamental equation = false
J_unify as an admission criterion over an operational interface = true
```

因此 LP7 的真实产物不是终极动力学方程，而是候选理论进入统一讨论之前必须显式给出的中间操作层：

```text
I[T] = (Phi_source, Phi_mediator, Phi_noise, Phi_entropy, Phi_obs, Phi_frame)
```

候选理论的正确审查链条是：

```text
Theory T -> Interface I[T] -> Criteria J_unify[I[T]]
```

而不是：

```text
Theory T -> one universal equation J_unify[T]
```

## 为什么单一公式被证否

`J_unify` 若被解释为单个统一方程，会立即失败在三层不匹配：

1. 层级不匹配：Page-Geilker 源项、BMV 媒介、hybrid noise、Page curve 熵规则、detector response、frame consistency 不属于同一种物理对象。
2. 动力学不闭合：六块判据只是候选约束，不给出共同的 Hamiltonian、action、path integral 或 stochastic generator。
3. 可观测字典不统一：强引力熵、弱场相位、实验室探测器响应和单次测量源项不能直接压入同一个标量距离。

所以，`J_unify[T]` 不是“统一动力学”；它只能是对 `I[T]` 的惩罚泛函或准入函数。

## 中间层定义

```text
I[T] = (Phi_source, Phi_mediator, Phi_noise, Phi_entropy, Phi_obs, Phi_frame)
```

各块含义：

| 中间层块 | 来源子题 | 最低要求 |
|---|---|---|
| `Phi_source` | LP7-S1 | 说明单次分支源项如何进入几何/势，不能把 ensemble expectation 当作每次运行的实际源项 |
| `Phi_mediator` | LP7-S2 | 说明媒介如何传递相位/纠缠，以及何种意义上非经典 |
| `Phi_noise` | LP7-S3 | 若走 classical-quantum hybrid 路线，必须显式支付 stochasticity / diffusion / decoherence 代价 |
| `Phi_entropy` | LP7-S4 | 给出 Page curve 或明确修改黑洞信息悖论四假设中的哪一条 |
| `Phi_obs` | LP7-S6 | 给出 detector response / phase / entropy / operational dictionary |
| `Phi_frame` | LP7-S7 / 公式确认 | 保证弱场、强场、测量源项与可观测映射在参考系变化下不互相矛盾 |

## 正确判据

准入条件应写成：

```text
all Phi_a in I[T] are defined
and
J_unify[I[T]] <= epsilon_unify
```

失败条件：

```text
exists a in {source, mediator, noise, entropy, obs, frame}: Phi_a undefined
=> T is not a LP7 unified candidate
```

六块判据对应为：

```text
J_unify[I[T]] =
(
  J_PG[Phi_source],
  J_BMV[Phi_mediator],
  J_hybrid[Phi_noise],
  J_BH[Phi_entropy],
  J_obs[Phi_obs],
  J_frame[Phi_frame]
)
```

其中 S6 的因果集传播子公式只能进入第五块：

```text
J_obs^CS[D,J] = dist_delta(D^T(K_i-K_j)J, Im M_cross)
```

它是 detector-response 实现模块，不是完整统一公式。

## S1-S7 收敛关系

| 子题 | 收敛角色 | 当前等级 |
|---|---|---|
| S1 Page-Geilker | 排除 naive expectation-source；要求 `Phi_source` | L2 |
| S2 BMV | 标准局域经典媒介不能生成纠缠；要求 `Phi_mediator` | K62 为 L2，K63 为 L3 |
| S3 hybrid no-go | deterministic naive hybrid closure 不合格；要求 `Phi_noise` | L2 |
| S4 black-hole information | 统一候选必须处理 Page curve / entropy rule；要求 `Phi_entropy` | L2 |
| S5 criterion matrix | 给出 U1-U5 准入矩阵；现重释为 `J_unify[I[T]]` | L2/L3 边界 |
| S6 causal-set bridge | 给出 `J_obs^CS` 作为 detector-response 实现 | L3，受 v13 GATE 未闭合限制 |
| S7 total block matrix | 加入 `J_frame` 稳定性门槛 | L3 |

## 对原问题的回答

若原目标是“找到统一公式”，当前答案是否定的：

```text
No single confirmed formula has been found.
```

若原目标是“找到所有候选公式必须经过的中间层”，当前答案是肯定的：

```text
The middle layer is I[T].
```

LP7 的结论类型仍为：

```text
有边界
```

边界精确定义为：LP7 已经给出统一候选的操作性接口层与准入判据，但尚未给出通过该判据的具体统一动力学。

## 下一步

下一阶段不应继续把 `J_unify` 当作终极方程硬推，而应转向候选理论筛查：

1. 选择一个候选理论 `T`；
2. 强制写出 `I[T]` 六块；
3. 计算或定性判定 `J_unify[I[T]]`；
4. 任一块缺失则登记为非 LP7 统一候选。
