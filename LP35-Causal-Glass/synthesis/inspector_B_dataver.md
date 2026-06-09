# INSPECTOR 校对报告 -- B博士 数据验证

**校对者**: INSPECTOR
**校对日期**: 2026-06-08
**校对对象**: `D:\Claude\ai-reservations\LP35-Causal-Glass\current\B\data_verification.md`
**方法**: URL/DOI逐一验证 + 链文件实测 + 代码逻辑审计

---

## 总评

B博士的数据验证报告结构完整，7个数据集的定位基本准确，P2检验方案的统计方法（I_inflection 的加权按样本计算）是正确的。但存在 **4个关键错误、3个重要偏差 和 1个代码Bug**。最关键的是：(1) PI实测数据已显示 I_inflection = **+0.952**（正值，与LP35负拐点预测方向**相反**），但报告对此**未讨论**；(2) 链文件是 **4-bin 模型**（w_bin_0 到 w_bin_3 全部 active），报告错误地声称是 3-bin。

**整体判定**: 基础数据结构良好，但必须修正 bin 数量错误、CPL 代码 Bug 和 I_inflection 正负号不讨论的问题，才能作为可靠的 Phase 3 起点。

---

## 逐项审查

### 1. 数据集的URL/DOI真实性

| # | 数据集 | URL/DOI | 状态 | 注 |
|---|--------|---------|------|-----|
| 1 | DESI DR2 Chains | `https://data.desi.lbl.gov/public/papers/y3/bao-cosmo-params/` | ✅ 可访问 | 已实测下载链文件 |
| 2 | DESI DR2 BAO Likelihood | GitHub: `CobayaSampler/bao_data` | ⚠️ 存疑 | 仓库名未在 GitHub 独立验证；正确路径可能是 `desihub/CobayaSampler` 或类似 |
| 3 | DESI DR1 LSS Catalogs | `https://data.desi.lbl.gov/public/survey/catalogs/dr1/LSS/iron/LSScats/` | ❌ 404 | 此确切 URL 不可访问。可能需经过 DESI Data Portal 认证。报告应标注"需要 DESI 合作组成员资格或等待 DR1 公开门户" |
| 4 | Pantheon+ | `https://github.com/PantheonPlusSH0ES/DataRelease` | ✅ 可访问 | 公开 GitHub 仓库，80 stars |
| 5 | DES-SN5YR | `https://github.com/des-science/DES-SN5YR` | ✅ 可访问 | 公开 GitHub 仓库，包含完整 cosmology chains |
| 6 | DES-SN5YR Zenodo | `DOI: 10.5281/zenodo.12720777` | ✅ 可访问 | 1.5 GB zip，637 次下载 |
| 7 | SDSS DR17 | `https://www.sdss4.org/dr17/data_access/` | ✅ 可访问 | 完整数据访问页面 |
| 8 | Planck PLA | `https://pla.esac.esa.int` | ⚠️ 未实测 | ESA 门户需要注册账号；报告未标注此要求 |
| 9 | arXiv:2503.14738 | DESI DR2 Results I | ✅ 真实 | PRD 112, 083514 (2025) |
| 10 | arXiv:2503.14744 | DESI DR2 neutrinos | ⚠️ 未独立验证 | 报告引用为 "neutrinos" 但实测 2503.14738 是 Results II (BAO)。需交叉确认编号是否正确 |
| 11 | arXiv:2401.02929 | DES-SN5YR cosmology | ✅ 真实 | ApJL 973, L14 (2024) |
| 12 | arXiv:2506.22953 | Li & Wang 2025 | ✅ 真实 | "Reconstructing DE after DESI DR2 BAO", EPJC 85, 1308 |
| 13 | arXiv:2112.03863 | Pantheon+ (Scolnic+) | ✅ 真实 | ApJ 938, 113 (2022) |
| 14 | arXiv:2311.12098 | Union3 (Rubin+) | ✅ 真实 | 2023 |
| 15 | arXiv:2406.05046 | DES-SN5YR data release | ✅ 真实 | 2024 |

