# LP23-R2 快通道 AB 验证：A路

## §0 框架声明

本轮采用的成熟框架是：**协变几何光学 + NP/GHP null congruence 光学标量 + 预度量/介质本构电动力学**。

攻击角度不是“holonomy 是否存在”，而是问：所谓 bridge structure 是否已经在标准文献中分别表现为：

1. null congruence 的 screen bundle / Sachs optical scalars；
2. tetrad/spin-frame 的 NP/GHP boost-spin 规范；
3. 偏振平行运输与 Rytov-Skrotskii/Berry 相；
4. 介质或真空修正中的 constitutive tensor；
5. 观测者分解 ADM/1+3 threading/slicing。

结论先行：**R2 的最大脆弱点是“桥接结构分类”很可能不是新对象，而是已有框架中 screen、tetrad、observer、medium、connection、constitutive law 的再命名。若不能给出一个不被 NP/GHP、spin optics、Berry phase 或 premetric electrodynamics 吸收的 quotient invariant，R2 应判为“方向可保留，原始命题不成立”。**

## 1. 最相关先发框架与覆盖范围

### 1.1 NP/GHP：screen 与 optical twist 已经内建

先发核心：

- Newman & Penrose, “An Approach to Gravitational Radiation by a Method of Spin Coefficients,” J. Math. Phys. 3, 566 (1962), DOI: 10.1063/1.1724257.
- Geroch-Held-Penrose formalism；现代工具见 Carminati & Vu, DOI: 10.1023/a:1002753318177.
- Dolan, “Geometrical optics for scalar, electromagnetic and gravitational waves on curved spacetime,” Int. J. Mod. Phys. D 27, 1843010 (2018), DOI: 10.1142/S0218271818430101.

标准对象：

令 `k^a` 为 null ray tangent，screen projector `q_ab` 投影到与 `k^a` 横向的二维空间。光学张量

`B_ab = q_a^c q_b^d nabla_d k_c`

分解为

本文件采用 `theta = (1/2) q^{ab} B_ab` 的二维 screen 归一化，因此

`B_ab = theta q_ab + sigma_ab + omega_ab`.

NP 中对应复 spin coefficient 通常写为

`rho = -(theta + i omega)`.

这里 `omega` 是 null congruence 的 twist/rotation，符号依惯例可反号。

覆盖判断：如果 R2 所谓 bridge 是“从 phase/polarization holonomy 映射到 optical twist”，NP/GHP 已经告诉我们：twist 是 congruence 的 screen-projected derivative，不是单条光线偏振相位的自然函数。要得到相位角，需要额外选择 screen basis 或 tetrad connection。这个额外选择正是 GHP 的 boost-spin gauge。

### 1.2 偏振运输：phase holonomy 已有 Rytov/Skrotskii/Berry 语言

先发核心：

- Dolan 2018, DOI: 10.1142/S0218271818430101.
- Bliokh, J. Opt. A 11, 094009 (2009), DOI: 10.1088/1464-4258/11/9/094009.
- Bliokh & Bliokh, PRL 96, 073903 (2006), DOI: 10.1103/physrevlett.96.073903.
- Bekshaev, Bliokh & Nori, PRX 5, 011039 (2015), DOI: 10.1103/physrevx.5.011039.

标准方程：

几何光学中电磁偏振向量 `f^a` 满足

`k^b nabla_b f^a = 0, f^a k_a = 0`,

并有 gauge freedom

`f^a ~ f^a + alpha k^a`.

偏振角的 holonomy 不是 `f^a` 本身给出的标量，而是相对于某个横向基底 `e_1^a,e_2^a` 的连接积分：

`Delta chi = integral A, A = e_1 dot nabla e_2`

或在动量空间/参数空间中写成 Berry connection。

覆盖判断：R2 中的 screen/observer/splitting 在这里不是新自由度，而是定义 `A` 的必要规范数据。若没有指定检测器 tetrad 或介质本征模基底，偏振 holonomy 只定义到局部 `SO(2)` 旋转规范。

### 1.3 Spin optics：自旋-曲率修正已经覆盖 helicity-dependent residual

先发核心：

