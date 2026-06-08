# LP28 Re-escalation B 草案

角色：B博士  
任务类型：Round 3 收尾 Re-escalation，不是新一轮探索  
边界：不声称 `I_phi` 已验证；不声称 DW disappearance suffices；所有升级声张均为待验证的材料设计纲领。

## 1. 被杀死或被压窄的原声张

原声张 X：trilayer nickelates 中，static DW-induced dz2 layer decoupling 可以被压力恢复为 phase-bus recovery，并由非循环的 `I_phi` predictor 指导 bulk superconductivity 优化。

被 REVIEWER 证伪/压窄的环节：

1. `I_phi` 目前没有同一块样品、同一 pressure axis 上的先验输入测量和独立 bulk output 验证，因此不能写成已成立 predictor。
2. DW 消失或减弱不是 superconductivity 的充分条件；tetragonal La4Ni3O10 反驳了“无 DW -> 自动 SC”的单因果链。
3. interlayer coherence、dz2-pz-dz2 hybridization、Pr4Ni3O10 dz2 incoherence 等背景物理已有先发，LP28 不能把这些概念本身作为原创。
4. 当前 protocol 的新颖性只剩“同一样品、同一调控轴、输入侧先验锁定、输出侧独立验证”的工程化 ordering，而不是机制已经被证明。

## 2. 更大的声张草案

更大声张：

> 高温镍酸盐材料设计不应再以“消灭竞争序”或“最大化配对胶水”为主路线，而应转向“相位传输架构设计”：先判断材料中是否存在可恢复、可连通、抗退相干的 orbital phase bus，再决定是否值得投入压力、应变、化学取代或界面工程。  
> 在 trilayer RP nickelates 中，Ni dz2/apical-O/dz2 通道不是背景能带细节，而可能是把局域配对涨落升级为 bulk superconductivity 的架构性瓶颈。设计目标因此从“让 DW 消失”改为“切断 static DW 对 phase bus 的锁死，同时保留或另行提供局域 pairing fluctuation，并恢复跨层相位投票通道”。

这比当前 protocol 更大，因为它不只是给 La4Ni3O10/Pr4Ni3O10 一个 pressure experiment，而是改变材料筛选顺序：

旧路线：

1. 找高 pairing scale 或强 fluctuation。
2. 压低 DW/磁序/结构畸变。
3. 看 zero resistance 或 Tc 是否出现。
4. 事后解释 interlayer coherence。

升级路线：

1. 先筛 orbital phase bus 是否可被恢复：dz2/apical-O/dz2 spectral pathway、registry/domain connectivity、dephasing linewidth 是否同时朝有利方向移动。
2. 再检查 local pairing channel 是否仍存在：DW fluctuations、spin/charge/orbital fluctuations 只能作为 pairing reservoir，不自动等于 bulk SC。
3. 最后才看 bulk phase output：shielding、Meissner、vortex、THz/Josephson 或 phase stiffness 证据。
4. 若 pairing signal 强但 phase bus 不恢复，判为“二维/局域前驱态陷阱”，不继续把资源投入到单纯增强 pairing。

## 3. 最硬的重新表述

LP28 可以把主张改成：

> 镍酸盐超导的可设计变量可能不是单一序参量的强弱，而是“pairing reservoir”和“phase bus”之间的解耦与重接线。Static DW 可能破坏 dz2-mediated phase bus；dynamic DW fluctuation 仍可能提供局域 pairing reservoir。真正的材料设计问题不是 DW 是敌是友，而是如何把同一 DW 通道的 static decoupler 功能和 dynamic pairing-reservoir 功能分离。

这句话绕开了 Reviewer 的 fatal 点：

- 它没有说 DW 消失足够。
- 它没有说 `I_phi` 已经预测成功。
- 它承认 interlayer coherence/dz2 背景已有先发，但把原创点放在“设计路线的重排”：先 phase-bus architecture，后 pairing enhancement。

## 4. 可检验版本

更大声张必须落成一个可杀死的实验纲领：

**核心判据不是 `I_phi` 成功，而是 ordering 是否成功。**

