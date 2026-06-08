# LP-22: Mott-Ioffe-Regel极限隐藏假设 — 形式推导

> 日期: 2026-06-03
> 状态: Phase 0 — 隐藏假设精确化与量级估算
> 子命题: S0 — 关联重正化对MIR判据的污染

---

## 0. 问题陈述

### 标准MIR论证（H）

传统论证如下：

1. 金属电阻率: $\rho = m^*/(n e^2 \tau)$
2. 平均自由程: $l = v_F \tau$
3. 当 $l$ 缩减到一个原子间距 $a$ 时, $k_F l \approx k_F a \approx (2\pi/a) \cdot a/(2\pi) \approx 1$
4. 此时准粒子图像自洽性丧失（$\Delta E \tau \approx \hbar$ → 能量不确定性超过费米能量）
5. 结论: $\rho$ 在 $k_F l = 1$ 处"饱和"（Mott极限 $\rho_{\text{Mott}} \approx ha/e^2$）

这个论证被广泛接受为"坏金属"的定义标准。

### 隐藏假设的识别

上述论证中**每一个等号都隐含了费米液体理论的假设**：

- **步骤1**: Drude公式 $\rho = m^*/(ne^2\tau)$ 中的 $n$ 和 $m^*$ 是**裸**电子密度和有效质量还是**重正化**后的？
- **步骤2**: $v_F$ 是裸费米速度 $v_F^0 = \hbar k_F^0/m$ 还是重正化的 $v_F^* = Z \cdot v_F^0$？
- **步骤3**: $a$ 是原子间距还是关联长度？$k_F$ 是裸费米波矢还是包含了Luttinger定理的重正化值？

### 核心洞察

**关联效应系统性地重正化了进入MIR判据的所有物理量，但标准论证在应用时隐式地使用了裸（非相互作用）值。**

如果采用重正化后的值，表观的"$k_F l = 1$ 饱和"可能对应真实准粒子平均自由程 $k_F^* l^* \gg 1$。

---

## 1. 形式体系

### 1.1 关联金属的谱表示

考虑一个强关联电子系统，其单粒子格林函数：

$$G(k, \omega) = \frac{Z_k}{\omega - \epsilon_k^* - i\Gamma_k(\omega)} + G_{\text{incoh}}(k, \omega)$$

其中:
- $Z_k \in [0,1]$: 准粒子残基 (quasiparticle residue)
- $\epsilon_k^* = Z_k(\epsilon_k^0 - \mu + \text{Re}\Sigma(k,0))$: 重正化色散
- $\Gamma_k(\omega) = -Z_k \text{Im}\Sigma(k,\omega)$: 散射率
- $G_{\text{incoh}}$: 非相干连续谱

### 1.2 重正化的Drude权重

光学求和规则给出Drude权重:

$$D = \frac{\pi n e^2}{2m} \cdot \frac{1}{V} \sum_{k,\sigma} n_k \frac{\partial^2 \epsilon_k^0}{\partial k_x^2} \bigg|_{\text{coh}}$$

在关联系统中，只有相干部分贡献Drude权重:

$$D = \frac{\pi n e^2}{2m^*} Z \equiv \frac{\pi n e^2}{2m_{\text{opt}}}$$

其中 $m_{\text{opt}} = m^*/Z$ 是光学有效质量。

### 1.3 重正化的输运量

| 物理量 | 裸值（非相互作用） | 重正化值（关联） | 重正化因子 |
|--------|-------------------|-----------------|-----------|
| 费米速度 | $v_F^0 = \hbar k_F^0/m$ | $v_F^* = Z \cdot v_F^0 \cdot (m/m^*)$ | $\propto Z \cdot m/m^*$ |
| 有效质量 | $m^*_{\text{band}}$ | $m^*_{\text{corr}} = m^*_{\text{band}}/Z$ | $1/Z$ |
| 费米波矢 (Luttinger) | $k_F^0 = (3\pi^2 n)^{1/3}$ | $k_F^* = k_F^0$ (Luttinger定理保护) | 1 |
| 态密度 | $N^0 = m^* k_F^0/\pi^2\hbar^2$ | $N^* = N^0/Z$ | $1/Z$ |
| 电阻率 | $\rho^0 = m/(n e^2 \tau^0)$ | $\rho^* = m^*/(n e^2 Z \tau^*) = m/(n e^2 Z \tau^*\cdot m/m^*)$ | 复杂 |

