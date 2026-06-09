# INSPECTOR Review: LP36 CFOL Case II v5 Fix

**Reviewer:** INSPECTOR (independent)
**Date:** 2026-06-09
**Target:** `round1_factorization.md` lines 447-471 (FIXED v5) + surrounding context lines 412-446
**Verdict:** **BLOCK** -- v5 argument contains a fatal logical gap; Case II remains unproven.

---

## Executive Summary

v5 attempts to replace v4's flawed trace-counting argument with a "direct proof" that r_2 = 1 in Case II. The core claim is that C^†C = I and D^†D = I together force T_0^†T_1 = 0, which then leads to a contradiction with r_2 = 2. **This claim is unjustified.** The derivation conflates "coefficient of T_0^†T_1 in the expansion of the identity matrix is zero" with "T_0^†T_1 is the zero operator" -- fundamentally different statements. Furthermore, a constructive example demonstrates that r_2 = 2 with diagonal S_ell and C^†C = D^†D = I is mathematically consistent, refuting the claimed contradiction.

Additionally, the v3 summary (R1.6 FIX, line 820) claims a cross block yields C^†D = 0, but the actual cross block yields C^†E = 0. This error-in-summary has been carried forward uncorrected, masking the fact that Case II has never been properly resolved.

**Case I (dim(Y) = d) is independently valid.** The theorem is proven for Case I. The gap is limited to Case II.

---

## 1. Logical Correctness

### 1.1 The T_0^†T_1 = 0 Gap (FATAL)

The v5 argument (lines 460-463) states:

> "两个酉性条件在子空间 span{T_0^†T_1, T_1^†T_0} 上给出两个独立的线性约束。在 d=2 下，这两个约束联立要求 T_0^†T_1 = 0"

Let us trace the derivation carefully. For r_2 = 2:

```
C^†C = t_0^2|c_0|^2 T_0^†T_0 + t_1^2|c_1|^2 T_1^†T_1 + t_0 t_1(cbar_0 c_1 T_0^†T_1 + cbar_1 c_0 T_1^†T_0) = I   (Eq-C)
D^†D = t_0^2|d_0|^2 T_0^†T_0 + t_1^2|d_1|^2 T_1^†T_1 + t_0 t_1(dbar_0 d_1 T_0^†T_1 + dbar_1 d_0 T_1^†T_0) = I   (Eq-D)
```

If {T_0^†T_0, T_1^†T_1, T_0^†T_1, T_1^†T_0} forms a basis for 2x2 matrices, we can match coefficients of the unique expansion of I. From (Eq-C) and (Eq-D) equating coefficients:

```
|c_0| = |d_0|,  |c_1| = |d_1|          (from T_0^†T_0, T_1^†T_1 terms)
cbar_0 c_1 = dbar_0 d_1                (from T_0^†T_1 term)
```

Combined with HS orthonormality |c_ell|^2 + |d_ell|^2 = 1 and Gram orthogonality cbar_0 c_1 + dbar_0 d_1 = 0:

```
|c_0| = |d_0| = 1/sqrt(2),  |c_1| = |d_1| = 1/sqrt(2)
cbar_0 c_1 = dbar_0 d_1 = 0
```

Thus the coefficient of T_0^†T_1 in the expansion of I is **zero** (t_0 t_1 * 0 = 0). But this only means:

```
I = t_0^2/2 * T_0^†T_0 + t_1^2/2 * T_1^†T_1
```

**It does NOT mean T_0^†T_1 = 0 as an operator.** The operator T_0^†T_1 is generally nonzero; only its coefficient in the specific expansion of I happens to vanish.

**Why this is a gap, not a minor oversight:** The entire remainder of the v5 argument (T_0^†T_1 = 0 -> orthogonal column spaces -> |t_0 c_0|^2 = 1 -> t_0^2 = t_1^2 = 2 -> contradiction via T_0 T_0^† = T_1 T_1^†) depends on T_0^†T_1 being the zero matrix. If T_0^†T_1 is not forced to zero, the chain collapses.

### 1.2 Constructive Demonstration that r_2 = 2 is Consistent

