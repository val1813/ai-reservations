# Dr. D -- Round 1: CMB Persistent Homology Feasibility Assessment for DGF HF1

**Date:** 2026-06-09
**Role:** Computational Astrophysicist
**Task:** Assess feasibility of computing persistent homology on Planck CMB data to test DGF's HF1 prediction of β₁ enhancement at 1°-5° scales.

---

## §-1 文献和数据搜索 (Literature and Data Search)

### 搜索策略

执行了7项覆盖性搜索：
1. Planck 2018 CMB maps (SMICA/Commander/NILC/SEVEM) download sources
2. Planck PR4/NPIPE 2025最新release
3. Persistent homology + CMB文献 (Python/GUDHI/Ripser)
4. Euler characteristic + non-Gaussianity + Planck偏差
5. CMB + topological data analysis + β₁ suppression/enhancement
6. DGF理论 + CMB persistent homology交叉
7. 自发补充搜索：代码仓库、数据镜像、复现/反驳文献

### 数据源确认

**Planck 2018 CMB Maps (PR3):**
- 官方release: ESA Planck Legacy Archive (PLA)
- URL: `http://pla.esac.esa.int/pla/#maps`
- 4张独立component-separation图: SMICA, Commander, NILC, SEVEM
- 分辨率: Nside=2048 (~50M像素), 5 arcmin FWHM
- 文件大小: ~0.6 GB (I-only), ~1.9 GB (IQU full)
- 文件名: `COM_CMB_IQU-{method}_2048_R3.00_full.fits`
- Common mask: `COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits`

**Planck PR4/NPIPE (2025/最新):**
- 检索到NPIPE maps referenced但未找到正式PR4 CMB likelihood release
- BeyondPlanck Bayesian分析 (Galloway et al. 2022, A&A) 提供了Commander3全Bayesian pipeline
- PR3 (2018) 仍是标准的CMB分析数据集，PR4主要影响极化/lensing

**FFP10 Simulations:**
- 1000个lensed scalar CMB realizations
- 可通过NERSC (`/global/cfs/cdirs/cmb/data/planck/`) 或PLA获取
- 仅300个含噪声realization（已知限制）
- ΛCDM best-fit参数: h=0.6702, Ω_b h²=0.02217, n_s=0.9637

### DGF + CMB Persistent Homology文献

**搜索结果: 零。** 使用"DGF dynamic gravitational field theory" + "persistent homology" + "CMB" + "Betti" + "cosmic topology"的任何组合均无已发表文献。HF1是关于DGF理论在CMB persistent homology上的纯理论预测，此前未被任何独立组检验。

---

## §-2 可行性评估 (Feasibility Assessment)

### 2.1 角尺度和分辨率对应

DGF HF1预测的目标尺度: θ = 1°-5° (arcmin: 60-300 arcmin)

| Nside | 像素数 | 像素尺度 | 1°特征采样 | 5°特征采样 | 可行性 |
|-------|--------|----------|-----------|-----------|--------|
| 128 | 196,608 | 27.5 arcmin | ~2.2 px | ~10.9 px | 勉强足够 (仅为2x采样) |
| 256 | 786,432 | 13.7 arcmin | ~4.4 px | ~21.9 px | 可接受 |
| 512 | 3,145,728 | 6.9 arcmin | ~8.7 px | ~43.6 px | 良好 |
| 1024 | 12,582,912 | 3.4 arcmin | ~17.5 px | ~87.3 px | 优秀 (但计算代价高) |

**结论:** Nside=256是1°-5°分析的最低可行分辨率。Nside=512在计算可行性和分辨率之间取得最佳平衡。Nside=1024是可取的但需要工作站级硬件。

Aurich & Steiner (2024) 使用Nside=128 + 120 arcmin (2°) Gaussian平滑——这主要探测≥2°的尺度，对于HF1的1°-5°范围而言过于粗糙。**要检验HF1，需要比Aurich & Steiner更高的分辨率。**

### 2.2 计算复杂度

**Persistent homology on 2D excursion sets on the sphere:**

方法1: Cubical complex (Ripser/GUDHI cubical)
- 将HEALPix投影到2D网格 → 引入投影畸变
- Cubical Ripser可处理4M+像素2D图像 ~16-32 GB RAM
- Nside=512 → 3.1M像素 → 可行
- Nside=1024 → 12.6M像素 → 需要64+ GB RAM或分布式

