"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def _es_primo(n: int) -> bool:
    """
    >>> _es_primo(7)
    True
    >>> _es_primo(8)
    False
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def proximo_primo(n: int) -> int:
    """
    >>> proximo_primo(7)
    11
    >>> proximo_primo(8)
    >>> proximo_primo(-1)
    """
    if n < 0:
        return None
    if not _es_primo(n):
        return None
    for i in range(n + 1, n * 2):
        if _es_primo(i):
            return i


if __name__ == "__main__":
    import doctest
    doctest.testmod()
