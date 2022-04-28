"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict


CONVERSION: Dict[str, float] = {
    "euro": 7.45, "dolar": 4.44, "yen": 0.035, "libra": 5.79,
}


def converter(local: float, foreign: str) -> float:
    return local * CONVERSION[foreign]


def main():
    bs = float(input("Bs: "))
    cambio = input("A: ")
    print(f"{converter(bs, cambio)}")


if __name__ == "__main__":
    main()
