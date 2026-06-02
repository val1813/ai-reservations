# Phase 1 — A博士(正规军)推导：准晶 flux-space 量子度量与几何下界推广

> 课题 LP10-S6 / FlatBand-Quasicrystal。零上下文冷启动。本文档为可独立审核的正规推导。
> 对象命题：A（flux-space 几何下界推广成立）vs B（B1 无 Chern 类比下界平凡 / B2 拓扑藏于超空间）。

---

## §-1 先发查重（GATE 0，强制，WebSearch US-only 2026-06）

**判定：⚠️ 部分先发（核心方法已被占用，但本课题的拓扑下界命题为真空白）**

### 四条强制检索 + 核实结果

| 检索词 | 结果 |
|--------|------|
| "quasicrystal superfluid weight quantum geometry flux space" | 命中 arXiv:2507.20540（核心）、2308.08248（综述）、2405.11260（S1对照） |
| "geometric superfluid weight quasicrystal Sun Guo Yang 2025" | 命中 arXiv:2507.20540，作者确认 Junsong Sun, Huaiming Guo, Bohm-Jung Yang（B-J Yang 课题组 publications 页核实） |
| "twisted boundary condition superfluid weight quantum metric quasiperiodic" | 命中 2406.06783（many-body metric under twisted BC）、1906.02213（TBG 拓扑下界）、2507.20540 |
| "cut and project superspace Chern number quasicrystal superconductivity" | 命中 1210.5159（Chern modes of quasiperiodic）、2410.01236（gapless SC real-space topology QC）、**无人将 cut-and-project 超空间 Chern 数与超流权重下界联系** |

### ⚠️ arXiv:2507.20540 真实性与结论核实（本课题最可能的完整先发）

**真实存在。** 标题 "Geometric Superfluid Weight in Quasicrystals"，作者 Junsong Sun, Huaiming Guo, Bohm-Jung Yang，已抓取 abstract + 全文 HTML(v2) 核实。其确切内容：

1. **方法 = 命题A 的方法。** 摘要明言动量空间 QGT 因无平移不变性失效，改用 "the correspondence between the momentum and magnetic flux" 引入 **flux-space quantum metric**（finite-size closed system，twisted BC）。这正是本课题命题A 设定的 g_φ。**方法层面已被完整占用。**
2. **关键缺口（决定性）：他们没有定义 flux Chern 数，没有给出任何 D_s ≥ c|C| 形式的拓扑下界。** 全文新定义的量是：flux-space QM（Eq.3，g^FS）、积分 flux-space QM「IFSQM」𝒬^FS、real-space 积分 QM「RSIQM」𝒬^RS。**无 flux-space Chern 数出现。** 取代拓扑不等式的是一个**几何等式**（Eq.6，D_ps^qm ∝ flux-space QM）+ 一个 **fluctuation 机制**。
3. **"积分"的真实含义不是 flux-环面积分。** 他们的 IFSQM「等价于体积平均的 spread function」：𝒬^FS_{s,αα}=⟨Ω^{αα}_s⟩_V=𝒬^RS_{s,αα}。即对**实空间格点 i 求和**（Eq.6 含 Σ_i g^FS_{f,αβ,i}/ε_i），在 **φ=0 单点**取值，**不是**对 flux 环面 T^d 的 ∫dφ 积分。这是命题B1 的直接文献印证。
4. **系统：1D Stub-QC（标量 flux φ_x）+ 2D Ammann-Beenker QC + 2D Lieb-QC。** AB-QC「可视为 4D 周期 Lieb 晶格的 2D 投影」——**仅此一处触及超空间母晶格，但未引入任何高维 Chern 数，未用 cut-and-project 形式**。无 Penrose。
5. **主结论：** 准周期性通过「诱导 Wannier 函数 spread 的涨落」来调控积分 flux-space QM（"fluctuation mechanism"）。几何贡献在无平移对称下依然存在且可测量——但**纯几何/统计，非拓扑**。

