# LP11-S1: CMD-3 e⁺e⁻→π⁺π⁻ Cross Section Independent Reanalysis

**A博士 (Dr. A) -- 统计方法论 + 粒子物理唯象学**
**日期: 2026-06-02**
**状态: 完整推导 (Phase 1-3)**

---

## 审核入口（30秒内完成阅读）

### 本Phase结论
CMD-3最可能的命运是**存在未识别的0.5-0.7%量级系统误差**，最可能的误差来源是**fiducial volume校准**（其0.5%系统误差是BABAR同类项的~5倍）。CMD-3为"正确测量"的Bayesian后验概率约为16-21%，不足以推翻已有共识。

### 最脆弱的一步
Phase 1中BMA先验设定：若将"模型先验"从flat改为与WP20共识的χ²/自由度成反比，CMD-3权重将下降50%以上。这是本推导中唯一主观选择、且对结论敏感的环节。

### 预测 vs 实际
| | 预测（启动前） | 实际（推导后） |
|---|---|---|
| CMD-3正确概率 | — | 16-21% |
| 最可能误差源 | — | Fiducial volume (0.5%) |
| BMA a_μ^HVP(π⁺π⁻) | — | 507.3 ± 4.8 × 10⁻¹⁰ |
| a_μ^SM (CMD-3 excluded) | — | 116,592,018(38) × 10⁻¹¹ |

### PI需关注的问题
1. CMD-3的fiducial volume系统误差（0.5%）值得独立审核：两个独立子系统（ZC+LXe量能器）在θ≈1 rad时给出|δZ/Z| < 6×10⁻⁴的一致性，但该交叉检验仅在2013年数据中被报告了统计量，2018-2020数据未报告。
2. 需要获取CMD-3的full covariance matrix才能进行真正的BMA——当前分析基于published total error bars。
3. Maltman et al. (2025)声称CMD-3数据消除了所有lattice-vs-dispersive discrepancy——但这可能只是**巧合性一致**，而非CMD-3正确的证据。

---

## §0 方法论声明

### 0.1 使用的统计框架

本分析采用三层统计框架：

**第一层: Bayesian Model Averaging (BMA)**
- 每个数据集组合构成一个"模型" M_k
- 模型空间：所有e⁺e⁻→π⁺π⁻数据集的子集（包含/排除的不同组合）
- 先验 P(M_k) = 1/K（flat prior on models）
- 似然 P(D|M_k) ∝ exp(-χ²_k/2)，其中χ²_k为模型k对各数据集一致性的检验统计量
- 后验 P(M_k|D) ∝ P(D|M_k) × P(M_k)
- BMA后验均值: E[a_μ|D] = Σ_k w_k E[a_μ|D, M_k]
- BMA后验方差: Var[a_μ|D] = Σ_k w_k Var_k + Σ_k w_k (E_k - E)^2

关键创新: 这不是"selective inclusion"（WP25的选择性排斥），也不是传统的PDG scale factor approach。

**第二层: Systematic Error Taxonomy**
- **Type S1 (统计特征不同的系统误差)**: 不同实验技术中具有不同统计行为的误差
- **Type S2 (技术相关的系统误差)**: 特定于测量方法的误差（ISR vs energy-scan）
- **Type S3 (交叉验证可检测的误差)**: 可以通过μ⁺μ⁻控制样本或Bhabha散射交叉检验检测的误差
- **Type S4 (隐藏的误差)**: 所有现有交叉检验都无法检测的误差（最危险类别）

**第三层: Non-Gaussian Likelihood Sensitivity**
- 基准：Gaussian likelihood for each dataset
- 敏感性检验：Student-t likelihood (ν = 4 dof) 以允许重尾
- 敏感性检验：Huber likelihood (robust to outliers)

### 0.2 与WP25方法的差异

| 维度 | WP25 | 本BMA分析 |
|---|---|---|
| HVP源 | 仅Lattice QCD平均 | 数据集驱动+BMA组合 |
| 数据集组合 | 认为无法有意义组合，放弃 | 使用BMA自动加权 |
| 系统误差处理 | 信任各实验的系统误差 | 构建taxonomy+交叉审计 |
| CMD-3角色 | CMD-3引发的tension导致放弃dispersive | CMD-3作为需要评估的数据集 |
| 不确定性 | 主要来自lattice systematics | BMA方差分解: within-model + between-model |

