# REVIEWER Round 3: LP28-CphiCollapse

角色：恶意终审审稿人。审查对象为 A Round 3、B Round 3 revised、Inspector A/B、PI Round 3 synthesis。北极星：独立 input-side `C_phi` 是否存在，或所有可测 `C_phi` 坍缩为 c-axis coherence / oxygen-disorder / strain / dephasing / dz2/self-doping / sample quality。

工具记录：读取指定五个本地文件；按 REVIEWER 要求做最低限度查重，使用 `paper-search-mcp` 查询 La3Ni2O7 / bilayer nickelate / qz RIXS / c-axis coherence / oxygen stoichiometry / dz2-5d self-doping；因 arXiv/Semantic 返回稀疏，降级 WebSearch 查询相同主题。未发现完整同题先发，但发现多个相邻解释通道足以构成强竞争风险。

## 1. 五条拒稿级攻击或致命卡点

1. **核心变量仍是统计残差，不是物理自由度。**  
   `R_oe = P_oe - E_crossfit[P_oe | B_min]` 只定义了“没被当前 B_min 吸收的剩余项”。这不是证明了独立 `C_phi`，而是把独立性推给了 B_min 的完备性、测量误差、交叉拟合和匹配设计。只要 B_min 漏掉一个普通输入侧变量，`R_oe` 就会冒充新物理。作者需要证明 `R_oe` 对新增普通基线封闭，而不是只对当前七块 B_min 残留。[致命]

2. **`B_min` 与目标的同源污染无法由文字禁令消除。**  
   `P_oe` 来自 qz / odd-even susceptibility extraction；`B_min` 又需要 c-axis coherence、qz broadening、orbital/self-doping、dephasing等正常态谱学量。协议说“不能共享 target-generating information”，但实际实验中同一压力池、同一谱学窗口、同一矩阵元校准和同一背景模型几乎必然相关。审稿人不会接受“预冻结 pipeline”作为独立性证明；这只是把目标泄漏改名为 metrology design。[致命]

3. **没有同一样品数据包，所有阈值都是无校准的协议数字。**  
   `CV_R2 >= 0.85`、`0.65 < CV_R2 < 0.85`、`abs(Z_oe) >= 2`、`3 sigma_total`、`pooled shift > 0.10`、`N>=20` 都没有来自 La3Ni2O7 真实噪声、压力非均匀性、氧偏离、批次漂移或 RIXS/optics 重复性的功效分析。没有数据分布时，这些阈值不是理论结果，只是审稿前看起来严谨的门槛。[严重]

4. **分母与校准层可以直接制造 `P_oe`。**  
   A Inspector 已指出 `median_abs_chi_sum_reference` 有循环风险，`S_channel -> chi_unit` 校准仍隐藏。B revised 用 `sign(S)*max(abs(S), S_floor)` 修正了括号，但没有解决 odd/even 两通道的 self-absorption、polarization leakage、background subtraction、matrix-element drift 是否同阶于目标残差。若 `chi_odd + chi_even` 接近 floor，`P_oe` 的符号和大小就是校准产物。[严重]

5. **PI synthesis 把“可杀协议”夸成“理论 hinge”。**  
   当前版本没有推出新的哈密顿量约束、响应函数恒等式、可计算无量纲控制参量或材料族可迁移定律。A/B 最终都退到同一句话：做一个 leakage-free matched-pair residual test。把这称为 breakthrough-direction 是叙事升级，不是理论突破。[严重]

**如果必须挑一个致命错误：** `R_oe` 的独立性完全依赖 “B_min 已覆盖所有普通输入侧混杂且与 P_oe 提取独立” 这个未证明前提；这不是可能有问题，而是当前稿件中唯一承托北极星的逻辑支点。  
**作者的出路：** 必须提供真实 same-sample 数据，证明新增普通基线、独立批次、独立仪器校准和 negative controls 加入后 `R_oe` 仍稳定；否则只能作为注册协议存在。

## 2. 引用虚构 / 先发冲突风险

引用虚构风险：中等。当前 round3 几乎没有外部文献引用，主要引用 `pi_round2_synthesis.md` 和 inspector 文件，因此“虚构论文”风险不高；但“把未核实文献事实当作存在”风险很高。

需要 PI 独立 WebSearch / 文献核实的具体 claim：

- 是否已有高压 La3Ni2O7 的 qz-resolved odd/even RIXS 或等价 bilayer form-factor 数据，足以先于本项目定义 `P_oe`。
- 是否已有 c-axis Drude weight / optical conductivity under pressure 工作把 superconducting onset 与 c-axis coherence 直接关联；若有，本项目的 `C_phi` 很可能只是改名。
- 是否已有 oxygen stoichiometry、apical oxygen occupancy、inner/outer layer charge asymmetry 对 La3Ni2O7 superconductivity 的解释，足以吞掉 `R_oe`。
- 是否已有 strain / pressure-path hysteresis / structural phase-transition 工作给出与 `P_oe` 同方向的 normal-state contrast。
- 是否已有 dz2 / rare-earth 5d self-doping / ligand-hole normal-state 理论或谱学论文解释同一 pressure window。
- 是否已有“normal-state bilayer odd/even susceptibility imbalance predicts or diagnoses nickelate superconductivity”的近似命题；若有，`P_oe` 不是新变量。

先发冲突风险：中高。最低限度检索未发现完整同题“`R_oe` residualization after B_min”论文，但相邻文献主题已经覆盖结构、氧、压力相变、self-doping、c-axis coherence 和 bilayer response。真正投稿时，任何一条相邻解释都可以把本文压成“统计控制协议”，而不是新机制。

## 3. 是否仍只是协议包装

是。Round 3 的主要成就是把失败条件写清楚，而不是形成理论突破。

它没有证明独立 input-side `C_phi` 存在；也没有证明所有 `C_phi` 坍缩。它只规定：如果未来某个 same-sample packet 满足一长串前置条件，则可以判定 survival / collapse / gray zone。这个价值是方法学和实验注册价值，不是理论物理结果。`B_plus` 是 tautology，`B_min` 是经验残差设计，二者之间没有新定理。

## 4. 是否有可挽救版本

有，但只能挽救为有界协议，不是突破候选。

最小可挽救条件：

1. 提供真实 same-sample pressure packet，含 qz/polarization/form-factor odd-even susceptibility 和完整 B_min，且 superconducting outputs 密封到 residual call 之后。
2. 用外部 calibration set 固定 `S_channel -> chi_unit`、`S_floor`、background、polarization leakage 和 matrix-element correction。
3. 证明 c-axis/qz coherence proxy 与 `P_oe` extraction 独立采集或独立降维；否则直接 protocol failure。
4. 在至少两个 batch、最好三个 batch 中做 leave-one-batch-out；negative controls 必须包括 non-bilayer / high-disorder / probe-window / calibration blank。
5. 预注册功效分析和阈值来源；没有真实噪声模型时不得使用 `CV_R2`、`Z_oe`、`3 sigma` 作为发现阈值。
6. 结论限定为“该 packet 下 `P_oe` 是否含 B_min 外残差信息”，禁止写成 universal `C_phi` no-go 或 phase-bus breakthrough。

## 5. 最终判定

**PASS AS BOUNDED PROTOCOL**

理由：当前版本已足够作为一个严格的预注册残差检验协议，但不构成理论突破候选。若按 PI synthesis 的“real theoretical hinge / breakthrough-direction”表述投稿，我会建议拒稿；若降格为有界实验协议并补真实数据包与独立校准，可进入大修式技术评审。