- Frolov & Shoom, Phys. Rev. D 84, 044026 (2011), DOI: 10.1103/physrevd.84.044026.
- Frolov, Phys. Rev. D 110, 064020 (2024), DOI: 10.1103/physrevd.110.064020.
- Frolov & Shoom, JCAP 2024, 039, DOI: 10.1088/1475-7516/2024/10/039.

覆盖判断：如果 R2 试图保留“holonomy residual 是 helicity 相关、不可规范消去”的物理自由度，spin optics 已经把它组织成 `1/omega` 阶修正、helicity-dependent ray shift 或 effective action。此类 residual 不能作为 R2 的新分类，除非 R2 给出不同于 spin Hall/spinoptics 的可测量项。

### 1.4 介质/本构结构：constitutive map 已有完整分类

先发核心：

- Hehl & Obukhov, *Foundations of Classical Electrodynamics*, Birkhauser (2003), DOI: 10.1007/978-1-4612-0051-2.
- Rubilar, Ann. Phys. 514, 717 (2002), DOI: 10.1002/andp.200251410-1102.
- Rubilar, Obukhov & Hehl, IJMPD 11, 1227 (2002), DOI: 10.1142/s0218271802002190.
- Obukhov & Rubilar, Phys. Rev. D 66, 024042 (2002), DOI: 10.1103/physrevd.66.024042.

标准对象：

预度量电动力学中本构关系为

`H^{ab} = 1/2 chi^{abcd} F_cd`.

线性本构张量 `chi` 有 36 个分量，可分为 principal、skewon、axion 部分。Fresnel 方程由 `chi` 决定，通常为 quartic wave surface；满足 closure/symmetry 条件时才退化出 conformal light cone。

覆盖判断：R2 中的 medium/constitutive map 基本已被此框架覆盖。若桥接结构包含介质，本构张量就是物理输入；若不包含介质，则不能把介质诱导的 holonomy residual 声称为真空几何的新自由度。

## 2. 对 R2 的核心攻击

R2 的北极星命题说：真正自由度可能在“桥接结构”的选择，不在 holonomy 本身。

A 路攻击：这句话一半正确、一半危险。

正确部分：桥接结构确实是物理输入。没有 screen/observer/tetrad/medium/splitting，phase holonomy 到 optical twist 没有自然、协变、唯一映射。

危险部分：这些桥接结构大多已经被成熟框架分类：

| R2 术语 | 标准文献对象 | 是否已有覆盖 |
|---|---|---|
| screen | Sachs screen bundle, optical scalars | 高度覆盖 |
| observer | 1+3 split, ADM slicing, detector tetrad | 高度覆盖 |
| splitting | threading/slicing, tetrad gauge | 高度覆盖 |
| polarization holonomy | Berry/Rytov/Skrotskii phase | 高度覆盖 |
| optical twist | NP coefficient `Im rho` / congruence vorticity | 高度覆盖 |
| medium | constitutive tensor `chi^{abcd}` | 高度覆盖 |
| bundle morphism | connection/gauge choice between bundles | 数学上高度覆盖，物理上需具体 observable |

因此，R2 不能再以“桥接结构存在”作为新意。唯一可能残余是：

`I_bridge = {bridge structures producing measurable holonomy} / {local tetrad/screen gauge, source-detector calibration, constitutive equivalence}`.

如果这个 quotient 非空，R2 有生命；如果它只还原为 NP/GHP + Berry + constitutive tensor，R2 判死。

## 3. 最小可检验 / 可失败命题

### 命题 A-R2-min

在真空 GR 几何光学极限中，给定同一条 null ray `gamma`、同一源端偏振态、同一探测器 tetrad，任何仅由中间 screen frame 选择导致的 polarization holonomy 差异都是 `SO(2)` gauge artifact；校准源端和探测端 tetrad 后，可测 Stokes 参数不变。

形式化写法：

若两个 screen basis 相差

`e'_A^a = R_A^B(psi(lambda)) e_B^a`,

则 Berry/Rytov 连接变换为

本文件采用 screen 旋转约定 `e_1+i e_2 -> e^{i psi}(e_1+i e_2)` 与连接约定 `A=e_1 dot nabla e_2`；在该约定下

`A' = A + d psi`,

闭合回路或固定端点测量给出

