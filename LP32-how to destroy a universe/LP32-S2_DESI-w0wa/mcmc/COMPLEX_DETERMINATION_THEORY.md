# 确定化场的复动力学与幻影穿越（修正版）

**日期:** 2026-06-08
**状态:** 修正v1的数学错误——幻影穿越来自ΔE符号翻转，不是V''符号

---

## 0. 修正v1的致命错误

v1声称：$V(|\mathcal{A}|^2) = V_0|\mathcal{A}|^2(1-|\mathcal{A}|^2)$，幻影穿越在 $|\mathcal{A}|^2 = 1/2$ 时发生。

**这是错的。** $V(|\mathcal{A}|^2) \geq 0$ 在 $|\mathcal{A}|^2 \in [0,1]$ 恒成立。标准标量场 $w = (K-V)/(K+V) \geq -1$ 永远不能产生 $w < -1$。

**正确的机制：** 真正被平方掩盖的符号是 $\omega_0^2 = (\Delta E/\hbar)^2$。$\Delta E = E_1 - E_0$ 可以改变符号——当确定化qubit的基态从 $|0\rangle$ 翻转到 $|1\rangle$ 时。$\omega_0^2$ 这个平方永远为正，掩盖了 $\Delta E$ 的符号翻转。

---

## 1. 基本变量：确定化振幅

qubit态：$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$，$|\alpha|^2 + |\beta|^2 = 1$

确定化复振幅：$\mathcal{A} = \beta = |\beta|e^{i\theta}$

DGF追踪：$q = |\alpha|^2$，$\Delta = |\beta|^2 = |\mathcal{A}|^2$（模方——丢了相位）

---

## 2. 动力学：能级差ΔE的符号翻转

### 2.1 单qubit能级

$|0\rangle$ = 未确定态，$|1\rangle$ = 确定态

单qubit Hamiltonian：$H_{\text{qubit}} = E_0|0\rangle\langle 0| + E_1|1\rangle\langle 1|$

能级差：$\Delta E = E_1 - E_0$

### 2.2 多体效应：平均场能级重整化

在宇宙学尺度的qubit系综中，每个qubit感受到的**有效**能级差依赖于周围已确定qubit的比例：

$$\Delta E_{\text{eff}}(t) = \Delta E_0 - g \cdot \frac{N_{\text{det}}(t)}{N_{\text{total}}} = \Delta E_0 \left(1 - \frac{|\mathcal{A}(t)|^2}{|\mathcal{A}|^2_{\text{crit}}}\right)$$

其中 $|\mathcal{A}|^2_{\text{crit}} = \Delta E_0/g$ 是临界确定化比例。

**物理图像：** 每个确定化事件释放/消耗能量。当足够多的qubit已被确定化，系综的"真空"翻转——$|1\rangle$ 成为新的基态。这是**驱动量子相变**（driven quantum phase transition）。

### 2.3 ΔE符号翻转的三个阶段

| 阶段 | $|\mathcal{A}|^2$ | $\Delta E_{\text{eff}}$ | 暗能量 | 对应宇宙学时期 |
|------|------------------|------------------------|--------|--------------|
| I | $< |\mathcal{A}|^2_{\text{crit}}$ | $> 0$ | 精质（w > -1） | z < z_cross（晚期） |
| II | $= |\mathcal{A}|^2_{\text{crit}}$ | $= 0$ | w = -1（穿越） | z = z_cross |
| III | $> |\mathcal{A}|^2_{\text{crit}}$ | $< 0$ | 幽灵（w < -1） | z > z_cross（早期） |

**穿越在 $\Delta E_{\text{eff}} = 0$ 时自动发生——无需精细调参。**

---

## 3. 动力学方程（修正后）

### 3.1 复Langevin方程

$$\frac{d\mathcal{A}}{dt} = -i\frac{\Delta E_{\text{eff}}(t)}{\hbar}\mathcal{A} - \gamma\mathcal{A} + \eta f(t)$$

代入 $\Delta E_{\text{eff}}$ 的形式：

$$\boxed{\frac{d\mathcal{A}}{dt} = -i\omega_0\left(1 - \frac{|\mathcal{A}|^2}{a_c^2}\right)\mathcal{A} - \gamma\mathcal{A} + \eta f(t)}$$

其中：
- $\omega_0 = \Delta E_0/\hbar$（裸能级频率）
- $a_c^2 = |\mathcal{A}|^2_{\text{crit}}$（临界确定化比例）
- $\gamma$：退相干/阻尼速率
- $\eta f(t)$：外部驱动（$f(t) = \text{SFR}(t)/\text{SFR}(0)$）
- 非线性项 $-i\omega_0(|\mathcal{A}|^2/a_c^2)\mathcal{A}$ 来自平均场反馈

### 3.2 相比于DGF电报方程

| 性质 | DGF电报方程 | 确定化复场 |
|------|-----------|----------|
| 阶数 | 二阶（实） | 一阶（复） |
| 变量 | $\Delta$（实数） | $\mathcal{A}$（复数） |
| 非线性 | $\gamma_0\Delta^n\dot{\Delta}$ | $-i\omega_0(|\mathcal{A}|^2/a_c^2)\mathcal{A}$ |
| 振荡 | 欠阻尼→振荡赝像 | 无振荡（一阶耗散） |
| 幻影穿越 | 需要精细调参 | **ΔE符号翻转——自动** |
| 自由参数 | 4个 | 4个（$\omega_0,\gamma,\eta,a_c$），但 $a_c$ 由穿越红移固定 |

