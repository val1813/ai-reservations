# ai-reservations 项目目录

> AI科研系统全部课题与基础设施
> 更新日期：2026-06-01

---

## 目录结构

```
ai-reservations/
├── ai/         科研窗口核心提示词（CLAUDE.md, PI.md, AHA.md, REVIEWER.md...）
├── ai2/        选题系统（SELECTOR.md）
├── ai3/        院长系统（DEAN.md）
├── shared/     跨课题共享文件（候选池、知识库汇总、学术指导、机制日志）
├── knowledge_graph/   知识图谱JSON（跨课题结论连接）
│
├── LP1-MBL2D/          长命题1：2D MBL热力学稳定性
├── LP2-Planckian/      长命题2：Planckian dissipation普适性
├── LP3-Nu5half/        长命题3：ν=5/2 bulk-edge correspondence
├── LP4-NHSE/           长命题4：非厄米多体趋肤效应
├── LP5-DQCP/           长命题5：DQCP真正连续还是弱一阶
├── LP6-BlackHoleInfo/  长命题6：黑洞信息悖论
├── LP7-QMGRUnification/ 长命题7：量子力学-广义相对论冲突到统一公式
│
└── IND/        独立课题（已结案/已转向）
```

---

## LP1-MBL2D：2D MBL热力学稳定性 ✅已解决

子命题完整，综合推导完成。院长评级A（附带补强条件）。

| 子目录 | 子命题 | 状态 |
|--------|--------|------|
| `LP1-S1_MBL-Avalanche/` | LP1-S1 雪崩自限性 | ✅已解决 |
| `LP1-S2_MBL-RareRegion/` | LP1-S2 罕见热区逾渗 | ✅已解决 |
| `LP1-S3_MBL-Quasiperiodic/` | LP1-S3 准周期势机制 + LP1综合推导 | ✅已解决 |
| `LP1-S4_MBL-Experiment/` | LP1-S4 实验区分能力 | ✅已解决 |

**综合推导文件：** `LP1-S3_MBL-Quasiperiodic/synthesis/LP1-综合推导.md`

---

## LP2-Planckian：Planckian dissipation普适性 🔄进行中

S1有边界结案，S2连续两次BLINDSPOT阻断，面临北极星溶解风险。院长评级B+（降级风险）。

| 子目录 | 子命题 | 状态 |
|--------|--------|------|
| `LP2-S1_Planckian-alpha/` | LP2-S1 α系统meta-analysis | ✅有边界 |
| `LP2-S2_Planckian-Framework/` | LP2-S2 理论框架比较 | 🔄Phase 3待执行 |

---

## LP3-Nu5half：ν=5/2 bulk-edge correspondence 🔄进行中

S1完成tradeoff定理+Onsager bulk上界。院长评级B+。

| 子目录 | 子命题 | 状态 |
|--------|--------|------|
| `LP3-S1_Nu5o2-EdgeThermal/` | LP3-S1 热输运非拓扑修正 | ✅有边界 |
| `LP3-S2_Nu5o2-Mapping/` | LP3-S2 映射稳定性 | 🔄进行中 |

---

## LP4-NHSE：非厄米多体趋肤效应 🔄进行中

S1完成Stinespring母框架+方向反转相变。院长评级B+。

| 子目录 | 子命题 | 状态 |
|--------|--------|------|
| `LP4-S1_NHSE-TopoUnify/` | LP4-S1 Lindbladian/postselected统一 | ✅有边界（v1+v2） |

---

## LP5-DQCP：DQCP真正连续还是弱一阶 🔄进行中

S1+S4均有边界结案，S2/S3需重新表述。

| 子目录 | 子命题 | 状态 |
|--------|--------|------|
| `LP5-S1_DQCP-Entanglement/` | LP5-S1 纠缠熵诊断鲁棒性 | ✅有边界 |
| `LP5-S4_DQCP-Complex/` | LP5-S4 复DQCP（4版本7Phase） | ✅有边界 |

---

## LP6-BlackHoleInfo：黑洞信息悖论 🆕进行中

最新认领。院长评级B+（潜力A）。

| 子目录 | 子命题 | 状态 |
|--------|--------|------|
| `LP6-S1_NESS-MerminWagner/` | LP6-S1 无质量引力岛屿 | 🔄进行中 |
| `LP6-S3_Hawking-Encoding/` | LP6-S3 信息编码微观机制 | 🔄进行中 |

---

## LP7-QMGRUnification：量子力学-广义相对论冲突到统一公式 ✅结构性收官

用户手动布置长命题，已完成 S1-S10。

核心结论：未确认终极统一动力学方程；已确认六通道候选准入图谱：

`Theory T -> I[T] -> J_unify[I[T]]`

其中 `I[T]=(Phi_source,Phi_mediator,Phi_noise,Phi_entropy,Phi_obs,Phi_frame)`。

后续只做具体候选理论 `T` 的六通道代入测试，不继续抽象扩块。

---

## IND：独立课题（已结案/转向）

非长命题的历史课题，按结案状态保留。

| 子目录 | 课题 | 评级 | 状态 |
|--------|------|------|------|
| `IND_BMV/` | 引力量子性判定树（14版本） | B | ✅结案 |
| `IND_Quantum-Mimicry/` | 量子引力模拟（5版本） | B | ✅结案 |
| `IND_v2-deepseek/` | 强耦合熵产生（10版本） | B | ✅结案 |
| `IND_v2-claude/` | （早期课题） | — | ✅结案 |
| `IND_bath-coupling/` | 浴耦合图拓扑（4版本） | B | ✅结案 |
| `IND_Schwarz-only/` | Schwarz条件唯一性（8版本） | C+ | ✅结案 |
| `IND_quantum-relativity-unification/` | 因果集QFT（13版本） | B | ✅v13 Phase1提前关闭 |
| `IND_KD-Graphene/` | 石墨烯ν=0热输运 | B+ | ✅结案 |
| `IND_Kaon-Isospin/` | K介子同位旋异常 | C | ✅结案（证伪） |
| `IND_Kagome-NQS/` | Kagome NQS | C | ✅转向否定性路线 |
| `IND_Beta-Ta-ShotNoise/` | β-Ta散粒噪声 | — | ✅有边界 |
| `IND_1D-CuO-RIXS/` | 1D铜氧化物RIXS | — | ✅结案（证伪） |

---

## 命名规范

**长命题（LP）：**
- 父目录：`LP{编号}-{英文简称}/`
  - 例：`LP1-MBL2D/`, `LP2-Planckian/`
- 子命题目录：`LP{编号}-S{子编号}_{原课题名}/`
  - 例：`LP1-S1_MBL-Avalanche/`, `LP3-S2_Nu5o2-Mapping/`

**独立课题（IND）：**
- 目录：`IND_{原课题名}/`
  - 例：`IND_BMV/`, `IND_KD-Graphene/`

---

## 杂项文件

| 文件 | 说明 |
|------|------|
| `AGENTS.md` | Agent配置说明 |
| `北极星选题报告_2026-05-30.md` | 历史选题报告 |
| `ai-reservations.zip` | 备份压缩包 |
