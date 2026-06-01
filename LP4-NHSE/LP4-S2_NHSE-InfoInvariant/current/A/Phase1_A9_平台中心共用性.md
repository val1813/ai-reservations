# Phase 1 A9：平台中心共用性

## 目标
检查平台中心 `rho*(L)` 是否在不同 sector、freeze 规则与边界条件下共用。

## 1. 定义
若平台区间为 `I_L=[rho_-(L), rho_+(L)]`，定义平台中心：

`rho*(L) = [rho_-(L)+rho_+(L)]/2`

## 2. sector-independent 的必要条件
若 QLIF 是 sector-independent 不变量，则应满足：

`lim_{L->∞} rho_h*(L) = lim_{L->∞} rho_d*(L) = lim_{L->∞} rho_c*(L)`

并且 PBC/OBC 下的差异可解释为边界修正。

## 3. 更强条件
平台中心还应与已知 bulk 结构变化点绑定，例如：
- point-gap closing
- generalized Brillouin zone winding change
- Liouvillian spectral transition

若 `rho*` 无法绑定到任何 bulk 结构，则平台中心只是经验拟合。

## 4. A侧可接受结果
可接受：
- `rho*` 共用，并与 bulk 谱结构变化一致
- OBC 有偏移，但偏移随 `L` 消失

不可接受：
- 三种 freeze 的 `rho*` 极限不同
- PBC/OBC 给出不同极限且差异不消失
- `rho*` 随 sector 选择无规律漂移

## 5. A侧当前结论
平台宽度和平台中心必须同时稳定。
只稳定宽度、不稳定中心，不足以支持不变量。

## 6. 下一步
B 侧攻击平台中心是否只是拟合参数。