`Delta chi' = Delta chi + psi_f - psi_i`.

若源端和探测端 tetrad 被物理固定，`psi_i, psi_f` 是校准项，不是传播 residual。因此：

`Delta chi_phys != F(omega_optical)`

除非额外指定 congruence、screen、observer tetrad 或 medium。

可失败条件：找到一个真空 GR 几何光学设置，其中两种中间 screen/splitting 在同一源-探测器 tetrad 校准下产生不同 Stokes observable，且差异不能写成：

1. endpoint tetrad rotation；
2. NP/GHP boost-spin gauge；
3. spinoptics `O(1/omega)` helicity correction；
4. 介质/本构 `chi` 差异。

若找到，R2 有新 residual。若找不到，R2 的“桥接结构残余”被标准理论吸收。

### 快速反例校准

Minkowski 平直时空中取直线光线：

`omega_optical = 0`.

沿路径人为选择旋转 screen frame：

`e_1 + i e_2 -> e^{i psi(lambda)}(e_1 + i e_2)`.

则连接给出

`A' = d psi, Delta chi' = psi_f - psi_i`.

若端点 frame 未固定，看似有 holonomy；若端点 frame 固定，这只是基底旋转。这说明：phase holonomy 可被桥选择制造，而 optical twist 仍为零。桥不是自然物理量，必须进入观测定义。

--- INSPECTOR_CHECK ---
[公式] `B_ab=q_a^c q_b^d nabla_d k_c = theta q_ab + sigma_ab + omega_ab`；`A'=A+dpsi`；`Delta chi'=Delta chi+psi_f-psi_i`。量纲：`B_ab, theta, sigma, omega` 为 `m^-1`；`A=dpsi` 沿参数积分后为无量纲角度 rad。
[方向] 真空几何光学中，未固定端点 tetrad 的 bridge-induced holonomy 是 screen `SO(2)` 规范项；不能自然唯一等同 optical twist。
[数据] Newman-Penrose 1962；Dolan 2018；Bliokh 2009；Frolov-Shoom 2011/2024；Hehl-Obukhov/Rubilar 2002。
[假设] 几何光学极限；无吸收介质；源端和探测端偏振参考架可校准；忽略 `O(1/omega)` spinoptics 修正，或将其单独归类。
---

## 4. 深挖1：若 R2 继续推进，下一层后果是什么？

第一层：R2 不能分类“所有桥”，只能分类“规范商后的可测桥”。

也就是从

`B = {screen, observer, medium, splitting, bundle morphism}`

改成

`B_phys = B / G`,

其中 `G` 至少包含 local screen rotation、NP/GHP boost-spin、polarization gauge `f^a ~ f^a + alpha k^a`、端点 tetrad calibration。

第二层：该商空间大概率分裂成三个已知物理簇：

1. 真空几何簇：NP/GHP optical scalars + Rytov/Skrotskii transport；
2. helicity 修正簇：spinoptics / spin Hall of light；
3. 介质簇：constitutive tensor `chi` 的等价类与 Fresnel surface。

如果 R2 的 residual 落入这三簇之一，就不是新自由度，而是已有文献的重新组织。

第三层后果：R2 的可发表切口不能是“发现桥接结构”，而只能是一个严格的 no-go/classification theorem：

> There is no natural covariant map from polarization phase holonomy to optical twist without choosing extra bridge data; after quotienting by standard gauge freedoms, the remaining measurable classes are exactly NP/GHP transport, spinoptical helicity corrections, and constitutive-medium classes.

这会把 R2 从“新物理自由度”降级为“清理概念混淆的分类定理”。

## 5. 深挖2：本轮依赖的前提中，哪个最可能错？

第一层可疑前提：我假设“source-detector tetrad calibration”足以消去所有中间 screen choices。这个前提在非平凡拓扑、强透镜多路径、或有 caustic/conjugate points 时可能失败。

Dolan 2018 特别讨论过 optical scalars 在 conjugate point 后的处理问题。这意味着 beam-level congruence 与 single-ray polarization transport 的关系在 caustic 附近不是简单端点规范问题。

