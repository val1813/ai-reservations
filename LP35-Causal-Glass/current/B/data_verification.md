# LP35 因果玻璃 — 公开数据验证报告

> B博士（野路子）| 2026-06-08 | Phase 1-3

---

## Phase 1: 数据定位

### 1.1 DESI DR2 (核心数据集 — 验证P1/P2最关键)

| 项目 | 详情 |
|------|------|
| **论文** | DESI DR2 Results I (Lyα BAO) + II (BAO & Cosmology), PRD 112, 2025 |
| **arXiv** | 2503.14738 (overview), 2503.14744 (neutrinos), main results PRD |
| **数据获取状态** | **部分公开** |

**已公开的数据产品（可直接下载）:**

- **DESI DR2 Cosmology Chains (MCMC后验样本):**
  - URL: `https://data.desi.lbl.gov/public/papers/y3/bao-cosmo-params/`
  - NERSC路径: `/global/cfs/cdirs/desi/public/papers/y3/bao-cosmo-params/`
  - 包含模型: ΛCDM (`base`), wCDM (`base_w`), w0waCDM (`base_w_wa`), binned w(z) (`base_w-binned-3uniform`)
  - 数据组合: DESI-BAO (7个红移bin) + Planck CMB + Pantheon+/Union3/DES-SN5YR
  - 格式: GetDist兼容ASCII chain文件 (`chain.[1-4].txt`) + YAML配置文件
  - 协方差矩阵: 各参数组合的 `chain.covmat`

- **BAO测量值（7个有效红移bin）:**
  | Tracer | z_eff | 测量量 |
  |--------|-------|--------|
  | BGS | 0.295 | D_H/rd, D_M/rd |
  | LRG1 | 0.510 | D_H/rd, D_M/rd |
  | LRG2 | 0.706 | D_H/rd, D_M/rd |
  | LRG3+ELG1 | 0.934 | D_H/rd, D_M/rd |
  | ELG2 | 1.321 | D_H/rd, D_M/rd |
  | QSO | 1.484 | D_H/rd, D_M/rd |
  | Lyα | 2.330 | D_H/rd, D_M/rd |

- **BAO Likelihood代码:**
  - GitHub: `CobayaSampler/bao_data` repo, directory `desi_bao_dr2`

**未公开的数据:**

- 原始光谱（spectra）和红移目录 — DR2尚未发布
- 底层星系目录 — 仍在embargo期

**精度:** 各向同性BAO精度从DR1的0.52%提升至DR2的0.30%（1.7x改进）

---

### 1.2 DESI DR1（补充 — 用于z>1大尺度结构分析）

| 项目 | 详情 |
|------|------|
| **论文** | DESI Collaboration (2025), arXiv:2503.14745 |
| **数据获取状态** | **完全公开** |

**已公开数据产品:**

- **主红移目录 (FITS格式):**
  ```
  https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/
  ```
  - `zall-pix-iron.fits` (20.8 GB) — HEALPix-based, 18.7M objects
  - `zall-tilecumulative-iron.fits` (23.6 GB) — tile-based

- **Large-Scale Structure (LSS) Catalogs (星系聚类分析专用):**
  ```
  https://data.desi.lbl.gov/public/survey/catalogs/dr1/LSS/iron/LSScats/
  ```
  - 包含聚类catalog、随机catalog、完备性权重、系统误差修正

- **Value-Added Catalogs:**
  - 恒星质量+发射线: `https://data.desi.lbl.gov/doc/releases/dr1/vac/stellar-mass-emline/`
  - AGN分类: `https://data.desi.lbl.gov/doc/releases/dr1/vac/agngal/`

- **VizieR镜像 (CDS):**
  - `https://vizier.cds.unistra.fr/viz-bin/VizieR-2?-source=V/161`

**红移覆盖（星系示踪物）:**
| Tracer | z范围 | 数量 |
|--------|-------|------|
| BGS | 0.1 < z < 0.4 | ~300k |
| LRG | 0.4 < z < 1.1 | ~2.1M |
| ELG | 0.8 < z < 1.6 | ~2.4M |

**关键:** DESI DR1的LSS catalog可用于测量z<1和z>1的大尺度结构聚类差异（P1的检验基础）。

---

### 1.3 Planck 2018 Legacy (CMB透镜+ISW — 验证P3)

| 项目 | 详情 |
|------|------|
| **论文** | Planck 2018 Results. VIII. Gravitational lensing, A&A 641, A8 (2020) |
| **数据获取状态** | **完全公开** |

**数据访问:**

