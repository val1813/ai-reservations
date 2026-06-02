# A博士 Phase 6 作业 - 边界代数分离命题

## ⚠ 审核入口（PI只读）

P6-A 是否成型：是，但只能作为 code-subspace proposition。  
wide algebra gap：无独立 `O(1)` gap；受 recovery error 控制。  
narrow algebra gap：`O(1)` 倾向成立，但依赖窄代数定义不含 decoder。  
theorem 等级：⚠️L1，不是 L2。  
K1.10 升级判定：维持 ⚠️L1。  
最脆弱步骤：`F(epsilon_N)` 的精确 bound 依赖 approximate recoverability 定理和具体 code error，当前只能写成定性函数。

---

## §1 代数定义

令 `H_code` 是 post-Page SYK/JT code subspace。定义：

- `A_full`：包含 island bulk effective operator 的 code algebra。
- `A_bdy^narrow`：单侧 SYK single-trace / simple boundary algebra，不含 bath/radiation decoder。
- `A_bdy^wide`：SYK 与 bath/radiation 生成的宽代数，允许 entanglement-wedge reconstruction。

三者的关系不是全 Hilbert space 包含定理，而是 code-subspace 层面的 operational inclusion。

## §2 命题 P6-A

**Proposition P6-A（boundary-algebra separation）**  
给定 reference state `rho_0` 与 island infallen-qubit excitation `rho_1`。若：

1. `A_full` 中存在 O(1) 可区分 `rho_0,rho_1` 的 bulk observable；
2. `A_bdy^narrow` 不包含对应 decoder/recovery resource；
3. `A_bdy^wide` 存在误差 `epsilon_N` 的 recovery map `R_N`，可在 code subspace 上恢复 `A_full` 的相关态区分；

则：

`Delta_narrow = S_Afull(rho1||rho0)-S_Anarrow(rho1||rho0) = O(1)` 倾向成立；

而

`0 <= Delta_wide = S_Afull(rho1||rho0)-S_Awide(rho1||rho0) <= F(epsilon_N)`，

其中 `F(epsilon_N)->0`。

## §3 证明骨架

Petz 单调性给出 `Delta >= 0`。若存在近似 recovery，则相对熵单调性的 equality defect 被 recovery error 控制。对宽代数，post-Page entanglement wedge reconstruction 正是这种 approximate sufficiency 的物理来源，因此不能维持独立的 `O(1)` gap。

对窄代数，缺少 bath/radiation decoder。`rho_1` 的 island excitation 在 `A_full` 中可由局域 bulk operator 区分，但在 simple single-trace algebra 上被 scrambling / typicality 压低可见性，因此 `Delta_narrow` 可以是 `O(1)`。

## §4 文献支撑

本轮多源检索确认：

- CPW, *Large N algebras and generalized entropy*, JHEP 04 (2023) 009, DOI `10.1007/JHEP04(2023)009`，提供 Type II_infinity large-N algebra 与 generalized entropy 的正式版本支撑。
- Gao, *Modular flow in JT gravity and entanglement wedge reconstruction*, JHEP 06 (2024) 151, DOI `10.1007/JHEP06(2024)151`，支持 JT 中 modular flow 可在 semiclassical/PETS 极限扩展 causal wedge algebra 到 entanglement wedge algebra。
- Takesaki operator algebra 章节给出 modular automorphism / conditional expectation 背景。
- Petz sufficiency theorem 提供 equality/recovery 判据。

## §5 结论

Phase 6 A 线没有证明新的全局 no-go theorem。它把 M.B 改写为一个边界代数选择命题：

> M.B 的 `O(1)` gap 是窄代数现象；一旦采用 Page curve 物理上自然的宽 radiation/bath 代数，gap 被 recovery error 控制，岛屿公式更像 algebraic recovery/bookkeeping，而不是独立 Lorentzian transport mechanism。

