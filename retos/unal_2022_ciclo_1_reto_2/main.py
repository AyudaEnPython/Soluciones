"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Tuple

DEFAULT = "MPD"


def sol(a: str, b: str, s: str, d: str = DEFAULT) -> str:
    (x, y, z), r = d, ""
    i = j = 0
    for c in s:
        i += 1 if c in a else 0
        j += 1 if c in b else 0
        r += x if i > j else (y if i < j else z)
    return r


def main():
    a = input()
    b = input()
    s = input()
    print(sol(a, b, s))


if __name__ == "__main__":
    main()