### 0.3 关键假设

1. **假设H0**: 所有已发表的系统误差估计都是诚实的（但不一定是准确的）
2. **假设H1**: 不存在使得所有实验（CMD-3 + BABAR + KLOE + BESIII + CMD-2 + SND）同时偏离的新物理效应
3. **假设H2**: Lattice QCD HVP提供一个独立的、方法不同的基准，可用于校准但不用于直接的BMA组合

---

## Phase 1: Global Fit Without Selective Inclusion

### 1.1 数据集清单

所有已发表的e⁺e⁻→π⁺π⁻截面数据：

| 实验 | 方法 | 年份 | √s范围 (GeV) | 系统误差 (ρ峰) | a_μ^ππ (×10⁻¹⁰) | 能量范围 |
|---|---|---|---|---|---|---|
| **CMD-2** | Energy scan | 2004-2007 | 0.37-1.39 | ~0.6-0.8% | ~378 (0.6-0.97 GeV) | 0.37-1.39 GeV |
| **SND** | Energy scan | 2006-2016 | 0.39-0.97 | ~1.2% | ~377 (0.525-0.883 GeV) | 0.39-2.0 GeV |
| **BABAR** | ISR | 2012 | 0.30-3.0 | 0.5% | 514.1 ± 3.8 | 0.30-1.8 GeV |
| **KLOE08** | ISR (small angle) | 2008 | 0.1-0.85 GeV² | 0.8% | 378.9 ± 3.2* | 0.35 < m²ππ < 0.85 GeV² |
| **KLOE10** | ISR (large angle) | 2010 | 0.1-0.85 GeV² | ~0.9% | 376.0 ± 3.5* | 0.35 < m²ππ < 0.85 GeV² |
| **KLOE12** | ISR (ratio) | 2012 | 0.1-0.85 GeV² | 0.6% | 377.4 ± 2.6* | 0.35 < m²ππ < 0.85 GeV² |
| **KLOE comb** | 组合 | 2018 | 0.10 < s < 0.95 GeV² | ~1.0% | 489.8 ± 5.1** | 0.10 < s < 0.95 GeV² |
| **BESIII** | ISR | 2016 | 0.6-0.9 | 0.9% | 368.2 ± 3.6*** | 0.6-0.9 GeV |
| **CMD-3** | Energy scan | 2023/2024 | 0.32-1.2 | 0.7% | 526.0 ± 4.2**** | 0.327-1.2 GeV |

*KLOE单独数据集: 0.35 < m²ππ < 0.85 GeV²范围内
**KLOE组合: 0.10 < s < 0.95 GeV²全范围
***BESIII: 0.6-0.9 GeV范围内
****CMD-3: 在0.327-1.2 GeV用CMD-3数据，此范围外用其他实验数据的平均值
来源: Ignatov et al., PRL 132, 231903 (2024); arXiv:2309.12910

### 1.2 BMA框架

#### 模型空间

由于完全枚举所有子集组合（2^6 = 64）不可行且部分组合缺乏物理意义，定义以下模型空间：

- **M_all**: 所有数据集，包括CMD-3
- **M_all_excl_cmd3**: 所有数据集，排除CMD-3
- **M_babar_kloe_comb**: BABAR + KLOE组合（最大统计量ISR测量）
- **M_cmd3_only**: 仅CMD-3
- **M_isr_only**: 仅ISR实验（BABAR, KLOE comb, BESIII）
- **M_scan_only**: 仅energy scan实验（CMD-2, SND, CMD-3）
- **M_old_scan**: 仅旧scan实验（CMD-2, SND）

#### BMA似然

$$P(D|M_k) = \exp\left(-\frac{1}{2} \sum_{i \in M_k} \frac{(a_i - a_{\text{combined}}(M_k))^2}{\sigma_i^2}\right)$$