方法2: 球面三角剖分 + Vietoris-Rips/Alpha complex
- 直接在HEALPix球面上构建simplicial complex
- 复杂度更高（非平面拓扑）
- 需要自定义实现

方法3: 直接计数法 (Aurich & Steiner 2024 approach)
- 对每个ν阈值计算excursion set的β₀, β₁
- β₀: Union-Find → O(N log N)，简单
- β₁: 需要homology计算，但Nside=128 (196K像素) 在常规硬件上可行
- 此方法本质上是persistent homology (superlevel set filtration)

**实用估计:**

| Nside | 像素数 | β₀计算 | β₁计算 (cubical) | 所需RAM | 典型时间 |
|-------|--------|--------|-------------------|---------|---------|
| 128 | 196K | 秒级 | 秒-分钟级 | <4 GB | 分钟 |
| 256 | 786K | 秒-分钟级 | 分钟级 | 4-8 GB | 10-30分钟 |
| 512 | 3.1M | 分钟级 | 10-60分钟 | 16-32 GB | 1-3小时 |
| 1024 | 12.6M | 10-30分钟 | 数小时 | 64+ GB | 0.5-1天 |

以上估计基于单张图的计算。完整分析需要:
- 4张Planck图 × N个mask处理 = 4组
- 1000个ΛCDM模拟 × Nside=分辨率 = 1000组

**关键瓶颈:** 1000个模拟的persistent homology计算。对于Nside=512，每个模拟需要1-3小时 → 1000-3000 CPU小时。这在单个工作站上需要1-4个月连续计算。

**但是:** 可以大大加速——
1. 仅使用β₀和β₁（不需要β₂），大幅简化
2. 使用Nside=256进行初始探索（<100 CPU小时）
3. FFP10模拟不需要自己跑——可以直接下载成品图
4. 仅对关键ν范围（均值附近，|ν|<2）进行精细计算

### 2.3 软件成熟度

| 工具 | 成熟度 | 适用性 | 球面支持 |
|------|--------|--------|---------|
| **GUDHI** | 成熟 (Inria, C++/Python) | 良好 | 需要2D投影 |
| **Cubical Ripser** | 成熟 (C++, R wrapper) | 优秀 | 需要2D投影 |
| **Dionysus** | 成熟 | 一般 | 需要适配 |
| **giotto-tda** | 成熟 (Python) | 一般 | 无直接支持 |
| **PixHomology** | 2024新工具 (分布式) | 仅β₀ | 需要适配 |
| **healpy** | 成熟 | 辅助 (需要) | 原生球面支持 |

**关键问题:** 没有现成的、公开的CMB persistent homology pipeline。Pranav et al. (2019) 的代码未公开发布。Aurich & Steiner (2024) 的Betti functional代码也未公开。

**需要自建pipeline:** healpy读取FITS → 降分辨率 → Gaussian平滑 → 应用mask → 计算superlevel set filtration → 提取Betti curves → 统计比较。这不是不可能，但需要1-2周开发+调试。

### 2.4 已有公开代码/结果

通过广泛搜索，**未找到**完整的CMB persistent homology公开代码。相关但限制使用的资源:
- Aurich & Steiner (2024) 使用healpy + 自写计数代码 (Nside=128)
- Pranav et al. (2019) 使用自定义C++代码 + DIPHA
- rcosmo R包可下载Planck数据但不含topology分析

---

## §-3 分析方案设计 (Analysis Plan)

### 如果执行：推荐的两阶段方案

#### Phase A: 快速侦察 (1-2周)

**目标:** 确认基本可行性，与已知结果交叉验证

1. **数据准备:**
   - 下载Planck 2018 SMICA, Commander, NILC, SEVEM (I-only, ~0.6 GB each)
   - 使用healpy降分辨率到Nside=128, 256, 512
   - 应用common mask, 去monopole+dipole, Gaussian平滑

2. **基准验证 (Nside=128, 120 arcmin平滑):**
   - 复现Aurich & Steiner (2024) Fig. 11-12的Planck Betti curves
   - 目标: 确认我们的pipeline产出与已发表结果一致

3. **扩展到Nside=256/512:**
   - 对所有4张图计算β₀(ν), β₁(ν)
   - 使用已有的100个FFP10模拟进行初步比较
   - 报告β₁在ν≈0 (均值附近)的值 vs ΛCDM期望

