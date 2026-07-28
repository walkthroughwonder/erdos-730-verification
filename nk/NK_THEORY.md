# The (n, n+k) equal-radical question — theory notes

*Question (M. Firsching, thread 730, Sept 2025 / renewed June 2026): for
every k ≥ 1, are there pairs (n, n+k) with
rad C(2n,n) = rad C(2n+2k, n+k)? Infinitely many for each k?*

Status of knowledge: k = 1 — infinitely many (the verified 730 proof).
k = 2 — examples exist ((10003, 10005)). General k — open.

Write B_m = C(2m,m), and D_p = {m : all base-p digits ≤ (p−1)/2}
(Kummer: p ∤ B_m ⟺ m ∈ D_p, for odd p).

## Lemma A (localization)

For every odd prime p not dividing any of the 2k bridge numbers
n+1, …, n+k, 2n+1, 2n+3, …, 2n+2k−1, one has v_p(B_{n+k}) = v_p(B_n).

*Proof.* B_{n+k}/B_n = 2^k · ∏_{j=1}^k (2n+2j−1) / ∏_{j=1}^k (n+j)
(telescoping B_{m+1}/B_m = 2(2m+1)/(m+1)). If p divides neither
numerator-odd-parts nor denominator factors, the p-valuation of the ratio
is 0. ∎

Consequently rad B_n = rad B_{n+k} ⟺ for every odd prime p dividing a
bridge number, (n ∈ D_p ⟺ n+k ∈ D_p). This makes testing a pair O(k)
factorizations of numbers ≤ 2n+2k.

## Lemma B (prime-gap obstruction)

If some prime q lies in (2n, 2n+2k], then rad B_n ≠ rad B_{n+k}.
Hence every valid pair requires the interval (2n, 2n+2k] to be
**prime-free**, and for fixed k the density of admissible n is governed by
prime gaps ≥ 2k+1 at 2n (positive density for every fixed k, by standard
sieve results — e.g. the gap-distribution consequences of
Gallagher/Westzynthius-type results; for our purposes even the elementary
fact that a positive proportion of intervals (2n, 2n+2k] are prime-free
for each fixed k suffices, which follows from the second-moment method).

*Proof.* q > 2n ⟹ q ∤ B_n (all prime factors of B_n are ≤ 2n).
q ≤ 2(n+k) and q odd (q > 2n ≥ 2): q | B_{n+k} ⟺ n+k ∉ D_q. In base q,
n+k is a single digit (n+k < q would need q > n+k; since q > 2n ≥ n+k for
n ≥ k, indeed n+k < q); the digit condition n+k ≤ (q−1)/2 would force
q ≥ 2(n+k)+1, contradicting q ≤ 2(n+k). So n+k ∉ D_q and q | B_{n+k}. ∎

Remark: for k = 1 this is precisely why the 730 construction makes
2n+1 = 3RS composite. For general k it couples the question to prime
gaps — an obstruction that is provably surmountable for every fixed k
(gaps of any fixed size occur with positive density), so it does NOT
block a "for every k" theorem; it only prices it.

## The k = 2 case, concretely

Bridge numbers: n+1, n+2, 2n+1, 2n+3. Conditions: for each odd p dividing
one of these, n ∈ D_p ⟺ n+2 ∈ D_p; plus 2n+1, 2n+3 both composite.
Parity note: n and n+2 share the last base-2 digit — vacuous (p = 2
excluded); for p = 3: n vs n+2 mod 3 differ unless carry structure —
handled by the general digit test.

A 730-style construction template for k = 2 would seek four simultaneous
factorizations with linear forms:
  n+1 = P₁Q₁, n+2 = P₂Q₂ (or one of them smooth-controlled),
  2n+1 = c₁·R₁S₁, 2n+3 = c₂·R₂S₂,
with digit-obstruction guarantees on each cofactor branch. The identity
engine from the 730 provenance analysis (coefficient matching
2·A·C = H·E·G etc.) generalizes: we need a PAIR of "2PQ−1 = 3RS"-type
identities holding at offset 2, i.e. a single parameter t making
  2·P₁(t)Q₁(t) − 1 = 3·R₁(t)S₁(t)  and  2·P₁(t)Q₁(t) + 1 = c·R₂(t)S₂(t)
