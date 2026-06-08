# INSPECTOR_B_round1

输入文件：`D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\current\B\round1.md`

检查协议：按 `D:\Claude\ai-reservations\ai\INSPECTOR.md` 的 Q1-Q6 执行。这里只做推导校对，不评价发表价值，不做 REVIEWER 工作。

## INSPECTOR_CHECK 1：单位相位轨迹 / 圆柱而非光锥

### Q1 量纲校对

- `x(t)=ell cos(omega t)`：左边 SI 单位 m；右边 `ell` 为 m，`omega t` 为无量纲，匹配。
- `y(t)=ell sin(omega t)`：左边 SI 单位 m；右边 `ell` 为 m，`omega t` 为无量纲，匹配。
- `T=t`：左边时间坐标，右边 s，匹配；若使用 Minkowski 量纲坐标 `(x,y,cT)`，`cT` 为 m。
- 切向 null 条件 `ell^2 omega^2 = c^2`：左边 `(m^2)(s^-2)=m^2 s^-2`；右边 `m^2 s^-2`，匹配。
- 曲面方程 `x^2+y^2=ell^2`：左边 `m^2`；右边 `m^2`，匹配。
- 对比命题 `x^2+y^2=c^2 T^2`：左边 `m^2`；右边 `m^2 s^-2 * s^2=m^2`，量纲匹配。
- 超越函数自变量：`omega t` 无量纲；`cos`、`sin` 合法。

结论：量纲通过。

### Q2 符号/方向校对

手动代入：

- 单根轨迹满足 `x^2+y^2=ell^2`，半径固定。
- 相位平移族 `x=ell cos(omega t+phi)`, `y=ell sin(omega t+phi)` 对任意 `t` 的截面仍为半径 `ell` 的圆，因此族面为圆柱。
- 光锥截面满足 `x^2+y^2=c^2T^2`，半径随 `|T|` 线性变化。

方向结论“单根单位螺旋或相位平移族自然给出圆柱，不给出光锥”正确。

### Q3 循环论证校对

本检查未使用实验数据；验证输入是显式参数化和 Minkowski 度规。结论由代入方程得到，不是由待证命题生成的数据回填。未发现循环论证。

### Q4 量级鸿沟标记

没有 `10^N` 与 `10^M` 型量级估算。无量级鸿沟。

### Q5 代数验算

速度：

```text
dx/dt = -ell omega sin(omega t)
dy/dt =  ell omega cos(omega t)
d(cT)/dt = c
```

切向 null：

```text
c^2 - (dx/dt)^2 - (dy/dt)^2
= c^2 - ell^2 omega^2[sin^2(omega t)+cos^2(omega t)]
= c^2 - ell^2 omega^2
```

故 null 切向条件为 `ell^2 omega^2=c^2`，正确。

轨迹面：

```text
x^2+y^2 = ell^2[cos^2(omega t)+sin^2(omega t)] = ell^2
```

不是 `x^2+y^2=c^2T^2`。代数通过。

### Q6 判定

通过。无阻断；无警告。

## INSPECTOR_CHECK 2：Hopf/null-spinor 二次映射

### Q1 量纲校对

- `k^mu = xi^\dagger sigma^mu xi`：Pauli 矩阵无量纲，`k^mu` 的量纲为 `xi` 的模平方。若 `xi` 未定标，则 `k^mu` 是自旋子二次量；若要解释为长度坐标或动量坐标，必须额外给出统一物理尺度。
- `k_mu k^mu=0`：各项均为 `|xi|^4`，匹配。
- `xi -> e^(i alpha) xi`：`alpha` 必须无量纲，合法。

结论：数学量纲通过；物理定标需显式保留。

### Q2 符号/方向校对

令 `a=|z1|^2`, `b=|z2|^2`, `q=z1^*z2`。则空间三向量平方为：

```text
(2Re q)^2 + (2Im q)^2 + (a-b)^2
= 4|q|^2 + (a-b)^2
= 4ab + a^2 - 2ab + b^2
= a^2 + 2ab + b^2
= (a+b)^2
```

在签名 `(+---)` 下 `k_mu k^mu=0`。且 `k^0=a+b>0` 对 `xi != 0` 成立。

整体相位：

```text
(e^(i alpha)xi)^\dagger sigma^mu (e^(i alpha)xi)
= xi^\dagger e^(-i alpha) sigma^mu e^(i alpha) xi
= xi^\dagger sigma^mu xi
```

方向结论“光锥可由 Hopf/null-spinor 二次映射得到；整体 U(1) 相位是纤维冗余，不是横向坐标”正确。

### Q3 循环论证校对

验证数据不是实验数据，而是 Pauli 矩阵恒等式与 Hopf 商结构。输入假设为 Weyl spinor 和 Minkowski 签名，结论为由二次映射落在 null cone 上。未发现“用待证光锥数据生成验证数据”的循环。

### Q4 量级鸿沟标记

没有数值量级估算。无量级鸿沟。

### Q5 代数验算

核心展开：

```text
k_mu k^mu
= (a+b)^2 - 4|q|^2 - (a-b)^2
= (a^2+2ab+b^2) - 4ab - (a^2-2ab+b^2)
= 0
```

其中 `|q|^2=|z1^*z2|^2=|z1|^2|z2|^2=ab`。代数通过。

已知极限：

- `z2=0` 时，`k=(|z1|^2,0,0,|z1|^2)`，null。
- `z1=0` 时，`k=(|z2|^2,0,0,-|z2|^2)`，null。
- `z1=z2` 且实数时，`k=(2z^2,2z^2,0,0)`，null。

