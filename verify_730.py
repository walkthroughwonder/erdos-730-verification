"""Numerical audit of the Erdos 730 candidate proof.

N1: brute-force Lemma 2.1 (transition criterion) for all n <= NMAX.
    rad B_n computed via Kummer (p in rad B_n iff n not in D_p), never by
    factoring binomials.
N2: the large-prime residue table and branch eliminations (finite checks).
N3: empirical density of good x for the explicit family, via the criterion
    (factoring P,Q,R,S with sympy); reports any good x found -> new
    consecutive pairs for A129515.
N4: the constants C, Lambda and the final elementary inequality.
"""
import sys
from sympy import factorint, primerange
from math import log

T = 3 * 41 * 43  # 5289


def digits_ok(m, p):
    """m in D_p: all base-p digits <= (p-1)/2."""
    h = (p - 1) // 2
    while m:
        if m % p > h:
            return False
        m //= p
    return True


def rad_support_odd(n, primes):
    """Odd primes p <= 2n dividing B_n = C(2n,n): p | B_n iff n not in D_p."""
    return frozenset(p for p in primes if p <= 2 * n and not digits_ok(n, p))


def criterion(n):
    """Lemma 2.1's conditions (2)+(3) for A = n+1, M = 2n+1."""
    A, M = n + 1, 2 * n + 1
    for p, a in factorint(A).items():
        if p == 2:
            continue
        if digits_ok(A // p**a, p):
            return False
    for p, a in factorint(M).items():
        if digits_ok((M // p**a - 1) // 2, p):
            return False
    return True


def n1(nmax=1200):
    primes = list(primerange(3, 2 * nmax + 3))
    mismatches = 0
    good = []
    prev = rad_support_odd(1, primes)
    for n in range(1, nmax):
        cur = rad_support_odd(n + 1, primes)
        truth = prev == cur
        claim = criterion(n)
        if truth != claim:
            mismatches += 1
            print(f"  N1 MISMATCH at n={n}: direct={truth} criterion={claim}")
        if truth:
            good.append(n)
        prev = cur
    print(f"N1: n < {nmax}: mismatches={mismatches}; "
          f"equal-radical n found: {good}")
    return mismatches == 0


def n2():
    """Large-prime residue table: for each branch, alpha*c^2 mod d over the
    admissible c-classes, and the necessary classes for s/d < 1/2.
    Branch data: Phi = (alpha p c^2 + beta c + gamma)/d with a=1."""
    # (branch, alpha, beta, gamma, d, form slope mod d, form const mod d)
    data = {
        "P": (12, -41, 0, 7),
        "Q": (7, 41, 0, 12),
        "R": (54, 129, -7, 14),
        "S": (7, -43, -6, 12),
    }
    # admissible c-classes: c coprime-ish residues arising from L(x)/p.
    # We just enumerate all residues c mod d with gcd-consistency, compute
    # s = alpha*c^2 mod d, and record which classes give s/d < 1/2.
    ok = True
    for br, (al, be, ga, d) in data.items():
        svals = {}
        for c in range(d):
            s = (al * c * c) % d
            svals.setdefault(s, []).append(c)
        # possible s values over c coprime to d (paper's claim concerns
        # residues where the branch can actually land; report all)
        all_s = sorted({(al * c * c) % d for c in range(d) if gcd(c, d) == 1})
        low = sorted({s for s in all_s if s / d < 0.5})
        classes = sorted({c for c in range(d) if gcd(c, d) == 1
                          and (al * c * c) % d / d < 0.5})
        print(f"N2 {br}: d={d} alpha*c^2 mod d over units: {all_s}; "
              f"s/d<1/2 for c in {classes}")
    # paper claims: P: {3,5,6} with classes c=3,4; Q: {7} none;
    # R: {6,10,12} classes c=5,9(mod 14); S: {7} none.
    return ok


from math import gcd


def n3(xmax=400):
    good = []
    for x in range(1, xmax + 1):
        P = 42 * T * x + 11
        Q = 72 * T * x + 13
        R = 28 * T * x + 5
        S = 72 * T * x + 19
        n = P * Q - 1
        A, M = P * Q, 3 * R * S
        assert 2 * n + 1 == M
        okx = True
        for p, a in {**factorint(A)}.items():
            if p == 2:
                continue
            if digits_ok(A // p**a, p):
                okx = False
                break
        if okx:
            for p, a in {**factorint(M)}.items():
                if digits_ok((M // p**a - 1) // 2, p):
                    okx = False
                    break
        if okx:
            good.append(x)
            print(f"  N3 GOOD x={x}: n={n} (consecutive pair (n, n+1)!)")
    print(f"N3: x <= {xmax}: good count={len(good)} "
          f"density={len(good)/xmax:.4f} (paper lower bound 0.0430)")
    return good


def n4():
    C = sum(4**-r * log((r + 2) / (r + 1)) for r in range(1, 200))
    Lam = 4 * C + (2 / 3) * log(2)
    print(f"N4: C={C:.15f} (paper 0.123737624319818)")
    print(f"N4: Lambda={Lam:.15f} (paper 0.957048617652571); "
          f"1-Lambda={1-Lam:.6f}")
    import math
    lhs = math.exp(8 / 3)
    print(f"N4: e^(8/3)={lhs:.4f} > 49621/3645={49621/3645:.4f} > 13.5: "
          f"{lhs > 49621/3645 > 13.5}")


if __name__ == "__main__":
    n4()
    n2()
    ok1 = n1(int(sys.argv[1]) if len(sys.argv) > 1 else 1200)
    n3(int(sys.argv[2]) if len(sys.argv) > 2 else 400)
    print("N1 FOUNDATION:", "PASS" if ok1 else "FAIL")
