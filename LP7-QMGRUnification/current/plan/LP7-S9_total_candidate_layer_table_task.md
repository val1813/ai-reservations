# LP7-S9 任务书：总候选分层表

生成时间：2026-06-01

## 题目

LP7-S9：总候选分层表。

## 目标

把 LP7 现有讨论过的候选理论类型，逐一投影到中间操作层 `I[T]`，明确它们分别在哪些块上成立、在哪些块上失败。

本 Phase 不再争论“是否存在统一公式”这种总口号，而是直接做候选对照表：

```text
Theory T -> I[T] -> J_unify[I[T]]
```

## 北极星

S9 不负责证明某个候选已经统一成功。

它只负责回答：

1. 哪些候选能把 `I[T]` 六块写全；
2. 哪些候选只能覆盖其中一部分；
3. 哪些候选在 `J_frame` 或 `J_entropy` 处必然断裂；
4. 是否存在一个现成候选可作为下一轮深挖对象。

## 候选池

优先比较以下类型：

1. `T_source`：Page-Geilker 式半经典源项候选；
2. `T_mediator`：BMV/媒介非经典候选；
3. `T_hybrid`：经典-量子混合动力学候选；
4. `T_entropy`：Page curve / island-like 候选；
5. `T_obs`：因果集传播子 detector-response 候选；
6. `T_frame`：带显式帧一致性约束的候选。

## 最小验证

1. 为每个候选写出 `I[T]` 的六块覆盖情况。
2. 判断 `J_unify[I[T]]` 的硬失败块。
3. 标出“部分通过但不能统一”的候选。
4. 选出下一轮最值得深挖的单一候选类型。

## 预期输出

- `current/A/LP7-S9_phase1.md`
- `current/B/LP7-S9_independent_check.md`
- `current/plan/LP7-S9_integration.md`

## 预期结论

有边界。

## 下一步

▶️ 下一步：执行 LP7-S9 的 A 正规推导，先把候选类型投影到 `I[T]` 总表。
