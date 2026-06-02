# B博士 Phase 5 作业 — physical commutant / edge-global mode 显式构造

## ⚡ 审核入口（PI 只读）

physical commutant X：未构造出；候选均归入 boundary charge、Tomita mirror、另一侧 TFD 表示或 gauge redundancy。  
最接近成功候选：QES area / dilaton edge mode。  
失败原因：在 JT 中 QES area/dilaton mode由 boundary Schwarzian/constraint 数据决定，不是与 `A_bdy^wide` 对易且独立的物理 observable。  
split bridge：未闭合；split failure 仍是 non-factorization 压力，不是 proper inclusion 定理。  
CP-010 影响：压缩但不关闭；commutant 路线目前不能证明 `[A_full:A_bdy]>1`。  
K1.10 升级判定：维持 ⚠️L1；对宽代数 no-go 方向有支持。

---

## §1 表示空间

本阶段把 `A_bdy` 分成窄/宽两种：

- 窄：单侧 SYK single-trace；
- 宽：SYK 加 bath/radiation，也即 Page curve 物理可用代数。

`physical commutant` 必须在 gravitationally constrained physical Hilbert space 或 code subspace 上定义。GNS 标准形式的 commutant不足够。

## §2 候选清单

### 2.1 ADM / boundary Hamiltonian

Hamiltonian 属于 boundary algebra 或其 affiliated observable。它不是 commutant 中的新元素；而且它通常不与所有 time-dependent boundary operators 对易。

判定：失败。

### 2.2 JT dilaton boundary charge / Schwarzian zero mode

JT 纯引力自由度由边界 Schwarzian 描述。dilaton profile 与 boundary reparametrization/energy constraint 相连。

若把 dilaton/QES area 当作 `X`，它不是独立于 boundary 数据的物理 observable；若它是 boundary charge，则 `X in A_bdy`；若它是 gauge redundancy，则不是 observable。

判定：最接近成功，但失败。

### 2.3 island QES area operator

QES area 在 JT 中对应 dilaton at extremal surface。它可能看似与 bulk matter local algebra 对易，但不保证与全部 boundary algebra 对易。更关键的是，它受 constraint 与 generalized entropy extremization 决定，不能证明 `X∉A_bdy`。

判定：未构造成功。

### 2.4 gravitational Wilson line / dressing endpoint

引力 dressing 的 endpoint 通常落在 boundary。若 endpoint data 在 boundary algebra 中，则 dressing 不给出独立 commutant；若 endpoint 未指定，则算符不是 gauge-invariant observable。

判定：失败。

### 2.5 Donnelly-Wall edge mode

Gauge theory entanglement edge modes提供跨域动机，但 JT/SYK 中没有在当前资料内构造出与 `A_bdy^wide` 全部对易且不属于 `A_bdy^wide` 的 edge mode。

判定：动机成立，显式构造失败。

### 2.6 Tomita mirror operator

`J A_bdy J` 在 GNS 中属于 commutant，但它是 state-dependent mirror，不自动是 physical Hilbert space 的独立可观测量。

判定：不能作为 physical `X`。

### 2.7 opposite-side TFD operator

双侧 TFD 中另一侧算符与单侧代数对易，但本课题物理问题是单侧 evaporating black hole + radiation/bath 的信息恢复。另一侧 TFD commutant 不是所需的单侧 physical commutant。

判定：表示伪影，失败。

### 2.8 microcanonical energy-window projector

Energy-window projection 在 microcanonical crossed product 中可用，但它是 ensemble/weight 选择的一部分，不是 canonical wide boundary 的独立 commutant。若作为 projector，它也与 Type III_1 canonical algebra 的 projection obstruction 相冲突。

判定：不能关闭 canonical CP-010。

## §3 split property bridge

Split failure 可说明没有 Type I 中间因子：

`A_bdy(region1) ⊂ F ⊂ A_full(region2)`

但 proper inclusion 需要额外桥梁，例如：

- nontrivial center；
- Haag duality failure with physical observable；
- finite-index expectation failure；
- explicit `X∈A_full\A_bdy`。

本阶段没有找到这条桥梁。因此 split failure 仍是结构压力。

## §4 对 CP-010 的影响

没有 physical commutant `X`，不能证明：

`A_bdy' ⊋ C1`

在所需物理表示中成立。尤其对宽 `A_bdy^wide`，所有显式候选都可被 boundary/radiation data、constraint 或 state-dependent mirror 解释掉。

这削弱了 "island 给出新物理代数" 的方向，支持 A 线的宽代数 no-go：island reconstruction 更像已有宽边界代数中的 recovery。

## §末 结果登记建议

- K5.4：Phase 5 未构造出 physical commutant。
- K5.5：QES area/dilaton edge mode在 JT 中不构成独立 commutant；它受 boundary Schwarzian/constraint 控制。
- K5.6：split failure 无 explicit bridge 时不能推出 `[A_full:A_bdy]>1`。
- CP-010：开放但进一步压缩。
- K1.10：维持 ⚠️L1。
