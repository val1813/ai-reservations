# B博士 round3：contact/twistor holonomy 是否生成 optical twist

## §0 框架声明

本轮的跨学科跳跃：建筑学的“竖向交通核心/楼层动线” -> 主丛联络的 holonomy -> contact/twistor lift 中的相位联络。

借来的结构不是“建筑像时空”这种表面类比，而是一个严格区分：电梯井或楼梯核可以让人在闭合路线后带着一个方向/高度的 holonomy 回来，但它不自动改变楼层平面里的动线旋度。翻译到 LP23：`U(1)` 相位联络的曲率可以给出闭合回路干涉相位，但不自动生成 spacetime null congruence 的 optical twist。若要等同，必须额外给出一个把内部相位纤维识别为 screen bundle 旋转的结构；没有这个结构，映射失败。

本轮显式采用第2轮 INSPECTOR 要求的符号约定：

```text
metric = (+---)
sigma^0 = I
sigma^1 = [[0, 1], [1, 0]]
sigma^2 = [[0, -i], [i, 0]]
sigma^3 = [[1, 0], [0, -1]]

xi = sqrt(rho) e^{i psi}
     ( cos(chi/2),
       e^{i phi} sin(chi/2) )^T
```

于是

```text
k^mu = xi^\dagger sigma^mu xi
     = rho(1,
            sin chi cos phi,
            sin chi sin phi,
            cos chi).
```

后文所有“旋转方向/手征方向”只在此 `sigma_y` 与 `phi` 约定下陈述；若换成 round2 旧参数化，`n_y` 符号会翻转，但本轮结论不变。

--- INSPECTOR_CHECK ---
[公式] `k^mu=xi^\dagger sigma^mu xi=rho(1,sin chi cos phi,sin chi sin phi,cos chi)`，`k_mu k^mu=0`；`psi,chi,phi` 无量纲，`[k]=[rho]`。
[方向] 明确采用标准 `sigma_y` 和 `z2=e^{i phi}sin(chi/2)`，所以 `n_y` 为正号约定；整体相位 `psi` 不改 null direction。
[数据] 无实验数据；使用 Pauli bilinear 代数。
[假设] 平直局部 Lorentz 背景；`rho` 的物理定标另行指定。

## 跳跃1：相位曲率 `F=dA` 的对象类型不对

令相位 lift 写成

```text
D xi = d xi + i A xi,
F = dA.
```

这里 `A` 是 `U(1)` 线丛联络，`F` 是 `u(1)` 值二形式。它的直接可观测量是闭合回路相位

```text
Hol(C)=exp(i integral_C A),
```

或在干涉中出现的相位差。这个对象的靶空间是内部 `U(1)` 纤维。

而 null congruence 的扭转需要的是 spacetime 中 null direction field `k` 的非超曲面正交性。为了避免重复 A 路线的 optical scalar 推导，我只用 contact/Frobenius 判据写最小形式：

```text
twist exists only if the spacetime distribution orthogonal to k
has nonzero Frobenius obstruction, schematically k wedge dk != 0.
```

这里 `dk` 是 spacetime 方向场的变化；不是 `U(1)` 相位的曲率。除非额外规定 `A` 就是 screen frame 的旋转联络，`F` 和 `k wedge dk` 不在同一个几何对象类别里。

强反例很短：取平直时空中的恒定 null congruence

```text
k^mu = rho(1,0,0,1),
x^mu(s,u,v)=x_0^mu(u,v)+s k^mu.
```

同时在相位线丛上任意放一个非零曲率联络，例如横向平面

```text
A = (B/2)(x dy - y dx),
F = B dx wedge dy.
```

此时 `F != 0`，闭合横向回路有非零相位 holonomy；但 `k` 完全恒定，spacetime congruence 没有 optical twist。于是“相位联络曲率 -> congruence twist”的一般映射失败。

--- INSPECTOR_CHECK ---
[公式] `A=(B/2)(x dy-y dx)`，`F=dA=B dx wedge dy`；恒定 `k` 满足 `dk=0`，故 `k wedge dk=0`。若 `x,y` 为 m，则 `B` 单位为 `m^-2`，使 `integral F` 无量纲。
[方向] 非零 `U(1)` 曲率可与零 optical twist 共存；因此 `F` 不蕴含 congruence twist。
[数据] 无实验数据；构造性反例。
[假设] `A` 是独立相位联络，不预先等同于 screen-frame spin connection。

## 跳跃2：即便使用 Hopf/Berry 曲率，仍然只得到方向球 holonomy

也许 LP23 会说：不要任意 `A`，只允许来自 Hopf/contact/twistor lift 的 canonical connection。那就取归一化 spinor

