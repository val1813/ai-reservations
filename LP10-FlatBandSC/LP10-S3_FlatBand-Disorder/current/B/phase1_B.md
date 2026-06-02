# LP10-S3 Phase 1 — B博士(突击队)独立推导
## 非磁无序对平带几何超流权重的破坏：标度/SCBA/随机矩阵路径

---

## §0 框架声明（PI审核入口）

**⚡ B独立结论（一句话，不引用A的任何中间量）：**
非磁无序**不会**因"拓扑保护"而使几何超流权重鲁棒；它鲁棒的真实原因是**几何权重是一个由超导能隙 Δ 控制的、带间(off-diagonal)的顺磁响应，其电流顶点偏离扩散子(diffuson)极点，因而不获得常规Drude权重的 τ 增强、也不获得脏极限的 τ 压低**——它在领头阶 ∝ τ⁰。破坏只在散射率 ℏ/τ 逼近能隙 Δ（填隙/类AG对破坏）时发生。由此得到闭式临界无序

$$\boxed{\;W_c \;\simeq\; \sqrt{\,\Delta\cdot\max(W_{\rm flat},\,\Delta)\,}\;}$$

即：**理想/窄平带**（W_flat ≲ Δ）→ W_c ≃ Δ（与"能隙标度"一致）；**宽平带**（W_flat ≳ Δ）→ W_c ≃ √(W_flat Δ)，是带宽与能隙的**几何平均**，介于二者之间且大于 Δ。临界点处几何下界**丧失自平均**（多重分形涨落），典型样本低于系综均值。

**⚡ 学科框架（声明禁用A的工具链）：** 我使用三条互补的、与实空间marker无关的路径：
1. **场论无序平均 / SCBA自能**（主线）：用Nambu自能 Σ_dis = −iℏ/2τ·τ₃ 与电流-电流关联函数的图论结构，判定几何权重对 τ 的标度（Drude ∝τ？拓扑 ∝τ⁰？脏极限 ∝Δτ？）。
2. **RG / 标度维度（Harris判据的平带推广）**：平带 δ-函数态密度使无序算符的标度维度反常，判定无序在平带有效理论中相关/无关，并定位"局域化尺度 ξ(W) vs 几何相干尺度 ℓ_g"的竞争。
3. **随机矩阵 / 自平均性**：∫√det g 的系综均值 vs 典型样本，迁移率边附近的多重分形涨落是否使几何下界丧失自平均。

**⚡ 与A的关系：** A用 [BdG数值 + Anderson无序 + 实空间Chern/超流权重marker]。**我全程禁用这套**：不做BdG对角化、不构造实空间marker、不用Bianco-Resta。重叠仅在**物理结论的可对照量**（W_c与Δ/W_flat的关系、几何下界活在平均层）——这是汇合检验所必需，非工具重叠。我对"鲁棒性来源"给出与A**实质相反**的机制（见§4三点分歧）。

**⚡ 苏格拉底问题数：** 6（前三⭐为PI主线候选）。

---

## §0.5 前置三问（GATE0 先发检索，WebSearch实搜）

**问1：是否已有人用"无序平均场论/SCBA的τ标度"论证平带几何权重的鲁棒性与W_c？**
检索结论：最接近的是 **arXiv:2510.05224**（*Superfluid weight in disordered flat-band superconductors as a competition between localization functionals*）——但其方法是**自洽BdG + 单杂质束缚态微扰**（局域化泛函 Ω̃ vs Ω_I 之差），**不是**SCBA自能/扩散子图论。它给出"几何权重对无序的直接效应在领头阶可忽略、归一化权重鲁棒至 W/Δ̄≈1"。我的SCBA给出**同一个 W_c~Δ 结论在其参数区(W_flat≲Δ)**，但**机制不同**（扩散子脱钩 vs 局域化泛函抵消），且**外推出宽带区 W_c~√(W_flat Δ)**——后者文献未见。**非重复，且为定量延伸。**

