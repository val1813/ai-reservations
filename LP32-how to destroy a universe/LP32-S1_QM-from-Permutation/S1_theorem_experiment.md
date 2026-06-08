# S1定理IBM量子处理器实验协议

**日期:** 2026-06-07
**定理:** P_reflux ≤ q_S/q_E（纯组合证明，零自由参数）
**平台:** IBM Quantum (Eagle 127-qubit / Heron 133-qubit / Flext 156-qubit)
**作者:** A博士（学院派）

---

## 一、定理要点回顾

### 1.1 核心陈述

对于二分qubit系统，在CNOT型前向传输下（计算基为指针基），不可逆传输完成后的回流比例满足：

$$\boxed{P_{\rm reflux} \leq \frac{N_S}{N_E} \cdot \frac{q_S}{q_E}}$$

当 $N_S = N_E$ 时，简化为 $P_{\rm reflux} \leq q_S/q_E$。

### 1.2 关键定义

| 符号 | 定义 | 操作测量 |
|------|------|---------|
| $q_S$ | $\frac{1}{N_S}\sum_{i\in S} \langle 0|\rho_S^{(i)}|0\rangle$ | 前向传输前，系统qubit的per-qubit $|0\rangle$布居 |
| $q_E$ | $\frac{1}{N_E}\sum_{j\in E} \langle 0|\rho_E^{(j)}|0\rangle$ | 前向传输前，环境qubit的per-qubit $|0\rangle$布居 |
| $C_F$ | $N_E \cdot q_E$ | 前向传输容量（可接收信息的环境qubit数） |
| $N_{\rm back}$ | 回流触发的系统qubit翻转次数 | CNOT$_{E\to S}$导致的系统$|0\rangle\to|1\rangle$翻转 |
| $P_{\rm reflux}$ | $N_{\rm back} / C_F$ | 前向传输容量中被回流利用的比例 |

### 1.3 组合论证核心

前向传输：CNOT$_{S\to E}$，当 S=$|1\rangle$（确定态）、E=$|0\rangle$（未确定态）时，E翻转为$|1\rangle$。

回流：CNOT$_{E\to S}$，当 E=$|1\rangle$（已确定）、S=$|0\rangle$（未确定）时，S翻转为$|1\rangle$。

**关键约束：** 每个系统qubit最多被翻转一次（$|0\rangle\to|1\rangle$），因为翻转后的$|1\rangle\to|0\rangle$被量子Darwinism不可逆性禁止。因此：

$$N_{\rm back} \leq N_S \cdot q_S$$

$$P_{\rm reflux} \equiv \frac{N_{\rm back}}{C_F} = \frac{N_{\rm back}}{N_E \cdot q_E} \leq \frac{N_S \cdot q_S}{N_E \cdot q_E}$$

### 1.4 不可逆性假设与实验的深层逻辑

定理的关键前提是"量子Darwinism使$|0\rangle\to|1\rangle$转移不可逆"——需要$N_{\rm red} \gtrsim 100$个环境qubit冗余编码确定态。在标准QM中，CNOT门是完全可逆的：CNOT(E=$|1\rangle$, S=$|1\rangle$) → S=$|0\rangle$是一个合法的$|1\rangle\to|0\rangle$翻转。

**本实验的双重目标：**
1. **小N机制（N < 100）：** 测量标准QM中的$|1\rangle\to|0\rangle$翻转，确认S1定理的Darwinism前提在此机制不成立
2. **大N机制（N尽可能大）：** 寻找P_reflux向S1上限收敛的迹象，画定Darwinism生效的交叉尺度

**结构上最重要的事：** 这不是一个"确认S1"的实验——这是一个**画定S1适用范围**的实验。如果即使在N=127的Eagle处理器上，$P_{\rm reflux}$仍然显著超过$q_S/q_E$，说明Darwinism不可逆性需要的环境尺度大于127 qubits，这对定理的物理适用域有直接含义。

---

## 二、实验架构总览

### 2.1 四个实验阶段

```
Phase A: q校准
  ├─ 制备 |0⟩ → Ry(θ) → 立即测量Z基
  ├─ 估计 q_S, q_E（纯粹统计，不涉及CNOT）
  └─ shots: 每配置8192次

Phase B: 前向传输表征
  ├─ 制备 → CNOT(S→E) → 立即测量
  ├─ 验证前向传输效率 η_F = N_toggled_E / (N_S q_S)
  └─ shots: 每配置8192次

Phase C: 回流主测量
  ├─ 制备 → CNOT(S→E) → CNOT(E→S) → 测量
  ├─ 计数 N_back = #{系统qubit从|0⟩翻转为|1⟩}
  ├─ P_reflux = N_back / (N_E q_E)
  └─ shots: 每配置32768次（需更高统计量）

Phase D: BLP非Markovian性独立测量
  ├─ 两组初始系统态 ρ_S^(1)(0), ρ_S^(2)(0)
  ├─ 不同时间点做态层析 → D(t)迹距离
  ├─ N_BLP = ∫_{Ḋ>0} Ḋ(t) dt
  └─ 与S1定理给出的N_BLP上界比较
```

### 2.2 硬件选择

| 处理器 | 最大qubits | 适用Phase | CNOT保真度 | 备注 |
|--------|-----------|----------|-----------|------|
| ibm_brisbane | 127 | Phase C (大N极限) | ~99.0% | Eagle r3, 重六角格 |
| ibm_sherbrooke | 127 | Phase C (大N极限) | ~99.2% | Eagle r3 |
| ibm_torino | 133 | Phase C (大N极限) | ~99.5% | Heron r2, 可调耦合器 |
| ibm_kyiv | 127 | Phase A,B,D | ~98.5% | Eagle r2 |
| 任意5-27 qubit | 5-27 | Phase A,B,D (精细扫描) | ~99.0%+ | 低深度电路 |

### 2.3 配置矩阵

