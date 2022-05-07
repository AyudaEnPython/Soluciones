"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from prototools import validate_float


def validar_notas(valor: str, min: float = 0, max: float = 20) -> float:
    return validate_float(valor, min=min, max=max)
