# LP7-S4 Phase 1 — A 正规推导

生成时间：2026-06-01

## 0. 输入与边界

本推导只处理 LP7-S4：黑洞信息悖论作为强引力统一判据。

不声称：

- 黑洞信息悖论尚无任何解决进展。
- island formula 已经给出所有物理问题的最终答案。
- S4 能直接给出统一公式。

本推导目标：

> 把黑洞信息悖论压缩为一组不可同真的假设，并判断各解决路线改写了哪条假设。

## 1. 四假设判据 J_BH

定义：

`J_BH = {Hawking_thermal, Complete_evaporation, Unitarity, No_new_entropy_rule}`

含义：

1. `Hawking_thermal`：半经典 Hawking 计算给出近热辐射，辐射细粒度熵按 Hawking 近热结果持续增长。
2. `Complete_evaporation`：黑洞完全蒸发，无稳定 remnant、无 baby universe 信息库。
3. `Unitarity`：纯态形成黑洞后，最终完整辐射仍为纯态。
4. `No_new_entropy_rule`：辐射熵按外部 QFT 区域熵计算，不引入 islands / quantum extremal surfaces / replica wormholes 等新规则。

四者不可同真。

最小理由：

- 若 1、2、4 成立，最终辐射保持混态，信息丢失。
- 若 3 成立，最终辐射应为纯态，Page curve 后期下降。
- 因此至少一条必须被修改。

## 2. Page curve 判据

Hawking 曲线：

`S_rad(t)` 随蒸发时间单调增长，直到黑洞消失仍保留大量熵。

Page curve：

`S_rad(t)` 早期增长，Page time 后下降；若初态纯且完全蒸发，晚期外部完整辐射应恢复纯态。

因此，统一公式或候选理论必须给出：

`S_rad^candidate(t) ≈ min(S_Hawking(t), S_BH(t))`

或等价的细粒度熵机制。

## 3. 解决路线分层

| 路线 | 修改的假设 | 作用 | 边界 |
|---|---|---|---|
| island / replica wormhole | 修改 `No_new_entropy_rule` | 通过广义熵、QES、路径积分新 saddle 恢复 Page curve | 需要解释微观含义与适用范围 |
| remnant | 修改 `Complete_evaporation` | 信息留在残余自由度 | 需处理 remnant 无限种类/稳定性问题 |
| baby universe | 修改 `Complete_evaporation` 或外部可访问 Hilbert space | 信息进入外部不可访问 sector | 对外部观察者仍可能非幺正 |
| stimulated emission | 修改 `Hawking_thermal` 的信息通道假设 | 辐射可能携带信息 | 需证明足以恢复完整 Page curve |
| complementarity / ER=EPR | 修改可同时使用的 EFT/观测者描述 | 试图保住 unitarity 与外部一致性 | 可能引出 firewall/观测者一致性问题 |
| firewall | 修改低能 EFT 或 horizon smoothness | 保住 unitarity 但牺牲等效原理/平滑视界 | 二级矛盾未消失 |
| “无悖论”路线 | 拒绝某个前提组合 | 可能重定义问题 | 必须说明 Page curve 或信息账本 |

## 4. island route 的地位

island/replica wormhole 不是简单地“半经典 Hawking 算错了”。更精确地说：

它保留了部分半经典引力技术，但改变了 fine-grained entropy 的计算规则：

`S(R) = min_ext [ Area(∂I)/(4G_N) + S_bulk(R ∪ I) ]`

这使辐射熵在 Page time 后选择含 island 的 saddle，从而得到 Page curve。

因此，S4 对 LP7 的判据是：

任何统一公式必须说明：

- 是否有 island/QES 等效结构；
- 若没有，如何替代地产生 Page curve；
- 若拒绝 Page curve，如何放弃或修改 unitarity/complete evaporation。

## 5. Adami / stimulated emission 路线

受激辐射路线声称 Hawking 原始 derivation 忽略了受激辐射信息通道。

S4 处理：

- 列为反例栏/替代路线。
- 不在本 Phase 判定其完全解决悖论。
- 关键审查点是：它是否恢复完整 Page curve，而不只是恢复部分 classical information capacity。

## 6. 结论

结论类型：**有边界**。

核心结论：

黑洞信息悖论作为 LP7-S4 的价值，是给出强引力统一判据而不是一个未解口号。真正不可同真的是 `J_BH` 四假设组合：Hawking 近热辐射、完全蒸发、幺正性、无新熵规则。island/replica wormhole 已经提供恢复 Page curve 的主流路线，但它通过修改 fine-grained entropy 规则和引入新 gravitational saddle 解决矛盾。其他路线则分别修改完全蒸发、Hawking 热性或低能 EFT/视界平滑性。

## 7. K 条目候选

K80 [✅ L2] 黑洞信息悖论的最小矛盾是 `J_BH={Hawking_thermal, Complete_evaporation, Unitarity, No_new_entropy_rule}` 四假设不可同真。
  来源：Hawking 信息悖论综述；Page curve；本 Phase 判据化。
  适用条件：纯态形成黑洞，完全蒸发，无 remnant/baby universe，外部辐射熵按 Hawking 半经典区域熵计算。
  math_object：`J_BH`, `S_rad(t)`, Page curve
  验证状态：待 B 独立验证。

K81 [✅ L2] island/replica wormhole 通过修改 fine-grained entropy 规则恢复 Page curve，而不是保留 naive Hawking entropy rule。
  来源：Almheiri et al. 2020; Wang-Li 2024。
  适用条件：适用 island formula / QES / replica wormhole saddle 的半经典引力系统。
  math_object：`S(R)=min_ext[Area/4G+S_bulk(R∪I)]`
  验证状态：待 B 独立验证。

K82 [⚠️ L3] stimulated emission / remnant / no-paradox / complementarity 路线均是修改 `J_BH` 不同假设的替代路线，不能在 S4 Phase 1 中判作完整解决。
  来源：Adami 2024/2025; Rovelli-Vidotto 2025; Ong 2025; complementarity/firewall 文献。
  适用条件：替代路线讨论层。
  math_object：`assumption-relaxation matrix`
  验证状态：待 B 独立验证。

## 8. 待 B 验证清单

1. `J_BH` 四假设是否足够表达最小矛盾。
2. island route 是否应写成“解决 Page curve 但修改熵规则”。
3. stimulated emission 是否只列反例栏，还是应升级为主路线。
4. S4 是否应该收官为“有边界”而非“已解决”。
