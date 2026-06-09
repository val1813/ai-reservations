# A博士: 抽象因果环→IBM Q Transmon设备映射

**课题:** LP38 -- QCMI Precision / Bridge to Device
**角色:** A博士 (理论物理+量子设备映射)
**日期:** 2026-06-09
**目标:** 将LP38的抽象因果环理论映射到IBM量子计算机的transmon qubit系统，给出可检验的预言和诚实的可行性评估

---

## Part 1: Transmon Hamiltonian → Cartan分解

### 1.1 Transmon有效两体Hamiltonian

两个capacitive coupled transmon qubit，在qubit子空间截断后的有效Hamiltonian为：

$$H_{\text{eff}} = -\frac{\omega_a}{2} Z_a - \frac{\omega_b}{2} Z_b + J(\sigma_+^a \sigma_-^b + \sigma_-^a \sigma_+^b)$$

其中：
- $\omega_a, \omega_b$：dressed qubit频率 (典型值: 4.8-5.2 GHz)
- $J/2\pi$：交换耦合强度 (典型值: 5-30 MHz for直接电容耦合; ~2-5 MHz有效耦合通过共同腔)
- $\delta/2\pi$：anharmonicity (~ -330 MHz for IBM transmon)

包括高阶transmon能级效应的完整模型：

$$H_{\text{sys}} = \sum_{j=a,b} \left(\tilde{\omega}_j b_j^\dagger b_j + \frac{\delta_j}{2} b_j^\dagger b_j(b_j^\dagger b_j - 1)\right) + J(b_a^\dagger b_b + b_a b_b^\dagger)$$

在 $|\omega_a - \omega_b| \gg J$ 的大失谐极限下，交换相互作用主要贡献一个有效的 $ZZ$ (cross-Kerr)耦合：

$$H_{\text{ZZ}} \approx -\zeta \, Z_a \otimes Z_b, \quad \zeta \approx \frac{J^2}{2} \cdot \frac{|\delta|}{(\omega_a - \omega_b)^2 + |\delta| \cdot |\omega_a - \omega_b|}$$

这对IBM设备至关重要：即使在没有特意施加门时，$ZZ$ 相互作用也是"always-on"的。

### 1.2 IBM原生双qubit门的Cartan分解

IBM Heron (r1/r2/r3) 的原生双qubit门是 **CZ** (Controlled-Z)，通过**可调耦合器**实现。Eagle (r3) 系列使用 **ECR** (Echoed Cross-Resonance)。Cartan分解：

$$\text{CZ} = \text{diag}(1, 1, 1, -1)$$

CZ的Cartan系数（Weyl chamber坐标系）：

$$\boxed{(c_x, c_y, c_z)_{\text{CZ}} = \left(0, 0, \frac{\pi}{4}\right)}$$

这意味着CZ是**Cartan轴对齐的**（c只沿z方向）。

等价地，CZ可写作：

$$\text{CZ} = \exp\left(i\frac{\pi}{4} \, Z \otimes Z\right) \cdot \exp\left(-i\frac{\pi}{4} Z \otimes I\right) \cdot \exp\left(-i\frac{\pi}{4} I \otimes Z\right)$$

去掉局域相位后，CZ本质上是一个 $RZZ(\pi/2)$ 门。

**关键映射——Cartan系数与门参数的关系：**

| 门类型 | Cartan系数 (c_x, c_y, c_z) | 局部等价于 | IBM原生？ |
|:------|:-------------------------|:--------|:--------:|
| CZ | (0, 0, π/4) | RZZ(π/2) | Heron原生 |
| CNOT | (π/4, 0, 0) | RXX(π/2) | Eagle CR+局域门 |
| ECR (Eagle原生) | (0, π/4, 0) | RYY(π/2) | Eagle原生 (ZX→局域旋转后) |
| RZZ(θ) | (0, 0, θ/2) | — | Heron分数门 |
| RXX(θ) | (θ/2, 0, 0) | — | 需分解 |
| RYY(θ) | (0, θ/2, 0) | — | 需分解 |
| SWAP | (π/4, π/4, π/4) | — | 3×CZ |
| sqrtSWAP | (π/8, π/8, π/8) | — | 需分解 |

### 1.3 轴对齐 vs. 轴失配门分类

**Cartan轴对齐** (所有Cartan系数沿单一方向)：
- CZ：纯ZZ相互作用 → c = (0, 0, π/4)
- RZZ(θ)：c = (0, 0, θ/2) —— **LP38对齐轴配置的核心门**
- CNOT：c = (π/4, 0, 0)
- ECR (原始ZX门)：c = (0, β, 0)，其中 $\beta \approx \nu_{ZX} \tau / 2$

**Cartan轴失配** (多方向Cartan系数)：
- SWAP：c = (π/4, π/4, π/4)
- sqrtSWAP：c = (π/8, π/8, π/8)
- 一般Haar酉：c跨多个方向

**IBM Heron的优势**：RZZ(θ) 分数门直接实现任意角度的ZZ相互作用——这恰好是LP38要对齐轴的配置！

### 1.4 Cross-Resonance gate的Cartan结构

IBM Eagle设备上的CR gate在旋转坐标系下的有效Hamiltonian：

$$H_{\text{CR}} = \frac{\nu_{ZX}}{2} ZX + \frac{\nu_{IX}}{2} IX + \frac{\nu_{ZI}}{2} ZI + \frac{\nu_{ZZ}}{2} ZZ + \ldots$$

Cartan分解视角：$ZX$ 相互作用通过局域旋转等价于不同的Cartan分量：
- $ZX$ 可以通过将目标qubit的Z基旋转到X基 → 变为 $ZZ$，此时Cartan轴变为z。
- 这就是echoed CR gate能够产生高保真CNOT的原因：echo脉冲消除了 $IX$, $ZZ$ 等杂散项，只保留 $ZX$ 分量。

**实验上**（ibm_hanoi, $\Omega = 36$ MHz）：

