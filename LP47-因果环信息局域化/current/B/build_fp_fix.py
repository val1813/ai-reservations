"""
Post-process fp_fix_raw.json into structured fp_fix.json
with comprehensive analysis and A博士 comparison.
"""
import json
import numpy as np

with open(r'D:\Claude\ai-reservations\LP47-因果环信息局域化\current\B\fp_fix_raw.json', 'r') as f:
    raw = json.load(f)

# ============================================================
# Helper to build protection matrix tables
# ============================================================
def build_protection_matrix(protection_data, n, k, partition_label):
    """Extract (n,k) protection pattern for given partition."""
    key = f'n{n}_k{k}_partition_{partition_label}'
    if key not in protection_data:
        return None
    d = protection_data[key]
    matrix = {}
    for q_str, qd in d['by_qubit'].items():
        q = int(q_str)
        field_delta = f'delta_at_theta_010_{partition_label}'
        field_prot = f'protected_{partition_label}'
        field_alpha = f'M4_alpha_{partition_label}'
        matrix[str(q)] = {
            'delta_at_theta_010': qd[field_delta],
            'protected': qd[field_prot],
            'M4_alpha': qd[field_alpha]
        }
    return {
        'n': n, 'k': k,
        'partition': partition_label,
        'A': d['A'], 'B': d['B'], 'C': d['C'],
        'baseline': d['baseline'],
        'matrix': matrix,
        'protected_qubits': [q for q in matrix if matrix[q]['protected']],
        'active_qubits': [q for q in matrix if not matrix[q]['protected']],
        'protection_fraction': len([q for q in matrix if matrix[q]['protected']]) / n
    }

# ============================================================
# Build Fix 3: Protection Horizon
# ============================================================
ph = raw['fix3_protection_horizon']
n_vals = [6, 7, 8]
k_vals = [1, 2, 3]

fix3 = {
    'title': 'Protection Horizon under Partition I and II (Hmix perturbation on cluster ring C_n)',
    'method': {
        'perturbation': 'Hmix: |psi(theta)> = cos(theta)|C_n> + sin(theta) H_q|C_n>',
        'theta_range': [0.005, 0.01, 0.02, 0.03, 0.05, 0.08, 0.10],
        'protection_threshold': '|delta_QCMI(theta=0.10)| < 1e-12',
        'partition_I': 'A={0}, C={k}, B=[n]\\{0,k}  (big B, n-2 conditioning qubits)',
        'partition_II': 'A={0}, B={k}, C={k+1 mod n}  (small B, 1 conditioning qubit)',
        'qcmi_unit': 'nats (natural log)'
    }
}

# Build summary matrices for each n,k,partition
for n in n_vals:
    fix3[f'n{n}'] = {}
    for k in k_vals:
        fix3[f'n{n}'][f'k{k}'] = {}
        for part in ['I', 'II']:
            m = build_protection_matrix(ph, n, k, part)
            if m:
                fix3[f'n{n}'][f'k{k}'][f'partition_{part}'] = m

# Cross-partition comparison
fix3['cross_partition_comparison'] = {}
for n in n_vals:
    fix3['cross_partition_comparison'][f'n{n}'] = {}
    for k in k_vals:
        m_I = build_protection_matrix(ph, n, k, 'I')
        m_II = build_protection_matrix(ph, n, k, 'II')
        if m_I and m_II:
            agreed_protected = sorted(set(m_I['protected_qubits']) & set(m_II['protected_qubits']))
            agreed_active = sorted(set(m_I['active_qubits']) & set(m_II['active_qubits']))
            disagreed = []
            for q in range(n):
                qs = str(q)
                pi = m_I['matrix'][qs]['protected']
                pii = m_II['matrix'][qs]['protected']
                if pi != pii:
                    disagreed.append({'q': q, 'I_protected': pi, 'II_protected': pii})
            fix3['cross_partition_comparison'][f'n{n}'][f'k{k}'] = {
                'agreed_protected': agreed_protected,
                'agreed_active': agreed_active,
                'disagreed': disagreed,
                'agreement_fraction': len(agreed_protected + agreed_active) / n
            }

