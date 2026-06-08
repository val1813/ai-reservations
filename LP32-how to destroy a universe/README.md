# LP32 — How to Destroy a Universe (DGF框架)

**长命题编号：** LP32
**框架：** DGF (Discrete Graph Framework) — 从信息因果到引力与量子力学的统一
**状态：** 2篇论文投稿中（PRD + PRL S1），新增1个子命题（S1: QM-from-Permutation）
**日期：** 2026-06-07

---

## 目录结构

```
LP32-how to destroy a universe/
├── README.md                          # 本文件
├── paper/                             # 论文
│   ├── two_rules_prd_final.tex        # DGF主论文 (PRD投稿)
│   ├── supplemental_prd_final.tex     # 补充材料
│   ├── prl_decoherence.tex            # 退相干PRL论文
│   ├── prl_s1.tex                     # S1定理PRL论文
│   ├── prl_s1_sm.tex                 # S1补充材料
│   ├── cover_letter_prl_s1.tex       # PRL投稿信
│   └── dgf_decoherence_verification.png
├── experiments/                       # 数值实验
│   └── S1_ibm_noise/                 # S1定理IBM量子噪声验证
│       ├── S1_ibm_noise.py/v2/v3
│       ├── S1_ibm_result.png/v2/v3
│       └── prl_decoherence_verify.py
├── current/                           # 当前工作状态
│   └── plan/                         # Phase清单
├── project/                           # 项目管理
│   └── 北极星队列.md
├── synthesis/                         # 综合报告
│   └── DGF_complete_summary.md       # DGF框架完整讨论总结
└── LP32-S1_QM-from-Permutation/      # 子命题S1
    ├── SELECTOR_entry.md             # SOP标准选题条目
    ├── AB_verification.md            # AB双博士验证
    ├── core_derivation.md            # 核心推导（从A1+A2→QM）
    ├── self_attack.md                # 自我攻击+文献交叉验证
    └── conclusions.md                # 可操作结论+框架修改建议
```

## 框架概要

**两条公理：** A1（因果存在）+ A2（容量有界1 bit/格点）。A3（因果视界）已降格为定理（S4证明可从A1+A2导出）。

**核心变量：** q = 未占用格点/总格点 ∈ [0,1]

**主要成果：**
- 统一telegraph方程：∂²_t q + γ₀(1-q)∂_t q = c²∇²(ln q)
- 静态极限→牛顿引力：q(r) = e^(-GM/rc²)
- Lorentz不变性由真空动态选择
- H-theorem（Lyapunov泛函）
- S1定理：P_reflux ≤ q_S/q_E

**已知局限（论文诚实声明）：**
- 依赖Zilly (2026)作为QM基础
- 全息张力（体积vs面积标度）
- 只能恢复牛顿极限（非完整GR）
- γ(q)=γ₀(1-q)是ansatz

## 新增工作（2026-06-07）

**LP32-S1：从置换动力学导出QM** — 消除Zilly依赖

- 新增A3公理（格点身份不可区分性）
- 完整推导链：A1+A2+A3 → QM全数学结构
- AB验证通过（2/6，刚好存活）
- 最大缺口：Kochen-Specker语境性证明（待完成）
