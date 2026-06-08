# INSPECTOR 校对报告：LP28 B博士 Round 1

输入：`current/B/round1.json`  
输出：`current/synthesis/inspector_B_round1.md`  
范围：只校对 LP28 B博士 Round 1；不做 REVIEWER 先发文献覆盖判断。

## 机械检查

- `validation/` 目录不存在，`validate.py` / `quantum.py` 不可用。本报告按 INSPECTOR 协议降级为手工检查 Q1-Q6.5。
- 阻断：`round1.json` 不是合法 JSON。`ConvertFrom-Json` 报错：`':' or '}' expected`。直接可见的格式问题包括第 6 行 `framework` 字符串未闭合；第 7-10、12、15、18-19 行也呈现类似未闭合字符串/结尾引号损坏。后续自动验证、schema 校验和 PI 机器读取都会失败。

## Q1 量纲检查

### F1: `Lambda = hbar*t_perp_eff/(k_B*T + hbar*Gamma_DW)`

- 左边：`Lambda`，无量纲。
- 右边：若 `t_perp_eff` 按文件声明为 hopping rate，单位 `s^-1`，则 `hbar*t_perp_eff` 为能量 `J`；`k_B*T` 为 `J`；`hbar*Gamma_DW` 为 `J`；比值无量纲。
- 结论：量纲通过。
- 注意：凝聚态文献中 `t_perp` 常被当作 hopping energy 而非 rate。当前写法只有在明确采用 `t_perp_eff` 为角频率/速率时成立。下一轮必须保留这个约定，或改写为 `t_perp_eff/(k_B*T + hbar*Gamma_DW)` 并把 `t_perp_eff` 标为能量。

### F2: `W_c_DW/W_c_normal`

- 左边：归一化谱权重，无量纲。
- 右边：同一能量 cutoff 下的谱权重比，无量纲。
- 结论：量纲通过。

### F3: `Theta_pair*(Lambda - Lambda_c)`

- `Theta_pair`、`Lambda`、`Lambda_c` 均声明为无量纲；乘积无量纲。
- 结论：量纲通过。
- 注意：该式只能作为符号判据，不能直接当作超导体积分数、Tc 或刚度的量化公式。

## Q2 方向检查

- F1 极限：`t_perp_eff -> 0` 给 `Lambda -> 0`；`Gamma_DW -> infinity` 给 `Lambda -> 0`。这支持“静态 DW 降低层间 coherence 并抑制 bulk superconductivity”的方向。
- F2 极限：`W_c_DW -> 0` 给归一化谱权重 0。若以 c-axis 谱权重作为层间 coherence 代理，方向一致。
- F3 极限：`Lambda -> Lambda_c` 给 0；`Lambda < Lambda_c` 时符号为负，`Lambda > Lambda_c` 时符号为正。作为“local pairing 不足以推出 bulk SC”的符号门槛，方向一致。
- 警告：P4 写 `d(rho_c/rho_ab)/d epsilon_c < 0` 但没有定义 `epsilon_c` 的正负号。如果材料力学惯例取压缩应变为负，则“c-axis compression 降低各向异性”对应导数符号可能相反。必须在下一轮定义 `epsilon_c > 0` 是否表示压缩；否则 P4 的方向判据不可执行。

## Q3 循环论证检查

- 主要验证链条是：DW 改变 dz2/层间通道 -> 降低 `Lambda` -> `rho_c/rho_ab` 增大、`W_c` 降低 -> bulk SC 受抑制。
- 风险：如果 `t_perp_eff` 或 `Gamma_DW` 没有独立测量，而是由 `rho_c/rho_ab` 或 `W_c` 反推，则用这些代理量再验证“Lambda 低”会变成重复输入假设。
- 判定：警告，不阻断。B 已提出可观测量 `rho_c/rho_ab`、低频 `sigma_c`、Meissner fraction 的交叉检验，具备跳出循环的路线；但下一轮必须明确哪些量是输入、哪些量是外部验证。

## Q4 量级鸿沟检查

- F1 数值代入：`hbar*t = 1.054e-21 J`；`kBT = 6.905e-22 J`；`hbar*Gamma = 1.054e-21 J`；`Lambda = 1.054e-21 / 1.7445e-21 = 0.604`，落在 `[0.1, 10]`。
- F2 数值代入：`0.2/1.0 = 0.2`，落在 `[0, 1]`。
- F3 数值代入：`1.0*(0.8-1.0) = -0.2`，落在 `[-1, 0]`。
- `rho_c/rho_ab` 从约 70 到约 2600，约 37 倍，约 1.6 个数量级；“从 10^2 toward 10^3”可接受。
- 警告：bulk 判据写成 `10^2-10^3` 是一整个数量级宽区间，只能作为半定量阈值，不能作为硬预测。若要落地为实验判据，需要给出材料、温度、压力窗口和误差条。