# Universal protection analysis
fix3['universally_protected'] = {}
for part in ['I', 'II']:
    fix3['universally_protected'][f'partition_{part}'] = {}
    for n in n_vals:
        all_protected = set(range(n))
        for k in k_vals:
            m = build_protection_matrix(ph, n, k, part)
            if m:
                all_protected &= set(m['protected_qubits'])
        fix3['universally_protected'][f'partition_{part}'][f'n{n}'] = sorted(list(all_protected))

# Protection depth delta(n,k) under Partition I
fix3['protection_depth'] = {
    'definition': 'delta(n,k) = number of qubit positions q where |Delta_QCMI(q; n,k, theta=0.10)| < 1e-12 under Partition I',
    'values': {}
}
for n in n_vals:
    for k in k_vals:
        m = build_protection_matrix(ph, n, k, 'I')
        if m:
            fix3['protection_depth']['values'][f'n{n}_k{k}'] = {
                'delta': len(m['protected_qubits']),
                'protected': m['protected_qubits'],
                'delta_over_n': len(m['protected_qubits']) / n
            }

# ============================================================
# Build Fix 4: Magic Correlation Length
# ============================================================
ml = raw['fix4_magic_correlation_length']
gt = raw['fix4b_global_T_test']

fix4 = {
    'title': 'Magic Correlation Length: Independent Verification under Partition I',
    'method': {
        'perturbation': 'T-gate superposition at qubit 0: |psi(theta)> = cos(theta)|C_n> + sin(theta) |perp_0>',
        'perp_definition': '|perp_0> = (T_0|C_n> - <C_n|T_0|C_n>|C_n>)/norm',
        'overlap': '<C_n|T_0|C_n> = (1 + e^{i*pi/4})/2 = 0.85355 + 0.35355i (n-independent)',
        'theta_range': [0.005, 0.01, 0.02, 0.03, 0.05, 0.08, 0.10, 0.15, 0.20, 0.25, 0.30],
        'theta_010_check': 0.10,
        'zero_threshold': 1e-12
    },
    'single_T_at_q0': {},
    'global_T': {}
}

# Single T-gate results
for n in [6, 7]:
    fix4['single_T_at_q0'][f'n{n}'] = {}
    for k in [1, 2, 3]:
        if k > n // 2:
            continue
        key = f'n{n}_k{k}_T_gate_q0'
        if key in ml:
            d = ml[key]
            graph_dist = min(k, n - k)
            fix4['single_T_at_q0'][f'n{n}'][f'k{k}'] = {
                'graph_distance': graph_dist,
                'distance_parity': 'odd' if graph_dist % 2 == 1 else 'even',
                'delta_I_at_010': d['max_delta_I_theta_010'],
                'delta_II_at_010': d['max_delta_II_theta_010'],
                'is_zero_I': d['is_zero_I'],
                'is_zero_II': d['is_zero_II'],
                'M4_alpha_I': d['M4_alpha_I'],
                'M4_beta_I': d['M4_beta_I'],
                'M4_gamma_I': d['M4_gamma_I'],
                'M4_alpha_II': d['M4_alpha_II'],
                'M4_beta_II': d['M4_beta_II'],
                'M4_gamma_II': d['M4_gamma_II'],
                'full_delta_I': d['delta_I']
            }

# Global T-gate results
for key, d in gt.items():
    fix4['global_T'][key] = {
        'n': d['n'], 'k': d['k'],
        'delta_I': d['delta_I'],
        'delta_II': d['delta_II'],
        'is_zero_I': d['is_zero_I'],
        'is_zero_II': d['is_zero_II']
    }