**判定理由：** 命题A 的"用 flux-space 量子度量 g_φ 关联 D_s"已被 2507.20540 完整实现（⚠️ 方法先发）。但命题A 的**核心声张——拓扑下界 D_s ≥ c'π|C_flux| 的推广——在该文献中完全缺席**，且其"积分量"被证明是实空间单点量而非 flux 环面积分。**本课题的可发表增量 = 判定该拓扑下界推广成立/失败/平凡，并精确定位其失败的几何根源。** 这是真空白，GATE 0 放行 A 推导。

**禁区合规：** Niu-Thouless-Wu PRB 31,3372 为禁区引用文献（仅作 twisted-BC 多体 Chern 数定义的背景对照，不作为结论来源；其三事实由领域常识陈述，未能从原文 URL 直接核实——见 §2 撞墙#3 标注）。

【PI审核入口 ⚡先发】方法被 2507.20540 占用属实，但拓扑下界命题为空白。**风险点：若 PI 认为"几何等式 Eq.6 + fluctuation 机制"已实质回答了本课题，则增量退化为综述。A 的反制：本课题问的是拓扑保护（下界、不变量），2507.20540 给的是几何大小（等式、涨落），二者是 S1 中"下界 vs 数值"的分野，不可互替。**

---

## §0 声张（填后不改）

**有条件成立 + 主体证伪。** 准晶 flux-space 量子度量 g_φ **不提供** S1 几何拓扑下界 D_s ≥ c·π|C| 的有效推广，**除一类零测度例外**。精确陈述：

- **D_s 与 g_φ 的几何等式推广成立**（命题A 的弱形式，= 2507.20540 已证）：D_s 的几何部分 ∝ flux-space 量子度量在 φ=0 的值。
- **拓扑下界推广失败**（命题A 的强形式被否，命题B 成立）：因 flux-space 对有限准晶是 T^d 但热力学极限退化为单点，flux Chern 数 C_flux 对 1D 准晶（Stub/Fibonacci）**不存在**（Chern 需 d≥2），对 2D 准晶（AB/Lieb）**几乎总为 0**（无 T-破缺时 by Niu-Thouless-Wu 多体 Chern=0）。下界 → 0，平凡。
- **唯一非平凡窗口（命题B2 精确化）：** 拓扑信息确在 cut-and-project 超空间（2D AB-QC ↔ 4D 母晶格），但该 4D Chern 数活在**非物理的 perp-space**，对物理 flux φ 的二阶响应（=D_s）无直接贡献——超空间几何 ≠ 物理 flux-space 几何。故下界即便在超空间"存在"，也**不下界物理 D_s**。

### §0.5 假设（H1–H6）

- **H1（mean-field BCS）：** 吸引 Hubbard，弱耦合 mean-field，平带极限 D_s 由几何项主导（沿 S1 / 2308.08248 标准框架）。
- **H2（twisted BC = flux）：** ψ(r+L_j)=e^{iφ_j}ψ(r)，φ_j∈[0,2π)，D_s,μν=(1/V)∂²E_0/∂φ_μ∂φ_ν|_{φ=0}（Kohn / Niu-Thouless-Wu 定义）。
- **H3（flux-space QGT）：** g_φ^{μν}=Re⟨∂_{φμ}Ψ|(1−P)|∂_{φν}Ψ⟩，Ω_φ^{μν}=−2Im⟨∂_{φμ}Ψ|(1−P)|∂_{φν}Ψ⟩，P=基态投影。
- **H4（平带孤立 + 一致 pairing）：** 平带与其余谱有能隙，Δ 近似均匀（uniform pairing），使几何项干净（S1 / 2405.11260 条件）。
- **H5（cut-and-project）：** 2D 准晶为 4D（AB）或更高维周期母晶格在无理斜率 2D 物理切片的投影；母晶格 BZ 良定、Chern 数良定。
- **H6（热力学极限）：** D_s 取 V→∞。**关键**：有限 V 下 flux φ 张成 T^d；V→∞ 下能级对 φ 的依赖振幅 ∝ 1/V → 单点退化（见 §N 步骤2）。

