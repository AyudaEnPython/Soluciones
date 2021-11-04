"""Se opta por modificar ligeramente la clase original.
"""
from typing import Any, List, Optional
from __future__ import annotations

class Vector:
    """Representación de un vector como un espacion multidimensional
    
    :param d: dimension del vector o iterable que representa al vector
    :d type: Opional[Any]
    """

    def __init__(self, d: Optional[Any] = None) -> None:
        if isinstance(d, int):
            self._coordenadas = [0] * d
        else:
            self._coordenadas = d

    def __len__(self) -> int:
        return len(self._coordenadas)

    def __getitem__(self, i) -> List[int]:
        return self._coordenadas[i]

    def __setitem__(self, i, valor) -> None:
        self._coordenadas[i] = valor

    def __add__(self, otro) -> Vector:
        if len(self) != len(otro):
            raise ValueError('Los vectores no tienen la misma dimension')
        return Vector([self[i] + otro[i] for i in range(len(self))])
    
    def __sub__(self, otro) -> Vector:
        return self + (-otro)

    def __mul__(self, otro) -> int:
        if len(self) != len(otro):
            raise ValueError('Los vectores no tienen la misma dimension')
        return sum(self[i] * otro[i] for i in range(len(self)))

    def __neg__(self) -> Vector:
        return Vector([-c for c in self._coordenadas])

    def __eq__(self, otro) -> bool:
        return self._coordenadas == otro._coordenadas

    def __ne__(self, otro) -> bool:
        return not self == otro

    def __str__(self) -> str:
        return f'< {str(self._coordenadas)[1:-1]} >'

    def __repr__(self) -> str:
        return f'Vector({self._coordenadas})'