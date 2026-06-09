# Writing Rationale Matrix — LP32-S2

## Abstract
- **功能**: 独立摘要，完整传达核心创新
- **服务Motivation**: Q2(Novelty) — 区分前人和我们
- **范文参考**: Gough 2025 abstract structure
- **证据**: 无需引用(摘要自包含)
- **检查**: ≤150词, 清晰区分"前人做了什么"和"我们做了什么", 无AI致谢

## §I. Introduction
### ¶1: Broad context + DESI puzzle
- **功能**: 建立大背景→DESI DR2动态暗能量信号
- **服务Motivation**: Q1(Relevance) — 让非本领域读者理解为什么重要
- **证据**: DESI:2025, Li:2025, Pang:2025

### ¶2: Phantom-crossing theoretical challenge
- **功能**: 解释为什么w(z) crossing是理论难题
- **服务Motivation**: Q2(Novelty) — 建立gap
- **证据**: Hu:2005, Feng:2005, Linder:2024, Khoury:2025, Chen:2026

### ¶3: Gough's empirical finding + gap
- **功能**: 引入information dark energy假说→指出缺微观理论
- **服务Motivation**: Q2(Novelty) — sharp gap statement
- **证据**: Gough:2025, Landauer:1961

### ¶4: Our contribution — microscopic theory preview
- **功能**: 宣布我们做了什么
- **服务Motivation**: Q2(Novelty) — 我们的回答
- **证据**: 自引用(DGF框架)

### ¶5: Distinction from prior mechanisms
- **功能**: 具体说明与Hu/quintom/DM-DE的区别
- **服务Motivation**: Q2(Novelty) — 差异化
- **证据**: Hu:2005, Feng:2005, Khoury:2025, Linder:2025

### ¶6: Roadmap (可考虑删除/简化 — P4要求)
- **功能**: 导航
- **服务Motivation**: N/A

## §II. Microscopic Theory
### §II.A: Qubit ensemble
- **功能**: 建立基本框架
- **服务Motivation**: Q4(Reuse) — 定义清晰
- **证据**: 定义性内容, 引用DGF:2024

### §II.B: Mean-field Hamiltonian + $a_c^2$
- **功能**: 推导临界分数
- **服务Motivation**: Q3(Trust) — 分析推导
- **证据**: 量子多体理论标准结果

### §II.C: Complex Langevin dynamics
- **功能**: 动力学方程
- **服务Motivation**: Q3(Trust) — 从Lindblad推导
- **证据**: SM Appendix A完整推导

## §III. Driving Function
### §III.A: $\mathcal{P}_{\rm coll}$ computation
- **功能**: 构建驱动函数
- **服务Motivation**: Q4(Reuse) — 可复现计算
- **证据**: Sheth:1999, Eisenstein:1998, Tinker:2008

### §III.B: Landauer assumption
- **功能**: 讨论最弱环节
- **服务Motivation**: Q5(Meaning) — 诚实讨论局限
- **证据**: Landauer:1961, LyndenBell:1967

## §IV. Dark Energy Equation of State
- **功能**: 连接qubit动力学→$w(z)$
- **服务Motivation**: Q3(Trust) — 可验证预言
- **证据**: 推导链

## §V. Comparison with DESI DR2
- **功能**: 数据比较
- **服务Motivation**: Q3(Trust) — 实验检验
- **证据**: Li:2025, Pang:2025 binned constraints

## §VI. Discussion
### §VI.A: Distinction from prior mechanisms
### §VI.B: $\mathcal{P}_{\rm coll}$ systematic uncertainties
### §VI.C: $\kappa$-$a_c^2$ degeneracy
### §VI.D: Analog quantum simulation
### §VI.E: Outlook (DESI DR3)
- **功能**: 综合讨论局限/未来/测试
- **服务Motivation**: Q5(Meaning) — 边界和未来

## §VII. Conclusion
- **功能**: 总结
- **服务Motivation**: Q1-Q5综合

## 检查: 每个声称+验证方式
| 声称 | 验证 |
|------|------|
| w(z) crossing at z~0.5-1 | DESI binned data comparison (§V) |
| $a_c^2$ from Curie-Weiss | Analytic derivation (§II.B + SM) |
| $\mathcal{P}_{\rm coll}$ drives qubits | Numerical computation decribed (§III.A + SM) |
| $\Delta\chi^2 \approx 5$ | Table I + method description (§V) |
| Analog QS feasible | Protocol in SM, not executed (honest) |
