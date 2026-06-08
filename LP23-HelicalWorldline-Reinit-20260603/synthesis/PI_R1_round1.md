# PI 综合 | LP23-R1 Round1

日期：2026-06-03

## 输入

- A：`current/A/R1_round1.md`
- B：`current/B/R1_round1.md`
- INSPECTOR_A：`synthesis/inspector_A_R1_round1.md`
- INSPECTOR_B：`synthesis/inspector_B_R1_round1.md`

## INSPECTOR 判定

- A：PASS WITH WARNING。阻断 0，警告 3。
- B：PASS WITH WARNING。阻断 0，警告 2。

警告不推翻本轮主结论，但约束后续写法：

1. `F_AB` 不能被写成已经与 screen tensor 同型的对象；必须先说明 pullback、基、bundle morphism 或 frame choice。
2. `F` 的 `L^-2` 量纲判断只能作为给定 coordinate/base convention 下的条件句，不能写成无条件 SI 断言。
3. Hopf/Berry 曲率反例只能作为分层警告；若要承担阻断功能，需给出与 spacetime congruence 的显式映射。
4. Berry phase 面积公式的正负号依赖 orientation/gauge convention。
5. “`F_phase in Omega^2(internal bundle)`” 类型不精确；曲率应写成 base 上的 Lie-algebra-valued 2-form。

## A/B 汇合判断

A 的成熟框架是 Lorentzian null congruence / optical geometry / two-spinor / null-geodesic contact geometry。B 的成熟框架是 polarization optics / Berry-Pancharatnam holonomy / Faraday-spin optics / memory observables。两者独立，但结论同向：

- `null geodesic space` 的 contact/Engel/retrievability 结构本身已有强 prior art 覆盖，不能作为 R1 新增量。
- 整体 `U(1)` phase 不改变 `k^a`，因此不改变只由 `k^a` 与 `nabla k` 定义的 optical twist。
- 非零 phase/Berry/Faraday holonomy 可以与零 optical twist 共存。
- 强式 `F_AB = chi omega_AB` 缺少自然量纲、自然同型、统一 gauge weight 与唯一 connection source。

## 本轮结论

R1 强版本判定为当前证伪：

> phase curvature / vertical holonomy 直接等同或自然生成 null congruence optical twist。

R1 弱版本仍有边界生命：

> projective spinor/contact 语言可以容纳两套相关但不同的 connection data：一套控制 polarization / phase / Faraday / memory / screen-frame holonomy observables，另一套控制 congruence optical data。二者不能无条件等同；只有在额外结构存在时才可能耦合。

这已经不是原来的“phase holonomy 统一 causal cone 与 optical twist”的强声张，而是一个分层命题：说明哪些 observables 属于 internal/polarization sector，哪些属于 horizontal/screen/congruence sector。

## 是否硬停止

不触发硬停止。

理由：强式已经被 A/B 同时压死，但弱式仍可能产生可检验、可发表的“分层定理/反例定理/非等同定理”。SOP 最少 3 轮；当前 R1 仅完成第 1 轮，除非 Round2 证明弱式完全被先发覆盖或只是重命名，否则不得收官。

## Round2 指令

Round2 不再追 `F_AB = chi omega_AB` 的强等式。下一轮只检验弱式是否有严格增量：

- A 路：在 4d Lorentzian spin/null congruence 框架下，寻找最小附加结构，使 screen-frame `SO(2)` connection 与 spin/polarization phase connection 有协变绑定；判断这是否已经是 Newman-Penrose/GHP、Robinson/CR、Walker-Penrose 或 spin-optics 既有内容。
- B 路：构造或定位“`omega_ab=0` 但 polarization/Faraday/memory holonomy 非零”的正面 observable，并检查它是否只是已有 Faraday/Berry/memory 文献的重述。

Round2 的生死口：

1. 如果弱式只能说“两个 bundle 都有 connection/holonomy”，则 R1 退化为术语重命名。
2. 如果弱式能给出一个清晰 theorem：在特定最小结构下 phase observable 与 screen-frame transport 有可检验关系、同时严格不等于 optical twist，则 R1 保留为有边界方向。
