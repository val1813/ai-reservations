# Confirmed Motivation: Capacity-Normalized Bound on Non-Markovian Backflow

## 一句话Motivation
Non-Markovian backflow bounds have been either general-but-expensive (MSV entropic, requires tomography) or specific-but-unbounded (BLP detects but doesn't constrain magnitude); we provide the first combinatorially-derived bound that is operationally accessible on current hardware.

---

## 三段论证

### 1. 问题 (Problem)
Non-Markovianity—information flowing back from environment to system—is a defining feature of open quantum dynamics beyond the Markov approximation. Detecting it (BLP trace-distance measure, RHP CP-divisibility criterion) and classifying it (Buscemi process-matrix framework) are well-developed. But constraining *how much* backflow can occur remains open: the only existing quantitative bound (MSV entropic) requires full quantum state tomography of the joint SE state—a measurement that scales exponentially and is impractical beyond ~5 qubits.

### 2. 现状 (Status quo)
- **BLP measure** (Breuer et al., PRL 2009): Detects non-Markovianity by integrating positive trace-distance derivative. Detects presence, doesn't bound magnitude.
- **RHP criterion** (Rivas et al., PRL 2010): Characterizes Markovianity as CP-divisibility. Yes/no criterion, not a quantitative bound.
- **MSV entropic bound** (Megier et al., PRL 2021): Upper bounds information backflow via Holevo skew divergence. General (any CPTP), but requires full tomography.
- **Buscemi classification** (Buscemi et al., PRX Quantum 2025): Separates causal vs noncausal revivals via QCMI. Classification, not magnitude.
- **Gap**: No bound exists that is (a) quantitative, (b) operationally simple (projective measurements only), and (c) rigorously derived from physical principles.

### 3. 窗口 (Why now)
Three developments make this bound timely:
1. **Superconducting hardware maturity**: IBM and Google devices now routinely perform mid-circuit measurements and conditional resets—projective population measurements of $q_S$, $q_E$ are standard operations.
2. **Finite-information paradigm**: Zurek's einselection (RMP 2003) established that pointer bases carry finite classical information. The logical next step—constraining dynamics from this finiteness—remained untaken.
3. **Complementarity gap**: MSV showed entropic bounding works but requires tomography. The natural complementary question—"can we bound backflow with only population counts?"—is answered affirmatively here via the pigeonhole principle.

---

## Reader 5问检验

### Q1. Relevance: 第一段能让非本领域读者理解为什么重要?
**检验**: Non-Markovian dynamics matter whenever a quantum system talks to its surroundings—from qubit decoherence to photosynthetic energy transfer. Knowing HOW MUCH information can flow back (not just IF it flows back) is a basic constraint that every open quantum system must satisfy. This paper gives that constraint in a form you can measure with simple population counts.
**通过**: Yes—the backflow constraint is a universal property, not a niche measure.

### Q2. Novelty: 摘要清晰区分"前人做了什么"和"我们做了什么新东西"?
**线左边(前人)**: BLP detects NM presence. RHP characterizes via CP-divisibility. Buscemi classifies causal vs noncausal. MSV bounds backflow entropically (requires tomography).
**线右边(我们)**: First combinatorial bound ($\mathcal{R} \leq q_S/q_E$) requiring only projective population measurements. Pigeonhole principle proof.
**通过**: Clear differentiation. 无重叠。

### Q3. Trust: 每个核心声称有≥1种独立验证方式?
| 声称 | 验证方式 |
|------|---------|
| $\mathcal{R} \leq q_S/q_E$ | ①组合证明(pigeonhole principle, 正文Eq.推导) ②碰撞模型数值例(SM Table) |
| 只需projective measurements | ①$q_S$, $q_E$定义=单qubit projective $\langle 0|\rho|0\rangle$ ②无需$\varrho_{SE}$重建 |
| Unidirectional $L$ without $|0\rangle\langle 1|$ | ①能量论证($\Delta E \gg k_B T$, SM §2) ②Jaynes-Cummings推导 |
| 与MSV互补 | ①MSV需tomography vs 我们只需populations (两者执行需求对比在SM §3) |
**通过**: 4/4核心声称有独立验证。

### Q4. Reuse: 方法和数据是否足够让同行复现?
**检验**: 删除所有记忆→看方法和数据能复现吗?
- $L$ operator形式给出: Eq.(2) + SM推导(Jaynes-Cummings → Born-Markov)
- 定义明确: $q_S$, $q_E$, $C_F$, $N_{\rm back}$, $\mathcal{R}$都有操作定义
- 证明完整: 三步证明在正文+SM
- 数值例: 碰撞模型参数完整
- 实验实现: SM §5 gate-level方案(Stinespring + cross-resonance)
**通过**: 复现可行。

### Q5. Meaning: 诚实讨论了边界和局限?
- $\mathcal{R}$不是$N_{\rm back}/N_F$(实际回流分数) — 明确说明
- $q_S < q_E$条件 — 明确说明非平凡区间
- $T_1$修正 — $|1\rangle \to |0\rangle$ relaxation的影响
- 三类失效模式(a,b,c) — 明确说明violation的可能解释
- 双向动力学扩展 — Discussion末段
**通过**: 局限诚实讨论。
