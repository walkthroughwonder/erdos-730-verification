"""Search for two-offset identity systems (the k=2 / triple construction).

Per Lemma C we need integers alpha > 0, D0 > 4*alpha and odd constants
(h1,h2,h3,h4) with
    D0        = h1^2 * c^2      (disc of F      : n+1  = h1*P1*Q1-type)
    D0 + 2a   = h2^2 * d^2      (disc of 2F-1   : 2n+1 = h2*R1*S1)
    D0 - 2a   = h4^2 * b^2      (disc of 2F+1   : 2n+3 = h4*R2*S2)
    D0 - 4a   = h3^2 * e^2      (disc of F+1    : n+2  = h3*P2*Q2)
where a := alpha. Enumeration: for each (alpha, h2, h4), factor
h2^2 d^2 - h4^2 b^2 = 4*alpha  as (h2 d - h4 b)(h2 d + h4 b) = e*f over
divisor pairs; then test the other two conditions against allowed h1, h3.

v1 scope: alpha <= 20000, h2,h4 in {1,3,5,7,9,15}, h1,h3 in {1,3,5,7,9,15,21,45}.
"""
import sys
from math import isqrt

AMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
H_MID = [1, 3, 5, 7, 9, 15]
H_OUT = [1, 3, 5, 7, 9, 15, 21, 45]
H_OUT_SQ = [(h, h * h) for h in H_OUT]


def as_h_square(v):
    """Return list of h in H_OUT with v = h^2 * square, v > 0."""
    out = []
    for h, h2 in H_OUT_SQ:
        if v % h2 == 0:
            w = v // h2
            r = isqrt(w)
            if r * r == w:
                out.append((h, r))
    return out


def divisors(m):
    ds = []
    i = 1
    while i * i <= m:
        if m % i == 0:
            ds.append(i)
            if i != m // i:
                ds.append(m // i)
        i += 1
    return ds


hits = 0
for alpha in range(1, AMAX + 1):
    m = 4 * alpha
    ds = divisors(m)
    for h2 in H_MID:
        for h4 in H_MID:
            for e in ds:
                f = m // e
                if e >= f:
                    continue
                # h2*d = (f+e)/2, h4*b = (f-e)/2
                if (f + e) % 2 or (f - e) % 2:
                    continue
                u, v = (f + e) // 2, (f - e) // 2
                if u % h2 or v % h4:
                    continue
                d, b = u // h2, v // h4
                if d <= 0 or b <= 0:
                    continue
                D0 = h4 * h4 * b * b + 2 * alpha
                if D0 <= 4 * alpha:
                    continue
                m1 = as_h_square(D0)
                if not m1:
                    continue
                m3 = as_h_square(D0 - 4 * alpha)
                if not m3:
                    continue
                hits += 1
                print(f"HIT alpha={alpha} D0={D0} "
                      f"h2={h2},d={d} h4={h4},b={b} "
                      f"D0 as {m1} ; D0-4a as {m3}", flush=True)
    if alpha % 2000 == 0:
        print(f"[ids] alpha={alpha} hits={hits}", flush=True)
print(f"DONE alpha<= {AMAX}: {hits} hits", flush=True)
