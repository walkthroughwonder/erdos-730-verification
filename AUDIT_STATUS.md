# Erdős #730 audit — status after day one (2026-07-27)

## Everything finitely checkable has now been verified ✓

| Item | Method | Result |
|---|---|---|
| Lemma 2.1 (transition criterion) | hand proof of both digit-sum branches + exhaustive machine check n < 1200 vs direct radical computation | **0 mismatches** |
| Cross-validation | equal-radical n found = 87, 199, 237, 467, 607, 967, 1127 | **exactly matches OEIS A129515's first seven terms** |
| Construction identities (4), coprimality, exactly-one-branch | hand algebra + mod arithmetic | ✓ |
| Large-prime residue table & branch eliminations | enumeration (N2) | ✓ P:{3,5,6}/c≡3,4(7); Q,S: none; R:{6,10,12}/c≡5,9(14) — verbatim as claimed |
| Constants C, Λ | 15-digit recomputation | ✓ C=0.123737624319819, Λ=0.957048617652572 < 1 |
| Final elementary chain e^{8/3} > 49621/3645 > 27/2 | direct | ✓ |
| The construction actually works | N3: x ≤ 400, full factorization of A=PQ, M=3RS, criterion tested prime-by-prime | **196/400 good (49% ≫ 4.3% bound)** |

## Byproduct: 196 explicit NEW consecutive equal-radical pairs

Each good x yields a proven pair (n_x, n_x+1) — proven by complete
factorization + Lemma 2.1 (which we proved by hand and validated
exhaustively). Smallest new: x=2, n = 338,381,863,522. Largest checked:
x=400, n ≈ 1.35×10^16. Previous known record: n = 10,005. These are
legitimate contributions to A129515/the 730 thread REGARDLESS of the
paper's analytic sections.

## Remaining before a verdict (the infinite parts)

- A4a: Lemma 3.2 line-by-line (completion, the s ≡ −h₀B step, Gauss-sum
  evaluation, harmonic bound). Standard shapes; must re-derive.
- A4b: §4 bookkeeping: small-prime block count, r_p grouping, Mertens
  uniformity at endpoints exp(cL^{2/3}), boundary/large-prime ranges.
- A6: read Tomodovodoo's "closing derivation" (ChatGPT share) — determine
  what it closes and whether the Overleaf already incorporates it.
- Statement fidelity vs FormalConjectures/ErdosProblems/730.lean.

## Honest current posture

No error found anywhere; every claim that CAN be checked by computation
or short hand-derivation has been checked and holds, including several
(residue table, constants, OEIS agreement, 49% empirical density) that
would have exposed a hollow proof instantly. The remaining risk is
concentrated in ~2 pages of standard-shape analytic argument (§3–§4).
Preliminary posture: leaning CONFIRM, verdict pending A4/A6.
