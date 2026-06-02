# Phase 3 A4：原始 QLIF 新任务边界

## 目标
明确：如果继续研究原始 QLIF，必须作为新任务启动，不能复用 DR-NHDD 的结论。

## 新任务要求
原始 QLIF 任务必须实现：

1. 构造子系统约化密度矩阵 `rho_A(t)`
2. 计算 `S_A(t)=-Tr rho_A log rho_A`
3. 构造 frozen-B evolution
4. 计算 `dS_A/dt - dS_A^{freeze B}/dt`
5. 比较左右方向

## 与 DR-NHDD 的关系
DR-NHDD 可作为预筛：
- 选择参数区
- 选择填充率区间
- 预测可能出现方向性分段的位置

但 DR-NHDD 不能替代 QLIF。

## 新任务命名建议
若继续，命名为：

`LP4-S2b_Entropy-QLIF`

## 当前项目处理
当前项目应收束为：

“原始不变量命题失败；发现 DR-NHDD 作为新诊断量。”

如果要做原始 QLIF，就开 S2b，不在当前结果中偷换。