---

## 2. 核心推导: MIR判据在关联系统中的分解

### 2.1 标准MIR判据

标准叙述:

$$\rho_{\text{MIR}} = \frac{h a}{e^2} \approx \frac{2\pi\hbar a}{e^2} \sim 1-10 \text{ m}\Omega\cdot\text{cm}$$

推导: $k_F l = 1 \Rightarrow (3\pi^2 n)^{1/3} \cdot v_F \tau = 1$

代入 $\rho = m/(ne^2\tau)$:

$$\rho_{\text{MIR}} = \frac{m v_F}{n e^2} \cdot \frac{1}{k_F^{-1}} = \frac{\hbar(3\pi^2)^{2/3}}{e^2 n^{1/3}}$$

对典型金属 ($n \sim 10^{22} \text{ cm}^{-3}$, $a \sim 3\text{Å}$):

$$\rho_{\text{MIR}} \approx \frac{h a}{e^2} \sim 1\text{ m}\Omega\cdot\text{cm}$$

### 2.2 关联重正化修正

**关键步骤**: 区分"输运表观值"和"准粒子内禀值"。

#### 输运表观平均自由程 $l_{\text{tr}}$

从电阻率反推的平均自由程:

$$\rho = \frac{1}{e^2} \cdot \frac{1}{N^* v_F^{*2} \tau^*} \cdot \frac{1}{2} \quad \text{(各向同性3D)}$$

重正化修正:

$$N^* = \frac{m^* k_F}{\pi^2 \hbar^2}, \quad v_F^* = \frac{\hbar k_F}{m^*}$$

代入:

$$\rho = \frac{1}{e^2} \cdot \frac{\pi^2 \hbar^2}{m^* k_F} \cdot \frac{m^{*2}}{\hbar^2 k_F^2} \cdot \frac{1}{\tau^*} = \frac{\pi^2 m^*}{e^2 k_F^3} \cdot \frac{1}{\tau^*}$$

输运平均自由程定义为 $l_{\text{tr}} = v_F^* \tau^*$:

$$k_F l_{\text{tr}} = k_F \cdot \frac{\hbar k_F}{m^*} \cdot \tau^* = \frac{\hbar k_F^2}{m^*} \tau^*$$

用电阻率表达:

$$k_F l_{\text{tr}} = \frac{\pi^2 \hbar}{e^2} \cdot \frac{1}{k_F \rho}$$

#### 准粒子内禀平均自由程 $l^*$

内禀平均自由程来自准粒子的量子相干性:

$$l^* = v_F^* \cdot \frac{\hbar}{\Gamma^*} = \frac{\hbar k_F}{m^*} \cdot \frac{\hbar}{\Gamma^*}$$

其中 $\Gamma^* = -Z\text{Im}\Sigma$ 是准粒子散射率（从自能虚部提取）。

在Drude-正则极限下, $\Gamma^* = \hbar/\tau^*$, 所以 $l_{\text{tr}} = l^*$。**但这只在 $Z \approx 1$ 时成立。**

### 2.3 关联修正的核心不等式

在强关联系统中 ($Z \ll 1$):

$$l_{\text{tr}} = v_F^* \tau^*_{\text{tr}} = \frac{\hbar k_F}{m^*} \cdot \frac{1}{\Gamma_{\text{tr}}}$$

而准粒子内禀寿命由:

$$\Gamma_{\text{qp}} = -Z \text{Im}\Sigma(\omega=0)$$

输运寿命和准粒子寿命的关系:

$$\Gamma_{\text{tr}} = \Gamma_{\text{qp}} \cdot \langle 1 - \cos\theta \rangle_{\text{FS}}$$

在大角度散射主导时 $\langle 1-\cos\theta \rangle \sim \mathcal{O}(1)$, 两者可比。在小角度散射主导时 $\Gamma_{\text{tr}} \ll \Gamma_{\text{qp}}$。

