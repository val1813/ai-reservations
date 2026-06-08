# INSPECTOR 校对报告：LP28 B博士 Round 2

输入：`current/B/round2.json`  
范围：只校对 LP28 B博士 Round 2；不做 REVIEWER 先发文献覆盖判断；不读取 A Round 2 输出。

## 机械检查

- `validation/` 目录不存在，`validate.py` / `quantum.py` 不可用。本报告按 INSPECTOR 协议降级为手工检查 Q1-Q6.5。
- JSON 格式检查通过：`Get-Content -Raw -Encoding UTF8 | ConvertFrom-Json` 通过；`python -m json.tool` 通过。
- 顶层识别：`project=LP28-NickelateLayerDecoupling`，`round=2`，`agent=B`，`claims=3`，`technology_routes=4`。

## Q1 量纲检查

### F1: `Q_phi = W_z2(0,Omega_c) * C_phi / (k_B*T + hbar*Gamma_phi)`

- 左边：`Q_phi`，声明为无量纲。
- 右边分母：`k_B*T` 为能量；`Gamma_phi` 声明为角频率 `s^-1`，`hbar*Gamma_phi` 为能量。分母量纲为能量。
- 右边分子：`C_phi` 无量纲；`W_z2(0,Omega_c)` 声明为 energy-integrated c-axis dz2/pz spectral-weight proxy normalized to eV。
- 判定：在且仅在 `W_z2` 的归一化结果保留能量单位 eV 时，右边为能量/能量，`Q_phi` 无量纲，量纲通过。
- 警告：`W_z2 normalized to eV` 表述仍需实验操作定义。若实际实验输出采用归一化光谱权重比值、sum-rule 比值或 arbitrary units，则 `W_z2` 会变为无量纲，当前公式将变成 `1/energy`。下一轮必须写明 `W_z2` 是能量尺度、等效积分能量，还是无量纲权重；若为无量纲，应改为 `Q_phi = E_z2*C_phi/(k_B*T+hbar*Gamma_phi)` 或引入能量标尺 `E0 W_z2`。

### F2: `epsilon_c = -(c-c0)/c0`

- 左边：应变，无量纲。
- 右边：长度差/长度，无量纲。
- 判定：量纲通过。

### F3: `Lambda_input != f(rho_c/rho_ab)`

- 这是非循环约束，不是物理等式；量纲不适用。
- `rho_c/rho_ab` 为无量纲比值，可作为下游症状或辅助观察量。

## Q2 符号/方向检查

- `epsilon_c = -(c-c0)/c0` 明确定义了 c-axis compression 为正、expansion 为负。上一轮 `epsilon_c` 符号警告已修正。
- 若 `epsilon_c > 0` 对应 `c<c0`，且压缩增强 dz2-pz-dz2 overlap，则 `dQ_phi/d epsilon_c > 0` 的方向与“压缩改善 phase bus”一致。
- B 已明确要求把压力引起的 bandwidth、carrier density、disorder 与 `epsilon_c`/dz2 通道分开；方向判断不再把 hydrostatic pressure 简化为单轴压缩。
- 判定：符号方向通过。

## Q3 非循环验证检查

- Round 2 明确把输入侧与验证侧分离：
  - 输入侧：c-axis optical Drude weight、polarization-resolved O K/Ni L-edge dz2-pz spectral weight、ARPES kz dispersion、RIXS/ultrafast dephasing、DFT/DMFT orbital-resolved hopping。
  - 验证侧：bulk diamagnetic shielding、c-axis Josephson plasma/THz response、pressure optical spectral-weight recovery、phase stiffness。
  - `rho_c/rho_ab` 被降级为 secondary transport consequence，不再允许同时定义和证明 `Lambda/Q_phi`。
- 判定：上一轮循环论证警告已实质修正。
- 警告：`pressure optical spectral-weight recovery` 同时出现在输入代理和验证侧时有潜在混用风险。建议下一轮固定一个协议：用于构造 `Q_phi` 的 `W_z2` 是高温/正常态或 onset 前的输入代理；用于验证的是独立的 shielding fraction、THz phase stiffness 或 Josephson plasma onset。不要用同一条 `Delta W_c(P,T)` 曲线既拟合 `Q_phi` 又宣称验证 `Q_phi`。

## Q4 数量级检查

- 本轮没有给出新的具体数值代入，因此不能做数值数量级验算。
- `Q_c` 被声明为 material- and disorder-dependent，且必须由 Meissner/shielding fraction 校准；这是合理的半经验阈值处理。
- 警告：四条 engineering route 的成功/失败判据多为“更强”“先于或同步”“更好预测”等关系判据，尚未给出最小可判别效应量、误差条或门槛值。作为 Round 2 设计变量可以继续，但下一轮若要收官，需要至少给出半定量阈值，例如 shielding fraction 下限、THz stiffness 可检出下限、`Delta W_c` 相对变化下限、Hall number 匹配容差、domain fraction 排除标准。

## Q5 代数与极限退化

