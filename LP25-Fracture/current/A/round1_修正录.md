# Round1 修正录

## 修正1：t→∞ 极限
- 原文：ρ_atom → diag(|α|², |β|²)
- 修正：ρ_atom → diag(1, 0)
- 验算：rho_ee(1000)=1.12×10⁻⁴⁴, rho_gg(1000)=1.0 ✅

## 修正2：Ĵ 定义补充
- Ĵ_mat ≡ S(ρ_total(t)) - S(ρ_total(0))（数学Ĵ，由幺正性=0）
- Ĵ_op ≡ I_recoverable - I_initial（操作Ĵ，依赖于观测者因果可达域）
- S1 验证 Ĵ_mat=0。S2 验证 Ĵ_op 在视界处≠0的条件。
