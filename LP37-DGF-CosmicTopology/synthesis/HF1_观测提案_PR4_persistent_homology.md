# HF1观测提案：Planck PR4 Persistent Homology @ 1-5°

**提案编号:** LP37-HF1-PR4-001
**日期:** 2026-06-09
**状态:** 可立即执行 — 所有数据、软件公开可用
**预计工时:** 3-5周（单人全职）

---

## 一、科学问题

DGF预测：CMB温度涨落的persistent homology中，β₁（1维Betti数/环结构）在1-5°尺度上有**0.2-2%的增强**，同时β₀（连通分量）在该尺度上**被抑制**。

现有唯一CMB persistent homology分析（Pranav et al. 2019, A&A 627, A163）在3-7°尺度发现β₁的4.5σ异常——方向与DGF一致但幅度（~10%）远超DGF预测（≤2%），且β₀也增强（与DGF的β₀抑制预测矛盾）。该分析使用Planck 2015 SMICA图，Nside=128。

**本提案要回答的问题：** 在DGF的预测尺度（1-5°），使用更新的Planck PR4数据，β₁是否增强了0.2-2%？β₀是否被抑制？

---

## 二、数据和软件

### 2.1 CMB数据

| 项目 | 详情 |
|------|------|
| 数据集 | **Planck PR4 (NPIPE)** — 2025年发布，最高信噪比CMB图 |
| 成分分离图 | SMICA, Commander, NILC, SEVEM（四张独立图用于交叉验证） |
| 分辨率 | Nside=512（像素~6.9 arcmin，远高于1°需求）→ 降采样至Nside=256用于计算 |
| 下载地址 | [ESA Planck Legacy Archive](https://pla.esac.esa.int/) → PR4 → Intensity maps |
| 文件格式 | FITS (HEALPix), ~300MB/图 @ Nside=512 |
| 掩模 | Planck PR4 common temperature mask (f_sky~0.8) + 点源掩模 |

### 2.2 ΛCDM模拟（对照样本）

| 项目 | 详情 |
|------|------|
| 模拟集 | Planck FFP10.1 CMB-only simulations（PR4配套） |
| 数量需求 | **至少5000个**（DGF 2%效应需要~0.2%统计精度 → 1/√5000 ≈ 1.4%） |
| 下载地址 | NERSC / ESA PLA → FFP10.1 CMB realizations |
| 格式 | FITS, 同数据格式 |
| 注 | 若FFP10.1不可获取，使用WebSky或PySM生成的Gaussian CMB模拟作为替代 |

### 2.3 软件

| 工具 | 用途 | 版本/来源 |
|------|------|---------|
| **healpy/healpix** | HEALPix球面数据处理 | `healpy` (pip) 或 HEALPix (F90) |
| **GUDHI** | Persistent homology计算 | [gudhi.inria.fr](https://gudhi.inria.fr/) v3.9+ |
| **Cubical Ripser** | 2D立方复形persistent homology | `ripser` Python 包 |
| **numpy/scipy** | 数值计算 | 标准科学Python栈 |

---

## 三、方法论

### 3.1 球面patch提取

从HEALPix全天地图中提取**等面积球面patches**，覆盖1-5°的角尺度范围：

| 参数 | 值 | 理由 |
|------|-----|------|
| Patch数 | 200-400 | 覆盖全天(~80% after mask)，平衡统计精度和计算成本 |
| Patch形状 | 10°×10° 切向投影 | 对应Nside=256时~150×150像素 |
| Patch位置 | HEALPix Nside=8 像素中心 | 均匀覆盖天球，避免重叠 |
| 投影 | Gnomonic (TAN) | 保留局部角度，失真有界(~1% at edge) |

**关键检查：** patch边界效应。10° patch内1-5°的特征有≥2°的边界缓冲，边界效应可忽略。

### 3.2 Persistent Homology计算

对每个patch计算**cubical persistent homology**（2D灰度图的superlevel set filtration）：

```
输入: 10°×10° CMB patch, Nside=256 → ~150×150 pixels
方法: cubical complex, superlevel set filtration
      阈值 ν = (T - <T>)/σ_T 从 +4 到 -4, 步长 0.1
输出: persistence diagram (birth, death) for β₀ and β₁
```

**具体步骤：**
1. 对patch进行3×3 Gaussian平滑（σ=0.5 pixel ≈ 2 arcmin，远小于1°信号尺度）
2. 构建superlevel set: {pixels: T(p) ≥ ν}
3. 用Cubical Ripser/GUDHI计算persistent homology
4. 提取persistence = death - birth，保留persistence > 0.5σ（滤除噪声）
5. 记录β₀(ν)和β₁(ν)曲线

### 3.3 尺度分离

关键操作：**只统计等效角尺度在1-5°范围内的环。**

方法：对每条persistent bar (birth, death)，其对应的拓扑特征的空间尺度为：
$$\theta_{\text{feature}} \approx \frac{\text{pixel\_size}}{\sqrt{|N_{\text{pixels}}|}}$$

其中N_pixels是形成该特征的像素数（从cubical complex的filtration index反推）。

或更简单地：对每个β₁的persistent bar，计算其"代表环"（representative cycle）的像素数N，检查是否满足：
$$1^\circ \leq \theta_{\text{pixel}} \cdot \sqrt{N} \leq 5^\circ$$

在Nside=256下，θ_pixel ≈ 0.23°。1°≈ 19像素，5°≈ 470像素。

### 3.4 统计处理

对每个独立patch p：

$$\beta_1^{(p)}(\nu) = \text{persistent cycles in } 1-5^\circ \text{ range at threshold } \nu$$

对所有patch平均：

$$\bar{\beta}_1(\nu) = \frac{1}{N_{\text{patches}}} \sum_{p=1}^{N_{\text{patches}}} \beta_1^{(p)}(\nu)$$

patch-to-patch方差给出误差棒：

$$\sigma_{\beta_1}(\nu) = \frac{\text{std}_p[\beta_1^{(p)}(\nu)]}{\sqrt{N_{\text{patches}}}}$$

对5000个ΛCDM模拟重复相同流程，得到β₁(ν)的期望分布。

---

## 四、DGF预测的定量形式

DGF预测在1-5°尺度上的β₁增强：

$$\beta_1^{\text{DGF}}(\nu) = \beta_1^{\Lambda\text{CDM}}(\nu) \cdot \left[1 + \delta \cdot f(\nu)\right]$$

其中：
- δ = 0.002 - 0.020（0.2%-2%，依赖b₁_eff(z_rec)的取值）
- f(ν) 是阈值ν的权重函数，在ν≈0（均值附近）取峰值：

$$f(\nu) = \exp\left(-\frac{\nu^2}{2}\right)$$

（理由：Cartan轴失配效应在统计意义上对正负涨落对称——环结构在均值附近最丰富。）

**最保守预测（最易被排除）：**
$$\delta \geq 0.005 \quad (0.5\%)$$

如果观测在95%置信度上排除δ ≥ 0.005，DGF的HF1被排除。

**核心预测（DGF有信心）：**
$$\delta \in [0.002, 0.020]$$

---

## 五、预期结果

### 5.1 统计灵敏度

| 参数 | 值 |
|------|-----|
| Patches数 | 300（全天~80%覆盖） |
| 每patch有效独立像素数 | ~150² = 22500 |
| ΛCDM模拟数 | 5000 |
| 每bin的statistical error | σ_stat ~ 1/√300 ≈ 5.8%（per patch） + 模拟误差 |
| 平均后误差 | σ_mean ≈ 5.8%/√300 ≈ 0.34%（per ν bin） |
| 模拟统计误差 | σ_sim ≈ 0.14%（平均10 bins后） |
| **总灵敏度 (1σ)** | **~0.4%** |
| **3σ detection** | **δ ≥ 1.2%** |
| **5σ detection** | **δ ≥ 2.0%** |

**关键：** DGF预测的0.5-2%在3σ（δ≥1.2%）处可被检验。若δ=2%（乐观值），可达到5σ。若δ=0.5%（保守值），需要>10,000模拟才能达到3σ。

### 5.2 四种可能的结果

| 观测结果 | 对DGF的意义 |
|---------|-----------|
| β₁增强≥2% + β₀抑制（≥3σ）| **DGF强烈支持** — two-pattern match |
| β₁增强≥2% + β₀也增强 | **DGF部分支持** — amplitude ok, pattern矛盾 |
| β₁增强<0.5%（95% CL）| **DGF HF1排除** — 在最保守预测以下 |
| β₁无显著偏离（<1σ）| **DGF HF1排除** — 效应为零 |
| β₁增强0.5-2% + β₀抑制（1-3σ）| **不确定** — 需要Planck PR5/Euclid |

---

## 六、执行计划

### Phase A: 环境搭建（1周）
- [ ] 安装healpy/GUDHI/CubicalRipser
- [ ] 下载Planck PR4 SMICA/Commander/NILC/SEVEM图
- [ ] 下载/生成5000 ΛCDM CMB模拟
- [ ] 实现patch提取+投影函数
- [ ] 在50个patches × 10个模拟上验证pipeline

### Phase B: 生产运行（1-2周）
- [ ] 对观测数据：400 patches × 4张图 = 1600 persistent homology计算
- [ ] 对ΛCDM模拟：5000 sims × 400 patches = 200万计算（需并行化，32核~3天）
- [ ] 提取β₁(ν, scale)曲线
- [ ] Scale分离：1-5°过滤

### Phase C: 统计分析（1周）
- [ ] 计算β₁观测值vs期望值
- [ ] 构建χ²和贝叶斯因子
- [ ] 限制δ（DGF增强参数）
- [ ] 系统误差评估：不同成分分离图的一致性
- [ ] β₀ vs β₁交叉检验

### Phase D: 论文（1周）
- [ ] 写论文草稿
- [ ] 生成图表
- [ ] 投A&A Letters 或 PRD Rapid Communications

---

## 七、关键风险

| 风险 | 概率 | 缓解 |
|------|:---:|------|
| PR4数据不可公开获取 | 低 | 用Planck 2018数据替代（已有Nside=2048图） |
| FFP10模拟不可获取 | 中 | 用PySM生成Gaussian模拟替代（无前景、无噪声CMB） |
| 计算资源不足 | 中 | 减少patches(400→200)或提高Nside(256→128)；合作者贡献CPU |
| 点源/前景污染1-5° | 低 | 标准Planck掩模+成分分离多图交叉验证 |
| Patch边界效应 | 低 | 10° patch内1-5°特征有≥2°边界缓冲 |
| Persistent homology软件bug | 中 | 在Gaussian模拟上验证恢复已知EC公式 |
| EC抵消不完全 | 高 | β₁和β₀单独报告，不使用EC；persistent homology天然分离Betti数 |

---

## 八、联系人和合作

**建议联系的团队：**
1. **Pranav团队**（Kapteyn Astronomical Institute, Groningen）— 拥有CMB persistent homology的现有代码和专业知识
2. **GUDHI开发团队**（INRIA, France）— persistent homology软件支持
3. **Planck Legacy Archive** — 数据访问

**若外部合作不可行，本提案可独立执行** — 所有数据和软件公开可用。单人全职3-5周可完成。

---

## 九、对DGF的意义

这是**DGF的第一次独立、可证伪的观测检验。** 不同于暗能量接口（HF4，模型依赖强），HF1直接检验DGF的核心机制：因果拓扑→CMB拓扑印记。

- **如果β₁增强被确认（≥3σ）+ β₀抑制：** DGF成为有观测支持的理论框架，可以开始写PRL
- **如果β₁增强被α排除（<0.5% @ 95% CL）：** DGF的宇宙学接口需要修正；因果拓扑核心(CFOL)不受影响
- **如果结果模糊（1-3σ）：** 需要Euclid/Planck PR5改进精度

---

*提案结束。可立即开始Phase A。*
