# 矛盾深挖与子命题提取

## 五个为什么

**表层矛盾:** DW 母相既像超导前体，又像通过 layer decoupling 抑制 bulk SC。

1. 为什么 DW 会同时像前体和抑制器？  
   因为 static DW order 与 dynamic DW/spin/charge fluctuations 承担不同功能。

2. 为什么这个功能差异重要？  
   因为 local pairing reservoir 与 bulk phase stiffness 是两个门槛；前者不自动推出后者。

3. 为什么 bulk phase stiffness 在 RP 镍酸盐中特别脆弱？  
   因为 superconducting bulk response 依赖跨 Ni-O 层的 dz2/apical-O/dz2 phase bus，而 static DW 可重构或切断这个通道。

4. 为什么 pressure/DW collapse 数据还不足以证明机制？  
   因为 pressure 同时改 bandwidth、carrier、structure、domain、oxygen/disorder；DW collapse 与 SC emergence 可能是共同第三变量的结果。

5. 最基础的理论问题是什么？  
   Layered unconventional superconductors 的设计瓶颈可能不是 pairing scale，而是 local pairing reservoir 与 recoverable phase bus 是否能被独立调控并同时满足。

## 自底向上子命题

### LP28-S1: Phase-bus predictor 是否独立于 bulk output？

**A vs B:**  
命题A：`I_phi = E_z2*C_phi/(kBT+hbar Gamma_phi+E_floor)` 可用 input-side spectroscopy/structure/dephasing 独立预注册，并预测 bulk output 的出现窗口。  
命题B：`I_phi` 无法脱离 shielding/Tc/phase boundary 后验标定，最终只是 output 的重命名。

**三步推进:**  
Phase1 固定 `E_z2/C_phi/Gamma_phi/E_floor` 单位和谱窗；Phase2 用现有 ambient PRL/Zenodo 数据做非SC baseline；Phase3 设计 pressure/strain blind test。

**状态:** 新子命题，待验证。

### LP28-S2: Static DW partition 与 dynamic pairing reservoir 能否分离调控？

**A vs B:**  
命题A：存在调控窗口能削弱 static DW 对 dz2 phase bus 的分割，同时保留 DW/spin/charge fluctuations 作为 pairing reservoir。  
命题B：解除 static DW partition 必然同时破坏 pairing reservoir，因此三门控路线不可实现。

**三步推进:**  
Phase1 找 pressure/strain/pump 下 static DW amplitude、fluctuation linewidth、c-axis spectral weight 的同步数据；Phase2 建立 static/dynamic 分量分离判据；Phase3 判断是否存在窗口。

**状态:** 新子命题，待验证。

### LP28-S3: 三门控筛选是否优于 Tc/zero-resistance 搜索？

**A vs B:**  
命题A：`pairing reservoir + recoverable phase bus + independent bulk output` 三门控筛选能更早排除 filamentary/2D precursor traps，指导材料优化。  
命题B：三门控只是复杂化表述，实际预测能力不优于 pressure-Tc/zero-resistance 搜索。

**三步推进:**  
Phase1 对已报道 La4Ni3O10/Pr4Ni3O10 pressure results 重新分类；Phase2 标注哪些是 bulk、filamentary、ambiguous；Phase3 比较三门控与传统指标的误判率。

**状态:** 新子命题，待验证。
