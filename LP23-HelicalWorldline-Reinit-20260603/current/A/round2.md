# LP23-S1' / A博士 round2

## 0. 框架声明

采用的成熟框架是：平坦 Minkowski 时空中的相对论波相位、光线 aberration、observer tetrad/celestial sphere 表述，以及 3+1 维二分量 spinor 的 null momentum 表述。第 1 轮已经判定“固定半径螺旋包络=光锥”不成立；本轮只检验可存活重表述是否能继续承接“量子动力学相位”

\[
\theta(x,p)=\frac{Et-\mathbf p\cdot\mathbf x}{\hbar}
          =\frac{p_\mu x^\mu}{\hbar}
\]

与 null 方向角 \(\alpha\) 的 Lorentz 变换。

本轮问题的核心不是“能否把一个角写成另一个角”，而是两类对象是否属于同一个 Lorentz 表示：

- \(\theta\)：由四动量协向量与事件四向量缩并得到的无量纲 Lorentz 标量。
- \(\alpha\)：observer tetrad 中的 projective null direction 坐标，在 boost 下按 aberration 非线性变换。

若 \(\alpha=\theta\) 或 \(\alpha=f(\theta)\) 被当作无额外结构的自然识别，则预期会失败；若 \(\alpha\) 改由 \(p^\mu\)、null spinor 或 observer tetrad 的方向投影给出，则可能有边界成立。

## -1. 先发文献检索矩阵