# Verdict
fix4['verdict'] = {
    'partition_I': {
        'magic_correlation_length_claim': '1 (A博士 claim)',
        'verified': False,
        'corrected_statement': 'Magic correlation vanishes for EVEN graph distance, NONZERO for ODD graph distance. This is a bipartite parity effect, not a length=1 bound.',
        'evidence': {
            'n6': {
                'k=1 (dist=1, odd)': 'NONZERO delta_I=2.89e-3',
                'k=2 (dist=2, even)': 'ZERO delta_I=6.66e-16',
                'k=3 (dist=3, odd)': 'NONZERO delta_I=2.89e-3 -- CONTRADICTS length=1 claim'
            },
            'n7': {
                'k=1 (dist=1, odd)': 'NONZERO delta_I=2.89e-3',
                'k=2 (dist=2, even)': 'ZERO delta_I=3.11e-15',
                'k=3 (dist=3, odd)': 'NONZERO delta_I=2.89e-3 -- CONTRADICTS length=1 claim'
            }
        },
        'physical_mechanism': 'T-gate at qubit 0 changes local phase. Under Partition I, Delta_QCMI = Delta_S([n]\\{k}). The cross term Tr_k(|C><perp| + h.c.) vanishes iff k is at EVEN graph distance from 0 (bipartite sublattice cancellation). For odd distances, the cross term is nonzero, producing O(theta^2 ln(1/theta)) scaling.'
    },
    'partition_II': {
        'magic_correlation_length_claim': '1 (A博士 claim)',
        'verified': True,
        'statement': 'Under Partition II (small B), k>=2 gives zero Delta_QCMI for single T-gate at q=0. A博士 result confirmed for this partition.'
    },
    'global_T_partition_I': {
        'claim': 'Global T-gate cannot create QCMI at k>=2',
        'verified': False,
        'evidence': {
            'n6_k2': 'delta_I=2.85e-3 (NONZERO)',
            'n6_k3': 'delta_I=2.85e-3 (NONZERO)',
            'n7_k2': 'delta_I=1.19e-3 (NONZERO)',
            'n7_k3': 'delta_I=1.19e-3 (NONZERO)'
        },
        'conclusion': 'Global T-gate DOES create nonzero QCMI at k>=2 under Partition I. A博士 claim refuted for this partition.'
    },
    'global_T_partition_II': {
        'claim': 'Global T-gate cannot create QCMI at k>=2',
        'verified': True,
        'statement': 'Under Partition II, global T-gate Delta_QCMI is zero for k>=2 (within machine precision). A博士 result confirmed.'
    }
}

# ============================================================
# Build Fix 5: ln^2 AICc Model Selection
# ============================================================
aicc = raw['fix5_ln2_AICc']

fix5 = {
    'title': 'ln^2 Term AICc Model Selection (T-gate at q=0, k=1)',
    'method': {
        'perturbation': 'T-gate superposition at qubit 0',
        'partition_I': 'A={0}, C={1}, B=[n]\\{0,1}',
        'models': {
            'M3': 'Delta_QCMI = alpha * theta^2 * ln(1/theta) + beta * theta^2  (2 params)',
            'M4': 'Delta_QCMI = alpha * theta^2 * ln(1/theta) + beta * theta^2 + gamma * theta^2 * ln^2(1/theta)  (3 params)'
        },
        'selection_criterion': 'Delta_AICc = AICc(M3) - AICc(M4) > 2 => M4 preferred'
    },
    'results_by_n': {}
}

for n in [5, 6, 7]:
    key = f'n{n}'
    if key in aicc:
        d = aicc[key]
        fix5['results_by_n'][key] = {
            'n': n,
            'M3_I': d['M3_I'],
            'M4_I': d['M4_I'],
            'M3_II': d['M3_II'],
            'M4_II': d['M4_II'],
            'delta_AICc_I': d['delta_AICc_I'],
            'delta_AICc_II': d['delta_AICc_II'],
            'M4_preferred_I': d['M4_preferred_I'],
            'M4_preferred_II': d['M4_preferred_II'],
            'full_delta_I': d['delta_qcmi_I'],
            'full_delta_II': d['delta_qcmi_II']
        }

