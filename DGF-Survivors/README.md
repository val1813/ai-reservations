# DGF Survivors — LP30-LP47 成果整理

**整理日期:** 2026-06-12
**范围:** LP30 (DGF起源) → LP47 (因果环信息局域化)，18个子课题
**总摘要:** [DGF_MASTER_SUMMARY.md](DGF_MASTER_SUMMARY.md)

---

## 目录结构

```
DGF-Survivors/
├── DGF_MASTER_SUMMARY.md          ← 总摘要 (从这里开始)
├── README.md                      ← 本文件
├── STATUS_2026-06-10.md           ← 最新进度
│
├── theorems/                      ← 定理级结果
│   ├── 06-cfol-sufficiency-calc.md
│   ├── 17-eta0-derivation.md
│   └── Gamma0_derivation.md
│
├── walls/                         ← 墙攻击报告
│   ├── 03-walls-to-break.md
│   ├── 14-wall7-attack.md
│   ├── 15-wall9-attack.md
│   ├── 16-wall2-attack.md
│   └── 18-wall5-attack.md
│
├── experiments/                   ← 实验验证
│   ├── 19-ibmq-hardware-results.md
│   └── 21-experimental-framework.md
│
├── papers/                        ← 论文资产
│   ├── S1_PRL_manuscript.md
│   ├── S1_PRL_SM.md
│   ├── S1_PRL_cover_letter.md
│   └── LITERATURE_POSITIONING.md
│
├── roadmaps/                      ← 路线图
│   ├── 04-directions-forward.md
│   └── 08-macro-extension-roadmap.md
│
├── supplements/                   ← 补充材料
│   ├── 12-computational-supplements.md
│   ├── 13-literature-supplements.md
│   └── 20-lp38-analytical-supplements.md
│
├── inspector_reviewer/            ← 审计报告
│   ├── 07-cfol-inspector-review.md
│   ├── 10-b1-inspector-review.md
│   ├── INSPECTOR_RG_R2.md
│   └── INSPECTOR_decoherence_amplifier.md
│
├── _surveys/                      ← 调查记录
│   ├── _survey_LP30-LP35.md
│   └── _survey_LP36-LP47.md
│
├── archive/                       ← 归档
│   └── superseded/                ← 已被替代的文件
│       ├── 11-wall-ab-verified.md
│       └── 12-reviewer-response.md
│
├── scripts/                       ← Python脚本
├── paper1-prl/                    ← PRL论文工作目录
├── papers/                        ← 参考文献PDF
├── future/                        ← 未来方向
└── time_perception/               ← 时间感知专题
```

---

## 核心文件索引（原编号系统）

| # | 文件 | 内容 |
|---|------|------|
| 01 | 01-established-results.md | 立得住的成果（按置信度分级） |
| 02 | 02-disproven-abandoned.md | 已证伪/中断的成果 |
| 03 | 03-walls-to-break.md | 待攻克的理论墙（详见walls/） |
| 04 | 04-directions-forward.md | 可继续推进的方向（详见roadmaps/） |
| 05 | 05-literature-context.md | 文献定位与先发分析 |
| 06 | theorems/06-cfol-sufficiency-calc.md | CFOL充分性完整解 |
| 07 | inspector_reviewer/07-cfol-inspector-review.md | INSPECTOR+REVIEWER审计 |
| 08 | roadmaps/08-macro-extension-roadmap.md | 宏观推广路线图 |
| 09 | 09-b1-scaling-results.md | b₁标度结果 |
| 10 | inspector_reviewer/10-b1-inspector-review.md | b₁ INSPECTOR审计 |
| 11 | archive/superseded/11-wall-ab-verified.md | 已被13替代 |
| 12 | supplements/12-computational-supplements.md | 计算补足 |
| 12 | archive/superseded/12-reviewer-response.md | REVIEWER回应(已过时) |
| 13 | supplements/13-literature-supplements.md | 文献补充 |
| 13 | 13-wall-ab-corrected.md | Wall A+B修正终版 |
| 14 | walls/14-wall7-attack.md | Wall #7攻击 |
| 15 | walls/15-wall9-attack.md | Wall #9攻击 |
| 16 | walls/16-wall2-attack.md | Wall #2攻击 |
| 17 | theorems/17-eta0-derivation.md | η₀推导 |
| 18 | walls/18-wall5-attack.md | Wall #5攻击 |
| 19 | experiments/19-ibmq-hardware-results.md | IBM Q硬件实测 |
| 20 | supplements/20-lp38-analytical-supplements.md | LP38解析补充 |
| 21 | experiments/21-experimental-framework.md | 实验框架 |
| 22 | 22-sin2phi-and-rho-verification.md | sin²φ验证 |
| 23 | 23-theta2-error-bounds.md | θ²误差界 |
| 24 | 24-cfol-nonaligned-extension.md | CFOL非对齐推广 |

---

## 课题发展弧线

```
LP30: DGF原始框架（attractor定理证伪→重定位为v6四层体系）
LP31: J-电流引力波（标量vs张量极化→可检验差异）
LP32: DGF大综合（6子命题+10桥接假设）
LP33: 欧几里得涌现（构造失败→发现Cencov-Petz+EPP否定框架）
LP34: Aporia机制（从"推导正确理论"翻转为"排除错误理论"）
LP35: 因果玻璃暗能量（AG证伪+DESI w(z)非单调）
LP36: DGF宣言（五项支柱: CFOL+η₀+对易性+指针基+经典/量子分离）
LP37: 宇宙拓扑（CFOL墙: 必要性已证明→充分性突破2026-06-09）
LP38: QCMI精确定量（η₀=1/(8ln2)确认+IBM Q实测+CCQ证伪）
LP39: 物理接口（Λ/Hubble/黑洞三项诚实否定）
LP40: RG数值实验（统计不显著, 方法学教训）
LP47: 因果环信息局域化（QCMI标度律→二部图宇称选择，未到达质量/引力）
```

---

## 全局判断

**已确立的**: CFOL充要条件(定理级)、投影角定理(定理级)、时间单向性定理(定理级)、Reflux界(定理级)、θ²ln(1/θ)标度律(解析+数值)、η₀=1/(8ln2)(渐近最优)、IBM Q硬件验证(S/N>600)、GW 2PN预言(4%偏差)、DESI w(z)连接(χ²=1.8 vs ΛCDM 17.3)

**核心缺口**: 微观→宏观RG流(Wall #3, 10⁶¹标度鸿沟)、d=3推导、𝔩独立确定、薛定谔/爱因斯坦方程涌现

**诚实定位**: DGF从信息论公理出发，在微观因果环网络上建立了因果拓扑→量子非马尔可夫性的精确定量理论。在静态球对称极限+校准后给出可检验的引力预言。框架不声称推导时空、量子力学或引力——这些是开放目标。
