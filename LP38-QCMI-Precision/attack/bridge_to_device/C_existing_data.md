# C: 数据侦察报告 -- 能否用别人的数据验证LP38？

**任务:** 数据侦察员 (Data Scout)
**日期:** 2026-06-09
**课题:** LP38 -- QCMI Precision / Bridge to Device
**问题:** 是否可以不用自己跑IBM Q实验，而是用别人已有的公开数据来验证LP38的QCMI预言？

---

## 总判：诚实回答

**不能直接使用别人的现有数据验证LP38的QCMI预言。但存在有限程度的数据复用和一些有前景的替代策略。**

核心原因：没有任何实验组在因果环拓扑上测量过QCMI（量子条件互信息）。已有的公开数据集中在不同物理量（门保真度、纠缠见证、Bell不等式违反、非马尔可夫性度量）和不同拓扑结构上。可复用的最多是：(a) 设备校准数据用于噪声建模，(b) 个别4-qubit态层析数据的二次分析，(c) 非马尔可夫性实验数据的概念重解释。但这些都不能替代专门的因果环QCMI实验。

**底线：最小需要的新数据是一组专门设计的、控制Cartan参数θ的4-qubit因果环QCMI测量。这个实验可以在<1天IBM Q机时内完成。**

---

## 搜索1: IBM Q公开校准数据

### 搜索策略
"IBM Q calibration data public API quantum gate fidelity dataset"

### 发现

IBM Q确实提供了丰富的公开校准数据API，但这些数据**不能直接用于验证QCMI**。

**可获取的数据：**

| 数据类型 | 获取方式 | 内容 |
|:--------|:--------|:----|
| T1, T2, 频率 | `backend.properties()` in qiskit-ibm-runtime | 每个qubit的弛豫和退相位时间 |
| 门错误率 | `properties.gate_error("cx", [i,j])` | 每个原生门的保真度 |
| 读出错误率 | `properties.readout_error(i)` | 单qubit读出差错率 |
| 历史校准数据 | `backend.properties(datetime="2023-04-15")` | 任意历史时间点的校准快照 |

**关键限制：**

1. 校准数据是**门级别**的指标（gate fidelity, T1, T2），而非**态级别**的信息论量（von Neumann熵，QCMI）。
2. QCMI = S(RQ') + S(Q'E') - S(Q') - S(RQ'E') 需要从演化后的多qubit密度矩阵计算。校准数据提供的是独立qubit和独立门的参数，不是多qubit联合的概率分布。
3. 即使知道每个门的去极化噪声参数，也无法精确重建因果环演化后的多qubit量子关联——因为coherent error和crosstalk是设备状态依赖的，不能从单门校准数据外推。

**校准数据的有限用途：**

校准数据可以用于**噪声建模**——即模拟"在这个噪声水平下，QCMI的预期是什么"。具体地：
- 从校准数据建立去极化噪声模型：每个RZZ(θ)门附加保真度$F_g = 1 - \epsilon_g$
- 估计假QCMI（去极化噪声产生的表观信息）：$\Delta I_{\text{depol}} \approx N_g \cdot \epsilon_g \cdot \log_2(d)$
- 这个值可以作为QCMI实验的**噪声地板**（noise floor）估计

但这不能替代实际实验，因为忽略了：(a) 相干错误的结构，(b) qubit间的串扰，(c) 读出串扰，(d) 时间依赖的噪声。

**结论：IBM Q校准数据可以用于噪声建模和实验设计优化，但不能用于直接验证QCMI。评级：部分有用但不足。**

---

## 搜索2: 已发表的量子过程层析(QPT)数据

### 搜索策略
"quantum process tomography 4-qubit IBM experimental data published"

### 发现

存在多篇已发表的4-qubit QPT/态层析实验，但**数据针对不同问题，且原始数据极少公开**。

**最相关文献：**