4. **HF1特异性分析:**
   - 在1°-5°对应angular scales上提取β₁信号
   - 使用band-pass filter隔离目标尺度
   - 量化β₁增强百分比 vs ΛCDM

#### Phase B: 完整统计分析 (4-8周)

**目标:** 用1000模拟+4张图给出统计显著性

1. 下载并处理1000个FFP10 CMB realizations
2. 对Nside=256和512各计算persistent homology
3. 对每个ν值构建β₀, β₁的经验分布
4. 计算观测值的p-value, χ², 和σ偏差
5. 特别报告β₁(ν≈0)在1°-5°尺度的行为
6. 产出: β₁ enhancement百分比 ± 1σ, 2σ置信区间

### 资源需求

| 项目 | Phase A | Phase B |
|------|---------|---------|
| 计算时间 | ~50 CPU-hr | ~2000-3000 CPU-hr |
| 存储 | ~50 GB | ~500 GB |
| 开发时间 | 1-2周 | 3-4周 |
| 硬件要求 | 32 GB RAM工作站 | 64+ GB RAM或集群 |

---

## §-4 文献已有结果汇总 (Literature Results Summary)

### 4.1 Pranav et al. (2019) — "Unexpected Topology of the Temperature Fluctuations in the CMB"

- **发表:** Astronomy & Astrophysics, 627, A163 (2019年7月)
- **DOI:** 10.1051/0004-6361/201834916 | **arXiv:** 1812.07678
- **引用数:** 31 (CrossRef, 截至2026年6月)
- **作者:** Pranav, Adler, Buchert, Edelsbrunner, Jones, Schwartzman, Wagner, van de Weygaert
- **机构:** ENS Lyon, Technion, IST Austria, UCSD, Kapteyn Institute

**核心方法:**
- 对Planck CMB温度图计算persistent homology (superlevel set filtration)
- 与1000个ΛCDM Gaussian模拟比较
- 多尺度分析: 降分辨率序列，像素分离0.05°到7.33°
- 引入"relative homology"概念处理mask

**主要发现:**

| 量 | 偏差 | 尺度 | 显著性 |
|----|------|------|--------|
| β₀ (连通分量数) | 观测 > 模拟 | 3°-7° | 3σ-4σ, p = 0.01-0.001 |
| β₁ (拓扑空洞数) | 观测 > 模拟 | 3°-7° | 3σ-4σ, p = 0.01-0.001 |
| χ²参数检验 | 整体偏离 | 2°-7° | p = percent到permil级 |

**关键声明:**
1. 异常在Planck和WMAP之间一致 → 排除仪器系统误差
2. 异常尺度与功率谱dip和低方差区域吻合
3. **Gaussian模拟即使匹配观测功率谱的dip也不能消除异常** ← 这是最关键的点
4. 可能解释: 原初非高斯性 或 非平凡拓扑 (如拓扑缺陷模型)
5. 报告的Euler characteristic异常与之前WMAP的3.66°异常现象学相关

**对HF1的相关性:**
- 直接证明了β₁在观测CMB中偏离ΛCDM Gaussian预期
- 但最强信号在3°-7°，不是HF1预测的1°-5°
- 偏差幅度(3-4σ, 相当于>5%偏差)远大于HF1预测的0.2-2%
- Pranav的结果是"gross anomaly"级别的，不是subtle modulation

### 4.2 Aurich & Steiner (2024) — "Betti Functionals as Probes for Cosmic Topology"

- **发表:** Universe, 10(5), 190 (2024年4月)
- **DOI:** 10.3390/universe10050190 | **arXiv:** 2403.09221
- **作者:** Ralf Aurich, Frank Steiner (Ulm University)
- **机构:** Ulm大学理论物理研究所

**核心方法:**
- 使用Betti functionals β₀(ν), β₁(ν), β₂(ν) + Euler characteristic χ(ν)
- 分析cubic 3-torus宇宙模型 (有限体积，边长L = 0.5-3.0 Hubble长度)
- 分辨率: Nside=128, FWHM=120 arcmin (2° Gaussian平滑)
- 1000 CMB模拟 per torus size
- 与4张Planck 2018图 (SMICA/Commander/NILC/SEVEM) 比较
- 开发了mask处理方法: β_min和β_max上/下界