**关键**: 表观 $k_F l_{\text{tr}} \approx 1$ 可以来自:

1. **真MIR**: $\Gamma_{\text{qp}} \tau^* \sim \hbar$, 准粒子确实无定义 → 非费米液体
2. **假MIR (重正化污染)**: $Z \ll 1$ 导致 $l_{\text{tr}}$ 被压低, 但 $\Gamma_{\text{qp}} \tau^* \ll \hbar$, 准粒子仍完好 → 费米液体

### 2.4 定量分解

定义重正化MIR参数:

$$\lambda_{\text{MIR}} \equiv \frac{k_F l_{\text{tr}}}{Z}$$

**¬H 的定量表述**: 存在关联金属体系, 其中:

$$\lambda_{\text{MIR}} = \frac{k_F l_{\text{tr}}}{Z} \gg 1 \quad \text{即使} \quad k_F l_{\text{tr}} \approx 1$$

物理含义: 表观MIR饱和 (k_F l_tr ≈ 1) 不代表准粒子死亡, 而只是 $Z$ 因子导致的有效质量增强和速度压低。

---

## 3. 量级估算: ¬H的可观测后果

### 3.1 重正化MIR参数的重整

对于典型的重费米子化合物 (如 YbRh₂Si₂, CeCoIn₅):

| 参数 | 典型值 |
|------|--------|
| 有效质量增强 $m^*/m_{\text{band}}$ | 10-100 |
| 准粒子残基 $Z$ | 0.01-0.1 |
| 裸 $v_F^0$ | $10^6$ m/s |
| 重正化 $v_F^* = Z v_F^0 (m_{\text{band}}/m^*)$ | $10^3-10^4$ m/s |
| 表观 $k_F l_{\text{tr}}$ | 0.5-1.5 (在"坏金属"区) |
| **真实 $\lambda_{\text{MIR}} = k_F l_{\text{tr}}/Z$** | **5-150** |

**结论**: $\lambda_{\text{MIR}} \gg 1$ 在 $\rho \approx \rho_{\text{MIR}}$ 时是**典型的**而非异常的。准粒子可以完好存在, 只是被重正化隐藏了。

### 3.2 可检验预言

如果 ¬H 为真, 以下所有条件应同时成立:

**(P1) 量子振荡与"坏金属"电阻率共存**: 
即使 $k_F l_{\text{tr}} \approx 0.5-1$, 仍应观察到 Shubnikov-de Haas 或 de Haas-van Alphen 振荡。
条件: $\omega_c \tau_{\text{qp}} > 1$, 即 $\mu_0 H \cdot (e\hbar/m^*) \cdot (\hbar/\Gamma_{\text{qp}}) > 1$
在 $Z \ll 1$ 时, $\tau_{\text{qp}}^{-1} = Z \cdot \tau_{\text{tr}}^{-1}$ (近似)
→ 量子振荡条件比经典输运条件宽松 $1/Z$ 倍

**(P2) 比热-电阻率解耦**:
$\gamma = C/T \propto N^* = m^* k_F / (\pi^2 \hbar^2)$ 在 $Z \ll 1$ 时增强
同时 $\rho \propto 1/\tau_{\text{tr}}$ 在 $k_F l_{\text{tr}} \sim 1$ 时饱和
→ $\gamma$ 和 $\rho$ 的乘积在关联金属中应偏离标准MIR预测

**(P3) 光学Drude峰窄化**:
光学电导率 $\sigma_1(\omega)$ 的Drude峰宽度 $\Gamma_{\text{opt}} = \Gamma_{\text{qp}} = Z \cdot \Gamma_{\text{tr}}$
→ 即使DC电阻率达MIR极限, 光学Drude峰仍应尖锐 ($\Gamma_{\text{opt}} \ll k_B T$)

**(P4) 质量重正化与MIR饱和的定量关系**:
$\rho_{\text{sat}} \propto 1/Z$ — 即重正化越强 ($Z$越小), 表观饱和电阻率越高
这应与比热有效质量 $m^*/m_{\text{band}} = 1/Z$ 呈正比

---

## 4. 现有数据中的初步证据

### 4.1 重费米子中的量子振荡

