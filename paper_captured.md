# Captured text: "Equal Radicals of Consecutive Central Binomial Coefficients" (GPT Pro, June 24, 2026)

Source: Overleaf read/gpttrsmhbhbk, PDF text layer, captured 2026-07-27.
Complete through the end ("Theorem 1.1 follows."). Math notation
reconstructed from the text layer; verify against the PDF for display
equations if a dispute arises.

## Abstract
Infinitely many consecutive central binomials share prime support.
Explicit quadratic sequence n_x; positive lower density of x with
rad C(2n_x,n_x) = rad C(2n_x+2,n_x+1). Kummer + algebraic factorisation +
finite restricted-digit estimate for quadratic polynomials mod prime
powers; first-moment calculation.

## §1
T := 3·41·43 = 5289; n_x := (42Tx+11)(72Tx+13) − 1.
C := Σ_{r≥1} 4^{-r} log((r+2)/(r+1)); Λ := 4C + (2/3) log 2.
THEOREM 1.1: Λ < 1 and liminf_X (1/X) #{x ≤ X : rad B_{n_x} = rad B_{n_x+1}}
≥ 1 − Λ > 0. Numerically C = 0.123737624319818, Λ = 0.957048617652571.

## §2
B_m := C(2m,m). D_p := nonneg integers with all base-p digits ≤ (p−1)/2.
Kummer: v_p(B_m) = #carries in m+m base p; so p ∤ B_m ⟺ m ∈ D_p.  (1)

LEMMA 2.1 (Transition criterion). n ≥ 1, A := n+1, M := 2n+1. Then
rad B_n = rad B_{n+1} iff for every odd prime p:
  (2) p^a ∥ A ⟹ A/p^a ∉ D_p;
  (3) p^a ∥ M ⟹ (M/p^a − 1)/2 ∉ D_p.
Proof: B_{n+1}/B_n = 2M/A, (A,M) = 1. A-branch: A = p^a u, digit sums give
v_p(B_n) = a + v_p(B_u), v_p(B_{n+1}) = v_p(B_n) − a; p disappears iff
u ∈ D_p. M-branch: M = p^a u, w := (u−1)/2, n = p^a w + (p^a −1)/2; lowest
a digits of n are (p−1)/2, doubling gives no carries: v_p(B_n) = v_p(B_w),
v_p(B_{n+1}) = v_p(B_n) + a; p newly introduced iff w ∈ D_p. Prime 2
divides every B_m, no condition. □

## §2.1 Construction
Seek n+1 = PQ, 2n+1 = 2PQ−1 = 3RS. Identity (2P−a)(Q+b) = 2PQ + (2bP−aQ) − ab;
relation 2bP − aQ = ab−1 gives 2PQ−1 = (2P−a)(Q+b). Choose a=7, b=6
(ab−1 = 41, ab+1 = 43 prime). Then 12P − 7Q = 41; 3R = 2P−7, S = Q+6;
18R − 7S = −43. (P,Q) | 41, (R,S) | 43. Parametrize: P = 4+7t, Q = 1+12t;
R integral needs t ≡ 1 (mod 3); t = 1+3u: P = 11+21u, Q = 13+36u, R = 5+14u,
S = 19+36u; u = 2v for oddness: P = 42v+11, Q = 72v+13, R = 28v+5, S = 72v+19.
Local: impose v ≡ 0 mod 3, 41, 43 (then (P,Q,R,S) ≡ (2,1,2,1) mod 3,
(P,Q) ≡ (11,13) mod 41, (R,S) ≡ (5,19) mod 43) ⟹ v = Tx.
FINAL FORMS: P := 42Tx+11, Q := 72Tx+13, R := 28Tx+5, S := 72Tx+19.
(4): 2PQ−1 = 3RS, 12P−7Q = 41, 18R−7S = −43. (P,Q) = (R,S) = 1;
(PQ, 3RS) = 1; 3 ∤ PQRS. Every odd prime ≠ 3 divides exactly one of P,Q,R,S.