同一块 pressure-tuned La4Ni3O10 或 Pr4Ni3O10 样品上，必须先验测量：

1. `E_z2`：dz2/apical-O/dz2 c-axis coherent spectral weight，需给能量标尺或明确归一化。
2. `C_phi`：domain/registry/kz/structural phase-connectivity factor。
3. `Gamma_phi`：dephasing linewidth，频率/能量单位协议预注册。
4. `E_floor`：只作为预注册 regularization，不作为事后调参。

然后独立测 bulk output：

1. shielding / Meissner fraction。
2. vortex evidence。
3. THz/Josephson/phase-stiffness response。
4. zero resistance 只能辅助，不能单独作为 bulk 证据。

成功只允许写成：

> phase-bus input recovery precedes or co-varies with independent bulk phase output under controlled Hall、ab Drude、domain、oxygen/disorder conditions.

失败判据：

1. bulk output 出现但 phase-bus inputs 不动。
2. phase-bus inputs 明显恢复但独立 bulk output 不出现。
3. DW 振幅减弱但 phase-bus connectivity 不恢复。
4. pairing/gap-like signal 增强但 c-axis phase bus 继续退相干。

## 5. 对材料设计路线的改变

若该升级命题为真，材料设计路线会从“寻找更强配对”改为“三层门控”：

第一门：pairing reservoir  
材料必须有可用的局域 pairing precursor，但这不是充分条件。

第二门：phase-bus restorability  
材料必须有一个可恢复的跨层相位通道，尤其是 dz2/apical-O/dz2 或等价 orbital bridge。没有这个门，强 pairing 只会停在局域或二维前驱态。

第三门：static/dynamic channel separation  
调控手段不应简单清空 DW，而应压制 static decoupling component，同时保留、绕开或替代 dynamic pairing component。

这个路线会直接改变实验优先级：

1. 少做“DW peak 是否消失”的单指标竞赛。
2. 多做同一样品的 c-axis spectral weight、linewidth、domain registry、phase stiffness 联测。
3. 用 pressure/strain/chemical substitution/interface 作为 phase-bus wiring tools，而不是只作为 Tc 搜索旋钮。
4. 对候选材料先问“能不能三维相位投票”，再问“有没有配对胶水”。

## 6. 最激进但合规的一句话

> LP28 的潜在突破不是证明了 La4Ni3O10 的某个 predictor，而是提出一个可证伪的镍酸盐设计反转：bulk superconductivity 的瓶颈可能常常不在 pairing glue，而在 orbital phase-bus architecture；因此高温镍酸盐应按“pairing reservoir + recoverable phase bus + independent bulk phase output”的三门控路线筛选，而不是按“压低 DW、等待 Tc”的单路线筛选。

## 7. 禁用表述

以下句式不能进入最终 manuscript 或 PI 收官文本：

1. “`I_phi` predicts superconductivity.”  
   改为：“`I_phi` is a preregistered candidate input-side ordering metric to be tested against independent bulk output.”

2. “DW disappearance enables superconductivity.”  
   改为：“DW disappearance alone is insufficient; the required test is phase-bus recovery plus independent bulk phase output.”

3. “We discover interlayer coherence as the organizing parameter.”  
   改为：“We operationalize interlayer/orbital coherence into a same-sample recovery-ordering protocol.”

4. “Pressure restores superconductivity by removing DW.”  
   改为：“Pressure is treated as a wiring perturbation whose success must be judged by input-side phase-bus recovery and independent bulk phase evidence.”

## 8. B博士结论

我建议 LP28 的 re-escalated claim 不再押注“一个公式能预测 Tc”，而押注“材料设计顺序错了”：

> 不是先找 superconductivity 再解释 coherence；而是先筛可恢复 phase bus，再允许 superconductivity claim 进入 bulk 验证。

这比当前 protocol 大，因为它能改变 nickelate、甚至更广义 layered unconventional superconductors 的筛选路线。它也比原声张更稳，因为它把 `I_phi` 降为待验证的输入侧候选指标，把 DW 降为 static/dynamic 功能分解问题，把最终裁决交给独立 bulk phase output。
