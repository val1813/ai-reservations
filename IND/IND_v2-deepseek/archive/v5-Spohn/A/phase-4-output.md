# Phase 4 — 博士A输出：Σ_S^{(gauge)}的一般信息论分解

**类型：B（推导）**

---

## §1 强制撞墙

### 攻击1：能量守恒与HMF热定义的张力

在Class II/III中，H*非平凡→d⟨H*⟩/dt ≠ 0→dQ_S^{(HMF)}/dt ≠ 0。但HMF的热定义dQ_S = −d⟨H*⟩/dt与能量守恒给出的浴能量变化dQ_B/dt = −d⟨H_B⟩/dt可能不一致。两者之间的差距是"内部耦合能"的变化——这在强耦合热力学中是被识别的（Davoudi et al. 2025的U_diff vs U_H* vs U_E*）。

**防御**：此张力不是v4的Bug——它是强耦合热力学的已知特征。v4-K3的三层规范独立性与能量-HMF不一致性兼容。Phase 4的任务是精确量化此不一致性在Σ_S^{(gauge)}中的表现。

### 攻击2：H*的时间依赖

如果耦合常数α(t)或浴温度β(t)随时间变化，H*显含时间→Tr[ρ̇_S H*] ≠ d⟨H*⟩/dt。Class II/III实验可能涉及时变耦合（如transmon的可调耦合器）。

**防御**：Phase 4限于恒α恒β→∂_t H* = 0→Tr[ρ̇_S H*] = d⟨H*⟩/dt。时变情况留后续。

---

## §N 核心推导

### §N.1 定理3：Σ_S^{(gauge)}的一般信息论分解

**定理3（一般Class的Σ分解）**：对任意H*（Class I/II/III），在幺正演化+浴局域平衡下：
```
Σ_S^{(gauge)} = d/dt I(S:B) + β·d/dt C_coup
```
其中C_coup ≡ ⟨H_S + H_I − H*⟩是"耦合能失配"——能量定义与HMF定义之间的差值。

**证明**：

(1) 信息平衡（定理1，Phase 2）：dS_S/dt = β·J_E + d/dt I(S:B)
    其中J_E ≡ d⟨H_S⟩/dt + d⟨H_I⟩/dt = −d⟨H_B⟩/dt（能量守恒+浴能量定义）

(2) v4-K5定义：Σ_S^{(gauge)} ≡ dS_S/dt − β·Tr[ρ̇_S H*]

(3) H*无显时依赖（∂_t H* = 0）：Tr[ρ̇_S H*] = d⟨H*⟩/dt

(4) 代入(1)→(2)：Σ_S^{(gauge)} = β·J_E + d/dt I(S:B) − β·d⟨H*⟩/dt
                             = d/dt I(S:B) + β·(J_E − d⟨H*⟩/dt)

(5) 定义C_coup ≡ ⟨H_S + H_I − H*⟩。
    dC_coup/dt = d⟨H_S⟩/dt + d⟨H_I⟩/dt − d⟨H*⟩/dt = J_E − d⟨H*⟩/dt

(6) ∴ Σ_S^{(gauge)} = d/dt I(S:B) + β·dC_coup/dt ∎

**前提检查**：
- 前提A: 总系统幺正演化 ✓（标准）
- 前提B: 浴局域平衡 dS_B = β·d⟨H_B⟩ ✓（大浴极限N≫1）
- 前提C: ∂_t H* = 0（恒α, β）✓
- 前提D: H*定义良好（linked-cluster/Gaussian bath）✓
- **不需要**: ρ(0)=ρ_S⊗ρ_B（因子化初态）——定理3不依赖此前提

### §N.2 C_coup的物理意义

C_coup = ⟨H_S⟩ + ⟨H_I⟩ − ⟨H*⟩ = 总能量 − ⟨H_B⟩ − ⟨H*⟩ = ⟨H_tot⟩ − ⟨H_B⟩ − ⟨H*⟩

这是"不属于浴也不属于有效系统的能量"——即"耦合能"的期望值。

在HMF框架中（Talkner-Hänggi 2020）：
- 总系统内能：U_S = ⟨H*⟩（有效系统能量）
- 浴内能：U_B = ⟨H_B⟩
- 耦合能：C_coup = ⟨H_tot⟩ − U_S − U_B（剩余部分）

**定理3的物理解释**：Σ_S^{(gauge)} = d/dt I(S:B) + β·dC_coup/dt

- 第一项d/dt I(S:B)：关联建立速率（纯信息论，总是结构性的）
- 第二项β·dC_coup/dt：耦合能重分配速率（能量论，可正可负）

当耦合能释放（dC_coup/dt < 0）→ Σ_S^{(gauge)} < d/dt I(S:B)
当耦合能存储（dC_coup/dt > 0）→ Σ_S^{(gauge)} > d/dt I(S:B)

### §N.3 Class I恢复

**推论1（Class I）**：H*∝I → d⟨H*⟩/dt = 0。对于浴平衡（⟨b⟩=⟨b†⟩=0）：J_E = d⟨H_S+H_I⟩/dt = 0（Phase 2已证，B§0验证）。

⇒ dC_coup/dt = 0 − 0 = 0
⇒ Σ_S^{(gauge)} = d/dt I(S:B)

