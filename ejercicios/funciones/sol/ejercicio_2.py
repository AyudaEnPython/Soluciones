"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def dividir(dividendo: int, divisor: int) -> int:
    """
    >>> dividir(10, 3)
    (3, 1)
    """
    return dividendo // divisor, dividendo % divisor


if __name__ == "__main__":
    import doctest
    doctest.testmod()