**主要发现:**
1. β₀和β₁的振幅随torus体积增大而**单调递减**
2. 4张Planck图的Betti curves几乎完全重叠 → 排除component-separation artifacts
3. **Planck图落在L=2.0和L=3.0 torus之间**，且在无限ΛCDM之上
4. **结论:** "a further hint that the Universe has a non-trivial topology"
5. 建立了β₁和ρ (CMB梯度场的归一化标准差) 之间的分析关系
6. 报告了parity violation α₀(ν)的首次计算
7. 引用了一篇"in preparation"的companion paper: **Pranav, Aurich, Buchert, France, Steiner (2024)** — 更全面地使用relative homology比较有限vs无限宇宙模型

**对HF1的相关性:**
- 确认了Planck Betti functionals系统地高于无限ΛCDM预期
- 但使用的分辨率(Nside=128, 2°平滑)不能很好地解析1°-5°尺度
- 他们的物理解释(有限torus宇宙)与DGF完全不同
- 如果Planck Betti数被证实高于ΛCDM，那么任何能解释此异常的模型(DGF或torus)都会得到部分支持
- 但Nside=128的粗糙分辨率意味着**不能直接提取HF1预测的1°-5°精细信号**

### 4.3 其他相关文献

1. **Buchert, France & Steiner (2017, CQG 34, 094002):** Minkowski functionals formalism for CMB — 为Aurich & Steiner 2024提供数学基础
2. **Aurich, Buchert, France & Steiner (2021, CQG 38, 225005):** CMB温度梯度方差作为multiply connected Universe的signature——ρ参数分析
3. **Kanafi, Ansarifard & Movahed (2023, arXiv:2311.13520):** 大尺度结构(LSS)的persistent homology + neutrino mass探测。证明此方法可约束宇宙学参数，M_ν不确定性达0.0152 eV (1σ, 对matter field)。虽然不直接涉及CMB，但展示了persistent homology对宇宙学参数constrain的能力。
4. **Pranav (2022, A&A 659, A115):** 关于persistent homology在宇宙学中的综述/方法论论文
5. **Torres (1994, ApJL 423, L9):** COBE-DMR CMB maps的拓扑分析——CMB拓扑研究的先驱工作

### 4.4 文献独立性评估

**核心问题: 是否有独立组复现或反驳了Pranav 2019的结果？**

- 经过广泛搜索，**未找到**任何独立组对Pranav et al. (2019)的完整复现或直接反驳
- Aurich & Steiner (2024) 部分确认了Betti functionals的异常行为，但方法和解释均不同
- 31次引用(CrossRef)中，大部分是方法论引用，非独立复现
- **这是一个显著的gap: 2019年的3-4σ CMB anomaly迄今未被独立验证**

---

## §-5 对HF1的裁决 (Judgment on HF1)

### 5.1 HF1预测概况

DGF HF1预测: CMB温度图的persistent homology中，β₁在θ~1°-5°尺度上有0.2-2%的增强（相对于ΛCDM Gaussian随机场的预期）。

### 5.2 当前数据能否检验HF1？

**能，但有重要限定条件。**

**可以检验的原因:**
1. Planck 2018数据公开可用（4张独立component-separation图）
2. FFP10模拟（1000 realization）公开可用
3. Persistent homology计算在Nside=256-512分辨率上技术上可行
4. 已有Aurich & Steiner (2024)的方法可以作为起点

**限定条件:**

| 问题 | 严重程度 | 说明 |
|------|---------|------|
| 无公开pipeline | 中等 | 需要1-2周开发 |
| 统计需求高 | 严重 | 0.2-2%效应需要~5000-10000模拟才能达到3σ |
| 与已知异常重叠 | 严重 | Pranav 2019的3-4σ异常 (3°-7°) 可能掩盖HF1的subtle 1°-5°信号 |
| 尺度分辨率张力 | 中等 | 1°尺度需要Nside≥512，计算代价高 |
| 球面拓扑复杂性 | 中等 | HEALPix球面→2D网格投影引入系统误差 |
| DGF无先例 | 低 | 这恰好是创新点 |

### 5.3 HF1预测vs已观测异常的对比

这是本报告最关键的分析:

| 特征 | HF1预测 | Pranav 2019观测 | 一致性 |
|------|---------|-----------------|--------|
| β₁行为 | 增强 (0.2-2%) | 增强 (3-4σ, >>2%) | 定性一致，定量不符 |
| 尺度 | 1°-5° | 3°-7° (峰值) | 部分重叠 |
| 显著性 | Subtle (需要大量统计) | Gross anomaly (1000模拟已可见) | 量级不同 |
| ν依赖性 | ν≈0 (均值附近) | 全曲线χ²异常 | 未专门测试 |
| β₀行为 | DGF预测β₀抑制? | Pranav观测β₀增强 | 可能矛盾 |
| 物理来源 | DGF修正引力 | 原初非高斯性/非平凡拓扑 | 完全不同 |