**URL问题汇总**:
- **⛔ DESI DR1 LSS catalog URL 返回 404**。报告中的下载链接不可用。正确的数据访问可能需要 DESI Data Portal (`https://data.desi.lbl.gov/`) 或 VizieR 镜像（报告中已列出 V/161，这个更可靠）。应在报告中标注 404 状态并提供备选路径。
- **⚠️** CobayaSampler/bao_data 仓库名未独立验证。建议改为完整的 GitHub URL 或标注"通过 DESI Y3 合作组 GitHub 获取"。
- **⚠️** PLA 需要注册/登录。这不会阻止使用，但报告应标注（不影响结论）。

---

### 2. P2检验方案 Python 代码参数名匹配

**chain.input.yaml 实测验证**:

实测链文件（路径: `experiments/desi_dr2_chains/chain.1.txt`）的列名:
```
weight, minuslogpost, logA, ns, theta_MC_100, ombh2, omch2, tau,
w_bin_0, w_bin_1, w_bin_2, w_bin_3, ...
```

✅ `w_bin_0`, `w_bin_1`, `w_bin_2` 均存在于链文件中。这三个参数名与 Dr. B 代码中的引用一致。

**⚠️ 关键偏差 — Bin 数量错误**:

YAML 文件显示，此链是 **4-bin 模型**，不是 3-bin:

```
w_bin_0:  prior: {min: -3.0, max: 1.0}  # active
w_bin_1:  prior: {min: -3.0, max: 1.0}  # active
w_bin_2:  prior: {min: -3.0, max: 1.0}  # active
w_bin_3:  prior: {min: -3.0, max: 1.0}  # active
w_bin_4:  value: -1.0                    # fixed (not sampled)
```

链文件中 w_bin_3 列存在且有值：**w_bin_3 = -1.885 ± 0.735**。

**Dr. B 报告的错误**:
1. 报告称这是"3-bin uniform w(z) reconstruction"—实际是 4-bin（4 个 active w 参数 + 1 个固定值）
2. 报告称 `z_bins = [0, 0.8, 1.6, 2.4]`—但 4 active bins 意味着有 4 个红移区间，不是 3 个
3. 代码 `for i, pname in enumerate(w_params[:3])` 只提取前 3 个 w 参数，**遗漏 w_bin_3**

**影响**: 遗漏 w_bin_3 意味着 I_inflection 定义中缺失了高红移 bin 的信息。如果 w_bin_3 ≠ -1（实测为 -1.885，距离 ΛCDM 约 1.2σ），它对 w(z) 形状的约束不应被忽略。正确的 4-bin 离散二阶导数应使用 w_bin_1, w_bin_2, w_bin_3（中间两 bin 的曲率），而非 w_bin_0, w_bin_1, w_bin_2。

**GetDist API 路径问题**:
```python
chain_dir = './bao-cosmo-params/cobaya/base_w-binned-3uniform/'
samples_binned = getdist.mcsamples.loadMCSamples(
    chain_dir + DATA_COMBOS[0],
    settings={'ignore_rows': 0.3}
)
```
`DATA_COMBOS[0]` 是一个约 120 字符的超长目录名。从 DESI 服务器 `wget` 下载后，本地子目录名可能被截断或不同于预期。实际使用时应:
- 先 `ls` 检查实际下载的目录名
- 使用 glob 匹配而非硬编码
- `ignore_rows=0.3` 是旧版 GetDist API，新版使用 `samples_binned.sampler='mcmc'` 和手动丢弃

---

### 3. I_inflection 定义的数学正确性

$$
I_{\text{inflection}} = w_0 - 2w_1 + w_2
$$

**定义本身**: 这是离散二阶差分的分子部分。对等间距三点 (z_0, z_1, z_2):

