"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Implemente un algorimo que muestre todos los números menores a 100 que
puedan formarse con los dígitos 1, 2, 3, 4, 5, 6.
"""

def _cr(_it, r):
    pool = tuple(_it)
    n = len(pool)
    if not n and r:
        return
    idx = [0] * r
    yield tuple(pool[i] for i in idx)
    while True:
        for i in reversed(range(r)):
            if idx[i] != n - 1:
                break
        else:
            return
        idx[i:] = [idx[i] + 1] * (r - i)
        yield tuple(pool[i] for i in idx)


def cr(ns, n):
    return map(lambda x: "".join(x), _cr(ns, n))


def main():
    print(*cr(list("123456"), 2), sep=", ")


if __name__ == "__main__":
    main()
