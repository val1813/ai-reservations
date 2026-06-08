# INSPECTOR 校对报告：LP28 B博士 Round 3

输入：`current/B/round3.json`  
范围：只校对 LP28 B博士 Round 3；不做 REVIEWER 先发文献覆盖判断；不读取 A Round 3 输出。  
重点：`I_phi/max` 公式量纲与极限、T1/T2 阈值是否可执行、三类替代解释最小排除条件是否充分、单实验建议是否非循环。

## 机械检查

- `validation/` 目录不存在，`validate.py` / `quantum.py` 不可用。本报告按 INSPECTOR 协议降级为手工检查 Q1-Q6.5。
- JSON 格式检查通过：`Get-Content -Raw -Encoding UTF8 | ConvertFrom-Json` 通过；`python -m json.tool` 通过。
- 顶层识别：`project=LP28-NickelateLayerDecoupling`，`round=3`，`agent=B`，`claims=3`。

## Q1 量纲校对

### F1: `I_phi = E_z2 * C_phi / max(k_B*T + hbar*Gamma_phi, E_floor)`

- 左边：`I_phi` 声明为无量纲设计分数。
- 右边分子：`E_z2` 为能量尺度；`C_phi` 为 0 到 1 的无量纲 connectivity factor。因此分子量纲为能量。
- 右边分母第一项：`k_B*T` 为能量；`Gamma_phi` 声明为角频率退相干率 `s^-1`，`hbar*Gamma_phi` 为能量。因此 `k_B*T + hbar*Gamma_phi` 为能量。
- 右边分母第二项：`E_floor` 声明为能量下限。因此 `max(energy, energy)` 合法。
- 判定：量纲通过。Round 2 中 `W_z2` 可能无量纲导致 `1/energy` 的警告已经通过 `E_z2` / `E0*W_z2` 协议修正。

警告：`Gamma_phi` 必须保持为角频率而非普通频率。若实验 linewidth 以 Hz 或 cm^-1 报告，需在输入协议里完成 `2*pi` 或能量单位换算，否则 `hbar*Gamma_phi` 会差一个常数因子。该问题不阻断当前概念校对，但会影响落地数值表。

## Q2 符号/方向与极限校对

对 F1 做极限代入：

- `E_z2 -> 0` 或 `C_phi -> 0` 时，`I_phi -> 0`。对应 dz2/pz 层间通道消失或连通性消失，方向正确。
- `E_z2` 增大且其他量固定时，`I_phi` 单调增大。对应 phase-bus capacity 增强，方向正确。
- `C_phi` 增大且其他量固定时，`I_phi` 单调增大。对应 domain/registry/coherence 改善，方向正确。
- `T` 增大或 `Gamma_phi` 增大且分母未被 `E_floor` 钳制时，`I_phi` 单调降低。对应热涨落与退相干抑制全局相位一致性，方向正确。
- `T -> 0` 且 `Gamma_phi -> 0` 时，分母退化到 `E_floor`，`I_phi = E_z2*C_phi/E_floor`，不再发散。Round 2 的低温/低退相干发散警告已经修正。
- 若 `k_B*T + hbar*Gamma_phi < E_floor`，分数被仪器分辨率、残余 disorder floor 或拟合退相干 floor 钳制。该极限说明 `I_phi` 是工程反馈分数，不是微观基态定理。B 已明确这一点。

判定：公式方向和极限通过，无阻断。

## Q3 非循环论证检查

B Round 3 明确了输入与输出分离：

- 输入侧：normal-state 或 onset-preceding 的 `E_z2`，结构/domain/registry 构造 `C_phi`，RIXS/ultrafast/linewidth 构造 `Gamma_phi`，以及 `E_floor` 约定。
- 禁止输入：shielding、Meissner、作为输出的 THz phase stiffness、作为输出的 Josephson plasma edge、zero resistance、以及若后续作为验证则不能使用的 `rho_c/rho_ab`。
- 输出侧：bulk shielding、Meissner/vortex、独立 THz phase stiffness 或 Josephson onset、vertical Josephson-like tunneling；zero resistance 只能作次级支持。
- 工作流要求先测输入、算 `I_phi`、再测输出，并要求同一条曲线不能同时构造输入又证明输出。

判定：非循环协议通过。特别是单实验建议中，`E_z2/C_phi/Gamma_phi` 在正常态或 onset 前测量，输出用 shielding 加独立 THz/Josephson，相比 Round 2 已显著收紧。

残余警告：如果实际执行时把同一 c-axis THz 谱区同时用于 `E_z2` 输入和 THz phase-stiffness 输出，仍会重新引入循环。Round 3 已写出“predeclared output window distinct from input spectral-weight extraction”，PI 后续实验表必须把谱窗、温区和拟合量分开列明。