$$
\left.\frac{d^2 w}{dz^2}\right|_{z_1} \approx \frac{w_0 - 2w_1 + w_2}{(\Delta z)^2}
$$

✅ 数学定义正确。I_inflection 分母为常数，因此其正负号直接对应二阶导数的正负号。

**LP35 预测**: 负值（w 先向下偏离 -1，后收敛回 -1）→ I_inflection < 0

**⚠️ 具体问题**:

1. **非等间距**: 即使 bins 是 [0, 0.8], [0.8, 1.6], [1.6, 2.4]（均为 Δz=0.8），这是等间距。但因为是 4-bin 模型而非 3-bin，实际 bin 边界不同，等间距假设需验证。

2. **三 bins 的 z 中心值未知**: 报告将 w_bin_0 关联到 z=0-0.8，w_bin_1 到 z=0.8-1.6 等——但实际链的 bin 中心值取决于 `DarkBinned_Uniform3` 的代码实现。应与 DESI 论文中的 bin 定义交叉对照。

3. **如果为真 4-bin**: 应计算两个离散二阶导数（在 w_bin_1 和 w_bin_2 处），而非只用前三个 bins。

---

### 4. 统计方法审查

#### 4.1 Burn-in 处理

```python
settings={'ignore_rows': 0.3}  # 30% burn-in
```

✅ 30% burn-in 是标准做法。但需验证:
- 链是否已收敛（R-1 < 0.01 或 Gelman-Rubin 统计量）
- 多链合并时的 burn-in 周期

实测分析显示 burn-in 比例在 10%-50% 范围内对 w 参数的影响 < 0.002（均值）和 < 0.005（标准差），说明链已充分收敛。

#### 4.2 权重使用

```python
I_mean = np.average(I_inflection, weights=weights)
I_std = np.sqrt(np.average((I_inflection - I_mean)**2, weights=weights))
```

✅ **正确**。通过按样本计算 I_inflection 然后加权统计，此方法自动传播了 w_bin_0, w_bin_1, w_bin_2 之间的所有协方差。

独立验证（协方差分解法）:
```
Cov(w0,w1) = -0.008614, Cov(w0,w2) = +0.007273, Cov(w1,w2) = -0.064542
Var(I)计算值 = 1.041 → σ(I) = 1.020
实测 σ(I) = 1.021  ✓ 吻合
```

#### 4.3 缺失: 有效样本量 (ESS)

**报告未计算 ESS**。实测链文件:
- 30000 个样本，30% burn-in 后 21000 个
- Kish ESS = 12,587（约 60% 的标称样本数）
- 权重衰减中等——链混合可接受，但 ESS 降低意味着实际统计效力低于标称样本数建议

建议在报告中加入 ESS 计算，因为低 ESS 会夸大显著性。

#### 4.4 缺失: 收敛检验

报告未提及 Gelman-Rubin R-1 统计量。对于多链（chain.1.txt 到 chain.4.txt），应验证链间和链内方差比 < 0.01。

---

### 5. 证伪阈值分级

| 阈值 | 解读 | 判定 |
|------|------|------|
| I_inflection < 0 at ≥ 3σ | 强支持 LP35 P2 | ✅ 合理：宇宙学中 3σ 是"证据"标准 |
| I_inflection < 0 at 2-3σ | 有趣暗示，需更多数据 | ✅ 合理：与 DESI DR2 当前精度匹配 |
| I_inflection = 0 at < 2σ | 可排除强拐点 `|d²w/dz²| > 0.3` | ⚠️ 问题：2σ 仅排除大效应；小拐点仍可能。阈值的物理含义（|d²w/dz²| > 0.3）需要论证 |
| I_inflection > 0 at ≥ 2σ | **排除 LP35 P2（方向相反）** | ✅ 正确：正 I_inflection 表示 w(z) 先升后降或单调上升——与 LP35 冻结机制逆向 |

**⚠️ 关键遗漏**: 报告讨论了 I_inflection < 0 的情形（支持 LP35）和 I_inflection = 0 的情形（null result），但 **未讨论当前实际数据所处的状态**：