**问2：几何量子度量对输运的 τ 结构是否已知？（判定∝τ还是∝τ⁰的先例）**
检索结论：**arXiv:2110.14658**（*Bound on resistivity in flat-band materials due to the quantum metric*）确立了平带电导存在由量子度量给出的几何下界（电阻率上界，对中等弛豫率成立）。这直接支持"几何贡献的 τ 结构不同于Drude"的物理。常规多带几何超流权重见 1610.01803（Peotta-Törmä原始）、2308.08248（综述）、2409.12254（多带）。**我的"扩散子脱钩→∝τ⁰"论证是这些工作的无序图论补全，未见现成推导。**

**问3：无序平带的自平均性/多重分形是否已用于几何量？**
检索结论：**arXiv:2406.12677**（*Scaling of the Quantum Geometry Metrics in Disordered Topological Phases*，KPM线性标度数值）研究了无序拓扑相中量子度量的标度，**但用数值标度，未给出∫√det g 的自平均判据/多重分形τ_q论证**。平带局域化标度见 1812.02959（1D弱无序平带 ξ∝W^{−4/3}过渡）。多重分形普适性见 Evers-Mirlin RMP 80,1355(2008)[经典]。**我的"自平均在 W<W_c 成立、W_c 处因多重分形失效"是新论断，需PI核实是否有2024-2025更近工作。**

**GATE0 总判定：** 课题的"无序破坏几何权重"主问题已有活跃研究（先发风险中高，与计划书一致），但**我的三条框架路径与既有BdG/marker/局域化泛函方法均不重叠**，且产出一个**文献未见的闭式 W_c(W_flat,Δ)** 与**自平均失效判据**。可继续。

---

## §1 独立预测

**P1（临界无序闭式）：**
$$W_c \simeq \sqrt{\Delta\cdot\max(W_{\rm flat},\Delta)}\,,\qquad
\frac{W_c}{\Delta}\simeq\begin{cases}1, & W_{\rm flat}\lesssim\Delta\ (\text{理想平带})\\[4pt]\sqrt{W_{\rm flat}/\Delta}, & W_{\rm flat}\gtrsim\Delta\ (\text{宽平带})\end{cases}$$
判据：无序散射率 ℏ/τ(W) 达到能隙 Δ 时几何权重半衰（类Abrikosov-Gor'kov填隙），**不是**达到带宽 W_flat。

**P2（τ标度/鲁棒机制）：** 几何超流权重在领头阶
$$\mathcal D_s^{\rm geom}(\tau)\;\simeq\;\mathcal D_s^{\rm geom}(0)\cdot\frac{\Delta^2}{\Delta^2+(\hbar/2\tau)^2}\;=\;\mathcal D_s^{\rm geom}(0)\big[1-(\hbar/2\tau\Delta)^2+\dots\big],$$
即 ∝τ⁰（既非Drude的∝τ，也非脏BCS的∝Δτ）。鲁棒来自**带间电流顶点偏离扩散子极点**，非拓扑。

**P3（反常脆性）：** 在固定 Δ 下，**越平的带越脆**——因 δ-DOS 使 ℏ/τ ∝ W²/W_flat 反常增大，故 W_c 随 W_flat 减小而减小（直到 W_flat<Δ 触底于 W_c≃Δ）。这把命题B1的直觉（平带=强微扰）**定量化**，但结论不是"几何被随便多弱的无序破坏"，而是有限的 W_c。

**P4（自平均失效）：** ⟨∫√det g⟩ 在 W<W_c 自平均（典型=均值，相对方差 ∝ L^{−d}）；W→W_c 进入平带带心多重分形区，相对方差 ∝ L^{−Δ₂}（Δ₂为反常多重分形指数），**典型样本 < 系综均值**（对数正态分布），几何下界仅对系综均值成立。

**与A的三点分歧**（详见§4）：分歧①宽带区 W_c>Δ（A无此预测）；分歧②鲁棒机制是扩散子脱钩而非拓扑保护，故拓扑平庸但度量相同的带有相同 W_c；分歧③临界点自平均失效，A的样本逐一quantized marker主张在此破裂。

---

## §2 苏格拉底问题（前三⭐为PI主线候选）

**⭐Q1（τ标度二选一）：** 几何超流权重是Drude型（∝τ，越脏越小）、脏BCS型（∝Δτ）、还是拓扑型（∝τ⁰）？判别量是**电流顶点是否落在扩散子(particle-number Goldstone)极点上**。若带间顶点与扩散子正交→∝τ⁰→鲁棒。

