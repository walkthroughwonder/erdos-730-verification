# Erdős #730 audit — first-read notes (2026-07-27)

Full paper captured (9 pp) via the Overleaf PDF text layer; structure:
Lemma 2.1 (transition criterion, with proof) → §2.1 construction (P,Q,R,S
linear forms, identities (4), obstruction polynomials Φ_L (5)-(6),
permutation property (9)) → §3 Fourier machinery (L3.1 restricted-digit
Fourier norm; L3.2 incomplete quadratic sums; P3.3 quadratic
restricted-digit estimate) → §4 first-moment count: small primes o(X),
repeated large primes o(X), main range Y < p ≤ X^{1/2}/log X contributes
(4C+o(1))X via blocks + P3.3, boundary range O(εX), large primes p > X^{1/2+ε}
contribute (2/3 log 2 + o(1))X via a residue-class analysis, total Λ =
4C + (2/3)log 2 < 1, density of good x ≥ 1 − Λ ≈ 0.0430.

## First-pass verification already done by hand (reading pass)

- **Lemma 2.1, A-branch**: recomputed the digit-sum identities myself:
  s_p(p^a u − 1) = s_p(u−1) + a(p−1); s_p(2p^a u − 2) = s_p(2u−1) + a(p−1) − 1;
  gives v_p(B_n) = a + v_p(B_u) ✓ and v_p(B_{n+1}) = v_p(B_u) ✓. Criterion
  (2) ⇔ p stays in the radical ✓ CHECKS.
- **Lemma 2.1, M-branch**: n = p^a w + (p^a−1)/2 ✓; v_p(B_n) = v_p(B_w) via
  digit sums ✓; criterion (3) = w ∉ D_p ⇔ p not newly introduced ✓ CHECKS
  (modulo one more careful pass at v_p(B_{n+1}) = v_p(B_n) + a).
- **Construction identities (4)**: 2PQ−1 = 3RS, 12P−7Q = 41, 18R−7S = −43
  — algebra checks; coprimality logic (41 | T, 43 | T exclusions) checks;
  "every odd prime ≠ 3 divides exactly one of P,Q,R,S" verified including
  41 ∤ PQ·3RS and 43 ∤ (mod arithmetic: PQ ≡ 20 (mod 41), 3RS ≡ 39 (mod 41)).
- **Λ numerics**: C = Σ 4^{-r} log((r+2)/(r+1)) = 0.12374; Λ = 4C + (2/3)log2
  = 0.95705 ✓ matches paper; 1 − Λ ≈ 0.0430.

## Soft spots for the deep audit (A4), ranked

1. **Lemma 3.2 proof**: the completion + "vanishes unless s ≡ −h₀B (mod p)"
   step, the Gauss-sum evaluation p√Q, and the harmonic bound
   N + Q log M ≪ Q log M (needs N ≤ Q ✓ since N = p^r, Q ≥ p^r). Re-derive.
2. **§4 small-primes block**: the (K/p^j + 1)H^j count via the permutation
   property, and the uniformity of exp(−c log K/log p) over p ≤ Y, p^a ≤ X^{1/2}.
3. **§4 main-range bookkeeping**: r_p definition, block decomposition,
   Mertens uniformity at endpoints exp(cL^{2/3}) (claimed o(1) uniformly —
   plausible since error ≪ L^{-2/3}), the grouped remainder Σ p^{r_p} bound.
4. **Large-prime residue table**: αc² mod d values and the branch
   eliminations (Q,S: none; P: c ≡ 3,4 mod 7 → p ≡ 1,6 mod 7; R: c ≡ 5,9
   mod 14 → p ≡ 1,13 mod 14); the claim s/d ∈ [3/7, 6/7]; the φ-density
   count (2 classes of 6 → 1/3 per branch, two branches → (2/3)log 2).
   ALL FINITE — verify by direct computation.
5. **First-moment logic**: E(x) ≥ 1_{E≥1}, union bound direction ✓; each
   obstruction attached to exactly one (branch, p, a) ✓ given exact-one-of
   -four divisibility. Looks sound.

## Numerics plan (A5) — the decisive tests

- N1: brute-force Lemma 2.1 for all n ≤ 2000: compare rad B_n = rad B_{n+1}
  directly vs the criterion. Any mismatch kills the paper's foundation.
- N2: verify the residue table + branch eliminations by enumeration.
- N3: empirical density: for x = 1..X₀ (X₀ ~ 2000–10⁴), factor P,Q,R,S
  (~1e10-sized; sympy), test all criterion conditions, measure the fraction
  of good x. Prediction: ≥ 1 − Λ ≈ 0.043 (likely much higher). Bonus: this
  YIELDS CONCRETE NEW PAIRS for OEIS A129515 if any x is good — the current
  known list is tiny (87, 607, 10003...).
- N4: verify C and Λ to high precision; verify the final elementary
  inequality chain (e^{8/3} > 49621/3645 > 27/2).

## Early impression

Unusually professional for the genre — every constant explicit, standard
analytic shapes, and the finitely-checkable claims are all stated crisply.
No red flags on first read. The verdict will hinge on A4 items 1–3 and the
N1/N3 numerics.