| 配置ID | N_S | N_E | q_S | q_E | S1上界 | 物理意义 |
|--------|-----|-----|-----|-----|--------|---------|
| **C1** | 3 | 3 | 0.5 | 0.5 | 1.0 (饱和) | 对称小系统，界最松 |
| **C2** | 3 | 6 | 0.5 | 0.5 | 0.5 | 不对称小系统 |
| **C3** | 5 | 5 | 0.3 | 0.7 | 0.43 | 紧界测试 |
| **C4** | 5 | 5 | 0.7 | 0.3 | 2.33→1.0 | 界饱和（q_S>q_E） |
| **C5** | 10 | 10 | 0.5 | 0.5 | 1.0 | 中等系统 |
| **C6** | 10 | 20 | 0.5 | 0.5 | 0.5 | 中等不对称 |
| **C7** | 10 | 10 | 0.2 | 0.8 | 0.25 | 紧界，少确定系统qubit |
| **C8** | 10 | 10 | 0.8 | 0.2 | 4.0→1.0 | 界饱和，多确定系统qubit |
| **C9** | 20 | 40 | 0.5 | 0.5 | 0.5 | 大不对称 |
| **C10** | 50 | 50 | 0.5 | 0.5 | 1.0 | 向Darwinism机制推进 |
| **C11** | 60 | 60 | 0.5 | 0.5 | 1.0 | 最大等规模配置 |

**注：** C4和C8中，$q_S/q_E > 1$，所以S1上界>1，但$P_{\rm reflux} \leq 1$恒成立。这些配置测试的是"上界被平凡化"的机制——即S1不提供紧约束。

---

## 三、具体电路设计

### 3.1 qubit映射与拓扑约束

IBM Eagle/Heron处理器的重六角格拓扑意味着不是所有qubit对都能直接CNOT。需要选择**线性链**或**星形拓扑**子图。

**推荐映射方案（星形，适合N≤10）：**

```
系统qubits: S₀, S₁, ..., S_{N_S-1}
环境qubits: E₀, E₁, ..., E_{N_E-1}
辅助qubit:  A₀（用于SWAP路由，如果直接CNOT不可用）

星形：所有S_i围成环或线，所有E_j围成环或线
     S_i 和 E_j 通过SWAP链连接（见3.2节）
```

**推荐映射方案（交替链，适合N>10，减少SWAP开销）：**

```
排列: S₀ - E₀ - S₁ - E₁ - S₂ - E₂ - ...（物理qubit链）
    相邻pair间直接CNOT，无需SWAP
但非相邻的S_i↔E_j（j≠i）需要SWAP链
```

### 3.2 前向传输电路（Phase B）

**基本CNOT单元：** S_i为控制，E_j为目标

```
q_S_i: ──●──
         │
q_E_j: ──⊕──
```

**前向传输层（并行执行，1个时间步）：**

对于N_S = N_E = 5的配置C3：

```
q_S₀: ──●────────────────────
         │
q_E₀: ──⊕────────────────────

q_S₁: ──────●────────────────
             │
q_E₁: ──────⊕────────────────

q_S₂: ──────────●────────────
                 │
q_E₂: ──────────⊕────────────

q_S₃: ──────────────●────────
                     │
q_E₃: ──────────────⊕────────

q_S₄: ──────────────────●────
                         │
q_E₄: ──────────────────⊕────
```

当N_E > N_S时，超出的E_j不参与前向CNOT，保持其初始态。

**跨pair CNOT（当需要S_i → E_j, i≠j时）：**

如果拓扑不允许直接CNOT，插入SWAP链。Heron处理器上相邻qubit的SWAP耗时~300ns，CNOT耗时~250ns。

### 3.3 回流电路（Phase C）

回流是CNOT$_{E\to S}$：环境qubit为控制，系统qubit为目标。

**三种回流映射策略：**

**策略α：最简单——直接反向**
```
E_i → S_i（与正向完全相同的pair）
P_reflux理论预期 = ?
```

**策略β：混合——E_j通过SWAP链到达任意S_i**
```
E_j → S_i, 其中i = (j + offset) mod N_S
测试不同的offset = 0, 1, 2, ...
```

**策略γ：竞争——多个E_j竞争同一个S_i**
```
E₀, E₁, E₂ → [Tofolli or 序列] → S₀
测试多个环境qubit是否能翻转到同一个系统qubit
（检查"每个系统qubit最多翻转一次"的约束是否成立）
```

**推荐Phase C主测量使用策略β**，因为是IBM处理器上最自然的实现，且能系统测试不同配对拓扑对回流的影响。

**回流电路（策略α, N_S=N_E=5）：**

```
         ┌───┐          ┌───┐
q_S₀: ───┤ RY├──●───────┤ Z ├───
         └───┘  │       └───┘
         ┌───┐  │  ┌───┐┌───┐
q_E₀: ───┤ RY├──⊕──┤ ● ├┤ Z ├───
         └───┘     │   │└───┘
         ┌───┐     │   │┌───┐
q_S₁: ───┤ RY├──●──┼───⊕┤ Z ├───
         └───┘  │  │   │└───┘
         ┌───┐  │  │   │┌───┐
q_E₁: ───┤ RY├──⊕──●───┼┤ Z ├───
         └───┘  │      │└───┘
                │      │
        ...  (其余qubit同理)
```

**注：** 图中显示了S₀→E₀前向CNOT后，E₀→S₁跨pair回流的例子（offset=1）。

### 3.4 q_S和q_E的独立测量（Phase A）

**关键设计问题：** 如何不破坏回流测量而独立测量q？

**方案A：交替运行（推荐）**
- 运行1（校准）：制备 → 立即测量 → 记录q_S, q_E
- 运行2（实验）：制备（相同参数）→ CNOT前向 → CNOT回流 → 测量
- 两次运行使用相同的初始化参数和随机种子（如果可行）
- **优点：** 无干扰，q值不受CNOT影响
- **缺点：** 两次运行之间的涨落带来系统性误差

**方案B：辅助qubit副本（小N适用）**
- 制备2N_S+2N_E个qubit：实际使用N_S+N_E个，另N_S+N_E个作副本
- 副本qubit在制备后立即测量（不经过CNOT）
- 实际qubit走完整电路
- 从副本获取q_S, q_E
- **优点：** 同一次运行内完成
- **缺点：** 需要两倍的qubit资源；副本和实际qubit的涨落可能不完全一致