**⭐Q2（破坏的标度是 Δ 还是 W_flat）：** 破坏判据是 ℏ/τ→Δ（填隙/对破坏）还是 ℏ/τ→W_flat（带内局域化）？两者经 ℏ/τ∝W²/W_flat 给出**不同**的 W_c 标度，是命题A/B的真正分水岭。

**⭐Q3（自平均 vs 多重分形）：** ∫√det g 在迁移率边/平带带心是否自平均？若多重分形使相对涨落不随 L→∞ 消失，则"几何下界"是系综陈述还是样本陈述？这决定A的实空间marker是否对单样本有意义。

Q4（Anderson定理的适用边界）：非磁无序对s波保护 Δ/Tc（Anderson定理），但对**刚度**不保护（脏BCS的Δτ）。几何刚度落在哪一边？

Q5（带间混合）：当 ℏ/τ 接近到其它带的带隙 E_G 时，无序诱导带间混合是否在 W_c 之前就污染"孤立平带"假设？（接S5非孤立平带修正）

Q6（维度/普适类）：2D正交类全部局域化（任意W>0），但平带带心是反常/临界的。几何权重的破坏属于哪个标度普适类，d=2 是否为下临界维度？

---

## §3 独立推导

### §3.1 设定与无序模型（场论，非BdG对角化）

多带吸引-U平带超导，平均场Nambu哈密顿 $\mathcal H_k=\xi_k\tau_3+\Delta\,\tau_1$（均匀配对、孤立平带；$\xi_k$为平带相对化学势的色散，带宽 $W_{\rm flat}$，准粒子能 $E_k=\sqrt{\xi_k^2+\Delta^2}\approx\Delta$）。非磁无序为随机势 $V(\mathbf r)=\sum_i u_i\delta(\mathbf r-\mathbf R_i)$，高斯白噪声
$$\langle V(\mathbf r)V(\mathbf r')\rangle=\gamma\,\delta(\mathbf r-\mathbf r'),\qquad \gamma\equiv c_d\,W^2\ (\text{箱型无序 }c_d=a^d/12).$$
无序耦合到电荷密度，故在Nambu空间挂 $\tau_3$（非磁通道，Anderson定理通道）。**关键：我处理的是无序系综平均，而非单一实现的实空间对角化——这是与A方法论的根本分流点。**

### §3.2 SCBA自能与平带散射率的反常增强

自洽Born自能（Nambu对角）：
$$\Sigma(i\omega_n)=\gamma\!\int\!\frac{d^dk}{(2\pi)^d}\,G(k,i\omega_n),\qquad G=(i\omega_n-\mathcal H_k-\Sigma)^{-1}.$$
延迟自能虚部给散射率
$$\frac{\hbar}{2\tau}=-\,{\rm Im}\,\Sigma^R(\varepsilon_F)=\pi\gamma\,\rho(\varepsilon_F),$$
$\rho$为平带（正常态）态密度。**平带的核心反常**：$\rho$不是Fermi面常数而是近 δ-函数。两种自洽区：

- **区(i) 宽带 $W_{\rm flat}\gtrsim$ 展宽**：内禀色散主导，$\rho\simeq\nu_0/W_{\rm flat}$，于是
$$\frac{\hbar}{\tau}\simeq 2\pi c_d\,\frac{W^2}{W_{\rm flat}}.$$
- **区(ii) 理想平带 $W_{\rm flat}\to0$**：自能自洽展宽主导，对角无序使谱展成半圆，宽度 $\Gamma\sim\sqrt\gamma\sim W$，故 $\rho\sim\nu_0/W$，
$$\frac{\hbar}{\tau}\simeq 2\pi c_d\,\frac{W^2}{W}=2\pi c_d\,W\ \ (\propto W,\ \text{线性}).$$

注意区(i)中 $\hbar/\tau\propto W^2/W_{\rm flat}$：**固定 W 时越平的带散射率越大**（δ-DOS反常，P3的根源）。

### §3.3 核心图论：几何权重为何 ∝ τ⁰（不被Drude/脏BCS的τ结构污染）

