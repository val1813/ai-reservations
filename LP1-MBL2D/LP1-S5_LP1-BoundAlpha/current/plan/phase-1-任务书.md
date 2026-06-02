# Phase 1 任务书 — LP1-S5_LP1-BoundAlpha

## A任务

把 `tau_MBL ~ exp(alpha L) * tau_0` 写成

`tau_MBL ~ exp(gamma * L_path(p_block)) * tau_0`

并用路径长度界把 `alpha` 变成 `gamma * lambda` 的区间。

## B任务

独立检查：

1. 多体协同隧穿是否只修正前因子
2. 下界是否足以保住 `tau >> tau_universe`

