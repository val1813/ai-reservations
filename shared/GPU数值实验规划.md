# 各 LP GPU 可计算实验缺口分析

> 48GB VRAM ≈ RTX 4090/A40/RTX 5070 Ti
> 2026-06-01

---

## 总表

| LP | 数值缺口 | GPU 加速 | 48GB 可行 | 科学回报 | 优先级 |
|----|---------|:--:|:--:|:--:|:--:|
| LP-1 2D MBL | Griffiths尾巴波函数 | ❌ CPU为主 | ⚠️ ED可做~20自旋 | 🟡 验证L_eff>ξ_perc | **P2** |
| LP-2 Planckian | 统计重算 | ❌ CPU | ✅ 秒级 | 🟢 关闭GMM BIC争议 | **P1** |
| LP-3 ν=5/2 | DMRG映射稳定性 | ❌ CPU | ❌ 需MPI集群 | 🟡 S2定量验证 | P3 |
| LP-4 NHSE | HN-Hubbard ED | ❌ CPU | ⚠️ ED可做~16格点 | 🟡 补1 γ_c标度 | P3 |
| **LP-5 DQCP** | **NQS训练J-Q模型** | ✅ **GPU原生** | ✅ **理想** | 🔴 **穿透符号壁垒** | **P1** |
| LP-6 BlackHole | SYK ED | ❌ CPU | ⚠️ N~20 Majorana | 🟢 验证Page曲线 | P2 |
| LP-7 QM-GR | 无 | — | — | — | — |

---

## P1: LP-5 DQCP — NQS 训练 J-Q 模型 🔴 最优先

### 为什么这是 48GB GPU 的最佳用途

LP-5 的 S2 原始问题是"用 NQS 穿透 J-Q 模型的符号问题壁垒"。J-Q 模型（2D 阻挫量子磁体）的基态是 QMC 的符号问题重灾区，DMRG 被限制在柱面几何。**NQS（神经网络量子态）原理上无符号问题**——这正是 GPU 的杀手级应用。

### 具体任务

**目标：** 在 2D J-Q 模型（J2/J1=0.5-0.6）上用 NQS 计算基态，验证 DQCP 是否存在。

**模型：** $$H = J_1 \sum_{\langle ij\rangle} \mathbf{S}_i\cdot\mathbf{S}_j + J_2 \sum_{\langle\langle ij\rangle\rangle} \mathbf{S}_i\cdot\mathbf{S}_j + Q \sum_{\langle ijkl\rangle} (\mathbf{S}_i\cdot\mathbf{S}_j - 1/4)(\mathbf{S}_k\cdot\mathbf{S}_l - 1/4)$$

**方法：** 
- Foundation NQS (arXiv:2602.02665) 或 ViT-NQS (Vision Transformer for quantum states)
- 格点: 10×10 到 16×16（~100-256 自旋）
- 48GB 足够：NQS 参数 ~10^6-10^7，batch size ~10^3，activation 存储 ~2-8 GB
- 训练时间：~24-72 小时/格点

**产出：**
1. 第一个无符号问题的 J-Q 基态计算（vs DMRG 柱面 + QMC 符号问题）
2. 基态能量 + 关联函数 + dimer-dimer 关联 → 判断 Néel/VBS/DQCP
3. 若成功 → PRL 级别（25 年难题的数值突破）

**风险：** NQS 训练在阻挫系统上的收敛性未知。Foundation NQS 在正方晶格有序态上验证过但未在三角 J1-J2 上测试。可能需要 ~1-2 周调试。

### 备选：NQS 训练 Kitaev-海森堡模型

若 J-Q 太难收敛，先在 Kitaev-海森堡模型上做控制实验（有精确解可验证）。

---

## P1: LP-2 Planckian — ν-BIC 修正 + 统计重算

### 为什么这是 P1

LP-2 最脆弱的环节是 GMM K=1 被文献确认为 BIC 小样本偏误。用 ν-BIC（Nguyen & Nguyen 2025, arXiv:2506.20124）重算 S1 的 40 点 α 数据，直接关闭此争议。**不需要 GPU**——纯统计计算，但科学回报极高。

### 具体任务

1. 用 ν-BIC 和 ε-BIC 替代标准 BIC 重做 GMM 模型选择
2. 交叉验证 + ICL 准则作为稳健性检验
3. 给出 α 分布真实组分数的可信区间

**产出：** 关闭 LP-2 最大方法论争议。10 分钟 CPU 时间。

---

## P2: LP-1 2D MBL — Griffiths 尾巴数值验证

### 任务

CP-Griffiths-001：验证 L_eff = L_max + 2ζ·ln(W/g) 在 LP-1 参数域。

**方法：** 2D 无序 Hubbard/HN 模型的精确对角化
- 系统: L×L 格点（L=4-8），L=8 → 64 格点 ~10^6 维稀疏矩阵
- 48GB 可做 shift-invert 提取低能本征态 + 波函数尾巴

**产出：** 验证或修正 L_eff > ξ_perc 的判据。若验证 → LP-1 需要修正"严格稳定"声张。若不成立 → 加强 LP-1 结论。

---

## P2: LP-6 BlackHole — SYK 模型 ED 验证

### 任务

用 ED 验证 SYK₄ 模型的 Page 曲线和 Hayden-Preskill 协议。

- SYK₄: N Majorana, 4-body random coupling
- N=18-20 → 2^(N/2) ~ 512-1024 维 Fock 空间 → 可 ED
- 48GB 足够用于 N=22 (~2048 维)

**产出：** 验证 K1.10 的 no-go 定理在有限 N 下的数值表现。PRD 级别。

---

## 不可行或低回报的

| LP | 任务 | 为什么不可行/低回报 |
|----|------|-------------------|
| LP-3 | ν=5/2 DMRG | 需要 2D 柱面 DMRG（~10^4-10^5 保留态），超出 48GB。需 MPI 集群 |
| LP-4 | HN-Hubbard 相图 | 1D 系统 ED 太小（~20 格点），科学信号不够 |
| LP-7 | — | 纯概念分析，无数值任务 |

---

## 建议执行顺序

```
第1周: LP-2 ν-BIC 统计修复 (CPU, 10分钟)
第1-2周: LP-5 NQS J-Q 模型训练 (GPU, 24-72h/格点)
第3周: LP-1 Griffiths尾巴 ED (GPU/CPU, hours)
第4周: LP-6 SYK ED (CPU, hours)
```

**最高科学回报：LP-5 NQS** ——若成功穿透 J-Q 符号壁垒，这是 PRL 级别的 25 年突破。48GB GPU 恰好适合中等规模 NQS（10×10~16×16 自旋）。
