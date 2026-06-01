# Phase 1 A3：最小模型对照

## 目标
在最小可算例子里检验 QLIF 是否具备 freeze-rule independent 的方向性标签。

## 模型
取 `L=4`，固定 `N=1` 或 `N=2` sector。

Hamiltonian:
`H = - sum_{j=1}^{3} (t_R c_{j+1}^\dagger c_j + t_L c_j^\dagger c_{j+1}) + U sum_{j=1}^{3} n_j n_{j+1}`

切分：
- `X = {1,2}`
- `Y = {3,4}`

## 三种 freeze
### 1. hard-delete
删除跨边界 hopping 与跨区 jump。

### 2. dephase-freeze
保留边界上的粒子数背景，但去掉跨区相干项。

### 3. clamped-source
固定 `X` 的约化态为静态输入，`Y` 只感受固定源项。

## 需要比较的量
`Delta T_N = T_N(X -> Y) - T_N(Y -> X)`

比较对象：
- 符号
- 零点位置
- 对 `t_L/t_R` 的依赖
- 对 `U` 的依赖

## A侧预期
如果三种 freeze 在 bulk-like 参数区给出相同方向标签，则可以把它当作不变量候选。

## A侧风险
如果三种 freeze 给出不同方向标签，则说明定义依赖建模约定，QLIF 不能直接作为拓扑不变量。

## 下一步
把这个最小模型写成表格式判据，交给 B 侧逐条攻击。