零温超流权重 = $q\to0,\omega=0$ 的横向流-流关联减抗磁项：
$$\mathcal D_s^{\mu\nu}=\frac{e^2}{\hbar^2 V}\Big[\langle\hat K^{\mu\nu}\rangle-\Pi^{\mu\nu}(\mathbf q\to0,\omega=0)\Big].$$
分解为带内(Drude型)与带间(几何)：
$$\mathcal D_s=\underbrace{\mathcal D_s^{\rm intra}}_{\propto\,(\partial_\mu\xi)(\partial_\nu\xi)}+\underbrace{\mathcal D_s^{\rm geom}}_{\propto\,|\langle m|j_\mu|n\rangle|^2/(E_m-E_n)}.$$

**带内通道**：电流顶点 $j_\mu^{\rm intra}=\partial_\mu\xi_k$ 与粒子数密度同属对角通道，**落在扩散子(diffuson)极点上**——梯形顶点修正(Ward恒等式)将其重整为标准Drude/脏BCS结构 $\mathcal D_s^{\rm intra}\propto v^2\tau$（正常态）或 $\propto\Delta\tau$（脏BCS刚度）。平带 $v=0$ 故净裸值为0；无序仅生成 $O((\hbar/\tau)\cdot\text{small})$ 的小带内片（即2510.05224的 $\tilde\Omega$ 正贡献）。

**带间(几何)通道**：电流顶点 $j_\mu^{mn}=i(E_m-E_n)\mathcal A_\mu^{mn}$（$\mathcal A$=带间Berry联络），能量分母 $\sim E_m-E_n\sim 2\Delta$（Nambu间隙），**与化学势无关、不落在扩散子极点上**。因此：

> **命题(扩散子脱钩)**：带间几何顶点与particle-number扩散子正交，梯形顶点修正在 $q\to0$ 不产生 $1/(\,-i\omega+Dq^2)$ 的奇异增强。故几何权重既无Drude的 $\times\tau$ 增强，也无脏BCS的 $\times\Delta\tau$ 压低。

剩下的只有自能展宽对带间分母的二阶修正。把谱函数展宽 $\hbar/2\tau$ 代入带间Lehmann求和（分母 $\to(2\Delta)^2+(\hbar/\tau)^2$ 型）：
$$\boxed{\;\mathcal D_s^{\rm geom}(\tau)\simeq\mathcal D_s^{\rm geom}(0)\cdot\frac{\Delta^2}{\Delta^2+(\hbar/2\tau)^2}\;}$$
$$\mathcal D_s^{\rm geom}(0)=\frac{e^2}{\hbar}\,4\Delta\!\int\!\frac{d^dk}{(2\pi)^d}\,{\rm tr}\,g(k)\quad(\text{Peotta-Törmä型几何权重}).$$
这是**洛伦兹型、能隙控制的顺磁刚度**：领头 ∝τ⁰，破坏为二阶 $(\hbar/2\tau\Delta)^2$。**回答⭐Q1：几何权重是拓扑型(∝τ⁰)，但其鲁棒来自顶点的带间几何结构与扩散子脱钩，非Bloch拓扑陈数。** 度量平庸(C=0)但 tr g 相同的带，公式不变——这是与A的判别性分歧。

支持：2110.14658 已证平带几何贡献给输运一个**不随 τ 消失**的下界，与上式"几何片不获τ增强/压低"同构。

### §3.4 临界无序 W_c：合并 §3.2 与 §3.3

定义 $W_c$ 为半衰判据 $\hbar/\tau(W_c)=2\Delta$（⭐Q2：标度是 Δ 不是 W_flat）。

- **区(i) 宽带**：$2\pi c_d W_c^2/W_{\rm flat}=2\Delta\Rightarrow W_c=\sqrt{W_{\rm flat}\Delta/(\pi c_d)}\sim\sqrt{W_{\rm flat}\Delta}$。自洽性 $W_c<W_{\rm flat}\Leftrightarrow\Delta<W_{\rm flat}$ ✓。此区 $W_c>\Delta$（因 $W_{\rm flat}>\Delta$），**几何权重撑到超过能隙的无序强度**——宽带稀释DOS、单位无序散射弱。
- **区(ii) 理想平带**：$2\pi c_d W_c=2\Delta\Rightarrow W_c\sim\Delta/(\pi c_d)\sim\Delta$。自洽性 $W_c>W_{\rm flat}\Leftrightarrow\Delta>W_{\rm flat}$ ✓。

