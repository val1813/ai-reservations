# A博士/ B博士 审稿任务书

## 审稿对象

DGF-Survivors 项目在 2026-06-10 的最新推进，包含以下模块：

### 模块1: 退相干放大器 (decoherence_amplifier.md + mu_analytic.py)
核心声称: 因果环网络中的Gram矩阵非对角元随环数指数衰减，|G_ab|=exp(μ·n_rings)，导致宏观经典性。
μ(c,p) = E[ln|p·e^{icΔ}+(1-p)·e^{-icΔ}|] 是每环退相干衰减率。

### 模块2: π/4和4边环最小结构 (ring_minimal_structure.md)
核心声称: 4边环是同时满足(1)非平凡退相干(2)非局域信息存储(3)最大效率的最小因果环结构。c=π/4是因为4边环的半环(2边)优化和全环(4边)DFS条件同时被满足。

### 模块3: 集体Clifford保护 (collective_clifford_protection.py)
核心声称: 当4c∈πℤ时，集体|+..+⟩/|-..-⟩模式被完美保护(D_global=0)，而其他自由度仍退相干。这是因果拓扑自然产生的DFS。

### 模块4: T1重建 (T1_reconstruction.md)
核心声称: 时钟精度受DGF基本极限约束: σ_f/f₀ ≥ √(|μ|·γ_E·b1_active/τ_meas)

### 模块5: 康复声明 (rehabilitation_claims.md)
对审稿人攻击的逐条回应和修正。

### 背景材料
- DGF-Survivors/01-established-results.md — 已有定理T1-T6
- DGF-Survivors/03-walls-to-break.md — 墙的状态
- DGF-Survivors/09-b1-scaling-results.md — b1标度律数据
- DGF-Survivors/13-wall-ab-corrected.md — Wall A+B修正
- DGF-Survivors/15-wall9-attack.md — QCMI→退相干映射
- DGF-Survivors/18-wall5-attack.md — 指针基证明
- DGF-Survivors/INSPECTOR_RG_R2.md — RG INSPECTOR审计
- DGF-Survivors/INSPECTOR_decoherence_amplifier.md — 退相干放大器INSPECTOR审计
- DGF-Survivors/pi4_conclusion_review.md — π/4结论自审查
- DGF-Survivors/LITERATURE_POSITIONING.md — 文献定位(含Jacobson对比)
- DGF-Survivors/review_corrections.md — Review修正
- DGF-Survivors/rg_breakthrough.md — RG突破
- DGF-Survivors/classicality_mechanism.md — 经典性机制
- DGF-Survivors/Gamma0_derivation.md — Γ₀推导
- DGF-Survivors/walls_status.md — 墙状态总览
- DGF-Survivors/eta0_wall_status.md — η₀墙状态
- DGF-Survivors/eta0_fundamental.py — η₀基本常数分析
- DGF-Survivors/eta0_noise_spectrum.py — η₀噪声谱预测
- DGF-Survivors/gram_spectrum_2d.py — 2D Gram谱
- DGF-Survivors/high_d_interference.py — 高维干涉
- DGF-Survivors/two_time_cosmology.md — 两时间宇宙学
- DGF-Survivors/two_time_hz.py — 两时间H(z)计算

## A博士任务 (形式攻击)

1. 逐条检查每个模块的核心声称
2. 找数学错误: 符号、单位、极限情况
3. 找逻辑跳跃: A→B的推理链是否有缺口
4. 找隐藏假设: 哪些声称依赖未陈述的前提
5. 区分: 数学事实 vs 物理解释 vs 过度声称
6. 检查: 不同模块之间是否有矛盾
7. 检查: 和已建立的DGF定理(T1-T6)是否一致
8. 检查: 数值代码是否有系统性错误
9. 评分: 每个声称 0(致命)/1(严重)/2(可修复)/3(坚固)
10. 给出总体判断和具体修正建议

## B博士任务 (跨域攻击)

1. 从以下领域找反例或结构问题:
   - 量子信息论: 是否已有等价结果? (HJPW, Fawzi-Renner, Petz, HSW)
   - 统计力学: 退相干放大器是否等价于已知的退相干模型?
   - 量子光学: 光钟精度极限是否已被量子计量学覆盖?
   - 凝聚态物理: 多体退相干是否有标准解释?
   - 量子场论: 因果环在QFT中是否有对应结构?
   - 引力物理: 和Jacobson/Verlinde/Padmanabhan的具体差异?

2. 对每个模块: 从跨域视角攻击
3. 找: DGF声称中哪些被其他领域先发?
4. 找: 哪些可以用更简单的已知机制解释?
5. 找: 哪些隐式借用了其他领域的概念但未引用?
6. 评分标准同A博士
7. 发现跨域连接: 标注"[领域] × DGF = [具体]"
8. 发现更优替代解释: 标注为"新北极星候选"

## 输出格式

两个agent各自输出到 D:\Claude\ai-reservations\DGF-Survivors\ab_audit\ 目录:
- A博士: ab_audit/A_dr_formal_attack.md
- B博士: ab_audit/B_dr_cross_domain_attack.md

格式: 逐模块审查, 每项声称评分, 致命问题标❌, 严重问题标⚠️, 最后总体判断。
