"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from collections import Counter
from time import sleep
from typing import Callable, Dict
# pip install prototools
from prototools import progressbar

CODIGO: Dict[str, Dict[str, float]] = {
    "00": {"kg": 0.25, "precio": 300},
    "01": {"kg": 0.5, "precio": 500},
    "10": {"kg": 1, "precio": 1200},
    "11": {"kg": 2, "precio": 2400},
}


def bar(n: int) -> None:
    print("Cargando datos de ventas...")
    for _ in progressbar(range(n)):
        sleep(0.05)


def read_data() -> Dict[str, int]:
    with open("database/ventas.txt", "r") as f:
        data = f.read().splitlines()
        return dict(Counter(data))


def totales(data: Dict[str, float], f: Callable, key: str) -> int:
    return sum(f(codigo, key) for codigo in data)