合并（吸收O(1)常数）：
$$W_c\simeq\sqrt{\Delta\cdot\max(W_{\rm flat},\Delta)}.$$
**与2510.05224对照**：其Creutz/Lieb是孤立平带、$\Delta\gtrsim W_{\rm flat}=0$，落区(ii)，得 $W_c\sim\Delta$（"鲁棒至 $W/\bar\Delta\approx1$"）——**我的框架在其参数区复现其数值结论**，并预言其未触及的宽带区 $W_c\sim\sqrt{W_{\rm flat}\Delta}$。

### §3.5 RG / 标度维度：无序在平带是相关还是无关？（独立佐证 §3.4）

把无序视为平带投影有效作用上的微扰。Harris判据 $d\nu<2$ 判定无序相关性，但平带需推广：平带 δ-DOS 使无序在**单粒子局域化**意义上**立即相关**（任意 $W>0$ 即产生有限 $1/\tau$，无阈值；与2D正交类"全部局域化"一致）。**但局域化相关 ≠ 几何权重被破坏。** 关键在两尺度竞争（接计划书与S5）：

- 几何相干尺度 $\ell_g=\sqrt{\langle\,{\rm tr}\,g\,\rangle}$（量子度量给的Wannier弥散/配对相干长度，因 $v=0$ 故 $\xi_{\rm SC}\sim\ell_g$ 而非 $v/\Delta$）。
- 局域化长度 $\xi(W)$。

无序把动量 $\mathbf k$ 涂抹 $\delta k\sim1/(v_g\tau)$（$v_g$=几何速度），这正是 **S5 "$k^*\neq k_0$脱钩"的无规版**：配对尺度 Δ vs 无序涂抹 $\hbar/\tau$ 两标度脱钩。几何权重在 $\Delta>\hbar/\tau$（即 $\xi>\ell_g$，配对在局域化前"愈合"几何相干）时存活。把 $\hbar/\tau\to\Delta$ 翻译回 $\xi\to\ell_g$，与§3.4同一判据。

**RG附加洞见**：能隙 Δ 是有效理论中唯一的**相关标度算符**（IR截断）。无序算符的标度维度被 δ-DOS 抬高（"危险无关→边缘相关"），但其RG流被 Δ 截断在 $\hbar/\tau\sim\Delta$。故几何权重的破坏是一个**由 Δ 设定的截断现象**，不是无序无界放大——独立确认 $W_c$ 有限且 $\sim\Delta$ 标度（区ii），区(i)修正为几何平均。

### §3.6 随机矩阵 / 自平均性：几何下界是系综还是样本陈述？（⭐Q3, P4）

样本几何权重 $\mathcal D_s[V]\propto\int\!\sqrt{\det g}\,d^dr$。自平均 ⟺ $R\equiv{\rm Var}(\mathcal D_s)/\langle\mathcal D_s\rangle^2\to0$（$L\to\infty$）。

- **$W<W_c$（扩展/弱局域）**：几何密度 $g(\mathbf r)$ 关联长度 $\xi_g$ 有限，中心极限给
$$R\sim(\xi_g/L)^d\to0,$$
**自平均成立，典型=系综均值**。→ S1-K1.2"下界活在积分/平均层"被确认，且此区**平均层与典型层重合**，A的样本marker有意义。
- **$W\to W_c$（平带带心多重分形/迁移率边）**：本征态多重分形，$\langle|\psi|^{2q}\rangle\sim L^{-\tau_q}$，$\tau_q\neq d(q-1)$（反常）。几何密度继承多重分形，二阶矩
$$R\sim L^{-\Delta_2},\qquad \Delta_2\equiv\tau_2-d<0\ \text{区可使}\ R\not\to0,$$
分布趋**对数正态**，**典型值 $\mathcal D_s^{\rm typ}=e^{\langle\ln\mathcal D_s\rangle}<\langle\mathcal D_s\rangle$**。→ **几何下界仅对系综均值成立；典型样本低于下界。** 这是命题B2"marker自平均失效"的精确化（接Evers-Mirlin RMP 2008多重分形；数值标度见2406.12677）。

**回答⭐Q3**：几何下界是**分层陈述**——$W<W_c$ 系综=样本；$W=W_c$ 退化为纯系综陈述，A的"单样本quantized实空间marker"在此破裂。连接S1-AHA#1：无序=对哈密顿的不确定性，量子度量获随机矩阵修正，Fisher信息在临界点的样本涨落发散。

