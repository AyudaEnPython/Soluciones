"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def factorizar(n: int):
    """
    >>> factorizar(12)
    [[2, 3], [2, 1]]
    >>> factorizar(13)
    [[13], [1]]
    >>> factorizar(14)
    [[2, 7], [1, 1]]
    >>> factorizar(-1)

    """
    if n < 0:
        return None
    fs = []
    for j in range(2, int(n ** 0.5) + 1):
        while n % j == 0:
            fs.append(j)
            n = n // j
    if (n != 1):
        fs.append(n)
    rs = [fs.count(i) for i in set(fs)]
    return [list(set(fs)), rs]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
