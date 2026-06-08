# LP23-R2 Round1（A路）：Bridge quotient invariant 生死检验

日期：2026-06-03

## §0 框架声明

本轮固定在三个成熟框架内工作，不重新发明术语：

1. 真空几何光学：Lorentzian geometry、null congruence、Sachs optical scalars、Newman-Penrose/GHP boost-spin gauge、polarization parallel transport。
2. 有限频率自旋光学：高频展开的次阶 `O(1/omega)` helicity correction、spin Hall / gravitational Faraday / spin-orbit coupling。
3. 本构电动力学：premetric electrodynamics 中的局域线性 `chi^{abcd}`，以及非局域、色散、记忆型响应核 `K(x,x')`。

本轮问题不是“bridge structure 是否可写”，而是以下商空间是否非空：

`R_{beta beta'}[gamma] = C_beta F_beta(H[gamma]) - C_beta' F_beta'(H[gamma])`

在商掉 endpoint tetrad calibration、screen `SO(2)`、NP/GHP boost-spin、spinoptics `O(1/omega)`、以及本构等价以后，是否还存在不能吸收的非零 residual。

结论先行：**真空几何光学分支判死；helicity-dependent 分支被 spinoptics 完全覆盖到当前目标所需精度；局域介质 `chi^{abcd}` 分支判死。唯一可能存活的活口是非局域、历史依赖、非端点可校准的响应核 `K(x,x')`，且它已经不是纯真空 holonomy-twist residual，而是一个介质/观测过程定义的 memory observable。**

## §-1 先发文献覆盖

四组先发文献检索结论：

1. 几何光学 / tetrad / optical scalars：
   - Dolan, *Geometrical optics for scalar, electromagnetic and gravitational waves on curved spacetime*, DOI `10.1142/S0218271818430101`。核心覆盖：null rays、polarization parallel transport、Skrotskii/Rytov effect、optical scalars、conjugate point 后的 second-order formulation。
   - Newman-Penrose spin-coefficient formalism 与 GHP boost-spin formalism 覆盖 screen/tetrad gauge 的标准语言。
2. Berry / spin Hall / spin optics：
   - Bliokh, *Geometrodynamics of polarized light: Berry phase and spin Hall effect in a gradient-index medium*, DOI `10.1088/1464-4258/11/9/094009`。
   - Frolov & Shoom, DOI `10.1103/physrevd.84.044026`。
   - Frolov, *Spinoptics in a curved spacetime*, DOI `10.1103/physrevd.110.064020`。
   - Frolov & Shoom, *Gravitational spinoptics in a curved space-time*, DOI `10.1088/1475-7516/2024/10/039`。
   - Oancea et al., *Gravitational spin Hall effect of light*, DOI `10.1103/physrevd.102.024075`。
   - Shoom, *Gravitational Faraday and spin-Hall effects of light: Local description*, DOI `10.1103/physrevd.110.024029`。
3. 局域本构 / Fresnel：
   - Hehl & Obukhov, *Foundations of Classical Electrodynamics*, DOI `10.1007/978-1-4612-0051-2`。
   - Rubilar, Obukhov & Hehl, DOI `10.1142/s0218271802002190`。
   - Hehl, Obukhov & Rubilar, DOI `10.1142/s0217751x0201162x`。
   - Obukhov & Rubilar, DOI `10.1103/physrevd.66.024042`。
4. 非局域本构 / memory kernel：
   - Muench, Hehl & Mashhoon, *Acceleration-induced nonlocal electrodynamics in Minkowski spacetime*, DOI `10.1016/s0375-9601(00)00316-9`。
   - Mashhoon, *Vacuum electrodynamics of accelerated systems: Nonlocal Maxwell's equations*, DOI `10.1002/andp.20035151002`。
   - Mashhoon, *Nonlocal special relativity*, DOI `10.1002/andp.200852009-1007`。
   - Mashhoon, *Toward Nonlocal Electrodynamics of Accelerated Systems*, DOI `10.3390/universe6120229`。

先发压力判断：若 residual 只依赖 local screen/tetrad、helicity、或 local constitutive map，它已被成熟框架覆盖；若 residual 依赖传播历史核，则进入非局域响应文献，而非真空几何光学新自由度。

## 三分支判据

### 分支 1：真空几何光学

设同一条 null ray `gamma`，同一源端偏振态，同一探测器 tetrad。几何光学中偏振向量满足

`k^b nabla_b f^a = 0,  f^a k_a = 0,  f^a ~ f^a + alpha k^a`。

对 screen basis `e_A^a` 的局域旋转

`e'_A{}^a = R_A{}^B(psi(lambda)) e_B{}^a`

偏振连接

`A_lambda = e_1 · nabla_k e_2`

变换为

