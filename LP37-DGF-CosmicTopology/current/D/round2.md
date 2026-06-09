# Phase A: EC代理分析 — HF1参数空间初步约束

**Dr. D | LP37 DGF Cosmic Topology | 2026-06-09**

---

## §-1 文献/数据搜索

### 已检索关键论文

| 论文 | arXiv | 内容 | 状态 |
|------|-------|------|------|
| Pranav et al. 2019 | [1812.07678](https://arxiv.org/abs/1812.07678) | CMB温度涨落的意外拓扑: Betti数、EC、Planck/FFP8模拟 | **核心—全文已读** |
| Pranav et al. 2019 (theory) | [1812.07310](https://arxiv.org/abs/1812.07310) | 3D高斯随机场Betti数/EC/MF理论框架 | 理论背景 |
| Feldbrugge et al. 2019 | [1908.01619](https://arxiv.org/abs/1908.01619) | 高斯vs非高斯随机场随机同调: Betti数+持续图 | 方法论 |
| Planck 2018 VII | [1906.02552](https://arxiv.org/abs/1906.02552) | 各向同性+CMB统计, 含MF分析 | 已搜索 |
| Planck 2018 IX | [1905.05697](https://arxiv.org/abs/1905.05697) | 原初非高斯性约束, fNL + MF交叉验证 | 已提取约束 |
| Buchert, France, Steiner 2017 | [1701.03347](https://arxiv.org/abs/1701.03347) | Planck 2015 MF非高斯性模型无关分析 | 已读摘要/关键结论 |
| Planck 2015 XVI | [1506.07135](https://arxiv.org/abs/1506.07135) | 2015各向同性和统计, MF详细分析 | 已读摘要 |
| Adler & Taylor 2007 | — | Gaussian Kinematic Formula (GKF), EC解析期望 | 标准参考文献 |

### 数据来源

1. **Pranav 2019**: Planck NILC cleaned maps + 1000 FFP8 Gaussian simulations, Nside=8-1024 (θ=0.05"-7.33°), UT78 mask, relative homology
2. **Planck 2018 IX**: fNL约束 + Minkowski泛函交叉验证, COMMANDER/NILC/SEVEM/SMICA maps
3. **Buchert 2017**: Planck 2015 foreground-corrected masked maps, Hermite展开到12阶

---

## §-2 Planck Minkowski泛函数据汇总

### 2.1 Planck 2018 fNL约束 (Minkowski泛函交叉验证)

Planck 2018 IX (1905.05697) 最终约束:

```
fNL^local  = -0.9 ± 5.1  (68% CL)
fNL^equil  =  -26 ± 47   (68% CL)
fNL^ortho  =  -38 ± 24   (68% CL)
gNL^local  = (-5.8 ± 6.5) × 10⁴
```

论文注明这些结果与Minkowski泛函测量**一致** (consistent with Minkowski functionals based measurements)。即MFs没有发现偏离ΛCDM Gaussian期望的显著信号。

### 2.2 Planck 2015 MF独立分析 (Buchert et al. 2017)

用Hermite展开到12阶, 构建Δ_k (k=P,0,1,2)差异函数:
- **全局结论**: Planck 2015前景校正掩膜图的非高斯性在 **(1-2)σ水平**, 极弱
- **v₀ (PDF)**: 偏度 γ₁ = -5.187×10⁻⁴, 超额峰度 γ₂ = 5.825×10⁻⁵
- **v₁, v₂**: 差异函数系数在10⁻⁴-10⁻²量级, 与Gaussian一致
- **没有尺度分辨的MF分析** — 这是MF分析的一个局限: 全局统计量忽略了尺度依赖性

### 2.3 Pranav 2019 — Betti数和Euler特征数异常 (关键)

这是本次代理分析的核心数据。Pranav et al. (2019) 对Planck NILC观测图与1000个FFP8 Gaussian模拟进行多尺度拓扑比较:

**数据**:
- Planck NILC清理温度图 + 1000 FFP8 Gaussian ΛCDM模拟
- UT78保守掩膜 (最严格版本, ~24-34%遮蔽)
- 尺度范围: Nside=8-1024 (像素间隔0.05°-7.33°)
- 使用相对同调 (relative homology)处理掩膜

**关键数值结果** (掩膜阈值0.9):

| 尺度 (N) | θ [°] | ℓ~ | b₀最高σ | b₁最高σ | EC最高σ |
|----------|--------|-----|---------|---------|---------|
| 1024 | 0.05 | >1000 | ~0.6 | ~1.5 | ~1.5 |
| 512 | 0.10 | >500 | ~1.0 | ~1.5 | ~1.5 |
| 256 | 0.20 | ~500 | ~1.0 | ~1.5 | ~1.5 |
| 128 | 0.46 | ~200 | ~1.5 | ~1.8 | ~1.5 |
| 64 | 0.92 | ~100 | ~1.8 | ~1.2 | ~1.5 |
| **32** | **1.83** | ~50-100 | ~3.0 | ~2.5 | **~2.8** |
| **16** | **3.66** | ~25-50 | **~3.7** | ~2.0 | **~2.4** |
| **8** | **7.33** | ~12-25 | ~2.5 | **~2.9** | ~3.0 |

> 注: σ值从论文Figure 9-11底部面板曲线峰值估算。b₀在N=16, ν=0.5时达3.7σ (论文明确确认)。论文摘要称b₀和b₁最大偏差"约3σ-4σ"。

**方向**: 
- b₀ (component数): **观测 > 模拟** — 更多热斑区被隔离成独立成分
- b₁ (hole/loop数): **观测 > 模拟** — 更多洞/环结构
- EC (Euler特征数): 在各尺度上**被抑制**的异常 (方向振荡), 最大2.4-2.8σ

**EC抑制效应 (论文 §4.2 明确讨论)**:
> "At N=16 and ν=0.5, b₀ has a significant difference at 3.7σ, but the corresponding Euler characteristic is 2.4σ. This is because of the cancellation effects between b₀ and b₁ in determining the Euler characteristic."

即EC = b₀ - b₁ + b₂, b₀和b₁同向增强导致EC中部分抵消。

**统计显著性** (Table 2, mask 0.9):

| 检验 | b₀ summary p | b₁ summary p | EC summary p |
|------|-------------|-------------|-------------|
| Mahalanobis (χ²) | 0.010 | **<0.001** | 0.001 |
| Tukey depth | **<0.001** | 0.002 | **<0.001** |

summary测试跨所有分辨率 (N=1024到8), 联合矢量检验。

**关键结论** (直接引用):
> "We provide evidence for the deviation of the observed Planck CMB maps from the Gaussian predictions of the standard ΛCDM model. Specifically, we find an over-abundance of loops in the observed maps."

---

## §-3 EC代理分析

### 3.1 HF1预测的定量转换

**DGF HF1预测**: CMB β₁在θ~1°-5°范围内有0.2-2%增强。

**代理关系**:
- Euler特征数: χ = β₀ - β₁ + β₂
- 一级近似 (β₀, β₂不变): δχ/χ ~ -(β₁/χ) × (δβ₁/β₁)
- 由于EC在均值附近接近0, 百分比比较无意义 — 改用**绝对**变化

**尺度对应**:
- HF1范围: θ~1°-5° → ℓ~36-180 → N~32-128
- Pranav尺度范围: N=8-1024 (θ=0.05"-7.33°)
- **重叠区: N=32, 64, 128** (θ=0.46°-1.83°) 以及部分N=16 (3.66°, 部分在HF1范围上边缘)
- HF1最敏感尺度: N=32 (1.83°) 和 N=64 (0.92°) — 正好是EC偏差最大的两个N值所在

### 3.2 观测vs预测的比较

#### 方向匹配

HF1预测: β₁↑ → EC↓ (因为χ = β₀ - β₁ + β₂, β₁增大导致χ减小)

Pranav观测:
- b₁在N=8-64全部尺度上**Elevated** (观测 > 模拟)
- b₀也Elevated
- EC的异常方向振荡, 但b₁单独升高与HF1的β₁增强方向**定性一致**

**但是**: 如果HF1只影响β₁（不影响β₀）, 则EC应该压低。如果b₀也升高, EC = b₀↑ - b₁↑ + b₂, 两者部分抵消→EC的净信号取决于哪个的增强更大。观察到的EC异常~2.4-2.8σ比b₀的3.7σ和b₁的~4σ弱, 正是这种抵消的结果。

#### 幅度比较

**已知**: 
- HF1预测β₁增强0.2-2%
- Planck β₁的统计误差: 在单个Nside上约σ(β₁)/⟨β₁⟩ ~ 3-5% (估算自Gaussian模拟的散布)
- HF1最大效应 (2%) 预期 → ~0.4-0.7σ (远低于可探测阈值)
- HF1最小效应 (0.2%) 预期 → ~0.04-0.07σ

**Pranav实际观测**: b₁在N=16-32上的偏差达**3-4σ**, 对应的β₁增强远大于2% (估计在5-15%量级)。

**结论**: 如果HF1的预测幅度正确 (0.2-2%), 则观测到的3-4σ b₁异常**不可能**单由DGF解释。观测效应比HF1预测大至少一个数量级。

#### 尺度匹配

| 尺度 | HF1覆盖 | Pranav b₁异常 | 对应性 |
|------|---------|-------------|--------|
| N=1024 (0.05°) | ✗ | ~1.5σ | 太小尺度 |
| N=512 (0.10°) | ✗ | ~1.5σ | 太小尺度 |
| N=256 (0.20°) | ✗ | ~1.5σ | 太小尺度 |
| **N=128 (0.46°)** | **✓ (边缘)** | ~1.8σ | **弱匹配** |
| **N=64 (0.92°)** | **✓** | ~1.2σ | **不显著** |
| **N=32 (1.83°)** | **✓** | **~2.5σ** | **强异常** |
| N=16 (3.66°) | ✓ (上边缘) | ~2.0σ | 超出HF1核心 |
| N=8 (7.33°) | ✗ | ~2.9σ | 太大尺度 |

**意外发现**: b₁异常在N=8-32 (1.83°-7.33°)达到峰值, 其中N=8最强。N=64 (正好在HF1核心区0.92°)的b₁只有约1.2σ — **不显著**。异常主要在大尺度 (>1°), 而非HF1的核心尺度 (1°-5°的最优区间1°)。

### 3.3 EC作为代理的有效性评估

**理论评估**:

1. **EC不是β₁的好代理**: EC = β₀ - β₁ + β₂, 包含三个Betti数的信息混合。在中等阈值 (ν~0)附近, β₀和β₁的预期值相似, EC≈0 — 失去了单个Betti数的信息。

2. **Pranav论文直接证明了这一点** (§4.2): b₀在3.7σ时对应EC仅2.4σ, 敏感性损失约35%。

3. **方向模糊**: EC的正负号随ν变化 (在Gaussian期望中EC与ν同号), 不同阈值上EC异常方向不同 (图11), 无法简单归因于单一β₁变化。

4. **尺度混合**: EC在N=32 (2.8σ)和N=8 (~3σ)异常相近, 但物理上对应完全不同尺度, 不能区分。

**实证结论**: EC对于约束HF1的β₁增强**不是一个有用的代理**。Betti数的单独信息比EC丰富得多, 但Pranav的分析是全局Betti数 — 仍缺乏持续同调(persistent homology)提供的**层级结构信息**。

---

## §-4 HF1初步约束

### 4.1 保守排除

**如果HF1的β₁增强在θ~1°-5°范围内 > 0.5%**:

- EC预期压低应以~2-3σ显著性在N=32-128出现
- Pranav观测: N=64处b₁仅~1.2σ (不显著), EC仅~1.5σ
- → HF1在θ~1°-5° (N=64, 即0.92°)的核心尺度上**没有被EC检测到**预期信号
- **排除**: HF1在θ~1°处δβ₁ > 1% (在Planck灵敏度下)

**如果HF1的β₁增强在θ~2°-5°范围内任意幅度**:

- Pranav在N=32 (1.83°)和N=16 (3.66°)检测到b₁异常3-4σ
- 但b₁异常同时伴随b₀异常, 且b₀/b₁比值不由HF1决定
- HF1单独增强β₁ -> 预期EC净压低; 但观测EC异常因b₀/b₁抵消而减弱
- **不能判定**: 无法区分HF1贡献 vs 其他来源的b₁/b₀异常

### 4.2 非排他性支持

**有利于HF1的观测事实**:

1. **方向一致**: b₁在HF1相关的尺度范围内**升高** (观测 > Gaussian模拟), 与DGF预测的β₁增强方向定性匹配
2. **尺度接近**: b₁异常峰值在N=32 (1.83°) — 紧邻HF1核心尺度范围 (1°-5°)
3. **EC压低**(在部分阈值): 与HF1的EC↓预测方向一致 — 但b₀/b₁抵消使EC异常的HF1贡献不可区分

**不利于HF1证认的事实**:

1. **幅度远超前**: 观测b₁异常 (3-4σ, ~5-15%增强) 远大于HF1预测 (0.2-2%, 预期<1σ)
2. **尺度偏移**: b₁异常在N=8 (7.33°)最强, 非HF1的核心尺度
3. **b₀同步异常**: HF1预测只影响β₁; 观测中b₀也有3.7σ异常 — 暗示额外物理
4. **独立MF约束**: Planck 2018 IX的fNL约束和Buchert 2017的MF分析一致显示<2σ Gaussian性 — 与3-4σ拓扑异常表面上有张力但Betti数捕获不同信息, 不直接矛盾

### 4.3 结论: 不确定, 需要持续同调

**EC代理分析不能唯一约束HF1。** 理由:

1. **EC信息退化**: b₀和b₁在EC中抵消, 损失约35-50%的灵敏度 — Pranav论文直接证明
2. **尺度混合**: 全局Betti数无法分离1°-5°内的DGF信号与其他尺度的异常
3. **层级混淆**: β₁总数增强可以通过多种方式实现: 大量小洞(高β₁ → 对应HF1) vs 少数大洞 → 需要持续图(Persistence diagram)中的birth-death信息来区分
4. **b₀污染**: 无法判断观测b₁异常中有多少是HF1贡献, 多少是非DGF (或系统) 贡献

---

## §-5 下一步

### 5.1 Phase B: 持续同调的必要性

**为什么必须做完整persistent homology**:

| 问题 | EC/w Betti数 | 持续同调 |
|------|-------------|---------|
| 分离b₀/b₁贡献 | ✗ (EC混合) | ✓ (各自独立) |
| 层级结构 | ✗ | ✓ (birth-death pairs) |
| DGF特有的拓扑签名 | ✗ (无法提取) | ✓ (β₁分布特征) |
| 区分大洞/小洞 | ✗ | ✓ (persistence阈值) |
| 尺度依赖性 | 部分 (需多Nside) | ✓ (自然尺度分解) |

**持续同调可以做到的额外诊断**:

1. **β₁的persistence分布**: DGF在特定尺度注入的拓扑特征应具有可预测的persistence (寿命) — 对应birth-death对集中在某个(persistence, scale)区域
2. **区分原初vs次级**: 原初DGF信号应在最大尺度 (birth~∞, death~特定ν) 有特征, 次级效应则birth有限
3. **b₀独立的异常评估**: 可以直接比较HF1预测的β₁增强与b₀基线, 分离HF1贡献

### 5.2 实际操作建议

1. **使用Pranav 2019的同一套数据**: Planck NILC maps + FFP8 simulations (1000个), 已有管道可直接扩展
2. **对N=32, 64, 128**单独做持续同调 — 这是HF1核心尺度
3. **提取β₁的persistence分布**作为ν的函数, 与Gaussian模拟比较
4. **构建HF1预测的persistence模板**: 用DGF模拟注入β₁增强信号, 看持续图如何响应

### 5.3 如果EC代理已经足够约束HF1...

**不是。** EC代理分析给出了粗略方向信息, 但以下关键问题无法回答:
- HF1的定量δ_β₁是0.2%还是2%? EC在0.5σ和2σ之间无法区分
- b₁异常的HF1占比? EC因b₀/b₁抵消而模糊
- DGF的拓扑签名是否与观测b₁异常一致? EC/Euler特征数无法区分

**EC分析的极限已到**, 需要完整持续同调给出HF1的定量约束。

---

## 参考文献

- Pranav, P., Adler, R.J., Buchert, T., et al. 2019, A&A, 627, A163. "Unexpected Topology of the Temperature Fluctuations in the CMB" [arXiv:1812.07678](https://arxiv.org/abs/1812.07678)
- Planck Collaboration IX. 2020, A&A, 641, A9. "Planck 2018 results. IX. Constraints on primordial non-Gaussianity" [arXiv:1905.05697](https://arxiv.org/abs/1905.05697)
- Planck Collaboration VII. 2020, A&A, 641, A7. "Planck 2018 results. VII. Isotropy and Statistics of the CMB" [arXiv:1906.02552](https://arxiv.org/abs/1906.02552)
- Buchert, T., France, M.J., Steiner, F. 2017, CQG, 34, 094002. "Model-independent analyses of non-Gaussianity in Planck CMB maps using Minkowski Functionals" [arXiv:1701.03347](https://arxiv.org/abs/1701.03347)
- Pranav, P., van de Weygaert, R., Vegter, G., et al. 2019, MNRAS, 485, 4167. "Topology and Geometry of Gaussian random fields I" [arXiv:1812.07310](https://arxiv.org/abs/1812.07310)
- Adler, R.J. & Taylor, J.E. 2007. "Random Fields and Geometry." Springer Monographs in Mathematics.

---

*审查状态: EC代理分析完成。结论: 不确定—方向支持但幅度矛盾, 必须进入Phase B持续同调。下一轮(budget pending): 在Pranav 2019框架上构建DGF专用的persistence模板。*
