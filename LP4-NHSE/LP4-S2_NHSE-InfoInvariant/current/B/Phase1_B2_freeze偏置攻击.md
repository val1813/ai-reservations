# Phase 1 B2：freeze 规则的偏置攻击

## 目标
检查 A2 的 `freeze X` 是否把方向性人为写进定义。

## 1. 删除跨边界 hopping 的偏置
A2 规则删除 `c_{m+1}^\dagger c_m` 和 `c_m^\dagger c_{m+1}`。在 NHSE 中，方向性正来自非互易 hopping 与边界条件的组合。

风险：
若 freeze 操作删除的正是承载方向性的项，则 `T_N` 反映的是“删掉方向性耦合后的差值”，不一定是拓扑因果流。

## 2. 跨边界相互作用的 mean-field 替换偏置
`U n_m n_{m+1} -> U <n_m>_X n_{m+1}` 会把量子关联降级为经典背景。

风险：
若 sector-dependent NHSE 的关键来自跨边界多体关联，则该 freeze 规则会系统性低估 sector 效应。

## 3. 删除跨区 Lindblad jump 的偏置
LP4-S1 的方向反转核心正是非局域 jump `L_j = sqrt(G)(c_j + i alpha c_{j+1})`。

若切分刚好穿过 `j,j+1`，A2 规则会删除此 jump。

风险：
QLIF 的方向性可能主要来自“跨区 jump 是否被删”，而非系统本身的拓扑结构。

## 4. 替代 freeze 检验
必须至少比较三种 freeze：

1. hard-delete：删除跨边界项
2. dephase-freeze：保留能量/粒子流，去掉相干项
3. clamped-source：固定 `X` 的一体密度矩阵，只允许 `Y` 响应

若三者给出不同 `sign(Delta T_N)`，则 QLIF 不是拓扑不变量。

## 5. B侧结论
A2 的规则可计算，但有强建模偏置。当前不能用它定义拓扑不变量，只能作为一类 operational diagnostic。

## 6. 必须进入卡点
freeze 规则依赖必须作为 active 卡点保留，直到三种 freeze 给出同一 bulk 标签。