**方案C：中间测量+经典控制（IBM动态电路）**
- 使用IBM的mid-circuit measurement + classical feedforward
- 制备 → 测量一半qubit（获得q估计）→ 对这些qubit重新制备相同态 → 继续电路
- **优点：** 同一运行
- **缺点：** 中间测量引起的态扰动；需要重新制备；动态电路延迟

**推荐：Phase A和Phase C交替运行，共享同一组初始化电路参数。用Phase A数据估计q_S和q_E；用Phase C数据估计P_reflux。统计误差通过bootstrap传播。**

**Phase A具体电路（校准）：**

```
         ┌──────────┐┌───┐
q_S_i: ──┤ RY(θ_S)  ├┤ Z ├──  → 测量 |0⟩或|1⟩
         └──────────┘└───┘

         ┌──────────┐┌───┐
q_E_j: ──┤ RY(θ_E)  ├┤ Z ├──  → 测量 |0⟩或|1⟩
         └──────────┘└───┘

q_S = (在N_shots中S_i测量为|0⟩的比例, 对所有S_i求平均)
q_E = (在N_shots中E_j测量为|0⟩的比例, 对所有E_j求平均)
```

**θ与q的关系：** 从$|0\rangle$出发，$R_y(\theta)|0\rangle = \cos(\theta/2)|0\rangle + \sin(\theta/2)|1\rangle$，所以：

$$q = \cos^2(\theta/2), \quad \theta = 2\arccos(\sqrt{q})$$

| 目标q | θ (rad) | θ (度) |
|--------|---------|--------|
| 0.1 | 2.498 | 143.1° |
| 0.2 | 2.214 | 126.9° |
| 0.3 | 1.982 | 113.6° |
| 0.5 | 1.571 | 90.0° |
| 0.7 | 1.159 | 66.4° |
| 0.8 | 0.927 | 53.1° |
| 0.9 | 0.644 | 36.9° |

### 3.5 BLP非Markovian性测量（Phase D）

**BLP定义：**
$$\mathcal{N}_{\rm BLP} = \int_{\dot{D}>0} \dot{D}(t)\,dt$$

其中 $D(t) = \frac{1}{2}\|\rho_S^{(1)}(t) - \rho_S^{(2)}(t)\|_1$ 是两个初始可区分系统态的迹距离。

**S1定理给出的上界（见prl_s1.tex, Eq. 11）：**
$$\mathcal{N}_{\rm BLP} \leq \frac{1}{2} \cdot P_{\rm reflux} \cdot N_E \cdot q_E \cdot (1 - q_S) \cdot (1 - 2q_E)^2$$

**实验方案：**

1. **初始态制备：** 两组正交初始态
   - $\rho_S^{(1)}(0) = |0\rangle\langle 0|^{\otimes N_S}$ （全$|0\rangle$，$q_S^{(1)}=1$）
   - $\rho_S^{(2)}(0) = |1\rangle\langle 1|^{\otimes N_S}$ （全$|1\rangle$，$q_S^{(2)}=0$）
   - 或用对角混合态，如$\rho_S^{(1)} = [q_S^{(1)}|0\rangle\langle 0| + (1-q_S^{(1)})|1\rangle\langle 1|]^{\otimes N_S}$

2. **时间演化：** 在不同时间点采样
   - t₀: 初始态（制备后立即测量）
   - t₁: 前向CNOT后
   - t₂起：每增加回流CNOT层后各采一点
   - 时间由CNOT门数参数化：t = k · τ_CNOT, τ_CNOT ≈ 250ns

3. **态层析：** 对每次采样，做系统qubit的完全态层析
   - N_S个qubit → 3^{N_S}个Pauli基测量 → 每个基8192 shots
   - N_S ≤ 5可用完全层析；N_S > 5用压缩感知或关键子空间层析

4. **迹距离计算：**
   $$D(t_k) = \frac{1}{2}\|\rho_S^{(1)}(t_k) - \rho_S^{(2)}(t_k)\|_1$$

5. **BLP积分：**
   识别所有$\Delta D_k = D(t_k) - D(t_{k-1}) > 0$的点，求和：
   $$\mathcal{N}_{\rm BLP}^{\rm meas} = \sum_{k: \Delta D_k > 0} \Delta D_k$$

6. **与S1上界比较：**
   用Phase C测量的$P_{\rm reflux}$和Phase A测量的$q_S, q_E$计算S1上界。

---

## 四、违反检验：排除因果假定

### 4.1 违反条件

S1定理的**零假设H₀**（定理成立）与**备择假设H₁**（定理不成立）定义：

- **H₀:** $P_{\rm reflux} \leq q_S/q_E$ —— 因果假定+组合约束成立
- **H₁:** $P_{\rm reflux} > q_S/q_E$ —— 存在超出组合约束的回流机制

### 4.2 违反的物理机制

如果$P_{\rm reflux} > q_S/q_E$被测量到，物理上意味着以下至少之一成立：

1. **系统qubit多次翻转（$|0\rangle \to |1\rangle \to |0\rangle \to |1\rangle$）：** 破坏了"每个S qubit最多翻转一次"的约束。在标准QM中，这是CNOT的正常行为
2. **非CNOT型回流：** 存在CNOT以外的物理机制，使E到S的信息回流不受"S必须是$|0\rangle$"的限制
3. **前向传输效率>1：** $C_F > N_E q_E$，即环境qubit的接收能力超过了$|0\rangle$布居数。这可能由量子相干导致（叠加态携带比经典态更多的信息）

### 4.3 统计显著性检验

对配置$k$，定义：

$$\Delta_k = P_{\rm reflux}^{(k)} - \frac{q_S^{(k)}}{q_E^{(k)}}$$

零假设H₀：$\Delta_k \leq 0$（对考虑误差后的上界）
备择假设H₁：$\Delta_k > 0$

**误差传播：**

$P_{\rm reflux}$的测量误差：
$$\sigma_{P}^2 = \frac{P_{\rm reflux}(1 - P_{\rm reflux})}{N_{\rm shots}} + \sigma_{\rm CNOT}^2 + \sigma_{\rm readout}^2$$