| 项 | 速率 (MHz) | Cartan对应 |
|:---|:--------|:---------|
| $ZI$ | 3.081 | 局域（非纠缠） |
| $ZX$ | -0.4915 | **Cartan非局域核心** |
| $IX$ | 0.4168 | 局域 |
| $ZZ$ | 0.0294 | always-on耦合 |
| $IY$ | 0.0649 | 局域 |
| $ZY$ | -0.0332 | 杂散 |
| $IZ$ | -0.0756 | 局域 |

### 1.5 有效Cartan系数的实验确定

给定一般2-qubit酉 $U$，其Cartan系数 $(c_x, c_y, c_z)$ 可以从局部不变量 $(g_1, g_2, g_3)$ 恢复：

$$\begin{aligned}
g_1 &= \frac{1}{4}[\cos(2c_x) + \cos(2c_y) + \cos(2c_z) + \cos(2c_x)\cos(2c_y)\cos(2c_z)] \\
g_2 &= \frac{1}{4} \sin(2c_x) \sin(2c_y) \sin(2c_z) \\
g_3 &= \cos(2c_x) + \cos(2c_y) + \cos(2c_z)
\end{aligned}$$

对于IBM硬件，这些局部不变量可通过**量子过程层析**（QPT）或**循环基准测试**（CB）实验测定——QPT给出完整的过程矩阵 $\chi$，从中提取局部不变量。

---

## Part 2: 因果环的IBM Q实现

### 2.1 重六角晶格的拓扑约束——关键挑战

IBM Heron/Eagle使用**重六边形（heavy-hex）晶格**，其**围长（girth）= 6**。

这意味着：**IBM硬件上不存在原生的4-qubit环**。最小环包含8个qubit（一个六边形+两条对角线）。

这是将LP38因果环映射到真实设备的最严重挑战。要构造4-qubit环，必须通过SWAP门将逻辑qubit路由到能形成环的物理qubit上。

### 2.2 策略A: SWAP辅助环（Eagle/Heron均可）

在重六角晶格上，选择一个包含6个物理qubit的六边形子图：

```
物理qubit: p0, p1, p2, p3, p4, p5 (六边形顶点)

逻辑映射:
  Q_a → p0
  E_1 → p1
  Q_b → p3
  E_2 → p4
  
边:
  u₁: Q_a-E₁ = p0-p1  ← 原生边 ✓
  u₂: E₁-Q_b = p1-p3  ← 需要1个SWAP (p1↔p2, 或直接W-pattern路由)
  u₃: Q_a-E₂ = p0-p4  ← 需要2个SWAP (p0↔p5↔p4, 或W-pattern)
  u₄: Q_b-E₂ = p3-p4  ← 原生边 ✓
```

SWAP开销估计（使用IBM SABRE transpiler）：

| 边 | 物理距离 | SWAP数量 | CNOT/CZ开销 | 说明 |
|:--|:------:|:------:|:----------|:----|
| u₁ (p0-p1) | 1 | 0 | 1×CZ | 原生 |
| u₂ (p1-p3) | 2 | 1 | 3×CZ+1×CZ | 1 SWAP = 3 CZ + 目标CZ |
| u₃ (p0-p4) | 2 | 1 | 3×CZ+1×CZ | 1 SWAP |
| u₄ (p3-p4) | 1 | 0 | 1×CZ | 原生 |
| **总计** | — | 2 SWAP | **10×CZ** (含SWAP中的6 CZ + 4门CZ) |

如果4个边的酉都是RZZ(θ)（Heron分数门），则原生CZ可替换为RZZ(θ)，但SWAP仍需要分解为3个CZ（因为IBM没有原生SWAP）。

**更坏的情况——如果RZZ(θ)不可用于SWAP：**
p-SWAP gate可以用2个CNOT+CZ替代3个CNOT的SWAP。但p-SWAP在IBM上的可用性待确认。

### 2.3 策略B: 间接环（通过SWAP链构造有效4-qubit环）

另一策略：不在物理上形成环，而在**时间域**上通过SWAP链模拟环拓扑。

```
时间步骤:
1. Q_a-E₁ 相互作用 (CZ/RZZ native)
2. SWAP: E₁ ↔ E₁' 
3. E₁'-Q_b 相互作用
4. Q_a-E₂ 相互作用  
5. SWAP: E₂ ↔ E₂'
6. Q_b-E₂' 相互作用
```

这种方法的总CZ数量为4×RZZ(θ) + N_SWAP×3，其中N_SWAP取决于布局。

### 2.4 策略C: 利用分数门RZZ(θ)直接实现对齐轴环

这是最有希望的方案。在Heron处理器上使用RZZ(θ)分数门：

```
Q_a (qubit 0) --- RZZ(θ) --- E₁ (qubit 1) --- RZZ(θ) --- Q_b (qubit 2)
    |                                                       |
    |___________________ RZZ(θ) ____________________________|
    |                                                       |
    └─────────────── E₂ (qubit 3) ────── RZZ(θ) ───────────┘
```

如果4个qubit能形成原生环，每边的RZZ(θ)是一个原生分数门操作。总电路深度 = 4个RZZ(θ)门（如果可并行）+ 单qubit操作。

**但重六角晶格的约束使这不能原生实现。** 需要一个特殊的4-qubit子图。

### 2.5 初始态制备协议

#### 2.5.1 R-Q Bell对制备

在IBM Q上制备 $|\Phi^+\rangle_{RQ} = (|00\rangle + |11\rangle)/\sqrt{2}$：

**标准电路（目标：Q_a=qubit 0, Q_b=qubit 2，通过RZZ环连接）：**

```
┌───┐
q0: ┤ H ├──■──  ← Hadamard + CNOT → |Φ⁺⟩
     └───┘┌─┴─┐
q2: ─────┤ X ├──  
          └───┘
```

对于Heron（原生CZ而非CNOT）：

```
     ┌───┐     ┌───┐
q0: ─┤ H ├──■──┤ H ├  ← H-CZ-H = CNOT等效
     └───┘  │  └───┘
            │
q2: ────────■────────
```