The following explicit construction satisfies ALL conditions that v5 has established at the point where it claims impossibility:

- S_0 = diag(1, 0), S_1 = diag(0, 1) in the adapted basis {|y>, |x>}_in, {|v>, |v^bot>}_out
- T_0 = U_0/sqrt(2), T_1 = U_1/sqrt(2), where U_0, U_1 are any HS-orthogonal 2x2 unitaries
- t_0 = t_1 = sqrt(2)

Verification:
1. **HS orthonormality of S_ell:** Tr(S_0^†S_0) = Tr(diag(1,0)) = 1, Tr(S_1^†S_1) = 1, Tr(S_0^†S_1) = 0. PASS
2. **HS orthonormality of T_ell:** Tr(T_0^†T_0) = Tr(I/2) = 1, Tr(T_1^†T_1) = 1, Tr(T_0^†T_1) = Tr(U_0^†U_1)/2 = 0. PASS
3. **C^†C = I:** C = t_0*1*T_0 + t_1*0*T_1 = sqrt(2)*U_0/sqrt(2) = U_0. C^†C = I. PASS
4. **D^†D = I:** D = t_0*0*T_0 + t_1*1*T_1 = U_1. D^†D = I. PASS
5. **u_2^†u_2 = I:** u_2 = sqrt(2)*diag(1,0) x U_0/sqrt(2) + sqrt(2)*diag(0,1) x U_1/sqrt(2) = diag(1,0) x U_0 + diag(0,1) x U_1. Then u_2^†u_2 = diag(1,0) x I + diag(0,1) x I = I x I. PASS
6. **u_2 u_2^† = I:** Similarly, diag(1,0) x I + diag(0,1) x I = I x I. PASS
7. **Sum t_ell^2:** 2 + 2 = 4 = d^2. PASS
8. **S_ell satisfy the adapted-basis constraints:** S_0|y> = |v>, S_0|x> = 0; S_1|y> = 0, S_1|x> = |v^bot>. Both S_ell(Y) subset span{|v>} and S_ell^†|v^bot> prop-to |x>. PASS
9. **T_0^†T_1 is NOT zero:** T_0^†T_1 = U_0^†U_1/2, generally nonzero (e.g., U_0=I, U_1=sigma_z gives sigma_z/2 != 0).

This construction has r_2 = 2 and satisfies every condition that the proof has established up to line 463. The v5 claim of impossibility is therefore **false for the u_2 sector in isolation.**

