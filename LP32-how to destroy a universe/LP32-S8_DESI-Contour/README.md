# LP32-S8 — DGF Dark Energy vs DESI DR2

**状态:** 6轮恶意审稿完成 → nature-polishing → 可投稿
**最终文件:** `paper/main_nature_polished.tex`

## 核心发现

自洽迭代是关键。驱动主导近似产生w(z)穿过零线的错误预言。自洽求解揭示负反馈抑制偏离ΛCDM至~2%。

| 指标 | ΛCDM (自由r_d) | DGF n=1 (自由r_d) |
|------|---------------|-------------------|
| χ² | 15.0 | 19.1 |
| r_d (Mpc) | 148.6 | 146.0 |
| AIC | 17.0 | 25.1 |
| ΔAIC | 0 | **+8.1** (ΛCDM preferred) |

**结论:** 模型未被排除，但不被偏好。关键可证伪预言：w(z)非单调峰。

## 审稿历程

| 轮次 | 发现 |
|------|------|
| R1 | CPL投影wa始终为正(+2.0)，挽救轮wa=-0.51是错的 |
| R2 | 驱动主导w(z)穿过零线，~18σ张力，被数据排除 |
| R3 | 必须做自洽迭代 |
| R3修复 | 自洽迭代收敛，负反馈抑制峰幅3倍 |
| R4 | 联合残差正确计算，C收敛验证 |
| R5 | 自由r_d对比：ΔAIC=+8.1倾向ΛCDM |
| R5修复 | n扫描，诚实报告 |
| R6 | AIC算术修正，补充材料需更新，代码需提交自洽迭代 |

## 目录

```
├── paper/main_nature_polished.tex   ← 最终投稿稿
├── code/generate_figures.py         ← 图生成
├── data/contour_package.json        ← 数值数据
├── figures/                         ← 图(png+pdf)
├── synthesis/                       ← 审稿综合
│   ├── REVIEWER_ROUNDS.md           ← 6轮审稿历程
│   └── NP_WRITING_ANALYSIS.md       ← Nature Physics写作分析
└── experiments/                     ← 开发代码(历史)
```
