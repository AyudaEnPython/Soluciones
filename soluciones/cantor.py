"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from fractions import Fraction


def cantor(n: int) -> Fraction:
    """Retorna el n término de la sucesión de cantor.

    >>> cantor(3)
    2
    >>> cantor(14)
    1/2
    >>> cantor(7)
    1/4
    """
    i = j = k = 1
    while k < n:
        j += 1
        k += 1
        if k == n:
            break
        while j > 1 and k < n:
            i += 1
            j -= 1
            k += 1
        if k == n:
            break
        i += 1
        k += 1
        if k == n:
            break
        while i > 1 and k < n:
            i -= 1
            j += 1
            k += 1
    print(f"{Fraction(i, j)}")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
