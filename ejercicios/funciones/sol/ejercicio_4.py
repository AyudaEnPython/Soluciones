"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def factorial(n: int) -> int:
    """
    >>> factorial(4)
    24
    >>> factorial(-2)
    """
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
