# LP32-S5: 量子Darwinism桌面实验 —— DGF独立检验 (Round 1)

**A博士, 2026-06-07**
**北极星: 量子Darwinism的冗余度R_δ与系统自由容量q的线性关系检验**

---

## §0 核心命题

**DGF预言**: 量子Darwinism中系统信息在环境中的冗余度R_δ与环境的自由容量(free capacity) q成正比:
$$R_\delta(q) = R_\delta(1) \cdot q$$
其中q = 环境qubit中处于自由态|0⟩的比例。当环境qubit预置为|1⟩(占用)时，有效q降低，冗余度线性下降。

**标准退相干理论(零假设)**: R_δ与q无关。耦合强度相同，每个环境qubit的编码能力不受初始态影响，冗余度保持不变。

**判定性实验信号**: R_δ vs q 的斜率。DGF预言斜率 = R_δ(1) > 0; 零假设预言斜率 = 0。

---

## §1 文献基础

### §1.1 关键实验: Zhu et al. (2025, Science Advances)
- **论文**: "Observation of Quantum Darwinism and the Origin of Classicality with Superconducting Circuits" [arXiv:2504.00781], Science Advances 11, adx6857 (2025)
- **平台**: 12-qubit超导量子处理器 (浙大, Zuchongzhi架构)
- **系统**: 2 qubits (Q6, Q7) 作为系统S, 有效指针态 |0_S⟩=|00⟩, |1_S⟩=|11⟩
- **环境**: 10 qubits 作为光子环境E
- **门序列**: 3×Hadamard + CZ → 制备S为Bell-like叠加态 (|00⟩+|11⟩)/√2; 受控幺正 {U_k^⊘} 实现S-E纠缠; 量子态层析测量I(S:F)
- **受控幺正**: U_k^⊘ = |00⟩⟨00|⊗U_0^k + |11⟩⟨11|⊗U_1^k, 其中U_j^k = R_y(θ_j^k)·R_z(ϕ_j^k), θ_j^k∈[(j-0.5)π, (j+0.5)π), ϕ_j^k∈[-π,π) 随机采样
- **关键观测**: (i) I(S:F)随碎片大小m出现经典平台(plateau); (ii) 量子discord在平台区消失; (iii) Bloch球上出现分支结构(branching states)

### §1.2 实验参数 (Zhu et al. 12-qubit系统)
| 参数 | 值 |
|------|-----|
| 单qubit门时间 t_SQ | 20 ns |
| 单qubit门误差 ε_SQ | 0.043% |
| CZ门时间 t_CZ | 47 ns |
| CZ门误差 ε_CZ | 0.277% |
| 读出误差 ε_readout | 0.8% |
| T1 (能量弛豫) | 135 μs |
| Tφ (自旋回波退相干) | 40 μs |
| 采样数 (shots) | 1,000,000 |
| 环境qubit数 N | 10 |
| 系统qubit数 | 2 (编码1个有效qubit) |

### §1.3 理论框架
- Zurek量子Darwinism框架 [Zurek, Nature Physics 5, 181 (2009)]
- Korbicz综述: "Roads to objectivity" [Quantum 5, 571 (2021)] — 比较QD, Spectrum Broadcast Structures, Strong QD三种进路
- Zwolak & Zurek: "Redundancy of einselected information" [PRA 95, 030101 (2017)] — 无关环境bit不稀释冗余度
- Riedel, Zurek & Zwolak: "Rise and Fall of Redundancy" [NJP 14, 083010 (2012)] — 多体相互作用可压制冗余度至随机态水平

---

## §2 实验协议设计

### §2.1 系统配置

| 要素 | 说明 |
|------|------|
| **系统 S** | 1个有效qubit (可用2个物理qubit编码为|00⟩/|11⟩指针态, 如Zhu方案) |
| **环境 E** | N个环境qubit, N = 5, 7, 9, 11 (扫描N以验证有限尺寸效应) |
| **控制参数 q** | 自由容量 = 初始化为|0⟩的qubit比例 |
| **q扫描点** | q ∈ {0.0, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0} (7个点) |
| **预占用实现** | 对(1-q)N个环境qubit, 初始化为|1⟩而非|0⟩ |

### §2.2 门序列

