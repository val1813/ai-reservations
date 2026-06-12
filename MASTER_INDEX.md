# AI科研系统 — 全课题总目录

> 更新：2026-06-12 | 49个课题 | 4个子系统

---

## 一、基础设施

| 目录 | 职能 | 核心文件 |
|------|------|---------|
| `ai/` | 科研窗口核心提示词 | `CLAUDE.md`(SOP入口), `PI.md`(PI操作), `A_AGENT.md`, `B_AGENT.md`, `INSPECTOR.md`, `REVIEWER.md`, `AUDITOR.md`, `AHA.md`, `WALL_BREAKER.md`, `EMBER_REKINDLER.md`, `Phase清单模板.md` |
| `ai2/` | 选题系统 | `SELECTOR.md`(中央选题流程) |
| `ai3/` | 院长系统 | `DEAN.md`(院长复盘) |
| `ai4/` | 论文自动化 | PaperSpine子模块 |
| `shared/` | 跨课题共享 | `北极星候选池.md`, `知识库汇总.md`, `学术指导.md`, `搁置命题.md` |
| `knowledge_graph/` | 知识图谱 | 跨课题结论JSON连接 |
| `polaris/` | 北极星优先级 | 矩阵量化打分系统 |

---

## 二、方法论沉淀

| 方法论 | 来源 | 核心原则 |
|--------|------|---------|
| SOP对抗审查 | `ai/CLAUDE.md` | Phase清单驱动，最低3轮，INSPECTOR/REVIEWER独立Agent |
| 选题SELECTOR | `ai2/SELECTOR.md` | 北极星优先级矩阵，长命题优先，S1+S2先行 |
| 墙破机制 | `ai/WALL_BREAKER.md` | 墙分类(Type A/B/C)，6策略破墙 |
| 复燃机制 | `ai/EMBER_REKINDLER.md` | 课题死后抢救：抢救评估→核心价值→距离→可行性 |
| 3D破局模板 | NS+DGF经验 | ①换表示(拉格朗日/谱) ②找天然有界量 ③对称性推普适形式 ④枚举最小相边界 |

---

## 三、LP课题 (按编号)

### LP1-LP9: 凝聚态/量子物理

| LP | 课题 | 状态 | 关键产出 |
|----|------|------|---------|
| LP1 | 2D MBL热力学稳定性 | ✅已解决 | 雪崩自限性+罕见热区逾渗+准周期势机制 |
| LP2 | Planckian dissipation普适性 | 🔄进行中 | α系统meta-analysis (S1有边界) |
| LP3 | ν=5/2 bulk-edge correspondence | 🔄进行中 | Tradeoff定理+Onsager bulk上界 |
| LP4 | 非厄米多体趋肤效应(NHSE) | — | — |
| LP5 | DQCP真正连续vs弱一阶 | — | — |
| LP6 | 黑洞信息悖论 | — | — |
| LP7 | 量子力学-广义相对论冲突→统一 | — | — |
| LP8 | MIPT测量诱导相变 | — | — |
| LP9 | 离散时间晶体(DTC) | — | — |

### LP10-LP29: 凝聚态/量子材料/宇宙学

| LP | 课题 | 状态 |
|----|------|------|
| LP10 | 平带超导 | — |
| LP11 | Muon g-2 HVP | — |
| LP12 | 量子疤痕 | — |
| LP14 | Altermagnetism | — |
| LP15 | 超导绝缘量子相变 | — |
| LP16 | 范畴Landau理论 | — |
| LP17 | CMB量子相干双谱 | — |
| LP18 | 含噪自由费米子输运 | — |
| LP19 | 孤子耗散 | — |
| LP23 | 螺旋世界线 | — |
| LP24 | Euler统一 | — |
| LP25 | FCS量子基础/断裂/恒等公式 | — |
| LP26 | 铜氧化物SFD | — |
| LP27 | T-linear NFL | — |
| LP28 | 镍酸盐层解耦 | — |
| LP29 | 非晶带 | — |

### LP30-LP47: DGF框架 (消相干几何框架)

