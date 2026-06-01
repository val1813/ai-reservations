# Phase 1 B5：PBC / OBC 攻击

## 目标
证明 PBC/OBC 分流本身就可能让 QLIF 退化成边界诊断量。

## 1. PBC 下的空洞性
若 PBC 下 `Delta T_N` 很弱，说明 QLIF 依赖边界开启。

那么它不是 bulk 拓扑不变量，而是边界条件敏感量。

## 2. OBC 下的扩展性
NHSE 典型地在 OBC 下出现边界堆积，影响可扩展到全链。
因此“边界局域修正”在 NHSE 中经常不成立。

## 3. sector 交叉破坏一致性
即使 PBC 下不同 sector 给出相同标签，只要 OBC 下 sector 之间出现系统性分裂，
sector-independent 的说法就站不住。

## 4. 结论
PBC/OBC 分流并不能拯救 QLIF 的不变量地位。
它最多说明：
- PBC 下可定义某种更平滑的 bulk 响应
- OBC 下则是边界敏感的方向性探针

## 5. B侧要求
A 必须证明：
- OBC 下的分裂不影响 bulk 标签
- 边界敏感性可被单独剥离
- sector 变化不引入新的标签翻转

若不能，QLIF 只是诊断量。