- F1 代数结构为简单乘除，无非平凡展开错误。
- 极限检查：
  - `W_z2 -> 0` 或 `C_phi -> 0` 时，`Q_phi -> 0`，对应 phase bus 断开，方向正确。
  - `Gamma_phi -> infinity` 时，`Q_phi -> 0`，对应强退相干抑制全局相位一致，方向正确。
  - `T -> 0` 且 `Gamma_phi -> 0` 时，分母趋零，`Q_phi` 发散。该极限提示公式是有限温度/有限退相干下的工程评分，而不是基态微观定理。需要在下一轮明确适用域：`k_B*T + hbar*Gamma_phi` 不得低于实验能量分辨率、残余 disorder/dephasing 或阈值正则项。
- `C_phi` 未给出严格构造。当前可作为 dimensionless phase-connectivity factor，但若后续要量化，必须说明其取值范围，例如 `0<=C_phi<=1`，以及是否已包含 domain fraction / layer coherence / structural correlation length。

## Q6.3 声张缩水检查

- 与 B Round 1 相比，Round 2 明显收窄了首创性：从“interlayer coherence/partition 解释 DW 与 bulk SC”收缩到“把 dz2-mediated interlayer coherence 改写为可工程化的 phase quorum variable `Q_phi`，并要求非循环实验证据链”。
- 这是对 PI Round 1 先发边界的必要收敛，不是无理由缩水。Round 2 仍保留了可检验核心：La4Ni3O10 trilayer 中 dz2/c-axis spectral recovery、bulk shielding/phase stiffness 与 static DW weakening 的因果顺序。
- 判定：无阻断；建议 PI 在北极星矩阵中按“收窄后命题”重算新颖性和可落地分，而不是沿用 Round 1 的宽口径 interlayer coherence 声张。

## Q6.4 替代解释检查

- B 已显式列出并给出区分测试：
  1. pressure bandwidth effect；
  2. scattering anisotropy and structural domains；
  3. common third variable，包括 oxygen stoichiometry、carrier density、disorder、structural phase fraction。
- 判定：上一轮“替代解释不足”警告已明显修正。
- 仍需补强：替代解释的排除标准目前是实验设计级，不是成败判据级。下一轮应把每个替代解释转为最小排除条件，例如“same Hall number within X%”“domain fraction below Y or measured as covariate”“ab-plane Drude weight cannot alone fit shielding trend within error”“oxygen stoichiometry uncertainty below Z”。

## Q6.5 落地计算/工程路线检查

- 本轮存在具体落地路线 R1-R4，且每条包含 control knob、observables、success criterion、failure criterion。不是“发现空白但完全无落地”，不触发强制阻断。
- R1 成败判据较清楚：要求 c-axis spectral weight/THz stiffness 先于或伴随 shielding，而 ab-plane Drude weight alone 不预测 transition；失败为只跟踪 ab-plane bandwidth 或 structural transition。
- R2 明确了 `epsilon_c` 符号，并要求 domain-controlled samples collapse onto `Q_phi` rather than `rho_c/rho_ab`；这是对上一轮应变符号和循环验证问题的有效修正。
- R3 对 chemical pressure 与 oxygen stoichiometry split tuning 的思路正确，能处理 common third variable。
- R4 对 non-equilibrium pump 路线有时间顺序判据，但仍缺少热效应排除的定量门槛。
- 警告：工程路线已从概念落地到半成品，但未达到可直接执行的实验判据表。缺项包括压力/应变范围、温度窗口、shielding fraction 门槛、THz/optical 可检出阈值、domain/crack/contact geometry 排除标准、pump heating control。

## 综合判定

INSPECTOR 通过，可继续。Round 2 已修正 Round 1 的主要警告：`Q_phi` 量纲约定基本成立，`epsilon_c` 符号明确，`rho_c/rho_ab` 循环验证被解除，替代解释被显式纳入，工程路线具备成败判据。

INSPECTOR 警告：`W_z2` 的单位/归一化仍是最脆弱点；`Q_phi` 公式在 `T,Gamma_phi -> 0` 极限需要适用域或正则项；工程路线判据仍偏半定量，下一轮应转化为可执行阈值表。

--- 投喂下一轮 ---

必须修正（阻断级）：

无。

建议修正（警告级）：

1. 固定 `W_z2` 的单位协议：若它是能量积分后的 eV 尺度，保留当前公式；若实验代理是无量纲光谱权重比值，改写为 `E_z2` 或 `E0 W_z2` 进入 `Q_phi`。
2. 明确 `Q_phi` 适用域或正则项，避免 `T -> 0` 且 `Gamma_phi -> 0` 时无物理发散。
3. 固定非循环验证协议：构造 `Q_phi` 的谱权重输入与验证 `Q_phi` 的 shielding/THz/Josephson 输出不得用同一数据重复证明。
4. 把 R1-R4 的成功/失败判据推进为阈值表：pressure/strain/temperature 窗口、`Delta W_c` 下限、THz stiffness 检出阈值、shielding fraction 门槛、Hall number 匹配容差、domain fraction 与 pump heating 排除标准。
5. 将三个替代解释的排除从“设计思路”升级为“最小排除条件”：bandwidth-only、scattering/domain-only、common-third-variable-only 各自需要明确观测反例。

---
