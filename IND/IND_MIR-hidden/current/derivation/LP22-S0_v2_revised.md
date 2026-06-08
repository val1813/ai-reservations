# LP-22 v2 (修订版): Mott-Ioffe-Regel极限的重正化污染

> 日期: 2026-06-03 | 修订: v2 (回应A博士自我攻击)
> 状态: Phase 0 — 隐藏假设精确化（v2弱化版）
> 上一版致命问题已修复: ①l_tr vs l_qp区分 ②排他性实验信号 ③微观推导

---

## 0. 修订摘要

v1被A博士攻击发现三个🔴致命问题。v2做以下调整:

1. **弱化声张**: 从"准粒子完好→MIR是假极限"改为"MIR判据在关联系统中系统性偏移因子 $1/Z$, 偏移量与独立测量的关联强度正相关"
2. **排他性信号**: 引入Dingle温度/输运散射率比值 $\eta = T_D / T_{\text{tr}}$ 作为区分重正化污染($\eta \sim Z$)和散射各向异性($\eta \ll 1$)的诊断量
3. **微观推导**: 用 electron-boson 模型 (Migdal-Eliashberg) 显式计算 $\lambda_{\text{MIR}}(Z, \lambda)$
4. **先占声明**: 承认Emery & Kivelson (1995)的先驱性讨论，定位差异化为"定量判据+排他性预言"

---

## 1. 隐藏假设H (精确化)

**H**: 在关联电子系统中, 当 $k_F l_{\text{tr}} \approx 1$ (输运平均自由程≈费米波长) 时, 系统达到Mott-Ioffe-Regel极限 — 准粒子图像自洽性丧失, 金属性终结。

这个假设以不同形式出现在:
- 几乎所有"坏金属"(bad metal)文献的引言段
- 电阻率饱和的实验解释中
- 对 $k_F l < 1$ 的系统的"非费米液体"分类中

**¬H (v2弱化版)**: 表观 $k_F l_{\text{tr}} \approx 1$ 不等价于准粒子图像失效。在强关联系统中 $(Z \ll 1)$, 关联重正化效应系统性地压低 $l_{\text{tr}}$ 的**表观值**, 使得即使真实准粒子平均自由程 $l_{\text{qp}} \gg a$ (原子间距), MIR判据仍被表观满足。正确的MIR判据应使用重正化参数: $k_F^* l_{\text{qp}} \approx Z$。

**与 v1 的关键区别**: v1声称"准粒子完好", v2声称"偏移因子的存在性和系统性" — 这是一个更弱但更精确的声张。

---

## 2. 形式体系 (修复 v1 的 $l_{\text{tr}}$ vs $l_{\text{qp}}$ 混淆)

### 2.1 两种寿命, 两种平均自由程

**输运寿命** $\tau_{\text{tr}}$ (从电阻率提取):
$$\rho = \frac{m^*}{n e^2 \tau_{\text{tr}}}$$
$$l_{\text{tr}} = v_F^* \tau_{\text{tr}} = \frac{\hbar k_F}{m^*} \tau_{\text{tr}}$$

**量子寿命** $\tau_{\text{qp}}$ (从Dingle温度提取):
$$T_D = \frac{\hbar}{2\pi k_B \tau_{\text{qp}}}$$
$$l_{\text{qp}} = v_F^* \tau_{\text{qp}}$$

**关键关系**:
$$\frac{\tau_{\text{qp}}}{\tau_{\text{tr}}} = \frac{\langle 1-\cos\theta \rangle^{-1}_{\text{tr}}}{\langle 1 \rangle_{\text{qp}}} \equiv \xi$$

- 各向同性散射 (如点杂质): $\xi \approx 1$
- 小角度散射主导 (如临界铁磁涨落): $\xi \gg 1$
- **关联重正化**: $\xi \sim \mathcal{O}(1)$, 因为重正化均等地影响所有散射角

**→ 排他性诊断量**: $\eta \equiv \frac{T_D}{T_{\text{tr}}} = \frac{1}{\xi} \cdot \frac{1}{2\pi}$

其中 $T_{\text{tr}} \equiv \hbar/(k_B \tau_{\text{tr}})$。

- **散射各向异性情形**: $\eta \ll 1/(2\pi) \approx 0.16$ (量子振荡可见而输运已MIR饱和)
- **重正化污染情形**: $\eta \sim 1/(2\pi)$ (两种寿命以相同因子增强)

