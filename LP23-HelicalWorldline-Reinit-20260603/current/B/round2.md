# B博士 round2：twistor/null congruence/contact lift 路线

## §0 框架声明

本轮的跨学科跳跃：计算机科学里的“变量名 alpha-equivalence / 绑定结构” -> 物理里的 `U(1)` 相位商空间 -> twistor/contact 中的 projective lift。

借来的结构不是“程序像宇宙”这种表面类比，而是一个严格的商结构：变量名整体改名不改变程序语义；只有绑定关系、相对引用、作用域绕行后的 monodromy 才能改变可观测结果。翻译回 LP23：`xi -> e^{i alpha} xi` 像变量整体改名，是垂直纤维自由度；`[xi]`、相对相位、spinor bilinear、connection holonomy 才可能落到可观测 null geometry。

因此我本轮不把“螺旋”当作 spacetime 里的曲线本体，而把它当作 null geodesic congruence 在 spinor/contact/twistor 总空间里的 lift。若这个 lift 的投影不变，它只是规范纤维；若投影改变，它必须通过 projective spinor 或 bilinear 改变 null 方向，不能再伪装成整体相位。

## 跳跃1：变量名改名 -> `U(1)` 整体相位 -> projective spinor

取二分量 spinor

```text
xi =
sqrt(rho) e^{i psi}
( cos(chi/2) e^{i phi/2},
  sin(chi/2) e^{-i phi/2} )^T
```

其中 `psi` 是整体相位，`chi, phi` 是 projective spinor 的方向坐标，`rho>0` 是尺度。Pauli bilinear 给出

```text
k^mu = xi^\dagger sigma^mu xi
     = rho (1,
            sin chi cos phi,
            sin chi sin phi,
            cos chi).
```

结论很硬：`psi` 完全消失；`phi` 和 `chi` 才改变 null 方向。也就是说，如果所谓“螺旋角”是 `psi(s)=Omega s`，它只是在 `U(1)` 纤维里绕圈，投影到 spacetime 仍是同一条 null 方向；如果所谓“螺旋角”是 `phi(s)=Omega s`，那它不是整体相位，而是在天球 `S^2` 上转动 null 方向。

--- INSPECTOR_CHECK ---
[公式] `k^mu = xi^\dagger sigma^mu xi = rho(1, sin chi cos phi, sin chi sin phi, cos chi)`，`k_mu k^mu = rho^2(1-|n|^2)=0`，`rho` 若作能量/长度尺度需另行定标；`psi` 无 SI 单位。
[方向] 整体 `U(1)` 相位不改变 null 方向；相对相位 `phi` 改变 null 方向。
[数据] 无实验数据；使用 Pauli bilinear 与 normalized spinor 参数化。
[假设] 使用 `(+---)` Minkowski 符号；`xi != 0`；`rho` 未被偷换为物理坐标，除非额外给出定标。

## 跳跃2：contact lift，而不是 spacetime 螺旋

把 null direction bundle 写成

```text
N = { (x, [xi], rho) : x in M, rho>0, [xi] in CP^1 }.
```

投影到 spacetime tangent/null vector 的映射是

```text
pi_N(x, xi) = (x, k^mu),   k^mu = xi^\dagger sigma^mu xi.
```

一个 admissible null lift 至少要满足

```text
dx^mu/ds = lambda(s) k^mu(x(s), xi(s)),     lambda(s)>0.
```

若它还要代表平直 Minkowski 中的一条 null geodesic，而不只是任意 null curve，则 projective 方向沿射线不变：

```text
d[xi]/ds = 0        in flat space,
```

或等价地 `dk^mu/ds` 只允许有重参数化比例项；方向不能在天球上转圈。此时可以允许

```text
xi(s) -> e^{i psi(s)} xi_0
```

这条曲线在 spinor 总空间里看起来是沿 `U(1)` 纤维的“螺旋”，但它投影出的 spacetime 轨迹是

```text
x^mu(s) = x_0^mu + K(s) k_0^mu,
```

也就是一条普通 null generator，不是固定半径 spacetime 螺旋。

contact 语言给出同一判据。projectivized null cotangent bundle 上有 canonical contact form

```text
theta = p_mu dx^mu       restricted to p^2=0, modulo p -> a p.
```

