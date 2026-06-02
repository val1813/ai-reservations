# Phase 3 A2：DRDD 术语边界

## 目标
判断 DRDD 能否保留 “information-flow” 相关措辞，还是必须降级为 “transport diagnostic”。

## 1. 当前 DRDD 的定义来源
DRDD 来自：
- center-of-mass velocity proxy
- `DeltaT` 的方向性符号
- density-resolved 分段

它不是 von Neumann entropy 的流。

## 2. 可保留的术语
可以保留：
- directionality
- density-resolved
- diagnostic
- transport proxy

不应保留：
- topological invariant
- sector-independent invariant
- quantum Liang information flow
- entropy causality quantifier

## 3. 推荐命名
更严格的名称：

`density-resolved non-Hermitian directionality diagnostic (DR-NHDD)`

比 `DRDD` 更准确，因为它明确是非厄米方向性诊断，而不是信息流本体。

## 4. 与原始 QLIF 的关系
DR-NHDD 可以作为原始 QLIF 计算前的预筛选量：
- 如果 DR-NHDD 无分段，原始 QLIF 不太可能显示强方向结构
- 如果 DR-NHDD 有分段，原始 QLIF 仍需独立验证

## 5. A侧结论
DRDD 应进一步改名为：

`DR-NHDD`

避免与原始 QLIF 混淆。