**Important nuance:** This construction verifies consistency within the u_2 constraints alone. Whether this r_2=2 solution is compatible with the FULL set of constraints (including u_1's R_k and the joint X-perp-Y condition) is a separate question not resolved by this counterexample. The counterexample's purpose is to show that v5's claimed u_2-sector contradiction does not exist.

### 1.3 The |t_0 c_0|^2 = 1 Derivation Gap

Even if T_0^†T_1 = 0 were true, the subsequent claim that |t_0 c_0|^2 = 1 (line 463) is not properly derived. From T_0^†T_1 = 0 and C^†C = I:

```
C^†C = t_0^2|c_0|^2 T_0^†T_0 + t_1^2|c_1|^2 T_1^†T_1 = I
```

This does NOT imply |t_0 c_0|^2 = 1 unless one additionally assumes that T_0^†T_0 acts as the identity on its range (or that T_0 is proportional to an isometry with a specific normalization). For a general HS-normalized T_0, T_0^†T_0 can have eigenvalues different from 1. For example, if T_0 = U_0/sqrt(2) with U_0 unitary, then T_0^†T_0 = I/2, and |t_0 c_0|^2 = 1 would require t_0^2 * 1/2 = 1 -> t_0^2 = 2, which happens to be true but is a consequence, not the premise.

### 1.4 The T_0 T_0^† = T_1 T_1^† Claim (Undefined Origin)

Line 463 states: "后者要求 T_0 和 T_1 的像空间满足 T_0 T_0^† = T_1 T_1^†". No derivation is provided for this equality. Where does it come from? Possibilities:
- From u_2 u_2^† = I? This gives C C^† = I and D D^† = I, not a relation between T_0 and T_1.
- From equating the two expansions of I? Already analyzed in 1.1.
- From some condition involving C and D being "unitary on orthogonal subspaces"? This is precisely what needs proving, not an input.

The equality T_0 T_0^† = T_1 T_1^† appears without justification.

---

## 2. Relationship with Case I

### 2.1 Case I is Independently Valid

Case I (dim(Y) = d) is proven rigorously:
1. dim(Y) = d => M > 0 (correct: sum of positive rank-1 terms spanning full space)
2. M > 0 and X perp Y => X = {0} (correct: a nonzero X would have a vector orthogonal to all of C^d)
3. X = {0} => S_ell^†|v^bot> = 0 for all ell (correct: by definition of X)
4. Each S_ell has rank at most 1 (correct: all share null vector |v^bot> != 0)
5. If r_2 >= 2, all S_ell share the same 1-dim range => u_2's E_1-component is 1-dim => rank(u_2) <= d < d^2, contradicting unitarity (correct rank argument)

**Case I does NOT depend on Case II's resolution.** It is a self-contained proof that when dim(Y) = d, r_1 = r_2 = 1.

### 2.2 The Logical Structure

The proof has a case split:
- Case I (dim(Y) = d): RESOLVED (r_1 = r_2 = 1)
- Case II (dim(Y) <= d-1): UNRESOLVED

The theorem is true if Case II is either (a) impossible, or (b) also leads to r_1 = r_2 = 1. Neither has been validly established.

### 2.3 Does Case I "Cover" the Theorem?

**No.** Case I only covers the situation where {R_k|gamma_tilde>} spans all of C^d. The condition QCMI = 0 does not a priori guarantee this; it only guarantees A_1 = mu A_0, which gives X perp Y and the dimensional constraints dim(X) >= 1, dim(Y) >= 1, dim(X) + dim(Y) <= d. For d=2, dim(Y) could be 1. One must prove that dim(Y) = d always holds, or handle the dim(Y) = 1 case separately.

---

## 3. Completeness

### 3.1 r_2 = 1 Case (Trivial Factorization)

If r_2 = 1, then u_2 = t_0 S_0 x T_0 is already factorized (S_0 acts only on E_1, T_0 only on Q_b). The proof's goal is to show r_2 = 1; the r_2 = 1 case is the target, not a gap.

### 3.2 d = 2 Assumption

The d = 2 assumption is used at several points in Case II:
- dim(X) = dim(Y) = 1 (from dim(X) + dim(Y) <= 2, dim(X) >= 1, dim(Y) >= 1): VALID
- S_ell is 2x2 upper triangular: VALID for d=2
- C is 2x2 unitary (from C^†C = I, square matrix): VALID for d=2
- The argument that "all S_ell commute" giving r_2 <= 2: VALID for d=2 (diagonal 2x2 matrices form a 2-dim space)

For d > 2, the Case II analysis would need substantial revision. The v5 claims (line 467) that "symmetry gives r_1 = 1, r_1^(34) = 1, r_2^(34) = 1", but this depends on Case II being resolved first.

### 3.3 gamma_0 != gamma_1 Condition

The condition gamma_0 != gamma_1 (or more generally, gamma being full-rank with non-degenerate eigenvalues) is NOT used in the v5 argument. The v5 argument only depends on S_ell being diagonal and C^†C = D^†D = I, neither of which requires gamma_0 != gamma_1. This is not a bug per se, but worth noting: the generality of the proof with respect to gamma is not compromised.

---

## 4. Gap Detection Summary

### Gap 1 (FATAL): T_0^†T_1 = 0 Unjustified

**Location:** Lines 460-463
**Nature:** Logical leap from "coefficient zero in expansion" to "operator zero"
**Severity:** BLOCK -- the entire v5 argument for r_2 = 1 depends on this step
**Fixability:** Requires a fundamentally different argument; cannot be patched by adding a few lines

### Gap 2: |t_0 c_0|^2 = 1 Unjustified

**Location:** Line 463
**Nature:** Missing derivation; assumes structure of T_ell^†T_ell not established
**Severity:** Would be BLOCK if Gap 1 were resolved
**Fixability:** Possibly fixable with additional lemmas about T_ell structure

### Gap 3: T_0 T_0^† = T_1 T_1^† Without Derivation

**Location:** Line 463
**Nature:** Claim appears ex nihilo; no equation in the setup yields this
**Severity:** Would be BLOCK if Gap 1 were resolved
**Fixability:** Unclear what would justify this equality

### Gap 4 (v3 summary error): C^†D = 0 Does Not Exist

**Location:** R1.6 FIX summary, line 820
**Nature:** The cross block of u_2^†u_2 = I gives C^†E = 0, not C^†D = 0. When S_ell is upper triangular:

```
S_ell^† S_m = [[cbar_ell c_m,    cbar_ell e_m   ],
              [ebar_ell c_m,    ebar_ell e_m + dbar_ell d_m]]
```

The (1,2) block involves e_m, not d_m. After proving e_ell = 0, S_ell is diagonal and there are NO cross terms in u_2^†u_2 at all -- only |v><v| x C^†C + |v^bot><v^bot| x D^†D = I x I. The v3 "contradiction" (C^†D = 0 -> D = 0) was never valid.

**Severity:** This means Case II has been unresolved since v3, not just since v5. The error was masked by an incorrect summary.

---

## 5. Comparison with v4

### 5.1 The v4 t_ell^2 Issue

v5 correctly identifies that v4's trace-counting argument omitted the operator Schmidt weights t_ell^2. The identity:

```
Tr(C^†C) + Tr(D^†D) = sum_ell t_ell^2 (|c_ell|^2 + |d_ell|^2) = sum_ell t_ell^2 = d^2
```

is correct. v4's conclusion "2d = r_2 d => r_2 = 2" would only follow with additional unjustified assumptions. v5 is right to discard this argument.

### 5.2 Does v5 Introduce New Problems?

**Yes.** v5 replaces one flawed argument (trace counting without t_ell^2 weights) with another flawed argument (T_0^†T_1 = 0 from coefficient matching). The new gap (Gap 1) is more subtle but equally fatal.

The v5 argument is also harder to audit because it compresses multiple reasoning steps into dense prose without explicit equations (lines 460-464 are a single paragraph covering coefficient matching, linear independence of constraints, T_0^†T_1 = 0, orthogonal column spaces, magnitude constraints, t_ell^2 = 2, the Gram/phase condition, and the final contradiction).

### 5.3 Status Progression

| Version | Case I | Case II | Status |
|---------|--------|---------|--------|
| v2 | GAP-1 (M>0 proof) | Not reached | BROKEN |
| v3 | VALID | Claimed C^†D=0 (ERROR) | BROKEN (Case II) |
| v4 | VALID | Trace counting w/o t_ell^2 | BROKEN (Case II) |
| v5 | VALID | T_0^†T_1=0 gap | BROKEN (Case II) |

---

## 6. Overall Assessment

### Verdict: BLOCK

The CFOL (==>) direction is **not fully proven.** Case I (dim(Y) = d) has a valid proof yielding r_1 = r_2 = 1. Case II (dim(Y) <= d-1) remains unresolved through all versions v3-v5.

### What Would Be Needed

To complete the proof, one of the following must be established:

**(A) Prove Case II is impossible.** Show that dim(Y) <= d-1 cannot occur under the QCMI = 0 condition. This would require finding a contradiction in the joint constraints on {S_ell, R_k} that is more subtle than v3's incorrect C^†D = 0 or v5's unjustified T_0^†T_1 = 0.

**(B) Prove Case II also yields r_1 = r_2 = 1.** Accept that dim(Y) = 1 is possible but show that the structure S_ell = diag(c_ell, d_ell) with C^†C = D^†D = I forces r_2 = 1. This is what v5 attempted but failed to do.

**(C) Bypass the X/Y subspace approach entirely.** Find a different proof strategy that avoids the Case I/II split.

### Recommendation

Route (A) seems most promising. The key observation is that in Case II, S_ell = diag(c_ell, d_ell) with both c_ell and d_ell potentially nonzero. The combined constraints from u_2^†u_2 = I and u_2 u_2^† = I give C^†C = C C^† = I and D^†D = D D^† = I, making C and D both unitary. With diagonal S_ell:

```
u_2 = |v><v| x C + |v^bot><v^bot| x D
```

This is a block-diagonal unitary. Its operator Schmidt rank is the number of nonzero singular values of the "correlation matrix" between {|v><v|, |v^bot><v^bot|} and the T_ell. Since both blocks are full-rank unitaries, the operator Schmidt rank is exactly 2. But this means r_2 = 2 IS possible in the u_2 sector -- it does NOT force r_2 = 1.

The path forward is to incorporate the u_1 constraints (R_k, Y = span{R_k|gamma_tilde>} = span{|y>}) and the cross-constraint X perp Y to find a joint contradiction, rather than trying to prove impossibility from u_2 alone.

---

## Appendix A: The C^†D = 0 Error in Detail

For the record, here is why C^†D = 0 does not appear in the u_2^†u_2 expansion.

With upper-triangular S_ell = [[c_ell, e_ell], [0, d_ell]]:

```
u_2^† u_2 = sum_{ell,m} t_ell t_m S_ell^† S_m x T_ell^† T_m

S_ell^† S_m = [[cbar_ell c_m,       cbar_ell e_m      ],
              [ebar_ell c_m,       ebar_ell e_m + dbar_ell d_m]]
```

Expanding in the E_1 basis {|v>, |v^bot>}:

```
u_2^† u_2 = |v><v|       x C^†C
          + |v><v^bot|   x C^†E        <-- THIS is the cross block
          + |v^bot><v|   x E^†C
          + |v^bot><v^bot| x (E^†E + D^†D)
```

where C = sum t_ell c_ell T_ell, E = sum t_ell e_ell T_ell, D = sum t_ell d_ell T_ell.

The cross block is C^†E = 0, **not** C^†D = 0. After proving E = 0 (from C unitary and C^†E = 0), S_ell is diagonal and ALL cross terms vanish. There is no C^†D equation anywhere in the u_2^†u_2 = I condition.

---

## Appendix B: Full Constructive Example

For concreteness, here is a complete r_2 = 2 operator Schmidt decomposition satisfying C^†C = D^†D = I and u_2^†u_2 = u_2 u_2^† = I x I:

```
E_1 basis: {|v>, |v^bot>}, Q_b basis: {|0>, |1>}

S_0 = |v><y|    (c_0 = 1, d_0 = 0, e_0 = 0)
S_1 = |v^bot><x| (c_1 = 0, d_1 = 1, e_1 = 0)

T_0 = I/sqrt(2) (2x2 identity, normalized)
T_1 = sigma_z/sqrt(2) (Pauli Z, normalized)

t_0 = sqrt(2), t_1 = sqrt(2)

u_2 = sqrt(2) * |v><y| x I/sqrt(2) + sqrt(2) * |v^bot><x| x sigma_z/sqrt(2)
    = |v><y| x I + |v^bot><x| x sigma_z

C = sqrt(2)*1*I/sqrt(2) + sqrt(2)*0*sigma_z/sqrt(2) = I,  C^†C = I
D = sqrt(2)*0*I/sqrt(2) + sqrt(2)*1*sigma_z/sqrt(2) = sigma_z, D^†D = I

u_2^† u_2 = (|y><v| x I + |x><v^bot| x sigma_z)(|v><y| x I + |v^bot><x| x sigma_z)
          = |y><y| x I + |x><x| x I = I_{E_1} x I_{Q_b}
```

This is a perfectly valid unitary with r_2 = 2. It resides in Case II because S_0 maps |y> -> |v> (preserving the Y-to-span{|v>} structure) and S_1 maps |x> -> |v^bot> (preserving the X-perp-Y structure). The v5 claim that r_2 = 2 leads to contradiction is refuted by this explicit counterexample to the claimed contradiction.

**Caveat:** This example satisfies all u_2-sector constraints. Whether it can be paired with a valid u_1 satisfying the joint X-perp-Y constraint AND the full unitarity of u_1 is not addressed here; the point is that v5's claimed u_2-only contradiction does not exist.