- **Planck Legacy Archive (PLA):** `https://pla.esac.esa.int`
  - CMB温度+极化图 (NILC, SMICA, SEVEM, Commander)
  - 透镜势图 + 透镜功率谱 C_L^{φφ}
  - Likelihood代码
  - 搜索关键词: "Legacy" → Lensing products

- **NASA LAMBDA 镜像:** `https://lambda.gsfc.nasa.gov`
  - 提供FITS格式的所有Planck数据产品

- **透镜数据规格:**
  - 多极范围: 8 ≤ L ≤ 400 (2015: 40-400)
  - 检测显著性: 迄今最强CMB透镜检测
  - 透镜振幅精度: ~2.6%
  - 透镜可能性: Gaussian in band powers with perturbative corrections

- **CMB ISW分析所需:**
  - CMB温度图 (NILC/SMICA, FITS格式, 分辨率~5 arcmin)
  - 透镜势图 (phi map, FITS格式)
  - ISW-lensing可能性: https://pla.esac.esa.int — search for "ISW"

**用于P3的ISW交叉相关:** Planck公共数据中的NILC/SMICA温度图可直接用于与DESI星系样本做ISW交叉相关。不需要额外申请。

---

### 1.4 SDSS/eBOSS (补充 — 独立的大尺度结构数据)

| 项目 | 详情 |
|------|------|
| **DR17 (最终SDSS-IV发布)** | 完全公开 |
| **数据访问** | `https://www.sdss4.org/dr17/data_access/` |

**大尺度结构相关产品:**

- **BOSS DR12 (0.15 < z < 0.70):**
  - 功率谱多极矩 (monopole+quadrupole): `https://www.ub.edu/bispectrum/bispectrum_public/boss_public.html`
  - LOWZ (z_eff=0.32: 361,762 galaxies) + CMASS (z_eff=0.57: 777,202 galaxies)
  - 包含2048 MD-Patchy mock catalogs

- **eBOSS DR16 LRG (0.6 < z < 1.0):**
  - 功率谱多极矩: `https://www.ub.edu/bispectrum/page13.html`
  - z_eff=0.70, 377,458 galaxies
  - NGC + SGC分别样本
  - 含Nseries + EZmocks

- **eBOSS DR16 QSO (z~1.5):**
  - 类星体聚类数据，可用于z>1的大尺度结构

**对LP35的用处:** 独立于DESI的LSS聚类数据，控制可能的仪器系统误差。

---

### 1.5 超新星数据集 (验证P2: w(z)重建)

#### Pantheon+

| 项目 | 详情 |
|------|------|
| **论文** | Scolnic+ (2022), ApJ 938, 113 (arXiv:2112.03863) |
| **数据状态** | **完全公开** |
| **下载** | `https://github.com/PantheonPlusSH0ES/DataRelease` |
| **红移谱** | Carr+ (2022): CDS catalog J/other/PASA/39.46 → 2,285 SNe Ia with CMB-frame redshifts |
| **样本规模** | 1,701条光变曲线, 1,550 unique SNe Ia, 18 surveys, z up to ~2.27 |
| **包含** | 光变曲线 + 距离模数 + 协方差矩阵 |

#### Union3

| 项目 | 详情 |
|------|------|
| **论文** | Rubin et al. (2023), arXiv:2311.12098 |
| **数据状态** | 方法论文已公开，数据可通过论文supplementary material获取 |
| **样本规模** | ~2,000 SNe Ia, unified UNITY Bayesian framework |
| **注意** | 与Pantheon+有较大样本重叠 |

#### DES-SN5YR

| 项目 | 详情 |
|------|------|
| **论文** | DES Collaboration (2024): arXiv:2401.02929 (cosmology), arXiv:2406.05046 (data release) |
| **数据状态** | **完全公开** |
| **下载** | `https://github.com/des-science/DES-SN5YR` |
| **Zenodo** | DOI: `10.5281/zenodo.12720777` |
| **样本规模** | 1,635 photometric SNe + 194 low-z → 1,829 total on Hubble diagram |
| **红移范围** | 0.1 < z < 1.13（单仪器最大红移覆盖） |
| **包含** | 距离模数+红移数据向量、统计+系统协方差矩阵、SALT3模型、MCMC chains |

---

### 1.6 未来数据集 (近期将公开)

| 数据集 | 预计公开时间 | 对LP35的相关性 |
|--------|-------------|---------------|
| **Euclid DR1** | 2026年10月 (images+catalogs), 2027 (cosmology results) | P1+P3: 弱透镜+星系聚类 z<2 |
| **DESI DR2 全数据** | TBD (>2026) — spectra+redshifts 仍在embargo | P1+P2: LSS catalog z<2 |
| **LSST/Rubin** | 2027+ | P1-P3: 最大统计量的LSS+SN+WL |

