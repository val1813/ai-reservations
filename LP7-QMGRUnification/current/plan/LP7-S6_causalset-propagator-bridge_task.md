# LP7-S6 任务书：因果集传播子路线对接

生成时间：2026-06-01

## 题目

LP7-S6：因果集传播子路线对接。

## 目标

评估现有 v7-v13 因果集 `J_ij[D,J]` 是否能作为 LP7-S5 统一公式候选判据矩阵的一个实现模块。

## 北极星

不是证明因果集路线已经统一量子力学和广义相对论，而是判断：

> v7-v13 的传播子差异、detector response 与共同参数空间投影，能否转写成 LP7 的统一判据模块 `J_unify` 的一个因果集实现。

## 输入边界

可用：

- v7-v12 已通过的传播子非唯一性与 detector response 结构。
- v13 的任务书、物理量身份证、研究计划。
- v13 B 单边推导只能作为“候选线索”，不得升级为知识库结论。

禁止：

- 不得把 v13 B 单边结论写成已验证。
- 不得声称 `J_ij[D,J]` 已经完成数值验证。
- 不得声称 causal set propagator route 已经给出统一公式。

## 最小验证

1. Page-Geilker：能否把 branch-sourced vs expectation-sourced 的差异写成 detector response 差。
2. BMV：能否把 mediator-induced phase / entanglement witness 写成 Green function / detector response 差。
3. S3：能否把 stochastic/diffusion cost 写成 response kernel 的噪声层或共同参数空间外分量。
4. v13：能否把 5 propagation constructions 的 `J_ij[D,J]` 作为 `J_unify` 的 causal-set realization。

## 预期输出

- A 正规推导：`current/A/LP7-S6_phase1.md`
- B 独立检查：`current/B/LP7-S6_independent_check.md`
- PI 审核：`synthesis/PI审核_S6.md`
- 总结：`synthesis/总结_S6.md`

## 下一步

▶️ 下一步：执行 LP7-S6 的 A 正规推导。