### 3.3 为什么这是一阶的、不振荡的

复Langevin方程是**一阶**的。演化是弛豫+旋转。没有二阶惯性项——DGF的 $\ddot{\Delta}$ 是复动力学投影到实轴的人为产物。

系统的特征值是 $\lambda = -\gamma \pm i\omega_{\text{eff}}$。实部恒为负（$-\gamma < 0$）→ 所有模都是**衰减**的——没有持续振荡。相位旋转提供"惯性"（延迟），但不产生谐振子式的过冲。

---

## 4. 暗能量状态方程

### 4.1 确定化场的能量-动量

确定化场的"能量"来自两个源：
1. **振幅动力学：** $K_a = |\dot{\mathcal{A}}|^2$——确定化比例的变更率
2. **相位动力学：** $K_\theta = |\mathcal{A}|^2\dot{\theta}^2$——确定化相位的旋转率

$\dot{\theta}$ 由方程给出：$\dot{\theta} = -\omega_0(1 - |\mathcal{A}|^2/a_c^2) - \frac{\eta f(t)}{|\mathcal{A}|}\sin\theta$

**当 $\omega_0(1 - |\mathcal{A}|^2/a_c^2)$ 改变符号（穿越临界点），$\dot{\theta}$ 的主导项翻转符号 → 相位动力学的有效压力改变符号 → w穿越-1。**

### 4.2 w(z)的计算

$$w(z) = -1 + 2\frac{|\dot{\mathcal{A}}(z)|^2}{\rho_{\mathcal{A}}(z)} \cdot \text{sgn}(\Delta E_{\text{eff}}(z))$$

其中 $\text{sgn}(\Delta E_{\text{eff}}) = \text{sgn}(1 - |\mathcal{A}|^2/a_c^2)$。

- $|\mathcal{A}|^2 < a_c^2$：$\text{sgn} > 0$ → $w > -1$（精质）
- $|\mathcal{A}|^2 > a_c^2$：$\text{sgn} < 0$ → $w < -1$（幽灵）

### 4.3 数值实现

在实际计算中，从 $\mathcal{A}(t)$ 的数值解直接计算：

$$\rho_{\mathcal{A}} = |\dot{\mathcal{A}}|^2 + V_0|\mathcal{A}|^2$$
$$P_{\mathcal{A}} = |\dot{\mathcal{A}}|^2 \cdot \text{sgn}(\Delta E_{\text{eff}}) - V_0|\mathcal{A}|^2$$
$$w = P_{\mathcal{A}}/\rho_{\mathcal{A}}$$

$V_0$ 和整体振幅由 $w(z=0) \approx -0.785$ 校准。

---

## 5. 可检验预言

### 5.1 宇宙学

| 预言 | 检验 |
|------|------|
| w(z)在某个红移穿越-1（$\Delta E_{\text{eff}}=0$） | DESI DR2 binned w(z)：已观测到bin1(w>-1)→bin3(w<-1)穿越 |
| 穿越红移由SFR峰值红移决定：$z_{\text{cross}} \approx z_{\text{SFR peak}} - \delta z$ | DESI穿越在z~0.5-1，SFR峰在z~2，δz~1-1.5来自弛豫延迟 |
| w(z)在精质区单调向w>-1演化 | DESI bin1 (z=0.25): w=-0.72 > -1，与预言一致 |
| $a_c^2$（临界确定化比例）是普适常数 | 从穿越红移校准后，应在所有宇宙学探针中保持一致 |

### 5.2 量子模拟

单qubit系统可以直接模拟这个动力学：
- 驱动：Rabi脉冲（对应SFR驱动 $\eta f(t)$）
- 退相干：环境耦合（对应 $\gamma$）
- 平均场反馈：用测量-反馈回路实现 $|\mathcal{A}|^2$ 依赖的能级移动
- 幻影穿越：当布居数穿越临界值 $a_c^2$ 时，有效Rabi频率改变符号

---

## 6. 与现有文献的关系

- **DGF (LP32)：** 提供了确定化→暗能量的基本图景，但用实变量Δ丢失了相位。电报方程是复动力学在实轴上的不完整投影。
- **DM-DE相互作用模型 (Khoury+Lin+Trodden 2025)：** 表观幻影穿越来自DM质量演化。我们的机制是内禀的——来自确定化场的量子相变。
- **Horndeski/KGB (Linder 2025, Cataneo+ 2025)：** 修改引力产生幻影穿越。我们的机制不需要修改引力——相变发生在物质扇区（qubit系综），通过标准引力耦合影响膨胀。
- **相变暗能量 (Linder 2024, "mirage DE")：** 最接近的精神前身。Linder提出"真空蜕变"（vacuum metamorphosis）产生幻影穿越。我们的具体实现是：qubit系综的基态翻转 = 真空蜕变。

---

## 7. 下一步

1. **数值求解完整的非线性复方程**，与DESI binned w(z)比较
2. **从第一原理推导 $a_c^2$**：在qubit系综的Hubbard-Stratonovich平均场理论中，$a_c^2 = 1/2$ 来自二能级系统的对称性
3. **量子模拟实验设计**：单qubit + 反馈回路 → 桌面宇宙学
