import numpy as np
import matplotlib.pyplot as plt

# Set up style
plt.rcParams.update({
    'font.size': 9,
    'font.family': 'serif',
    'axes.labelsize': 10,
    'legend.fontsize': 8,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'text.usetex': False,
})

fig, ax = plt.subplots(figsize=(3.4, 2.8))

# Parameter scan
q_E = np.linspace(0.05, 1.0, 200)
q_S_values = [0.1, 0.2, 0.3, 0.5, 0.7]
colors = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e']

for q_S, color in zip(q_S_values, colors):
    bound = q_S / q_E
    bound = np.clip(bound, 0, 3.0)  # clip for display
    ax.plot(q_E, bound, color=color, lw=1.2, label=rf'$q_S={q_S}$')

# Trivial boundary
ax.axhline(1.0, color='k', linestyle='--', lw=0.8, alpha=0.6, label='trivial boundary')

# Shade non-trivial region (q_S < q_E, i.e. bound < 1)
ax.fill_between(q_E, 0, 1.0, alpha=0.06, color='gray')
ax.text(0.55, 0.43, r'non-trivial ($\mathcal{R}<1$)', fontsize=7,
        color='gray', ha='center', style='italic')

# Also shade q_S > q_E region
ax.fill_between(q_E, 1.0, 3.0, alpha=0.03, color='red')
ax.text(0.3, 1.8, r'trivial ($\mathcal{R}>1$)', fontsize=7,
        color='lightcoral', ha='center', style='italic')

ax.set_xlabel(r'$q_E$')
ax.set_ylabel(r'$\mathcal{R}$ bound $= q_S/q_E$')
ax.set_xlim(0.05, 1.0)
ax.set_ylim(0, 2.5)
ax.legend(loc='upper right', frameon=False, ncol=1, handlelength=1.5)
ax.grid(True, alpha=0.2)

plt.tight_layout(pad=0.3)
plt.savefig('fig1_bound.pdf', dpi=300, bbox_inches='tight')
print("Figure saved to fig1_bound.pdf")