```text
u = ( cos(chi/2),
      e^{i phi} sin(chi/2) )^T,
u^\dagger u = 1.
```

标准 Hopf connection 是

```text
A_H = Im(u^\dagger du)
    = sin^2(chi/2) d phi,
F_H = dA_H
    = (1/2) sin chi d chi wedge d phi.
```

这确实是非零曲率；它测量 projective spinor 在 `CP^1 ~= S^2` 方向球上扫过的面积，也就是 Pancharatnam/Berry/Hopf holonomy。问题是：方向球面积不是 spacetime congruence twist。

第二个强反例：平直时空中从一点发出的未来光锥。其每条 generator 的方向由 `(chi,phi)` 标记，因此 Hopf/Berry 曲率在方向球上非零：

```text
F_H = (1/2) sin chi d chi wedge d phi.
```

但这个 congruence 是光锥面 `u=t-r=0` 的 null normal；`k` 可写成某个标量倍数的 `du`，因此 Frobenius obstruction 为零。直观说，它有 expansion，没有 optical twist。于是 canonical Hopf curvature 非零，也不等于 optical twist。

这比第一个反例更贴近 contact/twistor 路线：即使相位曲率不是外加的，而是 Hopf fibration 自带的，它仍然属于 projective spinor 的方向空间；它最多告诉我们光线方向在天球上绕了多少 solid angle，不告诉我们 spacetime 中横向波前是否不可积。

--- INSPECTOR_CHECK ---
[公式] `A_H=Im(u^\dagger du)=sin^2(chi/2)dphi`，`F_H=(1/2)sin chi dchi wedge dphi`；光锥 `u=t-r` 有 `k_a proportional partial_a u`，故 `k wedge dk=0`。
[方向] Hopf/Berry 曲率非零不推出 optical twist 非零；它是方向球 holonomy，不是 spacetime screen distribution 的扭转。
[数据] 无实验数据；使用标准 Hopf connection 与平直光锥反例。
[假设] 远离光锥顶点/caustic；只讨论局部光滑 congruence。

## twistor/contact 翻译：哪里可能有相关，哪里不能等同

在 twistor 语言中

```text
Z^I = (omega^A, pi_{A'}),
omega^A = i x^{AA'} pi_{A'},
Z ~ lambda Z, lambda in C^*.
```

`lambda` 的相位部分仍是 projective redundancy。若沿一族 null rays 比较 `pi` 的相位，得到的是线丛 holonomy；若比较的是 `[pi]` 如何随 spacetime 标签变化，得到的是方向场 `k^{AA'}=pi^A \bar pi^{A'}` 的变化。二者可以被同一个 lift 同时携带，但不是同一个量。

最接近“能映射”的情况是再添加一个结构：

```text
A_phase = A_screen
```

也就是把相位 `U(1)` 联络强行识别为 screen basis 的旋转联络。这样 `F_phase` 可以记录横向屏幕基底绕行后的旋转，类似引力 Faraday/Pancharatnam 相位。但这仍然是“沿 congruence 的横向 frame holonomy”，不是自动改变 `k` 的 Frobenius obstruction。它可以与 optical twist 有耦合项、相关项或共同来源，但不能无条件改写为

```text
F_phase = optical twist.
```

因此本轮判定：contact/twistor holonomy 路线能保留“相位 holonomy 可观测”，不能保留“相位曲率生成光锥扭转”。

--- INSPECTOR_CHECK ---
[公式] `Z~lambda Z`，`k^{AA'}=pi^A \bar pi^{A'}`；`pi -> e^{i alpha}pi` 时 `k` 不变。候选识别 `A_phase=A_screen` 是额外假设，不由 twistor projectivization 自动给出。
[方向] twistor/contact lift 支持相位 holonomy 与 null ray 数据共存；不支持把 projective redundancy 直接当成 optical twist。
[数据] 无实验数据；使用 twistor incidence 与 projective equivalence。
[假设] 采用局部 twistor/spinor 表示；忽略全局奇点与 caustic 对 congruence 空间的影响。

## 深挖1：同构的更深层结构

第一层：主 `U(1)` 线丛。

`psi` 是 fiber coordinate。局部 `psi` 可被 gauge transformation 改写；可观测的是闭合回路 holonomy 或两路干涉相位差。

第二层：Hopf connection 的曲率。

`F_H=(1/2)sin chi dchi wedge dphi` 是 `CP^1` 上的面积形式，等价于方向球上的 monopole curvature。它确实是 contact/Hopf 结构中的自然曲率。

第三层：spacetime contact distribution。