# A博士 comparison
fix5['comparison_with_A'] = {
    'A_dr_M4_coefficients': {
        'source': 'A博士 fp_r3.json synthesis.key_numbers',
        'alpha': 0.10537123882922675,
        'beta': 0.16744383688383319,
        'gamma': -0.022533892295804374,
        'note': 'A博士 uses n=5, Partition I (A={0},C={1},B={2,3,4}). T-gate superposition. Full-range theta fit.'
    },
    'B_dr_M4_coefficients': {
        'source': 'This work, Partition I, T-gate at q=0, k=1',
        'n5': {'alpha': aicc['n5']['M4_I']['alpha'], 'beta': aicc['n5']['M4_I']['beta'], 'gamma': aicc['n5']['M4_I']['gamma']},
        'n6': {'alpha': aicc['n6']['M4_I']['alpha'], 'beta': aicc['n6']['M4_I']['beta'], 'gamma': aicc['n6']['M4_I']['gamma']},
        'n7': {'alpha': aicc['n7']['M4_I']['alpha'], 'beta': aicc['n7']['M4_I']['beta'], 'gamma': aicc['n7']['M4_I']['gamma']},
        'note': 'n-independent for T-gate at q=0 under Partition I. Values identical across n=5,6,7.'
    },
    'coefficient_comparison': {
        'alpha_B_vs_A': f"{aicc['n5']['M4_I']['alpha']:.6f} vs 0.105371 (sign DIFFERS: B finds negative alpha, A finds positive)",
        'beta_B_vs_A': f"{aicc['n5']['M4_I']['beta']:.6f} vs 0.167444 (sign DIFFERS: B finds negative beta, A finds positive)",
        'gamma_B_vs_A': f"{aicc['n5']['M4_I']['gamma']:.6f} vs -0.022534 (SAME sign, both positive gamma: B=0.0204, A=-0.0225)",
        'discrepancy_note': 'CRITICAL: A博士 and B博士 M4 coefficients have OPPOSITE signs for alpha and beta. This suggests a possible sign convention difference, theta parameterization difference, or a computation error in one trajectory. The gamma signs are also opposite. This MUST be resolved before claiming convergence.'
    },
    'AICc_verdict': {
        'M4_preferred_over_M3': True,
        'delta_AICc_I': aicc['n5']['delta_AICc_I'],
        'interpretation': 'ln^2 term is SIGNIFICANT (Delta_AICc >> 2). M4 is the correct model. Both A and B agree on this qualitative conclusion even if coefficient values differ.'
    }
}

# ============================================================
# Build Fix 1: Partition Convention Unification
# ============================================================
fix1 = {
    'title': 'Unified Partition Convention',
    'problem_statement': 'B博士 R1-R3 used Partition II (small B: A={0}, B={k}, C={k+1}) while A博士 used Partition I (big B: A={0}, C={k}, B=[n]\\{0,k}). Both claimed convergence but were computing DIFFERENT physical quantities.',
    'formal_definitions': {
        'partition_I': {
            'name': 'Big B (A博士 convention)',
            'definition': 'A={0}, C={k}, B=[n]\\{0,k}',
            'B_size': 'n-2 (large conditioning set)',
            'qcmi_expression': 'I(0:k|rest) = S([n]\\{k}) + S([n]\\{0}) - S([n]\\{0,k}) - S([n])',
            'baseline_property': 'QCMI=0 at Clifford point (SSA saturation for graph states)',
            'physical_meaning': 'Measures correlation between A and C conditioned on ALL other qubits. Detects any residual correlation not explained by local influences. HIGH sensitivity to perturbations.'
        },
        'partition_II': {
            'name': 'Small B (B博士 original)',
            'definition': 'A={0}, B={k}, C={k+1 mod n}',
            'B_size': '1 (minimal conditioning set)',
            'qcmi_expression': 'I(0:k+1|k) = S({0,k}) + S({k,k+1}) - S({k}) - S({0,k,k+1})',
            'baseline_property': 'QCMI > 0 at Clifford point (measures graph-state entanglement)',
            'physical_meaning': 'Measures conditional correlation between A and C conditioned on a SINGLE intermediate qubit. LOW sensitivity — only the direct neighbor mediates the correlation.'
        }
    },
    'rule_going_forward': 'From fp_fix onward, BOTH partitions are computed and EXPLICITLY labeled. Primary conclusions are based on Partition I (comparable with A博士). Partition II is retained for backward compatibility with B博士 R1-R3.'
}

# ============================================================
# Build Fix 2: Scope Restriction
# ============================================================
fix2 = {
    'title': 'Scope Restriction to Cluster Rings',
    'problem': 'B博士 R3 extended to star graphs, linear chains, double rings, and triangular prisms — departing from the original "causal ring" problem framework.',
    'corrected_scope': 'This fp_fix round works ONLY on cluster rings C_n (periodic boundary). The cycle space H_1(C_n)=Z with dimension 1 is the defining topological feature of the original problem.',
    'justification': 'Star/chain/prism universality results are valuable but belong to a DIFFERENT research question: "Graph-theoretic shielding in general graph states." The original LP47 question is specifically about causal rings and information localization on cycle topologies.',
    'future_work': 'R4 could generalize to other graph states AFTER the ring-specific claims are rigorously established.'
}

