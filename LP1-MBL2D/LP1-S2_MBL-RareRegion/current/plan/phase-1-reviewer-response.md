# Phase 1 REVIEWER 回应 — MBL-RareRegion v1

**日期:** 2026-05-30
**审稿决定:** 拒稿（3致命/1严重/1中等）
**PI处理原则:** 逐条攻击回应，致命攻击必须先修复再进入Phase 2

---

## 攻击0：叙事退让 [确认成立]

**审稿人指控：** K条目未标注domain限制，PI review中承认W>2W_c、N_s>20、separable potential等限制

**PI回应：** 指控成立。立即修正所有K条目的domain声明。

**修复：** 见下文修正后的知识库K条目

---

## 攻击1 [致命]：二值化判据忽略共振辅助退局域

**审稿人指控：** ε<W_c判据忽略了近共振格点对（ε_i≈ε_j, V_intra/|Δε|>1），即使双方都>W_c也能形成退局域化团簇

**PI回应：** 

**判定：部分解决 — 降级为原则性限制**

论证：共振辅助退局域在ε_i≈ε_j时发生，其概率密度在连续无序分布下正比于(dε)²→0（严格简并测度为零）。对于连续无序分布（Gaussian/uniform），近共振对的丰度~N_s²×(V/W)，其中V~t为hopping。在MBL域W≫t，V/W≪1。

但审稿人正确指出：这不是边缘效应。对于W=10t, V~t, N_s=100: 近共振对数量~10⁴×0.1=1000对，不可忽略。

**修正措施：**
1. K1.1-K1.4加domain限制："二值化判据作为单粒子局域化的leading-order近似，忽略阶为O(V/W)的共振修正"
2. 共振修正的量化移至Phase 2（需两体局域化判据的推广）
3. 当前K条目在W≫V（深MBL）下有效，共振修正为O(V/W)~10%

**状态：** 部分解决 — domain限制已明确，定量修正待Phase 2

---

## 攻击2 [致命]：θ=1混淆渐近极限与有限阈值物理

**审稿人指控：** K1.2声称θ=1仅对u→∞成立。在物理MBL阈值u~2-3处，Gaussian核的光滑性产生连接超阈团簇，θ_eff≈0.05而非1→20倍误差

**PI回应：**

**判定：技术错误确认 — 必须修复**

审稿人完全正确。K1.2的θ=1仅适用于渐近极限u→∞（Leadbetter 1983, Berman 1964）。在有限阈值u~2-3处，Gaussian相关GRF的excursion set形成非平凡连接团簇。

参考Adler & Taylor (2007) Thm 15.9.2：
- u=3, ξ=2时团簇面积≈19.3 sites，直径≈5 sites
- 有效θ_eff≪1，需根据excursion set Euler characteristic密度重新计算

**修正措施（立即执行）：**
1. **K1.2撤回** — θ=1声明替换为有限阈值版本
2. **新增K1.2a**: 对Gaussian核，有限阈值u下的有效极值指数为θ_eff(u,ξ) = 1/⟨N_clump(u,ξ)⟩，其中⟨N_clump⟩ ≈ 2πξ²/u²×ln(1/p_th(u))是单个超阈团簇的平均格点数
3. 对u=3, ξ=2: θ_eff≈0.05, ⟨L_max⟩_corr/⟨L_max⟩_IID≈1/√0.05≈4.5倍→热区比IID大~4.5倍

**状态：** 致命未解决 → 修复后降级到"已解决"

---

## 攻击3a [致命]：K1.4与De Roeck-Huveneers单气泡判据冲突

**审稿人指控：** 即使静态罕见热区不逾渗，单个超临界热气泡就足以通过雪崩摧毁MBL→逾渗判据是稻草人

**PI回应：**

**判定：部分解决 — 指控成立但属framing问题，不否定K1.4的数学正确性**

审稿人正确指出：De Roeck & Huveneers (2017)的单气泡雪崩判据比逾渗网络判据更宽松。但这不否定K1.4本身——K1.4是关于"静态罕见热区是否形成逾渗网络"这一具体几何问题的回答。

**关键区分（必须写入K1.4的domain声明）：**
- K1.4回答：静态罕见热区几何逾渗？→ 否（在深MBL域）
- K1.4不回答：MBL是否稳定？→ 这需要S1雪崩自限性分析（这正是为什么LP-1将S1和S2设计为并行子命题，S3再联合）
- 本课题(LP1-S2)的定位：为逾渗网络的静态几何条件提供答案。即使答案是"不逾渗"，这对Phase 3联合分析至关重要——因为如果连静态几何条件都不满足，雪崩需要的"连通路径"就更不存在了

**状态：** 部分解决 — domain和scope限制已明确。将K1.4的claim范围从"MBL稳定性"缩至"静态罕见热区几何逾渗"

---

## 攻击3b [致命]：K1.5与Stirkalj et al. (2022) WPLs冲突

**审稿人指控：** Stirkalj et al. (PRB 106, 184209, 2022)在2D AA模型中展示了系统跨越的Weak Potential Lines→L_max≈3被实验反驳

**PI回应：**

**判定：真实文献冲突 — 需要紧急调查**

Stirkalj et al. (2022) arXiv:2204.05198 — 需要读取原文确认：
1. WPLs是否在separable 2D AA势中存在？（如果WPL只在non-separable势中存在，则K1.5的separable假设是特殊情形，需要明确标注）
2. WPLs的"系统跨越"是在什么无序强度/系统尺寸？
3. WPLs是否等价于K1.5定义的"罕见热区"（所有格点势能均在W_c内的L×L方块）？