**保真度估计：**
- 单qubit Hadamard: 由SX+RZ组成，保真度 > 99.97%
- CZ门保真度: 99.7-99.9% (Heron r3)
- 初始Bell对保真度: F ≈ 99.5-99.7%（由门错误主导）

#### 2.5.2 环境混合态 $\gamma_E = \text{diag}(p, 1-p)$ 的制备

LP38的要求：$\gamma_0 \neq \gamma_1$（避免退化），且理想情况下 $p \neq 0.5$。

**方案A：辅助qubit纯化方法**

环境mixed态 $\rho_E = p|0\rangle\langle 0| + (1-p)|1\rangle\langle 1|$ 通过引入辅助qubit (ancilla)纯化：

1. 将E qubit初始化为 $|0\rangle$
2. ancilla制备为 $\sqrt{p}|0\rangle + \sqrt{1-p}|1\rangle$（Ry旋转）
3. CNOT(ancilla → E)：$\sqrt{p}|00\rangle + \sqrt{1-p}|11\rangle$
4. 对ancilla部分求迹 → $\rho_E = \text{diag}(p, 1-p)$

**电路（对两个E qubit各重复一次）：**

```
E₁ qubit: ─────────────────■────────  → ρ_E₁ = diag(p, 1-p)
ancilla₁: ┤ Ry(2arccos(√p)) ├─■── DISCARD

E₂ qubit: ─────────────────■────────  → ρ_E₂ = diag(p, 1-p)  
ancilla₂: ┤ Ry(2arccos(√p)) ├─■── DISCARD
```

**方案B：利用门错误天然产生混合态（实用主义方案）**

IBM Q上每个native gate都有固有错误，经过足够多的门操作后，纯态会退化为混合态。但这不是可控的——p和(1-p)的比例无法精确调控，且不同qubit上不同。

**方案C：mid-circuit reset + 概率性准备（Heron支持）**

使用mid-circuit measurement + conditional reset制备经典混合：

1. 制备叠加态：$H|0\rangle \rightarrow (|0\rangle + |1\rangle)/\sqrt{2}$
2. Mid-circuit测量
3. **不**执行条件修正（保留结果）
4. 从结果分布：P(0) = P(1) = 1/2
5. 但这不是纯化意义上的混合态——qubit经过测量后塌缩到计算基。正确的方法是用classical register来控制制备，并**不记录**测量结果（或对所有结果概率求平均）。

**推荐方案**：使用**2个额外的辅助qubit**用纯化方法（方案A）制备两个E qubit的mixed态。对于4-qubit因果环 + 2个ancilla + 1个制备Bell对的额外qubit，至少需要7个物理qubit。

但如果将R-Q Bell对的制备量子比特复用为环境qubit之一（例如Q_b=Q系统的qubit 2，E_1=qubit 1, E_2=qubit 3），可以节省1个qubit。

**最终qubit预算（含辅助）：**
- 核心环：4 qubit (Q_a, E_1, Q_b, E_2)
- R Bell对制备辅助：0（利用Q_a和Q_b之间的原生CNOT/CZ即可，无需额外helper）
- E_1 mixed态辅助：1 ancilla
- E_2 mixed态辅助：1 ancilla
- SWAP链所需的中间qubit：取决于布局，最小0，典型2-4

**总计：至少 8-10 个物理qubit**（含辅助和路由qubit）

### 2.6 有效电路（对齐轴RZZ环）

使用Heron的RZZ(θ)分数门的完整电路流程：

```
                        ┌───────────────────────┐
Stage 1: 制备           │ Bell |Φ⁺⟩_RQ         │ × 1 CZ
                        │ γ_E1 = diag(p,1-p)    │ × 1 ancilla CNOT
                        │ γ_E2 = diag(p,1-p)    │ × 1 ancilla CNOT
                        └───────────────────────┘
                              ↓
                        ┌───────────────────────┐
Stage 2: 路由           │ SWAP将逻辑qubit映射  │ × 2-6 CZ
                        │ 到环拓扑位置          │
                        └───────────────────────┘
                              ↓
                        ┌───────────────────────┐
Stage 3: 因果环演化     │ RZZ(θ) on Q_a-E₁     │ × 1 RZZ
                        │ RZZ(θ) on E₁-Q_b      │ × 1 RZZ
                        │ RZZ(θ) on Q_a-E₂      │ × 1 RZZ
                        │ RZZ(θ) on Q_b-E₂      │ × 1 RZZ
                        └───────────────────────┘
                              ↓
                        ┌───────────────────────┐
Stage 4: 测量           │ 4-qubit QST          │ 81-300+ circuits
                        └───────────────────────┘
```

**总原生双qubit门数（对齐轴RZZ环——乐观估计）：**
- 制备: 1 CZ (Bell) + 2 CNOT (mixed态) 
- 路由: 2-6 CZ (最小化布局下)
- 环演化: 4 RZZ(θ) (Heron分数门)
- 合计: **5-9 个原生双qubit门**（不含QST所需）

**总双qubit门数（悲情估计——含SWAP分解）：**
- 制备: 1 CZ + 2×3 CZ = 7 CZ (将CNOT分解为CZ+H)
- 路由: 6-18 CZ 
- 环演化: 4 RZZ(θ)
- 合计: **17-29 个原生双qubit门**

---

## Part 3: QCMI测量协议

### 3.1 QCMI定义与所需观测量

$$\text{QCMI} = I(R;E'|Q') = S(RQ') + S(Q'E') - S(Q') - S(RQ'E')$$

其中各Vie熵 $S(\rho) = -\text{Tr}(\rho \log_2 \rho)$ 需要从约化密度矩阵计算。

**演化后的4-qubit态** $\rho_{RQ'E'} = |\Phi^+\rangle\langle\Phi^+|_{RQ} \otimes \gamma_{E_1} \otimes \gamma_{E_2}$ 经过因果环酉演化 $U = u_4 u_3 u_2 u_1$。

需要提取的4个约化态：