## Q4 数量级鸿沟检查

- Round 3 未给出具体数值代入，因此不能校验 `I_phi`、`E_floor`、`hbar*Gamma_phi` 的绝对数量级是否现实。
- T1/T2 给出的阈值多为相对变化、统计显著性和匹配容差：`2x`、`>=3 sigma`、`>=15%`、`>=20%`、Hall `5%`、residual disorder `10%`、oxygen `<=0.01`、shielding `>=10%`、domain/phase fraction `>=80%/90%` 等。这些是可执行的半定量门槛，而非空泛方向判断。
- 未出现明显跨越几十数量级的断言。

判定：数量级层面无阻断。警告是 `E_floor` 的实际取值必须在实验计划中由分辨率、残余 disorder floor 或拟合 floor 预声明，否则 `I_phi` 的绝对比较会有可调参空间。

## Q5 代数与阈值可执行性

### T1: pressure / c-axis strain feedback loop

可执行项：

- 输入阈值：同一样品或紧密匹配系列中，`I_phi` 至少 `2x` 或 `>=3 sigma` 增加，且发生在 bulk-SC 输出之前或同时。
- 光谱阈值：`E_z2` 或声明代理恢复 `>=15%` 且 `>=3 sigma`，并要求 ab-plane Drude/bandwidth 变化小于一半归一化效应或作为 nuisance covariate。
- 连通性阈值：`C_phi >=0.70`；若更低，则逐点测量并经 domain correction 后仍保持 `I_phi` 预测性。
- bulk 成功阈值：shielding `>=10%` 且有 Meissner/vortex，或 zero resistance 同时有独立 THz/Josephson phase stiffness。
- sequence 阈值：输入侧 `I_phi` recovery 必须在实验温度/压力分辨率内先于或同步于 output onset。

判定：T1 已从“路线设想”进入可执行门槛表。没有阻断。

警告：T1 仍缺少具体压力范围、压力步进、温度步进、`3 sigma` 误差模型和 hysteresis 容差定义。当前足以作为 Round 3 策略阈值，但还不是可直接排班的 beamtime protocol。

### T2: orthogonal-material-axis selector

可执行项：

- matched series：至少两对样品或状态；Hall `5%` 内匹配，residual-resistivity/disorder proxy `10%` 内匹配，oxygen stoichiometry 不确定度 `<=0.01` 每化学式单位或声明 metrology floor。
- orthogonal leverage：匹配对中 high-`I_phi` 成员的 `E_z2/C_phi` corrected score 高 `>=20%` 或 `>=3 sigma`。
- output：high-`I_phi` 成员 shielding fraction `>=5x`，或从 `<1%` 到 `>=10%`，或出现低 `I_phi` 成员没有的独立 THz/Josephson onset。
- pump：要求 coherent phonon/electronic window 内出现，并早于 equilibrium-heating control；单独 pump-induced reflectivity 不足。
- retention：DW/local gap 可保留，但 static DW partition/domain signature 必须降低或绕开到 `C_phi` 改善 `>=3 sigma`。

判定：T2 可执行性通过。它已经具备样品匹配、正交杠杆、输出差异、泵浦热控和 DW/domain retention 的最低判据。

警告：T2 的“至少两对样品或状态”是最低门槛，统计功效弱；如果进入收官实验设计，PI 应标注这是 selector/falsifier 级别，不是最终普适相图证明。

## Q6.3 声张缩水检查

与 B Round 2 相比，Round 3 没有无理由缩水，而是把 Round 2 的警告项压缩成工程反馈协议：

- `Q_phi` 改为 `I_phi`，并用 `E_z2` 与 `E_floor` 修正量纲和低温发散。
- R1-R4 压缩为 T1/T2，不是删弱主张，而是把多路线收敛到一个主实验和一个正交 selector。
- 替代解释从“列出风险”升级为三类最小排除条件。
- 非循环验证从原则声明升级为 input/output forbidden list 和 workflow。

判定：无声张缩水阻断。建议 PI 在北极星矩阵中把当前主张标记为“工程反馈协议/可杀死技术杠杆”，不要再按“微观定理证明”打分。

## Q6.4 替代解释最小排除条件

### 1. bandwidth-only

最小条件包括同一路径测 ab bandwidth proxy、至少一个 bandwidth 匹配或协变量剔除而 `I_phi` 差异 `>=3 sigma` 的比较、输出跟随 `I_phi` 而非 bandwidth-only fit。并明确若 bandwidth 与 `I_phi` 全程锁定，则不能排除。

