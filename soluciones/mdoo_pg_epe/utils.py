"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List
# pip install prototools
from prototools import validate_float


def validar_notas(valor: str, min: float = 0, max: float = 20) -> float:
    return validate_float(valor, min=min, max=max)


def validar_codigos(estudiantes: List[object], codigo: str) -> List[object]:
    if not estudiantes:
        return codigo
    for estudiante in estudiantes:
        if estudiante.codigo == codigo:
            raise ValueError
    return codigo