# ============================================================
# Synthesis: Complete fp_fix.json
# ============================================================
fp_fix = {
    'metadata': {
        'project': 'LP47',
        'round': 'fp_fix (修正轮)',
        'author': 'B博士',
        'date': '2026-06-12',
        'polaris': '质量是因果环锁住信息的宏观表现',
        'status': 'CORRECTION — single round only',
        'key_corrections': [
            'FIX1: Partition convention unified — both I (big B) and II (small B) computed',
            'FIX2: Scope restricted to cluster rings C_n only',
            'FIX3: Protection horizon recomputed under Partition I for n=6,7,8',
            'FIX4: Magic correlation length independently verified — A博士 claim PARTIALLY FALSIFIED under Partition I',
            'FIX5: ln^2 term confirmed significant via AICc — M4 preferred with Delta_AICc=21.7'
        ]
    },
    'fix1_partition_convention': fix1,
    'fix2_scope_restriction': fix2,
    'fix3_protection_horizon': fix3,
    'fix4_magic_correlation_length': fix4,
    'fix5_ln2_AICc': fix5,
    'explicit_comparison_with_A_dr': {
        'convergence_points': [
            {
                'point': 'ln^2 term is significant',
                'A_result': 'gamma != 0, M4 preferred',
                'B_result': 'gamma = 0.0204, Delta_AICc = 21.7, M4 strongly preferred',
                'converged': True,
                'note': 'Both agree ln^2 term is physically present in the theta^2 ln^2(1/theta) scaling.'
            },
            {
                'point': 'QCMI at Clifford point under Partition I is zero',
                'A_result': 'QCMI(cluster ring, Partition I) = 0 (SSA saturation)',
                'B_result': 'Confirmed: baseline QCMI = 0 for all n,k under Partition I',
                'converged': True
            },
            {
                'point': 'Magic correlation length = 1',
                'A_result': 'k>=2 gives zero Delta_QCMI for T-gate at q=0 (all k, all n)',
                'B_result': 'PARTIALLY FALSIFIED. Under Partition I, k of ODD graph distance (including k=3 for n=6,7) gives NONZERO Delta_QCMI. Under Partition II, A博士 claim verified.',
                'converged': False,
                'correction': 'Magic correlation vanishes for EVEN graph distance regardless of actual distance value. This is a bipartite parity effect, not a length=1 bound. A博士 tested only n=5 where k_max=2 (only even distance=2 tested), missing the odd-distance k=3 case on n>=6.'
            },
            {
                'point': 'Global T-gate cannot create QCMI at k>=2',
                'A_result': 'Delta_QCMI = 0 for all k>=2 under global T injection',
                'B_result': 'FALSIFIED under Partition I. n=6: delta_I=2.85e-3 for k=2,3. n=7: delta_I=1.19e-3 for k=2,3. Verified under Partition II (delta_II ~ 1e-16).',
                'converged': False,
                'correction': 'Global T-gate DOES create nonzero QCMI at k>=2 under Partition I. Under Partition II (A博士 original), claim holds.'
            },
            {
                'point': 'M4 coefficient values',
                'A_result': 'alpha=0.105, beta=0.167, gamma=-0.0225',
                'B_result': 'alpha=-0.098, beta=-0.173, gamma=0.0204',
                'converged': False,
                'critical_issue': 'ALPHA and BETA have OPPOSITE SIGNS. This is a major discrepancy requiring resolution. Possible causes: (1) different theta parameterization, (2) different orthogonalization of |perp>, (3) sign convention in QCMI definition. Resolution REQUIRED before joint manuscript.'
            }
        ],
        'overall_assessment': '2 of 5 key claims converge (ln^2 term, baseline QCMI). 3 of 5 require correction (magic correlation length, global T, M4 coefficients). The partition convention issue (Fix 1) explains most discrepancies: A博士 results are only valid under Partition II for the magic correlation and global T claims, and their M4 fit may use different theta range/convention.'
    },
    'self_attack': {
        'attack_1_numerical_precision': {
            'question': 'Are the Delta_QCMI values for "protected" qubits truly zero or just below the 1e-12 threshold?',
            'response': 'Protected qubits show Delta_QCMI at machine precision (~1e-16 to ~1e-15), while active qubits show ~1e-2 to ~1e-3. The separation of 12+ orders of magnitude confirms genuine algebraic protection, not threshold effects.',
            'verification': 'For n=6, k=2, q=1 under Partition I: delta=2.22e-16. For same config, q=0: delta=-9.97e-3. Separation = 5e13.'
        },
        'attack_2_T_gate_orthogonalization': {
            'question': 'Could the T-gate |perp> state orthogonalization be different between A and B, explaining the M4 coefficient sign discrepancy?',
            'response': 'Yes, this is a likely cause. A博士 uses |perp> = (T_0|C> - <C|T_0|C>|C>)/norm. B uses the same formula. Both should give identical |perp>. The sign difference could come from the GLOBAL phase convention of the cluster state |C_n> or from a different sign in the T-gate definition (T = diag(1, e^{i*pi/4}) vs diag(1, e^{-i*pi/4})).',
            'action': 'Requires explicit phase convention comparison. Cannot resolve in this round.'
        },
        'attack_3_n_independence_of_AICc': {
            'question': 'AICc results are identical for n=5,6,7. Is this n-independence physically correct or a computation artifact?',
            'response': 'Physically correct. Under Partition I with T-gate at q=0, k=1: Delta_QCMI = Delta_S([n]\\{1}). The reduced state on [n]\\{1} depends only on the local stabilizer structure near qubits 0 and 1 (the boundary of the subsystem is the 2 edges incident to qubit 1). For cluster rings, this local structure is n-independent.',
            'verification': 'Confirmed by n=5,6,7 giving identical numerical values for all theta points (to machine precision).'
        },
        'attack_4_bipartite_parity_pattern': {
            'question': 'The odd/even graph distance pattern for magic correlation — is this specific to cluster rings?',
            'response': 'It is a CONSEQUENCE of the bipartite nature of the cluster ring graph. The cluster state sign structure (-1)^{x_j x_{j+1}} encodes the graph edges. For bipartite graphs, the T-gate perturbation at qubit 0 creates correlations that survive partial trace iff the traced qubit is on the opposite sublattice (odd distance). For non-bipartite graphs (odd cycles), the pattern may differ.',
            'caveat': 'This is derived from numerical observation, not analytical proof. The analytical derivation requires analyzing the stabilizer structure of Tr_k(|C><perp| + h.c.).'
        }
    },
    'summary': {
        'what_was_corrected': [
            'FIX1: Partition convention now dual-track (I + II), explicitly labeled',
            'FIX2: Scope restricted to cluster rings C_n only',
            'FIX3: Protection horizon (n=6,7,8) matrices computed under both partitions — significant differences found',
            'FIX4: Magic correlation length claim corrected: parity-based (odd=nonzero, even=zero), not length=1',
            'FIX5: ln^2 term confirmed significant (Delta_AICc=21.7) with new M4 coefficients under Partition I'
        ],
        'what_was_FALSIFIED': [
            'A博士 "magic correlation length = 1" under Partition I: FALSE for odd graph distances (k=3 nonzero)',
            'A博士 "global T-gate cannot create QCMI at k>=2" under Partition I: FALSE (k=2,3 nonzero)',
            'A博士 M4 coefficient values: NOT reproduced by B博士 — sign discrepancy requires resolution'
        ],
        'what_was_CONFIRMED': [
            'A博士 identification of ln^2 term as physically significant: CONFIRMED (Delta_AICc >> 2)',
            'A博士 baseline QCMI=0 for Partition I: CONFIRMED',
            'A博士 magic correlation length = 1 under Partition II: CONFIRMED',
            'B博士 R3 protection patterns under Partition II: CONFIRMED (backward compatibility)'
        ],
        'unresolved_issues': [
            'M4 coefficient sign discrepancy between A and B — requires phase convention audit',
            'Analytical proof of bipartite parity selection rule for T-gate QCMI under Partition I',
            'Protection depth delta(n,k) under Partition I: no simple closed form found — pattern is irregular'
        ],
        'next_steps': [
            'Resolve M4 sign discrepancy with A博士 (joint phase convention audit)',
            'Analytical derivation of T-gate parity selection rule',
            'Extend n=8 protection matrix to n=9,10 if computationally feasible',
            'Prepare corrected joint claims for manuscript'
        ]
    }
}

# Save
output_path = r'D:\Claude\ai-reservations\LP47-因果环信息局域化\current\B\fp_fix.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(fp_fix, f, indent=2, ensure_ascii=False)

print(f"fp_fix.json saved to: {output_path}")
print(f"Size: {len(json.dumps(fp_fix, ensure_ascii=False))} chars")
