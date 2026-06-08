"""
Bayesian Reflux Diagnostic
给定测量数据, 计算理论满足容量约束的概率
"""

import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

np.random.seed(42)

def sample_under_H0(N_S, N_E, q_S, q_E, n_mc=10000):
    """H0下的P_reflux分布: 超几何不放回抽样"""
    n_E0 = max(1, int(N_E * q_E))
    n_S1 = int(N_S * (1 - q_S))

    results = []
    for _ in range(n_mc):
        # 前向转移: 从E的|0>中不放回抽取
        F_max = min(n_E0, n_S1)
        if F_max == 0:
            results.append(0.0)
            continue
        F = np.random.hypergeometric(n_S1, N_S - n_S1, F_max)

        # 回流: 最多min(S中|0>, F)次
        n_S0 = int(N_S * q_S)
        E_determined = F  # F次前向转移产生了F个E|1>
        R_max = min(n_S0, E_determined)
        R = np.random.hypergeometric(E_determined, N_E - E_determined, R_max) if R_max > 0 else 0

        C_F = n_E0
        results.append(R / C_F if C_F > 0 else 0)

    return np.array(results)


def diagnostic(N_S, N_E, q_S_est, q_E_est, P_reflux_obs,
               q_S_err=0.0, q_E_err=0.0, n_mc=10000):
    """
    回流贝叶斯诊断

    Parameters:
        N_S, N_E: 系统和环境格点数
        q_S_est, q_E_est: q_S, q_E的点估计
        P_reflux_obs: 观测到的P_reflux
        q_S_err, q_E_err: 如有测量误差, 给出1-sigma (默认0)
        n_mc: MC采样数

    Returns:
        dict with: p_value, bayes_factor, ci_95, h0_distribution, verdict
    """
    # 纳入测量误差: 从Beta分布抽样q_S, q_E
    if q_S_err > 0:
        a_S = q_S_est * (q_S_est*(1-q_S_est)/q_S_err**2 - 1) if q_S_err**2 < q_S_est*(1-q_S_est) else 1
        b_S = (1-q_S_est) * (q_S_est*(1-q_S_est)/q_S_err**2 - 1) if q_S_err**2 < q_S_est*(1-q_S_est) else 1
        q_S_samples = np.random.beta(max(0.1, a_S), max(0.1, b_S), n_mc)
    else:
        q_S_samples = np.full(n_mc, q_S_est)

    if q_E_err > 0:
        a_E = q_E_est * (q_E_est*(1-q_E_est)/q_E_err**2 - 1) if q_E_err**2 < q_E_est*(1-q_E_est) else 1
        b_E = (1-q_E_est) * (q_E_est*(1-q_E_est)/q_E_err**2 - 1) if q_E_err**2 < q_E_est*(1-q_E_est) else 1
        q_E_samples = np.random.beta(max(0.1, a_E), max(0.1, b_E), n_mc)
    else:
        q_E_samples = np.full(n_mc, q_E_est)

    # H0分布
    h0_dist = np.zeros(n_mc)
    for i in range(n_mc):
        dist = sample_under_H0(N_S, N_E, q_S_samples[i], q_E_samples[i], n_mc=1)
        h0_dist[i] = dist[0]

    # p值: P(P_reflux ≥ obs | H0) — 单侧检验
    p_value = np.mean(h0_dist >= P_reflux_obs)

    # 95% CI
    ci_95 = np.percentile(h0_dist, [2.5, 97.5])

    # Bayes Factor: P(data|H0) / P(data|H1)
    # H1: uniform on [0, 1]
    # 离散化: 计算H0分布在P_obs附近的概率质量 vs H1均匀分布
    window = 0.05  # 5%窗口
    mass_h0 = np.mean((h0_dist >= P_reflux_obs - window/2) &
                      (h0_dist <= P_reflux_obs + window/2))
    mass_h1 = window  # uniform on [0,1]
    bf = mass_h0 / mass_h1 if mass_h1 > 0 else np.inf

    # 如果H0分布退化(方差接近0), BF基于均值距离
    if np.std(h0_dist) < 1e-6:
        dist_from_mean = abs(P_reflux_obs - np.mean(h0_dist))
        if dist_from_mean < 1e-6:
            bf = 10.0  # 精确匹配退化分布
        else:
            bf = 1.0 / (1.0 + dist_from_mean * 100)  # 距离越远BF越小

    # 裁决
    if bf > 3:
        verdict = "consistent (moderate)"
    elif bf > 1:
        verdict = "consistent (weak)"
    elif bf > 1/3:
        verdict = "inconclusive"
    elif bf > 1/10:
        verdict = "inconsistent (moderate)"
    else:
        verdict = "inconsistent (strong)"

    return {
        'p_value': p_value,
        'bayes_factor': bf,
        'ci_95': ci_95,
        'h0_distribution': h0_dist,
        'verdict': verdict,
        'h0_mean': np.mean(h0_dist),
        'h0_median': np.median(h0_dist)
    }