Remark 2.2: Q,S branches have lowest base-p digit ~ 7p/12 (auto-excluded);
P,R branches confined to 2 of 6 reduced classes. Prime 3: R ≡ 2, S ≡ 1
(mod 3), 3 ∥ M, (RS−1)/2 ≡ 2 (mod 3) ∉ D_3 ⟹ (3) holds always.

Obstruction polynomials (a = v_p exponent, c = L/p^a):
(5) Φ_P(c) = (12 p^a c² − 41c)/7,  Φ_Q(c) = (7 p^a c² + 41c)/12,
(6) Φ_R(c) = (54 p^a c² + 129c − 7)/14,  Φ_S(c) = (7 p^a c² − 43c − 6)/12.
Obstruction ⟺ Φ_L(c) ∈ D_p. Slopes λ_P = 42T, λ_Q = 72T, λ_R = 28T,
λ_S = 72T; p ∤ λ_L when p^a | L(x). x = x₀ + p^a k, c = c₀ + λ_L k:
(7) Φ_L(c₀ + λ_L k) = 3024 T² p^a k² + (p^a u_L + b_L) k + v_L,
(8) b_P = −246T, b_Q = 246T, b_R = 258T, b_S = −258T;
(u_P,u_Q,u_R,u_S) = (144Tc₀, 84Tc₀, 216Tc₀, 84Tc₀). Prime divisors of b_L
lie in {2,3,41,43}; constant terms 11,13,5,19 nonzero mod those ⟹
(9) v_p(Φ_L(k₁) − Φ_L(k₂)) = v_p(k₁ − k₂): polynomial permutes Z/p^j ∀j.

## §3
H := (p+1)/2; D_{p,m} := {Σ_{j<m} d_j p^j : 0 ≤ d_j < H} ⊆ Z/p^m Z.
e(z) := exp(2πiz); unnormalised FT on Z/qZ.

LEMMA 3.1: ∃ absolute C₀: (1/p^m) Σ_{h mod p^m} |1̂_{D_{p,m}}(h)| ≤ (C₀ log p)^m.
Proof: S_H(θ) := Σ_{d<H} e(dθ); |S_H| ≤ min(H, 1/(2∥θ∥));
(10) (1/p) Σ_a |S_H(a/p + δ)| ≪ log p (1/p-spaced points, harmonic sum).
D_{p,m} = d + p·D_{p,m−1}: 1̂_{D_{p,m}}(h) = S_H(−h/p^m) 1̂_{D_{p,m−1}}(h mod p^{m−1});
h = b + a p^{m−1}, average over a, induct. □

LEMMA 3.2 (Incomplete quadratic sums): p odd, r ≥ 1,
G(k) = pAk² + Bk + C, p ∤ AB. I interval of p^r consecutive integers,
h ≢ 0 mod p^{2r}: Σ_{k∈I} e(hG(k)/p^{2r}) = 0 for v_p(h) ≥ r;
≪ r p^{r−1/2} log p for v_p(h) < r. Absolute constant.
Proof: v := v_p(h), h = p^v h₀, M := p^{2r−v}. G(k₁) − G(k₂) =
(k₁−k₂)(pA(k₁+k₂) + B); second factor p-adic unit ⟹ G permutes Z/MZ.
v ≥ r: M | p^r, I = union of complete systems mod M ⟹ 0.
v < r: M = pQ, Q = p^{2r−v−1} ≥ p^r. Completion (11):
Σ_{k∈I} = (1/M) Σ_s 1̂_I(s) Σ_y e((h₀G(y) + sy)/M). Inner sum: group y by
residue mod Q; translation by Q ⟹ vanishes unless s ≡ −h₀B (mod p)
[nonzero class mod p]. Then h₀B + s = pb; inner sum = p·|Σ_{y mod Q}
e((h₀Ay² + by)/Q)| = p√Q [Gauss: |Σ e((ay²+by)/Q)|² = Q for p ∤ a, odd
Q = p^j]. 1̂_I(s) ≤ min(N, M/(2|s|_M)), N = p^r; on the fixed class mod p:
Σ 1̂_I ≪ N + Q log M ≪ Q log M. Total ≪ √Q log M; Q ≤ p^{2r−1},
log M ≤ 2r log p. □