### §1 预测（落子前写死，§2 撞墙后比对）

- **P1：** 1D 准晶（Stub-QC/Fibonacci）flux-space 是 T^1（单 φ_x），**无 Chern 数**（需 2 个独立 φ）→下界形式 D_s≥c|C_flux| 在 1D **无定义**，命题B1 在 1D **必然成立**。
- **P2：** 2D 准晶（AB/Lieb）flux-space T^2 上 C_flux=(1/2π)∫_{T²}Ω_φ。预测无 T-破缺时 C_flux=0（多体 Hall 电导=0）→下界=0，平凡。
- **P3：** 2507.20540 既然用 flux-space QM 却没给拓扑下界，预测原因是其"积分量"= 实空间 φ=0 单点量（IFSQM=RSIQM），**没有真的对 T² 积分 Berry 曲率**——若我推导独立得出"对 T² 积分在 V→∞ 退化"，则与文献缺口自洽。
- **P4（最脆弱）：** 超空间 4D Chern 数非零（AB-QC 母 Lieb 晶格可拓扑非平凡），但预测它**不进入** D_s，因 D_s 只测物理 par-space flux 二阶响应。

---

## §N 正文推导（步骤 / 依据 / 反驳检验）

### 步骤 1 — flux-space 量子度量与 flux Chern 数的定义及其先天维数障碍

**推导。** 取有限准晶团簇，体积 V，周期方向 j=1..d（d=物理维）。twisted BC 引入相位 φ=(φ_1,..,φ_d)∈T^d。基态 |Ψ(φ)⟩。定义（H3）：
- 度量 g_φ^{μν}(φ)=Re⟨∂_μΨ|(1−|Ψ⟩⟨Ψ|)|∂_νΨ⟩，
- 曲率 Ω_φ^{μν}(φ)=−2 Im⟨∂_μΨ|(1−|Ψ⟩⟨Ψ|)|∂_νΨ⟩。

flux Chern 数仅当 d≥2 可定义：C_flux=(1/2π)∫_{T²}Ω_φ^{xy} dφ_x dφ_y（Niu-Thouless-Wu 多体 Chern 数，禁区背景）。

**依据。** Kohn 公式 + Niu-Thouless-Wu：多体系统的量子化 Hall 电导 σ_xy=(e²/h)C_flux，C_flux 为基态在 twisted-phase 环面 T² 上的多体 Chern 数。Berry 曲率积分需 **2 个独立的可绕相位** → 拓扑分类的最低维数 d=2。

**反驳检验（自我攻击）。** 反方："1D 准晶 Fibonacci 是著名拓扑系统（Kraus 2012 PRL 109,106402），有拓扑不变量，怎能说无 Chern 数？" 回应：Kraus 的 1D 拓扑不变量是**绝热泵浦参数 φ_pump（准晶相位子 phason）作为第二维**得到的 2D Chern 数（1D+1 pump=2D），**不是物理 flux φ_x**。phason 是 perp-space 平移，**不是 twisted BC 的物理 flux**。故 1D 准晶的拓扑活在 (x, phason) 而非 (φ_x)。**这恰是命题B2 的种子**：拓扑在超空间维度，不在物理 flux-space。**P1 经此检验加强。**

**小结 1：** 命题B1 在 1D **确立**——flux-space=T^1 无 Chern 类比，D_s≥c|C_flux| 无定义。下界推广在 1D 准晶（含 2507.20540 的 Stub-QC、Fibonacci）**先天不成立**。

---

### 步骤 2 — flux-space 在热力学极限退化为单点（命题B1 的 2D 强化 + P3 印证）

