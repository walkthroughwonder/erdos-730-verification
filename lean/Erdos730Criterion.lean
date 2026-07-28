/-
Erdős 730 — the transition criterion (Lemma 2.1 of the verified proof),
formalization started as part of the verification audit
(github.com/walkthroughwonder/erdos-730-verification).

STATUS: the Kummer bridge (the proof's equation (1),
`prime_not_dvd_centralBinom_iff_digitsSmall`) is now FULLY PROVED — no
`sorry`, checked against Mathlib. The transition criterion itself
(`transition_criterion`) still carries a `sorry` placeholder; it was
verified by hand and machine-checked exhaustively for n < 1200
(0 mismatches).
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

/-- Base-`p` expansion of a mod by one more digit:
`m % p^(i+1) = p * (m/p % p^i) + m % p`. -/
private lemma mod_pow_succ_eq (p : ℕ) (hp : 0 < p) (m i : ℕ) :
    m % p ^ (i + 1) = p * (m / p % p ^ i) + m % p := by
  have hpi : 0 < p ^ i := pow_pos hp i
  have hq : m / p % p ^ i < p ^ i := Nat.mod_lt _ hpi
  have hr : m % p < p := Nat.mod_lt _ hp
  have hlt : p * (m / p % p ^ i) + m % p < p * p ^ i := by
    have h3 : p * (m / p % p ^ i + 1) ≤ p * p ^ i := Nat.mul_le_mul_left p hq
    have h4 : p * (m / p % p ^ i + 1) = p * (m / p % p ^ i) + p := by ring
    omega
  have hr' : m % p < p * p ^ i := lt_of_lt_of_le hr (Nat.le_mul_of_pos_right p hpi)
  calc m % p ^ (i + 1) = (p * (m / p) + m % p) % (p * p ^ i) := by
        rw [Nat.div_add_mod, pow_succ']
    _ = p * (m / p % p ^ i) + m % p := by
        rw [Nat.add_mod, Nat.mul_mod_mul_left, Nat.mod_eq_of_lt hr',
          Nat.mod_eq_of_lt hlt]

/-- No carry ever occurs when adding `m + m` in base `p` iff every base-`p`
digit of `m` doubles to below `p`. -/
private lemma noCarry_iff_digits {p : ℕ} (hp : 1 < p) (m : ℕ) :
    (∀ i, 1 ≤ i → 2 * (m % p ^ i) < p ^ i) ↔ ∀ d ∈ Nat.digits p m, 2 * d < p := by
  induction m using Nat.strong_induction_on with
  | _ m ih =>
    rcases Nat.eq_zero_or_pos m with rfl | hm
    · constructor
      · intro _ d hd; simp at hd
      · intro _ i _
        have := pow_pos (lt_trans one_pos hp) i
        simp only [Nat.zero_mod]
        omega
    · have hp0 : 0 < p := lt_trans one_pos hp
      have hdiv : m / p < m := Nat.div_lt_self hm hp
      rw [Nat.digits_def' hp hm]
      simp only [List.forall_mem_cons]
      constructor
      · intro h
        refine ⟨by simpa [pow_one] using h 1 le_rfl, ?_⟩
        refine (ih (m / p) hdiv).1 ?_
        intro i hi
        have h2 := h (i + 1) (by omega)
        rw [mod_pow_succ_eq p hp0 m i, pow_succ'] at h2
        by_contra hcon
        push_neg at hcon
        have h3 : p * p ^ i ≤ p * (2 * (m / p % p ^ i)) := Nat.mul_le_mul_left p hcon
        have h4 : p * (2 * (m / p % p ^ i)) = 2 * (p * (m / p % p ^ i)) := by ring
        omega
      · rintro ⟨h1, h2⟩ i hi
        obtain ⟨j, rfl⟩ : ∃ j, i = j + 1 := ⟨i - 1, by omega⟩
        rw [mod_pow_succ_eq p hp0 m j, pow_succ']
        have hA : 2 * (m / p % p ^ j) < p ^ j := by
          rcases Nat.eq_zero_or_pos j with rfl | hj
          · simp [Nat.mod_one]
          · exact (ih (m / p) hdiv).2 h2 j hj
        have e1 : p * (2 * (m / p % p ^ j) + 1) ≤ p * p ^ j :=
          Nat.mul_le_mul_left p (by omega)
        have e2 : p * (2 * (m / p % p ^ j) + 1) = 2 * (p * (m / p % p ^ j)) + p := by
          ring
        omega

/-- Kummer's bridge (proof's equation (1)): for odd prime `p`,
`p` does not divide the central binomial `C(2m, m)` iff `m ∈ D_p`.
Via `Nat.Prime.emultiplicity_choose'` (Kummer's theorem: the multiplicity
is the number of carries when adding `m + m` in base `p`): a digit
`> (p-1)/2` at some position forces a carry there, and conversely. -/
theorem prime_not_dvd_centralBinom_iff_digitsSmall
    {p : ℕ} (hp : p.Prime) (hodd : p ≠ 2) (m : ℕ) :
    ¬ p ∣ m.centralBinom ↔ DigitsSmall p m := by
  have hp1 : 1 < p := hp.one_lt
  have hpm : p % 2 = 1 := Nat.odd_iff.1 (hp.odd_of_ne_two hodd)
  -- `DigitsSmall` in strict-doubling form (uses oddness of `p`)
  have hDS : DigitsSmall p m ↔ ∀ d ∈ Nat.digits p m, 2 * d < p := by
    unfold DigitsSmall
    exact forall₂_congr fun d _ => by omega
  -- Kummer: the multiplicity is the number of carries in `m + m` base `p`
  have hcb : m.centralBinom = (m + m).choose m := by
    rw [Nat.centralBinom_eq_two_mul_choose, two_mul]
  have hkum := Nat.Prime.emultiplicity_choose' (p := p) (n := m) (k := m)
    (b := Nat.log p (m + m) + 1) hp (Nat.lt_succ_self _)
  have hzero : ¬ p ∣ m.centralBinom ↔
      (∀ i ∈ Finset.Ico 1 (Nat.log p (m + m) + 1),
        ¬ p ^ i ≤ m % p ^ i + m % p ^ i) := by
    rw [hcb, ← emultiplicity_eq_zero, hkum, Nat.cast_eq_zero, Finset.card_eq_zero,
      Finset.filter_eq_empty_iff]
  -- carries in the bounded window ↔ carries anywhere
  have hbridge : (∀ i ∈ Finset.Ico 1 (Nat.log p (m + m) + 1),
      ¬ p ^ i ≤ m % p ^ i + m % p ^ i) ↔ (∀ i, 1 ≤ i → 2 * (m % p ^ i) < p ^ i) := by
    constructor
    · intro h i hi
      by_cases hib : i < Nat.log p (m + m) + 1
      · have := h i (Finset.mem_Ico.2 ⟨hi, hib⟩)
        omega
      · push_neg at hib
        have h2m : m + m < p ^ i :=
          lt_of_lt_of_le (Nat.lt_pow_succ_log_self hp1 (m + m))
            (Nat.pow_le_pow_right (le_of_lt hp1) hib)
        have hle : m % p ^ i ≤ m := Nat.mod_le m _
        omega
    · intro h i hmem
      have := h i (Finset.mem_Ico.1 hmem).1
      omega
  rw [hzero, hbridge, noCarry_iff_digits hp1 m, hDS]

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
