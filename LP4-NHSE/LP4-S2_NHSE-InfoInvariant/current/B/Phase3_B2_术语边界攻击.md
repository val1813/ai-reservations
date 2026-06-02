# Phase 3 B2：术语边界攻击

## 目标
确保 DRDD 不偷换回 QLIF 或拓扑不变量。

## 1. 为什么不能叫 information-flow
信息流在原始 QLIF 中有严格定义：entropy-rate difference under freezing。

DRDD 没有计算 entropy-rate。
因此叫 information-flow 会误导。

## 2. 为什么不能叫 invariant
DRDD 的符号随：
- density
- freeze
- sector
- boundary
变化。

这不是不变量。

## 3. 为什么可以叫 diagnostic
它确实诊断了非厄米系统中的方向性分段。
这个表述保守且准确。

## 4. B侧要求
所有后续文件中：
- 不再称 DRDD 为 QLIF
- 不再称其为 invariant
- 若要使用 QLIF，必须重新实现 entropy-flow 定义

## 5. B侧结论
推荐术语：

`density-resolved non-Hermitian directionality diagnostic (DR-NHDD)`