第二层可疑前提：我把 medium/constitutive map 全部归入 `chi^{abcd}`。但若 R2 的 bridge morphism 是非局域、色散、记忆型或量子测量诱导的 map，则局域线性 `chi` 不够。此时需要：

`H^{ab}(x)= integral K^{abcd}(x,x') F_cd(x') d^4x'`

而不是局域

`H^{ab}(x)=1/2 chi^{abcd}(x) F_cd(x)`.

第三层后果：若 R2 想活，最应该攻击的是“非局域/历史依赖 bridge”。但这已经偏离原始 optical twist 桥问题，转入 dispersive medium、open system、measurement-defined polarization observable。它仍可能有价值，但不再是纯 GR holonomy-twist 命题。

## 6. 判定

### 对矛盾 A/B 的判定

A. “存在自然、协变、唯一的 phase-holonomy 到 optical-twist 桥”  
判定：**基本判死**。NP/GHP 与偏振运输文献已经显示二者属于不同层级对象：optical twist 是 congruence 的 screen-projected derivative；phase holonomy 是偏振连接相对于选定 screen/tetrad/basis 的积分。

B. “任何桥都必须显式指定 screen/observer/medium/splitting，且该指定就是物理输入”  
判定：**成立，但新意不足**。这正是标准几何光学、GHP gauge、Berry connection、介质本构理论的共同结论。

### R2 是否仍有可分类且可观测的新残余？

当前 A 路结论：**默认无新残余；除非 R2 给出一个标准商空间之外的 invariant。**

保留的最小活口：

`exists I_bridge such that I_bridge notin {NP/GHP, Berry/Rytov, spinoptics, chi-constitutive classes}`

且它能改变端点校准后的 Stokes observable。否则 R2 应降级为 no-go/classification paper，而不是新物理自由度 paper。

## 本轮成果

本轮成果：从标准文献角度，R2 的“桥接结构”大部分已被 NP/GHP、偏振运输、spin optics、Berry phase 与 premetric constitutive electrodynamics 覆盖；真正可保留的最小命题是一个 quotient-invariant 的存在性检验。

新增引用文献：

1. Newman & Penrose, J. Math. Phys. 3, 566 (1962), DOI: 10.1063/1.1724257.
2. Dolan, Int. J. Mod. Phys. D 27, 1843010 (2018), DOI: 10.1142/S0218271818430101.
3. Bliokh, J. Opt. A 11, 094009 (2009), DOI: 10.1088/1464-4258/11/9/094009.
4. Bliokh & Bliokh, PRL 96, 073903 (2006), DOI: 10.1103/physrevlett.96.073903.
5. Frolov & Shoom, Phys. Rev. D 84, 044026 (2011), DOI: 10.1103/physrevd.84.044026.
6. Frolov, Phys. Rev. D 110, 064020 (2024), DOI: 10.1103/physrevd.110.064020.
7. Frolov & Shoom, JCAP 2024, 039 (2024), DOI: 10.1088/1475-7516/2024/10/039.
8. Hehl & Obukhov, *Foundations of Classical Electrodynamics* (2003), DOI: 10.1007/978-1-4612-0051-2.
9. Rubilar, Ann. Phys. 514, 717 (2002), DOI: 10.1002/andp.200251410-1102.
10. Rubilar, Obukhov & Hehl, IJMPD 11, 1227 (2002), DOI: 10.1142/s0218271802002190.

最弱的环节：“所有 bridge residual 都能被端点 tetrad calibration、NP/GHP gauge、spinoptics 或 constitutive tensor 吸收”这一覆盖性判断仍需逐项证明，尤其在 caustic、多路径、非局域色散介质中可能失败。

下一步计划：把 R2 改写成一个三分支判据：

1. 真空几何光学：证明无自然 map `Hol_pol -> twist`；
2. spinoptics：列出 `O(1/omega)` helicity residual 是否已完全覆盖；
3. 介质/非局域本构：检查 `chi` 或 `K(x,x')` 是否产生标准框架外 observable。

需要 PI 投喂的文献方向：`screen bundle polarization holonomy`, `GHP spin boost gauge polarization`, `Skrotskii gravitational Faraday rotation tetrad`, `nonlocal constitutive electrodynamics Berry phase`, `polarization transport caustics null congruence`。