### 2.2 Electron-Boson模型的微观推导

采用 Migdal-Eliashberg 框架, 电子与玻色子谱 $\alpha^2 F(\nu)$ 耦合:

自能 (有限温度):
$$\Sigma(k, i\omega_n) = -T \sum_{m} \int \frac{d^3k'}{(2\pi)^3} |g_{kk'}|^2 D(k-k', i\omega_n-i\omega_m) G(k', i\omega_m)$$

在费米面平均近似下 (各向同性):
$$\text{Im}\Sigma(\omega) = -\pi \int_0^\infty d\nu \alpha^2 F(\nu) [2\coth(\nu/2T) - \tanh((\omega+\nu)/2T) + \tanh((\omega-\nu)/2T)]$$

准粒子残基 ($\omega \to 0, T \to 0$):
$$Z = \left(1 - \frac{\partial\text{Re}\Sigma}{\partial\omega}\bigg|_{\omega=0}\right)^{-1} = (1 + \lambda)^{-1}$$
其中 $\lambda = 2\int_0^\infty d\nu \alpha^2 F(\nu)/\nu$ 是无量纲耦合常数。

输运散射率 (各向同性, $\langle 1-\cos\theta \rangle = 1$):
$$\Gamma_{\text{tr}} \equiv \frac{\hbar}{\tau_{\text{tr}}} = -2Z \cdot \text{Im}\Sigma(0)$$

在 $T \gg \nu_{\text{typ}}$ (高温极限, 典型声子/自旋涨落能量):
$$\text{Im}\Sigma(0) \approx -\pi \lambda k_B T$$
$$\Rightarrow \Gamma_{\text{tr}} = 2\pi Z \lambda k_B T = \frac{2\pi\lambda}{1+\lambda} k_B T$$

量子散射率 (Dingle, 所有角度):
$$\Gamma_{\text{qp}} \equiv \frac{\hbar}{\tau_{\text{qp}}} = -2Z \cdot \text{Im}\Sigma(0) \cdot \langle 1 \rangle_{\text{FS}}$$

在各向同性极限下 $\langle 1 \rangle_{\text{FS}} = 1$, 所以 $\Gamma_{\text{qp}} = \Gamma_{\text{tr}}$。

**→ 关键**: 在 electron-boson 模型中, 如果耦合是各向同性的, $\tau_{\text{qp}} = \tau_{\text{tr}}$, 即 $\xi = 1$。任何对MIR的表观违反而 $\xi \approx 1$ 的情形→重正化污染。

### 2.3 重正化MIR参数 (微观推导)

从电阻率出发:
$$\rho = \frac{m^*}{n e^2 \tau_{\text{tr}}} = \frac{m(1+\lambda)}{n e^2} \cdot \frac{2\pi\lambda}{1+\lambda} \cdot \frac{k_B T}{\hbar} = \frac{2\pi m \lambda}{n e^2} \cdot \frac{k_B T}{\hbar}$$

输运 $k_F l_{\text{tr}}$:
$$k_F l_{\text{tr}} = \frac{\hbar k_F^2}{m^*} \tau_{\text{tr}} = \frac{\hbar k_F^2}{m(1+\lambda)} \cdot \frac{\hbar(1+\lambda)}{2\pi\lambda k_B T} = \frac{\hbar^2 k_F^2}{2\pi m \lambda k_B T}$$

**重正化MIR参数**:
$$\lambda_{\text{MIR}} \equiv \frac{k_F l_{\text{tr}}}{Z} = k_F l_{\text{tr}} \cdot (1+\lambda) = \frac{\hbar^2 k_F^2}{2\pi m \lambda k_B T} \cdot (1+\lambda)$$

在 MIR 表观极限 ($k_F l_{\text{tr}} = 1$):
$$T_{\text{MIR}} = \frac{\hbar^2 k_F^2}{2\pi m \lambda k_B}$$
$$\lambda_{\text{MIR}}(T_{\text{MIR}}) = 1 + \lambda$$

**核心结果**: 在强耦合 ($\lambda \gg 1$) 系统中, 当表观 $k_F l_{\text{tr}} = 1$ 时, 真实重正化参数 $\lambda_{\text{MIR}} = 1+\lambda \gg 1$。准粒子仍完好——表观MIR极限比真实MIR极限早出现 $(1+\lambda)$ 倍。

---

## 3. 可检验预言 (v2排他性版)

### P1 (定量 — 主预言): $\eta$ 诊断量

