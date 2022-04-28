"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def factorial(n: int) -> int:
    return 1 if n == 0 else n * factorial(n - 1)


def combinatorio(m: int, n: int) -> int:
    return factorial(m) // (factorial(n) * factorial(m - n))


def main():
    n = 2
    m = 8
    print(combinatorio(m, n))


if __name__ == "__main__":
    main()
