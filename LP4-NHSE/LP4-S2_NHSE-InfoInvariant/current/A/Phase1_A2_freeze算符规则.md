# Phase 1 A2：HN-Hubbard 中的 freeze 算符规则

## 目标
把 QLIF 的 `freeze X` 操作写成可计算的算符规则，避免停留在语义层。

## 1. 模型
取一维 Hatano-Nelson-Hubbard 链：

`H = - sum_j (t_R c_{j+1}^\dagger c_j + t_L c_j^\dagger c_{j+1}) + U sum_j n_j n_{j+1}`

可选开放系统项：

`L_j = sqrt(G) (c_j + i alpha c_{j+1})`

固定粒子数 sector：

`H_N = span{|n_1,...,n_L>, sum_j n_j=N}`

## 2. 子区切分
令 `X = {1,...,m}`，`Y = {m+1,...,L}`。

把生成元分解为：

`G = G_X + G_Y + G_boundary`

其中：
- `G_X` 只含 `X` 内部项
- `G_Y` 只含 `Y` 内部项
- `G_boundary` 含跨越切分的 hopping、interaction 或 Lindblad jump

## 3. freeze X 的最小规则
定义：

`G^{freeze X -> Y} = G_Y + Pi_X(G_X)`

其中 `Pi_X(G_X)` 对 `Y` 的约化动力学没有直接作用，只保留 `X` 的静态背景约束。

更具体地，对 Hamiltonian 部分：

1. 删除跨边界 hopping：
   `c_{m+1}^\dagger c_m` 和 `c_m^\dagger c_{m+1}` 不进入 `Y` 的演化。

2. 跨边界相互作用替换为条件背景：
   `U n_m n_{m+1} -> U <n_m>_X n_{m+1}`

3. `X` 内部 Hamiltonian 对 `Y` 的约化演化只通过固定背景密度进入。

对 Lindblad 部分：

1. 删除同时支撑在 `X` 与 `Y` 的 jump operator：
   若 `supp(L_j) ∩ X != empty` 且 `supp(L_j) ∩ Y != empty`，则 `L_j` 不参与 freeze 后的 `Y` 演化。

2. `Y` 内部 jump operator 保留。

3. `X` 内部 jump operator 只改变 `X` 态，不直接进入 `Y` 熵变化率。

## 4. QLIF 定义
定义目标区熵：

`S_Y(t) = -Tr rho_Y(t) log rho_Y(t)`

则：

`T_N(X -> Y; t) = dS_Y^full/dt - dS_Y^{freeze X}/dt`

方向性差：

`Delta T_N(t) = T_N(X -> Y; t) - T_N(Y -> X; t)`

## 5. 这个定义的优点
- 可程序化：只需要构造 full generator 与 freeze generator。
- 可 sector-resolved：每个 `N` 独立计算。
- 可被 B 侧攻击：删除跨边界项可能人为抹掉 NHSE 的方向性传播。

## 6. A侧当前判断
这是一个可计算定义，但它仍然偏动力学。要进一步成为不变量，必须证明 `sign(Delta T_N)` 在 bulk 极限中形成稳定平台。

## 7. 下一步
构造最小 `L=4, N=1/2` 的符号级反例测试，比较 OBC/PBC 与不同初态下的 `Delta T_N`。
