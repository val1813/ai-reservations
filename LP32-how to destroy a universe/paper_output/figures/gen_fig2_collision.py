"""
Collision model Monte Carlo simulation for the backflow bound.
Demonstrates N_back(k) vs bound for a 3+3 qubit all-to-all system.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 9, 'font.family': 'serif',
    'axes.labelsize': 10, 'legend.fontsize': 8,
})

def simulate_collision(N_S, N_E, q_S, q_E, k_max, n_trials=500):
    N_back_avg = np.zeros(k_max + 1)
    for _ in range(n_trials):
        S = np.random.random(N_S) < q_S
        E = np.random.random(N_E) < q_E
        # Forward phase
        for k in range(k_max):
            i = np.random.randint(0, N_S)
            j = np.random.randint(0, N_E)
            if not S[i] and E[j]:
                E[j] = False
        # Backflow phase
        S_back = S.copy()
        E_back = E.copy()
        backflow_count = 0
        for k in range(k_max):
            i = np.random.randint(0, N_S)
            j = np.random.randint(0, N_E)
            if not E_back[j] and S_back[i]:
                S_back[i] = False
                backflow_count += 1
            N_back_avg[k + 1] += backflow_count
    return N_back_avg / n_trials

N_S, N_E = 3, 3
k_max = 30
n_trials = 2000

configs = [
    (0.1, 0.9, '#1b9e77', r'$q_S=0.1, q_E=0.9$'),
    (0.2, 0.8, '#d95f02', r'$q_S=0.2, q_E=0.8$'),
    (0.3, 0.6, '#7570b3', r'$q_S=0.3, q_E=0.6$'),
    (0.5, 0.5, '#e7298a', r'$q_S=0.5, q_E=0.5$ (trivial)'),
]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 3.0))
ks = np.arange(k_max + 1)

for q_S, q_E, color, label in configs:
    N_back = simulate_collision(N_S, N_E, q_S, q_E, k_max, n_trials)
    bound = N_S * q_S
    C_F = N_E * q_E
    ax1.plot(ks, N_back, color=color, lw=1.2, label=label)
    ax1.axhline(bound, color=color, linestyle='--', lw=0.6, alpha=0.5)
    R = N_back / C_F
    R_bound = q_S / q_E
    ax2.plot(ks, R / R_bound, color=color, lw=1.2, label=label)
    R_final = N_back[-1] / C_F
    print(f"q_S={q_S}, q_E={q_E}: R_final={R_final:.4f}, bound={R_bound:.4f}, ratio={R_final/R_bound:.4f}")

ax1.set_xlabel('Collision steps $k$')
ax1.set_ylabel(r'$N_{\rm back}$')
ax1.legend(loc='lower right', frameon=False, fontsize=7)
ax1.set_xlim(0, k_max)
ax1.grid(True, alpha=0.2)
ax1.text(0.95, 0.05, '(a)', transform=ax1.transAxes, ha='right', fontsize=9)

ax2.axhline(1.0, color='k', linestyle='--', lw=0.8, alpha=0.5, label='bound saturation')
ax2.set_xlabel('Collision steps $k$')
ax2.set_ylabel(r'$\mathcal{R} / (q_S/q_E)$')
ax2.legend(loc='lower right', frameon=False, fontsize=7)
ax2.set_xlim(0, k_max)
ax2.set_ylim(0, 1.15)
ax2.grid(True, alpha=0.2)
ax2.text(0.95, 0.05, '(b)', transform=ax2.transAxes, ha='right', fontsize=9)

fig.suptitle('Collision model Monte Carlo: backflow vs combinatorial bound', fontsize=10, y=1.02)
plt.tight_layout()
plt.savefig('fig2_collision.pdf', dpi=300, bbox_inches='tight')
print("Figure 2 saved.")