**实测数据**: I_inflection = +0.952 ± 1.034（PI 测量值）= +0.921 ± 1.021（本 INSPECTOR 独立验证）
- 中心值 **为正**（与 LP35 预测方向**相反**）
- 显著性 = 0.90σ（不足 1σ）——既不能支持也不能排除 LP35
- P(I_inflection < 0) = 19.2%（只有 19% 概率为负）
- 数据更倾向于 **无拐点** 或 **正拐点**（与 LP35 预测方向相反）

报告应显式讨论这一事实，而非仅讨论假设情况。

**修正建议**: 在 §3.4 数值阈值表中加入"当前数据实际状态"一行：
```
| 当前数据 (DESI DR2 4-bin chain) | I_inflection = +0.92 ± 1.02 (0.9σ) | 尚无统计显著结论。数据倾向于 I_inflection > 0（与 LP35 P2 预测方向相反），但不确定性太大无法做任何排除 |
```

---

### 6. P1 和 P3 可行性评估诚实度

#### P1 可行性: "中低" ⭐⭐

报告列举的挑战:
- 需要定义新的因果连通性诊断量
- 星系偏袒 b(z) 的红移演化难以与控制结构增长区分
- 因果纹理没有标准观测量

✅ **诚实**。这些是真实的障碍。特别是"因果连通性不是标准 LSS 统计量"——这是一个结构性困难，不仅仅是精度问题。报告应更显式地标注：P1 目前**无法执行**，因为检验所需的观测量定义尚不存在。

**额外注**: DESI DR1 LSS catalog URL 已返回 404。如果用 eBOSS QSO 样本（z~1.5）作为代理，应在报告中说明数据访问路径。

#### P3 可行性: "中低" ⭐

报告列举的挑战:
- ISW 信噪比低（标准 ΛCDM ISW ~2-3σ）
- 区分标准 ISW 和因果纹理 ISW 需额外尺度依赖性特征
- 与修正引力（f(R), DGP）简并风险

✅ **诚实**。这些是宇宙学界公认的 ISW 检测困难。特别是 CMB 透镜-ISW 简并在小尺度上难以分离。

**额外注**: 普朗克 2018 NILC/SMICA 温度图在 PLA 上的下载需要注册账号（报告中对此未标注）。这不影响可行性评估，但影响可复现性。

#### P2 可行性: "高" ⭐⭐⭐

报告评估 P2 是最可行的（⭐⭐⭐ 高）。但在考虑到以下因素后，此评估**过高**:
1. 链是 4-bin 而非 3-bin——报告的分析方案需要重构
2. I_inflection 当前显著性仅 0.9σ——离 ≥2σ 还有实质性距离
3. 报告声称"2-4周可完成"——如果只需代码分析链文件，1-2 天即可（无需重新做 MCMC）。但若要获得 ≥2σ 结论，需要结合更多数据集（Pantheon+/DES-SN5YR 联合 MCMC），这确实需要数周。

**修正建议**: P2 可行性从 ⭐⭐⭐"高"降为 ⭐⭐"中高"（现有数据分析 1-2 天可达，但 ≥2σ 结论可能需要额外数据组合——而 Euclid DR1 才可确定性解决）。

---

### 7. 量纲/方向/循环/量级/声张缩水

由于此报告是纯数据验证文档（非理论推演），大部分 Q1-Q5 检查项不直接适用。但仍有两个需要注意的点:

#### 方向: I_inflection 正负号与 LP35 预测矛盾

这是本审查最重要的发现。报告完全未讨论 **I_inflection > 0 意味着什么**。

定性分析:
- w_bin_0 = -0.842: 最接近 -1（Δw = +0.158, ~2.2σ 偏离 ΛCDM，但偏离方向是 w > -1）
- w_bin_1 = -1.481: 最远离 -1（Δw = -0.481, ~2.4σ 偏离 ΛCDM，**w < -1**，phantom crossing）
- w_bin_2 = -1.198: 中间态（Δw = -0.198, ~0.3σ，与 ΛCDM 一致）

