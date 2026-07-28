"""Segmented run-hunter: extends the consecutive equal-radical scan past
the in-memory-sieve limit. Same criterion as scan_runs.py; per block,
factor the A-window (n+1) and M-window (2n+1) by sieving primes up to
sqrt(2R), digit-checking each extracted prime power on the fly; residual
cofactors > 1 are prime and get the (vector-friendly) large-prime check.

Usage: python scan_runs2.py START END [BLOCK]
Appends to runs2_found.txt; prints runs of length >= 3 values.
"""
import sys
from math import isqrt

START = int(sys.argv[1])
END = int(sys.argv[2])
BLOCK = int(sys.argv[3]) if len(sys.argv) > 3 else 1_000_000


def small_primes(limit):
    sieve = bytearray([1]) * 0
    sieve = bytearray([1]) * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, isqrt(limit) + 1):
        if sieve[i]:
            sieve[i * i :: i] = b"\x00" * len(sieve[i * i :: i])
    return [i for i in range(2, limit + 1) if sieve[i]]


def in_Dp(m, p):
    h = (p - 1) // 2
    while m:
        if m % p > h:
            return False
        m //= p
    return True


def process_block(L, R, primes, bad):
    """Mark bad[n-L] for n in [L, R) where the k=1 criterion fails."""
    # ---- A-window: A = n+1 in [L+1, R+1) ----
    width = R - L
    cof = list(range(L + 1, R + 1))
    for p in primes:
        if p * p > R + 1:
            break
        start = ((L + 1 + p - 1) // p) * p
        for A in range(start, R + 1, p):
            i = A - (L + 1)
            a = 0
            while cof[i] % p == 0:
                cof[i] //= p
                a += 1
            if a and p != 2 and in_Dp(A // p**a, p):
                bad[i] = 1
    for i in range(width):
        q = cof[i]
        if q > 1:  # prime cofactor
            A = L + 1 + i
            if not bad[i] and in_Dp(A // q, q):
                bad[i] = 1
    # ---- M-window: M = 2n+1 in [2L+1, 2R+1), odd only ----
    cof = list(range(2 * L + 1, 2 * R + 1, 2))
    for p in primes:
        if p == 2:
            continue
        if p * p > 2 * R + 1:
            break
        # odd multiples of p in [2L+1, 2R+1)
        start = ((2 * L + 1 + p - 1) // p) * p
        if start % 2 == 0:
            start += p
        for M in range(start, 2 * R + 1, 2 * p):
            i = (M - (2 * L + 1)) // 2
            a = 0
            while cof[i] % p == 0:
                cof[i] //= p
                a += 1
            if a and not bad[i] and in_Dp((M // p**a - 1) // 2, p):
                bad[i] = 1
    for i in range(width):
        q = cof[i]
        if q > 1:
            M = 2 * L + 1 + 2 * i
            if not bad[i] and in_Dp((M // q - 1) // 2, q):
                bad[i] = 1


def main():
    primes = small_primes(isqrt(2 * END + 2) + 2)
    print(f"{len(primes)} small primes; scanning [{START}, {END})", flush=True)
    out = open("runs2_found.txt", "a")
    runlen = 0
    total = 0
    L = START
    while L < END:
        R = min(L + BLOCK, END)
        bad = bytearray(R - L)
        process_block(L, R, primes, bad)
        for i in range(R - L):
            if not bad[i]:
                total += 1
                runlen += 1
                if runlen >= 2:
                    n = L + i
                    msg = (f"RUN length {runlen + 1}: "
                           f"values {n - runlen + 1}..{n + 1}")
                    print(msg, flush=True)
                    out.write(msg + "\n")
                    out.flush()
            else:
                runlen = 0
        print(f"[seg] done {R}: k1-count so far {total}", flush=True)
        L = R
    print(f"DONE [{START},{END}): {total} k=1 pairs", flush=True)


if __name__ == "__main__":
    main()