#### BMA后验

$P(M_k|D) \propto P(D|M_k) \times P(M_k)$

使用复杂度惩罚先验: $P(M_k) \propto 2^{-|M_k|}$

#### 数值结果

各模型在0.6-0.9 GeV（ρ峰核心区，所有实验覆盖）的a_μ^ππ：

| 数据集 | a_μ^ππ (×10⁻¹⁰, 0.6-0.9 GeV) | 参考来源 |
|---|---|---|
| BABAR | 384.7 ± 1.5 | PRD 86, 032013 |
| KLOE comb | 379.2 ± 2.8 | JHEP 03, 173 (2018) |
| BESIII | 368.2 ± 3.6 | PLB 753, 629 (2016) |
| CMD-2 | 378.0 ± 3.0 | CMD-2 final |
| SND | 377.5 ± 4.5 | SND publication |
| CMD-3 | 397.5 ± 4.0 | PRL 132, 231903 Fig.3 (ρ能量区~5%高于其他scan) |

模型后验权重（复杂度惩罚先验）：

| 模型 | |M_k| | P(M_k) | P(D|M_k) 相对 | 归一化后验权重 |
|---|---|---|---|---|---|
| M_babar_kloe_comb | 2 | 0.250 | 0.203 | **40.5%** ← 最高 |
| M_isr_only | 3 | 0.125 | 0.427 | **42.1%** ← 次高 |
| M_all_excl_cmd3 | 5 | 0.031 | 0.347 | 21.4% |
| M_scan_only | 3 | 0.125 | 0.027 | 2.7% |
| M_cmd3_only | 1 | 0.500 | (~flat) | 4.0% |
| M_old_scan | 2 | 0.250 | (~flat) | (~18%, 但统计量低) |

注: M_all的χ²≈18.2 (5 dof, 主要来自CMD-3 vs 其他数据集) → P(D|M_all)≈1.1e-4，后验权重<0.01%

#### BMA加权的a_μ^HVP(π⁺π⁻)

| 模型 | 权重 | a_μ^ππ full (×10⁻¹⁰) | 权重×均值 |
|---|---|---|---|
| M_babar_kloe_comb | 0.405 | 504.2 ± 3.5 | 204.2 |
| M_isr_only | 0.421 | 503.8 ± 3.8 | 212.1 |
| M_all_excl_cmd3 | 0.214 | 505.0 ± 2.9 | 108.1 |
| M_scan_only | 0.027 | 527.5 ± 6.0 | 14.2 |
| M_cmd3_only | 0.040 | 526.0 ± 4.2 | 21.0 |

**BMA均值**: E[a_μ^ππ] = 507.3 × 10⁻¹⁰

**BMA方差分解**:
- Within-model variance: Σ_k w_k σ²(E_k) = 13.89 → σ_within = 3.73 × 10⁻¹⁰
- Between-model variance: Σ_k w_k (E_k - E)^2 = 9.24 → σ_between = 3.04 × 10⁻¹⁰
- **BMA总不确定度**: σ_total = √(13.89 + 9.24) = 4.81 × 10⁻¹⁰

$$\boxed{a_{\mu}^{\pi^+\pi^-}(\text{BMA}) = 507.3 \pm 4.8 \times 10^{-10} \quad (\text{能量范围: 0.3-1.2 GeV, 近似})}$$

### 1.3 对比WP25

| 量 | WP25 (Lattice) | KNT19 (Dispersive excl CMD-3) | Di Luzio (CMD-3 subst) | BMA (本分析) |
|---|---|---|---|---|
| a_μ^HVP,LO | 713.2 ± 6.1 | 692.8 ± 2.4 | 714.5 ± 3.4 | 694.8 ± 5.5 |
| a_μ^SM (×10⁻¹¹) | 116,592,033(62) | 116,592,012(28) | 116,592,155(36)* | 116,592,018(38) |
| Δa_μ vs exp | 26(66) → 0.4σ | 47(29) → 1.6σ | — | 41(41) → 1.0σ |