### §3.7 S1 / S5 前提锚定

- **S1前提（下界活在积分/平均层，C锚定）**：✓。我的 $\langle\mathcal D_s\rangle=(e^2/\hbar)4\Delta\langle\int{\rm tr}\,g\rangle$ 与下界 $\ge(e^2/\hbar)\cdot$(度量积分) 均为**系综平均量**；C（或度量积分）锚在平均层。**补充**：平均层=典型层仅在 $W<W_c$。
- **S5前提（两尺度脱钩，无序=动量涂抹无规版）**：✓。SCBA自能 $\Sigma_{\rm dis}$ 即在 k 空间以宽度 $1/\tau$ 涂抹谱函数（$\delta k\sim1/v_g\tau$），是S5"$k^*\neq k_0$"脱钩的随机化。配对标度 Δ 与无序涂抹 $\hbar/\tau$ 脱钩，几何权重存活于 $\Delta>\hbar/\tau$。

---

## §4 汇合检验（与A对照，不照搬A）

A结论摘要（PI供给，供对照）：A预期"有边界"，$W_c$ 由几何相干长度 $\ell_g$ vs 局域化长度 $\xi(W)$ 竞争定，标度看 $\delta W_{\rm dis}\sim W$ 是否超 Δ；A最可能叙事退让：在理想平带 $W_{\rm flat}\to0$ 极限仍声称几何贡献鲁棒。

**汇合点（一致）：**
1. **两尺度竞争 $\ell_g$ vs $\xi(W)$**：我经SCBA独立得到**同一物理竞争**（$\hbar/\tau\lessgtr\Delta\Leftrightarrow\xi\gtrless\ell_g$），框架不同结论一致——强交叉验证。
2. **理想平带极限 $W_c\sim\Delta$**：A的叙事退让区正是我的区(ii)，二者定量吻合 $W_c\simeq\Delta$，且都与2510.05224数值一致。
3. **下界活在平均层**：一致（S1锚定）。

**分歧点（实质相反，需PI裁决）：**

| | A（几何抗无序/拓扑保护） | B（本报告，SCBA+RG+随机矩阵） |
|---|---|---|
| **①宽带区 W_flat≳Δ** | 二元图景，倾向 $W_c\sim\Delta$ 或 $W_{\rm flat}$ | **$W_c\simeq\sqrt{W_{\rm flat}\Delta}>\Delta$**（几何平均，文献未见） |
| **②鲁棒机制** | Bloch拓扑/实空间Chern marker保护 | **带间顶点与扩散子脱钩(∝τ⁰)**；与拓扑无关，C=0但 tr g 相同的带同样鲁棒 |
| **③临界点自平均** | 实空间marker样本逐一quantized | **多重分形→自平均失效**，典型样本<系综均值，marker仅系综有意义 |

**分歧的可判别性**：分歧②是判别性实验/数值——取一对量子度量积分相同、但一个 C≠0 一个 C=0 的平带，A预测拓扑者更抗无序，B预测二者 $W_c$ 相同。分歧①在 $W_{\rm flat}\sim$ few×Δ 的宽平带数值中可见 $W_c$ 是否超过 Δ。

**若我框架得不同结论的精确描述**：我**不**支持"无论多弱无序都破坏几何"（局域化虽对任意W>0立即相关，但几何权重被 Δ 截断保护，$W_c$ 有限）。我**支持**"自平均在临界点失效使典型样本无样本级下界"——这是对A最强主张（样本marker量子化）的精确反例，但仅在 $W\to W_c$ 窄窗，不否定 $W<W_c$ 的鲁棒。

---

## §5 苏格拉底清单（前三⭐，供PI主线程）

