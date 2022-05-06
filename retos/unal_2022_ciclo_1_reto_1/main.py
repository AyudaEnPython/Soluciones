"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Union


def category(n: int) -> str:
    return {
        0 <= n <= 20: "uno",
        21 <= n <= 40: "dos",
        41 <= n <= 70: "tres",
        n > 70: "cuatro",
    }[True]


def sol(n: Union[str, int, float]) -> None:
    h = int(n)
    p = int(h << 1) + 4
    l = int((h + p) >> 1)
    print(h, p, l)
    print(category(l))


def main():
    sol(45)


if __name__ == "__main__":
    main()