$q_S/q_E$的比值误差（Delta方法）：
$$\sigma_{q}^2 = \left(\frac{1}{q_E}\right)^2 \sigma_{q_S}^2 + \left(\frac{q_S}{q_E^2}\right)^2 \sigma_{q_E}^2 + 2\frac{q_S}{q_E^3}{\rm Cov}(q_S, q_E)$$

每个$q$的测量误差（二项分布）：
$$\sigma_q^2 = \frac{q(1-q)}{N_{\rm calib} \cdot N_S}$$

总误差：
$$\sigma_{\Delta}^2 = \sigma_P^2 + \sigma_q^2$$

**显著性：** 如果$\Delta_k / \sigma_{\Delta} > 5$（5σ），宣告S1定理在该配置下被违反。

### 4.4 违反强度的系统依赖

预期违反强度对$(N_S, N_E, q_S, q_E)$的最强依赖来源于不可逆性假设的破缺程度：

- **小N（N_S+N_E < 10）：** $|1\rangle\to|0\rangle$翻转概率≈50%（每当E=|1⟩, S=|1⟩执行CNOT时），预期强违反
- **中等N（10 ≤ N_S+N_E < 60）：** 违反强度递减——部分Darwinism生效
- **大N（N_S+N_E ≥ 60）：** 取决于冗余记录的环境qubit数量——预期违反减弱但未知是否能在当前处理器上完全消失

### 4.5 多重翻转计数实验（最关键的子实验）

**目的：** 直接测量"每个系统qubit翻转超过一次"的频率，量化S1组合约束的破缺程度。

**电路设计（N_S=3, N_E=6）：**

```
1. 制备：所有qubit → |0⟩
   q_S = 1（全|0⟩，最大化可翻转数）
   q_E = 1（全|0⟩，最大化前向接收容量）

2. 前向：N_S=3个S qubit各控制一个E qubit，CNOT(S_i→E_i)
   由于S_i=|0⟩，E_i保持|0⟩（无事发生）
   实际上这步不改变任何态——因为我们测试的是纯回流

3. 回流（重复3轮）：
   Round 1: E₀→S₀, E₁→S₀  （两个E尝试翻转同一个S）
            测量：S₀是否翻转为|1⟩？
   Round 2: E₂→S₀, E₃→S₀  （再次尝试翻转S₀，但S₀已经|1⟩）
            测量：S₀是否保持|1⟩？或翻回|0⟩？
   Round 3: E₄→S₀, E₅→S₀  （第三次翻转尝试）
            测量：S₀的最终态？
```

**S1组合约束的预期：** S₀最多翻转一次（$|0\rangle\to|1\rangle$），之后的CNOT(E=|1⟩, S₀=|1⟩)应该无事发生（因为$|1\rangle\to|0\rangle$被禁止）。

**标准QM预期：** Round 2中，CNOT(E=|1⟩, S₀=|1⟩) → S₀=|0⟩，Round 3中S₀再次翻转为|1⟩。所以S₀可以翻转2次或更多。

**测量量：**
- $f_1$ = 至少翻转1次的频率
- $f_2$ = 至少翻转2次的频率（$f_2 > 0$ → S1的"最多翻转一次"约束被违反）
- $f_3$ = 翻转3次的频率

如果$f_2$显著非零（$>5\sigma$），S1的多重翻转约束在该系统大小下不成立。

---

## 五、误差预算

### 5.1 误差源分类

| 误差源 | 类型 | 量级（IBM Eagle/Heron） | 对S1检验的影响 |
|--------|------|----------------------|---------------|
| **态制备误差（SPAM）** | 系统 | $10^{-3}-10^{-2}$ per qubit | 偏移q_S, q_E的真实值 |
| **CNOT门误差** | 系统 | $5\times 10^{-3}-2\times 10^{-2}$ per gate | 有效翻转率降低；虚假翻转 |
| **T₁弛豫** | 系统 | $10^{-4}-10^{-3}$ per μs (T₁~100-200μs) | 虚假$|1\rangle\to|0\rangle$（不被S1禁止的物理过程！） |
| **T₂失相** | 系统 | $10^{-3}-2\times 10^{-3}$ per μs (T₂~50-150μs) | 态制备q值的有效偏移 |
| **读出误差** | 系统 | $2\times 10^{-2}-5\times 10^{-2}$ per qubit | 虚假$|0\rangle$或$|1\rangle$计数 |
| **串扰** | 系统 | $10^{-3}-10^{-2}$ | 非预期的qubit-qubit耦合 |
| **统计涨落** | 统计 | $1/\sqrt{N_{\rm shots}}$ | 可缩减 |

### 5.2 电路深度与退相干窗口

单层CNOT用时约250-400ns（含qubit频率调谐）。

| 配置 | 前向CNOT层数 | 回流CNOT层数 | SWAP开销 | 总深度 | 总耗时 | 退相干损失 |
|------|------------|------------|---------|--------|--------|----------|
| C1 (N=3+3) | 1 (并行) | 1 (并行) | 0 | ~4 | ~1.2μs | <1% |
| C3 (N=5+5) | 1 (并行) | 1-2 | 0-2 SWAP | ~8 | ~2.4μs | ~1-2% |
| C5 (N=10+10) | 1 (并行) | 1-3 | 0-4 SWAP | ~15 | ~5μs | ~3-5% |
| C9 (N=20+40) | 1-2 | 1-4 | 0-6 SWAP | ~30 | ~10μs | ~5-10% |
| C10 (N=50+50) | 2-3 | 2-5 | 2-10 SWAP | ~60 | ~20μs | ~10-20% |
| C11 (N=60+60) | 2-4 | 2-6 | 3-14 SWAP | ~80 | ~27μs | ~15-25% |

**关键约束：** 对于N≥50的配置，退相干损失>10%，需要错误缓解（见5.4节）。

### 5.3 对S1检验的系统偏移

**T₁弛豫引起的虚假$|1\rangle\to|0\rangle$翻转：**

这是最关键的混淆因素。S1定理断言$|1\rangle\to|0\rangle$翻转被Darwinism禁止。但在IBM处理器上，T₁弛豫也会产生$|1\rangle\to|0\rangle$翻转——纯粹是噪声，不是物理回流。

