# S3 结论报告: 量子信息度量边界检验

> 执行者: B博士 (野路子)
> 日期: 2026-06-08
> 判定: EPP扩展到量子域 — 量子信息度量也正定
> 依赖: S0(已解锁) → 为S4提供量子边界

---

## 核心结论

**Petz分类定理(1996)证明: 所有满足单调性的量子Fisher度量都在SLD(上界)和RLD(下界)之间, 全部是Riemannian正定度量。**

EPP不仅适用于经典信息论——也适用于量子信息论。

## 量子Fisher度量逐一检验

| 度量 | 正定? | 依据 |
|------|:--:|------|
| SLD Fisher | ✅ | Petz分类中的最大单调度量 |
| RLD Fisher | ✅ | Petz分类中的最小单调度量 |
| Bures/保真度 | ✅ | Riemannian浸没从正定矩阵空间 |
| Wigner-Yanase偏斜 | ✅ | 单调性→正定 |
| 所有Petz单调度量 | ✅ | 在SLD和RLD之间连续统 |

**零清洁反例。** 无任何论文声称标准量子信息度量可产生不定号差。

## Calmet & Calmet (2004)分析

- 从复数概率分布→Lorentzian号差 diag(-1,1,1,1)
- **不是反例**: 复数"概率"放弃Kolmogorov非负性公理
- 复数分布=量子/非Hermitian假设,不是信息论操作
- 经典Fisher信息(实概率)→永远正定; 复数化→Lorentzian

## 关键区分

| 操作 | 领域 | 号差 |
|------|------|:--:|
| 经典Fisher(实概率) | 信息论 | (+,+,+,+) |
| 量子Fisher(SLD/RLD/Bures/WY) | 量子信息论 | (+,+,+,+) |
| 复数概率Fisher(Calmet) | 量子物理 | (-,+,+,+) |
| 伪Riemannian OT(Wong-Yang) | 最优传输 | (n,n),非信息度量 |

## 对S4的影响

1. **EPP比最初设想的更强**: 经典+量子信息度量→必然Riemannian
2. **Lorentzian号差的唯一路径**: 必须跳出信息论框架→复数化或量子引力特有结构
3. **"第一个Determination"的核心张力**: 如果信息论(经典+量子)都不能产生Lorentzian, 那什么可以?

## 关键文献

1. Petz (1996): 分类定理。Linear Algebra Appl. 244:81-96 (437引用)
2. Calmet & Calmet (2004): 复数Fisher→Lorentzian
3. Wong & Yang (2019): 伪Riemannian OT嵌入
4. Bengtsson & Zyczkowski (2006): 量子态几何标准参考