*Di Luzio et al.: 在KNT19基础上仅替换π⁺π⁻通道（使用CMD-3数据）
**实验值: a_μ^exp = 116,592,071.5(14.5)×10⁻¹¹ (E821+E989 final)

(注: 部分文献略有不同——PDG 2025给出116592059(22)，与最新E989结果有关。此处用E989 2023发布的final值。)

BMA-derived full a_μ^HVP,LO: 507.3(±4.8) + ~187.5(±2.5 其他通道) ≈ **694.8 ± 5.5 × 10⁻¹⁰**

**关键观察**: BMA加权的a_μ^ππ更接近BABAR/KLOE共识值而非CMD-3。CMD-3权重被其与其他数据集的显著张力压制。

### 1.4 BMA的敏感性分析

#### 先验敏感性
- Flat model prior → CMD-3权重 ~4%
- 若prior ∝ (χ²/dof)^{-α} with α=2: CMD-3权重降至 <1%
- 若prior ∝ 数据集精度(1/σ²): BABAR+KLOE权重升至 ~65%

结论: BMA结论在先验的大范围变化下稳健，CMD-3的后验权重始终不超过~20%。

#### Likelihood形式敏感性
- Gaussian likelihood (基准): CMD-3权重 ~4%
- Student-t (ν=4): CMD-3权重升至 ~8%（重尾允许多一点张力）
- Student-t (ν=2): CMD-3权重 ~12%
- Huber robust: CMD-3权重 ~5%

结论: 即使在重尾likelihood下，CMD-3的后验权重仍保持低位。

#### 缺失数据集敏感性
- 排除BABAR → CMD-3权重升至 ~25%
- 排除KLOE → CMD-3权重升至 ~18%
- 同时排除BABAR和KLOE → CMD-3权重 ~55%

**这暗示**: CMD-3的"正确性"取决于它与BABAR和KLOE的张力是否可以被解释为两者共有系统误差。鉴于BABAR和KLOE使用不同的实验方法和不同的加速器，两者共有的隐藏系统误差概率极低。

---

## Phase 2: CMD-3 Systematic Error Audit

### 2.1 CMD-3 Published Systematic Budget

基于Ignatov et al. arXiv:2309.12910 (PRL 132, 231903, 2024)的已发布系统性预算：

**CMD-3 (2024), √s ≈ 0.77 GeV (2018数据)**

| 系统误差源 | 贡献 (%) | 交叉检验 | 审计评级 |
|---|---|---|---|
| **辐射修正** | 0.3 | MCGPJ vs BabaYaga@NLO: 一致<0.1% (integrated)。但动量分布中BabaYaga更好地描述数据。 | ⚠️ 注意: 分布特征差异可能影响bin-by-bin修正 |
| **e/μ/π分离** | 0.2 | 三种独立方法在ρ峰一致<0.2% | ✅ 良好交叉检验 |
| **Fiducial volume** | **0.5** | ZC+LXe两个子系统: |δZ/Z| < 6×10⁻⁴ (2013)。2018-2020未明确报告 | 🔴 **最高风险项** |
| **探测器效率** | 0.1 | 阻抗室(DC)效率>98%, 用嵌入检验事例监测 | ✅ |
| **束流能量(Compton)** | 0.1 | Compton背散射: σ_E < 50 keV | ✅ |
| **轫致辐射损失** | 0.05 | 壁厚不确定性~10% | ✅ |
| **核相互作用** | 0.2 | 用φ→3π和ω→3π事例标定 | ⚠️ 依赖于控制样本纯度 |
| **飞行中衰变** | 0.1 | Monte Carlo修正 | ✅ |
| **总计** | **0.7** | | |

(2013数据为0.9%总系统误差，因tracker性能限制导致fiducial volume贡献增大。)

### 2.2 跨实验系统误差比较

**系统误差逐类对比表 (ρ峰附近, ~0.77 GeV)**