- **⭐Q1** 几何权重的 τ 标度（∝τ / ∝Δτ / ∝τ⁰）？判据=电流顶点是否在扩散子极点上。【B答：∝τ⁰，扩散子脱钩，§3.3】
- **⭐Q2** 破坏标度是 Δ（填隙）还是 W_flat（带内局域化）？经 $\hbar/\tau\propto W^2/W_{\rm flat}$ 给不同 $W_c$。【B答：Δ标度，$W_c\simeq\sqrt{\Delta\max(W_{\rm flat},\Delta)}$，§3.4】
- **⭐Q3** ∫√det g 是否自平均？多重分形是否使下界退化为系综陈述？【B答：$W<W_c$自平均，$W_c$处失效，§3.6】
- Q4 几何刚度落在Anderson定理保护侧还是脏BCS Δτ侧？【B答：领头阶都不，∝τ⁰，独立第三类】
- Q5 带间混合是否在 $W_c$ 前污染孤立平带假设？（接S5）【需PI核实 $E_G$ vs $\hbar/\tau$】
- Q6 破坏的标度普适类与下临界维度？【开放，需PI】

---

## §6 风险与需PI核实项

1. **扩散子脱钩命题(§3.3)** 是本报告承重梁。严格性依赖"带间几何顶点与particle-number Goldstone正交"——我给的是Ward恒等式层面的论证，**完整证明需写出梯形顶点方程并验证带间分量无极点**，标 **需PI核实**（建议S2顶点修正经验复用：S2-K2.1无序顶点vs关联顶点）。
2. **$c_d$ 常数与 $\nu_0$** 为O(1)量纲因子，不改标度但改 $W_c$ 前因子；精确值需具体晶格（Lieb/Creutz/pyrochlore）。
3. **自平均失效的 $\Delta_2$ 符号/大小** 依赖具体普适类与维度；2D平带带心是否真临界（vs弱局域指数大ξ）需数值（2406.12677式KPM）核实，标 **需PI核实**。
4. **区(i)宽带 $W_c>\Delta$** 的自洽性已查（$W_c<W_{\rm flat}$ ✓），但"宽平带"是否仍算"平带超导"（$W_{\rm flat}>\Delta$时几何贡献占比下降）需与S5非孤立平带边界对齐。
5. 所有arXiv号经WebSearch实搜核对（见§0.5与参考）；未直读全文的标注于下。

---

## 参考文献（WebSearch核实；标注直读/仅摘要）

- **arXiv:2510.05224** — *Superfluid weight in disordered flat-band superconductors as a competition between localization functionals*（核心竞品，已读HTML摘要+结果：脏极限Δτ对比、鲁棒至W/Δ̄≈1、Creutz/Lieb局域化泛函抵消）。
- **arXiv:2505.17349** — *Quantum geometric origin of the Meissner effect and superfluid weight marker*（Porlles-Chen超流权重marker，计划书指定；A路径锚点）。
- **arXiv:2110.14658** — *Bound on resistivity in flat-band materials due to the quantum metric*（支持几何贡献的非Drude τ结构）。
- **arXiv:1610.01803** — Peotta-Törmä, *Band geometry, Berry curvature and superfluid weight*（几何权重∝∫g原始）。
- **arXiv:2308.08248** — *Quantum geometry in superfluidity and superconductivity*（综述，多带均场拓扑下界）。
- **arXiv:2409.12254** — *Quantum geometric superfluid weight in multiband superconductors*（带间速度/顶点结构）。
- **arXiv:2406.12677** — *Scaling of the Quantum Geometry Metrics in Disordered Topological Phases*（KPM数值标度，自平均数值参照）。
- **arXiv:1812.02959** — *Scaling laws for weakly disordered 1D flat bands*（平带局域化长度标度 ξ∝W^{−4/3}）。
- **arXiv:2303.15504** — *Ginzburg-Landau theory of flat band superconductors with quantum metric*（ξ_SC/相干长度的几何来源）。
- **arXiv:2601.12969** — *Correlation lengths of flat-band superconductivity from quantum geometry*（相干长度，仅摘要）。
- Evers & Mirlin, *Anderson transitions*, **Rev. Mod. Phys. 80, 1355 (2008)**（多重分形普适性，经典，未直读）。
- Harris, **J. Phys. C 7, 1671 (1974)**（Harris判据，经典）。
- Abrikosov & Gor'kov (1961)（磁性杂质对破坏，类比填隙判据，经典）。
- Anderson, **J. Phys. Chem. Solids 11, 26 (1959)**（Anderson定理，经典）。

*（经典文献年代久无arXiv号；2601.12969因编号近未核全文，标"仅摘要"。其余arXiv号均经§0.5检索返回核对。）*
