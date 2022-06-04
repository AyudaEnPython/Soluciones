"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict

MENSAJES: Dict[int, str] = {
    0: "OK",
    1: "CURSO SENSIBILIZACION",
    2: "MULTA",
}


def sol(e: float, vmp: float, t: float) -> str:
    if e <= 0 or vmp <= 0 or t <= 0:
        return "ERROR"
    v = e / t
    vmp *= 5 / 18
    if v < vmp:
        return MENSAJES[0]
    elif vmp < v <= vmp * 1.2:
        return MENSAJES[1]
    else:
        return MENSAJES[2]


def main():
    e, permitido, t = map(float, input().split())
    print(sol(e, permitido, t))


if __name__ == "__main__":
    main()