| 论文 | 内容 | 数据可用性 | 与LP38的关系 |
|:-----|:----|:---------|:-----------|
| **Dinca, Luitz & Debertolis (2025)** arXiv:2509.25342 | 4-qubit QPT on IBM超导处理器，Trotter vs compressed time evolution | 论文含过程矩阵图，原始数据未公开 | **最接近**：4-qubit QPT数据含噪声通道的完整χ矩阵 |
| **Tomis et al. (2024)** arXiv:2410.20241, *Adv. Quantum Tech.* | 4-qubit Dicke态Bell不等式违反，ibm_kyiv/ibm_sherbrooke | 论文含Pauli期望值，原始数据未知 | 4-qubit tomographic测量数据可用 |
| **Vedrukov et al. (2024)** *Lobachevskii J. Math.* 45, 119 | 云平台QPT (ibmq_belem + OriginQ)，含非马尔可夫性估计 | 需付费获取 | 2-qubit QPT + 非马尔可夫性 |
| **Wigner过程层析 (2024)** *Quantum Inf. Process.* | 扫描基Wigner函数层析，IBM Q实验结果 | 未知 | 过程层析数据可用 |
| **Gaikwad PhD thesis (2024)** arXiv:2401.09941 | QST+QPT on NMR和IBM云处理器，含压缩感知协议 | 学位论文，附件有待查找 | 含实际实验数据 |

**为什么这些数据不能直接用于LP38验证：**

1. **拓扑不匹配**：Dinca等人的QPT是针对Trotter时间演化电路的，不是因果环拓扑（四条边形成闭合环）。QCMI对整体拓扑极其敏感——不同拓扑结构上的相同门操作产生不同的QCMI。

2. **参数不可控**：已有的QPT数据测量的是特定电路上的过程矩阵，Cartan参数(c_x, c_y, c_z)是固定的而非连续可调的。LP38需要扫描θ（控制RZZ角度）来验证标度律。

3. **数据粒度不够**：QCMI需要演化后的4-qubit联合密度矩阵。即使有过程χ矩阵，也需要初始态的信息来计算最终的$\rho_{RQ'E'}$。大多数论文只报告过程保真度或局部不变量，而非完整的过程矩阵。

4. **原始数据极少公开**：尽管论文报告了结果，原始的电路计数数据（shot-level data）几乎从不公开。没有原始计数数据，无法重建带有统计误差的密度矩阵和熵的不确定性。

**部分可用的数据资源：**

- **Tomis et al. (2024)** 的4-qubit Dicke态数据：如果其补充材料包含完整的Pauli期望值（3^4=81个测量基的期望值），则可以从这些数据重建4-qubit密度矩阵，并计算互信息（非条件互信息）。但因果环拓扑和受控θ扫描仍缺失。
- **Dinca et al. (2025)** 的过程χ矩阵：如果作者愿意提供原始数据，可以从中提取Cartan参数并验证噪声通道的结构。

**结论：最接近的数据集（Dinca 2025 4-qubit QPT）有潜力但当前不可用。需要联系作者获取原始数据，且即使获得数据，也缺少θ扫描能力。评级：有潜力但需合作。**

---

## 搜索3: 量子基准测试中的QCMI相关信息

### 搜索策略
"quantum benchmarking mutual information NISQ experimental data open dataset"

### 发现

量子基准测试社区产生了大量公开数据，但**都集中在不同物理量上，QCMI未被包含在内**。

**已有公开数据集：**

| 数据集 | 来源 | 规模 | 内容 |
|:------|:----|:----|:----|
| **NISQ Error Measurement Dataset** | Patel et al. SC20, Northeastern Univ. | 开源 | IBM Q设备错误测量和表征 |
| **Quantum Volume Benchmarks** | IEEE DataPort | 24 NISQ设备 (IBM Q, IonQ, Rigetti, OQC, Quantinuum) | QV基准测试结果 |
| **QASMBench** | OSTI.gov | 开源 | 低层OpenQASM基准测试套件 |
| **量子互信息因果中介分析** | Kesiku (2026) arXiv:2603.16321 | 论文含数值数据 | 量子互信息在QML中的因果中介效应 |

**为什么不能用于LP38：**

1. **量子互信息 vs 量子条件互信息**：Kesiku (2026)的工作使用了量子互信息 I(A:B)，而非条件互信息 I(A:B|C)。两者在信息论上有本质区别——条件互信息涉及三方系统，且对因果结构敏感。

2. **基准数据集是摘要统计量**：QV数据给出的是单个数字（量子体积），不能重建态层析或过程层析。

3. **随机基准测试(RB)不能提供QCMI**：RB测量平均门保真度，这是一个标量。QCMI是态的函数，取决于具体电路结构和初始态。

**部分有用的资源：**

- Kesiku (2026)的因果中介分析框架提供了QCMI在QML语境下的第一个数值基准。虽然拓扑结构不同（变分电路而非因果环），但方法论（如何从电路输出计算QCMI）可以直接借鉴。

**结论：现有量子基准测试数据不包含QCMI。评级：不可用。**

---

## 搜索4: 量子非马尔可夫性实验数据

