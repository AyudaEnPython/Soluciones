"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def es_capicua(n: int) -> bool:
    """
    >>> es_capicua(787)
    True
    >>> es_capicua(108)
    False
    >>> es_capicua("101")

    """
    if not isinstance(n, int):
        return None
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