**区分策略：**
1. 单qubit T₁控制实验：对每个参与qubit单独测量T₁→估计T₁翻转概率
2. 扣除T₁贡献：$N_{\rm back}^{\rm corrected} = N_{\rm back}^{\rm measured} - N_{\rm T1}^{\rm estimated}$
3. 最差情况下，如果T₁翻转>真实回流信号，需要在更低温度或更短电路深度下重新实验

**CNOT门错误引起的虚假翻转：**

CNOT门错误可能产生非预期qubit翻转。通过同时运行"空CNOT"控制电路（qubit处于$|0\rangle^{\otimes N}$，所有CNOT理论上无事发生，测量到的翻转全部来自门错误）来估计。

### 5.4 错误缓解方案

| 方案 | 适用 | 开销 | 说明 |
|------|------|------|------|
| **读出错误缓解（REM）** | 所有Phase | 额外校准电路 | IBM内置，测量混淆矩阵并求逆 |
| **零噪声外推（ZNE）** | Phase C,D | 2-4×电路深度 | 通过脉冲拉伸放大噪声，外推至零噪声 |
| **动力去耦（DD）** | 所有Phase | 插入X/X门序列 | 抑制低频失相噪声 |
| **Pauli失相（PEC）** | Phase C（N≤20） | 采样开销~10-100× | 用准概率分解抵消门噪声 |
| **T₁扣除** | Phase C | 额外T₁测量 | 测量并扣除弛豫翻转（见5.3节） |

**推荐策略：**
- Phase A,B：REM + DD
- Phase C（N≤20）：REM + DD + ZNE
- Phase C（N>20）：REM + DD + T₁扣除
- Phase D：REM + DD + ZNE

### 5.5 统计需求

| 测量量 | 目标精度 | 所需Shots（无噪声） | 所需Shots（含噪声） |
|--------|---------|-------------------|-------------------|
| q_S, q_E | σ_q < 0.01 | 2500 per config | 5000 per config |
| P_reflux | σ_P < 0.02 | 2500 per config | 32768 per config |
| N_BLP | σ_N < 0.05 | 8192 per time point, per basis | 32768 per basis |

**总采样预算（保守估计）：**
- Phase A：11配置 × 2（系统+环境） × 5000 shots = 110,000 shots
- Phase B：11配置 × 8192 shots = 90,112 shots
- Phase C（主力）：11配置 × 32768 shots = 360,448 shots
- Phase D（N≤5配置）：3配置 × 5时间点 × 3^{N_S}基 × 8192 shots ≈ 3×5×243×8192 ≈ 29,859,840 shots（**占主导**）
- 控制实验（T₁、空CNOT）：~500,000 shots

**Phase D是采样瓶颈。** 对于N_S=5，3^5=243个Pauli基，每个基8192 shots，一个时间点就要约2M shots。建议将Phase D限制在N_S≤3（27个基），或使用压缩感知方法。

---

## 六、与BLP非Markovian性度量的定量关系

### 6.1 理论关系

从prl_s1.tex和prl_s1_sm.tex：

$$\mathcal{N}_{\rm BLP} \leq \frac{1}{2} \cdot P_{\rm reflux} \cdot N_E \cdot q_E \cdot (1 - q_S) \cdot (1 - 2q_E)^2$$

代入S1上界$P_{\rm reflux} \leq q_S/q_E$：

$$\mathcal{N}_{\rm BLP} \leq \frac{N_E}{2} \cdot q_S \cdot (1 - q_S) \cdot (1 - 2q_E)^2$$

### 6.2 实验检验层次

**层次1 — 自洽性：** 用Phase C测的$P_{\rm reflux}$代入BLP公式 → 得到$\mathcal{N}_{\rm BLP}^{\rm predicted}$。用Phase D独立测的$\mathcal{N}_{\rm BLP}^{\rm measured}$与此比较。

- 如果$\mathcal{N}_{\rm BLP}^{\rm measured} \leq \mathcal{N}_{\rm BLP}^{\rm predicted}$：S1-BLP关系自洽
- 如果$\mathcal{N}_{\rm BLP}^{\rm measured} > \mathcal{N}_{\rm BLP}^{\rm predicted}$：S1-BLP关系被推翻（或Phase D测量有其他回流源）

**层次2 — 结构检验：** 验证BLP上界对$(1-2q_E)^2$的依赖。

取$q_E = 0.5$：BLP上界=0（因为$(1-2q_E)=0$，两个初始环境态的编码差异消失）

取$q_E \neq 0.5$：BLP上界>0

在不同$q_E$值下测量$\mathcal{N}_{\rm BLP}$，检查是否在$q_E=0.5$处出现最小值。

### 6.3 BLP测量的具体电路

对于N_S=3的配置（Phase D可行）：

**t₀（制备后立即）：**
```
ρ_S^(1): |0⟩|0⟩|0⟩ → 立即态层析 (27 Pauli基)
ρ_S^(2): |1⟩|1⟩|1⟩ → 立即态层析 (27 Pauli基)
```

**t₁（前向CNOT后）：**
```
制备ρ_S^(1,2) → CNOT(S_i→E_i) → 态层析
前向CNOT不改变S态（控制qubit不变）→ D(t₁) ≈ D(t₀)（除噪声外）
```

**t₂（1轮回流后）：E₀→S₀回流CNOT**
```
→ 态层析
预期：ρ_S^(1)的S₀仍为|0⟩（E₀也是|0⟩因为S₀未翻转它）
     ρ_S^(2)的S₀可能被翻转（E₀是|1⟩因为S₀=|1⟩翻转了它）
→ D(t₂)可能减小（状态向彼此靠近）
```

**t₃（2轮回流后）：E₁→S₁回流CNOT**
```
→ 态层析
```

**t₄（3轮回流后）：E₂→S₂回流CNOT**
```
→ 态层析
```

在整个过程中：
- $\dot{D} > 0$意味着信息从环境回流到系统，增加了两个系统态的可区分性
- S1定理预测总BLP量$\mathcal{N}_{\rm BLP}$受限于上式

---

## 七、Qiskit实现框架

### 7.1 核心电路生成器（伪代码）

