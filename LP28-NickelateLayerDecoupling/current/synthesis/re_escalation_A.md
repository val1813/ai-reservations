# LP28 Re-escalation A: 收尾理论声张重构

身份：A博士  
任务性质：LP28 收尾 re-escalation，不是新一轮探索。  
输入依据：`pi_round3_synthesis.md`、`reviewer_round3.md`、`卡点登记册.md`。  
硬边界：

- 不能说 `I_phi` 已验证。
- 不能说 DW disappearance suffices。
- 不能把 interlayer coherence、dz2-pz-dz2 hybridization、Pr4Ni3O10 dz2 incoherence 当作 LP28 首创。
- 不能把 zero resistance 单独写成 bulk superconductivity 证据。

## 1. 启动时已被杀死的声张

### K1. “LP28 发现 interlayer coherence 是镍酸盐超导的核心组织参数”

状态：杀死。

原因：REVIEWER 查重已经指出，先发工作已覆盖 RP nickelates 中 interlayer electronic coherence 作为组织参数的叙事。LP28 不能以此作为原创发现。

可保留版本：LP28 只使用 interlayer coherence 作为背景变量，并把贡献限缩为 trilayer static-DW layer decoupling 的 same-sample recovery-ordering protocol。

### K2. “dz2-pz-dz2 hybridization / dz2 channel 是 LP28 的新机制”

状态：杀死。

原因：trilayer fermiology、dz2 相关 band、Pr4Ni3O10 dz2 incoherence、hybridization frustration 已有先发覆盖。LP28 不能把 dz2/hybridization 本身包装成新机制。

可保留版本：LP28 关注的是 static DW 如何把已有 dz2/apical-O/dz2 跨层通道转化为 layer-decoupled state，以及压力路径是否能恢复该通道的相位连通性。

### K3. “pressure suppresses DW, therefore bulk SC emerges”

状态：杀死。

原因：DW 消失不是充分条件。tetragonal La4Ni3O10 在 ambient pressure 下没有 DW transition 也没有 superconductivity，直接破坏“无 DW 自动得到 SC”的单因果链。

可保留版本：pressure 只有在导致可测 `I_phi` recovery 并同时出现 independent bulk output 时，才可被解释为 phase-bus recovery route；DW collapse 只是候选路径事件，不是充分原因。

### K4. “`I_phi` 是已经成立的 predictor”

状态：杀死。

原因：`I_phi = E_z2*C_phi/(kBT+hbar Gamma_phi+E_floor)` 目前没有同一样品 pressure-axis 的先验输入测量、阈值标定、误差传播和独立 bulk output 验证。若写成已成立 predictor，REVIEWER 判定 fatal。

可保留版本：`I_phi` 是待验证、预注册、非循环的 input-side ordering index / protocol variable。它只能提出 go/no-go 实验判据，不能在现阶段承担已验证预测器的地位。

### K5. “zero resistance 证明 bulk superconductivity”

状态：杀死。

原因：Round 3 已明确 zero resistance 只能作为辅助证据。bulk output 必须来自 shielding/Meissner/vortex/THz/Josephson phase-stiffness evidence。

可保留版本：zero resistance 可作为 transport consistency check，但不得单独作为 bulk gate。

## 2. 已被收窄但仍可使用的声张

### N1. 从“机制解释”收窄为“可杀死实验协议”

原强声张：LP28 给出了 nickelate superconductivity 的机制解释。

收窄后：LP28 给出一个可被同一样品 pressure-axis 实验杀死的 phase-bus recovery protocol。成功判据是 input-side `I_phi` recovery 先于或同步于 independent bulk output；失败判据是 bulk output 与 `I_phi` 脱钩，或 `I_phi` recovery 后没有 bulk output。

### N2. 从“DW 是竞争序还是前体”收窄为“static partition vs dynamic fluctuation”

原强声张：DW collapse 解释 SC emergence。

收窄后：LP28 不问 DW 是否简单竞争或简单前体，而是区分两类 DW 作用：

- static DW partition：把 trilayer 中 dz2/apical-O/dz2 跨层相位通道切成 layer-decoupled state，压低 bulk phase stiffness。
- dynamic fluctuation background：可能仍参与 pairing 或增强 pairing susceptibility。

理论风险由“是否有 DW”转为“能否解除 static partition，同时不把有利 dynamic fluctuation 一并消灭”。

### N3. 从“pressure 是设计目标”收窄为“pressure 是诊断轴”

原强声张：pressure 优化超导。

