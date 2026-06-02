# LP7-S2 PI 整合记录

生成时间：2026-06-01

## 当前状态

已完成：

- `current/plan/LP7-S2_BMV_locality_boundary_literature.md`
- `current/plan/LP7-S2_BMV_locality_boundary_task.md`
- `current/A/LP7-S2_phase1.md`
- `current/B/LP7-S2_independent_check.md`

待完成：

- 更新 `current/plan/当前状态.md`

## A 结论摘要

结论类型：有边界。

A 的核心判断：

BMV 只能在 locality、无直接探针-探针耦合、以及对 classical mediator 可观测结构的限制下推出“媒介非经典”。一旦放宽这些假设，尤其是允许 non-local-tomographic mediator，便不能直接升级到“量子时空”。

## B 结论摘要

B 的核心判断：

BMV 类实验能排除一类局域、可完全经典层析、且无法生成纠缠的媒介模型，但不能直接推出“引力的时空叠加是必要的”。最强结论是“在明确假设下，媒介非经典”。

## 待仲裁问题

| 问题 | A 结论 | B 结论 | PI 处理 |
|---|---|---|---|
| BMV 的最小假设是否包含 local tomography | 是 | 是 | 收紧：作为排除标准 classical mediator 的附加结构假设，不写成唯一不可替代公理 |
| non-local-tomographic classical mediator 是否为真实逃逸 | 是 | 是 | 一致，作为反例栏保留 |
| BMV 是否可直接推出“量子时空” | 否 | 否 | 一致，只能推出媒介非经典 |
| reference-frame 一致性是否应单列 | 可选边界 | 应单列 | 登记为边界项，留给 S3/S5 统一矩阵 |

## GATE 检查

- GATE 1 文献库/反例栏：通过。`LP7-S2_BMV_locality_boundary_literature.md` 已列核心文献和反例栏。
- GATE 2 审稿人/Reviewer：本阶段不是收官总审，未触发。
- GATE 3 B 独立推导：通过。`current/B/LP7-S2_independent_check.md` 已存在并声明独立性。
- GATE 4 攻击闭合：通过到 Phase 1 粒度。剩余攻击项已登记为后续边界，不阻断 S2 结论。

## PI 结论

结论类型：**有边界**。

LP7-S2 关闭的不是“引力必须按标准量子场量子化”这个总命题，而是一个更窄的判据：在 locality、无直接探针耦合、以及标准 classical mediator 可观测结构同时成立时，经典媒介不能生成 BMV 纠缠。Vidal et al. 2025 说明 observable spacetime superpositions 不是必要条件，因此 S2 的安全表述是“BMV 支持媒介非经典”，不是“BMV 证明量子时空”。

## 下一步

▶️ 下一步：把 LP7-S2 登记为“有边界”，并推进 LP7-S3 经典-量子混合动力学 no-go 边界。