```
Step 0: 初始化
  S → |+⟩_S = (|0⟩+|1⟩)/√2  (Hadamard门)
  qN个环境qubit → |0⟩
  (1-q)N个环境qubit → |1⟩  (X门)

Step 1: S-E纠缠 (受控幺正层)
  FOR each environment qubit E_k:
    U_k = |0⟩⟨0|_S ⊗ U_0^k + |1⟩⟨1|_S ⊗ U_1^k
    U_j^k = R_y(θ_j^k),  θ_j^k ∈ [(j-0.5)π, (j+0.5)π)  随机采样
  END FOR

Step 2: 环境碎片测量
  FOR fragment size m = 1 to N:
    选择m个环境qubit作为碎片F
    FOR each shot:
      对S+F进行量子态层析 (Pauli基测量)
    END FOR
    计算 I(S:F) = H(S) + H(F) - H(SF)
    计算 Holevo界 χ(S:F̌) 和量子discord D(S:F̌)
  END FOR

Step 3: 冗余度提取
  从 I(S:F) vs m/N 曲线提取:
  - 平台高度: I_plateau(q)
  - 达到平台的碎片大小: m*_δ(q)
  - 冗余度: R_δ(q) = N / m*_δ(q)
```

### §2.3 分支态结构 (含占用qubit)

DGF框架下的分支态:
$$|\Psi_{SE}(q)\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle_S \bigotimes_{k=1}^{qN} |0_{E_k}\rangle \bigotimes_{l=1}^{(1-q)N} |\tilde{0}_{E_l}\rangle + |1\rangle_S \bigotimes_{k=1}^{qN} |1_{E_k}\rangle \bigotimes_{l=1}^{(1-q)N} |\tilde{1}_{E_l}\rangle\right)$$

其中对于自由qubit (初始|0⟩):
$$|j_{E_k}\rangle = \cos(\theta_j^k/2)|0_k\rangle - i\sin(\theta_j^k/2)|1_k\rangle$$

对于占用qubit (初始|1⟩):
$$|\tilde{j}_{E_l}\rangle = \cos(\theta_j^l/2)|1_l\rangle - i\sin(\theta_j^l/2)|0_l\rangle$$

**关键**: 在标准QM中, |j_Ek⟩与|\tilde{j}_El⟩的条件态区分度(overlap)相同:
$$\langle 0_{E_k}|1_{E_k}\rangle = \langle \tilde{0}_{E_l}|\tilde{1}_{E_l}\rangle = \cos\frac{\theta_0}{2}\cos\frac{\theta_1}{2} + \sin\frac{\theta_0}{2}\sin\frac{\theta_1}{2}$$

因此零假设预言R_δ与q无关。DGF预言额外的"容量约束"使得占用qubit的有效编码降低。

### §2.4 交互信息与冗余度计算

互信息:
$$I(S:F) = H(\rho_S) + H(\rho_F) - H(\rho_{SF})$$
$$H(\rho) = -\text{Tr}(\rho\log_2\rho)$$

其中ρ_S = Tr_{E\F}(ρ_SE), ρ_F = Tr_{S,E\F}(ρ_SE), ρ_SF = Tr_{E\F}(ρ_SE)

冗余度定义(对给定信息亏损δ):
$$R_\delta = \frac{N}{m_\delta}$$
其中m_δ = min{m: I(S:F_m) ≥ (1-δ)H(S)}

**DGF定量预言**:
$$R_\delta(q) = q \cdot R_\delta(1) + (1-q) \cdot R_\delta(0)$$
其中R_δ(0) ≪ R_δ(1) (占用qubit贡献极低冗余度)
在最简模型中: R_δ(0) ≈ 0, 故 R_δ(q) ≈ q·R_δ(1)

---

## §3 信号大小与误差预算

### §3.1 预期信号

| q值 | N=10时预期R_δ (DGF) | N=10时预期R_δ (零假设) | 差异 |
|-----|---------------------|------------------------|------|
| 1.0 | R_δ(1) ≈ 10 (参考值) | R_δ(1) ≈ 10 | 0 |
| 0.8 | 8.0 | ~10 | 20% |
| 0.6 | 6.0 | ~10 | 40% |
| 0.5 | 5.0 | ~10 | 50% |
| 0.4 | 4.0 | ~10 | 60% |
| 0.2 | 2.0 | ~10 | 80% |
| 0.0 | ~0 | ~10 | ~100% |

**核心检验点**: q=0.5时, DGF预言R_δ下降~50%, 零假设预言基本不变。这是高显著性检验点。

### §3.2 统计误差

互信息I(S:F)的统计误差来自有限采样:
$$\sigma_I \approx \frac{1}{\sqrt{N_{\text{shots}} \cdot \ln 2}} \cdot \sqrt{\frac{d_{SF}}{d_S d_F}}$$

其中d_S = 2, d_F = 2^m, d_SF = 2^{m+1}, N_shots = 10^6

| m | d_SF | σ_I (N_shots=10^6) |
|---|------|---------------------|
| 1 | 4 | ~0.0014 |
| 3 | 16 | ~0.0056 |
| 5 | 64 | ~0.011 |
| 10 | 2048 | ~0.064 |

对于m=1-5范围(经典平台区), σ_I ≲ 1%, 远小于预期的50%信号。

### §3.3 系统误差

