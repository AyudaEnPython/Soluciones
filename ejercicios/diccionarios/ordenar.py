"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Ordenar alfabéticamente por nombre.

Output:
ANDRES VIÑALES CIENFUEGOS: 176812737
CARLOS PEREZ GONZALEZ: 78903228
EFRAIN SOTO VERA: 143618668
JOAQUIN ANDRADE SANDOVAL: 78684747
JUAN TAPIA BURGOS: 132254524
OSCAR PEREZ ZUÑIGA: 216352696
"""
from typing import List, Dict, Union

paddock_managers = [
    {"id": 1, "tax_number": "132254524", "name": "JUAN TAPIA BURGOS"},
    {"id": 2, "tax_number": "143618668", "name": "EFRAIN SOTO VERA"},
    {"id": 3, "tax_number": "78903228", "name": "CARLOS PEREZ GONZALEZ"},
    {"id": 4, "tax_number": "176812737", "name": "ANDRES VIÑALES CIENFUEGOS"},
    {"id": 5, "tax_number": "216352696", "name": "OSCAR PEREZ ZUÑIGA"},
    {"id": 6, "tax_number": "78684747", "name": "JOAQUIN ANDRADE SANDOVAL"}
]


def solver(data: List[Dict[str, Union[int, str]]]) -> None:
    for k in sorted(data, key=lambda x: x["name"]):
        print(f"{k['name']}: {k['tax_number']}")


if __name__ == "__main__":
    solver(paddock_managers)