本文采用屏幕旋转约定 `e'_1=cos psi e_1 - sin psi e_2`、`e'_2=sin psi e_1 + cos psi e_2`，因此

`A'_lambda = A_lambda + d psi/d lambda`，

因此相位 holonomy 变为

`Delta chi' = Delta chi + psi_f - psi_i`。

端点 tetrad 一旦校准，`psi_i, psi_f` 是仪器/基底项；中间 screen 的 `SO(2)` 旋转不产生新的 endpoint Stokes observable。NP/GHP 的 boost-spin gauge 只是同一事实的 spin-frame 表达。Dolan 2018 进一步说明 optical scalars 是 beam/congruence 数据，polarization transport 是沿 ray 的平行运输数据，二者不是无附加结构的自然同构对象。

真空分支判据：

`R_{beta beta'}[gamma] = 0 mod {endpoint tetrad, screen SO(2), NP/GHP boost-spin}`

只要 `beta,beta'` 的差别不改变源端/探测端物理 tetrad、不引入介质或有限频率 helicity dynamics，上式成立。

失败条件必须非常强：

`exists beta,beta' : Delta S_obs != 0`

且 `Delta S_obs` 不能写成 endpoint tetrad rotation、screen `SO(2)`、NP/GHP boost-spin、或 source/detector calibration。当前文献矩阵中没有这样的真空几何光学例子。

判定：**分支 1 判死。** 真空几何光学中的全部 `R` 被 endpoint calibration / screen `SO(2)` / NP-GHP gauge 吸收。

### 分支 2：spinoptics `O(1/omega)`

如果 `R` 带有 helicity 符号 `s = +/-1`，或者含有 wavelength/frequency scale，则它已经离开 leading geometrical optics，进入 spinoptics。标准形式可写成

`S_eff = integral [ p_a dx^a + s omega^{-1} A_a(x,p) dx^a - N H_s(x,p) d lambda ]`

或等价地写成 helicity-corrected eikonal/ray equations：

`dx^a/dlambda = partial H_s / partial p_a`,

`dp_a/dlambda = - partial H_s / partial x^a`,

其中 `H_s = H_0 + s omega^{-1} H_1 + O(omega^{-2})`。

Frolov-Shoom 2011、Frolov 2024、Frolov-Shoom JCAP 2024、Oancea et al. 2020、Shoom 2024 已经覆盖了：

1. helicity-dependent trajectory shift；
2. gravitational Faraday / spin-Hall effect；
3. observer/tetrad dependence；
4. arbitrary curved vacuum background 中的 covariant formulation；
5. EM 与 high-frequency gravitational wave 的 spinoptics effective-action 表述。

因此，若 residual 形式为

`R_s[gamma] = R_{+}[gamma] - R_{-}[gamma] != 0`

并且量级为 `O(1/omega)`，它不是 bridge quotient 的新活口，而是 spinoptics 的物理项。它可以非零，但不在标准覆盖边界之外。

分支 2 判据：

`R_helicity != 0` 存活为物理量，当且仅当它能写成 `O(1/omega)` spinoptics observable；但作为 LP23-R2 的“标准不可吸收 residual”，它判死，因为标准 spinoptics 已吸收其分类。

未覆盖条件只能是：

`R_s - R_s^spinoptics = O(omega^{-1})`

且该差值不依赖未固定 tetrad/observer，不等价于 Frolov/Oancea/Shoom 方程中的 spin-curvature coupling。当前未发现此类差值。

判定：**分支 2 覆盖 helicity-dependent 案例。** 若出现 helicity residual，应归入 spinoptics，而不是作为新的 bridge quotient invariant。

### 分支 3：介质本构 `chi^{abcd}` 与非局域 `K(x,x')`

局域线性本构中，

`H^{ab}(x) = (1/2) chi^{abcd}(x) F_cd(x)`。

`chi^{abcd}` 有 36 个独立分量，标准分解为 principal、skewon、axion。光传播由 `chi` 诱导的 Fresnel tensor / quartic wave surface 控制；在 reciprocity、closure、无双折射等条件下退化出 conformal light cone。Rubilar-Obukhov-Hehl 与 Hehl-Obukhov 已经把局域本构对 light cone、birefringence、axion/skewon 影响系统化。

因此局域介质判据为：

`R_chi[gamma] = 0 mod {constitutive equivalence of chi, Fresnel surface, axion/skewon/principal decomposition}`

只要 `beta,beta'` 的差别等价于 `chi` 的不同选择、不同分解、或同一 Fresnel surface 的重参数化，residual 不新。

真正边界在非局域响应：

`H^{ab}(x) = (1/2) integral_M K^{abcd}(x,x') F_cd(x') dV_{x'}`。