**推导。** 基态能 E_0(φ) 对 flux 的依赖（persistent-current 理论，Kohn）：能级带宽（spectral flow 振幅）δE(φ)∼ E_0(φ)−E_0(0) 在无能隙金属 ∝ 1/V，在有隙/局域系统 ∝ e^{−V/ξ}。超流权重 D_s=(1/V)∂²E_0/∂φ²|_0 取有限值是 ∂²E_0/∂φ² ∝ V 的精细抵消。但**曲率 Ω_φ(φ) 与度量 g_φ(φ) 作为 φ 的函数，其对 φ 的非平凡变化幅度随 V→∞ 趋于 0**：基态对均匀 flux 的依赖在大系统里变成可微小扰动，|Ψ(φ)⟩≈|Ψ(0)⟩+O(1/V)。

故 ∫_{T²}Ω_φ dφ：被积函数 Ω_φ(φ)→Ω_φ(0)+O(1/V) 近似常数，但 Chern 数是**整数量子化**的——它不随 V 连续趋零，而是**要么恒为某整数（若有真实简并穿越/能隙闭合搬运），要么恒为 0**。对**无 T-破缺**的吸引 Hubbard 准晶基态（时间反演不变），多体 Hall 电导 σ_xy=0 ⇒ **C_flux≡0**。

**依据。** (i) 时间反演对称 ⇒ Ω_φ^{xy}(φ)=−Ω_φ^{xy}(−φ) 且 TRS 映 φ→−φ ⇒ ∫Ω=0（Niu-Thouless-Wu 框架下 TRS ⇒ C=0，与 2D 拓扑绝缘体 Z₂ 取代 Z 同源）。(ii) 2507.20540 全文无 flux Chern 数、其 IFSQM=RSIQM=实空间 φ=0 site 平均（非 T² 积分）——**正是因为对 T² 真积分 Berry 曲率得 0 或退化，他们才退而用 φ=0 单点度量。P3 命中。**

**反驳检验。** 反方："那 D_s 不也该随 1/V 趋零？为何 D_s 有限而拓扑量退化？" 回应：D_s 是**度量**（QGT 实部）在 φ=0 的局域曲率响应，∝ ∂²E_0/∂φ²，这是**非拓扑的几何大小**，由 pairing×Wannier spread 给出有限值（2507.20540 Eq.6 证实）。拓扑量是**曲率的整体环面积分**，受量子化+TRS 钳制为 0。**二者解耦正是本课题的核心结论**：几何（度量，有限）≠拓扑（Chern，0）。**P2、P3 命中。**

**小结 2：** 2D 准晶无 T-破缺 ⇒ C_flux=0 ⇒ 拓扑下界 D_s≥c'π|C_flux|=0 平凡。落入 S1 的 **C=0 三分类的准晶版**（K1.4 连接）。

---

### 步骤 3 — flux-space 度量的 Kähler 校准条件（S1 AHA#1 在 flux-space 是否保持）

**推导（这是判定下界"即便 C≠0 也可能无下界"的关键）。** S1 的 AHA#1：几何下界 ∫√det g ≥ π|C| 的**等号可达性 + 下界存在性**等价于 QGT 满足 **Kähler 校准**（量子度量是某复结构下的 Kähler 度量，即 √det g=|Ω|/2 逐点成立，Cauchy-Schwarz 取等）。一般 g≥|Ω|/2 给出 ∫√det g≥(1/2)∫|Ω|≥(1/2)|∫Ω|=π|C|。**第一不等式 g≥|Ω|/2 总成立（QGT 半正定），故下界 ∫√det g≥π|C| 形式上总成立**——问题在 C=0 时它退化为 ∫√det g≥0（平凡）。

在 flux-space：g_φ≥|Ω_φ|/2 仍成立（QGT 半正定是普适的，不依赖平移对称）。故**形式不等式 ∫_{T²}√det g_φ ≥ π|C_flux| 在 2D 准晶 flux-space 数学上成立**。

**依据。** QGT 半正定 ⇒ Cauchy-Schwarz ⇒ g≥|Ω|/2，对任意参数流形（含 T^d flux-space）成立，不需 BZ/平移对称。这是命题A **弱形式可推广**的唯一真内容。