### 搜索策略
"quantum non-Markovianity experimental measurement superconducting qubit data"

### 发现

这是最丰富的实验数据方向——多个实验组在超导qubit上测量了非马尔可夫性。但这些测量使用不同的度量（BLP, RHP, 纠缠回复等），而非QCMI。

**关键实验：**

| 实验 | 平台 | 度量 | 数据可用性 |
|:-----|:----|:----|:---------|
| **Gaikwad et al. (2024)** PRL 132, 200401 | 超导qubit对 | 纠缠回复（非马尔可夫性签名） | 论文含数据图，原始数据未公开 |
| **Han et al. (2024)** Appl. Phys. Lett. 125, 124003 | 超导qubit+lossy resonator | 最大可提取qubit-reservoir纠缠 | 论文含实验数据 |
| **Mazhorina et al. (2025)** arXiv:2503.23431 | 超导transmon + 离子阱 | 改进的非马尔可夫性度量 | 论文含两种平台的比较数据 |
| **Li et al. (2023)** npj QI 9, 111 | 超导transmon单qubit | GST长序列中的非马尔可夫行为 | GST过程矩阵在补充材料中 |
| **Gao et al. (2026)** arXiv:2605.23385 | 超导双qubit + TLS | QPT揭示TLS诱导的非马尔可夫相关 | 最新预印本 |
| **Agarwal et al. (2024)** QST 9, 035017 | 超导qubit (driven) | qubit-TLS模型捕捉非马尔可夫噪声 | 含实验表征数据 |

**概念上的重解释可能性：**

非马尔可夫性度量和QCMI之间存在概念联系：
- 非马尔可夫动力学的特征是从环境回流到系统的信息
- QCMI衡量的是在给定环境状态条件下，系统不同部分之间的条件互信息
- 两者都涉及"信息通过环境传递"这一核心概念

但由于以下原因，不能直接转换：

1. **不同的数学定义**：BLP度量 = $\int_{dD/dt>0} \frac{d}{dt}D(\rho_1,\rho_2) dt$，而QCMI = S(RQ')+S(Q'E')-S(Q')-S(RQ'E')。两者没有直接的函数关系。

2. **不同的系统划分**：非马尔可夫性实验通常是1个系统qubit + 1个环境qubit。LP38需要的是R-Q-E'三方划分（R和Q是Bell对的两个qubit，环境是两个E qubit）。

3. **缺少θ扫描**：非马尔可夫性实验使用固定的门操作，不涉及Cartan参数连续调节。

**最有潜力的数据复用：**

- **Li et al. (2023)** 的GST过程矩阵（arXiv 2302.08690补充材料）：这些1-qubit GST数据包含完整的噪声过程矩阵，可用于验证"噪声Choi矩阵的Cartan分解"这一核心理论预测。特别是论文报告的非马尔可夫GST长序列行为可以直接与QCMI的理论结构相比较。但1-qubit数据不支持4-qubit因果环拓扑。

- **Gao et al. (2026)** 的TLS诱导双qubit相关QPT数据：这是最接近LP38精神的数据——TLS作为"隐藏的环境自由度"同时耦合两个qubit，产生非马尔可夫相关性。可以检验$\eta_0 \propto \sum|c|^4$（Cartan系数平方的平方和）作为噪声相关性强度的度量。

**结论：非马尔可夫性实验数据在概念层面与LP38精神一致，但不能直接转换为QCMI测量。部分数据（GST过程矩阵）可用于验证框架的子组件。评级：概念上有用但不可直接验证。**

---

## 搜索5: 门集层析(GST)公开数据

### 搜索策略
"gate set tomography open data superconducting qubit"

### 发现

pyGSTi完全开源且文档丰富，但**超导qubit的GST公开数据集非常稀少**。

**可用资源：**

| 资源 | 平台 | 内容 | 许可证 |
|:----|:----|:----|:-----|
| **NV中心金刚石GST数据** | 4TU.ResearchData (DOI: 10.4121/...) | 完整GST报告，过程矩阵，Jupyter notebooks | CC BY 4.0 |
| **CCZS-gate仓库** | github.com/warrench/CCZS-gate | 超导transmon双qubit GST数据 | 开源 |
| **pyGSTi教程和示例数据集** | github.com/pyGSTio/pyGSTi | 教程数据（模拟） | Apache 2.0 |
| **Li et al. (2023)补充材料** | arXiv 2302.08690 | 1-qubit GST过程矩阵（取{√X, √Y}门集） | 论文公开 |
| **QSCOUT Sandia数据** | Sandia QSCOUT 平台 | 离子阱GST数据（非超导） | 部分公开 |