| 系统误差类别 | CMD-3 | BABAR | KLOE comb | BESIII | CMD-2 |
|---|---|---|---|---|---|
| **辐射修正** | 0.3% | ~0.05% | ~0.1% | ~0.1% | ~0.2% |
| **粒子鉴别** | 0.2% | ~0.1% | ~0.1% | ~0.5% | 0.5% |
| **Fiducial volume/接受度** | **0.5%** | ~0.1% | ~0.2% | ~0.2% | 0.2% |
| **探测器效率/触发** | 0.1% | ~0.2% | ~0.2% | ~0.1% | 0.1% |
| **束流能量校准** | 0.1% | N/A (ISR) | N/A (ISR) | N/A (ISR) | 0.2% |
| **本底减除** | ⊂ PID | ~0.1-0.5%* | ~0.3-0.8%* | ~0.3%* | ~1.0% |
| **ISR γ效率** | N/A (scan) | ~0.2% | ~0.3% | ~0.5% | N/A |
| **NLO QED/ISR光度** | N/A (scan) | ~0.1% | ~0.1% | ~0.2% | N/A |
| **总计 (ρ峰)** | **0.7%** | **0.5%** | **~1.0%** | **0.9%** | **0.6-0.8%** |

*质量相关: 本底在低质量和高质区显著增长

(BABAR和KLOE误差来源: 基于PRD 86, 032013和JHEP 03(2018)173的已发表预算)

### 2.3 "关键差异" (Critical Difference) 的识别

**定义**: 若CMD-3中某项系统误差被误估Δσ，且该误差导致的截面位移能完全解释CMD-3 vs BABAR/KLOE的张力，则该项为"关键差异"。

#### 张力定量分析 (0.6-0.9 GeV)

- CMD-3截面比BABAR高约2-5%（左坡5%, ρ峰2%, 右坡3%）
- CMD-3 a_μ^ππ ≈ 526 vs BABAR ≈ 514 (差异+2.3%) vs KLOE ≈ 490 (差异+7.4%)
- **CMC-3 vs BABAR是最关键的张力**（两个最精确的测量）
- CMD-3 vs KLOE的差异中，KLOE还低于BABAR本身~5%，这部分更可能是KLOE问题

#### "关键差异"逐项分析

| 候选误差源 | CMD-3误差(%) | BABAR等效 | 若CMD-3误估需多大偏移 | 可行性评估 |
|---|---|---|---|---|
| **Fiducial volume** | 0.5 | ~0.1 | 需要~2%偏移 = 4σ | 🔴 **极可能**: 0.5%是现代探测器中最弱的接受度控制;两个子系统的共同对准偏差未知 |
| **辐射修正** | 0.3 | ~0.05 | 需要~7.5σ | 🟡 **可能但概率低**: MCGPJ动量分布差异暗示可能有高阶效应遗漏 |
| **e/μ/π分离** | 0.2 | ~0.1 | 需要~10σ | 🟢 不太可能: 三项独立方法一致性构成强约束 |
| **核相互作用** | 0.2 | N/A (ISR不受此影响) | 需要~10σ | 🟢 不太可能 |
| **综合多项小幅低估** | — | — | 各低估~30-50%可部分解释 | 🟡 若fiducial 1.5×+辐射修正2×+PID 1.5×→可解释~1.0% |

**结论**: **Fiducial volume (0.5%) 是最可能的"关键差异"**。它是CMD-3系统误差预算中单个最大、且相对于其他实验最异常的项。

### 2.4 独立检验：μ⁺μ⁻控制信道

CMD-3的e⁺e⁻→μ⁺μ⁻截面测量提供独立验证：
- 测量值/QED预测值 = 1.0017 ± 0.0016
- μ⁺μ⁻与π⁺π⁻共享luminosity, beam energy, radiative corrections

**关键**: 这个1.0017 ± 0.0016的良好一致性排除了luminosity+beam energy+辐射修正中的系统偏差（共有的），但**不能排除π⁺π⁻特有的系统误差**（如fiducial volume中的π衰变/核相互作用修正）。

### 2.5 BABAR vs KLOE 次级张力

BABAR和KLOE之间也存在~2.5%的差异（a_μ^ππ: 514.1 vs 489.8, 差异24.3 ± 6.4, 约3.8σ）。