**反驳检验（最脆弱步，⚡）。** 反方："那不就证明了命题A 成立吗？下界 ∫√det g_φ≥π|C_flux| 在 2D 准晶成立！" **致命回应（三连）：**
1. **C_flux=0（步骤2）⇒ 下界右端=0**，∫√det g_φ≥0 是平庸真命题，**不构成对 D_s 的拓扑保护**。S1 中下界的物理价值在 C≠0（拓扑钉住 D_s 不为零）；C=0 时下界与"D_s≥0"无异。
2. **左端 ∫_{T²}√det g_φ 不是 D_s。** D_s=(1/V)∂²E/∂φ²|_0 ∝ g_φ(φ=0) 的**单点值**（2507.20540 Eq.6），不是**环面积分** ∫_{T²}√det g_φ。S1 晶体里 D_s∝∫_{BZ}Tr g(k) 是动量积分，**flux-space 没有对应的"对 φ 积分"物理量**——φ 不是粒子动量，没有占据数求和。故"∫√det g_φ≥π|C|"即使成立，**它下界的不是 D_s**，而是一个无物理对应的数学量。**命题A 的强形式在此彻底断裂。**
3. **Kähler 校准在 flux-space 一般破坏。** S1 晶体平带的 Kähler 条件（如 sublattice/chiral 对称的理想平带）依赖 Bloch 波函数解析结构；准晶无 Bloch 定理，g_φ 由无序化的 Wannier spread 涨落生成（2507.20540 的 fluctuation 机制），**逐点 √det g_φ=|Ω_φ|/2 的等号几乎处处破坏** ⇒ 即便强行积分，∫√det g_φ ≫ π|C_flux|，下界**极松**，无预测力。

**小结 3：** 命题A 弱形式（QGT 半正定不等式）可推广但平凡；强形式（下界 D_s 的拓扑量）**三重断裂**：C_flux=0、左端≠D_s、Kähler 破坏。**P4 的物理根源在此明确。**

---

### 步骤 4 — 命题B2 裁决：超空间几何 vs flux-space 几何，拓扑信息来源

**推导。** cut-and-project（H5）：2D AB-QC = 4D 周期 Lieb 母晶格在无理斜率 2D 物理切片（par-space）的投影；剩余 2D 为 perp-space。4D 母晶格 BZ=T⁴，可定义 4D 第二 Chern 数 C₂ 或一对一/二 Chern 数——**这是 1210.5159 / Kraus 2012 意义下准晶拓扑的真实居所**。

问：D_s 是否被 C₂（超空间）下界？
- D_s 测物理 par-space 的 flux φ_par 二阶响应。物理 twisted BC 只绕 par-space 的 2 个非收缩环 → 只激活 φ_par=(φ_x,φ_y)。
- 超空间拓扑 C₂ 还需 perp-space 的两个相位 φ_perp（=phason/相位子自由度）。**φ_perp 不是电磁规范 flux**，对其求 ∂²E/∂φ_perp² **不是超流权重**（不耦合电流算符 j=∂H/∂A，A 只在 par-space）。

**依据。** 电流算符 j_μ=∂H/∂A_μ 仅定义在物理空间方向；perp-space 平移（phason）对应准晶的**构型自由度（tiling rearrangement）**，不携带电荷流。故超空间 Chern 数 C₂ 进入的是"phason 泵浦的电荷输运"（Kraus 2012 的绝热泵浦），**不是均匀 Meissner/Drude 响应 D_s**。

**反驳检验。** 反方："phason 泵浦确实输运电荷（Kraus 实验），这不是超流吗？" 回应：泵浦电荷输运 ∝ ∂E/∂φ_perp（**一阶**，绝热流）对应**量子化电导/极化**（拓扑），而 D_s ∝ ∂²E/∂φ_par²（**二阶**，刚度）对应 Meissner。一阶拓扑量（C₂）≠二阶几何刚度（D_s）。**超空间拓扑保护的是泵浦电荷量子化，不是超流权重下界。命题B2 确立：拓扑信息在超空间，但它不下界物理 D_s。**