| 子系统 | qubit | 维度 |
|:------|:------|:---:|
| RQ' | {Q_a, Q_b} | 4×4 |
| Q'E' | {Q_b, E₁, E₂} | 8×8 |
| Q' | {Q_b} | 2×2 |
| RQ'E' | {Q_a, Q_b, E₁, E₂} | 16×16 |

实际上，我们需要的是最终4-qubit态的**完整层析**（16×16密度矩阵），从中计算所有约化态。

### 3.2 态层析协议

**标准Pauli基QST（4-qubit）：**

测量基组合数：$3^4 = 81$ 个不同的Pauli测量设置。每个设置测量4个qubit在X/Y/Z基下的joint概率分布。

每个Pauli设置测量 $2^4 = 16$ 个投影概率。总测量概率数 = 81 × 16 = 1296个独立概率（约束下）。

**所需shot数估计：**

要达到密度矩阵元素误差 $\epsilon$：
$$N_{\text{shots}} \approx \frac{2^{2n}}{\epsilon^2} = \frac{256}{\epsilon^2}$$

目标精度 $\epsilon = 0.01$（1%密度矩阵元素精度）：
$$N_{\text{shots}} \approx 2.56 \times 10^6 \text{ 每个Pauli设置}$$

81个设置 × 2.56M shots = **~207M shots 总计**

这远超IBM Q的典型配额（每个job通常限制100-300个circuit，100k shots max）。

**实用估计——QCMI精度的shot需求：**

区分 $\alpha \approx 1.81$ 和 $\alpha \approx 4.00$ 需要的QCMI精度：

在 $\theta = \pi/16$（= 0.0625π）:
- QCMI$^{Rxx}$ (α≈1.81): ~0.231 bits
- QCMI$^{\text{CCQ}}$ (α≈4.0): ~0.0027 bits (如果CCQ正确)

差值为 **~0.228 bits**。要区分它们，需要QCMI测量精度 $\sigma_{I} \ll 0.228$ bits。取 $\sigma_I \approx 0.02$ bits (约10%误差)：

$$N_{\text{shots per setting}} \approx \frac{256}{(0.02)^2} \approx 6.4 \times 10^5$$

81设置 × 640k shots = **~52M shots total**

**这仍不现实。** 需要更高效的方法。

### 3.3 实用替代方案：直接保真度估计 (DFE) + 部分层析

对于对齐轴RXX环配置，LP38理论预测了一个解析可处理的特殊结构：
- $\rho_{RQ}$ 在 $\sigma_x$ 本征基下是对角的
- QCMI在p-independent的意义下等价于一个简单的二元熵差

**简化协议（利用σ_x基对角性）：**

只需要测量所有4个qubit在**X基**下的联合概率分布。在X基下的16个联合概率 $P(s_1, s_2, s_3, s_4)$ 完全确定了S的本征结构。

X基测量：每个qubit使用Hadamard门 + 标准Z测量。只需 **1个Pauli设置**（XXXX）。

从X基联合概率计算QCMI：
1. 对角化 $U$ 需要X基下的 $S(s) = (s_1+s_3)(s_2+s_4)$
2. $|\Phi^+\rangle_{RQ}$ 在X基下也是简单的（X基下$|\Phi^+\rangle = (|++,++\rangle + |+-,+-\rangle + |-+,-+\rangle + |--,--\rangle)/2$）
3. $\gamma_E$ 在计算基(Z基)下是对角的 → 在X基下有均匀分布 ✓

**这意味着：对于对齐轴RXX/RZZ环，QCMI可以仅从X基联合测量中确定！**

具体地，只需 $2^4 = 16$ 个X基投影的计数统计。每个需要足够的计数精度。

shot需求：16个bin中每个需要 $\approx 1/\epsilon^2$ 计数以获得精度 $\epsilon$。

对于 $\epsilon = 0.02$ bits的QCMI精度（在$\theta = \pi/16$时QCMI ≈ 0.23 bits，需要~10%精度）：
- 每个bin至少 $1/(0.02)^2 \approx 2500$ 有效计数
- 由于最稀有bin的概率 ~ $O(\theta^4)$ ≈ $10^{-6}$，有效计数由稀有bin支配
- 总shots: $\approx N_{\text{rare}}/\min(p_i) \approx 2500/10^{-6} = 2.5 \times 10^9$ shots

这仍然很大，但可以通过聚焦在较大的$\theta$来缓解。

**在 $\theta = \pi/4$（QCMI ≈ 1.22 bits）：**
- 最小概率bin ≈ $(\pi/4)^4/16 \approx 0.0024$
- 总shots: $2500/0.0024 \approx 10^6$ shots for precision

这更可行。

### 3.4 受限资源下的测量策略总结

| 方案 | 电路数 | 总shots | 精度 | 可行性 |
|:----|:-----:|:-----:|:---:|:----:|
| 完整QST | 81 | >50M | 高(~1%) | 不现实 |
| X基简化（LP38 RXX环专用）| 1 | 1-10M | 中等(~5%) | 可行 |
| 大θ+小shot预算 | 1 | 100k | 低(~15%) | 现实但粗糙 |
| 完整QST+compressed sensing | 31 | ~10M | 中等 | 勉强可行 |

**推荐方案：** 利用LP38的解析结构，仅用X基测量。从大θ开始（θ=π/4, π/8, π/16），使用尽可能多的shots（IBM Q上限100k/job，可提交多个job累积）。

### 3.5 熵计算的数值协议

从4-qubit X基概率分布 $\{P(s_1,s_2,s_3,s_4)\}_{s_i=\pm 1}$：

