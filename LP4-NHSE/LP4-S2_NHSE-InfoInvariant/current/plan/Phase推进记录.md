# Phase推进记录

## Phase 1A-1
完成：QLIF 多体推广的初始定义

## Phase 1B-1
完成：动力学量不是不变量的初始反证

## Phase 1A-2
完成：HN-Hubbard 中 freeze 算符规则

## Phase 1B-2
完成：freeze 偏置攻击

## Phase 1A-3
完成：L=4 最小模型对照

## Phase 1B-3
完成：最小模型反例

## 下一步
Phase 1A-4 / 1B-4：bulk 极限与 sector-independent 标签检验

## Phase 1A-4
完成：`L->∞` bulk 极限判据，提出三种 freeze 相对差异必须消失的条件。

## Phase 1B-4
完成：指出 NHSE 的 OBC 边界敏感性可能让 freeze 差异保持 `O(1)`，不能默认是局域边界误差。

## 下一步
Phase 1A-5 / 1B-5：PBC/OBC 分流判别表

## Phase 1A-5
完成：PBC/OBC 分流判据，说明 OBC 与 PBC 必须分开检验。

## Phase 1B-5
完成：指出 PBC/OBC 分流不能自动拯救不变量地位。

## 下一步
Phase 1A-6 / 1B-6：sector 结构一致性

## Phase 1A-6
完成：sector 结构一致性判据，要求不同 `N` 之间必须形成平台或清晰相变线。

## Phase 1B-6
完成：指出不同 `N` 之间的差异可能只是 Hilbert 空间结构差异，不是拓扑标签。

## 下一步
Phase 1A-7 / 1B-7：固定填充率平台判据

## Phase 1A-7
完成：固定填充率平台判据，要求出现稳定平台才可能继续谈不变量。

## Phase 1B-7
完成：指出平台可能是有限尺寸或采样分辨率假象。

## 下一步
Phase 1A-8 / 1B-8：平台宽度收敛

## Phase 1A-8
完成：平台宽度收敛判据，要求 `lim W(L)>0`。

## Phase 1B-8
完成：指出平台宽度可能随 `L` 缩窄，或三种 freeze 极限不同。

## 下一步
Phase 1A-9 / 1B-9：平台中心共用性

## Phase 1A-9
完成：平台中心共用性判据，要求 `rho*(L)` 在 freeze/sector/boundary 下有共同极限。

## Phase 1B-9
完成：指出平台中心可能随 freeze、OBC、sector 漂移，且可能只是拟合参数。

## Phase 1A-10
完成：Phase 1 综合判断，QLIF 是可检验的 directionality diagnostic，但尚未是拓扑不变量。

## Phase 1B-10
完成：B 侧裁决，建议进入 Phase 2 数值验证而非直接收官。

## 下一步
Phase 2：最小数值检验表

## Phase 2A-1
完成：最小数值脚本与结果表生成。

## Phase 2B-1
完成：最小数值初筛，发现大多数组合为正号，但 PBC/dephase/clamped 存在少量零/翻符。

## 下一步
Phase 2A-2 / 2B-2：扩大到 `L=10` 并定位翻符点。

## Phase 2A-2
完成：扩大规模门槛并复跑，确认高填充率与特定 freeze 规则下存在翻符。

## Phase 2B-2
完成：初裁为“诊断量优先，不变量未立”。

## 下一步
Phase 2A-3 / 2B-3：定位翻符填充率区间与受限成立条件。

## Phase 2A-3
完成：翻符区间定位，高填充率 `rho≈0.8/0.9` 最明显。

## Phase 2B-3
完成：高填充翻符更像占据数效应和边界堵塞，不支持不变量成立。

## 下一步
Phase 2A-4 / 2B-4：检查翻符是否对 freeze 规则稳健。

## Phase 2A-4
完成：受限条件提炼，得到低填充正、高填充负、`rho≈0.75` 过渡带的分段图景。

## Phase 2B-4
完成：受限条件反证，指出这意味着原始“不变量”命题失败，新对象需单独命名。

## 下一步
Phase 2A-5 / 2B-5：整理失败链并命名新对象。

## Phase 2A-5
完成：失败链整理，并命名新对象 `density-resolved directionality diagnostic (DRDD)`。

## Phase 2B-5
完成：失败确认，原始不变量命题失败，保留新对象继续推进。

## 下一步
Phase 3：新对象 DRDD 的独立验证或收官整理。

## Phase 3A-1
完成：原始 QLIF 定义对照，明确当前数值脚本不是原始 QLIF。

## Phase 3B-1
完成：代理量偷换反例，明确 Phase 2 结论只能归类为 DRDD/DR-NHDD，而非原始 QLIF 最终裁决。

## Phase 3A-2
完成：术语边界，建议将 DRDD 改名为 `density-resolved non-Hermitian directionality diagnostic (DR-NHDD)`。

## Phase 3B-2
完成：禁止把 DR-NHDD 混称为 QLIF 或 invariant。

## 下一步
Phase 3A-3 / 3B-3：Phase 2 结果重归类。

## Phase 3A-3
完成：Phase 2 结果全部重归类为 DR-NHDD 结论。

## Phase 3B-3
完成：确认原始 QLIF 仍未裁决。

## Phase 3A-4
完成：原始 QLIF 必须另开新任务，不能复用 DR-NHDD。

## Phase 3B-4
完成：列出不得偷换的表述边界。

## 下一步
Phase 3A-5 / 3B-5：收官前置检查。

## Phase 3A-5
完成：收官前置检查，原始 QLIF 失败、DR-NHDD 成立、原始 QLIF 必须另开任务。

## Phase 3B-5
完成：收官前置检查，确认当前项目不应再沿用“原始不变量”表述。

## 下一步
执行收官写回：同步当前状态、总结、审计记录与候选池。
