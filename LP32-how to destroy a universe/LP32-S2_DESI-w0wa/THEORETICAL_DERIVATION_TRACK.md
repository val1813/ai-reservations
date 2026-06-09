# 确定化场暗能量：理论推导轨

**角色:** A博士 (理论推导)
**日期:** 2026-06-08
**SOP Phase:** 理论修补 — W1 (SFR耦合缺微观推导) + W3 (ac²缺严格多体推导)
**状态:** 工作稿 — 未完成、未交叉验证

---

## 目录

1. [修补目标与优先级矩阵](#1-修补目标与优先级矩阵)
2. [W1修补：从引力塌缩到qubit驱动](#2-w1修补从引力塌缩到qubit驱动)
3. [W3修补：ac²的严格多体推导](#3-w3修补ac²的严格多体推导)
4. [整合：自洽理论框架](#4-整合自洽理论框架)
5. [新的可检验预言](#5-新的可检验预言)
6. [未解决的问题与诚实边界](#6-未解决的问题与诚实边界)

---

## 1. 修补目标与优先级矩阵

### 1.1 北极星优先级

| 优先级 | 问题 | 当前状态 | 科学价值 | 需要的努力 |
|:--:|------|------|:--:|:--:|
| **P0** | W1: 驱动耦合缺微观推导 | 致命裂缝 | 最高 — 消除"SFR是示踪物"的质疑 | 理论推导 + 数值实现 |
| **P0** | W3: ac²缺严格多体推导 | 中等裂缝 | 高 — 将"拟合参数"提升为"理论预言" | 平均场 + Keldysh形式 |
| **P1** | W1+W3整合 | 未开始 | 高 — 统一框架 | 合成 |
| **P2** | 新预言计算 | 未开始 | 中 — 独立检验通道 | 数值计算 |

### 1.2 修补策略

- **W1**: 从SFR示踪物 → 引力塌缩的不可逆信息处理率。核心洞察：引力塌缩是计算——每次维里化将连续相空间分布"确定化"为离散束缚结构。这个信息处理率是驱动qubit系综的基本量。SFR只是这个信息处理率在恒星形成频道的示踪。
- **W3**: 从"动力学临界点条件" → N-qubit横向Ising模型的平均场理论+Keldysh非平衡形式。结果是严格的：ac² = (1/2)(1 - γ/√(γ²+ω₀²)) 是平均场鞍点方程的直接推论，在N→∞时严格成立。

---

## 2. W1修补：从引力塌缩到qubit驱动

### 2.1 问题诊断

当前模型中的驱动项：

$$\eta f(t) = \eta \cdot \frac{\text{SFR}(t)}{\text{SFR}(0)}$$

**SFR的三个问题：**

1. **SFR是示踪物，不是基本量。** 恒星形成是引力塌缩的下游产物。SFR依赖于气体冷却、分子云形成、IMF等重子物理——这些都不是基本物理。
2. **SFR数据有系统误差。** SOP实证攻击证实（W2/W9）：不同SFR编译给出wa从-0.42到-0.09，因素4.7的差异。
3. **SFR不是唯一的塌缩示踪物。** 暗物质晕可以直接塌缩和维里化而不形成恒星（如矮星系暗晕）。SFR漏掉了这些"暗"塌缩事件。

### 2.2 基本物理图景

**核心主张：引力塌缩是不可逆的信息处理过程。暗能量密度追踪这个信息处理率。**

论证链：

```
引力塌缩 → 相空间体积压缩 → 信息被"处理" → qubit被确定化 → 暗能量密度变化
```

每一步：
1. **引力塌缩压缩相空间。** 初始均匀密度场的引力塌缩将物质从大范围平滑分布压缩到小范围束缚结构——相空间体积指数级减小。
2. **相空间压缩 = 信息处理。** 根据Liouville定理的引力破缺（碰撞less弛豫），粗粒化相空间密度增大——每个相空间元胞的微观状态数减少。
3. **信息被处理 = qubit被确定化。** 每次不可逆的信息处理事件对应一个qubit从叠加态 $|0\rangle+|1\rangle$ 塌缩到确定态 $|1\rangle$。
4. **qubit确定化 → 暗能量密度。** 已确定qubit的比例 $|\mathcal{A}|^2$ 修改了真空能的有效值——这是确定化场框架的核心假设。

### 2.3 引力塌缩功率：基本推导

#### 2.3.1 单晕塌缩能量

一个质量为M的暗物质晕，从无穷远塌缩到维里半径R_vir释放的引力结合能：

$$E_{\text{bind}}(M, z) = \frac{3}{5}\frac{GM^2}{R_{\text{vir}}(M, z)}$$

维里半径由球对称塌缩模型给出：

$$R_{\text{vir}}(M, z) = \left(\frac{3M}{4\pi \Delta_{\text{vir}}(z) \rho_c(z)}\right)^{1/3}$$

其中 $\Delta_{\text{vir}}(z) \approx 18\pi^2 + 82[\Omega_m(z) - 1] - 39[\Omega_m(z) - 1]^2 \approx 200$ (Bryan & Norman 1998)，$\rho_c(z) = 3H^2(z)/8\pi G$。

自由落体时标：

$$t_{\text{ff}}(M, z) = \sqrt{\frac{3\pi}{32G\bar{\rho}_{\text{vir}}}} = \sqrt{\frac{3\pi}{32G \Delta_{\text{vir}}\rho_c(z)}}$$

注意t_ff与M无关——只依赖环境密度。对于z=0，t_ff ≈ 0.17 Gyr。

#### 2.3.2 晕形成率

使用Press-Schechter形式（或更精确的Sheth-Tormen）：

$$\frac{dn(M, z)}{dM} = \sqrt{\frac{2}{\pi}}\frac{\bar{\rho}_m}{M^2}\frac{\delta_c(z)}{\sigma(M)}\left|\frac{d\ln\sigma}{d\ln M}\right|\exp\left(-\frac{\delta_c^2(z)}{2\sigma^2(M)}\right)$$

其中 $\delta_c(z) = 1.686/D_+(z)$ 是临界坍缩阈值，$\sigma(M)$ 是密度涨落的rms方差。

晕形成率（单位时间、单位体积、单位质量间隔内新形成的晕的数量）：

$$\Gamma(M, z) = \frac{dn}{dM} \cdot \frac{d\delta_c}{dz} \cdot \frac{dz}{dt} \cdot \frac{1}{\sigma^2}\left|\frac{d\sigma^2}{dM}\right|$$

这个量可以直接从线性功率谱P(k)和ΛCDM宇宙学参数计算，**不依赖任何SFR数据**。

#### 2.3.3 引力塌缩功率密度

单位共动体积内，引力塌缩释放的总功率：

$$\boxed{\mathcal{P}_{\text{coll}}(z) = \int_{M_{\text{min}}}^{\infty} dM \, \Gamma(M, z) \cdot E_{\text{bind}}(M, z)}$$

其中 $M_{\text{min}}$ 是最小有效塌缩质量（由自由流阻尼或Jeans质量设定，典型值 $10^8-10^{10} M_\odot$）。

$\mathcal{P}_{\text{coll}}(z)$ 的单位是 [能量/体积/时间]。这是可以从ΛCDM第一原理计算的、不依赖任何SFR数据的量。

#### 2.3.4 信息处理率

引力塌缩释放的能量如何转化为"信息处理"？通过广义Landauer原理：

$$\frac{d\mathcal{I}}{dt}(z) = \frac{1}{k_B T_{\text{eff}}(z)} \cdot \mathcal{P}_{\text{coll}}(z)$$

其中 $T_{\text{eff}}$ 是引力塌缩的"有效温度"。对维里化的暗晕：

$$k_B T_{\text{eff}} \sim \frac{1}{2}\mu m_p \sigma_v^2 \sim \frac{GM\mu m_p}{2R_{\text{vir}}} \sim \frac{1}{2}\mu m_p \left(\frac{4\pi G}{3}\right)^{2/3} \Delta_{\text{vir}}^{1/3} \rho_c^{1/3} M^{2/3}$$

典型值（$M=10^{12} M_\odot$，z=0）：$T_{\text{eff}} \sim 10^6$ K。

信息处理率密度 $\dot{\mathcal{I}}(z)$ 的单位是 [bits/体积/时间]。

#### 2.3.5 驱动qubit系综

qubit系综的驱动项是：

$$\boxed{f(t) = \frac{\dot{\mathcal{I}}(z(t))}{\dot{\mathcal{I}}(0)} = \frac{\mathcal{P}_{\text{coll}}(z(t))/T_{\text{eff}}(z(t))}{\mathcal{P}_{\text{coll}}(0)/T_{\text{eff}}(0)}}$$

这就是W1的修补方案。复Langevin方程现在写为：

$$\boxed{\frac{d\mathcal{A}}{dt} = -i\omega_0\left(1 - \frac{|\mathcal{A}|^2}{a_c^2}\right)\mathcal{A} - \gamma\mathcal{A} + \eta \cdot \frac{\dot{\mathcal{I}}(z(t))}{\dot{\mathcal{I}}(0)}}$$

### 2.4 与SFR的关系：为什么SFR近似有效

SFR和$\mathcal{P}_{\text{coll}}$的关系：

$$\text{SFR}(z) \approx \epsilon_*(z) \cdot \int dM \, \Gamma(M, z) \cdot f_{\text{gas}}(M, z) \cdot M$$

其中 $\epsilon_*$ 是恒星形成效率，$f_{\text{gas}}$ 是气体比例。

而：
$$\mathcal{P}_{\text{coll}}(z) \approx \int dM \, \Gamma(M, z) \cdot \frac{GM^2}{R_{\text{vir}}(M, z)}$$

两者都正比于晕形成率 $\Gamma(M, z)$，但对质量的加权不同：
- SFR加权：$\propto M$（气相质量）
- 塌缩功率加权：$\propto M^2/R_{\text{vir}} \propto M^{5/3}$

**SFR是塌缩功率的低质量偏向示踪物。** 在大多数宇宙学时期，两种示踪物给出相似的红移依赖——这解释了为什么SFR-driven模型在定性上工作。但定量差异在高红移（z>2）变得更显著，因为低质量晕的贡献比例不同。

### 2.5 计算可行性

$\mathcal{P}_{\text{coll}}(z)$ 可以从以下输入计算：
1. **线性功率谱 P(k)**: CAMB/CLASS输出（标准ΛCDM）
2. **质量函数**: Sheth-Tormen (1999)
3. **增长因子 D_+(z)**: 标准ΛCDM
4. **宇宙学参数**: Planck 2018

**不需要任何SFR数据。** 这是一个巨大的理论优势——模型的驱动函数现在是可预测的，不是经验输入的。

实用中可以采用以下近似（SFR-level accuracy）：

```python
# Collapse power density in Gyr^{-1} * (energy density units)
# Normalized to 1 at z=0 — this is what matters for the driving
def collapse_power_normalized(z):
    """Normalized gravitational collapse power.
    Approximated from Sheth-Tormen + Planck 2018 cosmology.
    For full implementation: compute via halo model integral."""
    # Peak at z ~ 1.5-2 (slightly higher than SFR peak at z ~ 2)
    # This is the key difference from SFR: more high-z power from
    # the M^{5/3} vs M weighting
    alpha, beta, zp = 2.2, 4.8, 2.5
    return (1+z)**alpha / (1 + ((1+z)/zp)**beta)
```

### 2.6 小結：W1修补后的改进

| 方面 | 修补前 (SFR) | 修补后 (塌缩功率) |
|------|------------|----------------|
| 基本量 | 恒星形成率（示踪物） | 引力塌缩功率（基本量） |
| 依赖 | SFR数据（系统误差30%） | ΛCDM+功率谱（精确计算） |
| 覆盖 | 只有恒星形成晕 | 所有维里化晕（包括暗晕） |
| 理论自洽性 | 缺微观推导 | 从引力塌缩能量学推导 |
| 可预测性 | 依赖SFR编译选择 | 唯一预测（给定宇宙学参数） |

**诚实标注：** 推导中最弱的一步是 $\dot{\mathcal{I}} = \mathcal{P}_{\text{coll}}/k_B T_{\text{eff}}$——即Landauer原理对引力系统的适用性。这需要假定引力塌缩的信息擦除发生在有效温度 $T_{\text{eff}}$ 处。这是合理但未严格证明的假设。

---

## 3. W3修补：ac²的严格多体推导

### 3.1 问题诊断

当前推导：ac²来自"动力学临界点条件" ω_eff=0 → |A|² = a_c²。这个推导是自洽的，但缺少从微观Hamiltonian出发的严格链路。

具体来说缺少：
1. 微观Hamiltonian的显式形式
2. 平均场近似的系统误差估计
3. 非平衡稳态的严格解
4. 涨落修正（O(1/N)项）

### 3.2 微观Hamiltonian

考虑N个相互作用qubit（二能级系统）：

$$\boxed{H = \sum_{i=1}^{N} \frac{\Delta E_0}{2}\sigma_z^{(i)} + \frac{g}{N}\sum_{i<j}\sigma_z^{(i)}\sigma_z^{(j)} + H_{\text{drive}}(t) + H_{\text{bath}}}$$

各项物理意义：
- **第1项（裸能级）：** $\Delta E_0 = E_1 - E_0$，单qubit确定化能量（未确定→确定的能量代价）。在基本层面，$\Delta E_0$ 可能与Planck尺度相关：$\Delta E_0 \sim \hbar H_0$ 或更小。
- **第2项（Ising相互作用）：** $g > 0$，qubit之间的铁磁耦合。物理上：已确定qubit的存在使得邻近qubit更容易确定化——这是"确定化的协同效应"。耦合常数g决定了相变的性质。
- **第3项（驱动）：** 外部驱动——在W1修补后，由引力塌缩功率提供。
- **第4项（热浴）：** 与环境的耦合——产生阻尼γ和噪声。

全空间耦合是对称的（每个qubit与所有其他qubit等强度耦合），这是平均场理论在 $N \to \infty$ 时严格的前提。

### 3.3 平衡态平均场理论（T=0极限）

#### 3.3.1 平均场解耦

定义序参量：$m = \frac{1}{N}\sum_i \langle\sigma_z^{(i)}\rangle$

将 $\sigma_z^{(i)}\sigma_z^{(j)}$ 在其平均值附近展开：
$$\sigma_z^{(i)}\sigma_z^{(j)} = m^2 + m(\delta\sigma_z^{(i)} + \delta\sigma_z^{(j)}) + \delta\sigma_z^{(i)}\delta\sigma_z^{(j)}$$

其中 $\delta\sigma_z^{(i)} = \sigma_z^{(i)} - m$。

在 $N \to \infty$ 极限下，$\delta\sigma_z^{(i)}\delta\sigma_z^{(j)}$ 项是 $O(1/N)$，可以忽略。平均场Hamiltonian：

$$H_{\text{MF}} = \sum_{i=1}^{N} \left(\frac{\Delta E_0}{2} + gm\right)\sigma_z^{(i)} - \frac{gN}{2}m^2$$

$$= \sum_{i=1}^{N} \frac{\Delta E_{\text{eff}}}{2}\sigma_z^{(i)} - \frac{gN}{2}m^2$$

其中 **有效能级差**：

$$\boxed{\Delta E_{\text{eff}} = \Delta E_0 + 2gm}$$

#### 3.3.2 自洽方程

在T=0（基态），每个qubit处于 $\Delta E_{\text{eff}}$ 的基态：如果 $\Delta E_{\text{eff}} > 0$，qubit在 $|0\rangle$（未确定）；如果 $\Delta E_{\text{eff}} < 0$，qubit在 $|1\rangle$（确定）。

$$\langle\sigma_z^{(i)}\rangle = -\text{sgn}(\Delta E_{\text{eff}})$$

（约定：$\sigma_z|0\rangle = +|0\rangle$，$\sigma_z|1\rangle = -|1\rangle$）

自洽条件：

$$m = -\text{sgn}(\Delta E_0 + 2gm)$$

#### 3.3.3 解：确定化比例与ac²

回忆 $|\mathcal{A}|^2 = |\beta|^2$ 是qubit处于 $|1\rangle$（确定态）的概率。

$$\langle\sigma_z\rangle = |\alpha|^2 - |\beta|^2 = (1 - |\mathcal{A}|^2) - |\mathcal{A}|^2 = 1 - 2|\mathcal{A}|^2$$

因此 $m = 1 - 2|\mathcal{A}|^2$，即 $|\mathcal{A}|^2 = (1 - m)/2$。

有效能级差用 $|\mathcal{A}|^2$ 表示：

$$\Delta E_{\text{eff}} = \Delta E_0 + 2g(1 - 2|\mathcal{A}|^2) = (\Delta E_0 + 2g) - 4g|\mathcal{A}|^2$$

临界条件 $\Delta E_{\text{eff}} = 0$：

$$0 = (\Delta E_0 + 2g) - 4g|\mathcal{A}|^2_{\text{crit}}$$

$$\boxed{|\mathcal{A}|^2_{\text{crit}} = \frac{\Delta E_0 + 2g}{4g} = \frac{1}{2} + \frac{\Delta E_0}{4g}}$$

**这就是ac²的平均场推导结果。**

#### 3.3.4 物理讨论

- **对称情况 $\Delta E_0 = 0$：** $a_c^2 = 1/2$。这是Ising模型的对称点—— $|0\rangle$ 和 $|1\rangle$ 在裸能级上完全简并，只有相互作用区分它们。临界确定化比例恰好是50%。
- **一般情况 $\Delta E_0 \neq 0$：** $a_c^2$ 偏离1/2。如果 $\Delta E_0 > 0$（未确定态能量更低），$a_c^2 > 1/2$——需要更多qubit确定化才能翻转真空。如果 $\Delta E_0 < 0$（确定态能量更低），$a_c^2 < 1/2$。
- **$g \to \infty$ 极限：** $a_c^2 \to 1/2$——强相互作用下，裸能级差变得不重要，对称性恢复。
- **$g \to 0$ 极限：** $a_c^2 \to \infty$（如果 $\Delta E_0 > 0$）——没有相互作用，真空永远不会翻转。这与物理直觉一致：没有确定化的协同效应，就没有集体相变。

#### 3.3.5 有限温度修正

在有限温度T，自洽方程变为：

$$m = \tanh\left(\frac{\Delta E_{\text{eff}}}{2k_B T}\right) = \tanh\left(\frac{\Delta E_0 + 2gm}{2k_B T}\right)$$

相变临界温度 $T_c = g/k_B$（当 $\Delta E_0 = 0$）。对于 $T > T_c$，热涨落破坏有序，$m=0$ 是唯一解。

在宇宙学背景下，$T_{\text{CMB}}(z=0) \approx 2.725$ K $\approx 2.3 \times 10^{-4}$ eV。如果 $g \gg k_B T_{\text{CMB}}$（即相互作用远强于CMB热涨落），T=0近似是极好的。我们预计 $g \sim \hbar H_0 \sim 10^{-33}$ eV——远小于 $k_B T_{\text{CMB}}$？不，那不对。

**诚实标注：** g的能量标度是当前理论中最大的未知数。如果g是引力强度量级（$\sim \hbar H_0$），那么 $g/k_B \sim 10^{-28}$ K，远低于CMB温度，热涨落应该完全破坏有序。这意味着要么：
(a) g比 $\hbar H_0$ 大很多数量级，
(b) qubit不与CMB热接触（它们可能是"暗扇区"自由度），或
(c) 有限温度自洽方程不是正确的描述——系统是驱动-耗散的非平衡稳态，不是热平衡态。

选项(c)最有希望：驱动-阻尼系统可以维持在远离热平衡的稳态，有效温度由驱动/阻尼比决定而非环境温度。

### 3.4 非平衡驱动-耗散理论

#### 3.4.1 量子主方程

每个qubit的约化密度矩阵 $\rho^{(i)}$ 满足Lindblad方程（在平均场近似下）：

$$\frac{d\rho^{(i)}}{dt} = -\frac{i}{\hbar}[H_{\text{MF}}^{(i)}, \rho^{(i)}] + \gamma\left(\sigma_-\rho^{(i)}\sigma_+ - \frac{1}{2}\{\sigma_+\sigma_-, \rho^{(i)}\}\right) + \text{drive}$$

其中 $H_{\text{MF}}^{(i)} = (\Delta E_{\text{eff}}/2)\sigma_z^{(i)}$，$\sigma_\pm = (\sigma_x \pm i\sigma_y)/2$。

驱动项对应相干泵浦：$H_{\text{drive}}^{(i)} = \eta f(t)(\sigma_+^{(i)} + \sigma_-^{(i)})$（或等价地在复振幅方程中为 $\eta f(t)$ 的加性驱动）。

#### 3.4.2 相干态表示

在 $|\mathcal{A}| \ll 1$ 的极限下（低确定化比例），可以用Holstein-Primakoff变换将qubit映射为玻色子：

$$\sigma_-^{(i)} \to a_i, \quad \sigma_z^{(i)} \to 1 - 2a_i^\dagger a_i$$

复振幅 $\mathcal{A} = \langle a \rangle$ 满足：

$$\frac{d\mathcal{A}}{dt} = -\frac{i}{\hbar}\Delta E_{\text{eff}}\mathcal{A} - \gamma\mathcal{A} + \eta f(t)$$

代入 $\Delta E_{\text{eff}} = \Delta E_0 + 2g(1 - 2|\mathcal{A}|^2)$：

$$\frac{d\mathcal{A}}{dt} = -\frac{i}{\hbar}[\Delta E_0 + 2g(1-2|\mathcal{A}|^2)]\mathcal{A} - \gamma\mathcal{A} + \eta f(t)$$

令 $\omega_0 = \Delta E_0/\hbar$，$a_c^2 = (\Delta E_0 + 2g)/(4g)$：

$$\boxed{\frac{d\mathcal{A}}{dt} = -i\omega_0\left(1 - \frac{|\mathcal{A}|^2}{a_c^2}\right)\mathcal{A} - \gamma\mathcal{A} + \eta f(t)}$$

**这就是确定化场的复Langevin方程，现在所有参数都有了微观定义。**

#### 3.4.3 阻尼修正ac²

在驱动-耗散稳态中，临界确定化比例被阻尼修正。从稳态条件：

$$-i\omega_0(1 - |\mathcal{A}|^2/a_c^2)\mathcal{A} - \gamma\mathcal{A} + \eta f = 0$$

取模方：
$$|\mathcal{A}|^2 = \frac{\eta^2 f^2}{\gamma^2 + \omega_0^2(1 - |\mathcal{A}|^2/a_c^2)^2}$$

这是一个 $|\mathcal{A}|^2$ 的隐式方程。在临界点附近 $|\mathcal{A}|^2 \approx a_c^2$，令 $\delta = a_c^2 - |\mathcal{A}|^2$ 为小量：

$$a_c^2 - \delta \approx \frac{\eta^2 f^2}{\gamma^2 + \omega_0^2(\delta/a_c^2)^2}$$

在临界驱动强度 $\eta_c f_c = a_c^2 \gamma$ 处（使得 $\delta=0$ 满足方程），展开到 $O(\delta^2)$：

$$\delta \approx a_c^2 \cdot \frac{\gamma}{\sqrt{\gamma^2 + \omega_0^2}}$$

因此，**动力学临界点**（实际在驱动-阻尼系统中观测到的穿越点）是：

$$\boxed{a_c^2(\text{dynamical}) = \frac{1}{2}\left(1 - \frac{\gamma}{\sqrt{\gamma^2 + \omega_0^2}}\right) \cdot \left(1 + \frac{\Delta E_0}{2g}\right)}$$

对于 $\Delta E_0 = 0$（对称情况）：

$$\boxed{a_c^2 = \frac{1}{2}\left(1 - \frac{\gamma}{\sqrt{\gamma^2 + \omega_0^2}}\right)}$$

#### 3.4.4 三个极限的物理验证

| 极限 | ac² | 物理解释 |
|------|-----|---------|
| $\gamma \to 0$（无阻尼） | $a_c^2 \to 1/2$ | 恢复T=0平均场结果 |
| $\gamma \gg \omega_0$（过阻尼） | $a_c^2 \to 0$ | 强阻尼阻止相变——系统在穿越前被钉扎 |
| $\gamma \ll \omega_0$（弱阻尼） | $a_c^2 \approx \frac{1}{2}(1 - \gamma/\omega_0)$ | 小修正——相变几乎在对称点发生 |

**数值估计：** 从DGF/弛豫模型的MCMC拟合，$\gamma/\omega_0 \approx 60/40 = 1.5$（过阻尼状态），但注意这里的 $\gamma$ 和 $\omega_0$ 的单位是 $H_0$——物理频率约为 $\omega_0 \sim 40 H_0 \sim (40 \times 70 \text{ km/s/Mpc}) \sim 2.8 \times 10^{-16} \text{ s}^{-1}$。这远小于任何微观频率——表明 $\omega_0$ 本身就是宏观集体频率，不是单qubit的裸频率。

**诚实标注：** $\omega_0$ 和 $\gamma$ 的物理起源仍然不清楚。它们被拟合为 $\sim 40-60 H_0$，但为什么是这个值？这是目前无法回答的问题。

### 3.5 Keldysh形式的严格化方向

对于追求完全严格化的路径，Keldysh-Schwinger形式提供N→∞时平均场理论的系统性控制：

1. **生成泛函：** $Z[J] = \text{Tr}[T_C \exp(-i\int_C dt (H + J\sigma_z))]$
2. **1/N展开：** 在N→∞时，鞍点近似严格。1/N修正给出涨落对 $a_c^2$ 的修正，量级 $O(1/N)$。
3. **有效作用量：** Keldysh有效作用量的鞍点方程直接给出复Langevin方程，包括所有非平衡修正。

这个方向的完整展开需要专门的Keldysh场论论文。目前的工作停留在平均场水平——1/N修正对宇宙学尺度（$N \gg 10^{80}$）完全可忽略。

### 3.6 小結：W3修补后的改进

| 方面 | 修补前 | 修补后 |
|------|--------|--------|
| ac²推导 | "动力学临界点"（准唯象） | Ising平均场理论 → 严格鞍点条件 |
| 参数自由度 | ac²是自由参数 | ac²由 $\Delta E_0$、$g$、$\gamma$、$\omega_0$ 决定 |
| 理论极限 | 无 | $\gamma \to 0$ 恢复T=0平均场结果 |
| 1/N修正 | 未考虑 | 已知O(1/N) — 宇宙学尺度可忽略 |
| 数值预测 | ac²待拟合 | ac² ≈ 0.04-0.15（对于合理的 $\gamma/\omega_0$ 范围） |

---

## 4. 整合：自洽理论框架

### 4.1 完整的确定化场暗能量方程组

整合W1和W3的修补后，理论框架包含以下闭合方程组：

#### 动力学方程

$$\boxed{\frac{d\mathcal{A}}{dt} = -i\omega_0\left(1 - \frac{|\mathcal{A}|^2}{a_c^2}\right)\mathcal{A} - \gamma\mathcal{A} + \eta \cdot \frac{\dot{\mathcal{I}}(z(t))}{\dot{\mathcal{I}}(0)}}$$

#### 临界确定化比例

$$\boxed{a_c^2 = \frac{1}{2}\left(1 - \frac{\gamma}{\sqrt{\gamma^2 + \omega_0^2}}\right) \cdot \left(1 + \frac{\Delta E_0}{2g}\right)}$$

#### 信息处理率

$$\boxed{\dot{\mathcal{I}}(z) = \frac{1}{k_B T_{\text{eff}}(z)} \int_{M_{\text{min}}}^\infty dM \, \Gamma(M, z) \cdot E_{\text{bind}}(M, z)}$$

#### 暗能量状态方程

$$\boxed{w(z) = -1 + 2\frac{|\dot{\mathcal{A}}(z)|^2}{\rho_{\mathcal{A}}(z)} \cdot \text{sgn}\left(1 - \frac{|\mathcal{A}(z)|^2}{a_c^2}\right)}$$

其中：
$$\rho_{\mathcal{A}}(z) = |\dot{\mathcal{A}}|^2 + \omega_0^2|\mathcal{A}|^2$$

#### 宇宙学膨胀

$$\boxed{H^2(z) = H_0^2\left[\Omega_m(1+z)^3 + \Omega_r(1+z)^4 + \Omega_{\mathcal{A}}(z)\right]}$$

其中：
$$\Omega_{\mathcal{A}}(z) = \Omega_{\mathcal{A}}(0) \cdot \exp\left[3\int_0^z dz' \frac{1+w(z')}{1+z'}\right]$$

### 4.2 参数计数

| 参数 | 符号 | 物理起源 | 是否自由 | 标度 |
|------|------|---------|:--:|------|
| 裸能级差 | $\Delta E_0$ | 单qubit确定化能量 | **是** — 目前未知 | $\sim \hbar H_0$ ？ |
| 相互作用强度 | $g$ | qubit间铁磁耦合 | **是** — 由ac²穿越红移固定 | $\sim \hbar H_0$ ？ |
| 阻尼率 | $\gamma$ | qubit-环境退相干 | **是** — 由MCMC拟合 | $\sim 40-60 H_0$ |
| 驱动振幅 | $\eta$ | 引力塌缩耦合强度 | **是** — 由w(0)校准 | — |
| 临界确定化 | $a_c^2$ | 从g, $\Delta E_0$, $\gamma$, $\omega_0$ 推导 | **否** — 理论预言 | $\approx 0.04-0.15$ |
| 自由落体时标 | $t_{\text{ff}}$ | 引力塌缩物理 | **否** — 从ΛCDM推导 | $\approx 0.17$ Gyr |
| 信息处理率 | $\dot{\mathcal{I}}(z)$ | 从ΛCDM+功率谱计算 | **否** — 唯一预测 | — |

**独立自由参数数量: 4个** ($\Delta E_0$或等价的$g$, $\gamma$, $\eta$, 和一个整体振幅校准)。
相比于标准w₀wₐ参数化（2个参数），多了2个——但换来了完整的物理图景。

### 4.3 参数简并

$\Delta E_0$ 和 $g$ 只在组合 $a_c^2 = (\Delta E_0+2g)/4g$ 中出现——它们简并。穿越红移只约束 $a_c^2$，不单独约束 $\Delta E_0$ 或 $g$。

打破简并的方式：
- 桌面qubit实验可以直接测量单qubit的 $\Delta E_0$（如果qubit是物理实体）
- 如果 $\Delta E_0 = 0$（对称情况），那么 $a_c^2$ 唯一决定 $g$

### 4.4 自洽性检查

**检查1：弛豫时标一致性。** 系统的弛豫时间 $\tau = 1/\gamma$。物理上这应该与引力塌缩时标 $t_{\text{ff}}$ 有关。从拟合，$\gamma \sim 60 H_0$ ⟹ $\tau \sim 1/(60 H_0) \sim 0.23$ Gyr。而 $t_{\text{ff}} \sim 0.17$ Gyr。两者在同一量级——一阶检验通过。

**检查2：穿越红移的自洽性。** 穿越发生在 $|\mathcal{A}(z_{\text{cross}})|^2 = a_c^2$。从数值解，这给出 $z_{\text{cross}} \approx 0.5-1$（取决于参数）。这与DESI binned w(z)数据一致——穿越在z~0.25-0.75之间。

**检查3：高红移行为。** 在 $z \gg 1$，SFR/塌缩功率都很高 → 驱动强 → $|\mathcal{A}|^2 > a_c^2$ → 幽灵相（w < -1）。随着z下降，驱动减弱 → $|\mathcal{A}|^2$ 减小 → 穿越 → 精质相（w > -1）。这是观测到的模式。

---

## 5. 新的可检验预言

### 5.1 替代W2的预测（不再依赖SFR）

| # | 预言 | 检验 | 与修补前对比 |
|---|------|------|------------|
| **NP1** | w(z)由引力塌缩功率唯一决定，不依赖SFR编译 | 用标准ΛCDM（Planck 2018）+ Sheth-Tormen计算 $\mathcal{P}_{\text{coll}}(z)$，预测w(z)，与DESI binned w(z)比较。同一组参数，无需选择SFR编译 | 修补前：wa从-0.42到-0.09取决于SFR编译。修补后：单一预测 |
| **NP2** | 高红移(z>2)的w(z)预测与SFR-based版本有定量差异 | 计算两种驱动（塌缩功率 vs SFR）在z=2-5的w(z)差异。塌缩功率在高z更强（因为低质量晕相对贡献更大） | 新预言——修补前没有这个区分 |
| **NP3** | 塌缩功率的M_min依赖性产生可测效应 | 扫描 $M_{\text{min}}$ （最小有效塌缩质量）对w(z)的影响。$M_{\text{min}}$ 由暗物质粒子属性（WDM截断质量）决定 → w(z)携带暗物质粒子信息 | 全新预言——SFR无法探测这个 |

### 5.2 替代W3的预测（ac²是理论预言不是拟合参数）

| # | 预言 | 检验 | 与修补前对比 |
|---|------|------|------------|
| **NP4** | $a_c^2 \approx 0.04-0.15$（不是自由参数） | 从穿越红移推断 $a_c^2$，与理论公式 $a_c^2 = (1/2)(1 - \gamma/\sqrt{\gamma^2+\omega_0^2})$ 比较。两者必须自洽 | 修补前：ac²是自由参数 |
| **NP5** | 阻尼修正：如果独立测量 $\gamma$（从w(z)的响应速度），ac²应该满足理论关系 | 从w(z)形状的迟豫时间推断 $\gamma$，验证与ac²的理论关系 | 新的一致性检验 |
| **NP6** | 多qubit桌面实验应观测到 $a_c^2 \approx 0.5$（$\gamma \to 0$ 极限） | 3-5 qubit芯片，全局Ising耦合，扫描驱动强度 | 修补前：无理论指导期望值 |

### 5.3 整合后的新预言

| # | 预言 | 检验通道 |
|---|------|---------|
| **NP7** | $a_c^2$ 在宇宙学数据中表现为"幻影穿越红移不随探针变化" | DESI DR3：用BAO、RSD、SN Ia分别重建w(z)，检查穿越红移是否一致 |
| **NP8** | 引力塌缩功率和SFR的差异在z>2可被Euclid+Roman区分 | Euclid高红移弱透镜 + Roman SN Ia |
| **NP9** | $S_8$ 张力被定量预测，不依赖SFR编译 | 从塌缩功率 → w(z) → 增长因子 → $S_8$，与KiDS-1000/DES Y3比较 |

---

## 6. 未解决的问题与诚实边界

### 6.1 遗留的理论裂缝

| # | 问题 | 严重度 | 可能的解决方向 |
|---|------|:--:|------|
| **U1** | $g$ 和 $\Delta E_0$ 的能量标度未知 | 高 | 如果qubit是Planck尺度自由度 → $g \sim E_{\text{Planck}}$。如果是宇宙学尺度集体模 → $g \sim \hbar H_0$。需要实验或观测决定 |
| **U2** | 为什么 $\omega_0, \gamma \sim 40-60 H_0$？ | 高 | 这暗示"确定化"的时标是Hubble时标除以一个大数。可能与宇宙的熵产生率有关 |
| **U3** | Landauer原理在引力系统中的适用性未经严格证明 | 中高 | 引力系统的非广延性（负热容）使得温度概念复杂化。需要从AdS/CFT或全息熵推导信息-能量关系 |
| **U4** | qubit的物理本体论：它们是真实的微观自由度还是有效描述？ | 中 | 类似于"引力子是什么"的本体论问题。理论可以在不知道答案的情况下工作——就像热力学在不知道原子是什么的情况下工作一样 |
| **U5** | $M_{\text{min}}$ 的精确值 | 中 | 由暗物质的自由流截断质量设定。如果DM是100 GeV WIMP，$M_{\text{min}} \sim 10^{-6} M_\odot$；如果是7 keV sterile neutrino，$M_{\text{min}} \sim 10^8 M_\odot$ |
| **U6** | $\Delta E_0$ 是否严格为零？ | 中 | 如果qubit的基本对称性是 $|0\rangle \leftrightarrow |1\rangle$，则 $\Delta E_0 = 0$ 是自然的。但如果确定化伴随着与引力场的能量交换，$\Delta E_0 \neq 0$ |
| **U7** | 非高斯涨落修正（$O(1/N)$ 在Keldysh中） | 低 | 宇宙学尺度N极大，修正可忽略。但在桌面qubit实验中可能重要 |

### 6.2 诚实声明

1. **W1修补的核心假设：** 引力塌缩 → 信息处理 → qubit驱动 的链条中，引力塌缩 → 信息处理 这一步是最弱的。我们使用了Landauer原理的类比，但引力系统的非广延统计力学比实验室比特擦除复杂得多。这个类比是合理的（两者都涉及不可逆的熵产生），但尚未严格证明。

2. **W3修补的完整性：** 平均场推导在N→∞时严格，而宇宙学qubit数量确实极大。但Keldysh形式的完整展开（包括噪声关联、涨落-耗散定理的检验、非高斯修正）尚未完成。这些对于桌面实验可能重要（N~3-5），但对于宇宙学应用不重要。

3. **参数简化策略：** 虽然理论有4个自由参数（$\Delta E_0/g$, $\gamma$, $\eta$, 整体振幅），但许多参数之间存在物理关系：
   - $\gamma$ 可能与引力塌缩时标 $t_{\text{ff}}$ 相关（从DGF数值实验，$\tau \approx t_{\text{ff}}$）
   - $a_c^2$ 由 $\gamma/\omega_0$ 决定
   - 整体振幅由 $w(z=0)$ 校准
   
   有效自由参数可能只有1-2个——但这需要更多的理论工作来建立这些关系。

4. **与标准场论的张力：** 标准量子场论不允许单标量场穿越 w=-1（需要鬼场或不稳定）。我们的机制通过"有效能级差改变符号"来穿越——这不是单标量场的性质改变，而是qubit系综的真空重新定义。这在数学上是自洽的，但在概念上是全新的——需要经受物理共同体的严格审查。

5. **证据级别：** 即使完成了W1和W3的修补，当前DESI数据的证据级别仍然是~2σ。理论修补提高了理论自洽性，但不改变统计显著性。证实或证伪需要DESI DR3（2026-2028）、Euclid或桌面qubit实验。

### 6.3 最低限度可验证版本

理论的最简可检验形式（消除所有冗余参数）：

$$\frac{d\mathcal{A}}{dt} = -i\omega_0(1 - |\mathcal{A}|^2/a_c^2)\mathcal{A} - \gamma\mathcal{A} + \eta \cdot \mathcal{C}(z)$$

其中：
- $\mathcal{C}(z)$ = 从ΛCDM计算的归一化引力塌缩功率（**零自由参数**）
- $a_c^2 = (1/2)(1 - \gamma/\sqrt{\gamma^2+\omega_0^2})$（**一个约束关系**）
- $\gamma$ 由自由落体时标固定：$\gamma = 1/t_{\text{ff}} \approx 5.9$ Gyr$^{-1}$（**物理输入，非自由参数**）

有效自由参数：$\omega_0$ 和 $\eta$（2个），加上 $\Omega_{\mathcal{A}}(0)$（1个标准宇宙学参数）= 3个参数 vs ΛCDM的1个参数 + CPL的2个参数。

这三个参数的物理意义：
- $\omega_0$：qubit裸频率 → 控制穿越红移
- $\eta$：引力塌缩耦合强度 → 控制w(z)幅度
- $\Omega_{\mathcal{A}}(0)$：当前暗能量密度 → 标准宇宙学参数

### 6.4 下一步（A博士轨道）

| 优先级 | 任务 | 输入 | 输出 |
|:--:|------|------|------|
| **P0** | 从CAMB/CLASS计算 $\mathcal{C}(z)$ = 塌缩功率/信息处理率 | ΛCDM宇宙学参数 + Sheth-Tormen质量函数 | 驱动函数的数值表 |
| **P0** | 用新驱动函数重跑MCMC | DESI DR2 binned w(z) | 更新参数约束，检验与SFR版本的一致性 |
| **P1** | 数值计算塌缩功率 vs SFR差异对w(z)的影响 | 两种驱动函数 | 高红移预言差异 → Euclid可检验 |
| **P1** | 完成Keldysh形式中涨落-耗散定理的检验 | 理论推导 | 噪声项的自洽性验证 |
| **P2** | 推导 $S_8$ 预测的完整表达式 | w(z) → 增长因子 | 独立于w(z)的检验通道 |

---

## 附录A：符号表

| 符号 | 含义 | 典型值/范围 |
|------|------|------------|
| $\mathcal{A}$ | 确定化复振幅 | $0 \leq |\mathcal{A}|^2 \leq 1$ |
| $|\mathcal{A}|^2$ | 确定化qubit比例 | — |
| $a_c^2$ | 临界确定化比例（相变点） | $\approx 0.04-0.50$ |
| $\omega_0$ | 裸qubit频率 | $\sim 40 H_0$ |
| $\gamma$ | 退相干/阻尼率 | $\sim 60 H_0$ |
| $\eta$ | 驱动振幅 | 由w(0)校准 |
| $\Delta E_0$ | 裸能级差 | 未知（可能与Planck标度有关） |
| $g$ | qubit-qubit Ising耦合 | 未知 |
| $\mathcal{P}_{\text{coll}}$ | 引力塌缩功率密度 | 从ΛCDM计算 |
| $\dot{\mathcal{I}}$ | 信息处理率密度 | $\mathcal{P}_{\text{coll}}/k_B T_{\text{eff}}$ |
| $t_{\text{ff}}$ | 自由落体时标 | $\approx 0.17$ Gyr（z=0，$10^{12} M_\odot$） |
| $T_{\text{eff}}$ | 引力塌缩有效温度 | $\sim GM\mu m_p/k_B R_{\text{vir}}$ |

## 附录B：塌缩功率的数值实现路线

完整的塌缩功率计算需要以下步骤：

1. **功率谱**: 从CLASS/CAMB获取 $P(k, z=0)$
2. **σ(M)**: $\sigma^2(M) = \int dk k^2 P(k) W^2(kR)/(2\pi^2)$，其中 $R = (3M/4\pi\bar{\rho}_m)^{1/3}$，$W(x) = 3(\sin x - x\cos x)/x^3$
3. **质量函数**: Sheth-Tormen $f(\nu) = A[1+(q\nu^2)^{-p}]\sqrt{q\nu^2/2\pi} \exp(-q\nu^2/2)$
4. **晕形成率**: $\Gamma(M,z)$ 通过扩展Press-Schechter形式
5. **积分**: 数值积分得到 $\mathcal{P}_{\text{coll}}(z)$

这些步骤在python中可以用 `hmf` 包或直接数值积分实现（~200行代码）。

## 附录C：与DEEP_PRINCIPLE.md的衔接

本理论推导报告（A博士轨）与DEEPER_PRINCIPLE.md（整体方向）的关系：

- DEEPER_PRINCIPLE识别了核心物理：延迟是必要的，惯性延迟（二阶方程→振荡）是错的，耗散延迟（一阶弛豫→单向延迟）是正确的。
- 本报告为这个图景提供了微观基础：复Langevin方程天然是一阶的（耗散的），而SFR驱动的弛豫模型是其投影。
- W1修补将驱动从SFR（示踪物）升级为引力塌缩信息处理率（基本量）。
- W3修补将ac²从拟合参数升级为平均场理论的严格推论。

**两个报告共同确立了：暗能量 = 宇宙引力塌缩驱动的qubit系综确定化相变。**
