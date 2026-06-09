"""
BLP trace-distance vs N_back comparison for the collision model.
Tests whether BLP measure increases monotonically with N_back during backflow.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 9, 'font.family': 'serif'})

def blp_vs_nback(N_S, N_E, q_S, q_E, k_max, n_trials=2000):
    """Compute BLP trace distance and N_back across collision steps."""
    N_back_avg = np.zeros(k_max + 1)
    D_avg = np.zeros(k_max + 1)  # trace distance

    for _ in range(n_trials):
        # Two initial states for BLP: |+> and |-> on S-qubit 0
        S1 = np.random.random(N_S) < q_S
        S2 = S1.copy()
        E = np.random.random(N_E) < q_E

        # Forward phase (same for both copies)
        for k in range(k_max):
            i = np.random.randint(0, N_S)
            j = np.random.randint(0, N_E)
            if not S1[i] and E[j]:
                E[j] = False

        # Backflow phase - track both copies
        S1_back, S2_back = S1.copy(), S2.copy()
        E1_back, E2_back = E.copy(), E.copy()
        backflow_count = 0

        for k in range(k_max):
            i = np.random.randint(0, N_S)
            j = np.random.randint(0, N_E)
            if not E1_back[j] and S1_back[i]:
                S1_back[i] = False
                backflow_count += 1
            if not E2_back[j] and S2_back[i]:
                S2_back[i] = False

            N_back_avg[k+1] += backflow_count

            # Trace distance: D = 1/2 * sum_i |p_i^{(1)} - p_i^{(2)}|
            # In pointer basis, each qubit is either |0> or |1>
            # D = 1/2 * sum_i |prob_diff| = fraction of qubits differing
            diff_count = np.sum(S1_back != S2_back)
            D_avg[k+1] += diff_count / N_S

    return N_back_avg / n_trials, D_avg / n_trials

N_S, N_E = 3, 3
k_max = 30
n_trials = 2000

configs = [
    (0.1, 0.9, '#1b9e77', r'$q_S=0.1, q_E=0.9$'),
    (0.2, 0.8, '#d95f02', r'$q_S=0.2, q_E=0.8$'),
]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 3.0))
ks = np.arange(k_max + 1)

for q_S, q_E, color, label in configs:
    N_back, D = blp_vs_nback(N_S, N_E, q_S, q_E, k_max, n_trials)

    # Left: D(t) and dD/dt > 0 regions
    dD = np.diff(D)
    ax1.plot(ks, D, color=color, lw=1.2, label=label)
    # Mark positive derivative regions (BLP non-Markovianity)
    pos_idx = np.where(dD > 0)[0]
    if len(pos_idx) > 0:
        ax1.scatter(ks[pos_idx+1], D[pos_idx+1], color=color, s=8, alpha=0.5,
                   marker='o', zorder=5)

    # Right: D vs N_back
    ax2.plot(N_back[1:], D[1:], color=color, lw=1.2, label=label)
    # Linear fit
    slope, intercept = np.polyfit(N_back[1:], D[1:], 1)
    print(f"q_S={q_S}, q_E={q_E}: D vs N_back slope = {slope:.4f}, correlation = {np.corrcoef(N_back[1:], D[1:])[0,1]:.4f}")
    print(f"  dD>0 fraction: {len(pos_idx)/len(dD):.1%}")

ax1.set_xlabel('Collision steps $k$')
ax1.set_ylabel('Trace distance $D$')
ax1.legend(loc='lower right', frameon=False, fontsize=7)
ax1.grid(True, alpha=0.2)
ax1.text(0.95, 0.05, '(a) BLP trace distance', transform=ax1.transAxes, ha='right', fontsize=8)

ax2.set_xlabel(r'$N_{\mathrm{back}}$')
ax2.set_ylabel('Trace distance $D$')
ax2.legend(loc='lower right', frameon=False, fontsize=7)
ax2.grid(True, alpha=0.2)
ax2.text(0.95, 0.05, '(b) D vs Nback', transform=ax2.transAxes, ha='right', fontsize=8)

fig.suptitle('BLP measure vs toggle-event backflow in collision model', fontsize=10, y=1.02)
plt.tight_layout()
plt.savefig('fig3_blp.pdf', dpi=300, bbox_inches='tight')
print("Figure 3 saved.")