---

### 1.7 数据可获取性总结

| 数据集 | 状态 | 对哪个预测最关键 | 直接下载URL |
|--------|------|-----------------|------------|
| DESI DR2 Cosmology Chains | ✅ 公开 | P2 (w(z)拐点) | `https://data.desi.lbl.gov/public/papers/y3/bao-cosmo-params/` |
| DESI DR2 BAO Likelihood | ✅ 公开 | P2 (w(z)重建) | GitHub: `CobayaSampler/bao_data` |
| DESI DR1 LSS Catalogs | ✅ 公开 | P1 (z>1聚类差异) | `https://data.desi.lbl.gov/public/survey/catalogs/dr1/LSS/` |
| Planck 2018 Lensing + CMB | ✅ 公开 | P3 (ISW纹理) | `https://pla.esac.esa.int` |
| Pantheon+ SNe | ✅ 公开 | P2 (w(z)约束) | `https://github.com/PantheonPlusSH0ES/DataRelease` |
| DES-SN5YR | ✅ 公开 | P2 (w(z)约束) | `https://github.com/des-science/DES-SN5YR` |
| SDSS/eBOSS DR17 | ✅ 公开 | P1 (LSS独立检验) | `https://www.sdss4.org/dr17/data_access/` |
| Union3 SNe | ⚠️ 部分 | P2 (w(z)约束) | 论文supplementary (arXiv:2311.12098) |
| Planck ISW data | ✅ 公开 | P3 (ISW交叉相关) | `https://pla.esac.esa.int` (CMB T map) |
| Euclid DR1 | 🔮 2026.10 | P1+P3 | `https://www.euclid-ec.org` |
| DESI DR2 Raw Catalogs | ❌ Embargo | P1 (z>1全星系样本) | 尚未 |

---

## Phase 2: 可检验性评估

### 2.1 预测P1: "z>1遍历 (因果冻结纹理仅在z<0.8出现)"

**需要的数据产品:**
1. DESI DR1 LSS catalogs — 按红移分割的星系聚类统计量
2. DESI DR2 BAO数据 (当full catalogs公开时)
3. 星系两点/三点相关函数 in different z-bins: 0.3-0.7 (低z), 0.7-1.0 (过渡), 1.0-1.5 (高z)
4. 功率谱多极矩 P_ℓ(k) for each redshift bin

**可用的替代方案（数据已公开）:**

- **SDSS/eBOSS DR16 DR17:** 独立星系样本, z < 1
- 但需要z > 1的聚类数据（eBOSS QSO样本z~1.5可用）
- 使用DESI DR1 LSS catolog直接计算z<0.8 vs z>1的聚类差异

**精度评估:**

| 量 | 当前精度 | 是否足够 |
|----|---------|---------|
| 星系偏袒 b(z) | 各z bin ~5-10% | 需要控制b(z)对聚类的影响才能检测因果纹理 |
| ξ(s) or P(k) in bins | S/N ~10-20 per bin | 如果因果纹理效应量级 >5-10% of clustering amplitude → 可检测 |
| 因果连通性诊断量 | 未知 — 需要定义 | ⛔ 核心问题：因果纹理没有标准观测量 |

**拒绝阈值:**
- 如果z>1星系的聚类统计量与z<1的系统性差异<2σ → 两个方向都不能排除
- 如果z>1聚类存在系统性差异（≥3σ），方向取决于差异模式：
  - z>1: 无冻结纹理（更高随机性/遍历）→ 支持B博士
  - z>1: 有冻结纹理（与z<1无差异）→ 支持A博士或否决R3

**主要挑战:**
1. 星系偏袒b(z)的红移演化难以与因果纹理效应区分
2. "因果连通性"不是标准大尺度结构统计量 — 需要定义新的观测量
3. 结构增长的非线性效应在低红移更强 → 需要模拟区分引力增长和因果纹理

**目前可行性: 中低。** 需要构建新的观测量+细致的红移binning+控制结构增长。用现有公开数据可在~6个月研究项目中完成。

---

### 2.2 预测P2: "w(z)在z_accel~0.8附近有拐点"

**需要的数据:**
1. DESI DR2 BAO: D_H(z)和D_M(z)在7个红移bin
2. 超新星数据（Pantheon+/Union3/DES-SN5YR）: 距离模数 μ(z)
3. CMB距离先验（Planck 2018）

