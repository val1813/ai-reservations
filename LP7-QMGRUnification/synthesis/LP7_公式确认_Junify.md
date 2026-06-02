# LP7 公式确认 — `J_unify` 判据矩阵

## 目标

用户要求“继续推理公式，确认它”。这里确认的不是终极统一方程，而是 LP7 当前阶段唯一稳妥的对象：

> 一个候选统一公式的可观测准入判据矩阵 `J_unify`.

现有 S6 给出的

`J_unify^CS[D,J] := dist_delta(D^T(K_i-K_j)J, Im M_cross)`

是正确的，但只覆盖 detector-response / propagation kernel 层。因此它不能单独作为完整 LP7 统一公式判据。需要把它嵌入块矩阵。

## 块矩阵形式

定义候选理论 `T` 的统一判据：

```text
J_unify[T] =
(
  J_PG[T],
  J_BMV[T],
  J_hybrid[T],
  J_BH[T],
  J_obs[T],
  J_frame[T]
)
```

其中合格候选要求：

`J_unify[T] <= epsilon_unify`

并且每一块都不能缺失。

## 各块定义

### 1. Page-Geilker / 测量源项块

```text
J_PG[T] = dist_delta(R_T[J_branch], R_exp[J_branch])
        + dist_delta(R_T[J_avg], R_forbidden[J_avg])
```

最低要求：

- 不把 ensemble `<T>` 当作每次实验的实际源项；
- 能说明单次分支 source 如何进入几何/势。

在因果集传播子实现中：

```text
Delta R_PG = D^T K_T (J_branch - J_avg)
```

### 2. BMV / 媒介非经典块

```text
J_BMV[T] = dist_delta(phi_T, phi_BMV)
         + penalty(classical_local_mediator_generates_entanglement)
```

最低要求：

- 若通过局域媒介生成纠缠，必须说明媒介非经典层级；
- 不能直接把 BMV 升级成“量子时空证明”。

传播核近似：

```text
Delta phi_T = J_A^T K_T J_B
```

### 3. Hybrid dynamics / 混合动力学块

```text
J_hybrid[T] = penalty(non_CP_or_signaling)
            + penalty(deterministic_naive_closure)
            + cost_noise_diffusion[T]
```

最低要求：

- deterministic naive closure 不合格；
- 存活路线必须显式支付 stochasticity / decoherence / diffusion 代价。

传播核表达：

```text
K_T -> K_T + eta_T
J_noise[T] = dist_delta(D^T eta_T J, Im M_cross)
```

### 4. Black-hole / Page curve 块

```text
J_BH[T] = dist_delta(S_rad^T(t), S_Page(t))
        + penalty(unmodified_J_BH_four_assumptions)
```

最低要求：

- 恢复 Page curve；
- 或明确说明修改 `J_BH={Hawking_thermal, Complete_evaporation, Unitarity, No_new_entropy_rule}` 中哪条假设。

这个块不能由 `D^T K J` 自动给出。它需要 entropy functional / Hilbert-space factorization / island-like rule。

### 5. Observable map / 可观测桥接块

```text
J_obs[T] = penalty(no_detector_response)
         + penalty(no_experimental_dictionary)
```

最低要求：

- 不允许只有形式方程；
- 必须给出 detector response、phase、entropy 或等价可观测量。

### 6. Frame / 协变一致性块

```text
J_frame[T] = penalty(frame_dependent_predictions)
```

最低要求：

- BMV/弱场相位、测量源项、强引力熵规则在参考系变化下不能互相矛盾；
- 该块在 S5 中是“可选第六维”，这里确认应升为正式块。

## 与 S6 公式的关系

S6 的公式应作为 `J_obs` 里的一个实现模块，而不是完整 `J_unify`：

```text
J_obs^CS[T;D,J] = dist_delta(D^T(K_i-K_j)J, Im M_cross)
```

因此：

```text
J_unify[T] =
(
  J_PG[T],
  J_BMV[T],
  J_hybrid[T],
  J_BH[T],
  J_obs^CS[T;D,J],
  J_frame[T]
)
```

## 确认结论

**确认 1：** `J_unify^CS[D,J] := dist_delta(D^T(K_i-K_j)J, Im M_cross)` 是合法的 detector-response 实现模块。

**确认 2：** 它不是完整统一公式判据，因为它缺少 Page curve / entropy block 和 frame consistency block。

**确认 3：** 完整可确认的公式应是块矩阵 `J_unify[T]`，其中 `J_obs^CS` 只是第五块的一种实现。

**确认 4：** 当前 LP7 结论仍是“有边界”：我们确认了候选统一公式的准入判据，而不是确认了某个具体统一公式已经成立。

## 否证尝试

把 `J_unify[T]` 当成单一公式去验证，会失败在三处：

1. **对象混杂**：`J_PG`, `J_BMV`, `J_hybrid`, `J_BH` 属于不同物理层，不能靠同一个标量度量无歧义比较。
2. **缺少共同动力学**：六块之和只是一组约束，不是一个演化方程或作用量。
3. **尺度不一致**：Page curve、纠缠见证、测量源项、detector response 不共享同一可观测字典，必须先经过中间层。

因此，`J_unify` 作为“统一公式”是假的；它作为“统一判据接口”是真的。

## 中间层

真正的中间层不是公式本体，而是**操作性通道层**：

```text
I[T] = (Φ_source, Φ_mediator, Φ_noise, Φ_entropy, Φ_obs, Φ_frame)
```

其中：

- `Φ_source` 负责 S1 的分支源项选择；
- `Φ_mediator` 负责 S2 的媒介/相位/纠缠通道；
- `Φ_noise` 负责 S3 的 stochastic / diffusion 代价；
- `Φ_entropy` 负责 S4 的 Page curve / island 类规则；
- `Φ_obs` 负责 detector-response 映射；
- `Φ_frame` 负责参考系一致性。

这层才是 LP7 各子题的共同数学对象。`J_unify` 应该看成对 `I[T]` 的判据，而不是反过来。

## 下一步

若继续推进，应做 LP7 综合收敛：

1. 把 S1-S6 的 K 条目重排为 `J_unify` 六块；
2. 明确哪些块已有 L2，哪些块仍是 L3；
3. 判断是否存在任何现有候选理论同时通过六块。