收窄后：pressure 只是最小实验中的 tuning axis，用来同时扫描 `E_z2`、`C_phi`、`Gamma_phi`、bulk output 和 Hall/Drude/domain/oxygen controls。真正的设计变量不是 pressure 本身，而是 phase connectivity recovery。

### N4. 从“相干性越强越好”收窄为“相位通道恢复必须与 bulk phase stiffness 解耦验证”

原强声张：interlayer coherence 控制 superconductivity。

收窄后：相干性必须被拆成 input-side 谱权重/结构/退相干变量与 output-side bulk phase stiffness 两套独立测量。只有二者在同一样品同一 tuning axis 上按预注册顺序协变，LP28 才获得机制地位。

## 3. 更大但仍文献可防守的理论突破声张草案

### 主声张草案

在 trilayer RP nickelates 中，高温超导的可调控瓶颈不应被写成“是否存在 DW”或“pressure 是否压掉 DW”，而应被写成一个更一般的相位连通性问题：static density-wave order 可以把本来承担跨层相位传输的 dz2/apical-O/dz2 通道分割成 layer-decoupled electronic sectors；superconducting bulk response 只有在该 static partition 被解除、且跨层 phase bus 的输入侧谱权重、结构连通性和退相干成本同时进入可工作窗口时，才可能出现。

这个声张的突破点不是首次提出 interlayer coherence，也不是首次识别 dz2 hybridization，而是把镍酸盐中的 DW-SC 关系从“竞争序/前体”的二分叙事升级为“静态分割与动态涨落的可实验拆分”。在这个框架下，DW disappearance 本身不构成成功；成功要求特定 pressure 或材料调控路径产生 input-side phase-bus recovery，并由 shielding/Meissner/vortex/THz/Josephson 等 independent bulk output 验证。

### 可投稿表达

We propose that the relevant control variable in trilayer nickelates is not the mere suppression of density-wave order, but the recovery of a cross-layer phase bus that had been statically partitioned by density-wave-induced dz2 layer decoupling. This reframes the density-wave/superconductivity relation as a separable problem: static density-wave partition can suppress bulk phase stiffness, while residual dynamic fluctuations may remain compatible with pairing. The proposed `I_phi` index is therefore not a validated predictor at present, but a pre-registered input-side ordering variable for testing whether phase-bus recovery, rather than density-wave disappearance alone, precedes independent bulk superconducting signatures.

### 中文主文表达

我们提出，trilayer nickelates 中需要被调控的不是 DW 是否简单消失，而是被 static DW 分割的跨层 phase bus 是否恢复。DW 的静态成分可以通过 dz2/apical-O/dz2 通道的 layer decoupling 压低 bulk phase stiffness；但 DW 相关的动态涨落未必必须被消灭，反而可能仍是 pairing environment 的一部分。因此，镍酸盐超导优化的理论目标应从“压掉竞争序”改写为“双条件工程”：解除 static layer partition，并保留或不破坏有利的 dynamic fluctuation background。

### 防守边界

该声张只要求现有文献支持三个背景事实：

- trilayer nickelates 存在 dz2/interlayer/hybridization 相关电子结构与 DW baseline。
- pressure-SC 与 DW/interlayer coherence 变量存在邻近性或相关动机。
- 现有文献尚未排除 same-sample phase-bus recovery protocol。

该声张不要求现有文献已经证明：

- `I_phi` 是 predictor。
- DW collapse 足以产生 bulk SC。
- LP28 首创 interlayer coherence 或 dz2 hybridization。
- transport zero resistance 等价于 bulk superconductivity。

## 4. 最小可杀死形式

最小实验仍应写成同一样品 pressure-tuned La4Ni3O10：

1. 预注册 `E_z2`、`C_phi`、`Gamma_phi`、`E_floor` 的单位、归一化和误差传播。
2. 沿同一 pressure axis 先测 input-side `I_phi`，不得由 superconducting output 反拟合。
3. 独立盲测 shielding/Meissner/vortex/THz/Josephson bulk output。
4. 同步控制 Hall number、ab Drude、domain/structure、oxygen/disorder。
5. 预声明失败判据：bulk output 出现但 `I_phi` 不动；或 `I_phi` 明显提升但 independent bulk output 不出现。

## 5. 收尾判定

LP28 的 re-escalation 不应回到“发现新机制”的强包装，而应升级为一个更大但可防守的理论框架：nickelate superconductivity 的工程瓶颈是 static layer partition 与 dynamic pairing fluctuation 的分离控制。`I_phi` 在此框架中只是待验证的 input-side phase-bus recovery index；它的价值在于让该理论框架可被同一样品实验杀死，而不是在当前阶段证明该框架已经成立。
