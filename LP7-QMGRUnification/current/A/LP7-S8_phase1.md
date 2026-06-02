# LP7-S8 Phase 1 — A 正规推导

生成时间：2026-06-01

## 0. 输入边界

本 Phase 只攻击 `J_frame` 的地位，不扩展新物理边界。

不声称：

- `J_frame` 已经被证明是新的物理作用；
- `J_frame` 与 `J_obs` 完全等价；
- `J_frame` 已经是统一理论中的终极第六公理。

## 1. `J_frame` 与 `J_obs` 的区别

`J_obs` 处理的是：

- 由理论到 detector response 的映射；
- 可观测差异；
- 传播子/核/噪声的外分量。

`J_frame` 处理的是：

- 不同描述帧下同一候选理论的判据是否保持一致；
- 是否存在“只在某一帧看起来通过”的假阳性；
- 判据本身是否具有可比性。

因此两者不等价。

`J_obs` 是“看得见什么”；
`J_frame` 是“在哪些描述下看见的结果还能互相对齐”。

## 2. 为什么不能并入完全同一块

若把 `J_frame` 完全并入 `J_obs`，会丢掉一个风险：

某些候选理论可能在一套 detector/source 约定下给出稳定输出，但在换帧或换描述后该输出不再是同一物理对象。

这不是普通的 observable 差异，而是判据可比性问题。

所以 `J_frame` 不应被简单删掉。

## 3. 但它也不是独立物理块

尽管 `J_frame` 不能删除，它也不应该被夸成新的物理结构。

原因：

- 它并不直接产生新的辐射、相位或熵项；
- 它只是约束已有判据是否可跨帧对照；
- 它更多是准入稳定性条件，而不是新的动力学方程。

## 4. 最小定位

`J_frame` 的最小内容可以写成：

`J_frame = consistency(observables under admissible frame changes)`

即它问的是：在允许的帧变换下，`J_PG/J_BMV/J_hybrid/J_BH/J_obs` 的结论是否保持同一物理含义。

## 5. 对总块矩阵的修正

`J_frame` 应保留在 `J_total` 中，但角色应从“疑似第六门槛”降格为“稳定性门槛”。

这意味着：

- 它能拒绝候选；
- 但不能单独确立候选；
- 它是元判据，不是主物理判据。

## 6. 结论类型

结论类型：**有边界**。

核心结论：

`J_frame` 不能被 `J_obs` 完全吸收，因为它约束的是跨帧可比性，而不是单一帧下的 detector response；但它也不是新的动力学块，更适合作为总块矩阵中的稳定性门槛，而非独立物理公理。

## 7. K 条目候选

K94 [⚠️ L3] `J_frame` 与 `J_obs` 不等价：前者约束跨帧可比性，后者约束单帧可观测差异。
  来源：LP7-S8 A/B 边界分析。
  适用条件：候选理论存在多帧/多描述比较需求。
  math_object：`consistency(observables under admissible frame changes)`
  data_access_level：derived
  验证状态：待 B 独立验证

K95 [⚠️ L3] `J_frame` 应作为元稳定性门槛保留，而不是新的动力学公理。
  来源：LP7-S8 A 推导。
  适用条件：统一候选需要跨帧可比。
  math_object：`frame-consistency constraint`
  data_access_level：derived
  验证状态：待 B 独立验证

## 8. 待 B 验证清单

1. `J_frame` 是否真的比 `J_obs` 多出新信息。
2. 是否存在候选理论能通过 `J_obs` 但失败于 `J_frame`。
3. `J_frame` 作为稳定性门槛是否会太弱。