**Step 1:** $\rho_{RQ}$ = 对E₁和E₂求迹：
$$P_{RQ}(s_1, s_3) = \sum_{s_2,s_4} P(s_1,s_2,s_3,s_4)$$
$S(RQ') = -\sum P_{RQ} \log_2 P_{RQ}$（因为ρ_RQ在σ_x基对角）。

**Step 2:** $\rho_Q$ = 对R, E₁, E₂求迹：
$$P_Q(s_3) = \sum_{s_1,s_2,s_4} P(s_1,s_2,s_3,s_4) = \frac{1}{2} \quad (\forall s_3)$$
$S(Q') = 1.0$ bits（理论保证）。

**Step 3:** $\rho_{QE}$ = 对R求迹：
$$P_{Q'E'}(s_3,s_2,s_4) = \sum_{s_1} P(s_1,s_2,s_3,s_4)$$
对角化8×8密度矩阵（但可用解析理论值$S(Q'E') = \sum_{k=1}^3 h_2((1+\cos^k(2\theta))/2)$）。

**Step 4:** $S(RQ'E')$ = 全4-qubit X基分布的熵。
由于$U$在X基对角，初始态$\rho_{QE}$（计算基）在X基的变换是简单的旋转，$S(RQ'E') = S_{\text{init}}$（酉保熵）。

**Step 5:** QCMI = S(RQ') + S(Q'E') - S(Q') - S(RQ'E')

### 3.6 门保真度下的测量误差估计

设每个CZ/RZZ门的保真度为 $F_g = 1 - \epsilon_g$：
- Heron r3: $\epsilon_g \approx 3 \times 10^{-3}$ for CZ
- Eagle r3: $\epsilon_g \approx 7.6 \times 10^{-3}$ for ECR

经过 $N_g$ 个双qubit门的累积保真度：
$$F_{\text{total}} \approx \exp(-N_g \cdot \epsilon_g) \approx 1 - N_g \cdot \epsilon_g$$

对于 $N_g = 10$（含制备+路由+演化）：
- Heron r3: $F_{\text{total}} \approx 1 - 10 \times 0.003 = 0.97$（3%错误）
- Eagle r3: $F_{\text{total}} \approx 1 - 10 \times 0.0076 = 0.924$（7.6%错误）

**门保真度对QCMI测量的影响：**

门错误以两种方式影响QCMI：
1. **去极化噪声**：每个门附加概率 $\epsilon_g$ 的完全混合态 → 引入假QCMI
2. **相干错误**：系统性的over/under-rotation → 改变有效Cartan系数

去极化噪声的假QCMI：$\Delta I_{\text{depol}} \approx N_g \cdot \epsilon_g \cdot \log_2(d)$ bits。

对于 $N_g=10, \epsilon_g=0.003, d=4$（RQ子系统）: $\Delta I_{\text{depol}} \approx 10 \times 0.003 \times 2 = 0.06$ bits。

这个系统误差与QCMI信号本身（在θ=π/16时~0.23 bits）的比较：
$$\frac{\Delta I_{\text{depol}}}{I_{\text{QCMI}}(\theta=\pi/16)} \approx \frac{0.06}{0.23} \approx 26\%$$

**这是显著的但未必致命的系统误差。** 可通过以下方法部分缓解：

- **Richardson外推（推荐）：** 在不同门计数（N_g = 7, 10, 13）下重复实验，外推到N_g→0。与RZZ(θ)完全兼容。
- **Gate-folding ZNE（备选）：** IBM标注为兼容RZZ(θ)但标记为"experimental"。通过折叠门序列增加噪声比例，外推到零噪声极限。
- **⚠️ Pauli twirling不适用：** IBM官方文档明确声明Pauli twirling与分数门RZZ(θ)在非Clifford角度下不兼容——不满足twirling的数学条件。仅当使用标准CZ分解（Clifford角度）时可用。

---

## Part 4: 可检验预言

### 4.1 主预言: QCMI ∝ θ²·log(1/θ)

对于IBM Q上的对齐轴配置（RZZ(θ)门在所有四条边上）：

$$\boxed{\text{QCMI}(\theta) = \frac{\theta^2}{\ln 2}\left[1 + 2\ln\frac{1}{\theta}\right] + O(\theta^4|\log\theta|)}$$

这是我们LP38的解析结果。对于IBM Heron：
- RZZ(θ)分数门的θ在实验上是连续可调的（0 < θ ≤ π/2）
- 每次校准的θ可以不同 → 可以扫描θ

### 4.2 有效标度指数

$$\boxed{\alpha_{\text{eff}}(\theta) = 2 - \frac{1}{\ln(1/\theta)} + O\left(\frac{1}{\ln^2(1/\theta)}\right)}$$

具体数值：

| θ (×π) | θ (rad) | α_eff | QCMI (bits) |
|:------|:------|:-----:|:----------:|
| 0.5 | 1.571 | -0.29 | 1.000 |
| 0.25 | 0.785 | 0.30 | 1.224 |
| 0.125 | 0.393 | 1.22 | 0.597 |
| 0.0625 | 0.196 | 1.49 | 0.231 |
| 0.03125 | 0.098 | 1.63 | 0.078 |
| 0.015625 | 0.049 | 1.70 | 0.024 |
| 0.0078125 | 0.025 | 1.75 | 0.0073 |
| 0.00390625 | 0.012 | 1.79 | 0.0021 |

### 4.3 在可实现θ范围内的预期α

**受门保真度限制的可实现θ范围：**

对于RZZ(θ)，门的实现保真度与θ有关。Heron的分数门RZZ(θ)在任意θ下由单个控制脉冲驱动，保真度随θ变化：

在小θ极限：$F_{\text{RZZ}}(\theta) \to 1$（门接近identity）。但实际上，任何脉冲的最小持续时间受限于控制电子学带宽（~1 ns分辨率）。对θ → 0，相对误差 $\Delta\theta/\theta$ 发散。

**实用下限：** $\theta_{\text{min}} \approx 0.01\pi$ (≈ 0.03 rad)，此时QCMI ≈ 0.003 bits，与去极化噪声的假QCMI (~0.06 bits) 可比，信噪比 ~ 0.05 — 不可测。

**实用上限：** $\theta_{\text{max}} = 0.5\pi$（RZZ(π/2) = CZ）。QCMI ≈ 1.0 bit。门错误 ~ 3×10⁻³。

**可用θ区间：** $\theta \in [0.05\pi, 0.5\pi]$（0.16-1.57 rad）。

在此区间内：

| θ (×π) | α_eff (predicted) | 所需QCMI精度 (区分α=1.8 vs 4.0) |
|:------|:----:|:--------------------------|
| 0.5 | -0.29 | 大θ，α不可靠（高阶项主导）|
| 0.25 | 0.30 | 大θ，log近似差 |
| 0.125 | 1.22 | α提取困难（高阶项大）|
| 0.0625 | 1.49 | 中等精度需求 (~5% QCMI误差) |
| 0.05 | 1.57 | 最佳折衷点？ |

**最佳测量点：** $\theta \approx 0.05\pi - 0.10\pi$（QCMI ~ 0.15-0.60 bits），此时α_eff显著偏离2但仍在log近似范围内，且QCMI足够大以克服噪声。

### 4.4 与CCQ O(θ⁴)预言的对比——在IBM Q上可区分吗？

**CCQ预言**（已被LP38证伪，但作为null hypothesis仍有意义）：
$$\text{QCMI}_{\text{CCQ}}(\theta) = O(\theta^4)$$

具体地，如果CCQ正确，在θ=0.1π时QCMI ≈ 2×10⁻⁴ bits（用η₀ ∝ Σ|c|⁴ = θ⁴/4的典型值）。

LP38预言：在θ=0.1π时QCMI ≈ 0.30 bits。

**差值：** Δ ≈ 0.30 bits — 巨大！

$\theta = 0.1\pi$ 时：
- LP38 (α≈1.6): QCMI ≈ 0.30 bits
- CCQ (α≈4.0): QCMI ≈ 2×10⁻⁴ bits  
- Δ ≈ 1500倍
- 信噪比 ≈ 0.30/0.06 ≈ 5 (噪声主要来自门去极化)

**结论：在IBM Q上，区分LP38和CCQ在θ≈0.1π时是完全可行的**——只需要约 O(10⁵) shots的X基测量即可以>10σ区分。

但是，$\theta = 0.1\pi$ 处α_eff ≈ 1.6，不是1.81。要在α≈1.81处区分，需要θ↓ ≈ 0.004π，此时QCMI ≈ 0.002 bits，与假信号(~0.06 bits)不可区分。

**调整后的可检验声明：**

| 声明 | 检验方法 | 所需θ | 可验证？ |
|:-----|:-------|:----|:------:|
| QCMI > 0 (CFOL定性) | QCMI显著超过噪声地板 | >0.03π | ✓ |
| QCMI ∝ θ²·log(1/θ) 而非 θ⁴ | 两相邻θ点的斜率 | 0.05-0.15π | ✓ |
| α_eff → 2 (渐近) | 拟合多θ点，外推 | 需多θ扫描 | ✓ 但噪声限制精度 |
| α_eff ≈ 1.81 at small θ | 需要极小θ | <0.005π | ✗ 噪声淹没 |

**注：本评估与B博士的"区分α≈1.8 vs 4.0极易"不矛盾——两者讨论不同精度层级。** 区分O(θ²) vs O(θ⁴)（相差~1500倍于θ=0.01π）只需粗糙QCMI测量，当前可行。精确测量α≈1.81到±0.01需要极高精度，当前不可行。

**实际可行的实验问题：** 在IBM Q上可以回答：

1. QCMI的θ标度是O(θ²)还是O(θ⁴)？（可行，3-5个θ点足够）
2. QCMI是否随log(1/θ)偏离纯θ²标度？（需要高统计，但可行）
3. α的精确数值是多少？（精度受限于门噪声→约±0.2）

### 4.5 反事实预言——如果用非对齐轴

如果各边的Cartan轴不对齐（例如，边1用RZZ，边2用RXX，边3用RYY，边4用RZZ）：

对易性定理预言：QCMI在轴失配时大于轴对齐时。具体地，对于轴失配配置，BCH展开中的非相邻边对易子非零 → 产生额外的θ²阶贡献。

**可检验声明：对齐轴QCMI < 失配轴QCMI，对相同θ。**

在IBM Q上这比测试α值更容易：
- 两组θ相同的实验，不同轴配置
- 差值应显著 > 0
- 所需统计：中等（~10⁶ shots per configuration）

---

## Part 5: 实验可行性评估

### 5.1 4-qubit因果环所需的原生门数

| 阶段 | 操作 | 双qubit门数 (乐观) | 双qubit门数 (保守) | 单qubit门数 |
|:----|:-----|:---:|:---:|:--:|
| R-Q Bell对 | 1 CZ + 2 H | 1 | 1 | 2 |
| E₁ mixed态 | 1 ancilla CNOT + Ry | 1 | 1 | 1 |
| E₂ mixed态 | 1 ancilla CNOT + Ry | 1 | 1 | 1 |
| 路由SWAP | 0-2 SWAPs | 0 | 6 (2×3 CZ) | 0-4 |
| 环演化u₁-u₄ | 4 RZZ(θ) | 4 | 4 | 0 |
| X基测量准备 | 4 H (X→Z基) | 0 | 0 | 4 |
| **总计** | — | **7** | **13** | **8-12** |

最悲观估计下（2个完整SWAP分解为6个CZ），总双qubit门数 = 13。

### 5.2 电路深度在相干时间内吗？

**门持续时间：**
- CZ gate (Heron): ~100-200 ns（tunable coupler实现）
- RZZ(θ) 分数门: ~100-200 ns（与CZ类似，单脉冲）
- SX (√X): ~35 ns
- SWAP (3 CZ + 单qubit门): ~400-600 ns
- 测量: ~1-2 μs

**总电路时间：**
- 制备阶段: ~600 ns (1 CZ + 单qubit门)
- 路由阶段 (2 SWAP): ~1200 ns
- 环演化 (4 RZZ): ~800 ns
- 测量准备 (4 H): ~140 ns
- 测量: ~2 μs

**总计原始门时间: ~4.7 μs**

加上每个门之间的idle/缓冲时间和parallel scheduling的开销：
- 实际电路深度: ~8-15 μs（取决于并行度）

**与相干时间的比较：**

| 处理器 | T1 (μs) | T2 (μs) | 电路时间 (μs) | T1内？ | T2内？ |
|:------|:-----:|:-----:|:---:|:---:|:---:|
| Heron r1 (ibm_torino) | 168 | 130 | 8-15 | ✓ (11-21倍裕度) | ✓ (9-16倍裕度) |
| Heron r3 | >200 | >150 | 8-15 | ✓ (~15倍裕度) | ✓ (~10倍裕度) |
| Eagle r3 (ibm_sherbrooke) | 265 | 186 | 12-25 | ✓ (~10倍裕度) | ✓ (~7倍裕度) |

**结论：电路深度在相干时间内，有约10-20倍的安全裕度。**

主导错误源是门保真度（每个CZ ~0.3-0.7%错误率），而非退相干。

### 5.3 QCMI层析所需的shot数

**核心问题：** 要区分α≈1.8和α≈4.0需要多少shots？

使用X基简化协议（1个Pauli设置，16个bin）：

区分两个模型的所需统计量：
$$\Delta\text{QCMI} = |I_{\text{LP38}} - I_{\text{CCQ}}| \gg \sigma_I$$

其中 $\sigma_I \approx \frac{1}{\sqrt{N}} \cdot f(\{p_i\})$ 是QCMI估计的统计误差。

对于N个总shots和16个bin概率 $\{p_i\}$，最大似然估计的方差：
$$\text{Var}[\hat{S}] \approx \sum_i p_i(\log_2 p_i + S)^2 / N$$

在θ=0.1π时，用解析值$p_i$估计：
$$\sigma_I \approx \frac{1.5}{\sqrt{N}} \text{ bits}$$

要求 $\sigma_I < 0.02$ bits（<10% of signal）：
$$N_{\text{required}} > \left(\frac{1.5}{0.02}\right)^2 \approx 5625 \text{ shots}$$

**但这是理想统计。实际上还有系统误差（门噪声、读取错误等）。**

加上系统误差后的effective shot需求：
$$N_{\text{eff}} \approx N_{\text{stat}} \cdot \left(1 + \frac{\sigma_{\text{sys}}^2}{\sigma_{\text{stat}}^2}\right)$$

如果系统误差 $\sigma_{\text{sys}} \approx 0.03-0.06$ bits（来自门去极化），那么 $\sigma_{\text{sys}} \gg \sigma_{\text{stat}}$，shot数不重要——门保真度才是限制因素。

**诚实结论：在IBM Q上，QCMI精度的限制因素不是shot统计，而是门保真度。** 即使无限多的shots，只能将QCMI精度降到~0.03-0.06 bits的系统误差水平。

### 5.4 门保真度对α测定的影响

考虑去极化噪声模型，每个RZZ(θ)门附加保真度 $F = 1-\epsilon$。

测得的密度矩阵：
$$\rho_{\text{meas}} = F^{N_g} \rho_{\text{ideal}} + (1-F^{N_g}) \frac{I}{d}$$

其中 $I/d$ 是完全混合态。

对于对齐轴RXX/RZZ环：
- 理想 $\rho_{RQ}$ 的QCMI = $S_{\text{ideal}}$
- 测得 $\rho_{RQ}^{\text{meas}} = F^{N_g} \rho_{RQ}^{\text{ideal}} + (1-F^{N_g}) I/4$ (4×4)
- 测得QCMI: $I_{\text{meas}} \approx I_{\text{ideal}} - N_g \epsilon \cdot (S_{\text{mixed}} - S_{\text{ideal}})$

对于小θ（理想态接近纯态→$S_{\text{ideal}}$小→$S_{\text{mixed}}-S_{\text{ideal}}$大），门错误贡献的假QCMI可能**超过**真实信号。

**有效α测量的可行性窗口：**

| θ | QCMI (理想, bits) | 噪声floor (bits, N_g=10, ε=0.003) | 信噪比 |
|:--|:--|:--|:--:|
| π/2 | 1.0 | 0.06 | 16.7 |
| π/4 | 1.22 | 0.06 | 20.3 |
| π/8 | 0.60 | 0.06 | 10.0 |
| π/16 | 0.23 | 0.06 | 3.8 |
| π/32 | 0.078 | 0.06 | 1.3 |
| π/64 | 0.024 | 0.06 | 0.4 |
| π/128 | 0.0073 | 0.06 | 0.12 |

**实际可测范围：θ ≥ π/32（约 3.3σ at π/32, S/N ≈ 1.3）。**

在这个范围内（θ: π/32 → π/4），α_eff 范围：~1.63 → ~0.30。

**此范围内区分α≈1.81和α≈4.0？** 不能直接用3个点拟合（α~0.3→1.6之间的log修正太弱）。但可以检验**趋势**：

- 如果CCQ正确：QCMI ∝ θ⁴，在[π/32, π/4]区间变化约 $2^8 = 256$倍
- 如果LP38正确：QCMI ∝ θ²·log(1/θ)，在[π/32, π/4]区间变化约 $8^2$·log(32)/log(4) ≈ 160倍，但有额外的log增强

用2-3个点测量标度指数可以直接区分两者。

### 5.5 当前IBM Q硬件的适用性总结

| 需求 | 状态 | 问题 |
|:-----|:---:|:----|
| 4-qubit拓扑环 | ❌ | 重六角无4-环，需SWAP路由 |
| RZZ(θ)原生门 | ✅ | Heron分数门，2024 Nov引入 |
| 相干时间内的电路 | ✅ | 10-20倍裕度 |
| 满秩环境态制备 | ⚠️ | 需2 ancilla + pure ρ→mixed |
| X基测量（1设置） | ✅ | 简单 |
| 门保真度足够区分α | ⚠️ | 只在大θ(≥π/32)可行 |
| 测量精度足够区分配置 | ⚠️ | 系统误差>统计误差 |
| Bell对制备保真度 | ✅ | ~99.5% |
| 多θ扫描校准 | ⚠️ | 每次RZZ(θ)需独立校准 |

### 5.6 最终诚实评估

**可行的实验范围：**

| 能回答的问题 | 可行性 | 说明 |
|:--------|:---:|:----|
| QCMI > 0 是否被因果环强制？ | **高** | 大θ, 明显信号 |
| QCMI标度是O(θ²)还是O(θ⁴)？ | **中等** | 3-5点θ扫描，S/N ≥ 3 |
| 对齐vs失配轴的差异？ | **中等** | 两配置比较，相同θ |
| α → 2的渐近趋势？ | **低** | 需要多θ+外推，系统误差大 |
| α ≈ 1.81的精确验证？ | **不可行** | 需要的θ太小，噪声淹没 |

**推荐实验设计：**

1. **最小可行实验（1天）**：θ=0.25π一点，X基测量，验证QCMI > noise floor
2. **核心实验（1周）**：θ∈{0.25π, 0.125π, 0.0625π, 0.03125π}四点扫描，RZZ对齐 + 对照组，拟合α
3. **完整实验（1月）**：+失配轴配置 + RYY + RXX对比 + 误差缓解

**如果一切顺利：** 可以在IBM Q上以~3σ置信度排除CCQ的O(θ⁴)声称，并为LP38的O(θ²·log)标度律提供~2σ支持。

**但这不应作为独立的验证——** IBM Q实验的意义在于**原理验证（proof-of-principle）**，证明因果环拓扑在真实量子硬件上确实产生非零QCMI，且标度与理论一致。精确的α值需要用更高保真度的设备（如离子阱或中性原子）来验证。

---

## 附录A: Qiskit伪代码——对齐轴RZZ环

```python
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
import numpy as np

def prepare_bell_pair(qc, qubit_a, qubit_b):
    """Prepare |Φ⁺⟩ = (|00⟩ + |11⟩)/√2"""
    qc.h(qubit_a)
    qc.cz(qubit_a, qubit_b)  # IBM native CZ
    qc.h(qubit_a)  # Convert CZ→CNOT equivalent
    return qc

def prepare_mixed_state(qc, target, ancilla, p):
    """Prepare diag(p, 1-p) on target via purification"""
    theta = 2 * np.arccos(np.sqrt(p))
    qc.ry(theta, ancilla)
    qc.cx(ancilla, target)  # Will transpile to CZ+H
    qc.reset(ancilla)  # Discard ancilla (mid-circuit reset)
    return qc

def build_causal_ring_circuit(theta, p, use_rzz=True):
    """
    Build 4-qubit causal ring circuit.
    
    Qubits: q[0]=Q_a, q[1]=E_1, q[2]=Q_b, q[3]=E_2
    Ancillae: q[4]=anc_E1, q[5]=anc_E2
    """
    n_qubits = 6  # 4 core + 2 ancillae
    qc = QuantumCircuit(n_qubits, 4)  # 4 classical bits for measurement
    
    # Stage 1: State preparation
    prepare_bell_pair(qc, 0, 2)       # |Φ⁺⟩ on Q_a-Q_b
    prepare_mixed_state(qc, 1, 4, p)  # ρ_E1 = diag(p,1-p)
    prepare_mixed_state(qc, 3, 5, p)  # ρ_E2 = diag(p,1-p)
    
    # Stage 2: Causal ring evolution (aligned RZZ)
    if use_rzz:
        qc.rzz(theta, 0, 1)  # u₁: Q_a-E₁
        qc.rzz(theta, 1, 2)  # u₂: E₁-Q_b
        qc.rzz(theta, 0, 3)  # u₃: Q_a-E₂
        qc.rzz(theta, 2, 3)  # u₄: Q_b-E₂
    else:
        # Fallback: decompose RZZ(θ) = CNOTs + RZ
        # Each RZZ(θ) implemented as: CX, RZ(θ), CX
        for pair in [(0,1), (1,2), (0,3), (2,3)]:
            qc.cx(pair[0], pair[1])
            qc.rz(theta, pair[1])
            qc.cx(pair[0], pair[1])
    
    # Stage 3: X-basis measurement (for LP38 simplified protocol)
    for i in range(4):
        qc.h(i)  # Rotate X→Z for standard measurement
    qc.measure([0, 1, 2, 3], [0, 1, 2, 3])
    
    return qc

# Transpile for specific backend
service = QiskitRuntimeService()
backend = service.backend('ibm_torino', use_fractional_gates=True)
circuit = build_causal_ring_circuit(theta=np.pi/8, p=0.7)
transpiled = transpile(circuit, backend=backend, optimization_level=3)
```

## 附录B: 理论参数速查表

| 参数 | 符号 | 典型值 | 单位 |
|:---|:---|:-----|:---|
| Transmon频率 | ω/2π | 4.8-5.2 | GHz |
| anharmonicity | δ/2π | -330 | MHz |
| 交换耦合 | J/2π | 5-30 | MHz |
| CZ gate时间 | τ_CZ | 100-200 | ns |
| RZZ(θ) gate时间 | τ_RZZ | 100-200 | ns |
| T1 (Heron r1) | — | 168 | μs |
| T2 (Heron r1) | — | 130 | μs |
| CZ gate fidelity (Heron r3) | F_CZ | 0.997-0.999 | — |
| 读取保真度 | F_read | 0.98 | — |
| 耦合图围长 | girth | 6 | — |
| 6-cycle存在？ | — | 是（六边形面） | — |
| 4-cycle存在？ | — | 否 | — |

---

*文档完成。这是LP38因果环理论→IBM Q transmon设备的第一份完整映射。核心发现：(1) RZZ(θ)分数门是天然对齐轴配置；(2) 重六角晶格无4-环是需要SWAP路由的严重限制；(3) 系统噪声（非shot统计）是精度限制；(4) O(θ²) vs O(θ⁴)的区分在IBM Q上可行，但α≈1.81的精确验证不可行。*
