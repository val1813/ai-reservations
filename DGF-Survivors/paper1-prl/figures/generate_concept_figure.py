"""
Nature-figure concept schematic: Causal Ring Topology
Shows why cycle topology forces quantum memory.
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "font.size": 7.5,
    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.linewidth": 0.8,
    "legend.frameon": False,
})

fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.6))

# ========================================
# Panel (a): Acyclic — open chain, Markovian
# ========================================
ax = axes[0]
ax.set_xlim(-0.3, 2.3)
ax.set_ylim(-0.3, 1.3)
ax.axis('off')
ax.set_title('(a) Open chain\n(standard theory)', fontsize=8, fontweight='bold', pad=8)

# System qubits (squares)
sq1 = plt.Rectangle((-0.15, 0.85), 0.3, 0.3, fc='#2c7bb6', ec='white', lw=0.5, zorder=3)
sq2 = plt.Rectangle((1.85, 0.85), 0.3, 0.3, fc='#2c7bb6', ec='white', lw=0.5, zorder=3)
ax.add_patch(sq1); ax.add_patch(sq2)
ax.text(0, 1.0, r'$Q_a$', ha='center', va='center', fontsize=9, fontweight='bold', color='white')
ax.text(2, 1.0, r'$Q_b$', ha='center', va='center', fontsize=9, fontweight='bold', color='white')

# Environment qubits (circles)
e1 = plt.Circle((0.65, 0.15), 0.18, fc='#d7191c', ec='white', lw=0.5, zorder=3)
e2 = plt.Circle((1.35, 0.15), 0.18, fc='#d7191c', ec='white', lw=0.5, zorder=3)
ax.add_patch(e1); ax.add_patch(e2)
ax.text(0.65, 0.15, r'$E_1$', ha='center', va='center', fontsize=8, fontweight='bold', color='white')
ax.text(1.35, 0.15, r'$E_2$', ha='center', va='center', fontsize=8, fontweight='bold', color='white')

# Edges: Qa->E1, E1->Qb (no cycle back to Qa)
ax.annotate('', xy=(1.35, 0.33), xytext=(0.65, 0.33),
            arrowprops=dict(arrowstyle='->', color='#333333', lw=1.2))
ax.annotate('', xy=(1.85, 0.7), xytext=(1.35, 0.33),
            arrowprops=dict(arrowstyle='->', color='#333333', lw=1.2))
ax.annotate('', xy=(0.65, 0.33), xytext=(0.15, 0.7),
            arrowprops=dict(arrowstyle='->', color='#333333', lw=1.2))

# Labels
ax.text(0.65, 0.5, r'$U_1$', ha='center', fontsize=6.5, color='#555555')
ax.text(1.6, 0.5, r'$U_2$', ha='center', fontsize=6.5, color='#555555')
ax.text(0.4, 0.5, r'$U_0$', ha='center', fontsize=6.5, color='#555555')

# Result annotation
ax.text(1.0, -0.22, 'No closed loop', ha='center', fontsize=7, color='#2c7bb6', fontweight='bold')
ax.text(1.0, -0.38, r'QCMI $\approx$ 0 (Markovian)', ha='center', fontsize=6.5, color='#888888')


# ========================================
# Panel (b): Cyclic — closed causal ring — non-Markovian
# ========================================
ax = axes[1]
ax.set_xlim(-0.3, 2.3)
ax.set_ylim(-0.3, 1.3)
ax.axis('off')
ax.set_title('(b) Closed causal ring\n(this work)', fontsize=8, fontweight='bold', pad=8)

# System qubits
sq1 = plt.Rectangle((-0.15, 0.85), 0.3, 0.3, fc='#2c7bb6', ec='white', lw=0.5, zorder=3)
sq2 = plt.Rectangle((1.85, 0.85), 0.3, 0.3, fc='#2c7bb6', ec='white', lw=0.5, zorder=3)
ax.add_patch(sq1); ax.add_patch(sq2)
ax.text(0, 1.0, r'$Q_a$', ha='center', va='center', fontsize=9, fontweight='bold', color='white')
ax.text(2, 1.0, r'$Q_b$', ha='center', va='center', fontsize=9, fontweight='bold', color='white')

# Environment qubits
e1 = plt.Circle((0.65, 0.15), 0.18, fc='#d7191c', ec='white', lw=0.5, zorder=3)
e2 = plt.Circle((1.35, 0.15), 0.18, fc='#d7191c', ec='white', lw=0.5, zorder=3)
ax.add_patch(e1); ax.add_patch(e2)
ax.text(0.65, 0.15, r'$E_1$', ha='center', va='center', fontsize=8, fontweight='bold', color='white')
ax.text(1.35, 0.15, r'$E_2$', ha='center', va='center', fontsize=8, fontweight='bold', color='white')

# Full cycle: Qa->E1->Qb->E2->Qa
# Edge Qa->E1
ax.annotate('', xy=(0.65, 0.33), xytext=(0.15, 0.7),
            arrowprops=dict(arrowstyle='->', color='#d7191c', lw=1.5))
# Edge E1->Qb
ax.annotate('', xy=(1.85, 0.7), xytext=(0.83, 0.15),
            arrowprops=dict(arrowstyle='->', color='#d7191c', lw=1.5, connectionstyle='arc3,rad=0.3'))
# Edge Qb->E2
ax.annotate('', xy=(1.35, 0.33), xytext=(2.0, 0.7),
            arrowprops=dict(arrowstyle='->', color='#d7191c', lw=1.5, connectionstyle='arc3,rad=-0.3'))
# Edge E2->Qa (closes the cycle!)
ax.annotate('', xy=(0.0, 0.85), xytext=(1.17, 0.15),
            arrowprops=dict(arrowstyle='->', color='#d7191c', lw=1.5, connectionstyle='arc3,rad=-0.3'))

# Cycle highlight ring
cycle = plt.Circle((1.0, 0.5), 0.55, fc='none', ec='#d7191c', lw=1.5, ls='--', alpha=0.4, zorder=1)
ax.add_patch(cycle)

# Result annotation
ax.text(1.0, -0.22, 'Closed causal cycle', ha='center', fontsize=7, color='#d7191c', fontweight='bold')
ax.text(1.0, -0.38, r'QCMI $>$ 0 iff $c_j\notin(\pi/2)\mathbb{Z}$', ha='center', fontsize=6.5, color='#888888')

# ========================================
# Panel (c): Gate algebra — Pauli subgroup closes without memory
# ========================================
ax = axes[2]
theta = np.linspace(0, np.pi, 200)
qcmi = np.array([0.0]*200)
# Simplified QCMI curve
for i, t in enumerate(theta):
    if abs(t - np.pi/2) < 0.01 or abs(t - 0) < 0.01 or abs(t - np.pi) < 0.01:
        qcmi[i] = 0.0
    else:
        qcmi[i] = np.sin(2*t)**2 * 1.5

ax.plot(theta, qcmi, 'k-', lw=1.0)
# Mark zero points (Pauli subgroup)
for c_val in [0, np.pi/2, np.pi]:
    ax.scatter([c_val], [0], c='#2c7bb6', s=40, zorder=5, edgecolors='white', lw=0.5)
    ax.axvline(c_val, color='#2c7bb6', lw=0.3, alpha=0.3, ls='--')
# Mark non-zero region
ax.axvspan(np.pi/4, 3*np.pi/8, alpha=0.08, color='#d7191c')
ax.annotate(r'QCMI $>0$', xy=(np.pi/3, 1.3), fontsize=7, ha='center', color='#d7191c')

ax.set_xlabel(r'Cartan angle $c_j$')
ax.set_ylabel('QCMI (bits)')
ax.set_xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
ax.set_xticklabels(['0', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$'])
ax.set_ylim(-0.1, 1.7)
ax.set_title('(c) Gate algebra constraint', fontsize=8, fontweight='bold', pad=8)

# Annotate Pauli points
ax.annotate(r'$I\otimes I$', xy=(0, 0), xytext=(0.15, 0.3), fontsize=6.5,
            arrowprops=dict(arrowstyle='->', lw=0.5, color='#555555'), color='#2c7bb6')
ax.annotate(r'$\sigma\otimes\sigma$', xy=(np.pi/2, 0), xytext=(np.pi/2+0.2, 0.3), fontsize=6.5,
            arrowprops=dict(arrowstyle='->', lw=0.5, color='#555555'), color='#2c7bb6')

plt.tight_layout(pad=0.8)
for ext in ['svg', 'pdf', 'tiff']:
    fp = f'D:/Claude/ai-reservations/DGF-Survivors/paper1-prl/figures/fig0_concept.{ext}'
    if ext == 'tiff':
        plt.savefig(fp, dpi=600, bbox_inches='tight')
    else:
        plt.savefig(fp, bbox_inches='tight')
print("Concept figure saved: fig0_concept.{svg,pdf,tiff}")
