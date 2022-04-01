"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def binario(n: int) -> int:
    """
    >>> binario(12)
    1100
    >>> binario(2)
    10
    >>> binario(-1)

    """
    if n < 0:
        return None
    return int(bin(n)[2:])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