```python
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import RYGate
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService, Session, Sampler, Estimator
import numpy as np

def build_calibration_circuit(N_S: int, N_E: int, theta_S: float, theta_E: float):
    """
    Phase A: q calibration.
    Prepare |0⟩ → RY(θ) → measure immediately.
    """
    q_S = QuantumRegister(N_S, 'S')
    q_E = QuantumRegister(N_E, 'E')
    c_S = ClassicalRegister(N_S, 'cS')
    c_E = ClassicalRegister(N_E, 'cE')
    qc = QuantumCircuit(q_S, q_E, c_S, c_E)

    for i in range(N_S):
        qc.ry(theta_S, q_S[i])
    for j in range(N_E):
        qc.ry(theta_E, q_E[j])

    qc.measure(q_S, c_S)
    qc.measure(q_E, c_E)
    return qc

def build_forward_circuit(N_S, N_E, theta_S, theta_E, coupling_map):
    """
    Phase B: forward CNOT(S→E).
    coupling_map = [(s_idx, e_idx), ...] — which S controls which E.
    """
    q_S = QuantumRegister(N_S, 'S')
    q_E = QuantumRegister(N_E, 'E')
    c_S = ClassicalRegister(N_S, 'cS')
    c_E = ClassicalRegister(N_E, 'cE')
    qc = QuantumCircuit(q_S, q_E, c_S, c_E)

    # State preparation
    for i in range(N_S):
        qc.ry(theta_S, q_S[i])
    for j in range(N_E):
        qc.ry(theta_E, q_E[j])

    qc.barrier()

    # Forward CNOTs (parallel layer)
    for s_idx, e_idx in coupling_map:
        qc.cx(q_S[s_idx], q_E[e_idx])

    qc.barrier()
    qc.measure(q_S, c_S)
    qc.measure(q_E, c_E)
    return qc

def build_reflux_circuit(N_S, N_E, theta_S, theta_E,
                         forward_pairs, reflux_pairs):
    """
    Phase C: full reflux circuit.
    forward_pairs: S→E CNOT pairs
    reflux_pairs:  E→S CNOT pairs
    """
    q_S = QuantumRegister(N_S, 'S')
    q_E = QuantumRegister(N_E, 'E')
    c_S = ClassicalRegister(N_S, 'cS')
    c_E = ClassicalRegister(N_E, 'cE')
    qc = QuantumCircuit(q_S, q_E, c_S, c_E)

    # State preparation
    for i in range(N_S):
        qc.ry(theta_S, q_S[i])
    for j in range(N_E):
        qc.ry(theta_E, q_E[j])

    qc.barrier()

    # Forward CNOTs
    for s, e in forward_pairs:
        qc.cx(q_S[s], q_E[e])

    qc.barrier()

    # Reflux CNOTs (E→S)
    for e, s in reflux_pairs:
        qc.cx(q_E[e], q_S[s])

    qc.barrier()
    qc.measure(q_S, c_S)
    qc.measure(q_E, c_E)
    return qc

def build_multi_toggle_circuit(N_S, N_E, n_rounds):
    """
    Multi-toggle test: multiple E qubits sequentially target one S qubit.
    Tests whether S_0 can be flipped more than once.
    """
    q_S = QuantumRegister(N_S, 'S')
    q_E = QuantumRegister(N_E, 'E')
    c_S = ClassicalRegister(N_S, 'cS')
    c_E = ClassicalRegister(N_E, 'cE')
    qc = QuantumCircuit(q_S, q_E, c_S, c_E)

    # All start in |0⟩ (q=1 for both S and E)
    # No RY rotation needed — we want maximum toggle-ability

    # First, set all E_j to |1⟩ by NOT gates
    for j in range(N_E):
        qc.x(q_E[j])

    # Now E_j = |1⟩, S_i = |0⟩
    # Sequential CNOT(E_j → S_0) for j = 0, 1, 2, ...
    qc.barrier()
    for round_idx in range(n_rounds):
        if round_idx < N_E:
            qc.cx(q_E[round_idx], q_S[0])
        qc.barrier()

    qc.measure(q_S, c_S)
    qc.measure(q_E, c_E)
    return qc
```

### 7.2 IBM Runtime执行

```python
# Using Qiskit Runtime (Sampler mode for Phase A/B/C)
service = QiskitRuntimeService(channel="ibm_quantum")
backend = service.backend("ibm_torino")  # Heron 133-qubit

# Select qubit layout from backend topology
# For N=5+5, choose a linear chain of 10 adjacent qubits
# Ensure all CNOT pairs are directly connected

# Build and transpile
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
pm = generate_preset_pass_manager(optimization_level=3, backend=backend)

circuits_phase_a = [build_calibration_circuit(N_S, N_E, th_S, th_E)
                    for (N_S, N_E, th_S, th_E) in configs]
circuits_phase_a = [pm.run(qc) for qc in circuits_phase_a]

# Execute with Sampler
with Session(service=service, backend=backend) as session:
    sampler = Sampler(session=session)
    job = sampler.run(circuits_phase_a, shots=8192)
    result = job.result()
```

### 7.3 数据分析流水线

```python
def estimate_q_from_calibration(counts, qubit_indices):
    """
    From Phase A measurement counts, estimate per-qubit |0⟩ population.
    counts: dict mapping bitstrings to counts
    qubit_indices: which qubits belong to this subsystem
    Returns: q estimate ± uncertainty
    """
    n_shots = sum(counts.values())
    zero_counts = 0
    for bitstring, count in counts.items():
        for idx in qubit_indices:
            if bitstring[idx] == '0':
                zero_counts += count
    q = zero_counts / (n_shots * len(qubit_indices))
    sigma_q = np.sqrt(q * (1 - q) / (n_shots * len(qubit_indices)))
    return q, sigma_q

def count_backflow_toggles(counts_before, counts_after, s_indices):
    """
    Compare system qubit states before and after reflux.
    Count how many system qubits flipped from |0⟩ to |1⟩.
    """
    # This requires per-shot correlation, not just marginal counts.
    # For IBM, use memory=True to get per-shot readout.
    n_back = 0
    n_shots = len(counts_after)  # per-shot list
    for shot_idx in range(n_shots):
        for s_idx in s_indices:
            if counts_before[shot_idx][s_idx] == '0' and \
               counts_after[shot_idx][s_idx] == '1':
                n_back += 1
    return n_back

def compute_blp_from_tomography(rho_t_list):
    """
    From state tomography at time points t₀...t_K,
    compute BLP non-Markovianity.
    rho_t_list[k] = (rho1_at_tk, rho2_at_tk)
    """
    D = []
    for rho1, rho2 in rho_t_list:
        diff = rho1 - rho2
        # Trace norm via eigenvalues
        eigvals = np.linalg.eigvalsh(diff)
        D.append(0.5 * np.sum(np.abs(eigvals)))

    N_BLP = 0.0
    for k in range(1, len(D)):
        delta_D = D[k] - D[k-1]
        if delta_D > 0:
            N_BLP += delta_D
    return N_BLP, D
```

