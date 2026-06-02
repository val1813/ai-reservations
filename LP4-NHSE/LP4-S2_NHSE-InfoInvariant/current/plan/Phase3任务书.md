# Phase 3 任务书

## 目标
把“原始 QLIF”与“当前代理量 DRDD”严格分开，避免方法偷换。

## 已知事实
- 原始 QLIF：冻结发送子系统，比较目标子系统 von Neumann entropy 的变化率。
- 当前脚本：是方向性代理量，不是完整 QLIF。
- 之前的结论：关于 DRDD 的方向性分段成立，但不能直接冒充原始 QLIF 的不变量判据。

## Phase 3 任务
1. 写出原始 QLIF 的定义对照。
2. 写出我们当前 DRDD 与原始 QLIF 的差异。
3. 判断 DRDD 是否只是 transport proxy，而不是 causal-flow quantifier。
4. 若不能等同，则给出最终术语边界。

## 判别标准
### 支持等同
- DRDD 的 freeze 规则与原始 QLIF 的冻结机制一致
- DRDD 与 entropy-flow 在同一参数区给出相同标签
- 代理误差可控且可解释

### 支持降级
- DRDD 依赖不同的可观测量
- DRDD 不能还原为 entropy-flow
- DRDD 只是在输运层面反映方向性

## 预期结论
大概率是：
- 原始 QLIF = entropic causality quantifier
- DRDD = operational transport diagnostic

## 下一步
写定义对照，并把 Phase 2 结论重新归类。