**需要的工具:**
- Cobaya MCMC sampler + DESI DR2 BAO likelihood
- w(z)重建方法: CPL参数化、binned w(z)、Gaussian Process回归、多项式插值

**精度评估（这是最可行的预测）:**

| 数据组合 | σ(w0) | σ(wa) | 能否检测拐点? |
|---------|-------|-------|-------------|
| DESI DR2 BAO + CMB | ~0.08 | ~0.35 | 勉强 |
| DESI DR2 BAO + CMB + Pantheon+ | ~0.06 | ~0.25 | 概率高 |
| DESI DR2 BAO + CMB + DES-SN5YR | ~0.06 | ~0.25 | 概率高 |
| DESI DR2 BAO + CMB + SN (all) | ~0.05 | ~0.20 | 可检测 |

**DESI DR2实测结果（已公开）:**
- DESI BAO + DES Y5 SN + CMB: w0 = -0.76±0.07, wa = -0.97±0.28
- w(z)重建显示: w(z)在z~0.5附近有"phantom crossing"（穿过w=-1）
- 3-bin均匀w(z)重建: z_bins = [0, 0.8, 1.6, 2.4]

**拐点检测可行性分析:**

LP35预测w(z)在z_accel~0.8±0.3附近有二阶导数符号变化（拐点）。具体地:
- z < z_accel: w(z)偏离-1越来越远（冻结正在发生）
- z > z_accel: w(z)收敛回-1（冻结尚未开始）

检验等价于: 在binned w(z)重建中，z~0.5-1.0 bin的w与z~1.0-1.5 bin的w存在**方向性差异**。

**当前数据信号:**

DESI DR2的3-bin w(z)重建（arXiv:2506.22953, Li & Wang 2025）:
- Bin 1 (z=0-0.8): w有偏离（phantom crossing, w≠-1 迹象）
- Bin 2 (z=0.8-1.6): w可能更接近-1
- Bin 3 (z=1.6-2.4): w约束很弱，与-1一致

**现有关键发现:** DESI DR2已经显示z<1和z>1的w(z)行为有**定性差异** — 这与LP35预测方向一致（z<1: 冻结活跃, z>1: 冻结弱/无）。但当前数据精度不足以区分"拐点"和"趋势性漂移"。

**≥2σ判断可行性:**

| 条件 | 是否满足 |
|------|---------|
| DESI DR2 w(z) binned constraints 已公开 | ✅ |
| 精度σ(w)~0.05-0.1 per bin | ✅ |
| 需要检测 w(z~0.6) - w(z~1.2) 差值 | 差值~0.1-0.2量级 |
| σ(Δw) ~ √(σ^2_1 + σ^2_2) ~ 0.07-0.14 | → S/N ~ 1-3 |
| **2σ检测需要额外的低z和高z SN数据或更强的先验** | ⚠️ 边界情况 |

**结论:** P2目前是最可检验的预测。DESI DR2的公开chain数据+Pantheon+/DES-SN5YR可能给出≥2σ的指示（取决于w(z)的实际形状）。Euclid DR1 (2027)将确定性地解决。

**可行性: 高。** 数据已公开，工具链成熟（Cobaya/GetDist），分析流程标准。可用现有数据在~2-4周完成。

---

### 2.3 预测P3: "晚期ISW因果纹理"

**需要的数据:**
1. Planck 2018 CMB温度图 (NILC/SMICA) — 公开，PLA下载
2. DESI DR1 LSS catalog — 按红移分割 (z<0.8, z>0.8)
3. 星系-CMB交叉功率谱 C_ℓ^{gT} 测量工具

**精度评估:**

ISW检测本身信噪比低（标准ΛCDM ISW ~2-3σ in single tracer）。检测"因果纹理调制"的额外ISW信号更困难:
- Planck×DESI交叉相关: 预计S/N ~3-5 for standard ISW
- 因果纹理额外贡献: 需要在小尺度 (k>0.1 h/Mpc) 有超额功率
- 区分标准ISW vs 因果纹理ISW: 需要额外的尺度依赖性特征

**挑战:**
1. 小尺度ISW信号被primary CMB和噪音主导
2. 需要精确的星系偏袒建模来提取ISW幅度
3. 修正引力模型 (f(R), DGP) 也有类似尺度的ISW修正 → 简并

**可行性: 中低。** ISW检测需要大天区+高密度星系样本，信噪比有限。Euclid DR1将大幅改善（2027）。

---

### 2.4 可行性排名

