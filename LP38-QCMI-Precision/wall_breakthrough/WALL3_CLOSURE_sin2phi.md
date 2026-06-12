# Wall 3 Closure: Cartan Axis φ-Scan — sin(2φ) Discovery

**Date:** 2026-06-09
**Status:** WALL CLOSED — continuous curve replaces 2-point claim
**Key Finding:** QCMI ∝ sin(2φ), NOT sin²φ

---

## Before (Vulnerable)

> "Cartan axis controls QCMI magnitude." Supported by only 2 data points: φ=0 (aligned) and φ=π/2 (misaligned).

**Reviewer attack:** "You have two points. You drew a line through them and called it a theory. Show me the curve."

## After (Defensible)

30-point continuous φ-scan with R² = 0.953 for sin(2φ) model. The functional form is:

$$\boxed{\text{QCMI}(\phi) = 1.715 + 1.420 \cdot \sin(2\phi) - 0.104 \cdot \cos(2\phi)}$$

with R² = 0.978 for the full Fourier model and R² = 0.953 for pure sin(2φ).

## Physical Discovery

The original theory predicted QCMI ∝ sin²φ (from |c×c'|² commutator argument). The experiment reveals a **different mechanism:**

| φ | Cartan axis | XX coupling | ZZ coupling | QCMI |
|:--|:--|:--|:--|:--|
| 0 | Pure ZZ | 0 | θ | 1.76 bits |
| π/4 | Mixed XX+ZZ | θ/√2 | θ/√2 | **3.20 bits (PEAK)** |
| π/2 | Pure XX | θ | 0 | 2.00 bits |

**The peak is at φ=π/4 (45°), not φ=π/2 (90°).**

This means the QCMI φ-dependence comes from **constructive interference** between XX and ZZ Cartan channels (cross-term), not from simple axis misalignment. The product sin(φ)·cos(φ) = ½sin(2φ) captures this cross-term.

## Control Experiments

| Control | QCMI | Interpretation |
|:--|:--|:--|
| All identity | 0.000 | No artifact in initial state |
| 1 ZZ edge | 0.881 | **ZZ DOES generate QCMI** (refutes original premise) |
| 2 ZZ edges | 1.763 | Exactly 2× single edge — additive |

**Why ZZ generates QCMI (despite [Z⊗Z, I/2⊗γ] = 0):** The Cartan unitary acts on Qa-E1 while Qa is Bell-entangled with Ra. ZZ coupling leaks Qa-Ra entanglement into tripartite Qa-E1-Ra correlations → QCMI > 0. The original premise that "aligned ZZ = no QCMI" was correct for the Qa reduced state alone, but WRONG for the full system.

## Paper Impact

| Before | After |
|:--|:--|
| "Cartan axis controls QCMI" (2 points) | "QCMI(φ) = A + B·sin(2φ)" (30 points, R²=0.953) |
| Predicted max at φ=π/2 | Measured max at φ=π/4 — constructive XX-ZZ interference |
| sin²φ from commutator argument | sin(2φ) from cross-term interference — **new physical mechanism** |
| Narrative vulnerability | Narrative STRENGTHENED — sin(2φ) is a sharper, falsifiable prediction |

## Remaining Task

- [ ] Update bridge_to_smoking_gun.md §4.1 to replace sin²φ with sin(2φ)
- [ ] Update PRL narrative framework with corrected functional form

---

*Wall 3 CLOSED. The 2-data-point vulnerability is replaced by a 30-point sin(2φ) curve. The physical mechanism (constructive XX-ZZ interference) is more interesting than the original sin²φ prediction.*
