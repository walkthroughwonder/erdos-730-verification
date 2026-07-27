# Draft forum post for erdosproblems.com thread 730
(post under Edwin's account after his login; AI disclosure included)

---

**Verification report: the GPT-5.5 Pro proof is correct.** (AI-assisted
audit, disclosed: Claude/Anthropic throughout.)

We have completed an independent line-by-line verification of the proof
posted by Liam Price on 24 June ("Equal Radicals of Consecutive Central
Binomial Coefficients"), and our verdict is **confirmed**. Full auditor's
report, methodology, and reproduction code:
https://github.com/walkthroughwonder/erdos-730-verification

What was checked: the transition criterion (Lemma 2.1) was re-proved by
hand and machine-checked exhaustively for all `n < 1200` against direct
radical computation (zero mismatches — and the resulting equal-radical
list 87, 199, 237, 467, 607, 967, 1127 matches A129515 exactly); all
algebraic identities, the large-prime residue table, and the constants
were verified by independent computation; and the analytic sections (the
restricted-digit Fourier lemma, the incomplete quadratic sums, and the
Section 4 first-moment bookkeeping, including the Mertens uniformity at
the endpoints `exp(c (log X)^{2/3})`) were re-derived line by line. We
found no gaps. Tomodovodoo's addendum is a provenance analysis (it
explains where the coefficients came from); its independent re-derivations
of the four `Phi_L` agree with the paper.

As an empirical bonus: running the construction for `x <= 400` (with
complete factorizations of `n+1 = PQ` and `2n+1 = 3RS`) yields **196
explicit new consecutive equal-radical pairs** — observed density 49%,
comfortably above the guaranteed `1 - Lambda ≈ 4.3%`. The smallest is

    n = 338381863522,  (x = 2)

i.e. rad C(2n, n) = rad C(2n+2, n+1), far beyond the previously known
n = 10005. The full list and a verifier script are in the repository. A
Lean formalization of Lemma 2.1 has been scaffolded there as well.

Congratulations to Liam and GPT-5.5 Pro — the answer to this problem is
yes, and consecutively so.
