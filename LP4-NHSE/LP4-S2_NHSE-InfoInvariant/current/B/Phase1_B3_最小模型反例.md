# Phase 1 B3：最小模型反例

## 目标
证明最小模型中的方向标签可能不是 freeze-rule independent。

## 反例思路
### 反例 1：hard-delete 与 dephase-freeze 不一致
如果 hard-delete 得到 `Delta T_N > 0`，而 dephase-freeze 得到 `Delta T_N < 0` 或接近 0，
则方向标签来自 freeze 规则，而不是系统本体。

### 反例 2：clamped-source 产生伪平台
如果 clamped-source 因为固定源项而得到稳定正号，但只要换初态就翻转，
则所谓平台只是输入约定。

### 反例 3：U 驱动的局域关联伪装成拓扑跳变
在小 `L` 下，`U` 改变局域关联即可让 `Delta T_N` 跳变。
这不等于 bulk 拓扑相变。

### 反例 4：sector 变化本身就是主要效应
若 `N=1` 与 `N=2` 的方向标签完全不同，而且没有可解释的平台结构，
则 sector dependence 说明它不是 sector-independent 不变量。

## B侧当前判断
最小模型极可能给出：`QLIF` 是一个对 freeze 规则敏感的方向性量，而不是稳定拓扑标签。

## 需要 A 回答
A 必须证明三种 freeze 的差异只是在有限尺寸上出现，并在 `L->∞` 时收敛到同一标签。