**关键张力:**
- HF1预测β₁增强0.2-2%，但Pranav观测到的是远远更大的效应
- 如果Pranav的3-4σ异常是真实的，HF1的0.2-2% modulation可能会被淹没
- 如果Pranav的异常**部分**来自DGF效应，那DGF的β₁增强就应该远大于0.2-2%，需要HF1修正

### 5.4 建议的行动路线

**路线A: 计算型 (最直接，成本高)**
1. 开发CMB persistent homology pipeline (2周)
2. 在Nside=256上运行Phase A侦察 (1周)
3. 如果发现与Pranav/Aurich一致 → 在Nside=512上运行Phase B (4周)
4. 提取1°-5° scale的β₁信号
5. 产出: 观测β₁ enhancement百分比 ± 误差

**路线B: 文献型 (成本低，产出有限)**
1. 联系Pranav/Aurich团队询问原始数据和/或代码
2. 如果他们已计算了1°-5°尺度的β₁ (但未在论文中展示)，直接获取结果
3. 使用他们的Betti curves重新分析HF1预测
4. 写评论文章将已有结果映射到HF1参数空间

**路线C: 代理检验 (折中)**
1. 使用Euler characteristic χ(ν)或Minkowski functionals作为proxy
   - χ(ν) = β₀ - β₁ + β₂
   - Minkowski functionals已有成熟的Planck分析
2. 从Planck的Minkowski functional分析中提取1°-5°尺度的约束
3. 估算β₁ enhancement的上限
4. 论证该上限是否与HF1的0.2-2%兼容

### 5.5 最终裁决

**对于"当前数据+公开工具能否检验HF1":**

```
裁定: 条件可行 (Conditionally Feasible)
置信度: 75%

可行理由:
  + 数据和模拟均已存在
  + 计算方法已成熟 (Cubical Ripser + healpy)
  + 已有Pranav和Aurich的两组独立Betti functional分析可作交叉验证
  + Nside=256的分辨率足以解析1°-5°特征

不可行理由:
  - 0.2-2%效应太小，需要10000+模拟的统计量 (现有仅1000 FFP10)
  - 没有现成pipeline，自建需要显著开发投入
  - Pranav的3-4σ异常 (大效应) 在相邻尺度上可能混淆subtle DGF信号
  - 即使计算出的β₁与ΛCDM相比有差异，也无法区分DGF效应 vs 其他非标
    准物理 (原初非高斯性、torus拓扑、 foreground residuals)
```

**底线:** HF1**原则上可以被检验**，但实际操作需要:
1. 至少2-3个月的全职工作（含开发+计算+分析）
2. 足够计算资源（64+ GB RAM工作站或小型集群）
3. 创新的统计方法来隔离0.2-2% subtle signal from the 3-4σ gross anomaly
4. 与Pranav/Aurich团队的沟通以避免重复工作

如果团队决定推进，我建议从**路线C (代理检验)** 开始，使用已有Euler characteristic/Minkowski functional结果估算HF1参数空间，然后再决定是否投入路线A的全规模计算。

---

## 附录: 关键资源和链接

### 数据下载
- Planck 2018 CMB maps: http://pla.esac.esa.int/pla/#maps
- FFP10 simulations: https://wiki.cosmos.esa.int/planck-legacy-archive/index.php/Simulation_data
- Common mask: `COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits`

### 软件
- healpy: https://healpy.readthedocs.io/
- GUDHI: https://gudhi.inria.fr/
- Cubical Ripser: https://github.com/CubicalRipser
- rcosmo (R): https://github.com/frycast/rcosmo

### 关键论文
- Pranav et al. 2019: https://doi.org/10.1051/0004-6361/201834916 | arXiv: 1812.07678
- Aurich & Steiner 2024: https://doi.org/10.3390/universe10050190 | arXiv: 2403.09221
- Buchert, France & Steiner 2017: https://doi.org/10.1088/1361-6382/aa5ce2 | arXiv: 1701.03347
- Kanafi et al. 2023: arXiv:2311.13520 (LSS persistent homology)
- Torres 1994: https://doi.org/10.1086/187223 (先驱CMB topology)
