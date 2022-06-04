"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict

MENSAJES: Dict[int, str] = {
    0: "OK",
    1: "MULTA",
    2: "CURSO SENSIBILIZACION",
}


def sol(e: float, lim: float, t: float) -> str:
    if e <= 0 or lim <= 0 or t <= 0:
        return "ERROR"
    v = (e/t) * (18/5)
    if v < lim:
        return MENSAJES[0]
    elif lim < v < lim * 1.2:
        return MENSAJES[1]
    else:
        return MENSAJES[2]


def main():
    e, permitido, t = map(float, input().split())
    print(sol(e, permitido, t))


if __name__ == "__main__":
    main()
