# INSPECTOR_B | LP23-R1 Round2

结论：`INSPECTOR阻断`

阻断项 1 条；警告项 2 条；其余检查通过。

## 阻断项

1. `omega_ab` 的定义式写法存在机械性错误，当前式子不宜作为后续论证基底。  
   位置：`current/B/R1_round2.md:23`  
   原文：`omega_ab = q_[a]^c q_b]^d nabla_c k_d`  
   问题：
   - 反对称化括号不配对，当前写法是坏公式；
   - `q_[a]^c q_b]^d` 的指标记号不规范，机械上无法唯一解析。
   影响：这是全文核心对象的定义式；在未修正前，关于 “`omega_ab=0` 与内部 holonomy 脱钩” 的后续表述都建立在一个记号损坏的入口上。  
   建议：改成可机械读取的标准写法，例如 `omega_ab = q_a{}^c q_b{}^d nabla_[c k_{d]}`，或等价的明确反对称化形式，并在全文保持一致。

## 警告项

1. Berry 线路的适用域与 `null congruence` 语言没有在文中机械闭合。  
   位置：`current/B/R1_round2.md:99-105, 128-132`  
   说明：文本取的是 “flat spacetime 中的光纤或偏振电路”，但这里的传播通常是介质/波导中的受限传播，不是标准真空 `null congruence`。文中因此写成“最保守读法就是 `omega_ab=0`”，这在方向上合理，但不是由同一套几何对象直接推出。  
   判定：不阻断主结论的“分层非等同”方向，但若要把该例当成严格同框架反例，需要补一句：此例只证明内部 bundle holonomy 可独立存在，不证明同一真空 null congruence 模型中的一一对应失败机制。

2. memory 支线没有给出可机械验算的主公式，因此该支线当前只能算旁证。  
   位置：`current/B/R1_round2.md:163-167`  
   说明：文中已明确“本轮未给出可无歧义落地的单一公式”；因此该处无法执行量纲、极限、代数三项硬校对。  
   判定：与正文自评一致，作为旁证可以保留；若在后续轮次上升为主张，必须补最小公式和 `omega_ab=0` 的显式同场设置。

## 通过项

1. `U[C] = P exp(-∮_C A)` 与 `U = P exp(-∫ A_i dxi^i)` 的指数结构在量纲上可自洽：路径积分应为无量纲，作为 Wilson line / path-ordered exponential 形式正确。  
   位置：`current/B/R1_round2.md:23, 84, 90`

2. Faraday 线路的方向判断通过。  
   位置：`current/B/R1_round2.md:40-58, 66-69`  
   核查：若 `k_a ∝ nabla_a u`，则 congruence hypersurface-orthogonal，`omega_ab=0` 的方向成立；同时 `Delta chi_F = RM lambda^2` 允许在固定几何下随 `lambda^2` 变化，故“`omega_ab=0` 且 `Delta chi_F != 0`”在逻辑上成立。

3. Berry / Pancharatnam 线路的相位方向与极限通过。  
   位置：`current/B/R1_round2.md:103-119, 129-132`  
   核查：
   - `gamma_B = -s Omega` 为无量纲相位关系；
   - 当 `Omega -> 0` 时，`gamma_B -> 0`；
   - 回路反向时 `Omega -> -Omega`，故 `gamma_B -> -gamma_B`，方向一致。

4. “不同 bundle 的 connection data 默认不可等同” 这一弱结论，与文内给出的 Faraday/Berry 两条线路是相容的，未见代数反向或极限反例。  
   位置：`current/B/R1_round2.md:191-195`

## 综合判定

- 致命/阻断：1 条  
- 警告：2 条  
- 结论：在修正 `omega_ab` 定义式之前，本稿不能按“机械校对通过”进入下一层推导；修正后，Faraday 与 Berry 两条主线可保留为支持“分层非等同”的非阻断材料。