**关键限制：**

1. **维度限制**：所有可用GST数据是1-qubit或2-qubit的。4-qubit GST需要的电路序列数随qubit数指数增长——对于4 qubit，标准GST需要>10^4个电路。这是实验上可能的但数据密集的，且没有公开数据集。

2. **平台差异**：金刚石NV中心的GST数据（最完整的公开GST）与超导transmon的噪声结构有本质区别（NV中心的主要噪声源是核自旋浴，transmon是TLS和1/f噪声）。

3. **门集不对应**：GST数据测量的是特定门集（如{I, X_π/2, Y_π/2, CNOT}）的过程矩阵。LP38需要的RZZ(θ)分数门（可变角度，连续参数）不在标准GST门集中。

**潜在用途：**

- Li et al. (2023) 的GST数据可用于验证"噪声过程矩阵的Cartan分解"这一理论子组件
- CCZS-gate数据的2-qubit GST可用于验证"2-qubit门的环境Gram矩阵满秩"条件

**结论：最完整的公开GST数据（NV中心金刚石）在错误平台上。超导qubit的1-2 qubit GST数据存在但不足以验证4-qubit因果环QCMI。评级：部分可用但不充分。**

---

## 搜索6: 量子云平台的开放数据

### 搜索策略
"quantum computing cloud open dataset IBM Q Experience public results 4-qubit entanglement"

### 发现

IBM Q Experience和其他量子云平台产生了大量实验，但**原始数据极少以可复用的格式公开**。

**已知的4-qubit IBM Q实验数据：**

| 数据来源 | 设备 | 态 | 数据格式 |
|:--------|:----|:---|:-------|
| **PRResearch (2023)** Vol. 5, 013226 | IBM Q (ibmq_singapore等) | 4-qubit Smolin态, 8-qubit W态 | 论文含重建的密度矩阵 |
| **Qiskit教程** | ibmqx2等 | 2-qubit Bell态 | Jupyter notebook, fidelities |
| **Ozaeta & McMahon (2019)** | ibmqx5 | 1-8 qubit GHZ态 | 论文含保真度衰减数据 |
| **Pereira et al. (2023)** | IBM Q 7-qubit | QND测量Choi矩阵 | 论文含过程矩阵 |

**为什么不能用于LP38：**

1. **态而非过程**：大多数数据是特定态的层析（Smolin态、GHZ态、W态），而非因果环演化后的态。QCMI在Smolin态上的值与在因果环演化态上的值完全不同。

2. **缺少θ参数扫描**：所有数据是固定θ的单点测量，不能用于提取标度指数α。

3. **拓扑结构不同**：Smolin态和GHZ态没有因果环拓扑结构。它们的状态是在星型或线型电路（而非环型）中制备的。

**部分有用的数据：**

PRResearch Smolin态4-qubit数据：如果补充材料包含完整的态层析数据（16×16密度矩阵或81个Pauli期望值），可以从中计算互信息（非条件）。虽然不能直接验证因果环QCMI，但可以验证QCMI从态层析重建的端到端pipeline。

**结论：开放数据集提供了一些4-qubit态层析数据，但不在因果环拓扑中，且缺少θ扫描。评级：不可用于直接验证，但可用于验证测量pipeline。**

---

## 综合评估矩阵

### 能用于验证LP38吗？

| 数据类型 | 替代θ扫描QCMI? | 验证子组件? | 验证噪声模型? | 验证pipeline? |
|:--------|:---:|:---:|:---:|:---:|
| IBM Q校准数据 | **否** | 否 | **是** (noise floor) | 否 |
| 4-qubit QPT (Dinca 2025) | **否** | 部分 (过程噪声结构) | 是 | 是 |
| 量子基准测试集 (QV, RB) | **否** | 否 | 否 | 否 |
| QMI因果分析 (Kesiku 2026) | **否** (QMI非QCMI) | 是 (方法论) | 否 | 否 |
| 非马尔可夫性实验 (Gaikwad 2024等) | **否** | 是 (概念层面) | 是 | 部分 |
| GST数据 (Li 2023, CCZS) | **否** | **是** (噪声Cartan分解) | 是 | 是 |
| 4-qubit态层析 (PRResearch) | **否** | 否 | 否 | **是** (pipeline) |

### 诚实打分卡