| LP | 课题 | 状态 | 关键产出 |
|----|------|------|---------|
| LP30 | DGF基础公理 | ✅定理 | 投影角定理、时间单向性定理、q场方程 |
| LP31 | 信息容量 | — | — |
| LP32 | 宇宙热寂 | — | Reflux界定理、黑洞熵面积律 |
| LP33 | Euclid涌现 | — | EPP No-Go |
| LP34 | Aporia机制 | — | — |
| LP35 | 因果玻璃 | — | — |
| LP36 | W因果积累 | — | CFOL充要条件(d=2)、b₁标度 |
| LP37 | DGF宇宙拓扑 | — | CFOL充要条件完成 |
| LP38 | α起源/QCMI精密 | — | η₀=1/(8ln2)、多边环Fawzi-Renner下界 |
| LP39 | DGF物理接口 | — | 微观→宏观RG流(Wall #3核心) |
| LP40 | DGF RG流 | — | 初步尝试但统计不显著 |
| LP41 | CFOL推广/空间维度 | — | d>2推广(猜想η₀(d)=η₀(2)/d²) |
| LP42 | 幽灵零 | — | — |
| LP43 | DGF引力唯象 | — | — |
| LP44 | DGF经典性 | — | — |
| LP45 | Gram关联退相 | — | — |
| LP46 | μ*普适性 | 🔄进行中 | SELECTOR S1产出 |
| LP47 | 因果环信息局域化 | — | — |

### DGF-Survivors (精选存活课题)

| 文件 | 内容 |
|------|------|
| `DGF_MASTER_SUMMARY.md` | 5个严格定理+推导链+数值结果 |
| `03-walls-to-break.md` | 10个待攻墙的完整清单 |
| `walls/` | Wall #2(b₁推广), #3(RG流), #5(指针基), #7(T2回流), #9(QCMI→退相干) 的攻击报告 |
| `roadmaps/` | RG突破口、宏观扩展路线 |
| `papers/` | PRL手稿、文献定位、诚实推导树 |
| `scripts/` | 数值工具(rg_flow, discrete_poisson_enum, cat2系列, wall攻击脚本) |

---

## 四、非LP专项

| 目录 | 内容 |
|------|------|
| `CEP-Causal-Economy/` | 因果经济学 |
| `IND/` | 独立课题(已结案/转向) |
| `aixsci/` | AI×科学交叉 |
| `l30-deepseek/` | DeepSeek相关 |
| `投稿须知/` | 期刊投稿规范 |

---

## 五、方法论工具箱

### NS千禧年问题（2026-06-11~12，D:\Claude下）

| 工具 | 文件 | 功能 |
|------|------|------|
| κ_τ三元组分类 | — | 共线triad=无涡旋拉伸 (DNS验证: 13数量级差异) |
| 无条件|T|上界 | — | |T|≤C₁/τ^(3/2)D^(3/2)+... 仅用τ>0 |
| 拉格朗日归约 | — | D_t ω_L=νF⁻¹Δ(Fω_L) — 涡旋拉伸精确消失 |
| 几何对齐诊断 | — | H1_std×H6_pos_frac → R²=0.9994预测η |
| Gevrey-Gibbon猜想 | — | κ_τ层次闭合 + m_*~log(1/ν)标度 |

### DGF框架（2026-06-12，D:\Claude下）

| 工具 | 文件 | 功能 |
|------|------|------|
| 谱维度检测 | `dgf_spectral_tool.py` | 输入邻接矩阵→输出d_eff+收敛条件 |
| RG标度律 | `dgf_rg_spectral.py` | D(L)~L^{-2.58} 扩散衰减标度 |
| EFT推导 | `dgf_eff_field_theory.md` | 对称性→q场方程 无需枚举 |
| 度规修正 | `dgf_metric_derivation.md` | q=exp(-Φ) 1PN匹配GR (β=γ=1) |
| Caticha桥 | `dgf_caticha_bridge.py` | 熵动力学→Schrödinger 三层结构 |
| d_eff相边界 | — | 平均度20-70→3D涌现 (跨4种图类型验证) |

---

## 六、快速入口

```
新课题:  读 ai/CLAUDE.md → 读 shared/北极星候选池.md → 选北极星
继续科研: 说"继续科研" → 自动加载Phase清单
选题:     读 ai2/SELECTOR.md → 执行S1+S2
破墙:     说"破墙" → 触发WALL_BREAKER
复燃:     说"复燃" → 触发EMBER_REKINDLER  
写论文:   读 ai4/ → PaperSpine流程
院长复盘: 读 ai3/DEAN.md
```
