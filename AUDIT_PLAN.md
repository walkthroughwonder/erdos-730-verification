# Erdős #730 — verification audit (kickoff 2026-07-27)

**Problem.** Are there infinitely many pairs n ≠ m with rad-equal central
binomials: C(2n,n) and C(2m,m) having the same set of prime divisors?
(EGRS 1975; Erdős–Graham–Ruzsa–Straus believed "no doubt" yes; known pairs
(87,88), (607,608), (10003,10004,10005); OEIS A129515.)

**Candidate.** "Equal Radicals of Consecutive Central Binomial
Coefficients" — GPT-5.5 Pro via Liam Price (Leeham), posted 24 Jun 2026,
⚪ unverified a month later. Claims the STRONG form: infinitely many
consecutive pairs (n, n+1).

**Artifacts.**
- Overleaf (read): https://www.overleaf.com/read/gpttrsmhbhbk
  (project id 6a3c240f2713eba67ec93405, single main.tex)
- Closing derivation addendum (Tomodovodoo, 25 Jun):
  https://chatgpt.com/share/6a3c7e81-cab8-83eb-a247-cd10b62e80fb
- Forum thread: https://www.erdosproblems.com/forum/thread/730
- Formal statement (for statement-fidelity check):
  FormalConjectures/ErdosProblems/730.lean (google-deepmind repo)

**Document structure** (from the Overleaf outline):
1. Introduction
2. The transition criterion and the algebraic family
3. Construction of the family
4. A quadratic restricted-digit estimate
5. Counting transition obstructions

**Known mechanism sketch** (from the forum post): primes p dividing
C(2n,n) vs C(2n+2,n+1); transition governed by p | (n+1)(2n+1) behavior;
construction imposes n+1 = PQ, 2n+1 = 3RS with P,Q,R,S prime-ish;
a density/counting argument (4^{-r} terms — Kummer/base-p digit flavor)
shows infinitely many n avoid all "transition obstructions."

**Audit plan.**
- A1: read the full main.tex (scroll-capture from the Overleaf editor in
  the browser; no download without Edwin's ok).
- A2: verify the transition criterion (which primes enter/leave the
  radical between n and n+1) — this is Kummer's theorem territory; check
  independently.
- A3: verify the algebraic family construction and its compatibility
  (CRT solvability, infinitude of candidates).
- A4: THE LIKELY CRUX: the "quadratic restricted-digit estimate" and the
  obstruction count — sieve/counting arguments are where the 10 refuted
  AI proofs died. Check constants, uniformity, and whether the estimate
  is actually strong enough for the final union bound.
- A5: numerically sanity-check the criterion and (if the construction is
  explicit) hunt a concrete new consecutive pair predicted by it.
- A6: read Tomodovodoo's closing derivation; determine if the original
  had a gap it patches, and whether the patch holds.
- Verdict memo -> forum/wiki (with Edwin's go before posting).

**Discipline.** Same as always: independent verification (our own
derivations, not proofreading vibes); numerics before trust; the
verdict can be CONFIRMED, GAP (localized), or REFUTED (with witness).