LP35 预测（B 博士版本，§3.3）:
- w_bin_0 (z<0.8): w > -1（偏离 ΛCDM）→ ✅ 当前数据显示这一点
- w_bin_1 (z~0.8-1.6): w ~ -1 或过渡 → ❌ 实际 w_bin_1 是 **最远离 -1 的 bin**（-1.481）
- w_bin_2 (z>1.6): w ≈ -1 → ✅ 与 ΛCDM 一致

**实际的三 bin 模式是**: w(z) 先在 z=0-0.8 接近但温和偏离 -1 (+0.16)，然后在 z=0.8-1.6 **最深地进入 phantom 区域** (-1.48)，最后在 z=1.6+ 回归。这与 LP35 预测的模式（冻结在低 z 最强）**不一致**——低 z bin 反而是最近 ΛCDM 的，中 z bin 才是偏离最大的。

#### 声张缩水

报告 §3.3 的"预测成立 vs 不成立"表合理，但应在结论中显式标注:

> "当前 DESI DR2 链数据显示 I_inflection = +0.92 ± 1.02 (0.9σ)，不构成对 LP35 P2 的统计支持。数据模式（中 z bin 显示最强 phantom crossing）与 LP35 预测的定性方向（低 z 最强冻结）不一致。需要 Euclid DR1 才能确定性检测。"

---

## 特别审查: PI 实测值与 B 博士代码复现能力

### PI 实测结果验证

PI 从 chain.1.txt 测量的值:
- `w_bin_0 = -0.842 ± 0.075`
- `w_bin_1 = -1.487 ± 0.203`
- `w_bin_2 = -1.179 ± 0.764`
- `I_inflection = +0.952 ± 1.034`

**本 INSPECTOR 独立验证**（相同 chain.1.txt，30% burn-in）:
- `w_bin_0 = -0.842 ± 0.073`  （均值差 0.000）
- `w_bin_1 = -1.481 ± 0.200`  （均值差 0.006）
- `w_bin_2 = -1.198 ± 0.754`  （均值差 0.019）
- `I_inflection = +0.921 ± 1.021`（均值差 0.031）

✅ **PI 的测量结果被精确验证。** 微小差异（< 0.03σ）可归因于: burn-in 比例微调、链合并方式（仅 chain.1.txt vs 全部 4 条链）或数值精度。

### B 博士代码是否能复现这些结果？

**部分可以，但存在以下障碍**:

#### 问题 1: Bin 数量错误（阻断级）

B 博士代码只提取前 3 个 w 参数:
```python
for i, pname in enumerate(w_params[:3]):
```

链文件有 4 个 active w 参数（w_bin_0 到 w_bin_3）。`w_params[:3]` 会遗漏 w_bin_3。如果 GetDist 参数的排列顺序与 YAML 一致，`w_params[:3]` 会拿到 w_bin_0, w_bin_1, w_bin_2（恰好是 I_inflection 所需的 3 个），但这只是巧合。更严重的是，报告对 bin 结构的描述（3 bins at [0, 0.8, 1.6, 2.4]）与实际链模型（4 active + 1 fixed）不匹配。

#### 问题 2: CPL 代码有严重 Bug（阻断级）

```python
d2w = (w15 - 2*w08 + w0_cpl) / (0.8 * 0.7 * (w0_cpl**2 + 0.01))
```

