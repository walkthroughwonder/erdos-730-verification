/-
Erdős 730 — the transition criterion (Lemma 2.1 of the verified proof),
formalization started as part of the verification audit
(github.com/walkthroughwonder/erdos-730-verification).

STATUS: definitions + faithful statements; the two digit-sum lemmas and the
criterion carry `sorry` placeholders — this is the scaffold for a full
formalization, not a completed proof. The criterion itself was verified by
hand and machine-checked exhaustively for n < 1200 (0 mismatches).
-/
import Mathlib

open Nat

namespace Erdos730Audit

/-- `DigitsSmall p m`: every base-`p` digit of `m` is at most `(p-1)/2` —
the set `D_p` of the proof. -/
def DigitsSmall (p m : ℕ) : Prop :=
  ∀ d ∈ Nat.digits p m, d ≤ (p - 1) / 2

instance (p m : ℕ) : Decidable (DigitsSmall p m) := by
  unfold DigitsSmall; infer_instance

/-- Kummer's bridge (proof's equation (1)): for odd prime `p`,
`p` does not divide the central binomial `C(2m, m)` iff `m ∈ D_p`.
Follows from `Nat.Prime.multiplicity_choose` (carries characterization);
a digit `> (p-1)/2` at position `i` forces a carry at `i` and conversely. -/
theorem prime_not_dvd_centralBinom_iff_digitsSmall
    {p : ℕ} (hp : p.Prime) (hodd : p ≠ 2) (m : ℕ) :
    ¬ p ∣ m.centralBinom ↔ DigitsSmall p m := by
  sorry

/-- The transition criterion (Lemma 2.1). With `A = n+1`, `M = 2n+1`:
the central binomials at `n` and `n+1` have the same prime support iff for
every odd prime `p`, (2) `p^a ∥ A → ¬DigitsSmall p (A / p^a)` and
(3) `p^a ∥ M → ¬DigitsSmall p ((M / p^a - 1) / 2)`. -/
theorem transition_criterion (n : ℕ) (hn : 1 ≤ n) :
    (n.centralBinom.primeFactors = (n + 1).centralBinom.primeFactors) ↔
    (∀ p : ℕ, p.Prime → p ≠ 2 →
      (∀ a : ℕ, p ^ a ∣ (n + 1) → ¬ p ^ (a + 1) ∣ (n + 1) → 1 ≤ a →
        ¬ DigitsSmall p ((n + 1) / p ^ a)) ∧
      (∀ a : ℕ, p ^ a ∣ (2 * n + 1) → ¬ p ^ (a + 1) ∣ (2 * n + 1) → 1 ≤ a →
        ¬ DigitsSmall p (((2 * n + 1) / p ^ a - 1) / 2))) := by
  sorry

/-- Machine-checkable instance of the criterion at n = 87 (the classical
(87, 88) pair). Since `88 = 2^3 * 11` and `175 = 5^2 * 7`, the only
non-vacuous conditions are the three below: condition (2) at p = 11
(with `88 / 11 = 8`) and condition (3) at p = 5 (`(175/25 - 1)/2 = 3`)
and p = 7 (`(175/7 - 1)/2 = 12`). Each quotient has a base-p digit
exceeding `(p-1)/2`, so all conditions hold. -/
example : (88 = 2 ^ 3 * 11 ∧ 175 = 5 ^ 2 * 7) ∧
    ¬ DigitsSmall 11 8 ∧ ¬ DigitsSmall 5 3 ∧ ¬ DigitsSmall 7 12 := by
  refine ⟨by norm_num, ?_, ?_, ?_⟩ <;> decide +kernel

end Erdos730Audit
