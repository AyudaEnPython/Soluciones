"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Implemente un algorimo que muestre todos los números menores a 100 que
puedan formarse con los dígitos 1, 2, 3, 4, 5, 6.
"""

def _cr(it, r):
    pool = tuple(it)
    n = len(pool)
    if not n in r:
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
    for n in cr(list("123456"), 2):
        print(n)


if __name__ == "__main__":
    main()
