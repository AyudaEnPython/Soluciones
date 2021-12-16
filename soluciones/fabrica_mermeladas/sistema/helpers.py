"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from collections import Counter
from typing import Dict

CODIGO: Dict[str, Dict[str, float]] = {
    "00": {"kg": 0.25, "precio": 300},
    "01": {"kg": 0.5, "precio": 500},
    "10": {"kg": 1, "precio": 1200},
    "11": {"kg": 2, "precio": 2400},
}


def read_data():
    with open("database/ventas.txt", "r") as f:
        data = f.read().splitlines()
        return dict(Counter(data))