| 排名 | 预测 | 可行性 | 关键原因 |
|------|------|--------|---------|
| 1 | P2: w(z)拐点 | ⭐⭐⭐ 高 | DESI DR2 chains已公开+标准MCMC分析 |
| 2 | P1: z>1遍历 | ⭐⭐ 中 | 需要定义新观测量+控制b(z)演化 |
| 3 | P3: ISW纹理 | ⭐ 中低 | ISW信噪比低+与修正引力简并 |

---

## Phase 3: 具体检验方案 — P2 w(z)拐点

### 3.1 方案概述

**目标:** 用DESI DR2公开cosmology chains检测w(z)在z_accel ~ 0.8 ± 0.3附近是否存在二阶导数拐点，区分"w(z)整体漂移"和"w(z)在z~0.8有拐点"。

**数据来源:**
- **DESI DR2 BAO chains:** `https://data.desi.lbl.gov/public/papers/y3/bao-cosmo-params/`
- **DES-SN5YR chains:** `https://github.com/des-science/DES-SN5YR` (data vectors + MCMC)
- **Pantheon+:** `https://github.com/PantheonPlusSH0ES/DataRelease` (distance moduli for independent check)

**工具:**
- Cobaya (MCMC sampler): `pip install cobaya`
- GetDist (chain analysis): `pip install getdist`
- 可选: CAMB (理论预测), classy (替代)

---

### 3.2 分析步骤

#### Step 1: 下载DESI DR2 cosmology chains

```bash
# Download chains from DESI DR2
wget -r -np -nH --cut-dirs=5 \
  https://data.desi.lbl.gov/public/papers/y3/bao-cosmo-params/cobaya/base_w_wa/

# Each data combination is a subdirectory:
# desi-bao-all_planck2018-lowl-TT-clik_planck2018-lowl-EE-clik_planck-NPIPE-highl-CamSpec-TTTEEE_planck-act-dr6-lensing/
```

**关键模型+数据组合:**
| 目录 | 参数化 | 数据 |
|------|--------|------|
| `base_w-binned-3uniform/` | w in 3 redshift bins [0,0.8],[0.8,1.6],[1.6,2.4] | DESI BAO + CMB |
| `base_w_wa/` | CPL: w0+wa | DESI BAO + CMB + SNe |
| `base_w/` | 常数w | DESI BAO + CMB |

#### Step 2: 分析binned w(z) chains

```python
# 使用GetDist分析chain
import getdist

# Load chains for 3-bin w(z) model
chains = getdist.mcsamples.loadMCSamples(
    '/path/to/base_w-binned-3uniform/desi-bao-all_CMB/'
)

# Extract w in 3 bins: w_0 (z=0-0.8), w_1 (z=0.8-1.6), w_2 (z=1.6-2.4)
# Parameter names in chain: w_bin_0, w_bin_1, w_bin_2
samples = chains.samples

# Get 1D marginalized constraints
w0_mean, w0_std = samples['w_bin_0'].mean(), samples['w_bin_0'].std()
w1_mean, w1_std = samples['w_bin_1'].mean(), samples['w_bin_1'].std()
w2_mean, w2_std = samples['w_bin_2'].mean(), samples['w_bin_2'].std()
```

#### Step 3: 拐点检测

**关键统计量:**

定义拐点指示器:

```
I_inflection = (w_bin_0 - w_bin_1) - (w_bin_1 - w_bin_2)
             = w_0 - 2*w_1 + w_2
```

这是w(z)在中间bin处的离散二阶导数。如果w(z)在z~0.8有拐点:
- **LP35预测:** I_inflection ≠ 0 (负值: w先在低z偏离-1, 在高z回归-1)
- **平滑漂移 (无拐点):** I_inflection ≈ 0
- **ΛCDM:** w_i = -1 for all i → I_inflection = 0

**从MCMC chains计算:**

```python
import numpy as np

# Extract unnormalized posterior weights
w0 = samples['w_bin_0']
w1 = samples['w_bin_1']
w2 = samples['w_bin_2']
weights = samples['weight']

# Compute I_inflection for each sample
I_inflection = w0 - 2*w1 + w2

# Weighted statistics
I_mean = np.average(I_inflection, weights=weights)
I_std = np.sqrt(np.average((I_inflection - I_mean)**2, weights=weights))

# Significance: is I_inflection < 0?
significance = abs(I_mean / I_std)

print(f"I_inflection = {I_mean:.4f} ± {I_std:.4f}")
print(f"Deviation from 0: {significance:.1f}σ")
```

#### Step 4: CPL参数化一致性检验

