# A博士 Round 1 推导

> 框架: Landau FL + Migdal-Eliashberg + Keldysh
> 日期: 2026-06-03

## 核心结论

η = T_D/T_tr 在已有文献中从未被系统研究过。ρ_sat vs γ 可用10-15个已知材料立即编译。

## 关键发现

1. η搜索: 0篇命中 — 完全无人涉足
2. ρ_sat vs γ搜索: 无直接图，A/γ²广泛研究但不同物理量
3. k_F l + Z + MIR: 0篇理论论文
4. CeCoIn₅估算: η(T→0)≈0.075, λ_MIR≈6-12在k_F l≈2-4时
5. ρ_sat/γ比例: 3D中(1+λ)抵消, 2D中不抵消

## 深挖

深挖1: η≈0.1-0.3→准粒子图像在k_F l→1时存活→坏金属超导体Tc窗口
深挖2: 各向同性e-boson假设→最弱环节，需带分辨验证

## INSPECTOR_CHECK标记

--- INSPECTOR_CHECK ---
[公式] η = T_D/T_tr = τ_tr/(2πτ_qp)
[方向] η≈0.1-0.3→重正化污染; η≪0.05→散射各向异性
[数据] CeCoIn₅: T_D=0.12K (Settai 2002), τ_tr=4.76×10⁻¹²s (from ℓ=1760Å and v_F*=3.7×10⁴m/s)
[假设] 各向同性e-boson耦合, τ_qp≈τ_tr在各向同性极限
--- INSPECTOR_CHECK ---

--- INSPECTOR_CHECK ---
[公式] λ_MIR = k_F l_tr / Z = k_F l_tr × (1+λ)
[方向] 强耦合λ≫1→λ_MIR≫1→准粒子完好
[数据] CeCoIn₅: λ≈1-3, k_F l_tr≈2-4 (at 300K)
[假设] FL框架成立, Luttinger定理保护k_F
--- INSPECTOR_CHECK ---

--- INSPECTOR_CHECK ---
[公式] ρ_sat/γ = (9π²ħ³)/(e²k_B²m_b k_F_bare²) (3D, (1+λ)抵消)
[方向] 此比值仅含裸带参数+基本常数，跨材料族普适
[数据] 待编译10-15种重费米子
[假设] 3D各向同性, 单带, e-boson耦合
--- INSPECTOR_CHECK ---

## 新增引用
[1] Settai 2002, [2] Shi 2023/PRB2025, [3] Gunnarsson RMP 2003, [4] Hall cond-mat/0102533, [5] Li 2023 Front.Electron.Mater., [6] Stewart RMP 1984, [7] Hussey JPSJ 2005, [8] Jacko Nat.Phys. 2009, [9] arXiv:2403.09283, [10] Moshopoulou cond-mat/0202211

## 脆弱环节
τ_qp和τ_tr在有限温度下成正比的假设（各向同性近似）