其中 `dV_{x'}=sqrt(-g(x'))d^4x'`；`K` 取为双张量核，满足 `K dV_{x'}` 与局域 `chi` 同量纲。局域极限写作 `K^{abcd}(x,x') = chi^{abcd}(x) delta_V(x,x')`，其中 `delta_V` 按 `dV` 归一化。

若 `K(x,x') = chi(x) delta(x,x')`，退回局域 `chi`，判死。若 `K` 具有有限支持、历史依赖、频散、加速度诱导 memory，且 endpoint calibration 不能把积分历史压缩成 `psi_f - psi_i`，则可能产生非局域 residual：

`R_K[gamma] = C_beta F_beta[ integral K_beta(x,x') F(x') dV_{x'} ] - C_beta' F_beta'[ integral K_beta'(x,x') F(x') dV_{x'} ]`。

但这个活口的物理性质必须说清楚：它不是纯真空 GR 中 holonomy 与 optical twist 的新等同，而是介质/观测过程的非局域 memory observable。Muench-Hehl-Mashhoon 与 Mashhoon 的非局域电动力学已经给了先发框架；LP23 只有在给出特定 `K` 的 quotient residual，并证明它不等价于已知 nonlocal electrodynamics kernel 时，才有新意。

判定：**局域 `chi` 分支判死；非局域 `K(x,x')` 是唯一可能存活活口。**

--- INSPECTOR_CHECK ---
[公式] `A'_lambda=A_lambda+dpsi/dlambda`，`Delta chi'=Delta chi+psi_f-psi_i`；`H^{ab}(x)=1/2 chi^{abcd}(x)F_cd(x)`；`H^{ab}(x)=1/2 integral K^{abcd}(x,x')F_cd(x')dV_{x'}`。量纲：`A_lambda` 为每仿射参数的角速度；`Delta chi` 为无量纲角度 rad；`chi` 在 SI 中承载本构单位使 `H` 与 `F` 量纲相配；`K dV_{x'}` 与 `chi` 同量纲，`delta_V` 按协变体积测度归一化。
[方向] 真空 leading-order residual 被端点/屏幕/NP-GHP gauge 吸收；helicity residual 归入 `O(1/omega)` spinoptics；局域介质 residual 归入 `chi` 等价类；唯一可能逃逸项是非局域 memory kernel。
[数据] Dolan 2018；Bliokh 2009；Frolov-Shoom 2011/2024；Oancea 2020；Shoom 2024；Hehl-Obukhov 2003；Rubilar-Obukhov-Hehl 2002；Muench-Hehl-Mashhoon 2000；Mashhoon 2003/2008/2020。
[假设] 源端与探测端 tetrad 可校准；leading vacuum geometric optics 不含介质；spinoptics 只保留到 `O(1/omega)`；局域本构为线性响应；非局域核满足因果支持但尚未指定具体模型。
---

## 深挖1：本轮结论的下一层后果

第一层后果：LP23-R2 不能再声称“bridge structure 本身是新物理”。标准框架已经告诉我们，bridge data 必须先被商掉：

`B_phys = B / G_standard`

其中

`G_standard = {endpoint tetrad calibration, screen SO(2), NP/GHP boost-spin, f^a~f^a+alpha k^a, spinoptics O(1/omega), chi-constitutive equivalence}`。

第二层后果：论文若继续推进，唯一可发表的命题不是“发现 residual”，而是一个清理性分类定理：

`Bridge quotient nonempty only if response is nonlocal/history-dependent or if a higher-order spinoptics term escapes known equations.`

当前证据下，后半句没有支撑；前半句有先发框架但还有可计算余地。也就是说，R2 的生命只剩“非局域本构核下的商不变量是否可构造”。

第三层后果：若转向 `K(x,x')`，LP23 的标题和北极星必须改变。它不再是 “vacuum holonomy-twist bridge”，而是 “nonlocal constitutive memory residual under polarization endpoint calibration”。这是降级也是保命：新意从几何本体论转到可观测响应核。

## 深挖2：本轮依赖的前提中，哪一个最可能错

第一层可疑前提：端点校准足够强。强透镜多路径、caustic/conjugate points、beam cross-section divergence 附近，单 ray 的 endpoint tetrad calibration 可能不足以定义 beam-level observable。Dolan 2018 明确把 conjugate point 后的 optical scalars 作为技术难点处理。

第二层可疑前提：所有可观测偏振 residual 都能局域化为 ray-wise phase。若实际 observable 是 beam-integrated Stokes map，

`S_A^{obs} = integral_beam W_A{}^B(x) S_B(x) d Sigma`

则 caustic、多路径干涉、非局域响应会把“端点旋转项”变成不可压缩的路径历史项。此时 residual 不是单条 `gamma` 的 `R[gamma]`，而是 path family / kernel 的函数。