PROP 3.3: ∃ absolute C₁: p odd, r ≥ 1, G as above, I interval of p^r:
(12) #{k ∈ I : G(k) mod p^{2r} ∈ D_{p,2r}} = p^r (H/p)^{2r}
+ O(p^{r−1/2} (C₁ log p)^{2r+1}). For fixed r: proportion = 4^{-r} + o_r(1).
Proof: Fourier inversion mod q = p^{2r}; h=0 term p^r(H/p)^{2r}; v_p(h) ≥ r
frequencies vanish (L3.2); others ≪ r p^{r−1/2} log p; total Fourier weight
(C₀ log p)^{2r} (L3.1). □

## §4
Mertens (13) Σ_{p≤x} 1/p = log log x + B + o(1);
(14) Σ_{p≤x, p≡a(q)} 1/p = (1/φ(q)) log log x + B(q,a) + o(1), (a,q)=1
fixed. Chebyshev π(x) ≪ x/log x.
E(x) := # odd primes failing Lemma 2.1 for n = n_x. Prime 3 contributes
never; each contribution attached to exactly one of P,Q,R,S.
1_{E≥1} ≤ E(x); ENOUGH: (15) Σ_{x≤X} E(x) ≤ (Λ + o(1)) X.
L := log X, Y := exp(L^{2/3}).

