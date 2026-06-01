# Phase 1 A 定义收紧：QLIF 与 sector 不变量

## 1. 原始锚点
原始 QLIF 的核心操作是：
- 冻结 / 去掉某个发送子系统
- 比较目标子系统的 von Neumann entropy 变化率
- 用“有无冻结”的差值刻画因果影响

这意味着 QLIF 不是几何量，也不是谱量，而是一个“受冻结机制定义的动力学因果量”。

## 2. 多体推广
对固定粒子数 sector `H_N`，定义子区 `X, Y` 的 sector 限制密度矩阵：

`rho_N^{XY}(t) = Tr_rest rho_N(t)`

候选方向性量：

`T_N(X -> Y; t) = [d/dt S(rho_{N,Y}(t))] - [d/dt S(rho_{N,Y}^{freeze X}(t))]`

其中 `freeze X` 表示按 Liang 方案冻结发送子区 `X` 的相关作用，只保留与 `Y` 无关的演化分量。

## 3. sector-independent 候选不变量
若要变成拓扑不变量，至少要把方向性量离散化为：

`nu_Q = lim_{L->∞} sign( T_N(L->R) - T_N(R->L) )`

或更强地：

`nu_Q = lim_{L->∞} Phi(Delta T_N)`

其中 `Phi` 必须是对连续缩放不敏感的离散映射。

## 4. 需要额外证明的四件事
1. 对初态不敏感
2. 对时间窗不敏感
3. 对归一化不敏感
4. 对 sector 选择只发生结构性变化，而不是任意漂移

## 5. A侧当前判断
QLIF 可以自然升级成 sector-resolved directionality，但还不能直接升级成拓扑不变量。

## 6. A侧下一步
把 `freeze` 方案写成可用于 HN-Hubbard 的显式算符操作，再看能否定义 bulk 稳定标签。