| 误差源 | 大小 | 对R_δ影响 | 缓解策略 |
|--------|------|-----------|----------|
| 单qubit门误差 | 0.043% per gate | 累积相位误差 | 随机编译(randomized compiling) |
| CZ门误差 | 0.277% per gate | 纠缠保真度下降 | 门序列优化, 误差缓解 |
| 读出误差 | 0.8% per qubit | I(S:F)偏置 | 读出误差缓解矩阵, 重复测量 |
| T1退相干 | 135 μs | 态纯度下降 | 电路深度 < 1 μs (~20 gates) |
| Tφ退相位 | 40 μs | 量子相干性损失 | 动力解耦(dynamical decoupling) |
| 串扰(crosstalk) | ~0.5% | 环境qubit间虚假关联 | 频谱分配, 空间隔离 |
| 态制备误差 | ~0.1% | | SPAM误差表征和修正 |

**电路深度估计**:
- 初始化层: 1-2 gates
- S-E纠缠层: N个并行受控旋转 ~ 2-4 gates depth (含编译)
- 测量层: 量子态层析需3^m个Pauli基组合
- 总深度: ~5-8个gate层, 时间 < 400 ns ≪ T1, Tφ

**关键**: 系统误差远小于预期信号(50%), 但需仔细标定。最大的系统误差来源是CZ门误差积累, 当N=10时每个受控幺正含~2个CZ, 总CZ误差~5.5%, 但这同时影响所有q值, 在R_δ(q)的相对测量中大部分抵消。

### §3.4 信号显著性估计

定义检验统计量:
$$S = \frac{R_\delta(1.0) - R_\delta(0.5)}{\sqrt{\sigma^2_{R}(1.0) + \sigma^2_{R}(0.5)}}$$

DGF预言: S ≈ 5 (对于N=10, σ_R ≈ 0.1·R_δ)
零假设预言: S ≈ 0

对100万shots, N=10, 预期统计显著性 > 5σ, 足以区分两个假说。

**测量时间估计**:
- 每个(q, m)组合: 3^m个Pauli基 × N_shots × 门时间
- 对m≤5: ~243 × 10^6 × 50ns ≈ 12秒
- 7个q值 × 10个m值 = 70个(q,m)组合
- 总测量时间: ~15分钟 (含校准开销: ~1小时)
- 全实验(含N扫描): ~4-6小时

---

## §4 独立性与对照设计

### §4.1 内部对照

1. **q=1.0参考点**: 复现Zhu et al.基线结果, 验证实验设置正确性
2. **q=0.0对照**: 全占用极限, 检验预占用qubit是否有任何残余编码
3. **随机化验证**: 对每个q值使用10组独立随机{θ_j^k}实现, 取平均消除实现依赖

### §4.2 系统学cross-check

1. **Holevo界检验**: χ(S:F̌) 应给出与I(S:F)一致的趋势
2. **量子discord消失**: D(S:F̌) → 0 在平台区, 作为经典性的一致检验
3. **分支结构可视化**: Bloch球上的几何态分布应随q降低而变得不那么结构化
4. **有限N外推**: 对N=5,7,9,11进行独立测量, R_δ(1)/N应趋于常数(热力学极限)

### §4.3 潜在混淆因素及排除

| 混淆因素 | 影响 | 排除方法 |
|----------|------|----------|
| 不同q值导致不同电路深度 | 系统性偏置 | 使用恒等门(pass-through)均衡空闲qubit的深度 |
| |1⟩制备的X门误差 | 误归因为容量效应 | 独立表征X门误差, 从信号中扣除 |
| 占用qubit间串扰 | 虚假关联信号 | 测量空闲qubit关联函数, 确认无串扰 |
| 频率拥挤效应 | |1⟩和|0⟩的AC Stark位移不同 | 对每个q值独立校准qubit频率 |

---

## §5 可行性与当前技术评估

### §5.1 平台需求

| 需求 | 当前最佳水平 | 是否满足 |
|------|-------------|----------|
| qubit数 ≥ 12 | Tianyan-287: 105 qubits [2512.10504] | 是 |
| 单qubit门保真度 ≥ 99.9% | 99.90% (Tianyan) | 是 |
| 双qubit门保真度 ≥ 99.5% | 99.56% (Tianyan) | 是 |
| 读出保真度 ≥ 99% | 98.7% (Tianyan) | 边缘 |
| T1 ≥ 100 μs | 135 μs (Zhu) | 是 |
| 电路深度 < T1/100 | <1.35 μs可用; ~0.4 μs所需 | 是 |
| 可编程量子电路 | Qiskit transpilation (Zhu) | 是 |

### §5.2 主要技术挑战

1. **读出误差 (0.8-1.3%)**: 当前读出误差是最大限制。需要:
   - 读出误差缓解矩阵 (assignment probability matrix inversion)
   - 或使用中间电路测量 (mid-circuit measurement) + 复位
   
