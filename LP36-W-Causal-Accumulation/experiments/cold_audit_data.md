# LP36 实验数据包（冷启动审计用）

## 实验1: DGF因果图Monte Carlo模拟

**设置:** 960次模拟，500节点因果DAG（1+1D Minkowski散布→Hasse图），扫参数：散布密度ρ/ρ₀∈[0.3,12]×重置强度r∈[0.1,0.7]×因果聚类f_cluster∈[0.3,1.0]

**核心结果:**
- b₁（1维Betti数）在所有密度下恒定为~1809（E-V+1，Hasse团复形1维→无三角形→循环数）
- b₁存活率r₁随重置强度r单调递减：r=0.1→r₁=0.92, r=0.3→0.73, r=0.5→0.54, r=0.7→0.30
- 因果聚类f_cluster显著增强存活：fc=0.3→r₁=0.83, fc=0.5→0.72, fc=0.7→0.58, fc=1.0→0.36
- 聚类增强倍数：fc=0.3 vs fc=1.0 → 2.3倍
- 高密度极限(ρ/ρ₀=12)无b₁灭绝现象

**关键发现:** b₁不随密度变化（常数~1809），推翻"Goldilocks密度窗口"假说。替代机制：因果聚类驱动存活。

## 实验2: CMB Betti泛函分析

**设置:** 100张合成CMB温度图（nside=32 HEALPix，ΛCDM功率谱），25个阈值ν∈[-3,3]，计算Betti泛函β₀(ν),β₁(ν),χ(ν)

**高斯ΛCDM基线（ν≈0处）:**
- β₀≈41.9, β₁≈6264.2

**注入W信号后（ν≈0处，25%抑制+20%增强）:**
- β₀≈31.5（-25.0%）
- β₁≈7517.0（+20.0%）

**信噪比:**
- β₀信号: 1.5σ
- β₁信号: **6.6σ**
- 达3σ检测需: β₀~4张图, β₁~1张图

## 实验原始数据文件

MC实验代码和数据: D:\Claude\ai-reservations\LP36-W-Causal-Accumulation\experiments\dgf_mc_goldilocks.py
CMB分析代码和数据: D:\Claude\ai-reservations\LP36-W-Causal-Accumulation\experiments\cmb_betti_analysis.py