第三层可疑前提：`K(x,x')` 的非局域性只是介质修饰。若 `K` 来自观测者加速度、测量协议或开放系统 tracing-out，那么它可能模拟“真空中的 effective memory”。但这仍然需要外部物理输入；不能回头声称它是纯真空几何光学的自然 bridge。

硬边界：若下一轮不能给出具体 `K`、具体 beam/path family、具体 endpoint-calibrated observable，则非局域活口也必须判死。

## 最终判定

三分支压缩判据如下：

| 分支 | 标准覆盖 | `R` 是否可非零 | 对 LP23-R2 是否存活 |
|---|---|---:|---|
| 真空几何光学 | endpoint tetrad + screen `SO(2)` + NP/GHP | gauge 上可非零，物理上校准后为零 | 判死 |
| spinoptics `O(1/omega)` | Frolov/Shoom/Oancea/Shoom helicity dynamics | 可非零 | 作为新 residual 判死，归入 spinoptics |
| 局域本构 `chi` | Hehl-Obukhov/Rubilar Fresnel 与 principal/skewon/axion | 可非零 | 作为新 residual 判死，归入 `chi` |
| 非局域本构 `K(x,x')` | Mashhoon/Hehl 非局域电动力学已覆盖框架，但未覆盖具体 LP23 quotient | 可非零 | 唯一活口 |

**最可能存活的唯一活口：非局域、历史依赖、endpoint calibration 不可压缩的 kernel residual**

`I_K[Gamma] = [ C_beta F_beta(K_beta; Gamma) - C_beta' F_beta'(K_beta'; Gamma) ] / G_standard`

其中 `Gamma` 不应是一条孤立 ray，而应是含 caustic/multipath/beam weighting 的 path family。若 `I_K` 能在同一源端与探测端 tetrad、同一入射 Stokes data 下保持非零，并且不能由 `chi delta(x,x')`、spinoptics `O(1/omega)` 或 endpoint rotation 表示，则 LP23-R2 仍有生命。

否则：**全部判死。**

## 下一轮可计算公式 / 模型

建议下一轮不要再抽象谈 bridge，而是直接计算最小模型：

1. 背景：Minkowski 或 Schwarzschild weak lensing。
2. 路径族：两条 null paths `gamma_1,gamma_2`，允许一个简单 caustic/multipath phase。
3. 非局域核：

   `K^{abcd}(x,x') = chi_0^{abcd} delta^4(x-x') + epsilon P^{abcd} exp[-(tau(x)-tau(x'))/T] Theta(tau-tau') delta^3_perp(x,x')`

4. observable：

   `S_obs = sum_i w_i U_i[K] S_in U_i[K]^dagger`

5. 生死检验：

   `I_K = S_obs[K_beta] - R_endpoint(psi_f) S_obs[K_beta']`

   若对所有 `psi_f`、screen gauge、NP/GHP spin-boost 都不能令 `I_K=0`，则活口成立；若可令其为零，则 R2 全部判死。

最弱环节：这个模型需要证明 `epsilon P^{abcd}` 不是普通 dispersive `chi(omega,k)` 的改写，也不是 Mashhoon kernel 的已知特例。

## 本轮成果

本轮成果：把 LP23-R2 压缩成三分支判据；真空几何光学、helicity spinoptics、局域 `chi` 三支均被标准理论吸收；唯一可能存活的是非局域 `K(x,x')` memory residual。

新增引用文献：Dolan 2018 DOI `10.1142/S0218271818430101`；Bliokh 2009 DOI `10.1088/1464-4258/11/9/094009`；Frolov & Shoom DOI `10.1103/physrevd.84.044026`；Frolov 2024 DOI `10.1103/physrevd.110.064020`；Frolov & Shoom 2024 DOI `10.1088/1475-7516/2024/10/039`；Oancea et al. DOI `10.1103/physrevd.102.024075`；Shoom 2024 DOI `10.1103/physrevd.110.024029`；Hehl & Obukhov DOI `10.1007/978-1-4612-0051-2`；Rubilar/Obukhov/Hehl DOI `10.1142/s0218271802002190`；Muench/Hehl/Mashhoon DOI `10.1016/s0375-9601(00)00316-9`；Mashhoon DOI `10.1002/andp.20035151002`、`10.1002/andp.200852009-1007`、`10.3390/universe6120229`。

最弱的环节：非局域 `K` 活口仍只是条件性活口；如果下一轮不能给出 endpoint-calibrated 非零 `I_K`，则应全部判死。

下一步计划：计算上面的两路径/指数记忆核模型，检查 `I_K` 是否能被 `psi_f`、screen `SO(2)`、NP/GHP、spinoptics、局域 `chi` 消掉。

需要 PI 投喂的文献方向：`nonlocal electrodynamics kernel polarization memory`，`caustic polarization transport Stokes multipath`，`dispersive constitutive kernel Berry phase`。

建议保存路径：`current/A/R2_round1.md`