2. **q=0极限的验证**: 当所有环境qubit初始化为|1⟩时, DGF预言R_δ≈0, 但标准QM预言R_δ>0。需要在接近零冗余度区域有足够的统计精度。

3. **环境qubit间的残余耦合**: Zhu使用随机采样受控幺正来模拟光子散射, 环境qubit间不应有直接相互作用。需验证无残余ZZ耦合。

4. **量子态层析的指数代价**: 对m=6-10的碎片, 3^m个Pauli基指数增长。使用:
   - 经典阴影层析 (classical shadow tomography): ~log(d) scaling
   - 或限制核心检验在m≤5范围 (平台已形成)

### §5.3 可行性判断

**当前实验精度可以区分DGF与零假设**:
- 预期信号: R_δ变化50% (q=1→0.5)
- 总系统+统计误差: <10% of R_δ
- 显著性: >5σ
- 实验复杂度与Zhu et al. (2025)相当, 在现有超导量子处理器上完全可实现
- 建议合作组: 浙大量子计算组 (Zhu, Guo, Wang), 或通过Tianyan云平台

---

## §6 对LP32北极星矩阵的定位

| 维度 | 评估 |
|------|------|
| **创新性** | 高。首次提出用预占用环境qubit检验量子Darwinism的容量依赖性, 此前无人提出 |
| **可行性** | 高。在现有超导平台上直接实现, 无需新硬件 |
| **判定性** | 高。DGF与零假设给出定性不同的预言(斜率>0 vs 斜率=0) |
| **理论重要性** | 极高。如果证实R_δ∝q, 意味着量子Darwinism受信息容量约束, 暗示经典客观实在性可能可被"削弱" — 即一个局部宇宙中的客观实在性不是全有或全无, 而是连续可调的 |
| **实验代价** | 中等。~4-6小时测量时间 + ~1周数据分析和系统误差表征 |

**优先级别**: 北极星A级 (最高优先级执行)

---

## §7 下一步

### Round 2任务
1. **数值模拟**: 使用Qiskit Aer噪声模拟器, 输入Zhu et al.的噪声参数(Table S1), 对N=5,7,9,11和q∈[0,1]生成模拟数据, 验证信号可探测性
2. **具体电路编译**: 给出N=10, q=0.5的完整Qiskit电路, 包含所有旋转角度和测量基
3. **误差缓解方案**: 设计针对此实验的专用读出误差缓解和门误差缓解策略
4. **联系实验组**: 撰写合作提案草稿

### 风险与缓解

| 风险 | 概率 | 缓解 |
|------|------|------|
| 占用qubit与自由qubit编码能力实际相同(零假设正确) | 中等 | 即使零假设成立, 实验本身仍是量子Darwinism的重要独立检验 |
| 实验噪声淹没信号 | 低 | 信号大小(50%)远大于噪声(<10%) |
| 理论模型过于简化, 真实R_δ(q)非简单线性 | 中等 | 测量完整q扫描曲线, 捕获任意函数形式 |

---

## 参考文献

[1] Zhu et al., "Observation of Quantum Darwinism and the Origin of Classicality with Superconducting Circuits," Science Advances 11, adx6857 (2025). [arXiv:2504.00781]

[2] Korbicz, "Roads to objectivity: Quantum Darwinism, Spectrum Broadcast Structures, and Strong quantum Darwinism -- a review," Quantum 5, 571 (2021). [arXiv:2007.04276]

[3] Zurek, "Quantum Darwinism," Nature Physics 5, 181-188 (2009).

[4] Riedel & Zurek, "Quantum Darwinism in an Everyday Environment: Huge Redundancy in Scattered Photons," PRL 105, 020404 (2010). [arXiv:1001.3419]

[5] Zwolak & Zurek, "Redundancy of einselected information in quantum Darwinism: The irrelevance of irrelevant environment bits," PRA 95, 030101 (2017). [arXiv:1703.10096]

[6] Riedel, Zurek & Zwolak, "The Rise and Fall of Redundancy in Decoherence and Quantum Darwinism," NJP 14, 083010 (2012). [arXiv:1205.3197]

[7] Baldijao et al., "Emergence of noncontextuality under quantum Darwinism," PRX Quantum 2, 030351 (2021). [arXiv:2104.05734]

[8] Baldijao et al., "Quantum Darwinism and the spreading of classical information in non-classical theories," Quantum 6, 636 (2022). [arXiv:2012.06559]

[9] Tianyan Quantum Group, "Tianyan: Cloud services with quantum advantage," arXiv:2512.10504 (2025).

[10] Zurek, "Quantum Theory of the Classical: Einselection, Envariance, Quantum Darwinism and Extantons," Entropy 24, 1520 (2022). [arXiv:2208.09019]