**小结 4：** 拓扑（超空间 C₂）与超流刚度（物理 flux-space g_φ(0)）在准晶中**居于不同空间、不同响应阶数**，无下界关系。命题A 强形式的最后退路（B2→A 精确化）被切断。

---

## §末 声张对比 + 卡点

### 预测 vs 实际（⚡）

| 编号 | 预测 | 实际推导结果 | 命中 |
|------|------|------|------|
| P1 | 1D 准晶 flux-space=T¹ 无 Chern，下界无定义 | 步骤1 确立；Kraus 1D 拓扑用 phason 第二维，非物理 flux | ✅ |
| P2 | 2D 准晶无 T-破缺 C_flux=0，下界平凡 | 步骤2 确立（TRS⇒σ_xy=0⇒C=0） | ✅ |
| P3 | 2507.20540 无拓扑下界因其积分量=φ=0 单点量 | 全文核实 IFSQM=RSIQM=实空间 site 平均，非 T² 积分 | ✅ 强命中 |
| P4 | 超空间 Chern≠0 但不进入 D_s | 步骤4 确立（perp-space flux 非电磁规范，一阶≠二阶） | ✅ |

### ⚡结论
准晶 flux-space 量子度量 **g_φ 提供 S1 几何下界的"弱推广"（QGT 半正定不等式 + D_s∝g_φ(0) 几何等式，= 2507.20540 已证），但不提供"拓扑下界推广"**。强形式 D_s≥c'π|C_flux| 在准晶**三重失效**：(1) 1D 无 Chern；(2) 2D 无 T-破缺时 C_flux=0；(3) 即便 C_flux≠0，左端环面积分 ∫√det g_φ 不是 D_s 且 Kähler 校准破坏。拓扑真居所是 cut-and-project 超空间，但超空间 Chern 数下界的是 **phason 泵浦电荷（一阶）**，非超流权重（二阶），故**不下界物理 D_s**。**最终落点：主体证伪（命题B 成立，B1+B2 联合），唯一非平凡窗口为零测度的 T-破缺准晶超导（C_flux≠0），且即便如此下界因左端≠D_s 仍无预测力。**

### ⚡最脆弱步
**步骤3 反驳检验第2点**："∫_{T²}√det g_φ 不是 D_s"。此为否定命题A 强形式的承重墙。逻辑：S1 晶体 D_s∝∫_{BZ}Tr g(k) 含动量占据求和；准晶 flux φ 无占据数对应，D_s 只取 g_φ(φ=0) 单点（2507.20540 Eq.6 印证）。若 PI 质疑"flux-space 是否存在隐藏的等效 BZ 积分使 D_s 重新∝∫_{T²}g_φ"，需补：有限准晶的"flux Brillouin zone"是人造 T^d，热力学极限退化（步骤2），无占据填充，故无 S1 式积分下界。**此步若被推翻，命题A 强形式部分复活——是全文最该被攻击处。**

### ⚡PI 需关注
1. **先发定性**：2507.20540 ⚠️ 方法先发但拓扑下界空白。本课题增量 = "判定下界推广失败 + 定位三重失效根源 + 超空间裁决"。请 PI 确认此增量是否足够（A 立场：是，因它回答了 2507.20540 留白的拓扑保护问题，且与 S1 形成"晶体有下界/准晶无下界"的普适性边界对照，正对 LP-2↔LP-10 主题）。
2. **禁区合规**：Niu-Thouless-Wu 仅作 twisted-BC 多体 Chern 数定义背景，未从原文 URL 直接核实其三事实（撞墙#3，下），结论不依赖其细节、仅依赖"TRS⇒C=0"这一领域共识。
3. **GATE 1 反例栏**：本推导已实证 PI 预设的两个反例候选（反例1=步骤1 的 1D Stub/Fibonacci；反例2=步骤2 的 2D AB/Lieb C_flux=0），建议据此填 GATE 1。