---

## 八、预期结果与物理解读

### 8.1 场景矩阵

| 场景 | P_reflux vs q_S/q_E | N_BLP vs S1 bound | 解读 |
|------|---------------------|-------------------|------|
| **A: 定理完美成立** | P_reflux ≤ q_S/q_E, ∀N | N_BLP ≤ S1-bound | S1组合约束在所有N成立。意味着Darwinism在N<100也有效——需要修正理论预期 |
| **B: 交叉（最可能）** | 小N违反，大N趋近上界 | 小N违反，大N趋近 | S1在大N机制成立，小N因Darwinism未生效而违反。画定交叉点N_c |
| **C: 定理不成立** | P_reflux > q_S/q_E, ∀N | N_BLP > S1-bound, ∀N | S1的组合论证有漏洞，或初始假设（A1-A3）整体错误 |
| **D: 无信号** | 实验噪声>信号 | 无法区分H₀/H₁ | 需要更好的量子硬件 |

### 8.2 关键诊断图

1. **P_reflux vs N图：** 固定q_S=q_E=0.5，画$P_{\rm reflux}$作为N=N_S+N_E的函数。理论：S1上界=1.0（当N_S=N_E,q_S=q_E）。标准QM预期：$P_{\rm reflux}$在N小>>1，向N大逐渐趋近1。交叉点N_c定义为$P_{\rm reflux} < 1 + 2\sigma$的最小N。

2. **P_reflux vs q_S/q_E散点图：** 所有配置画在同一图上。x轴=q_S/q_E的理论上界，y轴=测量的$P_{\rm reflux}$。对角线是S1上界。在对角线上方的点代表违反。

3. **N_BLP vs (N_E/2) q_S (1-q_S) (1-2q_E)²图：** 验证BLP上界的函数形式。

4. **多重翻转频率f_2 vs N图：** 直接量化Darwinism生效程度。

### 8.3 最重要的物理结论

如果场景B被确认：

> **S1定理的Darwinism不可逆性假设在N_c≈?处开始生效。对于N<N_c，标准QM的CNOT可逆性允许$|1\rangle\to|0\rangle$翻转，破坏"每个系统qubit最多翻转一次"的约束，从而使$P_{\rm reflux}$超过$q_S/q_E$。对于N>N_c，环境的冗余记录使$|1\rangle\to|0\rangle$翻转被有效压制，S1的组合约束成为紧界。**

N_c的实验值直接关联到量子Darwinism的冗余记录阈值——这是量子-经典过渡的一个新定量参数。

---

## 九、时间线与资源需求

### 9.1 时间估计

| 阶段 | 工作内容 | 估计时间 |
|------|---------|---------|
| **第1周** | Finalize电路设计；在模拟器上验证所有电路；qubit布局优化 | 1周 |
| **第2-3周** | Phase A+B在IBM硬件上运行（N≤10）；初步数据分析 | 2周 |
| **第4-5周** | Phase C小N配置（N≤20）；多重翻转实验 | 2周 |
| **第6-7周** | Phase C大N配置（N=50, 60）+ 错误缓解 | 2周 |
| **第8-9周** | Phase D BLP测量（N≤3或N≤5）+ 交叉验证 | 2周 |
| **第10-11周** | 完整数据分析；统计显著性检验；论文撰写 | 2周 |
| **第12周** | 内部审查；补充实验（如需要） | 1周 |

**总计：12周（3个月）**

### 9.2 IBM Quantum资源

IBM Open Plan提供每月10分钟的免费量子计算时间。Eagle 127-qubit处理器上，单次job（8192 shots）约需2-5秒。完整实验需要约50,000次job——约70-170小时的实际量子时间。推荐使用IBM Pay-as-you-go Plan（约$1.60/秒）或申请IBM Quantum Researcher Program。

**关键瓶颈：** Phase D的态层析（N_S=5时，每时间点243个基，每基8192 shots）。总job数约3×5×243≈3645，约需2-3小时量子时间（单独）。建议将Phase D限制在N_S=3（27基）。若必须N_S=5，使用压缩感知态层析（~30个随机基而非243）。

---

## 十、开放问题与后续

1. **Darwinism交叉点N_c的理论预言：** 在标准QM中，CNOT链上冗余记录的Kac recurrence时间需要N_red≈100。能否给出N_c的解析估计？

2. **超导qubit vs 离子阱：** 离子阱的qubit连接是全局的（不需要SWAP），coherence时间更长（秒级别），可能更适合大N回流实验。但qubit数目前限于~50。

3. **模拟器先行：** 在经典模拟器上运行N≤30的精确态矢模拟，获取无噪声基线。用作IBM硬件误差分析的ground truth。

4. **关系到量子Darwinism冗余实验：** 现有的量子Darwinism实验（如Zurek组2020年在IBM Q上的环境冗余记录测量）可以用来独立标定$N_{\rm red}$（每个系统qubit的冗余记录数），将其与本实验的$P_{\rm reflux}$测量交叉比对。

5. **如果S1定理在所有N被实验违反：** 需要回到理论层面——是否存在CNOT以外的回流限制机制？或者DGF的组合论证是否在某一步有隐性假设（例如"环境qubit独立"这个在量子电路中通常成立但在真实物理环境中不成立的条件）？

---

## 附录A：Qiskit完整代码示例（配置C3: N_S=N_E=5, q_S=0.3, q_E=0.7）