SMALL PRIMES & REPEATED LARGE: branch L₀, p ≤ Y, a ≥ 1: solutions of
p^a | L₀(x) = one class mod p^a; k-interval length K = Xp^{-a} + O(1).
If p^a ≤ X^{1/2}: j := ⌊log K / (2 log p)⌋. p^a | L₀(x), x ≤ X ⟹ p^a ≤
C_{L₀} X (a ≪ log X/log p). By (9) branch polynomial permutes mod p^j:
obstruction ⟹ ≤ (K/p^j + 1) H^j ≪ K exp(−c log K/log p) + √K
possibilities (all relevant p ≥ 5). Uniformly p ≤ Y, p^a ≤ X^{1/2}:
factor ≤ exp(−c' L^{1/3}). Σ_{p≤Y, a} with Σ p^{-a/2} ≪ √Y:
≪ X e^{−c'L^{1/3}} log log Y + √(XY) + Y log X = o(X).
If p^a > X^{1/2}: #{x} ≤ X/p^a + 1; geometric tails + O(log X) exponents:
≪ X^{1/2} π(Y) + π(Y) log X = o(X).
p > Y with a ≥ 2: p² | L₀(x), L₀(x) ≪ X ⟹ p ≪ X^{1/2}:
Σ (X/p² + 1) ≪ X/Y + X^{1/2} = o(X).

MAIN RANGE Y < p ≤ X^{1/2}/log X, first power. N_{L₀}(p;X) := #{x ≤ X :
p ∥ L₀(x), Φ_{L₀}(L₀(x)/p) ∈ D_p} (a = 1). Unique class x₀ mod p;
x = x₀ + pk; K_p = X/p + O(1); r_p := max r with p^{r_p} ≤ K_p; partition
into blocks of length p^{r_p} + remainder. For p > Y the polynomial (7) has
the form required by P3.3 (p > Y excludes fixed-coefficient primes);
dropping p ∥ (vs p |) only enlarges. Global obstruction forces lowest 2r_p
digits restricted. Per block:
(16) N_{L₀}(p;X) ≤ K_p ((p+1)/(2p))^{2r_p} + O(K_p η_{p,r_p} + p^{r_p}),
η_{p,r} := p^{-1/2}(C₁ log p)^{2r+1}.
r_p ≤ L/log p + O(1) ≤ 2L^{1/3}; log η ≤ −(1/2)L^{2/3} + O(L^{1/3} log L)
⟹ sup η = o((log X)^{-A}) ∀A. Σ K_p η ≪ sup η (X Σ_{p≤X^{1/2}} 1/p +
π(X^{1/2})) = o(X). Remainders: group by r_p = r: p^{r+1} ≤ 2X,
Z := (2X)^{1/(r+1)}: Σ p^r ≤ Z^r π(Z) ≪ (r+1) X/log X; Σ_{r ≤ 2L^{1/3}}
≪ X L^{-1/3} = o(X). Main term: K_p → X/p costs O(π(X^{1/2})) = o(X);
((p+1)/2p)^{2r_p} = 4^{-r_p}(1+o(1)). If r_p = r: (X/2)^{1/(r+2)} < p ≤
(2X)^{1/(r+1)}; Mertens: Σ_{r_p = r} 1/p ≤ log((r+2)/(r+1)) + o(1),
uniformly (endpoints ≥ exp(cL^{2/3})); enlarged-interval mass ≤ log(3/2)
+ o(1) uniformly; tail r > R: ≪ Σ_{r>R} 4^{-r}. X→∞ then R→∞:
Σ_{Y<p≤X^{1/2}/log X} 4^{-r_p}/p ≤ C + o(1).
(17) per branch: Σ N_{L₀}(p;X) ≤ (C + o(1)) X. Four branches: (4C+o(1))X.

BOUNDARY X^{1/2}/log X < p ≤ X^{1/2+ε}: trivial X/p + 1:
(18) ≪ O(εX) + o(X).

LARGE p > X^{1/2+ε}, first power: c = L₀(x)/p; c/p ≪ X/p² ≪ X^{-2ε} = o(1).
Φ(c) = (αpc² + βc + γ)/d. Write αc² = dq + s, 0 ≤ s < d:
Φ(c) = pq + t, t = (sp + βc + γ)/d integer; t/p = s/d + o(1). All possible
s/d ∈ [3/7, 6/7]; for large X, 0 < t < p, so t IS the lowest base-p digit.
Obstruction needs t ≤ (p−1)/2; s/d ≠ 1/2 ⟹ necessary: s/d < 1/2.
Residue table: branch P: d=7, αc² mod d ∈ {3,5,6}, necessary classes
c ≡ 3,4 (mod 7); Q: d=12, αc² ≡ 7, none; R: d=14, ∈ {6,10,12}, c ≡ 5,9
(mod 14); S: d=12, ≡ 7, none. For P: pc ≡ P ≡ 4 (mod 7) ⟹ p ≡ 1,6
(mod 7). For R: pc ≡ R ≡ 5 (mod 14) ⟹ p ≡ 1,13 (mod 14). Two branches
survive, two of six reduced classes each; p ≤ C_{L₀}X;
by (14): each branch ≤ (−(1/3) log(1/2+ε) + o(1)) X; O(1)-term O(X/log X).
Both branches, X→∞, ε↓0:
(19) (2/3 log 2 + o(1)) X.

(17)+(18)+(19)+negligible ⟹ (15). Λ < 1: r=1 term + log(1+u) < u:
Λ < log(3/2) + (2/3)log 2 + 4Σ_{r≥2} 4^{-r}/(r+1) ≤ log(3/2^{1/3}) + 1/9 hmm
[paper: ≤ log(3·2^{1/3}/2?) — displayed: log(3/2^{1/3}) + 1/9]; final:
e^{8/3} > 49621/3645 > 27/2 ⟹ log(3/2^{1/3}) < 8/9 ⟹ Λ < 1.
#{x ≤ X : E(x) ≥ 1} ≤ Σ E(x). Theorem 1.1 follows. ∎ [end of paper]
