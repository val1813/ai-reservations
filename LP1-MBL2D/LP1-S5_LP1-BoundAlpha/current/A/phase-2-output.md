# A博士 Phase 2 — 显式不等式版本

## 任务

把 Phase 1 的形式拆分推进为可引用的不等式。

---

## 1. 定义

令阻塞格点密度为 `p_b = p_block`，易热化格点密度为 `p_e = 1 - p_b`。

LP1-S1 的强无序稳定区对应：

`p_b > p_c`

等价于易热化簇处于子临界区：

`p_e < p_c`

热区若要继续增长，必须穿越一条由阻塞格点形成的对偶阻塞带。记最短有效穿越长度为：

`L_path(L; p_b)`

其中 `L` 是热区线性尺度。

---

## 2. 渗流几何界

由二维子临界渗流的指数衰减与对偶阻塞结构可得：

存在 `c_1(p_b), c_2(p_b), a_-(p_b), a_+(p_b) > 0`，使得对足够大的 `L`，

`P[a_-(p_b) L <= L_path(L; p_b) <= a_+(p_b) L] >= 1 - c_1(p_b) exp[-c_2(p_b) L]`

解释：

- 下界：穿越一个线性尺度为 `L` 的阻塞带，不可能只用亚线性步数完成。
- 上界：子临界易热化簇没有跨越箱体的长程连通，阻塞对偶路径以线性长度封闭热区前沿。

这个陈述只需要线性同阶，不需要精确最优常数。

---

## 3. 局域隧穿代价界

设每个阻塞步的量子隧穿率满足

`Gamma_step(j) <= Gamma_0 exp[-eta_j]`

并假设强无序窗口内存在统一界

`eta_- <= eta_j <= eta_+`

其中

`eta_j ~ 2 W_j / (g xi_loc)`

则一条长度为 `n` 的有效穿越路径满足

`Gamma_path(n) <= Gamma_0 exp[-eta_- n]`

从寿命角度：

`tau_path(n) >= tau_0 exp[eta_- n]`

同时，若允许最有利路径并使用 `eta_+` 作保守上界：

`tau_path(n) <= tau_0 exp[eta_+ n]`

---

## 4. 合并

在高概率事件上，

`tau_0 exp[eta_- a_-(p_b) L] <= tau_MBL(L) <= tau_0 exp[eta_+ a_+(p_b) L]`

因此可定义

`alpha_min(p_b,g,W,xi_loc) = eta_- a_-(p_b)`

`alpha_max(p_b,g,W,xi_loc) = eta_+ a_+(p_b)`

并得到：

`alpha in [alpha_min, alpha_max]`

---

## 5. 对 LP1-S1 的修正

原来的

`alpha ~ 5`

应改写为：

`alpha = eta_eff * a_eff(p_b)`，且在强无序稳定区有 `0 < alpha_min <= alpha <= alpha_max < infinity`。

数值 `[3,8]` 只能作为典型参数窗口，不能写成严格定理。

---

## 6. 关键结论

**K1.1候选：** 在 `p_block > p_c` 且局域隧穿代价有统一正下界时，随机强无序2D MBL的亚稳寿命满足高概率指数夹逼：

`tau_0 exp[alpha_min L] <= tau_MBL(L) <= tau_0 exp[alpha_max L]`

其中 `alpha_min > 0`。