| 检索组 | 文献/框架 | 对本轮的作用 |
|---|---|---|
| 相对论波相位 | 标准狭义相对论/QFT 平面波写法 \(e^{-ip_\mu x^\mu/\hbar}\)；Greiner, *Relativistic Quantum Mechanics*, ch. “Lorentz Covariance of the Dirac Equation”, DOI: 10.1007/978-3-662-04275-5_3 | 支持 \(\theta=p_\mu x^\mu/\hbar\) 是标量，\(\partial_\mu\theta=p_\mu/\hbar\) 才携带方向信息。 |
| 光行差 | Einstein 1905 的光线方向变换；Jackson, *Classical Electrodynamics*, 3rd ed., Sec. 11.3；Rindler, *Relativity: Special, General, and Cosmological*, aberration section | 给出 \(\cos\alpha'=(\cos\alpha-\beta)/(1-\beta\cos\alpha)\) 型非线性变换。 |
| celestial sphere / tetrad | Penrose, “Twistor geometry of light rays”, DOI: 10.1088/0264-9381/14/1A/023；Penrose & Rindler, *Spinors and Space-Time*, Vol. 1 | 支持 null ray 是 projective direction；角坐标依赖 observer tetrad/screen basis。 |
| null spinor | Spinor-helicity 标准式 \(k_{A\dot A}=\lambda_A\bar\lambda_{\dot A}\)；Dixon, “Calculating scattering amplitudes efficiently”, arXiv:hep-ph/9601359 | 支持 3+1 维中 null 方向由 spinor bilinear/projective spinor 给出；整体 \(U(1)\) 相位不改变 \(k^\mu\)。 |
| Berry/U(1) 相位 | Berry 1984, DOI: 10.1098/rspa.1984.0023 | 支持相位作为纤维/holonomy 变量，而不是自动等同 spacetime 方向角。 |

注：本轮新增文献只作数学结构锚点。核心公式以下直接从 Lorentz 变换推导，避免把文献中的坐标约定差异引入 LP23。

## 1. 量子动力学相位是 Lorentz 标量

取 \(x^\mu=(ct,x,y,z)\)，\(p^\mu=(E/c,p_x,p_y,p_z)\)，度规号差取 \((+---)\)，则

\[
p_\mu x^\mu = Et-\mathbf p\cdot\mathbf x .
\]

在 Lorentz 变换 \(\Lambda\) 下，

\[
x'^\mu=\Lambda^\mu{}_\nu x^\nu,\qquad
p'_\mu=p_\nu(\Lambda^{-1})^\nu{}_\mu,
\]

所以

\[
p'_\mu x'^\mu
=p_\nu(\Lambda^{-1})^\nu{}_\mu \Lambda^\mu{}_\rho x^\rho
=p_\rho x^\rho .
\]

因此

\[
\theta'(x',p')=\theta(x,p)\pmod{2\pi}.
\]

这说明相位值本身是标量。方向信息不在 \(\theta\) 的数值中，而在其梯度

\[
\partial_\mu\theta=\frac{p_\mu}{\hbar}
\]

或等价的四动量 \(p^\mu\) 中。若只给 \(\theta\in S^1\)，丢失了 \(p^\mu\) 的三维方向和能量尺度。

--- INSPECTOR_CHECK ---
[公式] \(\theta=p_\mu x^\mu/\hbar\)，\(\theta'=\theta\)，\(\partial_\mu\theta=p_\mu/\hbar\)。SI：\(Et\) 与 \(\mathbf p\cdot\mathbf x\) 均为 J s；除以 \(\hbar\)[J s] 后无量纲。
[方向] \(\theta\) 是 Lorentz 标量；方向信息属于 \(p_\mu\) 或 \(d\theta\)，不属于相位值本身。
[数据] 标准 relativistic plane wave/Dirac covariance；Greiner DOI:10.1007/978-3-662-04275-5_3。
[假设] 平坦时空；全局惯性系；暂不讨论规范场中 \(p_\mu\to p_\mu-qA_\mu\) 的联络相位。

## 2. null 方向角 \(\alpha\) 在 boost 下按 aberration 变换

先在 2+1 维截面中写最小公式。令 null 方向由

\[
k^\mu=\kappa(1,\cos\alpha,\sin\alpha)
\]

表示，其中坐标采用 \(x^0=ct\)，\(\kappa\) 可取为频率尺度或任意正比例因子；方向只取 projective class \([k]\)。沿 \(x\) 轴作速度 \(\beta c\) 的 boost：

\[
k'^0=\gamma(k^0-\beta k^x),\quad
k'^x=\gamma(k^x-\beta k^0),\quad
k'^y=k^y,
\quad \gamma=(1-\beta^2)^{-1/2}.
\]

代入 \(k^x=k^0\cos\alpha\)、\(k^y=k^0\sin\alpha\)，得到

\[
\cos\alpha'
=\frac{k'^x}{k'^0}
=\frac{\cos\alpha-\beta}{1-\beta\cos\alpha},
\]

\[
\sin\alpha'
=\frac{k'^y}{k'^0}
=\frac{\sin\alpha}{\gamma(1-\beta\cos\alpha)},
\]

等价地，

\[
\tan\alpha'
=\frac{\sin\alpha}{\gamma(\cos\alpha-\beta)}
\]

并且象限由上面两式共同决定。

这与 \(\theta'=\theta\) 的标量变换不相容。若设 \(\alpha=f(\theta)\) 且 \(f\) 不含 boost 方向、observer tetrad 或四动量方向，则

\[
\alpha'=f(\theta')=f(\theta)=\alpha,
\]

但 aberration 要求一般 \(\alpha'\ne\alpha\)。除非 \(\beta=0\) 或 \(\alpha=0,\pi\) 的共线退化情形，否则矛盾。

更一般地，对任意 boost 向量 \(\boldsymbol\beta\)，\(\mathbf n=(\cos\alpha,\sin\alpha)\) 的变换可写为

\[
\mathbf n'
=
\frac{
\mathbf n+\left[\frac{\gamma-1}{\beta^2}(\boldsymbol\beta\cdot\mathbf n)-\gamma\right]\boldsymbol\beta
}{
\gamma(1-\boldsymbol\beta\cdot\mathbf n)
}.
\]

这清楚显示 \(\alpha\) 是方向坐标，不是标量相位。

--- INSPECTOR_CHECK ---
[公式] \(\cos\alpha'=(\cos\alpha-\beta)/(1-\beta\cos\alpha)\)，\(\sin\alpha'=\sin\alpha/[\gamma(1-\beta\cos\alpha)]\)。SI：\(\alpha,\beta,\gamma,\sin,\cos\) 均无量纲；\(k^\mu\) 比例尺度在方向比值中消去。
[方向] boost 下 null 方向发生 aberration；\(\alpha=f(\theta)\) 的无结构识别会给 \(\alpha'=\alpha\)，与一般 boost 矛盾。
[数据] Lorentz 变换直接推导；Einstein 1905/Jackson/Rindler 的标准光行差公式。
[假设] 被比较的是两个惯性 observer 的方向测量；\(k^\mu\) 为 future null；boost 沿 \(x\) 轴时采用被动坐标约定。

## 3. tetrad 与 spinor 表述：可协变，但需要额外结构

### 3.1 observer tetrad 表述

在 3+1 维中，令 observer tetrad 为

\[
e_a{}^\mu=(u^\mu,e_1{}^\mu,e_2{}^\mu,e_3{}^\mu),
\quad
u^2=-c^2,
\quad
e_i\cdot e_j=\delta_{ij},
\quad
u\cdot e_i=0
\]

若采用 \((-+++)\) 号差，一个 future null 向量可分解为

\[
k^\mu=\omega\left(u^\mu/c+n^i e_i{}^\mu\right),
\quad n^i n_i=1,
\]

其中 \(\omega=-k\cdot u/c\) 是 observer 测得的频率尺度。给定屏幕基 \((e_1,e_2)\) 后，

\[
\alpha=\operatorname{atan2}(n^2,n^1).
\]

boost 不是改变 \(\theta\) 的标量性，而是改变 observer tetrad \(u,e_i\)，从而改变同一条 null ray 在新 observer 屏幕上的 \(n'^i\)。因此 tetrad 语言能自然给出 \(\alpha\to\alpha'\)，但它已经显式引入了 observer/screen basis 这一额外结构。

### 3.2 spinor 表述

在 3+1 维，用 Hermitian 矩阵表示 null momentum：

\[
k_{A\dot A}=k_\mu\sigma^\mu_{A\dot A}
\]

对 future null \(k^\mu\)，有秩一分解

\[
k_{A\dot A}=\lambda_A\bar\lambda_{\dot A}.
\]

Lorentz 变换由 \(SL(2,\mathbb C)\) 作用

\[
\lambda_A\mapsto \lambda'_A=S_A{}^B\lambda_B,
\quad
k'_{A\dot A}=S_A{}^B\bar S_{\dot A}{}^{\dot B}k_{B\dot B}.
\]

方向是 projective spinor \([\lambda]\in\mathbb{CP}^1\)。若取局部坐标 \(\zeta=\lambda_1/\lambda_0\)，则

\[
\zeta\mapsto \zeta'=\frac{S_1{}^0+S_1{}^1\zeta}{S_0{}^0+S_0{}^1\zeta},
\]

即 Möbius 变换。整体相位

\[
\lambda_A\mapsto e^{i\chi}\lambda_A
\]

不改变

\[
k_{A\dot A}=\lambda_A\bar\lambda_{\dot A}.
\]

所以 3+1 维中 \(U(1)\) 相位天然是纤维冗余或 little-group/holonomy 变量，不是 null 方向角本身。若要把它变成可观测角，需要额外选定 spin frame、截面和联络。

--- INSPECTOR_CHECK ---
[公式] \(k^\mu=\omega(u^\mu/c+n^ie_i{}^\mu)\)，\(\alpha=\operatorname{atan2}(n^2,n^1)\)；\(k_{A\dot A}=\lambda_A\bar\lambda_{\dot A}\)，\(\zeta'=(S_1{}^0+S_1{}^1\zeta)/(S_0{}^0+S_0{}^1\zeta)\)。SI：\(k^\mu\) 携带频率/动量尺度；\(n^i,\alpha,\zeta\) 无量纲。
[方向] tetrad/spinor 能协变描述 null 方向，但 \(\alpha\) 依赖 observer/screen 或 spin frame；整体 \(U(1)\) 相位不改变 null vector。
[数据] Penrose null ray/twistor geometry DOI:10.1088/0264-9381/14/1A/023；spinor-helicity 标准分解；Dixon arXiv:hep-ph/9601359。
[假设] 使用 future null vector；\(\lambda\) 非零；忽略全局 chart 覆盖问题，\(\zeta\) 只在 \(\lambda_0\ne0\) 的 patch 中使用。

## 4. 是否存在自然映射 \(\alpha=f(\theta,p^\mu,e_a{}^\mu)\)

分三种强度判定。

### 4.1 只用 \(\theta\)：不存在

\[
\alpha=f(\theta)
\]

不自然且一般不协变。因为 \(\theta\) 是标量，\(f(\theta)\) 也是标量；而 \(\alpha\) 必须按 aberration 变换。除共线退化方向外，这一路线证伪。

### 4.2 用 \(\theta\) 与 \(p^\mu\)：仍不够，除非 \(p^\mu\) 是 null 且承认 \(\theta\) 只提供梯度

若 \(p^\mu\) 是 massive particle 四动量，\(p^2=m^2c^2\)，它不是 null cone generator。可以取某个 observer 看到的三动量方向，但这给的是 massive velocity/momentum direction，不是光锥方向；要映射到 null direction 还需规则，例如

\[
k^\mu \propto u^\mu/c+\hat{\mathbf p}^{\,i}e_i{}^\mu,
\]

其中 \(\hat{\mathbf p}\) 是 observer tetrad 中的单位三动量方向。这已经引入 observer \(u^\mu\) 和空间基 \(e_i\)。

若 \(p^\mu\) 本身是 massless，则可定义

\[
\alpha(p,e)
=\operatorname{atan2}(p_\mu e_2{}^\mu,\;p_\mu e_1{}^\mu)
\]

或用同等的符号约定从 \(p^\mu=\hbar k^\mu\) 的 spatial direction 取角。此时真正起作用的是 \(p^\mu=d\theta\,\hbar\)，不是 \(\theta\) 的相位值。

### 4.3 用 \(\theta,p^\mu,e_a{}^\mu\)：有边界的自然映射

在最小结构齐备时，可以写

\[
\alpha=f(\theta,p^\mu,e_a{}^\mu)
\equiv
\operatorname{atan2}(p\cdot e_2,\;p\cdot e_1),
\]

但 \(f\) 实际不依赖 \(\theta\) 的值，只依赖 \(p^\mu=\hbar\,d\theta\) 和 observer tetrad。若 LP23 说“量子相位本身生成 null 方向”，则不成立；若说“平面波相位的梯度给出四动量，而 massless 四动量在 observer tetrad 中给出 null 方向角”，则成立但边界很窄。

最小额外结构为：

1. 一个 future null covector/vector \(k_\mu\) 或 massless 四动量 \(p_\mu=\hbar k_\mu\)。若研究 massive Dirac 相位，则还需单独的 null 投影规则。
2. 一个 observer tetrad \(e_a{}^\mu\)，至少包括 \(u^\mu\) 和屏幕基 \((e_1,e_2)\)，用于把 projective null ray 变成角 \(\alpha\)。
3. 一个尺度/归一化约定，例如 \(k^\mu\sim\lambda k^\mu\) 的 projective 等价；方向角不应依赖频率尺度。
4. 若走 spinor 路线，还需 spin frame 与 \(U(1)\) gauge/connection 约定；整体 spinor 相位不能被直接当作 spacetime 方向。

--- INSPECTOR_CHECK ---
[公式] \(\alpha=f(\theta)\Rightarrow\alpha'=\alpha\) 与 aberration 冲突；可用的有界形式为 \(\alpha=\operatorname{atan2}(p\cdot e_2,p\cdot e_1)\)，并要求 \(p^2=0\) 或另给 null 投影规则。SI：\(p\cdot e_i\) 为动量量纲，atan2 比值无量纲；\(\theta\) 无量纲。
[方向] 不存在仅由标量相位到方向角的自然 Lorentz 映射；存在由相位梯度/四动量加 observer tetrad 到方向角的有界映射。
[数据] 本轮第 1-3 节推导；第 1 轮 PI 的 K4 卡点。
[假设] \(\alpha\) 表示 observer 测得的 celestial angle；不是内部 zitter angle；不把 \(\rho=ct\) 反写成固定半径螺旋。

## 5. S1' 判定

若 S1' 被理解为：

> \(\theta=(Et-\mathbf p\cdot\mathbf x)/\hbar\) 的动力学相位可直接等同 null 方向角 \(\alpha\)，从而 \(e^{i\theta}\) 扫出 Lorentz 光锥方向。

则本轮判定为：证伪。

理由是 \(\theta\) 是 Lorentz 标量，而 \(\alpha\) 是 celestial direction 坐标；boost 下 \(\alpha\) 按 aberration 变换。二者不属于同一变换律。

若 S1' 被降格为：

> \(e^{i\alpha}\) 只标记 observer tetrad 中的 null 方向；光锥由 \(\rho=ct\) 或 null vector \(k^\mu\) 生成；量子相位 \(\theta\) 只通过 \(d\theta=p_\mu dx^\mu/\hbar\) 的四动量梯度参与，不能直接替代 \(\alpha\)。

则本轮判定为：有边界成立。

这个边界包括：

- 对 massless 平面波，\(p^\mu\) 本身可给 null direction；\(\alpha\) 可由 \(p^\mu\) 和 observer tetrad 读出。
- 对 massive Dirac/zitter 相位，\(p^\mu\) 是 timelike，不能无规则地产生 null direction；必须另给 null spinor、内部光速 zitter 变量、或 observer 依赖的投影规则。
- \(U(1)\) 相位若作为 spinor 纤维相位或 Berry holonomy，可保留为 connection/holonomy；但它不等于 projective null direction。

## 6. 两层深化

### 深化1：本轮结论的下一层后果

第一层后果：LP23 若继续承接 QM 相位，必须把“相位值 \(\theta\)”与“相位梯度 \(d\theta\)”分开。前者是 \(S^1\) 纤维坐标或干涉相位，后者才给四动量。把 \(e^{i\theta}\) 直接画成 \(e^{i\alpha}\) 会破坏 Lorentz 变换律。

第二层后果：这会把 LP23 的可存活主线从“一个单位圆相位同时编码量子演化和光锥方向”改成“双层结构”：

\[
\text{base: } [k]\in \mathbb{P}N^+ \quad+\quad
\text{fiber: } U(1)\text{ phase/holonomy}.
\]

也就是 null direction 属于 projective light cone/celestial sphere，量子相位属于其上的纤维或沿路径的作用量积分。两者可由联络耦合，但不能同一化。

硬边界：若没有给出 connection 或 spin frame，所谓“相位绕一圈导致方向绕一圈”只是坐标图像，不是 Lorentz 协变命题。

### 深化2：本轮依赖的前提中最可能错误的是哪一个

最可能错误的前提：本轮默认 \(\alpha\) 是 observer celestial angle，而不是内部 zitter 相位角。若 LP23 的 \(\alpha\) 实际指内部 spin phase，例如 Dirac 电子 rest frame 中的 zitter loop angle，那么它不必按光线 aberration 公式变换。

第一层后果：如果 \(\alpha\) 是内部相位，则它应通过 little group、spin supplementary condition 或 rest-frame tetrad 运输，而不是通过 photon null direction aberration 运输。此时 S1' 需要重写为“内部相位如何诱导 null congruence”，而不是“相位角就是 null 方向角”。

第二层后果：这条路线会把最小结构进一步提高到：worldline \(X^\mu(\tau)\)、四速度 \(u^\mu\)、Fermi-Walker 或 spin connection 运输的 tetrad、内部 spinor \(\lambda_A(\tau)\)，以及由 \(\lambda_A\bar\lambda_{\dot A}\) 生成的 null flag。没有这些结构，massive quantum phase 与 null cone 之间仍缺一座桥。

硬边界：本轮没有证明内部 zitter 模型不可能生成某个 null congruence；它只证明“Lorentz 标量相位值 = celestial null 角”不可能自然成立。

## 7. 本轮结论

S1' 的强版本被证伪：\(\theta\) 不能直接等同 \(\alpha\)。可保留的弱版本是：

> 光锥方向由 null vector/projective spinor 加 observer tetrad 给出；量子相位的 Lorentz 标量性不妨碍其梯度 \(p_\mu/\hbar\) 在 massless 情形提供该 null vector，但相位值 \(e^{i\theta}\) 只能作为纤维/holonomy 变量，不能单独生成 aberration 正确的 null 方向角。

因此，LP23 继续推进时应避免“\(\theta=\alpha\)”；应改写为“\(d\theta\to p_\mu\)，若 \(p^2=0\) 则 \([p]\to\alpha_e\)，另有 \(U(1)\) phase 作为纤维联络变量”。

## 末尾产出格式

本轮成果：证明 \(\theta=(Et-\mathbf p\cdot\mathbf x)/\hbar\) 是 Lorentz 标量，而 null 方向角 \(\alpha\) 在 boost 下满足 \(\cos\alpha'=(\cos\alpha-\beta)/(1-\beta\cos\alpha)\)，因此 \(\alpha=f(\theta)\) 的无结构识别被证伪；只有 \(\alpha=\operatorname{atan2}(p\cdot e_2,p\cdot e_1)\) 这种依赖四动量/相位梯度与 observer tetrad 的版本有边界成立。

新增的引用文献：Einstein 1905 光行差公式；Jackson, *Classical Electrodynamics*, 3rd ed., Sec. 11.3；Rindler, *Relativity: Special, General, and Cosmological*；Greiner DOI:10.1007/978-3-662-04275-5_3；Penrose DOI:10.1088/0264-9381/14/1A/023；Dixon arXiv:hep-ph/9601359；Berry DOI:10.1098/rspa.1984.0023。

最弱的环节：本轮把 \(\alpha\) 解释为 observer celestial angle；若 LP23 改称 \(\alpha\) 是内部 zitter/spin phase，则需要另建 worldline tetrad、spin transport 与 null flag 映射，本轮判定不自动覆盖该新命题。

下一步计划：第 3 轮应检验“内部 zitter/spin phase 是否能通过 spinor bilinear 或 Fermi-Walker transported tetrad 生成 observer-independent null congruence”，关键公式为 \(k_{A\dot A}=\lambda_A\bar\lambda_{\dot A}\)、\(D e_a{}^\mu/d\tau\) 的运输律，以及整体 \(U(1)\) 相位是否只产生 holonomy 而不改变 \([k]\)。

需要 PI 投喂的文献方向：Dirac zitterbewegung 的 Lorentz-covariant spin frame；massive particle 的 spin supplementary condition；null flag/spinor bilinear 与 Berry phase/Thomas-Wigner rotation 的关系；Newman complex worldline 或 shear-free null congruence。