此分母有三个独立错误:
1. **`w0_cpl**2` 不应出现**。二阶导数的分母是网格间距乘积（或非均匀网格的等效因子），不应依赖于 w0 的数值。除以 `w0_cpl**2` 意味着当 w0 ~ -1 时，d2w 值被大约放大了 1 倍（巧合），但当 w0 取其他值时，结果完全不可靠。
2. **`+ 0.01` 是无物理意义的数值稳定技巧**，防止除以零。但这里 `w0_cpl**2 + 0.01` 整体作为缩放因子本来就不应该出现。
3. **非均匀网格公式错误**。对于 z=0, 0.8, 1.5（Δz1=0.8, Δz2=0.7），正确的二阶导数公式是:
   ```
   d2w/dz2 = 2 * [(w15 - w08)/0.7 - (w08 - w0)/0.8] / (0.8 + 0.7)
   ```

**正确代码应为**:
```python
# 非均匀网格二阶导数（中点差分法）
dz1 = 0.8  # z(0.8) - z(0)
dz2 = 0.7  # z(1.5) - z(0.8)
d2w_dz2 = 2.0 * ((w15 - w08)/dz2 - (w08 - w0_cpl)/dz1) / (dz1 + dz2)
```

#### 问题 3: 缺少收敛和有效样本量检查

代码未检查:
- Gelman-Rubin R-1 统计量（多链收敛）
- 有效样本量（ESS < 100 会显著影响 σ 估计的可靠性）
- `samples_binned.weights` 在 GetDist 中的属性名取决于版本（某些版本中是 `.weights` 数组，其他是 `.getWeights()`）

#### 问题 4: weight 列的实际含义

链文件的 `weight` 列包含整数权重（1, 2, 3, 4, 7...），这是 GetDist 的 thinning 权重的倒数（weight=1 表示该样本未被 thin，weight=7 表示该样本代表 7 个连续链步）。Dr. B 的代码使用 `np.average(x, weights=weights)` 是正确的。

#### 复现路径修复建议

若正确使用以下修正，B 博士代码 **可以** 复现 PI 的结果:

```python
# 修正 1: 确认 4-bin 结构，使用正确的 3 个 bin 计算 I_inflection
# （如果 LP35 拐点在 z~0.8，使用的应该是 w_bin_0, w_bin_1, w_bin_2 没问题，
#  但必须显式确认 bin 边界对应关系）

# 修正 2: 先检查参数列表
param_names = samples_binned.getParamNames().list()
w_params = [p for p in param_names if p.startswith('w_bin_')]
print(f"Available w bins: {w_params}")  # 预期: ['w_bin_0', 'w_bin_1', 'w_bin_2', 'w_bin_3']

# 修正 3: 正确提取并计算 ESS
weights = samples_binned.samples['weight']
ess = np.sum(weights)**2 / np.sum(weights**2)
print(f"Effective sample size: {ess:.0f}")

# 修正 4: 用正确的非均匀网格公式计算 CPL 曲率
```

---

## 阻断与警告汇总