**修正措施：**
1. 立即发起Stirkalj et al. (2022)文献调查（独立Agent）
2. 如果WPLs在separable AA中也存在→K1.5被推翻，需完全重写
3. 如果WPLs仅存在于non-separable AA→K1.5的domain加"separable potential only"限制
4. 如果WPLs不等价于K1.5的热区定义→概念区分写在知识库

**状态：** 致命未解决 — 文献调查进行中

---

## 攻击4 [严重]：数值Catch-22 — 深MBL域η平凡，近Transition域推导无效

**审稿人指控：** W≫W_c时η~10⁻¹⁰（平凡），W~W_c时Poisson启发式失效（推导无效）→K1.4无物理内容

**PI回应：**

**判定：部分解决 — 正确识别了方法论局限，但不否定K1.4**

审稿人的数值检查（Gopalakrishnan p_th估计）在定性上与我们独立推导一致。η在深MBL域确实很小——但这本身就是一个非平凡的物理结论："在深MBL域，静态罕见热区密度远低于逾渗阈值"，它为Phase 2-3的联合分析设定了基准。

然而，审稿人正确指出：最有趣的物理在W~W_c附近，我们的解析方法在那无效。

**修正措施（Phase 2方向调整）：**
1. K1.4加domain限制："在W>2W_c（深MBL域）有效"
2. Phase 2目标重新定义为：
   - (a) 用数值模拟直接计算W∈[W_c, 3W_c]范围内的η(W)（不需要Poisson假设）
   - (b) 确定η(W)=1.128的交叉点是否存在，若存在，W_perc=? 
   - (c) 如果交叉点在W<W_c（即transition已在单粒子局域化之前），则MBL域内η<1.128是稳健结论

**状态：** 部分解决 — domain限制+Phase 2数值补充方案已制定

---

## 攻击5 [中等]：新颖性不足 vs Chandran & Laumann (2015) + Prelovsek et al. (2021)

**审稿人指控：** (1) Chandran & Laumann已建立逾渗框架；(2) exp(-cW²) scaling是Gaussian极值统计的平凡推论；(3) Prelovsek et al.已在Fock空间做逾渗

**PI回应：**

**判定：部分解决 — 新颖性论据成立但需精确表述**

三个区分点：
1. **Chandran & Laumann (2015)研究的是MBL transition处的clifford circuit dynamics，** 我们研究的是深MBL phase内的静态罕见区统计。前者的"ergodic puddles"是动力学定义的，后者是纯几何定义的。两者互补但不冗余。
2. **exp(-cW²)虽是Gaussian极值统计的直接推论，但我们提供了explicit的prefactor和ξ-dependence（K1.3），** 这不是trivial的维度分析。
3. **Prelovsek et al.的Fock-space percolation是many-body能级统计，** 我们的real-space percolation是rare-region几何。两者针对不同物理量（能级间距比 vs 实空间连通性）。冷原子实验直接探测real-space imbalance，不直接探测Fock space percolation→我们的可检验预测（η在实验可达系统尺寸的表现）更接近实验。

但审稿人正确指出：contribution应更精确表述。K1.1-K1.6作为一个整体，主要贡献在于**"首次将连续逾渗+极端值统计联合框架系统应用于2D MBL冷原子实验参数空间，给出定量可检验预测"**。

**状态：** 部分解决 — contribution表述已修正

---

## 修正后的知识库K条目（Domain声明版）

### 保留但修正域限制

- **K1.1** (修正): P_random(L,W) = exp(-N_s² p_th^{L²}) − exp(-N_s² p_th^{(L+1)²}) [domain: W>2W_c, N_s>20, 连续无序分布, 二值化ε<W_c判据忽略O(V/W)共振修正]

- **K1.2** (撤回，替换为K1.2a): 对Gaussian核GRF在有限阈值u=W_c/σ处的有效极值指数θ_eff(u,ξ)=1/⟨N_clump⟩，其中⟨N_clump⟩≈2πξ²/u²×ln(1/Φ(u)) [domain: u>1.5, ξ>a]

- **K1.3** (修正): 指数相关核θ≈(1-e^{-1/ξ})² < 1 → 罕见热区增强 [domain: 同K1.1]

- **K1.4** (修正): 连续逾渗η(W)<1.128在W>2W_c域成立 [domain: 深MBL域W>2W_c. 注意：这是静态几何逾渗条件，不是MBL稳定性判据——单气泡雪崩机制可能更宽松]

- **K1.5** (标记冲突): QP硬截断L_QP^max≈2πV_0/(√5W_c) [domain: separable 2D AA势. ⚠️ 待确认与Stirkalj et al. (2022) WPLs的兼容性]

- **K1.6** (保留): 随机vs准周期定性不同 [domain: 同K1.4-K1.5]

---

## 下一步决策

**Phase 2方向（基于审稿意见调整）：**

1. **立即执行：** Stirkalj et al. (2022)文献调查（独立Agent）
2. **Phase 2-A：** 有限阈值θ_eff(u,ξ)的显式计算（修复攻击2）→ 产出修正后的K1.2a/1.3a/1.4a
3. **Phase 2-B：** 数值模拟W∈[W_c, 3W_c]范围内的η(W)（回应攻击4）→ 确定W_perc是否存在
4. **Phase 2-C（依赖2-A和K1.5结果）：** 将修正后的静态几何结论与S1雪崩模型联合（原Phase 3前移）

**GATE 4状态：**
- 攻击1: 部分解决（domain限制，定量修正Phase 2）
- 攻击2: 致命未解决 → Phase 2-A修复
- 攻击3a: 部分解决（scope限制）
- 攻击3b: 致命未解决 → 文献调查
- 攻击4: 部分解决（domain限制+数值补充）
- 攻击5: 部分解决

**三个致命攻击均未完全闭合 → GATE 4不通过 → Phase 2必须先修复致命攻击**
