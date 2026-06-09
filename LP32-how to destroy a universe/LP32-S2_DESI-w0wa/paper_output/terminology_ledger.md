# 术语分类账 — LP32-S2 Information Dark Energy

> ⛔ 后续所有Agent只使用规范形式。术语一致性优先于词汇多样性。

## 核心物理学概念

| 规范形式 | 首次展开 | 来源变体 |
|---------|---------|---------|
| qubit (two-level system) | quantum two-level system, \|0⟩ undetermined, \|1⟩ determined | qubit, TLS, 二能级系统, quantum bit |
| determination amplitude $\mathcal{A}$ | complex order parameter of the qubit ensemble | $\mathcal{A}$, A, order parameter |
| determined fraction $|\mathcal{A}|^2$ | fraction of qubits in \|1⟩ state | determination fraction, $|\mathcal{A}|^2$, $\rho_{11}$ |
| critical fraction $a_c^2$ | threshold at which $\Delta E_{\rm eff}=0$ | $a_c^2$, critical determination, threshold |
| effective energy gap $\Delta E_{\rm eff}$ | $\Delta E_0 + 2g(1-2|\mathcal{A}|^2)$ | effective gap, renormalized gap |
| complex Langevin equation | $d\mathcal{A}/dt = -i\omega_0(1-|\mathcal{A}|^2/a_c^2)\mathcal{A} - \gamma\mathcal{A} + \eta f(t)$ | CLE, Langevin dynamics, complex dynamics |

## 宇宙学概念

| 规范形式 | 首次展开 | 来源变体 |
|---------|---------|---------|
| DESI DR2 | Dark Energy Spectroscopic Instrument Data Release 2 | DESI DR2, DESI Y1 |
| phantom crossing | $w(z)$ crossing $w=-1$ at some redshift | $w=-1$ crossing, phantom divide |
| CPL parametrization | Chevallier-Polarski-Linder: $w(a)=w_0+w_a(1-a)$ | CPL, $(w_0,w_a)$ |
| $\Lambda$CDM | Lambda Cold Dark Matter (standard cosmology) | LCDM, standard cosmology |
| BAO | Baryon Acoustic Oscillations | BAO |
| CMB | Cosmic Microwave Background | CMB |
| SN | Supernovae (Type Ia) | SN, SNe, SNIa |

## 结构形成

| 规范形式 | 首次展开 | 来源变体 |
|---------|---------|---------|
| gravitational collapse power $\mathcal{P}_{\rm coll}$ | rate of gravitational binding energy release from halo formation | $\mathcal{P}_{\rm coll}$, collapse power, binding energy rate |
| SFR | Star Formation Rate density | $\dot{\rho}_*$, SFRD, cosmic SFR |
| SMD | Stellar Mass Density | $\rho_*$, SMD, stellar mass |
| halo mass function | $dn/dM$, comoving number density of halos per mass bin | HMF, mass function |
| Sheth-Tormen | Sheth-Tormen (1999) multiplicity function | ST, Sheth-Tormen |
| Press-Schechter | Extended Press-Schechter formalism | PS, Press-Schechter |
| Eisenstein-Hu | Eisenstein-Hu (1998) transfer function for $P(k)$ | EH, Eisenstein-Hu |

## 量子多体理论

| 规范形式 | 首次展开 | 来源变体 |
|---------|---------|---------|
| mean-field Hamiltonian | $H_{\rm MF}^{(i)} = \frac{1}{2}\Delta E_{\rm eff}\sigma_z^{(i)}$ | MF, mean-field |
| Curie-Weiss theory | mean-field theory of all-to-all Ising model | Curie-Weiss, mean-field Ising |
| transverse Ising model | Ising model with transverse field | TIM, Ising model |
| Lindblad master equation | $\dot{\rho} = -i[H,\rho] + \gamma(L\rho L^\dagger - \frac{1}{2}\{L^\dagger L,\rho\})$ | Lindblad, master equation |
| ferromagnetic coupling $g$ | all-to-all Ising coupling strength | $g$, coupling, $J$ |

## 热力学/信息论

| 规范形式 | 首次展开 | 来源变体 |
|---------|---------|---------|
| Landauer's principle | erasing 1 bit dissipates $\ge k_B T \ln 2$ | Landauer, Landauer principle, Landauer bound |
| information processing rate $\dot{\mathcal{I}}$ | bits processed per unit time by structure formation | $\dot{\mathcal{I}}$, info rate |

## 暗能量类型

| 规范形式 | 首次展开 | 来源变体 |
|---------|---------|---------|
| quintessence | $w \ge -1$ scalar field dark energy | quintessence-like, $w>-1$ |
| phantom | $w \le -1$ dark energy | phantom-like, $w<-1$ |
| quintom | two-field model crossing $w=-1$ | quintom, hybrid |

## 检查冲突
- "DGF" vs "Discrete Graph Framework" → 使用 DGF（内部指代框架），但论文正文中不使用DGF缩写
- $a_c^2$ vs "critical fraction" vs "threshold" → 统一为 $a_c^2$ (critical fraction)
- $\mathcal{A}$ vs "amplitude" vs "order parameter" → 统一为 determination amplitude $\mathcal{A}$

## 锁定
⛔ 已锁定。后续所有Agent prompt注入本分类账作为硬约束。