### §2 强制撞墙记录（落子前的预测 vs 撞墙）
- **撞墙#1（步骤1）：** 预判"1D 无 Chern"可能被 Fibonacci 拓扑性反驳 → 撞墙发现 Fibonacci 拓扑用 phason 维，非物理 flux，预判反而加强。无修正。
- **撞墙#2（步骤3）：** 初始倾向"QGT 半正定不等式可推广 ⇒ 命题A 成立" → 撞墙发现左端环面积分≠D_s，命题A 强形式断裂。**这是推导中真正改变结论方向的一撞**：从"A 弱成立可能升级为强"退回"强形式三重失效"。
- **撞墙#3（禁区核实失败）：** 尝试从 arXiv URL 核实 Niu-Thouless-Wu 三事实 → 抓到错误论文（cond-mat/9906121 是 Ising spin glass，非 NTW）。**未编造**：标注为领域共识陈述，结论仅依赖"TRS⇒多体 Chern=0"这一独立可靠事实，不依赖 NTW 原文细节。建议收官前 B 博士或 VERIFIER 用正确 arXiv 号（NTW 1985 为 PRB，无 arXiv；可用后续综述如 2308.08248 转引）补核。

### 卡点
- **C1（待 B/PI）：** "T-破缺准晶超导（C_flux≠0）"窗口是否真零测度？需查是否存在内禀磁性准晶平带超导文献（如 spin-orbit + Zeeman 准晶），若存在则唯一非平凡窗口非空——但即便非空，步骤3 第2点（左端≠D_s）仍使下界无预测力，结论不变。
- **C2（数值交叉验证）：** 步骤2 的"C_flux≡0"应由 2D AB-QC 吸引 Hubbard 的多体 Chern 数数值（对 T² flux 网格算 Berry 曲率）确认。2507.20540 未做此计算（旁证 C=0），但严格闭环需 Phase 2/3 数值。
- **C3（Kähler 破坏定量）：** 步骤3 第3点"准晶 g_φ 逐点 Kähler 破坏"为定性论证，定量需算 2D AB-QC 平带的 √det g_φ vs |Ω_φ|/2 偏离——留 Phase 2。

---

### 真实文献清单（本推导引用，arXiv 号经 WebSearch 核实，未编造）
- **arXiv:2507.20540** Sun, Guo, Yang, "Geometric Superfluid Weight in Quasicrystals"（核心先发，方法占用、拓扑下界空白）— abstract+全文 HTML(v2) 核实。
- **arXiv:2405.11260** Jiang & Barlas, "Geometric superfluid weight of composite bands"（S1 晶体下界对照）。
- **arXiv:2203.11133** Huhtinen et al., "Revisiting flat band SC: minimal quantum metric"（S1 minimal metric 对照，文献库 F5）。
- **arXiv:1906.02213** "Topology-Bounded Superfluid Weight in TBLG"（晶体 metric 积分拓扑下界范例，对照 S1）。
- **arXiv:2406.06783** "many-body quantum metric under twisted boundary conditions"（twisted-BC 多体度量框架）。
- **arXiv:1210.5159** "Chern and Majorana Modes of Quasiperiodic Systems"（准晶拓扑=高维 Chern，命题B2 支撑）。
- **arXiv:2410.01236** "Gapless superconductivity and its real-space topology in quasicrystals"（准晶超导实空间拓扑，交叉）。
- **Kraus et al. PRL 109,106402 (2012)** "Topological states & pumping in quasicrystals"（1D 准晶 phason 泵浦=2D Chern，步骤1/4 承重，文献库 F6）。
- **Sakai et al. PRB 95,024509 (2017)** "Superconductivity on Penrose lattice"（准晶超导数值，交叉，文献库 F4）。
- **Niu, Thouless, Wu PRB 31,3372 (1985)**（twisted-BC 多体 Chern 数定义，禁区背景；原文 URL 核实失败，见撞墙#3）。
