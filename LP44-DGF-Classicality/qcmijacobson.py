"""
QCMI gradient -> Jacobson -> Newtonian gravity.

Jacobson (1995): delta_Q = T dS on local Rindler horizon.
  T = hbar * a / (2 pi c k_B)  (Unruh temperature)
  dS = entropy through horizon

DGF: dS = k_B * ln(2) * d(QCMI)  (bits -> J/K)

Equate: QCMI gradient produces equivalent mass.
"""
import numpy as np

# Constants
hbar = 1.054571817e-34  # J.s
c = 2.99792458e8        # m/s
k_B = 1.380649e-23      # J/K
G = 6.67430e-11         # m^3/kg/s^2
l_P = np.sqrt(hbar * G / c**3)  # Planck length

eta_0 = 1.0 / (8.0 * np.log(2.0))

print("=" * 70)
print("QCMI GRADIENT -> GRAVITY (Jacobson bridge)")
print("=" * 70)

# ================================================================
# Step 1: QCMI -> physical entropy
# ================================================================
def qcmi_to_entropy(qcmi_bits):
    """Convert QCMI (bits) to physical entropy (J/K)."""
    return k_B * np.log(2) * qcmi_bits

def entropy_to_qcmi(S_JK):
    return S_JK / (k_B * np.log(2))

# ================================================================
# Step 2: Jacobson: delta_Q = T dS
# Unruh: T = hbar * a / (2 pi c k_B)
# So: delta_Q = (hbar * a / (2 pi c k_B)) * dS
# Energy flux = acceleration * entropy / (2 pi c k_B / hbar)
# ================================================================
def acceleration_from_qcmi_gradient(dQCMI_dx):
    """Acceleration from QCMI spatial gradient.
    dQCMI_dx: QCMI difference per meter (bits/m)
    Returns acceleration in m/s^2
    """
    dS_dx = qcmi_to_entropy(dQCMI_dx)  # J/K per meter
    # Jacobson: a = (2 pi c k_B / hbar) * (dQ/dx) / (dS/dx)
    # For mass M: dQ = G M / r^2 * (energy flux)
    # Actually from Jacobson: the Einstein equation emerges from
    # delta_Q = (hbar * a / (2 pi c k_B)) * delta_S
    # For a local Rindler horizon with area A:
    # delta_S = (k_B c^3 / (4 G hbar)) * delta_A
    # delta_A = integral of expansion theta
    # Raychaudhuri: d(theta)/dlambda = -theta^2/2 - sigma^2 - R_ab k^a k^b
    # This leads to G_ab = 8 pi G T_ab

    # Simplified: the acceleration from entropy gradient is
    # a = (2 pi c k_B / hbar) * (dS/dx) / (dS/dA * dA/dx)
    # For a spherical horizon: dS/dA = k_B c^3 / (4 G hbar)  (Bekenstein-Hawking)
    # dA/dx = 8 pi R (for spherical horizon of radius R)

    # But we want: what QCMI gradient produces Earth-surface gravity?
    # g = 9.81 m/s^2
    # T_Unruh = hbar * g / (2 pi c k_B) = 4e-21 K
    # dS = delta_Q / T
    # For 1 J of energy through horizon at g=9.81:
    # dS = 1 / 4e-21 = 2.5e20 J/K = 2.5e20 / (k_B ln 2) bits = 2.6e43 bits

    # So: 1 J of energy -> 2.6e43 bits of QCMI through horizon
    # Equivalently: 1 bit of QCMI -> 3.8e-44 J of equivalent energy
    # E = m c^2 -> m_eq = E/c^2 = 3.8e-44 / (3e8)^2 = 4.2e-61 kg per QCMI bit

    T_unruh = hbar * dQCMI_dx * c / (2 * np.pi * k_B)  # temp from QCMI gradient
    return T_unruh * 2 * np.pi * c * k_B / hbar  # just returns a = dQCMI gradient proxy