(with n+2 = P₂Q₂ handled analogously). Whether the coefficient-matching
system for BOTH offsets simultaneously has integer solutions is exactly
the computational-algebra search to run (SAT/CP or enumeration — the 712
toolchain applies).

## Program

- S1 (running): scan n ≤ 2·10^5, k ≤ 16 — which k have small examples?
  Expected: density decreasing in k (prime-gap price × digit price
  ~4^{−ω}-ish); the data calibrates both.
- S2: for k lacking examples, extend scan (SPF sieve scales to ~10^7).
- S3: build the two-offset coefficient-matching engine; search identity
  systems for k = 2, 3 explicitly.
- S4: the theorem target — "for every fixed k there exist (infinitely
  many) pairs (n, n+k)": combine a k-fold construction with the 730
  counting method, or find a softer argument (e.g. for EVEN k, note
  (n, n+1) and (n+1, n+2) pairs compose: two overlapping k=1 pairs give a
  k=2 pair via transitivity! rad B_n = rad B_{n+1} = rad B_{n+2}. The
  triple (10003, 10004, 10005) is exactly this. So k = 2 REDUCES to
  consecutive TRIPLES — does the verified k=1 construction produce
  triples? The criterion at n and n+1 simultaneously — a second-moment
  question over the same family! CHECK THE 196 PAIRS FOR ADJACENT x's
  giving triples... no — triples need n AND n+1 both good, i.e.
  consecutive INTEGERS not consecutive x. Test directly: for good x, is
  n_x + 1 also the start of a good pair? n_x+1 has its own A, M — not in
  the family. But the SCAN will reveal triples at small n if any.)
- S5: transitivity structure generally: pairs at k₁ and k₂ with shared
  endpoint compose to k₁+k₂. So "every k" would follow from e.g.
  "arbitrarily long equal-radical RUNS" (strong!) or from per-k
  constructions. Runs of length 3 = A129515-triples: known example exists
  (10003–10005). Are runs of every length plausible? Heuristic density of
  a run of length L ~ product of L−1 dependent 4%-ish events — rare but
  nothing forbids; worth its own scan (S1 detects runs automatically as
  k=1 pairs at consecutive n).

## Empirical findings (2026-07-27 scans)

- n ≤ 2×10^5, k ≤ 16: k=1: 1830 pairs; k=2: 11 pairs; k ≥ 3: none.
- **Every k=2 pair in range is triple-transitive** (a run n, n+1, n+2):
  zero direct k=2 pairs found. Explanation: a direct pair needs a prime
  to exit at one step and re-enter at the next — a coincidence of
  coincidences, rarer than two clean transitions. (NB: the 730 thread
  cites Moritz's kummer repo for direct (n, n+2) examples with failing
  intermediates — reconcile; presumably larger than 2×10^5.)
- Run hunt to n = 3×10^6: 30,780 k=1 pairs (density ≈ 1.03%, stable);
  ~180 triples (ONLY ONE previously known: 10003); ZERO quadruples —
  consistent with quasi-independence (expected λ ≈ 2, P(none) ≈ 14%).
  First quadruple predicted within n ≲ 10^7–10^8.
- Run hunt to n = 10^7 (2026-07-27): 73,760 k=1 pairs; 557 triples;
  **FIVE QUADRUPLES** — runs of four consecutive equal-radical values at
  n = 3894942, 4505065, 6218569, 7506679, 8879450 (starts corrected for a
  reporting off-by-one that was caught by independent brute-force
  verification — the flagship quadruple 3894942..3894945 is confirmed by
  full support comparison over all odd primes ≤ 2(n+3), ~3.6×10^5 primes).
  Hence the **first known (n, n+3) pairs**, e.g. (3894942, 3894945),
  answering the existence part of the k = 3 question. First quintuple
  (⟹ (n, n+4)) predicted around n ~ 10^9±1 — beyond this scanner;
  needs optimized sieving (PARI/C or the criterion in compiled form).
- Emerging conjecture (weak): for every L, runs of length L exist
  (density ~ ρ^{L-1} with ρ ≈ 0.01, modulated by the shared-bridge
  correlations); hence (n, n+k) pairs for every k via transitivity.
  The k-fold simultaneous version of the 730 construction is the
  plausible proof route for fixed small k.