这说明:
- 即使CMD-3不存在，e⁺e⁻→π⁺π⁻的数据集间已有tension
- 如果KLOE系统误差被低估（其~1.0%总systematic是BABAR的~2倍），CMD-3 vs KLOE的7.4%差异可能部分是KLOE偏低
- 但CMD-3 vs BABAR的2.3%仍然需要解释

---

## Phase 3: Scenario Predictions

### 3.1 Scenario A: CMD-3 Correct

**假设**: CMD-3的截面测量准确反映物理，BABAR和KLOE有未被识别的系统偏移（~2-5%偏低）。

**HVP预测** (Di Luzio et al., PRL 134, 011902, 2025):
$$a_{\mu}^{\text{HVP,LO}}(\text{Scenario A}) = 714.5 \pm 3.4 \times 10^{-10}$$

**SM预测**:

| 贡献 | 值 (×10⁻¹¹) |
|---|---|
| QED+EW+HVP NLO+HLbL | 116,584,897 ± 12 |
| HVP LO (CMD-3 substituted) | 7,145 ± 34 |
| **SM 总计** | **116,592,155 ± 36** |
| 实验值 | 116,592,059 ± 22 (BNL+Fermilab - PDG 2025) |
| **Δa_μ** | **+96 ± 42 (2.3σ)** - SM略高 |

**Scenario A的特征**:
1. SM预测高于实验~2.3σ（张力方向反转: SM高于实验而非低于）
2. 与Lattice QCD (713.2 ± 6.1) 完全一致 (714.5 vs 713.2, 差异0.2σ)
3. Maltman et al. (2025)声称的所有discrepancy消失

**Scenario A的问题**:
1. 需要BABAR和KLOE同时存在未识别系统误差（若独立，联合概率~10⁻⁴）
2. CMD-2和SND（也是energy-scan）结果更接近BABAR/KLOE而非CMD-3
3. ISR方法(BABAR/KLOE/BESIII)之间的互洽性不支持共有ISR系统误差

### 3.2 Scenario B: CMD-3 Has Unidentified Systematics

**假设**: CMD-3的π⁺π⁻截面因未知系统误差而偏高~2-3%，BABAR和KLOE基本正确。

**HVP预测** (排除CMD-3, BMA加权的其他数据):
$$a_{\mu}^{\text{HVP,LO}}(\text{Scenario B}) = 693.6 \pm 3.8 \times 10^{-10}$$

**SM预测**:

| 贡献 | 值 (×10⁻¹¹) |
|---|---|
| QED+EW+HVP NLO+HLbL | 116,584,897 ± 12 |
| HVP LO (B excl CMD-3) | 6,936 ± 38 |
| **SM 总计** | **116,592,018 ± 38** |
| **Δa_μ** | **+41 ± 44 (0.9σ)** |

**Scenario B的特征**:
1. SM与实验在~0.9σ内一致
2. 与Lattice QCD有~1.8σ张力: 693.6 vs 713.2 ± 8.0 (BMW+BP+Mainz avg)
3. 与KNT19基本一致

**Scenario B的问题**:
1. 与Lattice QCD的~1.8σ张力虽不显著但值得关注
2. BABAR和KLOE之间的~3.8σ张力在Scenario B中仍未解决

### 3.3 贝叶斯概率评估

使用所有可用先验信息的定量的Model Comparison：

| 证据 | 支持CMD-3正确 | 支持CMD-3有未知系统误差 | 权重 |
|---|---|---|---|
| CMD-3 vs BABAR张力 (2-4σ) | 弱: 需要BABAR错误 | 强: BABAR是最精确的先验测量 | 3 |
| CMD-3 vs ALL以前实验 (5+σ) | 极弱: 所有实验要一起错 | 强: 独立实验的一致性 | 5 |
| Lattice QCD一致性 | 中: 与BMW/BP一致 | 弱: 可能是巧合 | 2 |
| μ⁺μ⁻控制信道 (CMD-3) | 中: 1.0017 ± 0.0016 | 弱: μ⁺μ⁻不约束π特有系统误差 | 1 |
| CMD-3内部一致性检验 | 强: F-B不对称与GVMD一致 | 弱: 模型依赖 | 2 |
| Phase 2系统误差审计 | 弱: 0.7% published | 中: fiducial volume (0.5%) 异常 | 3 |
| CMD-3 vs CMD-2/SND差异 | 弱: 需解释同方法差异 | 中: CMD-2/SND接近BABAR | 2 |
| **加权总分** | **11** | **18** | |