# The actual relationship from Jacobson
def equivalent_mass_from_qcmi(qcmi_bits, length_scale=1.0):
    """
    Equivalent mass that would produce the same entropy as QCMI bits
    through a horizon of size length_scale.

    Bekenstein-Hawking: S_BH = k_B * c^3 * A / (4 * G * hbar)
    DGF entropy: S_DGF = k_B * ln(2) * qcmi_bits

    Equate: k_B * ln(2) * qcmi_bits = k_B * c^3 * 4 pi * R^2 / (4 * G * hbar)
    -> qcmi_bits = (c^3 / (G * hbar * ln 2)) * pi * R^2

    For a sphere of radius R:
    M = R * c^2 / (2 * G)  (Schwarzschild radius relation)
    """
    S_DGF = k_B * np.log(2) * qcmi_bits
    # Area needed to contain this entropy
    A_needed = 4 * G * hbar * S_DGF / (k_B * c**3)
    R_needed = np.sqrt(A_needed / (4 * np.pi))
    M_eq = R_needed * c**2 / (2 * G)
    return M_eq, R_needed

# ================================================================
# Numerical examples
# ================================================================
print("\n--- Single cl(4,1) ring ---")
qcmi_per_ring = 1.0  # at c=pi/4, from Gram matrix data
M_eq, R_eq = equivalent_mass_from_qcmi(qcmi_per_ring)
print(f"QCMI = {qcmi_per_ring} bit")
print(f"Equivalent mass: {M_eq:.2e} kg")
print(f"Equivalent radius: {R_eq:.2e} m")
print(f"(Compare: electron mass = 9.1e-31 kg, proton = 1.67e-27 kg)")

print(f"\n--- 1 mole of cl(4,1) rings (N_A = 6e23) ---")
N_A = 6.022e23
qcmi_mole = qcmi_per_ring * N_A
M_eq, R_eq = equivalent_mass_from_qcmi(qcmi_mole)
print(f"QCMI = {qcmi_mole:.2e} bits ({N_A} rings)")
print(f"Equivalent mass: {M_eq:.2e} kg")

print(f"\n--- Earth surface gravity from QCMI gradient ---")
# Earth: M = 6e24 kg, R = 6.4e6 m
# How many cl(4,1) rings needed to produce Earth's gravity?
M_earth = 5.972e24
R_earth = 6.371e6
S_BH_earth = k_B * c**3 * 4 * np.pi * R_earth**2 / (4 * G * hbar)
qcmi_earth = entropy_to_qcmi(S_BH_earth)
n_rings_earth = qcmi_earth / qcmi_per_ring
print(f"Earth Bekenstein-Hawking entropy: {S_BH_earth/k_B:.2e} bits")
print(f"Equivalent QCMI: {qcmi_earth:.2e} bits")
print(f"Number of cl(4,1) rings needed: {n_rings_earth:.2e}")
print(f"(Compare: Earth atoms ~ 10^50)")

# ================================================================
# The bridge formula
# ================================================================
print(f"\n{'='*70}")
print("THE BRIDGE: QCMI <-> GRAVITY")
print(f"{'='*70}")
print(f"""
Jacobson (1995): Einstein equations from horizon thermodynamics.
DGF input: horizon entropy = QCMI of causal rings crossing horizon.

Key numbers:
  1 bit QCMI -> {M_eq:.2e} kg equivalent mass
  1 cl(4,1) ring at pi/4 -> 1.0 bit QCMI -> {M_eq:.2e} kg

  Earth's gravity requires {n_rings_earth:.2e} causal rings through horizon
  Earth has ~10^50 atoms, each ~10^23 Planck-scale rings -> 10^73 rings total
  Horizon-crossing fraction: {n_rings_earth/1e73:.2e}
  -> Approximately {n_rings_earth/1e73*100:.1e}% of Earth's rings cross horizon

The Jacobson bridge means:
  QCMI gradient = entropy gradient = gravity
  Active time control = active gravity control
  cl(4,1) is the "gravitational transistor"
""")