判定：充分，且保留了不可排除时的失败标签。

### 2. scattering/domain-only

最小条件包括禁止用 `rho_c/rho_ab` 作主输入、分离 Drude spectral weight 与 linewidth/scattering rate、domain/phase fraction 成像或量化、single-domain fraction `>=80%` 或纳入 `C_phi`、用 optical/THz/XAS/ARPES/RIXS 等 contact-independent probe 排除 cracks/contact geometry。并明确若 domain fraction 可解释输入与输出则不能排除。

判定：充分。该部分直接覆盖了 Round 2 的循环与 contact/domain 风险。

警告：若 THz 同时作为 contact-independent probe 和输出 phase stiffness，需要预声明不同谱窗或改用 XAS/ARPES/RIXS/optical sum-rule 作为输入侧 probe，避免 Q3 中的同曲线复用。

### 3. common-third-variable-only

最小条件包括 Hall/carrier proxy `5%` 匹配、oxygen stoichiometry `<=0.01` 或样品特定 metrology limit、residual disorder `10%` 匹配或协变量、structural phase fraction `>=90%` 或纳入 `C_phi`、pump off-resonant 与 fluence-matched heating controls、同一时间窗口 `>=3 sigma` 超过 heating control。并明确若没有 same carrier/disorder but different `I_phi` 的 crossed trajectory，则 common-third-variable-only 仍开放。

判定：充分，且比 Round 2 明确。

综合判定：三类替代解释最小排除条件通过，无阻断。

## Q6.5 落地计算/单实验建议检查

Round 3 存在明确落地：

- T1：pressure / c-axis strain phase-bus feedback loop，给出 actuator、input measurements、output measurements、go thresholds、failure conditions、feedback loop。
- T2：orthogonal-material-axis phase-bus selector，给出 matched pairs、orthogonal leverage、output difference、pump control、failure conditions。
- 单实验建议：pressure-tuned La4Ni3O10 high-quality single crystal；先测 input-side c-axis/orbital spectral tracking，再测 output-side bulk shielding plus independent THz/Josephson phase stiffness，并同步 ab Drude/Hall/domain controls。

单实验非循环判定：

- 非循环点 1：`I_phi` 的输入不允许使用 shielding/Meissner/zero resistance/输出 THz phase stiffness。
- 非循环点 2：minimal version 明确“first measure normal-state E_z2/C_phi/Gamma_phi proxies; then measure shielding and a separate phase-stiffness/Josephson output”。
- 非循环点 3：decisive success 要求 controls 不能单独解释 transition；decisive failure 也包括 `I_phi` 改善但无 bulk output。

判定：单实验建议非循环，通过。

警告：La4Ni3O10 同一高质量单晶的 pressure-tuned 光谱、shielding、THz/Josephson 联合测量技术难度高。若实际平台不能同一样品完成，必须转为“tightly matched series”并继承 T1/T2 的匹配容差；否则同样品因果顺序会弱化。

## 综合判定

INSPECTOR 通过，可继续。Round 3 已实质修正 Round 2 对 `W_z2` 量纲、`T,Gamma_phi -> 0` 发散、循环验证、阈值表和替代解释不足的主要警告。

INSPECTOR 警告：当前阈值已经可执行到“实验设计/杀死假说”层级，但尚未细化为 beamtime 级别 protocol。后续 PI 若进入收官实验方案，应补齐压力/温度步进、误差模型、`E_floor` 预声明、THz 输入/输出谱窗分离、hysteresis 容差和 matched-series 替代方案。

--- 投喂下一轮 ---

必须修正（阻断级）：

无。

建议修正（警告级）：

1. 固定 `Gamma_phi` 单位换算：声明 linewidth 若以 Hz、cm^-1、meV 或角频率给出时如何进入 `hbar*Gamma_phi`。
2. 预声明 `E_floor` 的数值来源：仪器分辨率、残余 disorder floor、拟合退相干 floor 三者取最大值，避免后验调参。
3. 把 T1/T2 的半定量阈值推进到实验表：压力/温度步进、`3 sigma` 误差模型、hysteresis 容差、THz/optical 可检出下限。
4. 明确输入 THz/optical 谱窗与输出 THz phase-stiffness/Josephson 谱窗不能复用同一曲线；若无法分离，输出改用 shielding/Josephson tunneling，输入改用 XAS/ARPES/RIXS/normal-state optical sum-rule。
5. 若单实验无法同一样品完成 input-output 顺序，必须改写为 tightly matched series 并继承 Hall 5%、disorder 10%、oxygen <=0.01、domain/phase fraction 的匹配容差。
---
