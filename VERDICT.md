# VERDICT: Erdős #730 candidate solution — CONFIRMED (auditor's report)

*Audit by Edwin Rosero with AI assistance (Claude, Anthropic), 2026-07-27.
Subject: "Equal Radicals of Consecutive Central Binomial Coefficients"
(GPT-5.5 Pro via Liam Price, posted 24 Jun 2026, Overleaf read/gpttrsmhbhbk).*

## Verdict

**CONFIRMED.** After a line-by-line audit we find the proof correct. The
answer to Erdős #730 is YES: there are infinitely many pairs — indeed
infinitely many consecutive pairs — of central binomial coefficients with
equal prime support, with an explicit quadratic family achieving lower
density ≥ 1 − Λ ≈ 0.0430 (empirically ≈ 49%).

## What was checked, and how

1. **Lemma 2.1 (transition criterion).** Re-proved by hand (both digit-sum
   branches recomputed independently) AND verified exhaustively by machine
   for all n < 1200 against direct radical computation: zero mismatches.
   The resulting equal-radical list (87, 199, 237, 467, 607, 967, 1127)
   equals the first seven terms of OEIS A129515 exactly.
2. **§2.1 construction.** All identities re-derived ((4), coprimality,
   exactly-one-branch); the Φ_L formulas re-derived independently two ways
   (ours, and Tomodovodoo's addendum — which is provenance analysis, not a
   mathematical patch; its algebra agrees). Slope identity
   (12/7)(42T)² = (7/12)(72T)² = (54/14)(28T)² = 3024T² verified.
3. **Lemma 3.1.** Recursion 1̂_{D_{p,m}} = S_H · 1̂_{D_{p,m−1}} and the
   1/p-spaced harmonic estimate re-derived; induction sound.
4. **Lemma 3.2.** Re-derived in full: the permutation property for
   v_p(h) ≥ r; the completion identity; the y → y+Q translation forcing
   s ≡ −h₀B (mod p) (a nonzero class, so s = 0 never survives); the
   reduction of the inner sum to p·|Gauss sum| = p√Q (squaring argument
   checked for odd prime-power modulus); the harmonic bound
   ≪ N + Q log M with N = p^r ≤ Q. Final bound ≪ r p^{r−1/2} log p: sound.
5. **Proposition 3.3.** Assembly of L3.1 + L3.2 checked; error
   p^{r−1/2}(C₁ log p)^{2r+1} absorbs the factor r: sound.
6. **§4 small primes / repeated primes.** The (K/p^j + 1)H^j count via the
   permutation property (9); uniformity exp(−c'L^{1/3}) over p ≤ Y,
   p^a ≤ X^{1/2}; the √(XY), Y log X, X/Y tails: all o(X). Sound.
7. **§4 main range.** Block decomposition; per-block Prop 3.3 with 2r_p
   digits (upper-bound direction only — legitimate); η uniformity
   (log η ≤ −½L^{2/3} + O(L^{1/3} log L)); remainder grouping
   Σ p^{r_p} ≪ XL^{−1/3}; K_p → X/p replacement; (1+1/p)^{2r_p} = 1+o(1);
   the r_p = r ⟺ (X/2)^{1/(r+2)} < p ≤ (2X)^{1/(r+1)} windows; Mertens
   with uniform o(1) at endpoints ≥ exp(cL^{2/3}); the R-tail double
   limit. Result Σ 4^{−r_p}/p ≤ C + o(1) per branch: sound.
8. **§4 boundary + large primes.** The O(εX) window; the t = lowest-digit
   argument (s/d ∈ [3/7, 6/7] verified numerically — never 1/2, so the
   o(1) cannot flip the test); the residue table VERIFIED by enumeration;
   the class conversions (P: p ≡ 1,6 mod 7; R: p ≡ 1,13 mod 14) verified
   by modular inversion; the (14)-density count (2 of 6 classes → 1/3 per
   branch, two branches → (2/3)log 2). Sound.
9. **Constants.** C and Λ recomputed to 15 digits (match); the elementary
   chain e^{8/3} > 49621/3645 > 27/2 ⟹ Λ < 1 verified.
10. **Empirical validation of the whole pipeline.** For x ≤ 400, factoring
    A = PQ and M = 3RS completely and applying the (independently proved)
    criterion: 196/400 parameters give genuine consecutive equal-radical
    pairs — density 49%, comfortably above the guaranteed 4.3%. Byproduct:
    196 explicit new pairs, smallest n = 338,381,863,522 (previous record
    n = 10,005), largest checked n ≈ 1.35 × 10^16.
11. **Statement fidelity.** The formal statement (FormalConjectures
    ErdosProblems/730.lean: infinitude of {(n,m) : n < m, equal prime
    support of central binomials}) is implied by the paper's theorem.

## Caveats

- Human verification (with extensive machine assistance on every finitely
  checkable component); not yet a formal end-to-end Lean proof. The
  analytic sections (§3–§4) were re-derived by the auditors, not
  machine-checked.
- The paper's argument is an upper-bound/first-moment argument throughout;
  no step requires equidistribution beyond the proved estimates.
- One presentational nit: the final display's bound
  "≤ log(3/2^{1/3}) + 1/9" absorbs the r = 1 and r ≥ 2 terms; the chain is
  correct but terse (we verified numerically and via the stated inequality).

## Recommended actions (pending Edwin's go)

1. Post this verdict + the 196 new pairs to the erdosproblems.com 730
   thread (crediting Liam Price / GPT-5.5 Pro's paper, and Tomodovodoo's
   provenance note).
2. Update the AI-contributions wiki row for 730: ⚪ → ✅ (verified).
3. Offer the new pairs to OEIS A129515 (b-file extension).
4. Optional: formalize Lemma 2.1 in Lean (the criterion is
   finite-combinatorial and would make the pairs machine-checkable
   end-to-end).
