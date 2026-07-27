"""Hunt runs of consecutive equal-radical values: n with
rad B_n = rad B_{n+1} = ... = rad B_{n+L-1}. A run of length L gives
(n, n+k) pairs for every k <= L-1 by transitivity.

k=1-only test per n (criterion of the verified 730 proof):
  A = n+1: for p^a || A (p odd), A/p^a not in D_p;
  M = 2n+1: for p^a || M, (M/p^a - 1)/2 not in D_p.
Usage: python scan_runs.py NMAX [start]
"""
import sys
from array import array

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3_000_000
START = int(sys.argv[2]) if len(sys.argv) > 2 else 1
LIMIT = 2 * NMAX + 4

spf = array('i', bytes(4 * (LIMIT + 1)))
for i in range(2, LIMIT + 1):
    if spf[i] == 0:
        for j in range(i, LIMIT + 1, i):
            if spf[j] == 0:
                spf[j] = i
print(f"sieve done to {LIMIT}", flush=True)


def in_Dp(m, p):
    h = (p - 1) // 2
    while m:
        if m % p > h:
            return False
        m //= p
    return True


def k1_ok(n):
    A = n + 1
    m = A
    while m > 1:
        p = spf[m]
        a = 0
        while m % p == 0:
            m //= p
            a += 1
        if p != 2 and in_Dp(A // p**a, p):
            return False
    M = 2 * n + 1
    m = M
    while m > 1:
        p = spf[m]
        a = 0
        while m % p == 0:
            m //= p
            a += 1
        if in_Dp((M // p**a - 1) // 2, p):
            return False
    return True


def main():
    out = open("runs_found.txt", "a")
    prev = False
    runlen = 0
    count1 = 0
    for n in range(START, NMAX + 1):
        cur = k1_ok(n)
        if cur:
            count1 += 1
            runlen = runlen + 1 if prev else 1
            if runlen >= 2:
                # runlen consecutive k1-true indices ending at n cover the
                # values n - runlen + 1 .. n + 1  (runlen + 1 values)
                msg = f"RUN length {runlen + 1}: values {n - runlen + 1}..{n + 1}"
                print(msg, flush=True)
                out.write(msg + "\n")
                out.flush()
        else:
            runlen = 0
        prev = cur
        if n % 200000 == 0:
            print(f"[runs] n={n}: k1-count={count1}", flush=True)
    print(f"DONE: {count1} k=1 pairs up to {NMAX}", flush=True)


if __name__ == "__main__":
    main()