null geodesic lift 是它的 characteristic/geodesic flow。若 `x'^\mu` 与 `p^\mu` 平行，则

```text
theta(gamma') = p_mu x'^\mu = lambda p_mu p^\mu = 0.
```

这说明 lift 可以是 contact/Legendrian 意义上的，而不是 spacetime 中多出一条横向圆周运动。

--- INSPECTOR_CHECK ---
[公式] `dx^mu/ds=lambda k^mu`，`k^2=0`；`theta=p_mu dx^mu`，当 `x'^\mu=lambda p^\mu` 时 `theta(gamma')=lambda p^2=0`。`lambda` 若 `s` 无量纲则单位为长度或时间参数对应单位。
[方向] null geodesic 的 contact lift 允许纤维相位绕行；但 spacetime 投影仍由 `k^mu` 决定。
[数据] 无实验数据；使用 null cotangent/contact 标准结构。
[假设] 平直背景中用普通导数；弯曲背景需把 `d[xi]/ds=0` 替换为 spin connection 下的平行运输。

## twistor 翻译：投影类，而非绝对相位

twistor 坐标可写为

```text
Z^I = (omega^A, pi_{A'}),       omega^A = i x^{AA'} pi_{A'}.
```

projective twistor 识别

```text
Z^I ~ lambda Z^I,       lambda in C^*.
```

其中 `lambda` 的相位部分正是整体相位型自由度。它不会改变 projective twistor，也不会改变由 spinor bilinear 确定的 null 方向。对 LP23 最有杀伤力的是：twistor 语言天然支持“总空间 lift”，但它同时禁止把 `C^*` 或 `U(1)` 的垂直相位误读成 spacetime 横向坐标。

若要描述一族 null geodesics，即 null congruence，真正可测的是 congruence 的 optical data：膨胀、剪切、twist/vorticity。这些来自 `k^mu` 场及其导数，例如 `nabla_mu k_nu` 的投影分解；它们不是来自 `xi` 的整体相位 `psi`。所以“twist”这个词可以存活，但含义从“空间里一根螺旋线”降级为“null congruence 的投影几何/holonomy 数据”。

--- INSPECTOR_CHECK ---
[公式] `omega^A=i x^{AA'} pi_{A'}`；`Z~lambda Z`；`k^{AA'} = pi^A \bar pi^{A'}` 或等价 Pauli bilinear。`lambda` 无量纲；`k` 的物理单位仍由 spinor 定标决定。
[方向] twistor 支持 projective lift；整体相位属于 projective 缩放冗余，不是 spacetime 坐标。
[数据] 无实验数据；使用 twistor incidence relation 与 projective equivalence。
[假设] 采用平直或局部共形平直的 twistor 表述；实 Lorentzian null ray 的完整实结构需另行指定，但不影响整体相位商掉这一点。

## 深挖1：同构的更深层结构

第一层：`U(1)` 主丛。

`xi` 的整体相位是 principal `U(1)` fiber。商掉后得到 projective spinor：

```text
(C^2 \ {0}) / C^* = CP^1,
```

若只商 `U(1)` 而保留尺度，则得到去顶点 null cone：

```text
(C^2 \ {0}) / U(1) ~= R_+ x CP^1 ~= R_+ x S^2.
```

第二层：connection/holonomy。

若引入联络 `A`，沿 lift 的相位演化可写成

```text
D_s xi = d_s xi + i A_s xi.
```

局部 `psi(s)` 可被规范变换移动；闭合回路的

```text
exp(i integral A)
```

或相干比较中的相对相位，才可能成为可观测对象。于是“螺旋”若要有物理内容，不能是 `psi(s)` 的局部转动，而必须是 connection curvature 或 holonomy 的表现。

第三层：contact quotient。

null geodesic flow 再 quotient 掉仿射参数，得到“无参数 null geodesic 的空间”。这一步把 `s` 也商掉，进一步说明固定半径螺旋里的“随时间绕圈”不是不变量；不变量是 ray/congruence 及其 contact/holonomy 结构。

--- INSPECTOR_CHECK ---
[公式] `(C^2\{0})/U(1) ~= R_+ x S^2`；`D_s xi=d_s xi+iA_s xi`；holonomy `Hol=exp(i integral A)`。`A_s ds` 无量纲。
[方向] 可观测相位必须是相对相位或 holonomy；局部整体相位是规范选择。
[数据] 无实验数据；使用主丛、联络、商空间。
[假设] 回路 holonomy 的可观测性依赖相干比较装置；单条孤立 null ray 上的局部相位不可观测。

