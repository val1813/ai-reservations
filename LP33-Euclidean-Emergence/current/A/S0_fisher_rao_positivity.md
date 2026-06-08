# S0 结论报告: Fisher-Rao正定性定理

> 执行者: A博士 (学院派)
> 日期: 2026-06-08
> 判定: ✅ 成立
> 依赖: 无 → 解锁S1和S3

---

## 核心结论

**Fisher-Rao度量在任何正则的实值光滑概率分布族上是严格Riemannian的。**

号差恒为 (+,+,...,+)。零特征值仅对应参数化冗余。负特征值永不出现。

## 数学链

1. **g_ij = Cov[s_i, s_j]**: Fisher信息矩阵是score functions的协方差矩阵
2. **v^i g_ij v^j = Var[v^i s_i] ≥ 0**: 实L^2空间中协方差必半正定
3. **线性独立→严格正定**: 参数化无冗余时score functions线性独立→Cov>0
4. **负特征值不可能**: 实L^2内积 (f,f)≥0恒成立

## 边界情况

| 情况 | 结果 | 影响 |
|------|------|------|
| 离散分布(多项/Dirichlet) | 严格正定 | 无 |
| 奇异分布(支撑依赖参数) | Fisher-Rao可能不存在(非不定) | 正则条件边界 |
| 无穷维流形 | 协方差算子正定(弱Riemannian) | 技术性退化≠不定号差 |
| 混合模型 | 正半定,边界降秩(冗余) | 无 |

## 反例搜索: 零发现

- Alshal (2023): "pseudo-Riemannian Fisher" — 需要**复指数族**。实值部分仍Riemannian
- Wong-Yang (2021): Kim-McCann伪Riemannian (n,n)几何 — Fisher-Rao是其在子流形上的**Riemannian限制**
- 量子Fisher信息: 非交换概率→不在实值范围内

**所有声称的伪Riemannian Fisher构造都需要复值或量子扩展。**

## 对S1的影响

S1的推广路径: 任何从实L^2内积导出的度量→正定。无向实值结构的协方差型度量共享此性质。

找到反例的唯一方式: 使用非Fisher-Rao度量(α-联络)或非实结构(复化/量子)。

## 关键文献

1. Čencov (1972/1982): 唯一性定理
2. Amari & Nagaoka (2000): 标准教材
3. Le (2016): 强连续性→唯一Fisher
4. Bauer, Bruveris, Michor (2016): 微分同胚不变→Fisher
5. Le Brigant et al. (2020): Dirichlet Fisher-Rao显式计算
6. Wong & Yang (2021): 伪Riemannian OT嵌入≠Fisher本身
7. Alshal (2023): 复扩展→Lorentzian