| 验证目标 | 可用现有数据？ | 置信度 | 替代方案 |
|:--------|:---:|:---:|:----|
| QCMI > 0 (CFOL定性) | **否** | N/A | 需要实验 |
| QCMI ∝ θ² (vs θ⁴) | **否** | N/A | 需要多θ实验 |
| α_eff标度律 | **否** | N/A | 需要精细θ扫描 |
| 噪声Cartan分解 | **部分** (Li 2023 GST数据) | 低 (仅1-qubit) | 可补充为框架验证 |
| 环境Gram矩阵满秩 | **部分** (CCZS 2Q GST) | 中 (仅2-qubit) | 可验证2Q子组件 |
| 实验可行性 (噪声floor) | **是** (IBM Q校准) | **高** | 直接可用 |
| 测量pipeline | **是** (PRResearch 4Q数据) | 中 | 可验证数据流 |
| 对齐vs失配轴差异 | **否** | N/A | 需要实验 |

---

## 最小需要的新数据

### 如果必须跑实验，最少需要什么？

**最小可行实验 (MVP):**

| 项目 | 规格 | 估计时间 |
|:----|:----|:------|
| 设备 | IBM Heron或Nighthawk (156+ qubit, sq lattice/hex) | — |
| 物理qubit | 6-8 (4核+2-4 ancilla/SWAP路由) | — |
| θ值扫描 | 3个θ值: π/4, π/8, π/16 | — |
| 测量设置 | X基联合测量 (1个Pauli设置) | — |
| Shots | 10^5 per θ值 | — |
| 校准 | 标准Qiskit Runtime Primitives校准 | ~30 min |
| 纯运行时间 | 3 θ × 10^5 shots × 10 μs | ~3 sec |
| 总QPU机时 | 含队列、校准、重校准 | **< 1天** |
| 数据分析 | 16-bin X基概率 → von Neumann熵 → QCMI → α拟合 | ~1天 |

**这个实验可以回答：**

1. QCMI > noise floor? (大θ点: π/4, QCMI ~ 1.2 bits vs noise floor ~ 0.06 bits → S/N ~ 20)
2. QCMI标度是O(θ²)还是O(θ⁴)? (3点足够区分幂律指数差异>2)
3. α_eff ≈ 2? (3点拟合足够排除α→4.0，得到α=1.5±0.5的数量级估计)

**需要的资源：**

- IBM Q Open Plan或Premium Plan访问 ($0-$100k/year)
- 或学术合作 (IBM Q Network学术成员)
- 1名研究生或博后花1-2周时间（编码+运行+分析）

### 更理想但非必需的扩展

| 扩展 | 额外时间 | 产出 |
|:----|:-----|:----|
| 5-7个θ值 | +1天 | α拟合精度+50% |
| 对齐vs失配轴对比 | +1天 | 验证轴对齐 <= 轴失配预言 |
| 不同设备对比 (Heron vs Eagle) | +1天 | 设备独立性检验 |
| b_1=2 (双环) | +1-2天 | 环计数标度验证 |
| Classical shadow + error mitigation | +2-3天 | 保真度提升 |

---

## 替代策略：不需要自己跑实验的方案

### 方案A: 噪声模拟 + 校准数据 (零实验方案)

**可行性：中等**

使用IBM Q公开校准数据构建参数化噪声模型，用经典计算机模拟：

1. 从`backend.properties()`获取每个qubit的T1, T2, gate error
2. 构建去极化+T1+T2噪声通道的参数化模型
3. 经典模拟4-qubit因果环在噪声模型下的演化
4. 计算噪声下的QCMI及其与理想理论的偏差

**优点：** 零QPU机时，可任意扫描θ值
**缺点：** 忽略coherent error和crosstalk，结论对审稿人说服力不足

**评级：可作为理论论文的补充，但不能替代真实实验。**

### 方案B: 联系作者获取原始数据

**可行性：中等偏低（取决于作者合作意愿）**

最有希望的目标：

1. **Dinca, Luitz & Debertolis (2025)**: 联系获取4-qubit QPT原始数据
2. **Tomis et al. (2024)**: 联系获取4-qubit Dicke态Pauli期望值
3. **Gaikwad et al. (2024)**: 联系获取非马尔可夫性实验的密度矩阵重建数据

**优点：** 利用已有的高质量数据，无需QPU机时
**缺点：** 数据可能不可获得，且不是为因果环拓扑设计的

**评级：值得尝试，但不应依赖。**

### 方案C: 公开数据集元分析

**可行性：低**

