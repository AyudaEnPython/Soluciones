"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict, Tuple

VALID = "kV+*@aAZ1P[]Coler"
DEFAULTS = "U", "A", "D"


def _load_players(default_: Tuple[str, str], n: int = 0) -> Dict[str, int]:
    return {name: n for name in default_}


def validate(input_: str, valid: str = VALID) -> str:
    if not all(c in valid for c in input_):
        return "!"*len(input_)
    return input_


def sol(xs: str, ys: str, d: Tuple[Tuple[str, str], str] = DEFAULTS) -> str:
    (a, b, t), p, s = d, _load_players(d[:-1]), ""
    for x, y in zip(xs, ys):
        if ord(x) > ord(y):
            p[a] += 1
        elif ord(x) < ord(y):
            p[b] += 1
        if p[a] > p[b]:
            s += a
        elif p[a] < p[b]:
            s += b
        else:
            s += t
    return s


def main():
    U = validate(input())
    A = validate(input())
    print(sol(U, A))


if __name__ == "__main__":
    main()
