# Phase 1 A5：PBC / OBC 分流判据

## 目标
把 freeze-rule independence 的检验拆成 PBC 与 OBC 两条线，避免把边界敏感性混成 bulk 结论。

## 1. 判别表
### PBC
若在 PBC 下三种 freeze 的 `Delta T_N` 收敛到同一标签，则说明方向性主要由 bulk 非互易性控制。

### OBC
若在 OBC 下三种 freeze 的 `Delta T_N` 不收敛，但差异只出现在边界局域窗口，则仍可视为边界修正。

若 OBC 下差异扩展到 bulk 区并随 `L` 保持，则不能称为局域修正。

## 2. 需要验证的结构
1. PBC 下 `nu_Q^h = nu_Q^d = nu_Q^c`
2. OBC 下 `nu_Q^h, nu_Q^d, nu_Q^c` 的差异是否只存在于边界附近
3. 差异是否在 `L->∞` 时消失

## 3. A侧判定标准
QLIF 仍可作为不变量候选，当且仅当：
- PBC 与 OBC 的差异能被清晰解释为边界效应
- 三种 freeze 的 bulk 标签一致
- 该一致性在 sector 改变时保留结构

## 4. A侧当前观点
如果 PBC 收敛、OBC 不收敛，这说明 QLIF 具有边界敏感性，但不必立刻判死刑。
它可能是“bulk 候选不变量 + 边界修正强”的对象。

## 5. 下一步
把 `PBC/OBC` 的判别写成表格式问句，交给 B 侧逐项攻击。
