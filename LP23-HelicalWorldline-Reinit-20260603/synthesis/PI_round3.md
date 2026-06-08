# PI 综合 round3

## 输入

- A博士：`current/A/round3.md`
- B博士：`current/B/round3.md`
- INSPECTOR(A)：`synthesis/inspector_A_round3.md`，通过，无阻断；警告：`ln A` 需显式无量纲化，`k_a=f nabla_a u` 中 `f` 的 SI 标注应修正为无量纲。
- INSPECTOR(B)：`synthesis/inspector_B_round3.md`，通过，无阻断；仅轻微记号警告。

## 汇合判断

A/B 独立汇合：LP23 中“螺旋/扭转”若指 spacetime 固定半径螺旋或光锥上的旋转坐标，仍是坐标效应，不是物理 twist。

- A 路线：null congruence 的 optical tensor 为 `B_ab=q_a^c q_b^d nabla_d k_c`，分解为 expansion/shear/twist。标准光锥 congruence 因 `k_a proportional nabla_a u` hypersurface-orthogonal，twist 为零。单条平直 null generator 没有内禀 optical twist；非零 twist 必须属于非 hypersurface-orthogonal null congruence 或额外联络/holonomy 结构。
- B 路线：`U(1)` 相位联络曲率可给干涉 holonomy，但不能自然映射为 congruence optical twist。恒定 null congruence 可同时有非零相位 holonomy 和零 optical twist；Hopf/Berry 曲率非零也不推出 spacetime screen distribution twist 非零。

## 核心结论

LP23-S1 原始版本三轮后形成稳定判定：

1. **证伪：** 固定半径单位螺旋包络不是光锥。
2. **证伪：** `theta=alpha` 的量子相位值与 null 方向角强同一化不 Lorentz 协变。
3. **证伪/降级：** `U(1)` 相位曲率不自动生成光锥或 null congruence 的 optical twist。
4. **可存活弱版：** 相位可作为 fiber/connection/holonomy；null direction 由 projective spinor/null vector/tetrad 给出；“扭转”若物理化，必须是 congruence optical twist 或特定 screen/spin connection 的 holonomy，而这需要额外结构。

## 新 K 条目

K9（否定）：标准光锥母线族 twist 为零；旋转角坐标不改变 hypersurface-orthogonal 性。

K10（边界）：单条 null generator 没有内禀 optical twist。twist 是 congruence 的横向导数数据，依赖邻近 ray 族。

K11（否定）：非零 `U(1)` holonomy 不蕴含非零 optical twist。相位 holonomy 与 spacetime screen twist 分属不同 bundle/base 对象，除非额外指定识别。

K12（最小降级命题）：LP23 的可保留版本应表述为：相位 holonomy 可影响干涉或偏振/screen-frame运输，但不生成光锥本身；任何“几何统一”必须给出 spin/screen connection 到 null congruence optical data 的量纲正确、协变的耦合。

## 停止条件检查

- 当前轮次：第3轮。
- 硬停止：未触发形式上的“无路可走”，但原始强声张已被三轮共同削弱。
- N>=3：满足最低轮次，可进入北极星收尾。

## 收尾前待办

1. GATE 1.5：grep A/B 推导中“深挖1”“深挖2”各至少2层。
2. Re-escalation：原声张明显收窄，需列出被杀死声张，并要求 A/B 产出更大声张草案，或将弱版注册为降级候选。
3. 矛盾深挖：从“相位=因果几何”深挖到“fiber holonomy 与 base null geometry 是否可由自然联络耦合”。