收集所有公开的4-qubit态层析数据，提取互信息（非条件），并用因果环理论重新解释这些数据中的信息结构。

**问题：**
- 不同的态在不同的设备上以不同的θ制备 — 不可比较
- 没有θ扫描数据，无法提取标度指数
- 很少数据包含完整的态层析重建（通常只有保真度数字）

**评级：不建议。**

---

## 最终建议

### 对LP38论文的策略建议

**短期（当前论文）：**
1. 在Discussion中诚实声明："没有现有的公开数据集可以直接验证我们的预言。"
2. 利用IBM Q校准数据进行噪声建模（方案A），证明预期的信噪比在可行范围内。
3. 提供具体的实验协议（此目录中A_ibm_mapping.md已经提供），供实验组直接使用。
4. 将实验验证定位为"proposed experimental test"，给出明确的成功标准。

**中期（6-12个月）：**
1. 寻找量子硬件实验合作者（IBM Q Network或其他）
2. 跑最小可行实验（3个θ值，~1天QPU机时）
3. 收集首批因果环QCMI数据

**在论文中可以写的声明：**

> "所有所需组件（4-qubit QCMI电路，RZZ(θ)分数门，X基联合测量）在当前Heron/Nighthawk级设备的能力范围内。单次实验（含10^5 shots和3个θ值扫描）预计需要<1天QPU机时。"
>
> "现有的公开数据集（校准数据、过程层析、非马尔可夫性实验）提供了噪声建模和实验可行性评估的有用基准，但不能直接替代因果环QCMI的测量。"

### 事实总结

| 问题 | 答案 |
|:-----|:----|
| 可以用别人的数据吗？ | **不能直接验证**，但部分数据可用于噪声建模 |
| 最接近的数据集？ | Dinca et al. (2025) 4-qubit QPT (拓扑不匹配+数据未公开) |
| 可验证的子组件？ | 噪声Cartan分解 (Li 2023 GST), 环境Gram满秩 (CCZS 2Q) |
| 最小需要什么新数据？ | 3个θ值的4-qubit因果环X基测量, <1天QPU机时 |
| 最现实的路径？ | 噪声建模(现在) + 寻找实验合作者(6月内) + 跑最小实验(12月内) |

---

*数据侦察完成。结论：诚实的"不能"。但缺口很小——<1天QPU机时的专门实验即可填补。建议现在用校准数据做噪声建模作为论文支撑，同时启动实验合作。*

---

## 附录: 关键数据源详细信息

### A. IBM Q校准数据API (部分有用)

```python
# 获取历史校准数据
from qiskit_ibm_runtime import QiskitRuntimeService
service = QiskitRuntimeService()
backend = service.backend("ibm_torino")
properties = backend.properties(datetime="2024-06-01")

# 提取每个qubit的T1, T2
for i in range(backend.num_qubits):
    t1 = properties.t1(i)
    t2 = properties.t2(i)
    freq = properties.frequency(i)
    readout_err = properties.readout_error(i)

# 提取双qubit门错误
for gate in properties.gates:
    if gate.gate == "cz":
        qubits = gate.qubits
        error = properties.gate_error("cz", qubits)
```

### B. Li et al. (2023) GST过程矩阵 (单qubit验证用)

- arXiv: 2302.08690
- 内容: 单qubit门集 {I, X_π/2, Y_π/2} 的GST过程矩阵
- 用途: 验证噪声过程矩阵的Cartan分解框架
- 获取: arXiv PDF补充材料

### C. CCZS-gate 2-qubit GST (双qubit验证用)

- 仓库: github.com/warrench/CCZS-gate
- 平台: 超导transmon
- 内容: 双qubit CCZS门的GST数据
- 用途: 验证2-qubit噪声通道的Gram矩阵满秩条件

### D. Dinca et al. (2025) 4-qubit QPT (最有希望但需合作)

- arXiv: 2509.25342
- 内容: IBM超导处理器上4-qubit Trotter vs compressed时间演化QPT
- 用途: 如果获得原始数据，可提取过程χ矩阵并验证噪声Cartan结构
- 获取: 需联系作者 (Maria Dinca, David Luitz, Maxime Debertolis)

### E. PRResearch (2023) 4-qubit Smolin态层析

- DOI: 10.1103/PhysRevResearch.5.013226
- 内容: IBM Q上Smolin态4-qubit态层析，163,840 shots
- 用途: 验证测量pipeline，计算互信息（非条件）
- 获取: Physical Review Research (开源期刊)