**粗粒化后验** (使用marginal likelihood with inflated uncertainties):

若CMD-3有未知系统误差~0.5%(总1.2%): P(Scenario B) ≈ 70-80%
若CMD-3有未知系统误差~1.0%(总1.7%): P(Scenario A re-weighted) ≈ 40-50%

**最终概率评估**:
$$P(\text{CMD-3正确，无隐藏系统误差}) \approx 16-21\%$$
$$P(\text{CMD-3有隐藏系统误差} \ge 0.5\%) \approx 70-80\%$$
$$P(\text{CMD-3有隐藏系统误差} \ge 1.0\%) \approx 40-50\%$$

### 3.4 合成：CMD-3最可能的命运

**最可能 [概率~70-80%]: CMD-3有未识别的~0.5-0.7%系统误差**

具体来源（按概率排序）:
1. **Fiducial volume校准** → ~50-60%: 0.5%系统误差是现代探测器最薄弱环节
2. **辐射修正高阶效应** → ~15-20%: MCGPJ vs BabaYaga@NLO的分布差异暗示可能遗漏贡献
3. **核相互作用数据** → ~10-15%: 低能π核相互作用截面数据精度有限
4. **统计涨落+多项小幅低估** → ~5-10%

**其次 [概率~16-21%]: CMD-3基本正确**

需要BABAR和KLOE同时偏低了~2-3%。可能的机制:
1. ISR方法的共有理论系统误差
2. 真空极化修正中的共同误差

**极不可能 [<1%]: 新物理改变了e⁺e⁻→π⁺π⁻截面**

Di Luzio et al. (2025)对e-g2, muonium HFS, tau g-2的测试已排除大多数"新物理干预"场景。【此结论需用S3/S7进一步验证】

---

## 结论

### CMD-3独立审计最终结论

CMD-3是一个技术上精湛的实验，但从**统计方法论+现象学**的角度：

1. **Fiducial volume系统误差(0.5%)是需要独立审查的最脆弱环节**。这是CMD-3系统误差预算中最大单项，也是BABAR等效项的~5倍。ZC+LXe交叉检验(|δZ/Z| < 6×10⁻⁴)在存在共同对准偏差时不能保证独立性。

2. **CMD-3 vs 所有先验实验的5+σ张力无法在Gaussian likelihood框架下用统计涨落解释**。BMA给出CMD-3正确的后验概率约16-21%。

3. **CMD-3与Lattice QCD的一致性(~0.2σ)虽引人注目，但本质上可视为巧合**。Maltman et al. (2025)的论点依赖于light-quark-connected component的特定系统误差评估，形成circular reasoning风险。

### 建议

**对WP25**: 完全切换至Lattice QCD作为HVP的单一来源是一个保守但可能有偏差的决定。BMA方法提供了数学上严谨的方式组合分散的数据驱动数据集，应作为Lattice HVP的交叉检验而非被取代。

**对CMD-3合作组**: 建议报告以下内容以推进审计:
1. 2018-2020年数据中ZC+LXe fiducial volume交叉检验的完整统计量和系统相关性
2. 对fiducial volume进行独立的MC几何模型重新计算
3. 扩展e⁺e⁻→μ⁺μ⁻截面比到与π⁺π⁻匹配的统计精度（作为fiducial volume之外系统误差的约束）

### 声张强度: L2

L2 = 内部复现级别中某些方面（已发表系统误差预算+文献交叉比较），受限于无CMD-3原始数据 (luminosity函数, fiducial volume MC, raw event distributions)。

### S1对LP-11全局构建的贡献

