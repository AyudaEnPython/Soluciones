"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List
# pip install prototools
from prototools import int_input


def get_notas(n: int = 3) -> List[int]:
    return [int_input(f"Nota {i+1}: ") for i in range(n)]


class Calificacion:

    def __init__(self, notas: List[int]):
        self.notas = notas

    def promedio(self) -> float:
        return round(sum(self.notas) / len(self.notas))

    def mayor(self) -> int:
        return max(self.notas)

    def menor(self) -> int:
        return min(self.notas)


if __name__ == "__main__":
    notas = get_notas()
    calificacion = Calificacion(notas)
    print(f"Mayor calificación: {calificacion.mayor()}")
    print(f"Menor calificación: {calificacion.menor()}")
    print(f"Promedio: {calificacion.promedio()}")