对于任何表观满足 $k_F l_{\text{tr}} \lesssim 2$ 的关联金属:
- 测量 Dingle 温度 $T_D$ (从量子振荡振幅的温度/场依赖)
- 测量输运温度 $T_{\text{tr}} = \hbar/(k_B \tau_{\text{tr}})$ (从电阻率)
- 计算 $\eta = T_D / T_{\text{tr}}$

**¬H 预言**: $\eta \in [0.05, 0.5]$ (即 $0.3 \lesssim \xi \lesssim 3$), 与 $k_F l_{\text{tr}}$ 的减小**无系统关联**

**散射各向异性替代解释预言**: $\eta \ll 0.05$ 当 $k_F l_{\text{tr}} \lesssim 2$, 且 $\eta$ 与 $k_F l_{\text{tr}}$ **强负相关**

**→ 两个预言在 $\eta$ 的行为上可区分。**

### P2 (定量 — 关联强度定标): $\rho_{\text{sat}}$ vs $\gamma$

$$\rho_{\text{sat}} \equiv \rho(T_{\text{MIR}}) = \frac{h a}{e^2} \cdot (1+\lambda)$$

比热系数:
$$\gamma = \frac{C}{T} = \frac{\pi^2}{3} k_B^2 N^* = \frac{\pi^2}{3} k_B^2 \frac{m^* k_F}{\pi^2 \hbar^2} = \frac{k_B^2 m k_F}{3\hbar^2} (1+\lambda)$$

**¬H 预言**: $\rho_{\text{sat}}$ 和 $\gamma$ 在关联金属族中呈**线性正相关**, 斜率为基本常数组合。

**H 预言**: 无系统关联 — "饱和"电阻率是材料特定的偶然值。

### P3 (定性 — 光学Drude峰): $\Gamma_{\text{opt}}$ vs $\Gamma_{\text{tr}}$

在各向同性 electron-boson 耦合下:
$$\Gamma_{\text{opt}} = \Gamma_{\text{qp}} = \Gamma_{\text{tr}}$$

而在 $T \gg \nu_{\text{typ}}$ 极限下:
$$\Gamma_{\text{opt}} = \Gamma_{\text{qp}} = \frac{2\pi\lambda}{1+\lambda} k_B T$$

DC电阻率散射率:
$$\Gamma_{\text{DC}} = \Gamma_{\text{tr}} = \frac{2\pi\lambda}{1+\lambda} k_B T$$

**¬H 预言**: $\Gamma_{\text{opt}} \approx \Gamma_{\text{DC}}$ (在各向同性系统中)
如果观察到 $\Gamma_{\text{opt}} \ll \Gamma_{\text{DC}}$ → 散射各向异性主导
如果观察到 $\Gamma_{\text{opt}} \approx \Gamma_{\text{DC}}$ 且两者都 $\approx k_B T/\hbar$ → 重正化污染主导

### P4 (预言 — 跨材料族): $\eta$ 对材料参数的独立性

在 ¬H 下, $\eta$ 应该相对恒定 ($\sim 0.1-0.3$), 对以下参数不敏感:
- 残余电阻率 RRR
- 掺杂浓度
- 无序度

而散射各向异性情形下, $\eta$ 应对这些参数高度敏感 (因为它们改变散射机制)。

---

## 4. A vs B (v2修订版)

**命题A (H成立 — 标准MIR解释)**:
表观 $k_F l_{\text{tr}} \approx 1$ 意味着系统达到了 Mott-Ioffe-Regel 极限。此时:
- 平均自由程≈原子间距
- 准粒子图像丧失自洽性
- 进一步增加散射 → 金属-绝缘体转变或"坏金属"饱和
- 饱和电阻率 $\rho_{\text{sat}}$ 由几何因子 $h a/e^2$ 决定
- 系统在 $k_F l_{\text{tr}} \lesssim 1$ 时不再支持量子振荡

**命题B (¬H成立 — 重正化污染)**:
表观 $k_F l_{\text{tr}} \approx 1$ 可以来自关联重正化的系统性压低:
- $Z \ll 1$ → $v_F^* = Z v_F^0$ 压低 → $l_{\text{tr}} = v_F^* \tau$ 压低
- 即使 $\tau$ 很大 (准粒子长寿命), 表观 $l_{\text{tr}}$ 仍可≈原子间距
- 真正的MIR条件应是 $k_F l_{\text{qp}} \approx Z$ (而非 $k_F l_{\text{tr}} \approx 1$)
- $\rho_{\text{sat}} \propto (1+\lambda) \propto 1/Z$, 与关联强度系统地相关
- $\eta \equiv T_D/T_{\text{tr}} \sim \mathcal{O}(0.1)$, 不随 $k_F l_{\text{tr}} \to 1$ 发散

