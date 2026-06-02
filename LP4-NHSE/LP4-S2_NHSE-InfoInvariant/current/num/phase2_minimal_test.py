import itertools
import math
from pathlib import Path

import numpy as np


def basis_states(L, N):
    return [sum(1 << i for i in occ) for occ in itertools.combinations(range(L), N)]


def fermion_sign(state, i, j):
    if i == j:
        return 1
    lo, hi = sorted((i, j))
    mask = sum(1 << k for k in range(lo + 1, hi))
    return -1 if (state & mask).bit_count() % 2 else 1


def hop(state, src, dst):
    if not (state & (1 << src)):
        return None
    if state & (1 << dst):
        return None
    new_state = state ^ (1 << src) ^ (1 << dst)
    return new_state, fermion_sign(state, src, dst)


def build_hamiltonian(L, N, tR, tL, U, boundary, freeze, cut):
    states = basis_states(L, N)
    index = {s: i for i, s in enumerate(states)}
    H = np.zeros((len(states), len(states)), dtype=complex)

    bonds = [(j, j + 1) for j in range(L - 1)]
    if boundary == "PBC":
        bonds.append((L - 1, 0))

    x_sites = set(range(cut))
    y_sites = set(range(cut, L))

    for col, state in enumerate(states):
        # Interaction
        for a, b in bonds:
            na = 1 if state & (1 << a) else 0
            nb = 1 if state & (1 << b) else 0
            cross = (a in x_sites and b in y_sites) or (a in y_sites and b in x_sites)
            if freeze == "hard" and cross:
                continue
            if freeze in {"dephase", "clamped"} and cross:
                # Mean-field boundary background. This is intentionally simple:
                # it tests whether the sign is stable under a noncoherent freeze.
                H[col, col] += U * na * 0.5 if b in y_sites else U * nb * 0.5
            else:
                H[col, col] += U * na * nb

        # Hopping. Convention: tR moves j -> j+1, tL moves j+1 -> j.
        for a, b in bonds:
            cross = (a in x_sites and b in y_sites) or (a in y_sites and b in x_sites)
            if freeze == "hard" and cross:
                continue
            coherent_factor = 1.0
            if freeze == "dephase" and cross:
                coherent_factor = 0.0
            if freeze == "clamped" and cross:
                coherent_factor = 0.5

            if coherent_factor:
                moved = hop(state, a, b)
                if moved:
                    new_state, sign = moved
                    if new_state in index:
                        H[index[new_state], col] += -tR * coherent_factor * sign
                moved = hop(state, b, a)
                if moved:
                    new_state, sign = moved
                    if new_state in index:
                        H[index[new_state], col] += -tL * coherent_factor * sign

    return H, states


def initial_state(states, L, side):
    weights = np.zeros(len(states), dtype=float)
    half = L // 2
    for i, state in enumerate(states):
        left_count = sum(1 for j in range(half) if state & (1 << j))
        right_count = state.bit_count() - left_count
        weights[i] = left_count if side == "left" else right_count
    if weights.sum() == 0:
        weights[:] = 1.0
    psi = weights.astype(complex)
    psi /= np.linalg.norm(psi)
    return psi


def center_of_mass(prob, states, L):
    cm = 0.0
    particles = 0.0
    for p, state in zip(prob, states):
        for j in range(L):
            if state & (1 << j):
                cm += p * j
                particles += p
    return cm / particles if particles else 0.0


def velocity(H, states, L, psi, dt=1e-3):
    # First-order evolution is enough for a diagnostic table.
    psi2 = psi - 1j * dt * (H @ psi)
    nrm = np.linalg.norm(psi2)
    if nrm:
        psi2 /= nrm
    p0 = np.abs(psi) ** 2
    p1 = np.abs(psi2) ** 2
    return (center_of_mass(p1, states, L) - center_of_mass(p0, states, L)) / dt


def run():
    rows = []
    for L in [4, 6, 8, 10]:
        for N in range(1, L):
            if math.comb(L, N) > 260:
                continue
            for boundary in ["OBC", "PBC"]:
                for freeze in ["hard", "dephase", "clamped"]:
                    H, states = build_hamiltonian(
                        L=L,
                        N=N,
                        tR=1.4,
                        tL=0.7,
                        U=0.6,
                        boundary=boundary,
                        freeze=freeze,
                        cut=L // 2,
                    )
                    v_lr = velocity(H, states, L, initial_state(states, L, "left"))
                    v_rl = -velocity(H, states, L, initial_state(states, L, "right"))
                    delta = v_lr - v_rl
                    sign = 1 if delta > 1e-8 else -1 if delta < -1e-8 else 0
                    rows.append((L, N, N / L, boundary, freeze, v_lr, v_rl, delta, sign))

    out = Path(__file__).with_name("phase2_minimal_results.csv")
    with out.open("w", encoding="utf-8") as f:
        f.write("L,N,rho,boundary,freeze,T_LR,T_RL,DeltaT,nu_Q\n")
        for row in rows:
            f.write(",".join(str(x) for x in row) + "\n")
    print(out)


if __name__ == "__main__":
    run()
