# Phase 1 A4：bulk 极限判据

## 目标
判断三种 freeze 规则是否在 `L->∞` 后收敛到同一个方向标签。

## 1. 需要的极限顺序
不能直接取有限链 `L=4` 的符号。必须规定极限顺序：

1. 固定填充率 `rho = N/L`
2. 固定切分比例 `m/L -> x in (0,1)`
3. 取 `L -> ∞`
4. 再取时间窗极限或短时导数极限

定义：

`delta_f(L,N,t) = sign[Delta T_N^f(L,t)]`

其中 `f` 是 freeze 规则：
- `f=h`: hard-delete
- `f=d`: dephase-freeze
- `f=c`: clamped-source

候选 bulk 标签：

`nu_Q(rho) = lim_{t window} lim_{L->∞, N/L->rho} delta_f(L,N,t)`

## 2. 不变量候选成立条件
必须满足：

`nu_Q^h(rho) = nu_Q^d(rho) = nu_Q^c(rho)`

并且该值对以下扰动稳定：
- 局域 onsite 势扰动
- 小的 hopping 改变量
- 小的相互作用 `U` 改变量
- 不改变点隙/谱结构的 Lindblad 噪声

## 3. 与拓扑跳变的绑定
若 `nu_Q` 是拓扑不变量，则其跳变必须绑定到 bulk 结构变化：

`jump(nu_Q) => point gap closing / generalized Brillouin-zone winding change / Liouvillian spectral transition`

若跳变只对应：
- 初态换了
- 时间窗换了
- 切分位置换了
- freeze 规则换了

则不是拓扑跳变。

## 4. 当前可得判断
从定义结构看，三种 freeze 在 finite L 上不必一致。若它们要在 bulk 极限一致，必须有一个强条件：

跨区 freeze 只改变边界局域项，而 `Delta T_N` 的符号由 bulk 非互易性决定。

也就是说，必须证明 freeze 规则差异是 `O(1/L)`。

## 5. A侧命题
A4 给出一个可检验命题：

`|Delta T_N^h - Delta T_N^d| / |Delta T_N^full| -> 0`

且

`|Delta T_N^h - Delta T_N^c| / |Delta T_N^full| -> 0`

当 `L->∞`、`N/L=rho` 固定时成立。

若这两个极限为 0，则 freeze-rule independence 成立。

## 6. A侧当前结论
现在不应宣称 QLIF 已是不变量。正确表述是：

QLIF 具有成为 bulk 方向性不变量的候选条件，当且仅当三种 freeze 差异在热力学极限中消失。
