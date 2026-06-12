# DGF on IBMQ — Feasibility Assessment

## Experimental Protocol

**Goal**: Verify b₁=1 → c=1/2 Ising CFT via entanglement scaling on IBMQ hardware.

**Circuit architecture**:
- N=8-12 qubits in a ring topology (b₁=1 in G_conn)
- Alternating layers: local CNOTs (nearest-neighbor) + nonlocal Cartan gate (diametric, creates the causal loop)
- Tune nonlocal gate Cartan angle θ to vary ρ_K
- At critical θ_c: entanglement should show c=1/2 Ising scaling
- Away from θ_c: area-law (θ<θ_c) or volume-law (θ>θ_c)

**Measurement**: Randomized measurement protocol (Brydges et al. 2019, Science 364, 260)
- Apply random single-qubit unitaries before measurement
- Compute Rényi-2 entropy from cross-correlations
- Requires ~10^4 shots per setting × ~100 random unitaries = ~10^6 shots total

## Hardware Requirements

| Parameter | Minimum | Recommended | IBMQ Open Plan |
|:--|:--|:--|:--|
| Qubits | 8 | 12-16 | 5-7 ❌ |
| 2Q gate fidelity | >99% | >99.5% | ~99% ⚠️ |
| Circuit depth | 15-20 layers | 30-40 layers | Marginal |
| Total shots | 10^5 | 10^6 | Hours of runtime |
| Connectivity | Ring + 1 long-range | Full ring | Limited |

## Feasibility by b₁

| b₁ | c | θ_c (ideal) | θ_c^eff (η≈0.28) | Verdict |
|:--|:--|:--|:--|:--|
| 1 | 1/2 | 0.50 | ~1.8→饱和 | ❌ 需要100%非局域门, NISQ不可达 |
| 2 | 7/10 | 0.29 | ~1.05 | ❌ 仍饱和 |
| 3 | 4/5 | 0.19 | ~0.68 | 🟡 首次可测, 但需b₁=3拓扑 |
| 5 | 25/28 | 0.10 | ~0.35 | 🟢 可测, 需5环 |
| 10 | ~0.96 | 0.05 | ~0.18 | 🟢 理想, 需10环 |

## The Real Problem

θ_c^eff(b₁) = θ_c(b₁) / η ≈ (1-cos(π/(b₁+2))) / 0.28

η≈0.28 (门保真度×连通性×Cartan对齐) 是当前硬件的杀手。
b₁=1,2 的 θ_c^eff 饱和在1——意味着需要100%非局域门，
物理上不可能。**b₁≥3才是NISQ可测区域。**

但b₁=3需要3个独立因果环的量子电路拓扑，
对当前IBMQ硬件的连通性是挑战。

## 替代方案: 经典模拟→硬件共设计

1. **先经典验证**: TensorNetwork.jl/iPEPS验证b₁=3, N≤24的c(b₁)
2. **设计硬件友好电路**: 为IBMQ Heron鱼骨拓扑优化b₁=3环嵌入
3. **申请IBMQ学术额度**: 需要≥27 qubits, ≥50层深度
4. **若获批**: 完整DGF验证实验可在一个维护窗口内完成

## 诚实结论

IBMQ Open Plan (free tier): **不够**。需要学术合作额度。
经典模拟: N≤24的b₁=1验证**现在就能做**，且成本更低。
