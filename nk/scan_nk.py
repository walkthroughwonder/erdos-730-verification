"""Scan for equal-radical pairs (n, n+k): rad C(2n,n) = rad C(2n+2k,n+k).

Theory (see NK_THEORY.md):
  - Only primes dividing a bridge number n+j (1<=j<=k) or 2n+2j-1 can change
    membership, so the test is local.
  - Any prime in (2n, 2n+2k] kills the pair (divides B_{n+k}, not B_n).
Test per surviving prime p: (n in D_p) <-> (n+k in D_p), where D_p = all
base-p digits <= (p-1)/2. Full-support equality follows (localization).

Usage: python scan_nk.py NMAX KMAX [start]
Output: nk_pairs.txt lines "k n" + progress to stdout.
"""
import sys
from array import array

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200_000
KMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 16
START = int(sys.argv[3]) if len(sys.argv) > 3 else 1
LIMIT = 2 * (NMAX + KMAX) + 2

# smallest-prime-factor sieve
spf = array('i', [0]) * 0
spf = array('i', bytes(4 * (LIMIT + 1)))
for i in range(2, LIMIT + 1):
    if spf[i] == 0:
        for j in range(i, LIMIT + 1, i):
            if spf[j] == 0:
                spf[j] = i
print(f"sieve done to {LIMIT}", flush=True)


def prime_factors(m):
    fs = set()
    while m > 1:
        p = spf[m]
        fs.add(p)
        while m % p == 0:
            m //= p
    return fs


def in_Dp(m, p):
    h = (p - 1) // 2
    while m:
        if m % p > h:
            return False
        m //= p
    return True


def pair_ok(n, k):
    # prime-gap obstruction: no prime in (2n, 2n+2k]
    for q in range(2 * n + 1, 2 * n + 2 * k + 1, 2):
        if spf[q] == q:
            return False
    ps = set()
    for j in range(1, k + 1):
        ps |= prime_factors(n + j)
        ps |= prime_factors(2 * n + 2 * j - 1)
    ps.discard(2)
    return all(in_Dp(n, p) == in_Dp(n + k, p) for p in ps)


def main():
    found = {}
    out = open("nk_pairs.txt", "a")
    for n in range(START, NMAX + 1):
        for k in range(1, KMAX + 1):
            if pair_ok(n, k):
                found.setdefault(k, []).append(n)
                out.write(f"{k} {n}\n")
                out.flush()
                if len(found[k]) <= 3:
                    print(f"  k={k}: n={n}", flush=True)
        if n % 20000 == 0:
            print(f"[scan] n={n}; ks found: "
                  f"{sorted((k, len(v)) for k, v in found.items())}",
                  flush=True)
    print("SUMMARY (k: count, first examples):", flush=True)
    for k in range(1, KMAX + 1):
        v = found.get(k, [])
        print(f"  k={k}: {len(v)} pairs; first: {v[:5]}", flush=True)


if __name__ == "__main__":
    main()