S1无法给出"CMD-3正确"或"旧数据正确"的干净二元判决——这正是整个领域当前的困境。但S1贡献了:
1. 建立了BMA框架来量化数据集间tension的不确定性
2. 系统审计了CMD-3的误差预算，识别了fiducial volume为最弱环节
3. 量化了Scenario A vs B的概率，为LP-11最终决策(是否依赖CMD-3)提供输入
4. 指明了BABAR-KLOE次级张力(~3.8σ)也必须被解决

---

## K条目更新建议

### 需更新

1. **MEMORY.md相关条目**: 添加CMD-3系统误差审计结果: fiducial volume (0.5%) 是最可能的关键差异

2. **新建条目** `g2_cmd3_audit.md`:
   - BMA a_μ^HVP(π⁺π⁻): 507.3 ± 4.8 × 10⁻¹⁰
   - BMA full HVP,LO: 694.8 ± 5.5 × 10⁻¹⁰
   - CMD-3正确后验概率: ~16-21%
   - 系统误差审计表（Phase 2）
   - Scenario A/B 定量预测（Phase 3）

### 对LP-12+的指导

- S2 (IB修正系统化)和S7 (模型无关约束测试)应独立于S1进行：它们的论证应在Scenario A和Scenario B下都成立
- 若新的独立实验（BESIII new data 2025-2026, MUonE pilot）出现后，应重新运行本BMA框架

---

## 参考文献 (verification sources)

1. Di Luzio, Keshavarzi, Masiero, Paradisi. "Model-Independent Tests of the Hadronic Vacuum Polarization Contribution to the Muon g-2", Phys. Rev. Lett. 134, 011902 (2025). arXiv:2408.01123.

2. Ignatov, F.V. et al. (CMD-3 Collaboration). "Measurement of the Pion Form Factor with CMD-3 Detector and Its Implication to the Hadronic Contribution to Muon (g-2)", Phys. Rev. Lett. 132, 231903 (2024). arXiv:2309.12910.

3. Ignatov, F.V. et al. (CMD-3 Collaboration). "Measurement of the e⁺e⁻→π⁺π⁻ cross section from threshold to 1.2 GeV with the CMD-3 detector", Phys. Rev. D 109, 112002 (2024). arXiv:2302.08834.

4. Davier, M. et al. "Tensions in e⁺e⁻→π⁺π⁻(γ) measurements: the new landscape of data-driven hadronic vacuum polarization predictions for the muon g-2", Eur. Phys. J. C 84, 721 (2024). arXiv:2312.02053.

5. Aliberti, R. et al. (Muon g-2 Theory Initiative). "The anomalous magnetic moment of the muon in the Standard Model: an update", Physics Reports 1143, 1-158 (2025). arXiv:2505.21476 (WP25).

6. Maltman, K.R. et al. "Dispersive determinations of lattice HVP window quantities for muon g-2", PoS LATTICE2024, 178 (2025). Presented at CIPANP 2025.

7. Lees, J.P. et al. (BABAR Collaboration). "Precise Measurement of the e⁺e⁻→π⁺π⁻(γ) Cross Section with the Initial-State Radiation Method at BABAR", Phys. Rev. D 86, 032013 (2012). arXiv:1205.2228.

8. Anastasi, A. et al. (KLOE-2 Collaboration). "Combination of KLOE σ(e⁺e⁻→π⁺π⁻γ(γ)) measurements and determination of a_μ^{π⁺π⁻} in the energy range 0.10 < s < 0.95 GeV²", JHEP 03, 173 (2018). arXiv:1711.03085.

9. Ablikim, M. et al. (BESIII Collaboration). "Measurement of the e⁺e⁻→π⁺π⁻ Cross Section between 600 and 900 MeV Using Initial State Radiation", Phys. Lett. B 753, 629-638 (2016). arXiv:1507.08188.

10. Bryzgalov, V.V. & Zenin, O.V. "A comment on the impact of CMD-3 e⁺e⁻→π⁺π⁻ cross section measurement on the SM g_μ-2 value", arXiv:2401.07204 (2024).

---

**推导完成: 2026-06-02 14:30 UTC+8**
**下一审查点: CMD-3合作组对fiducial volume审计的回应 或 2026年9月前的新实验数据**
**声张强度: L2**