YbRh₂Si₂ 在磁场诱导的反铁磁QCP附近:
- 电阻率显示 $\rho \propto T$ (非费米液体行为), $k_F l_{\text{tr}}$ 估算 ≈ 0.5-2
- 同时观察到清晰的 dHvA 振荡 (Taufour et al., 2011; Friedemann et al., 2014)
- 这表明准粒子在输运"坏金属"区仍然存在

### 4.2 铜氧化物中的量子振荡

欠掺杂 YBa₂Cu₃O₆₊ₓ:
- $k_F l_{\text{tr}}$ 在赝能隙区 ≈ 0.5-3
- 高场下观察到量子振荡 (Doiron-Leyraud et al., 2007; Sebastian et al., 2014)
- 标准解释: 磁场抑制超导后恢复了费米液体 — 但 ¬H 给出替代解释: 准粒子从未消失, 只是被强重正化隐藏

### 4.3 光学电导率中的"失踪"Drude权重

许多"坏金属"显示:
- DC电阻率接近MIR极限
- 但光学Drude峰仍存在且窄 ($\Gamma_{\text{opt}} \ll \hbar/\tau_{\text{tr}}$)
- 这直接符合 ¬H 的 P3 预言

---

## 5. A vs B 构造

**命题A (H成立 — 标准观点)**:
在 $k_F l_{\text{tr}} \approx 1$ 时, 准粒子图像失效。系统进入非费米液体区, 不能谈论明确定义的准粒子。MIR极限代表金属性的真正边界——超过此限系统变为"坏金属"或绝缘体。

**命题B (¬H成立 — 重正化污染)**:
在 $k_F l_{\text{tr}} \approx 1$ 时, 由于 $Z \ll 1$, 真实准粒子平均自由程 $k_F l^* \gg 1$。准粒子仍然完好, 表观"坏金属"行为来自能带重正化($m^*/m \gg 1$)和速度压低($v_F^* \ll v_F^0$), 而非准粒子衰变。MIR极限在关联金属中是"假极限"。

**为什么不能同时为真**:
如果 A 和 B 同时为真, 同一个系统必须在同一参数区间既"有"又"没有"准粒子——矛盾。P1-P4 的四个预言可以直接区分 A 和 B。

---

## 6. 检验策略

### 立即可行的检验（使用已发表数据）

**Test 1 (P1检验)**: 系统文献调查 — 在所有报道 $k_F l_{\text{tr}} < 2$ 的材料中, 有多少同时报道了量子振荡？预期(¬H): 相当比例。预期(H): 几乎没有。

**Test 2 (P3检验)**: 收集"坏金属"的光学电导率数据, 比较 $\Gamma_{\text{opt}}$ (Drude峰宽) 和 $\hbar/\tau_{\text{tr}}$ (DC电阻率散射率)。预期(¬H): $\Gamma_{\text{opt}} \ll \hbar/\tau_{\text{tr}}$。预期(H): $\Gamma_{\text{opt}} \approx \hbar/\tau_{\text{tr}}$。

**Test 3 (P4检验)**: 在重费米子材料中, 画出 $\rho_{\text{sat}}$ vs $m^*/m_{\text{band}}$。预期(¬H): 线性正相关, 斜率由基本常数决定。预期(H): 无关联。

### Phase 1路线图

Phase 1: 执行 Test 1 的系统文献调查 (2-3天)
Phase 2: 执行 Test 2 的光学数据收集 (3-5天)
Phase 3: 执行 Test 3 的重费米子数据编译 (2-3天)
综合推导: Phase 1-3 完成后 (第2周末)

---

## 参考文献（初步，待扩充）

1. Mott, N.F. "Metal-Insulator Transitions" (2nd ed., 1990) — MIR极限的原始论证
2. Emery & Kivelson, PRL 74, 3253 (1995) — 关联系统中MIR极限的早期讨论
3. Hussey et al., Phil. Mag. 84, 2847 (2004) — "坏金属"中量子振荡的综述
4. Hartnoll & Mackenzie, RMP (2022) — Planckian耗散的综述
5. Gunnarsson et al., RMP 75, 1085 (2003) — 强关联电子系统中的MIR问题