| # | 等级 | 位置 | 内容 |
|---|------|------|------|
| **⛔1** | 阻断 | §3.1-3.2 | 报告将链描述为 3-bin 模型 [0, 0.8], [0.8, 1.6], [1.6, 2.4]，但实际链文件有 4 个 active w bins (w_bin_0 到 w_bin_3，w_bin_4 固定)。Bin 数量错误导致 I_inflection 定义与链模型不匹配 |
| **⛔2** | 阻断 | §3.2 Step 4 | CPL 曲率代码有严重 Bug：分母 `(0.8 * 0.7 * (w0_cpl**2 + 0.01))` 将 w0 的平方作为归一化因子（无物理依据），且使用了错误的非均匀网格有限差分公式 |
| **⛔3** | 阻断 | §3.3-3.4 | 报告未讨论当前实际数据的核心事实：I_inflection = +0.95 ± 1.03 (PI 实测)，中心值为正（与 LP35 预测的负值方向相反）。PI 已验证此结果。报告仅讨论了假设性阈值，未分析实际链数据给出的信号 |
| **⚠️1** | 警告 | §1.1 | DESI DR1 LSS catalog URL (`.../LSS/iron/LSScats/`) 返回 404。报告应更新为有效访问路径或标注需 DESI Data Portal 认证 |
| **⚠️2** | 警告 | §3.1 | DESI DR2 chain URL 只列到 `bao-cosmo-params/` 目录，但实际链文件在 `cobaya/base_w-binned-3uniform/{超长子目录名}/` 下。报告的 wget 命令会下载整个目录树，但本地路径可能与硬编码的 `DATA_COMBOS[0]` 不匹配 |
| **⚠️3** | 警告 | §3.2 | 代码未计算有效样本量 (ESS)，未做 Gelman-Rubin 收敛检验。ESS = 12,587 / 21,000 = 60% — 汇报 σ 时应注明 ESS 影响 |
| **⚠️4** | 警告 | §3.3 | §3.3 的数据引用 "DESI DR2的3-bin w(z)重建 (arXiv:2506.22953)" — 该论文作者使用 n=3, 4, 5 三种 binning，不是只用 3-bin。引用不精确 |
| **⚠️5** | 警告 | §2.2 | P2 可行性 "高" ⭐⭐⭐ 偏高。当前数据仅给出 0.9σ 的 I_inflection 信号。若目标为 ≥2σ 结论，仅靠链后处理不足——需联合 MCMC 包含 Pantheon+/DES-SN5YR，工作量超出"2-4周链分析"范畴 |
| **⚠️6** | 警告 | §1.5 | Union3 标注为 "⚠️ 部分" 公开——实际上 Rubin+ (2023) arXiv:2311.12098 论文公开，但正式的 supplementary data 文件可能需要从论文页面或作者处获取。标注合理但应说明"部分"的含义（方法 vs 完整数据向量） |
| **⚠️7** | 警告 | §3.5 | 代码中 `DEBUG_COMBOS[0]` 目录名约 120 字符——在 Windows 文件系统上可能超出 `MAX_PATH` (260 字符) 限制，导致文件无法访问。应使用 `\\?\` 前缀或缩短路径 |

---

## 附录: 链文件实测数据卡

以下为 INSPECTOR 独立实测结果，用作交叉验证基准:

```
数据源: DESI DR2 chain.1.txt (30,000 样本)
Burn-in: 30% (9,000 样本丢弃)
有效样本量 (Kish ESS): 12,587 (~60%)

w_bin_0 = -0.842 ± 0.073  [P(w_bin_0 > -1) = 98.5%]
w_bin_1 = -1.481 ± 0.200  [P(w_bin_1 > -1) =  1.3%]
w_bin_2 = -1.198 ± 0.754  [P(w_bin_2 > -1) = 39.3%]
w_bin_3 = -1.885 ± 0.735  [P(w_bin_3 > -1) = 12.8%]

I_inflection (3-bin)  = +0.921 ± 1.021  [|I|/σ = 0.90]
I_inflection (4-bin)  = +0.139 ± 1.336  [|I|/σ = 0.10]
  (4-bin: w_bin_1 - 2*w_bin_2 + w_bin_3)

Corr(w0,w1) = -0.590
Corr(w0,w2) = +0.132
Corr(w1,w2) = -0.428

ΛCDM偏差 (Δw = w + 1):
  Δw0 = +0.158 ± 0.073  (2.2σ from ΛCDM, w > -1)
  Δw1 = -0.481 ± 0.200  (2.4σ from ΛCDM, w < -1, phantom)
  Δw2 = -0.198 ± 0.754  (0.3σ from ΛCDM, 一致)
  Δw3 = -0.885 ± 0.735  (1.2σ from ΛCDM)

LP35 P2 预测模式: 低z bin最强偏离ΛCDM, 中z过渡, 高z回归
实际模式: 低z bin温和偏离(+0.16), 中z bin最强phantom crossing(-0.48), 高z回归
→ 模式方向与LP35预测不完全一致
```

---

*INSPECTOR 校对完成。报告写入 `D:\Claude\ai-reservations\LP35-Causal-Glass\synthesis\inspector_B_dataver.md`*
