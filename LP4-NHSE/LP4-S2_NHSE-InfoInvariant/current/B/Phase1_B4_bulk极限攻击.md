# Phase 1 B4：bulk 极限攻击

## 目标
攻击 A4 的关键假设：freeze 规则差异是否真的只是 `O(1/L)`。

## 1. 主要攻击
在 NHSE 中，边界不是普通局域边界。OBC 下本征态整体堆积到边界，边界条件会重排整个谱和态分布。

因此跨区 freeze 的差异不必是 `O(1/L)`，可能是 `O(1)`。

## 2. hard-delete 的非局域后果
hard-delete 删除一个跨切分 hopping，在 Hermitian bulk 系统中可能只是边界切口。

但在非厄米 NHSE 中，一个切口可以改变 generalized Brillouin zone 的有效边界条件。其影响可能不是局域误差。

## 3. dephase-freeze 的相干性问题
dephase-freeze 保留密度背景但去掉相干项。NHSE 与非互易 hopping 的相干传播直接相关。

若相干项被去掉，`Delta T_N` 的方向性标签可能系统性偏向“无拓扑”。

## 4. clamped-source 的输入偏置
clamped-source 固定源区态。若源区态本身偏向左/右边界，则 `Delta T_N` 会继承输入偏置。

这不是 bulk 拓扑标签。

## 5. 关键反命题
B4 反命题：

`lim_{L->∞} |Delta T_N^h - Delta T_N^d| / |Delta T_N^full| != 0`

至少在 OBC NHSE 中可能成立。

若成立，则 QLIF 不具备 freeze-rule independent 的 bulk 标签。

## 6. B侧当前结论
在 NHSE 问题里，把 freeze 规则差异当作边界 `O(1/L)` 误差是不安全的。由于 NHSE 的边界敏感性，QLIF 更可能是 operational diagnostic，而不是拓扑不变量。

## 7. 对 A 的最低要求
A 必须把 OBC 与 PBC 分开：
- PBC 下检验 freeze 差异是否消失
- OBC 下检验 freeze 差异是否保持 `O(1)`

若只有 PBC 下收敛而 OBC 下不收敛，则 QLIF 不能分类 NHSE，只能分类 bulk 非互易驱动。