从CPL chain (base_w_wa)提取w0, wa:
```python
chains_cpl = getdist.mcsamples.loadMCSamples(
    '/path/to/base_w_wa/desi-bao-all_CMB_SN/'
)
w0 = chains_cpl.samples['w0']
wa = chains_cpl.samples['wa']

# Compute w(z) at z=0, z=0.8, z=1.5
w_z0 = w0
w_z08 = w0 + wa * (0.8 / (1 + 0.8))  # w(a) = w0 + wa*(1-a), a=1/(1+z)
w_z15 = w0 + wa * (1.5 / (1 + 1.5))

# Curvature at z~0.8: d^2w/dz^2 approximated by finite difference
# Using z=0, z=0.8, z=1.5 as grid points
# Δz1 = 0.8, Δz2 = 0.7
d2w_dz2 = (w_z15 - 2*w_z08 + w_z0) / (0.8 * 0.7)  # approximate
```

**拐点条件 (LP35):**
- d²w/dz²|_{z~0.8} < 0: w(z)先向下弯曲（偏离-1），后向上回归（⇒冻结在z~0.8最剧烈）
- |d²w/dz²| > 0: 有拐点 vs d²w/dz² ≈ 0: 平滑趋势

#### Step 5: 与Pantheon+/DESY5 SN交叉验证

使用超新星数据做独立w(z)重建（Gaussian Process或binned），不依赖CPL参数化:

```python
# 使用scikit-learn Gaussian Process Regression
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel

# Load SN distance moduli + redshifts
# From DES-SN5YR: use the pre-computed distance moduli
# Or from Pantheon+: mu(z) with covariance matrix

# GP reconstruction of w(z)
# ...
```

**注意:** 需要从μ(z)通过Friedmann方程逆推出w(z)，这涉及对μ(z)求导 → 噪声放大。更好的方法是直接在w(z)空间做参数化MCMC（如binned w）。

#### Step 6: 系统误差检查

1. **bin边界敏感性:** 改变3-bin的边界 (如 [0, 0.6], [0.6, 1.2], [1.2, 2.4])，检查I_inflection是否稳定
2. **SN compilation敏感性:** 分别用Pantheon+, Union3, DES-SN5YR，检查w(z)重建是否一致
3. **CMB prior敏感性:** 使用不同的CMB可能性 (Planck PR3 vs PR4)，检查结果稳定性

---

### 3.3 预测成立 vs 不成立的预期

**如果LP35 P2成立 (因果冻结由暗能量驱动):**

| 观测量 | 预期值 | 置信度需求 |
|--------|--------|----------|
| I_inflection (3-bin) | < 0, 幅度 |I| > 0 | ≥2σ away from 0 |
| w_bin_0 (z<0.8) | > -1 (偏离ΛCDM) | ≥2σ away from -1 |
| w_bin_1 (z~0.8-1.6) | 接近-1 或 穿越 | 与bin_0的差值≥2σ |
| w_bin_2 (z>1.6) | ≈ -1 (与ΛCDM一致) | 与-1一致（Δχ² ≤ 1） |
| d²w/dz²\|_{z~0.8} | < 0 (拐点) | 符号确定≥2σ |

**定性特征:** w(z)在z~0.5-0.8附近有一个"弯曲" — 低红移偏离ΛCDM, 高红移回归ΛCDM。

**如果P2不成立:**

| 情景 | 观测特征 |
|------|---------|
| ΛCDM为真 | 所有w_i = -1 within error, I_inflection ≈ 0 at <1σ |
| 冻结在DE前 (A博士) | w在所有z偏离-1，无拐点。I_inflection ≈ 0但各w_i ≠ -1 |
| 标准精质 (无因果玻璃) | w(z)为平滑单调函数, I_inflection ≈ 0 |
| 冻结从未发生 | w(z)行为由其他物理驱动，无LP35特定模式 |

---

### 3.4 数值阈值

**可发表性阈值:**

| 结果 | 解读 | 行动 |
|------|------|------|
| I_inflection < 0 at ≥ 3σ | **强支持LP35 P2** | 写论文: "w(z)在z~0.8有显著拐点，与因果冻结原理预测一致" |
| I_inflection < 0 at 2-3σ | 有趣暗示，需更多数据 | 写note: "DESI DR2 hints at w(z) inflection at z~0.8" + 等Euclid DR1确认 |
| I_inflection = 0 at < 2σ | 可排除强拐点（|d²w/dz²| > 0.3 at 95%CL） | 记录为LP35的null result |
| I_inflection > 0 at ≥ 2σ | **排除LP35 P2 (方向相反)** | 记录排除，更新理论 |
| 各w_bin均= -1 at <1σ | 无DE动力学证据 | LP35预测现阶段无法检验，等更大数据集 |