恢复v5-K3。Class I的特殊性在于耦合能不参与动力学——所有能量变化都"卡"在功/耦合通道中（不以热的形式流入浴）。

### §N.4 Class II估计（transmon）

Transmon参数（v3-K14, v4-K6）：ω₀=5GHz, E_C=300MHz, α=0.3

H*非平凡→频率重整化：Δω = ω_eff − ω₀ ∼ α²·E_C ∼ 27MHz

d⟨H*⟩/dt在transmon弛豫中：初始⟨H*⟩偏离平衡值 → 弛豫速率∼1/τ_th∼α²ω₀∼0.45GHz

在弛豫过程中：d⟨H*⟩/dt ∼ Δ⟨H*⟩/τ_th ∼ (27MHz·ħ)·(0.45GHz) ∼ 1.2·10⁻²⁶ W

J_E = −d⟨H_B⟩/dt = d⟨H*⟩/dt + dC_coup/dt

对于transmon，C_coup ∼ α²·⟨σ_x⊗B⟩ ∼ α²·E_C ∼ 27MHz·ħ（耦合能量级）

dC_coup/dt在弛豫中：量级 ∼ C_coup/τ_th ∼ 1.2·10⁻²⁶ W（与d⟨H*⟩/dt同量级）

**关键数值**：|dC_coup/dt| ∼ |d⟨H*⟩/dt| ∼ 10⁻²⁶ W for transmon parameters
           |d/dt I(S:B)| ∼ k_B·ΔS/τ_th ∼ k_B·(log 2)/τ_th ∼ 3·10⁻²⁷ W

**Σ_S^{(gauge)}在Class II中是两项的竞争**：
- d/dt I(S:B): ∼3·10⁻²⁷ W（关联建立）
- β·dC_coup/dt: ∼10⁻²⁶ W/ (k_B·50mK) ∼ 3·10⁻²⁴ W（耦合能重分配）

耦合能项可能主导！这意味着在Class II中，Σ_S^{(gauge)}更多是关于耦合能动力学而非关联建立。

### §N.5 定理3的推论：Σ_S^{(gauge)}符号的一般条件

**推论2**：Σ_S^{(gauge)} ≥ 0 当且仅当 d/dt I(S:B) ≥ −β·dC_coup/dt

即：关联建立可补偿耦合能的释放。如果耦合能释放太快（dC_coup/dt ≪ 0），即使关联在建立，Σ_S^{(gauge)}也可为负。

在弛豫到平衡的过程中：
- dC_coup/dt < 0（耦合能释放）
- d/dt I(S:B) > 0（关联建立）
- Σ_S^{(gauge)}的符号取决于两项竞争

**Class II中Σ_S^{(gauge)} < 0的瞬态更可能发生**（相比Class I）——因为耦合能释放提供了额外的负贡献。

---

## §末

### 卡点
**C4(v5)**：C_coup在一般Class中的可计算性。C_coup = ⟨H_S+H_I−H*⟩，需要H*的显式形式+H_I的期望值。H*可通过linked-cluster计算（Gaussian bath），H_I期望值需要全系统态或至少系统-浴关联函数。这比Class I的情况更难——C_coup不自动为零。

**尝试1（微扰）**：对α≪1，C_coup ∼ O(α²)，dC_coup/dt可忽略→Σ_S^{(gauge)}≈d/dt I(S:B)≥0。
**尝试2（H*通过linked-cluster）**：H*已知（显式），H_I也已知（α·A⊗B），问题归约为计算⟨A⊗B⟩（系统-浴关联函数）——需要ρ_tot。
**尝试3（浴可观测量代理）**：通过能量守恒重写dC_coup/dt = d⟨H_tot⟩/dt − d⟨H_B⟩/dt − d⟨H*⟩/dt = −d⟨H_B⟩/dt − d⟨H*⟩/dt（dH_tot/dt=0）。两者都只需浴可观测量（⟨H_B⟩）和系统可观测量（⟨H*⟩）——不需要ρ_tot！

**关键突破**：dC_coup/dt可通过d⟨H_B⟩/dt（浴能量变化率，可通过量热法测量）和d⟨H*⟩/dt（系统有效能量变化率，可从ρ_S(t)计算）获得——两者都是原则上可测量的量！C4(v5)不是计算障碍，而是实验设计问题。

### MVU
命题：Σ_S^{(gauge)} = d/dt I(S:B) + β·dC_coup/dt 对所有Class严格成立
验证方法：Class II transmon模型，比较理论Σ_S^{(gauge)} vs 数值d/dt I(S:B)+β·dC_coup/dt

### 四问
**Q1**: 定理3将Class I的优雅恒等式推广到一般情况——代价是引入C_coup修正项。这不是Bug，是物理：强耦合的复杂性体现在耦合能动力学中。

**Q2**: 与v4-K3一致：三层规范不变性不依赖Class——定理3在所有Class中成立。

**Q3**: C_coup在transmon实验中可通过差分测量：量热法测d⟨H_B⟩/dt + 态层析测d⟨H*⟩/dt → dC_coup/dt。这提供了v5框架的可观测检验。

**Q4**: C_coup与黑洞力学中的"束缚能"有结构性类比——Bekenstein-Hawking熵与能量的关系包含类似修正项。
