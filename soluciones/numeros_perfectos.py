"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Perfect numbers up to "n".
"""
from prototools import timer


def sieve(n):
    p = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if p[i]:
            p[i*i::2*i] = [False] * int((n-i * i-1)/(2*i) + 1)
    return [2] + [i for i in range(3, n, 2) if p[i]]


def lucas_lehmer(p: int) -> bool:
    m = (1 << p) - 1
    s = 4
    for _ in range(2, p):
        s = (s * s - 2) % m
    if p == 2 or s == 0:
        return True
    return False


@timer
def main():
    n = 18
    ns = sieve(10000)
    i = k = 0
    while i != n:
        p = ns[k]
        if lucas_lehmer(p):
            i += 1
            pn = (2 ** (p - 1)) * ((2 ** p) - 1)
            print(f"{i:02}: {pn}")
        k += 1
    print(f"Digits of {i}th: {len(str(pn))}")
    assert len(str(pn)) == 1937


if __name__ == "__main__":
    main()  # around 7 secs to find the 18th perfect number.