## Lemma C (four-squares obstruction for naive triple constructions)

Seek a 730-style family for TRIPLES: one quadratic F(t) = n+1 with
F = P₁Q₁, 2F−1 = R₁S₁, F+1 = P₂Q₂, 2F+1 = R₂S₂, all factors linear in t.
A quadratic with integer coefficients splits into rational linear forms
iff its discriminant is a perfect square. With F = αt² + βt + γ and
D₀ = β² − 4αγ, the four discriminant conditions are (up to the uniform
factor 4 on the doubled ones):
  disc(F) → D₀,   disc(2F−1) → D₀ + 2α,
  disc(F+1) → D₀ − 4α,   disc(2F+1) → D₀ − 2α.
These are FOUR SQUARES IN ARITHMETIC PROGRESSION (common difference 2α),
impossible for α ≠ 0 by Euler–Fermat. **Hence no constant-free
linear-splitting family can produce triples.**

**Correction (same evening).** A first draft claimed constant multipliers
h relax the conditions; they do not: disc(h·R·S) = h²·(integer)² is still
a perfect square, so all four splitting conditions are genuinely
"perfect square" and the Euler–Fermat obstruction applies WITH OR WITHOUT
constants. (An automated search over α ≤ 2×10⁴ with multiplier tuples
returned zero systems — an empirical confirmation of Fermat, as it must
be.) Hence the strengthened statement:

**Lemma C′.** No 730-type construction based on a single quadratic
F = n+1 can have all four of F, 2F−1, F+1, 2F+1 split into linear forms.
At most THREE of the four can split, since three squares in AP with
common difference 2α do exist (classically parametrized via
u² + w² = 2v²), e.g. the configuration splitting F, 2F−1, 2F+1
(conditions D₀−2α, D₀, D₀+2α squares) and leaving F+1 IRREDUCIBLE.

**The real route to a triple/k=2 theorem** is therefore hybrid:
engineer three of the four transitions' quadratics as in the 730 proof,
and handle the leftover irreducible quadratic (n+2 = F(t)+1) by the
ANALYTIC method — its per-prime local analysis is exactly Prop 3.3
(restricted digits for quadratic polynomials mod p^{2r}, already proved
for irreducible G!), with the global bookkeeping now over prime divisors
of an irreducible quadratic's values (Chebotarev-flavored densities in
place of linear-form Mertens). Concrete next steps:
1. ~~Parametrize 3-squares-in-AP triples~~ DONE, and it is clean:
   writing the three discriminant squares as s₂² , e², s₁² (gaps 2α),
   the system s₁²+s₂² = 2e² is solved by s₁ = m+n, s₂ = m−n with
   m² + n² = e² — **Pythagorean triples** — and then α = mn. The
   smallest triple (3,4,5) yields the first concrete hybrid family:
       n+1  = (3t+1)(4t+3)
       2n+1 = (4t+1)(6t+5)
       2n+3 = (2t+1)(12t+7)
       n+2  = 12t² + 13t + 4   (disc = −23 < 0: irreducible, positive)
   with all six forms odd for even t. EMPIRICS (t ≤ 4000, even):
   first-transition success 146/2000 = 7.3% (≈7× ambient k=1 density);
   ONE FULL TRIPLE already at t = 2490, n = 74,433,572 (brute-force confirmed: full support comparison over all odd primes to 2(n+2)) — family triple
   rate ≈ 5×10⁻⁴ per member ≈ 8× ambient, with the n+2 branch entirely
   unengineered. The construction manufactures triples.
2. For surviving families, develop the first-moment count with the
   fourth branch quadratic irreducible: the new ingredient is
   Σ_p (obstruction density at p) over p | values of an irreducible
   quadratic — needs the analogue of (17) with the density of
   {p : p | F(t)+1 solvable} ~ Chebotarev 1/2-ish weights. Target:
   total constant Λ₃ < 1. If the constant fails, enlarge the engineered
   side (split MORE structure off F+1, e.g. force a fixed prime factor).

## Honest difficulty assessment

k = 2 via triples looks GENUINELY ATTACKABLE (one known example; the 730
machinery already controls one transition; controlling two simultaneous
transitions doubles the branch bookkeeping but the method plausibly
survives). "Every k" is a real theorem-sized target. The scan data will
tell us where the wall is.