## Q5 代数与极限退化

- F1 无非平凡代数错误；两个极限均退化正确。
- F2 是直接比值，无代数错误。需补充 `W_c_normal != 0` 和相同 cutoff/同一归一化规范。
- F3 代数正确；但 `Theta_pair` 若可能为负或未定义正定，则符号判据失效。下一轮应声明 `Theta_pair >= 0`，且它只表示局域 pairing tendency 的正强度。
- 引用数值来源级别：文件给出 DOI 与标签，但本轮未做 REVIEWER 文献核验。`PRL 136, 216501 (2026)` 的 `70 -> 2600`、`Nat Commun 2025` 的 DW collapse/SC emergence 只能标为“有引用标签，未核文献全文”。INSPECTOR 不在此处判定引用属实。

## Q6.3 声张缩水

- Round 1 无 B 博士上一轮可比较，声张缩水不适用。
- 当前声张强度：从“静态 DW 是 bulk superconductivity suppressor”到“fluctuating DW 仍可能是 precursor”的分层表述内部一致，不构成本轮缩水。

## Q6.4 替代解释

- B 已回答一个替代解释：DW fluctuations as pairing glue，并用 “local pairing vs global phase quorum” 区分。
- 警告：替代解释仍不充分。至少还需显式排除或区分：
  1. 压力直接改变带宽、载流子浓度、晶格畸变或 disorder，而非通过 dz2/quorum 通道导致 SC。
  2. `rho_c/rho_ab` 增大来自散射各向异性或结构畴，而非相位 coherence 断裂。
  3. DW collapse 与 SC emergence 只是共同受第三变量控制，而非 DW 静态态本身为抑制器。
- 判定：警告，可进入下一轮，但 PI/B 下一轮必须把这些替代解释纳入可区分预测。

## Q6.5 落地计算检查

- 本轮存在落地尝试：P1-P4 给出具体系统、观测量和方向预测；P1 有 `rho_c/rho_ab ~ 10^2 -> 10^3`、`>10^3`、`10^2-10^3` 等半定量阈值；P3 给出 `omega < 40 meV` cutoff。
- 不阻断：不是“发现空白但完全无落地”。
- 警告：落地仍偏弱。P2 未给出压力点、压力范围或 shielding fraction 阈值；P3 未给出时间尺度和 `Delta sigma_c/Delta sigma_ab` 的数值下限；P4 未定义应变符号和应变量级。

## 综合判定

INSPECTOR 阻断：当前 `round1.json` 格式非法，不能作为标准 A/B 产出进入自动验证或后续机器消费。修正 JSON 后，核心物理公式的量纲、基本极限和数值代入没有发现致命错误。

INSPECTOR 警告：P4 应变方向符号含混；`Lambda` 代理量验证存在循环论证风险；替代解释排除不足；落地阈值多为半定量。

--- 投喂下一轮 ---

必须修正（阻断级）：

1. 修复 `current/B/round1.json` 的 JSON 语法。至少第 6 行 `framework` 字符串未闭合；第 7-10、12、15、18-19 行也疑似存在结尾引号损坏。修复后必须能被 `ConvertFrom-Json` 或等价 JSON parser 解析。

建议修正（警告级）：

1. 明确 `t_perp_eff` 的单位约定：若为速率保留 `hbar*t_perp_eff`；若为能量则去掉 `hbar`。
2. 定义 `epsilon_c` 的符号；若 `epsilon_c > 0` 表示压缩，则保留 `d(rho_c/rho_ab)/d epsilon_c < 0`，否则需要改号。
3. 明确验证链条中哪些是输入代理、哪些是独立外部验证，避免用 `rho_c/rho_ab` 反推 `Lambda` 后再用它证明 `Lambda`。
4. 加入可区分替代解释的预测：压力直接带宽效应、散射各向异性/结构畴、共同第三变量。
5. 把 P2-P4 推进为可执行数值判据：压力范围、时间尺度、`Delta sigma_c/Delta sigma_ab` 下限、Meissner/shielding fraction 阈值、应变量级。

---