```python
"""
S1 Theorem Experiment — Configuration C3
N_S = 5, N_E = 5, q_S = 0.3, q_E = 0.7
S1 bound: P_reflux ≤ 0.3/0.7 ≈ 0.43

IBM Eagle/Heron backend
"""
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Session
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# ─── Parameters ───
N_S, N_E = 5, 5
q_S_target, q_E_target = 0.3, 0.7
theta_S = 2 * np.arccos(np.sqrt(q_S_target))  # ≈ 1.982 rad
theta_E = 2 * np.arccos(np.sqrt(q_E_target))  # ≈ 1.159 rad
SHOTS = 32768

# ─── Qubit layout on ibm_torino (Heron 133-qubit, heavy-hex) ───
# Use physical qubits forming a linear path
# Example: qubits 0-9 on ibm_torino (verify coupling map!)
S_PHYSICAL = [0, 1, 2, 3, 4]    # system qubits
E_PHYSICAL = [5, 6, 7, 8, 9]    # environment qubits

# ─── Phase A: Calibration circuit ───
qr_S = QuantumRegister(N_S, 'S')
qr_E = QuantumRegister(N_E, 'E')
cr_S = ClassicalRegister(N_S, 'cS')
cr_E = ClassicalRegister(N_E, 'cE')

qc_calib = QuantumCircuit(qr_S, qr_E, cr_S, cr_E)
for i in range(N_S):
    qc_calib.ry(theta_S, qr_S[i])
for j in range(N_E):
    qc_calib.ry(theta_E, qr_E[j])
qc_calib.barrier()
qc_calib.measure(qr_S, cr_S)
qc_calib.measure(qr_E, cr_E)

# ─── Phase C: Full reflux circuit ───
# Forward: S_i → E_i (adjacent pairs)
# Reflux:  E_i → S_{(i+1) % N_S} (offset=1 to test cross-pair reflux)

qc_reflux = QuantumCircuit(qr_S, qr_E, cr_S, cr_E)
for i in range(N_S):
    qc_reflux.ry(theta_S, qr_S[i])
for j in range(N_E):
    qc_reflux.ry(theta_E, qr_E[j])

qc_reflux.barrier()

# Forward transfer
for i in range(min(N_S, N_E)):
    qc_reflux.cx(qr_S[i], qr_E[i])

qc_reflux.barrier()

# Reflux (offset=1 cross-pair)
for i in range(min(N_S, N_E)):
    target_s = (i + 1) % N_S
    qc_reflux.cx(qr_E[i], qr_S[target_s])

qc_reflux.barrier()
qc_reflux.measure(qr_S, cr_S)
qc_reflux.measure(qr_E, cr_E)

# ─── Submitting to IBM ───
service = QiskitRuntimeService(
    channel="ibm_quantum",
    token="YOUR_IBM_TOKEN"  # or use saved credentials
)
backend = service.backend("ibm_torino")

pm = generate_preset_pass_manager(
    optimization_level=3,
    backend=backend,
    initial_layout=S_PHYSICAL + E_PHYSICAL
)

qc_calib_transpiled = pm.run(qc_calib)
qc_reflux_transpiled = pm.run(qc_reflux)

with Session(service=service, backend=backend) as session:
    sampler = Sampler(session=session)

    # Phase A
    job_a = sampler.run([qc_calib_transpiled], shots=SHOTS)
    result_a = job_a.result()

    # Phase C
    job_c = sampler.run([qc_reflux_transpiled], shots=SHOTS)
    result_c = job_c.result()

print("Phase A counts:", result_a[0].data.meas)
print("Phase C counts:", result_c[0].data.meas)
```

---

## 附录B：误差传播完整公式

### B.1 q_S, q_E的统计误差

$$q_X = \frac{n_0}{N_{\rm shots} \cdot N_X}$$

其中 $n_0$ 是测量为 $|0\rangle$ 的总次数。二项误差：

$$\sigma_{q_X} = \sqrt{\frac{q_X(1-q_X)}{N_{\rm shots} \cdot N_X}}$$

### B.2 P_reflux的测量误差

$P_{\rm reflux} = N_{\rm back} / C_F$，其中 $C_F = N_E \cdot q_E$。

$N_{\rm back}$ 是二项随机变量（每shot中，最多$N_S$个系统qubit可能翻转，每个翻转概率取决于$q_S$和回流拓扑）：

$$\sigma_{N_{\rm back}} = \sqrt{N_{\rm back} \cdot \left(1 - \frac{N_{\rm back}}{N_{\rm shots}}\right)} \quad (\text{近似})$$

加上门误差和读出误差的系统贡献：

$$\sigma_{N_{\rm back}}^{\rm total} = \sqrt{\sigma_{N_{\rm back}}^2 + (N_{\rm shots} \cdot \epsilon_{\rm gate})^2 + (N_{\rm shots} \cdot \epsilon_{\rm readout})^2}$$

其中 $\epsilon_{\rm gate} \sim 0.01$ (CNOT门翻转概率), $\epsilon_{\rm readout} \sim 0.03$ (读出错误概率)。

$$\sigma_{P_{\rm reflux}} = \frac{1}{C_F}\sqrt{\sigma_{N_{\rm back}}^2 + \left(\frac{N_{\rm back}}{q_E}\right)^2 \sigma_{q_E}^2}$$

### B.3 比值 q_S/q_E 的误差

使用一阶Taylor展开（Delta方法）：

$$\sigma_{q_S/q_E}^2 = \frac{\sigma_{q_S}^2}{q_E^2} + \frac{q_S^2 \cdot \sigma_{q_E}^2}{q_E^4}$$

若q_S和q_E从不同qubit集合独立测量，协方差项为零。

### B.4 违反显著性

$$Z = \frac{P_{\rm reflux} - q_S/q_E}{\sqrt{\sigma_{P_{\rm reflux}}^2 + \sigma_{q_S/q_E}^2}}$$

$Z > 5$ → 5σ违反。

---

*实验设计完成。下一步：联系IBM Quantum Researcher Program申请计算时间；在Qiskit Aer上完成经典模拟验证；准备实验运行脚本。*