**为什么不能同时为真**:
命题A预言 $\eta \to 0$ 当 $k_F l_{\text{tr}} \to 1$ (准粒子无定义→$T_D$ 发散)。命题B预言 $\eta$ 保持有限。两者对同一可测量给出相反的极端行为。

---

## 5. 先占文献定位

### Emery & Kivelson, PRL 74, 3253 (1995)
首次讨论了"坏金属"中的MIR极限与相涨落的关系。核心关注超导 $T_c$ 的上界而非MIR判据本身的重正化。**未引入 $\lambda_{\text{MIR}}$ 参数, 未提出 $\eta$ 诊断量。**

### Gunnarsson et al., RMP 75, 1085 (2003)
综述了关联电子中的MIR问题, 定性地讨论了有效质量重正化对MIR判据的可能影响。**未做定量分解, 未提出排他性实验检验。**

### v2的差异化
| 方面 | E&K 1995 | Gunnarsson 2003 | 本工作 (v2) |
|------|----------|-----------------|------------|
| MIR重正化的定量参数 | 无 | 定性讨论 | $\lambda_{\text{MIR}} = k_F l_{\text{tr}}/Z$ |
| $l_{\text{tr}}$ vs $l_{\text{qp}}$ 区分 | 无 | 无 | $\eta = T_D/T_{\text{tr}}$ 诊断量 |
| 微观推导 | 现象学 | 现象学 | Migdal-Eliashberg $\lambda$ |
| 跨材料族预言 | 无 | 无 | $\rho_{\text{sat}} \propto \gamma$ |
| 排他性 (vs散射各向异性) | 无 | 无 | $\eta$ 定标行为 |

---

## 6. Phase 1 路线图

### Phase 1a: 文献元分析 (3天)
系统地编译已发表文献中同时报告了以下两个量的关联金属:
1. 电阻率 (可提取 $k_F l_{\text{tr}}$)
2. 量子振荡 (可提取 $T_D$)

候选材料族: 重费米子 (CeCoIn₅, YbRh₂Si₂, CeRhIn₅, URu₂Si₂), 
           钌氧化物 (Sr₂RuO₄, Sr₃Ru₂O₇), 
           铁基超导体 (BaFe₂(As₁₋ₓPₓ)₂), 
           铜氧化物 (YBa₂Cu₃O₆₊ₓ, Nd-LSCO)

对每个材料提取: $\rho(T)$, $k_F$, $m^*$, $T_D$, RRR, 掺杂/压力/磁场

→ 目标: 计算 $\eta$ 对 $k_F l_{\text{tr}}$ 的散点图, 检验 P1

### Phase 1b: 重费米子焦点分析 (2天)
对 CeCoIn₅ (数据最丰富):
- 高场 ($H > H_{c2}$) 量子振荡的 $T_D$ 外推到低场
- 与低场电阻率 $k_F l_{\text{tr}}$ 比较
- 验证 $\eta$ 是否在跨场区保持一致

### Phase 2: 光学数据编译 (3天)
收集"坏金属"的光学电导率, 比较 $\Gamma_{\text{opt}}$ vs $\Gamma_{\text{DC}}$
关键材料: V₂O₃, VO₂, 有机导体 $\kappa$-(BEDT-TTF)₂X

### Phase 3: 综合推导 (第2周末)
整合 Phase 1-2 的元分析结果, 定量判断 ¬H 成立/证伪/有边界

---

## 参考文献

1. Emery & Kivelson, PRL 74, 3253 (1995) — 坏金属中MIR极限的先驱性讨论
2. Gunnarsson, Calandra & Han, RMP 75, 1085 (2003) — 关联电子MIR问题综述
3. Hussey et al., Phil. Mag. 84, 2847 (2004) — 坏金属中量子振荡综述
4. Hartnoll & Mackenzie, RMP (2022) — Planckian耗散综述
5. Khansili et al., arXiv:2311.11914 (2023) — CeCoIn₅ 热阻抗谱
6. Settai et al., PRL 96, 077207 (2006) — CeCoIn₅ 高场dHvA和Dingle温度