def run_examples():
    """测试案例"""
    examples = [
        # (N_S, N_E, q_S, q_E, P_obs, q_S_err, q_E_err, label)
        (10, 10, 0.30, 0.50, 0.25, 0.05, 0.05, "Typical, consistent"),
        (10, 10, 0.30, 0.50, 0.65, 0.05, 0.05, "Reflux too high"),
        (5, 5, 0.20, 0.20, 0.10, 0.0, 0.0, "Small system, no error"),
        (3, 50, 0.30, 0.90, 0.005, 0.03, 0.02, "Large environment"),
        (10, 10, 0.80, 0.50, 0.80, 0.0, 0.0, "High q_S — bound loose"),
    ]

    print("=" * 70)
    print("Bayesian Reflux Diagnostic — Test Cases")
    print("=" * 70)

    for N_S, N_E, q_S, q_E, P_obs, q_S_err, q_E_err, label in examples:
        r = diagnostic(N_S, N_E, q_S, q_E, P_obs, q_S_err, q_E_err, n_mc=5000)

        print(f"\n{'-'*50}")
        print(f"Case: {label}")
        print(f"N_S={N_S}, N_E={N_E}, q_S={q_S}±{q_S_err}, q_E={q_E}±{q_E_err}")
        print(f"P_reflux(obs)={P_obs}")
        print(f"  H0 mean={r['h0_mean']:.3f}, median={r['h0_median']:.3f}")
        print(f"  95% CI = [{r['ci_95'][0]:.3f}, {r['ci_95'][1]:.3f}]")
        print(f"  p-value = {r['p_value']:.4f}")
        print(f"  Bayes Factor = {r['bayes_factor']:.2f}")
        print(f"  Verdict: {r['verdict'].upper()}")
        if r['bayes_factor'] < 0.5:
            print(f"  WARN: Possible causes: (a) carriers not bits (b) multiple toggles")
            print(f"     (c) measurement error underestimated (d) H0 wrong")

    # 图示
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()

    for idx, (N_S, N_E, q_S, q_E, P_obs, q_S_err, q_E_err, label) in enumerate(examples):
        r = diagnostic(N_S, N_E, q_S, q_E, P_obs, q_S_err, q_E_err, n_mc=5000)
        ax = axes[idx]
        ax.hist(r['h0_distribution'], bins=40, density=True, alpha=0.7, color='steelblue')
        ax.axvline(P_obs, color='red', lw=2, linestyle='--', label=f'Obs={P_obs:.3f}')
        ax.axvline(r['ci_95'][0], color='gray', lw=1, linestyle=':')
        ax.axvline(r['ci_95'][1], color='gray', lw=1, linestyle=':')
        ax.set_title(f'{label}\nBF={r["bayes_factor"]:.1f} {r["verdict"]}', fontsize=10)
        ax.set_xlabel('P_reflux')
        ax.legend(fontsize=8)

    axes[-1].axis('off')
    plt.suptitle('Bayesian Reflux Diagnostic — H0 Distributions\n'
                 'Red line = observed P_reflux. Gray lines = 95% CI.',
                 fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig('D:/Claude/ai-reservations/LP34_Aporia-Mechanism/bayesian_diagnostic_examples.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\nPlot saved.")


def run_power_analysis():
    """检验力分析: 给定q_S, q_E, 需要多少样本才能区分H0 vs H1?"""
    N_S, N_E = 10, 10
    q_S, q_E = 0.3, 0.5
    n_mc_range = [100, 500, 1000, 5000, 10000]
    true_P_under_H0 = np.mean(sample_under_H0(N_S, N_E, q_S, q_E, n_mc=5000))

    print("\n" + "=" * 60)
    print("Power Analysis: MC samples vs CI width")
    for n in n_mc_range:
        dist = sample_under_H0(N_S, N_E, q_S, q_E, n_mc=n)
        ci = np.percentile(dist, [2.5, 97.5])
        print(f"  n_mc={n:5d}: 95% CI = [{ci[0]:.4f}, {ci[1]:.4f}], width={ci[1]-ci[0]:.4f}")


if __name__ == '__main__':
    run_examples()
    run_power_analysis()
    print("\nDone.")