## 深挖2：源学科结构继续下推

第一层：alpha-equivalence。

在 lambda calculus 中，`lambda x. x` 与 `lambda y. y` 是同一程序；变量名整体替换不改变语义。对应到 LP23：`xi` 与 `e^{i psi} xi` 是同一 null direction 的不同名字。

第二层：绑定/作用域。

真正影响语义的是变量绑定结构，而不是名字本身。对应到 spinor：真正改变方向的是 projective 比值

```text
z_2/z_1 = tan(chi/2) e^{-i phi},
```

也就是相对相位和模比，而不是共同乘上的 `e^{i psi}`。

第三层：作用域绕行的 monodromy。

程序模块经过宏展开或依赖解析，局部名字可改，但跨模块引用的绑定图不能乱；绕一圈后的绑定差异才是全局信息。对应到物理：connection holonomy 可以留下相干相位；但这仍不是把 `psi` 画成 spacetime 圆周坐标。

这个下推给出一个反直觉但干净的结论：LP23 若想让“螺旋”有物理内容，应放弃“绝对相位角 = 空间横向角”，改成“相位联络的 holonomy = congruence lift 的全局数据”。

--- INSPECTOR_CHECK ---
[公式] `z_2/z_1 = tan(chi/2)e^{-i phi}` 在 `xi -> e^{i psi}xi` 下不变；`phi` 改变时 `n=(sin chi cos phi, sin chi sin phi, cos chi)` 改变。
[方向] 源学科下推支持同一判据：名字/整体相位不可观测；绑定比值/相对相位可观测。
[数据] 无实验数据；使用商结构类比并落回 spinor 公式。
[假设] 类比只用于发现结构；物理判据以 spinor bilinear 和 contact/twistor quotient 为准。

## 强反例：把相对相位当成“螺旋角”会破坏 geodesic

设

```text
chi = const != 0, pi,
phi(s)=Omega s,
rho = const,
```

则

```text
n(s) = (sin chi cos Omega s,
        sin chi sin Omega s,
        cos chi),
k^mu(s)=rho(1,n(s)).
```

每一点的 `k^2=0` 仍成立，但方向在天球上旋转：

```text
|dn/ds|^2 = Omega^2 sin^2 chi.
```

若令 spacetime 曲线满足 `dx^mu/ds=k^mu(s)`，它是一条 null curve，但不是平直 Minkowski 中的 null geodesic；因为方向不恒定，`d^2x^mu/ds^2` 的空间部分非零。它最多描述一个被外力或非平直联络驱动的 null trajectory，不能说是自由光锥母线。

这给出对“螺旋即光锥”的最强反例之一：如果螺旋角是整体相位，它不可观测；如果螺旋角改变相对相位，它可观测但不再是一条自由 null geodesic。两边都不能支持原始 S1。

--- INSPECTOR_CHECK ---
[公式] `|dn/ds|^2=Omega^2 sin^2 chi`；`k^2=0` 但 `dk^mu/ds != alpha(s) k^mu`，故方向改变。`Omega` 单位为 `s^{-1}` 若 `s` 是时间，或为参数倒数。
[方向] 相对相位旋转给出 null curve，不给出平直自由 null geodesic；整体相位旋转则不给出可观测 spacetime 变化。
[数据] 无实验数据；使用显式参数化反例。
[假设] 平直 Minkowski、无外部场；若引入外部联络，必须把它作为新物理结构显式加入。

## S1' 的最强存活形式

我给出的最强存活版本是：

```text
LP23-S1'_contact/twistor:
平直 3+1 时空中的未来 null cone 或 null geodesic congruence
不是固定半径 spacetime 螺旋的包络；
它可由 spinor/twistor/contact 总空间中的 lift 投影得到。
lift 变量 xi 的整体 U(1) 相位只标记纤维坐标或联络 holonomy；
null 方向由 projective spinor [xi] 或 bilinear k^mu=xi^\dagger sigma^mu xi 决定。
若 lift 曲线在 U(1) 纤维中呈螺旋状，其 spacetime 投影仍是 null ray/congruence；
只有相对相位、holonomy 或 bilinear 的改变才可能改变可观测量。
```

