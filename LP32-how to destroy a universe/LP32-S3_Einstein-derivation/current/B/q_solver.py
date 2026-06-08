"""
B博士 R3: 独立数值验证 q(r) 非线性解
耦合 q-Einstein ODE 系统 — 球对称静态真空
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar
import json

# ========== 物理常数 (几何化单位 G=c=1) ==========
M_P = 1.0          # Planck质量 (归一化)
kappa = 1.0 / M_P**2  # κ = 1/M_P²
V0 = 1e-122        # V₀ ~ H₀² ~ 10⁻¹²² M_P⁴ (宇宙学常数标度)
xi_0 = 1e-2        # 非最小耦合参数 (小值以验证弱耦合极限)

# ========== DGF 参数 ==========
M_BH = 1.0         # 黑洞质量 (几何化单位, 可缩放到任何M)
r_s = 2.0 * M_BH   # Schwarzschild半径

# ========== ODE 系统 ==========
# 变量: y = [m(r), Phi(r), q(r), q'(r)]
# 其中 m(r) = 质量函数, Phi(r) = 度规势, q(r) = q场

def dq_dr_asymptotic(r):
    """大r处q'的解析近似: q≈1-GM/rc² → q'≈GM/r²c²"""
    return M_BH / r**2  # 在几何化单位中

def coupled_odes(r, y):
    """
    耦合 q-Einstein 方程
    y[0] = m(r)  质量函数
    y[1] = Phi(r) 度规势
    y[2] = q(r)   q场
    y[3] = q'(r)  q场导数
    """
    m, Phi, q, qp = y

    # 防止奇点
    if r < 1e-6:
        r = 1e-6
    if q < 1e-10:
        q = 1e-10
    if q > 1.0:
        q = 1.0

    B_inv = 1.0 - 2.0 * m / r  # 1/B(r) = g^{rr}
    if B_inv < 1e-10:
        B_inv = 1e-10

    # q场能量密度
    eps_q = 0.5 / (kappa * q**2) * B_inv * qp**2

    # m' 方程: m' = 4πG r² ε_q
    dm_dr = 4.0 * np.pi * r**2 * eps_q

    # Phi' 方程: (rr) Einstein → 2(1-2m/r)Phi'/r - 2m/r³ = 8πG ε_q
    dPhi_dr = (4.0 * np.pi * r * eps_q + m / r**2) / B_inv

    # q场方程: □_g q - (∇q)²/q + κ q² V'(q) + ξκ q² R = 0
    # □_g q = e^{-Φ} √(B^{-1}) / r² · ∂_r(r² e^Φ √(B^{-1}) q')
    #
    # 简化: 在缓慢变化的度规中, □q ≈ B_inv q'' + (2/r + Phi' + B_inv'/(2B_inv)) B_inv q'
    # 其中 B_inv' = ∂_r(1-2m/r) = 2m/r² - 2m'/r

    B_inv_prime = 2.0 * m / r**2 - 2.0 * dm_dr / r

    # 有效扩散系数
    coeff_qpp = B_inv
    coeff_qp = B_inv * (2.0/r + dPhi_dr) + 0.5 * B_inv_prime

    # (∇q)² = B_inv (q')²
    grad_q_sq = B_inv * qp**2

    # 曲率标量 R (从Einstein方程回代)
    # R = -8πG T^μ_μ, T^μ_μ = Π^μ_μ = -2ε_q
    R_scalar = 16.0 * np.pi * eps_q

    # V'(q) = V₀ ln q
    V_prime = V0 * np.log(q) if q > 0 else -1e10

    # q'' 方程
    # coeff_qpp * q'' + coeff_qp * q' - grad_q_sq/q + κ q² V'(q) + ξκ q² R = 0
    if abs(coeff_qpp) < 1e-15:
        dqp_dr = 0.0
    else:
        dqp_dr = -(coeff_qp * qp - grad_q_sq/q + kappa * q**2 * V_prime + xi_0 * kappa * q**2 * R_scalar) / coeff_qpp

    return [dm_dr, dPhi_dr, qp, dqp_dr]

def asymptotic_solution(r):
    """大r处的渐近解 (r ≫ r_s)"""
    # q ≈ 1 - GM/rc²
    q_asym = np.exp(-M_BH / r)  # 精确的牛顿极限解
    qp_asym = M_BH / r**2 * q_asym

    # 度规 ≈ Schwarzschild
    m_asym = M_BH
    Phi_asym = 0.5 * np.log(1.0 - 2.0 * M_BH / r)

    return [m_asym, Phi_asym, q_asym, qp_asym]

def solve_q_field(r_span=(100.0, 2.01), n_points=1000, tol=1e-8):
    """
    从大r向内积分求解q(r)
    返回 r, m(r), Phi(r), q(r), q'(r) 数组
    """
    r_start = r_span[0]
    r_end = r_span[1]

    y0 = asymptotic_solution(r_start)

    # 确保 r_eval 在积分区间内
    r_eval = np.logspace(np.log10(r_end), np.log10(r_start), n_points)
    # 反转使得从大到小
    r_eval = r_eval[::-1]
    # 确保端点精确匹配
    r_eval = np.clip(r_eval, r_end, r_start)

    sol = solve_ivp(
        coupled_odes,
        [r_start, r_end],
        y0,
        t_eval=r_eval,
        method='RK45',
        rtol=tol,
        atol=tol,
        max_step=(r_start - r_end) / 100.0
    )

    return sol.t, sol.y[0], sol.y[1], sol.y[2], sol.y[3]

def compute_observables(r, m, Phi, q, qp):
    """计算关键可观测量"""
    results = []

    for i in range(len(r)):
        ri = r[i]
        mi = m[i]
        qi = q[i]
        qpi = qp[i]

        B_inv = 1.0 - 2.0 * mi / ri
        if B_inv < 0:
            B_inv = 0

        # 信息渗透压能量密度
        eps_q = 0.5 / (kappa * qi**2) * B_inv * qpi**2

        # 有效引力常数 G_eff/G = 1 / (1 + 16πG ξ(q))
        # 对于简单估计: ξ(q) = ξ₀ (1-q)²
        xi_q = xi_0 * (1.0 - qi)**2
        G_eff_ratio = 1.0 / (1.0 + 16.0 * np.pi * xi_q)

        # q场与牛顿极限的偏差
        q_newton = np.exp(-M_BH / ri)
        q_deviation = (qi - q_newton) / q_newton * 100  # 百分比

        # 信息应力与"预期"物质密度的比值
        # 使用吸积流密度估计: ρ_acc ~ Ṁ/(4πr²v_r)
        # 保守取 ρ_acc(r_s) ~ 1e-19 g/cm³ ~ 1e-42 M_P⁴
        rho_acc_rs = 1e-42  # M_P⁴ 单位
        rho_acc = rho_acc_rs * (r_s / ri)**2
        stress_ratio = eps_q / rho_acc if rho_acc > 0 else np.inf

        results.append({
            'r': ri,
            'r_rs': ri / r_s,
            'm': mi,
            'q': qi,
            '1-q': 1.0 - qi,
            'eps_q': eps_q,
            'G_eff_G': G_eff_ratio,
            'q_deviation_pct': q_deviation,
            'stress_ratio': stress_ratio,
            'B_inv': B_inv
        })

    return results

def find_firewall_radius(results, threshold=1.0):
    """找到信息火墙半径 r_I 满足 Π_00 = ρ_acc"""
    for res in results:
        if res['stress_ratio'] >= threshold:
            return res['r_rs'], res['r']
    return None, None

# ========== 主计算 ==========
if __name__ == '__main__':
    print("=" * 70)
    print("B博士 R3: q(r) 非线性解 — 耦合 q-Einstein 数值积分")
    print("=" * 70)
    print(f"\n参数: M = {M_BH} M_P (归一化), r_s = {r_s}")
    print(f"κ = {kappa}, V₀ = {V0:.1e}, ξ₀ = {xi_0}")

    # 从大r向内积分
    r_start = 100.0 * r_s  # 从100 r_s开始
    r_end = 1.5 * r_s       # 积到1.5 r_s (光子球附近)

    print(f"\n积分范围: r ∈ [{r_end/r_s:.1f}, {r_start/r_s:.1f}] r_s")
    print("正在积分...")

    r, m, Phi, q, qp = solve_q_field(
        r_span=(r_start, r_end),
        n_points=500,
        tol=1e-10
    )

    print(f"积分完成: {len(r)} 个点")

    # 计算可观测量
    results = compute_observables(r, m, Phi, q, qp)

    # 打印关键半径处的数值
    print("\n" + "=" * 70)
    print("关键半径处的数值结果")
    print("=" * 70)
    print(f"{'r/r_s':>8s}  {'q':>12s}  {'1-q':>12s}  {'ε_q [M_P⁴]':>14s}  {'G_eff/G':>10s}  {'Δq/q_N [%]':>12s}")
    print("-" * 70)

    key_radii = [1.5, 2.0, 3.0, 4.0, 6.0, 10.0, 20.0, 30.0, 50.0, 100.0]

    output_data = []
    for r_target in key_radii:
        idx = np.argmin(np.abs(r/r_s - r_target))
        res = results[idx]
        print(f"{res['r_rs']:8.2f}  {res['q']:12.6f}  {res['1-q']:12.6e}  "
              f"{res['eps_q']:14.6e}  {res['G_eff_G']:10.6f}  {res['q_deviation_pct']:12.4f}")
        output_data.append(res)

    # 找信息火墙半径
    r_I_rs, r_I = find_firewall_radius(results, threshold=0.01)
    if r_I_rs:
        print(f"\n信息火墙半径 (Π_00 = 0.01 ρ_acc): r_I ≈ {r_I_rs:.2f} r_s")
    else:
        print(f"\n信息火墙半径: 在积分范围内未达到阈值")

    # 找G_eff偏离1%的半径
    for res in results:
        if abs(res['G_eff_G'] - 1.0) > 0.01:
            print(f"G_eff偏离1%的半径: r ≈ {res['r_rs']:.2f} r_s (G_eff/G = {res['G_eff_G']:.6f})")
            break

    # 保存结果到JSON
    with open('D:/Claude/ai-reservations/LP32-how to destroy a universe/LP32-S3_Einstein-derivation/current/B/numerical_results.json', 'w') as f:
        json.dump(output_data, f, indent=2)

    print("\n结果已保存到 numerical_results.json")

    # 比较q(r)与牛顿极限q_N(r) = e^{-GM/rc²}
    print("\n" + "=" * 70)
    print("q(r) 与牛顿极限的对比")
    print("=" * 70)
    print(f"{'r/r_s':>8s}  {'q_DGF':>12s}  {'q_Newton':>12s}  {'偏差[%]':>10s}")
    print("-" * 70)
    for res in output_data:
        q_N = np.exp(-M_BH / res['r'])
        print(f"{res['r_rs']:8.2f}  {res['q']:12.6f}  {q_N:12.6f}  {res['q_deviation_pct']:10.4f}")

    # 渐进分析: q(r)的函数形式
    print("\n" + "=" * 70)
    print("渐进分析: ln(1-q) vs ln(r/r_s)")
    print("=" * 70)
    for res in output_data:
        if res['1-q'] > 1e-15:
            ln_1mq = np.log(res['1-q'])
            ln_r = np.log(res['r_rs'])
            print(f"r/r_s={res['r_rs']:6.1f}: ln(1-q)={ln_1mq:10.4f}, ln(r/r_s)={ln_r:8.4f}, 斜率≈{ln_1mq/ln_r:8.4f}")

    print("\n完成。")