null rays 的 contact 结构来自 projectivized null cotangent bundle 上的 `theta=p_mu dx^mu`。ray/congruence 的 twist 是这个 spacetime/contact 分布投影后的不可积性，而不是 Hopf fiber 的不可积性。两种“不可积”同名但不共域：一个在内部相位线丛/方向球，一个在 spacetime screen distribution。

这三层给出本轮最关键的否定：`U(1)` holonomy 可以是相位物理，但它并不生成光锥几何的扭转。

## 深挖2：源学科结构继续下推

第一层：建筑学中的竖向交通核。

楼梯井/电梯核让人在闭合路线后发生楼层或朝向变化；这相当于 fiber holonomy。它是真实的全局信息，但它不是楼层平面动线本身的旋度。

第二层：平面动线的旋度。

某一层里的动线是否有回旋、是否可由无旋势函数组织，取决于平面布局与门厅/走廊分布；不由电梯按钮的内部相位决定。翻译回 LP23：congruence optical twist 取决于 `k(x)` 的 spacetime 分布；不由 `xi -> e^{i psi}xi` 的 fiber angle 决定。

第三层：把两者绑定需要设计规范。

如果建筑师规定“电梯核每转一层必须同步旋转整层走廊布局”，那 holonomy 会和动线旋度相关；但那是额外设计规范，不是竖向交通核的定义。翻译回物理：若规定 `A_phase=A_screen` 或给出某种 constitutive law，`F_phase` 才可能和 optical data 相关；这不是 contact/twistor 基础结构自动推出的。

--- INSPECTOR_CHECK ---
[公式] 本段无新公式；使用前述 `F_phase` 与 `k wedge dk` 的对象区分。
[方向] 源学科下推支持“holonomy 可观测但不自动生成 base-space twist”的结构判断。
[数据] 无实验数据；类比只用于发现结构，物理判据仍以前述公式为准。
[假设] 建筑学类比不作为证明，只作为 bundle/base 区分的组织原则。

## 最小降级命题

原可存活版本还需要再降级。第3轮后我建议把 LP23-S1' 改写为：

```text
LP23-S1'':
光锥/null congruence 的方向由 null vector、projective spinor 或 twistor/contact lift 给出。
整体 U(1) 相位及其联络 holonomy 可以成为可观测干涉量，
也可以记录 spinor/twistor lift 的全局相位信息；
但 U(1) 相位联络曲率本身不生成 congruence optical twist。
若要把相位曲率映射到 optical data，必须额外指定
screen bundle 识别、spin connection 或 constitutive coupling；
该额外结构才是物理假设，而不是 e^{i theta} 或 Hopf fibration 自动给出的结果。
```

这保留了“相位通过 holonomy 进入物理”的弱版本，同时杀掉“相位曲率就是光锥扭转”的强版本。

## 本轮产出格式

本轮的跨学科跳跃：建筑学竖向交通核/楼层动线 -> 主丛 holonomy 与 base distribution 的区分 -> contact/twistor phase holonomy 与 null congruence optical twist 的区分。

这个结构的数学对象：`U(1)` principal/line bundle connection `A`、curvature `F=dA`、Hopf connection `A_H=Im(u^\dagger du)`、Berry curvature `F_H=(1/2)sin chi dchi wedge dphi`、projective twistor equivalence `Z~lambda Z`、spacetime Frobenius obstruction `k wedge dk`。

如果这个同构成立，最奇怪的可检验预测是：存在非零相位 holonomy 的干涉实验可以在同一 null congruence 的 optical twist 为零时发生；例如恒定 null beam 加外部相位联络，或光锥方向球上的 Hopf/Berry holonomy，都不要求 spacetime 波前发生扭转。

A博士最可能反对的点：A 会说我没有给出完整 optical scalar 分解；我的回应是本轮任务是 contact/twistor holonomy 映射检验，反例只需对象类型与极限例即可击穿一般等同，不需要重推 `B_ab` 分解。

本轮失败记录：`F_phase = optical twist` 映射失败。失败原因不是 holonomy 不存在，而是 holonomy 的曲率在内部相位/方向球上；optical twist 在 spacetime screen distribution 上。二者无自然同构。

下一步计划：若 PI 继续推进，建议不再追“相位曲率生成扭转”，而检验更弱的 coupling 命题：`A_phase` 是否可在特定物理模型中被识别为 polarization/screen-frame connection，并只预测干涉相位或偏振旋转，而非光锥自身扭转。

需要 PI 投喂的文献方向：Pancharatnam-Berry phase on CP1；Hopf fibration connection curvature；projective twistor space and null geodesics；screen bundle connection along null congruences；gravitational Faraday rotation versus optical twist。

## 本轮改动文件

`D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\current\B\round3.md`