**B博士具体预测检验:**

LP35 P2的核心定量预言是:
> "Δq(z) = Δq_0 · Θ(z_freeze - z) · ((z_freeze - z)/z_freeze)^ν"

检验等价于:
1. **Θ函数检验:** w(z≠-1) 仅出现在 z < z_freeze (≈0.8±0.3)
2. **幂律检验:** |w(z) - (-1)| ∝ (z_freeze - z)^ν  for z < z_freeze, ν>0

用binned w(z)的3个bin:
- Bin 0 (z<0.8): |w - (-1)| > 0 (≥2σ)
- Bin 1 (z=0.8-1.6): |w - (-1)| ~ 0 或过渡
- Bin 2 (z>1.6): |w - (-1)| ≈ 0 (与ΛCDM一致)

**如果两个低z bin都偏离-1但高z bin不偏离:** 方向正确但数据不足以确定拐点位置 → B博士和A博士都兼容。

**如果只有最低z bin偏离-1:** 拐点在z<0.8 → 冻结开始得比预期晚 → B博士预测的z_freeze需要下调。

---

### 3.5 代码清单

**最小可运行分析管道:**

```python
# lp35_p2_test.py
# 用DESI DR2公开chains检验P2: w(z)在z~0.8的拐点

import numpy as np
import getdist
from getdist import plots, MCSamples
import os
import urllib.request
import tarfile

# ===== Step 1: Download chains =====
CHAIN_URL = ("https://data.desi.lbl.gov/public/papers/y3/"
             "bao-cosmo-params/cobaya/")
MODELS = ['base_w-binned-3uniform', 'base_w_wa', 'base_w']
DATA_COMBOS = [
    'desi-bao-all_planck2018-lowl-TT-clik_planck2018-lowl-EE-clik_'
    'planck-NPIPE-highl-CamSpec-TTTEEE_planck-act-dr6-lensing'
]

# Download script: use wget or curl
# os.system(f'wget -r -np -nH {CHAIN_URL}')

# ===== Step 2: Load and analyze binned w(z) =====
chain_dir = './bao-cosmo-params/cobaya/base_w-binned-3uniform/'
samples_binned = getdist.mcsamples.loadMCSamples(
    chain_dir + DATA_COMBOS[0],
    settings={'ignore_rows': 0.3}  # burn-in
)

# Extract parameters
# Note: actual param names depend on chain YAML — check chain.input.yaml
# Typical names: w_bin_0, w_bin_1, w_bin_2  or w0, w1, w2
param_names = samples_binned.getParamNames().list()
w_params = [p for p in param_names if p.startswith('w')]

print(f"Available w parameters: {w_params}")

# If 3-bin model:
w = {}
for i, pname in enumerate(w_params[:3]):
    w[i] = samples_binned.samples[pname]
    mean = np.average(w[i], weights=samples_binned.weights)
    std = np.sqrt(np.average((w[i]-mean)**2,
                  weights=samples_binned.weights))
    print(f"  {pname}: {mean:.4f} ± {std:.4f}")

# ===== Step 3: Inflection test =====
I_infl = w[0] - 2*w[1] + w[2]
I_mean = np.average(I_infl, weights=samples_binned.weights)
I_std = np.sqrt(np.average((I_infl - I_mean)**2,
                weights=samples_binned.weights))
significance = abs(I_mean) / I_std

print(f"\n=== P2 Inflection Test ===")
print(f"I_inflection = {I_mean:.4f} ± {I_std:.4f}")
print(f"Significance: {significance:.1f}σ")
print(f"P(I_inflection < 0) = "
      f"{np.sum((I_infl < 0) * samples_binned.weights) / np.sum(samples_binned.weights):.3f}")

# ===== Step 4: Check Θ-function prediction =====
# Is |w_bin_0 + 1| > 0 while |w_bin_2 + 1| ≈ 0?
delta_w0 = w[0] + 1  # deviation from -1 in lowest z bin
delta_w2 = w[2] + 1  # deviation from -1 in highest z bin

p_deviation_lowz = np.sum((delta_w0 > 0) * samples_binned.weights) / \
                   np.sum(samples_binned.weights)
print(f"\nP(w_bin_0 > -1) = {p_deviation_lowz:.3f}")
print(f"P(w_bin_2 > -1) = "
      f"{np.sum((delta_w2 > 0) * samples_binned.weights) / np.sum(samples_binned.weights):.3f}")

# ===== Step 5: CPL consistency check =====
if os.path.exists('./bao-cosmo-params/cobaya/base_w_wa/'):
    samples_cpl = getdist.mcsamples.loadMCSamples(
        './bao-cosmo-params/cobaya/base_w_wa/' + DATA_COMBOS[0],
        settings={'ignore_rows': 0.3}
    )
    w0_cpl = samples_cpl.samples['w0']
    wa_cpl = samples_cpl.samples['wa']

    # w(z) at z=0, z=0.8, z=1.5 in CPL
    a_08 = 1.0 / 1.8  # a = 1/(1+z)
    a_15 = 1.0 / 2.5
    w08 = w0_cpl + wa_cpl * (1 - a_08)
    w15 = w0_cpl + wa_cpl * (1 - a_15)

    # curvature
    d2w = (w15 - 2*w08 + w0_cpl) / (0.8 * 0.7 * (w0_cpl**2 + 0.01))
    print(f"\n=== CPL Cross-check ===")
    print(f"w0 = {np.average(w0_cpl, weights=samples_cpl.weights):.3f} ± "
          f"{np.std(w0_cpl):.3f}")
    print(f"wa = {np.average(wa_cpl, weights=samples_cpl.weights):.3f} ± "
          f"{np.std(wa_cpl):.3f}")
    print(f"P(d^2w/dz^2 < 0 at z~0.8) = "
          f"{np.sum((d2w < 0) * samples_cpl.weights) / np.sum(samples_cpl.weights):.3f}")

print("\n=== Summary ===")
print("LP35 P2 prediction: w(z) has inflection at z_accel~0.8±0.3")
print(f"Current data: I_inflection significance = {significance:.1f}σ")
if significance >= 2.0:
    if I_mean < 0:
        print("→ ≥2σ support for LP35 P2 (inflection detected, direction correct)")
    else:
        print("→ ≥2σ inflection detected but WRONG DIRECTION (excludes LP35 P2)")
elif significance >= 1.0:
    print("→ Hint of inflection, insufficient significance (need Euclid DR1)")
else:
    print("→ No evidence for inflection in current data")
```