这个版本保留了“相位结构和因果结构有关”的野心，但把原始图像从 spacetime 中的圆柱螺旋，降级/升级为主丛、contact lift 和 twistor projectivization。它牺牲了“看起来像螺旋”的直观，却换来一个可检验、不偷换维度和量纲的版本。

## 可检验判据

判据1：整体相位不变性。

```text
xi -> e^{i alpha} xi
```

必须满足

```text
k^mu -> k^mu,       [xi] -> [xi],       null direction unchanged.
```

若模型中绝对 `alpha` 直接改变光线方向或 spacetime 坐标，则判为规范错误。

判据2：相对相位可观测性。

若改变的是 `z_2/z_1` 的相位，则 `n` 应按天球角改变。这可以改变 congruence，但必须承认改变的是 null direction，而不是整体量子相位。

判据3：holonomy 才能给相位物理内容。

局部 `psi(s)` 不可观测；闭合路径或两路相干比较中的

```text
Delta psi = integral A
```

才可能可观测。若没有联络、回路或相干比较，就不能声称纤维螺旋产生物理效应。

判据4：geodesic 条件。

平直自由 null geodesic 要求 projective direction 沿射线不变：

```text
d[xi]/ds = 0
```

或 `dk^mu/ds` 只差重参数化比例。若“螺旋”导致 `d[xi]/ds != 0`，它描述的是非测地 null curve 或 congruence optical twist，而不是单条光锥母线。

## 对 S1 的判决

原始 S1 继续失败：固定半径单位螺旋包络不是光锥。

S1' 可以存活，但只以 contact/twistor lift 形式存活：

1. “螺旋”只能是 spinor/twistor 总空间中的纤维绕行或联络 holonomy。
2. spacetime 中的光锥来自 projective spinor/bilinear 的投影。
3. 整体 `U(1)` 相位不得改变 null 方向。
4. 任何声称可观测的相位效应，必须落在相对相位、holonomy、spinor bilinear 或 congruence optical scalar 上。

如果 LP23 不接受这些降级条件，强反例已经足够：整体相位螺旋不可观测；相对相位螺旋破坏平直 null geodesic。两者都不是原始 spacetime 螺旋包络。

## 本轮产出格式

本轮的跨学科跳跃：计算机科学 alpha-equivalence/绑定结构 -> `U(1)` 主丛商空间 -> projective spinor/twistor/contact lift -> null geodesic congruence。

这个结构的数学对象：`C^2\{0}` 的 `U(1)`/`C^*` 商、`CP^1 ~= S^2`、Pauli bilinear `k^mu=xi^\dagger sigma^mu xi`、null cotangent contact form `theta=p_mu dx^mu`、twistor incidence `omega^A=i x^{AA'}pi_{A'}`。

如果这个同构成立，最奇怪的可检验预测是：沿同一 null ray 任意改变整体 `U(1)` 相位都不应改变任何光锥方向；只有相对相位、holonomy 或 bilinear 改变时，null congruence 的方向/optical data 才会改变。

A博士最可能反对的点：这已经不是原始“固定半径 spacetime 螺旋包络=光锥”，而是把命题迁移到 spinor/twistor 总空间；同时 twistor 的 projective 缩放比单纯 `U(1)` 更大，必须小心区分尺度、相位和物理定标。

本轮失败记录：若试图把相对相位 `phi(s)=Omega s` 当成螺旋角，虽然每点 `k^2=0`，但方向随 `s` 改变，平直自由 null geodesic 条件失败；若把整体相位 `psi(s)` 当成螺旋角，则它是纯规范纤维，不能产生 spacetime 包络。

下一步计划：若进入第3轮，建议打 congruence optical scalar：把“螺旋/扭转”严格改写为 null congruence 的 twist 标量，检验它是否能从 spinor connection curvature 或 twistor CR/contact 结构中自然出现。

需要 PI 投喂的文献方向：projective twistor space incidence relation；null geodesic flow contact structure；space of null geodesics contact geometry；spinor helicity little group phase；Berry/Pancharatnam phase and Hopf fibration；optical scalars of null congruences。

## 本轮改动文件

`D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\current\B\round2.md`