### Q6 判定

通过，有警告：

- 警告：`k^mu` 若被解释为物理长度坐标或动量坐标，必须显式给出尺度定标；当前文本已提示“未定标时为自旋子二次量”，可继续。

## INSPECTOR_CHECK 3：Hopf/contact/symplectization

### Q1 量纲校对

- `S^3/U(1)=CP^1=S^2`：拓扑/微分几何同构，无 SI 量纲。
- `alpha = Im(z^\dagger dz)`：在单位 `S^3` 上可作无量纲 contact form；若 `z` 带物理量纲，则需要归一化。当前上下文为标准 Hopf contact structure，量纲一致。
- `alpha(R_alpha)=1`：左边无量纲，匹配。
- `i_R d alpha=0`：二形式收缩为一形式，零一形式，类型匹配。
- `C^2\{0}/U(1) ~= R_+ x S^2`：维数与拓扑匹配。

结论：量纲/类型通过。

### Q2 符号/方向校对

标准 `S^3` 上取 `z_j=r_j e^{i phi_j}`，则：

```text
alpha = Im(sum conj(z_j) dz_j) = sum r_j^2 d phi_j
```

整体相位流的向量场为 `R = partial_phi1 + partial_phi2`。在 `S^3` 上 `r_1^2+r_2^2=1`，故：

```text
alpha(R)=r_1^2+r_2^2=1
```

且该整体相位流为 Hopf 纤维方向，商掉后得到 `CP^1=S^2`。方向结论“相位纤维是 null 方向的前像/纤维，而不是光锥面本身”正确。

### Q3 循环论证校对

该步验证使用标准 Hopf fibration、contact form 与商空间结构。没有用构造出的光锥形状反过来证明 Hopf 商；未发现循环论证。

### Q4 量级鸿沟标记

没有数值量级估算。无量级鸿沟。

### Q5 代数验算

维数：

```text
dim_R(C^2\{0}) = 4
dim_R(U(1)) = 1
dim_R((C^2\{0})/U(1)) = 3
dim_R(R_+ x S^2) = 1 + 2 = 3
```

分解：

```text
C^2\{0} ~= R_+ x S^3
(R_+ x S^3)/U(1) ~= R_+ x (S^3/U(1)) ~= R_+ x S^2
```

与去顶点未来 null cone 的结构一致。代数/类型通过。

### Q6 判定

通过，有警告：

- 警告：`alpha = Im(z^\dagger dz)` 的标准 contact 解释依赖单位 `S^3` 或归一化自旋子；若后续给 `z` 加物理量纲，需同步重写或归一化 contact form。

## INSPECTOR_CHECK 4：单相位维数不足

### Q1 量纲校对

- `dim S^1=1`、`dim S^3=3`、`dim(R_+ x S^2)=3`：维数为无量纲整数，类型匹配。
- `S^1 x R` 维数 `1+1=2`：类型匹配。

结论：类型通过。

### Q2 符号/方向校对

对光滑流形：

```text
dim(S^1 x R) = 2
dim(R_+ x S^2) = 3
```

二维光滑参数域不能通过无奇异局部坐标覆盖三维光滑流形。方向结论“单相位螺旋维数不足；至少需要二分量复自旋子或等价三维 contact 总空间”对 3+1 去顶点光锥成立。

### Q3 循环论证校对

验证输入为流形维数与光滑覆盖要求，结论为维数不足。未发现循环论证。

### Q4 量级鸿沟标记

没有数值量级估算。无量级鸿沟。

### Q5 代数验算

维数计算：

```text
dim(S^1 x R) = 1 + 1 = 2
dim(R_+ x S^2) = 1 + 2 = 3
```

若目标是 3+1 Minkowski 中的去顶点未来光锥，该维数阻断正确。

已知退化检查：

- 若只讨论 2+1 光锥面，去顶点光锥维数为 2，此处“维数不足”不再单独构成阻断。
- 但 INSPECTOR_CHECK 1 已给出圆柱方程 `x^2+y^2=ell^2` 与 2+1 光锥方程 `x^2+y^2=c^2T^2` 不同，因此原“单位圆柱螺旋包络面严格等价于光锥面”仍不成立。

### Q6 判定

通过，有警告：

- 警告：维数阻断需限定为 3+1 去顶点光锥 `R_+ x S^2`。若后续文本改谈 2+1 光锥，不能继续用“2 维不能覆盖 3 维”作为阻断理由，需回到圆柱/圆锥方程差异。

## 阻断/警告汇总

阻断：无。

警告：

1. `k^mu = xi^\dagger sigma^mu xi` 若被解释为物理长度坐标或动量坐标，必须显式给出尺度定标；未定标时只能称为自旋子二次量。
2. `alpha = Im(z^\dagger dz)` 的标准 contact 解释依赖单位 `S^3` 或归一化；若 `z` 后续带物理量纲，需同步归一化。
3. `S^1 x R` 维数不足的阻断只对 3+1 去顶点光锥成立；对 2+1 情形应改用 CHECK 1 的圆柱/圆锥方程差异。

## 最终综合判定

INSPECTOR 通过。B round1 的四个 `INSPECTOR_CHECK` 在量纲、符号/方向、循环论证、量级鸿沟和代数验算上未发现阻断错误。可继续，但上述警告需在后续推导中显式标注，不能把未定标的 spinor 二次量直接偷换成物理坐标或动量，也不能把 3+1 维数论证误用于 2+1 目标。

## 本轮改动文件

`D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\synthesis\inspector_B_round1.md`