---

### 3.6 所需计算资源

| 资源 | 需求 |
|------|------|
| 计算时间 | 链已预制 — 不需要重新MCMC。仅分析 ~1小时 |
| 硬盘空间 | ~10 GB (chain samples + SN data) |
| 软件 | Python 3.9+, GetDist, Cobaya (可选), numpy, scipy |
| 专业知识 | 宇宙学参数估计基础，MCMC链分析 |

---

### 3.7 备选检验方案 (P1: z>1 遍历性)

如果P2检验遇到意外困难，可从P1开始:

**简化方案:** 使用DESI DR1 LSS catalog的LRG样本，在z<0.8和z>1之间比较:

1. **星系聚类幅度 A_clust(z)** = σ_8(z) * b(z) at R~8 Mpc/h
2. **红移空间畸变 fσ_8(z)** — 如果因果纹理影响速度场
3. **三点相关函数 Q(r1,r2)** — 对非高斯纹理更敏感

**具体处方:**
```python
# 使用nbodykit或Corrfunc计算两点/三点相关函数
# 分别在z=0.5-0.8和z=1.0-1.3的LRG样本中
# 比较: 如果z>1的聚类与z<1显著不同 (控制了b(z)和结构增长后)
# 且差异方向为z>1更接近Poisson/随机 → 支持B博士
```

---

## 参考文献

1. DESI Collaboration (2025), "DESI DR2 Results I & II", PRD 112, 083514-083515
2. Li & Wang (2025), "Reconstructing dark energy after DESI DR2 BAO", EPJC 85, 1308, arXiv:2506.22953
3. DESI Collaboration (2025), "DESI DR1 Data Release", arXiv:2503.14745
4. Planck Collaboration (2020), "Planck 2018 results. VIII. Gravitational lensing", A&A 641, A8
5. Scolnic+ (2022), "The Pantheon+ Analysis", ApJ 938, 113, arXiv:2112.03863
6. DES Collaboration (2024), "DES-SN5YR Cosmological Results", ApJL 973, L14, arXiv:2401.02929
7. Rubin+ (2023), "Union Through UNITY", arXiv:2311.12098
8. SDSS-IV eBOSS DR17: https://www.sdss4.org/dr17/

---

## 文档签字

- **执行者:** B博士（野路子）
- **日期:** 2026-06-08
- **Phase覆盖:** Phase 1 (数据定位) + Phase 2 (可检验性评估) + Phase 3 (P2具体检验方案)
- **归档:** `ai-reservations/LP35-Causal-Glass/current/B/data_verification.md`
