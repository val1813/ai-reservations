# A博士 Phase 1 — LP1-S5_LP1-BoundAlpha

## 目标

把 `alpha ~ 5` 改写成可控上下界。

---

## 结论骨架

设

`tau_MBL(L) ~ tau_0 * exp(gamma * L_path(L))`

其中：

- `gamma` 是单步穿越一个“有效阻塞层”的最小代价
- `L_path(L)` 是从热区边界穿过阻塞网络到达下一可热化区的最短路径长度

若存在线性路径界

`lambda_- * L <= L_path(L) <= lambda_+ * L`

则立刻得到

`exp(gamma * lambda_- * L) <= tau_MBL / tau_0 <= exp(gamma * lambda_+ * L)`

因此

`alpha in [gamma * lambda_-, gamma * lambda_+]`

---

## Kesten型输入

在2D渗流对偶图中，Kesten式路径界给出的不是“任意长曲线都可忽略”，而是：

1. 只要 `p_block > p_c`，阻塞跨越事件的概率对箱体尺度指数衰减。
2. 条件在的最短跨越路径长度与系统线性尺度同阶。

这足够把 `L_path` 写成 `Theta(L)`，从而把 `alpha` 锁进线性区间。

---

## 当前可写结论

- `alpha` 不是自由漂移的经验常数，而是 `gamma` 与渗流几何因子的乘积。
- 只要 `p_block > p_c`，寿命仍然是 `exp(const * L)` 级别。
- 真正待补的是常数范围，而不是指数形式。

---

## 暂定卡点

1. `gamma` 的下界需要从局域隧穿率给出。
2. `lambda_-` / `lambda_+` 需要从更明确的渗流几何估计落地。

