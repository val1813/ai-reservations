# Phase 2 A5：失败链整理与新对象命名

## 失败链
1. QLIF 可推广到多体 sector
2. 可以定义冻结因果量
3. 可以做 freeze-rule 对照
4. 但三种 freeze 并不稳定共用同一标签
5. PBC/OBC 分流后仍有边界敏感性
6. sector 扫描显示填充率分段
7. 平台与平台中心都不是全局稳定不变量

## 最终判断
原始命题失败：
“NHSE 作为定向信息信道的拓扑不变量能否统一描述 sector-dependent 行为？”

答案更接近：
不能作为 sector-independent 拓扑不变量统一描述，但可以作为 density-resolved directionality diagnostic 描述。

## 新对象命名
建议命名为：

`density-resolved directionality diagnostic (DRDD)`

其含义：
- 不是拓扑不变量
- 是对 NHSE 方向性在填充率和 sector 上的分段诊断量
- 可用于区分低填充正向区、高填充负向区与过渡带

## A侧保留的价值
DRDD 仍然是一个有用对象，因为它抓住了：
- freeze 依赖
- boundary 敏感性
- sector 结构
- density 分段

## A侧最终态度
不把它冒充为不变量。
保留失败链，单独命名新对象。
