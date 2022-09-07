"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Para preparar aperitivos, un barman almacena en tres baldes distintas
medidas de vino, ginebra y jugo de limón, según la siguiente tabla:

    +-------+------+---------+---------------+
    | Balde | Vino | Ginebra | Jugo de limón |
    +-------+------+---------+---------------+
    |   A   |   20 |      30 |            50 |
    |   B   |   30 |      20 |            60 |
    |   C   |   30 |      30 |            32 |
    +-------+------+---------+---------------+

Por otro lado, se tiene la información de los precios por litro de cada
líquido:

    +----------------+--------+
    | Líquido        | Precio |
    +----------------+--------+
    | Vino           |      5 |
    | Ginebra        |     45 |
    | Jugo de Limón  |     10 |
    +----------------+--------+

a) Escriba un programa que muestre cuál es el precio de cada uno de los
    baldes.

b) Escriba un programa que muestre el precio total de 10 baldes A, 4
    baldes B y 5 baldes C.
"""
from typing import Callable, List, Iterable, Sequence

baldes: Iterable[Sequence[int]] = [
    [20, 30, 50],
    [30, 20, 60],
    [30, 30, 32],
]
precios: List[int] = [5, 45, 10]
cantidades: List[int] = [10, 4, 5]

_mul: Callable = lambda x, y: x * y

total = list(map(lambda v: sum(map(_mul, v, precios)), baldes))
total_b = list(map(_mul, total, cantidades))

for balde, precio in zip("ABC", total):
    print(f"El precio del balde {balde} es {precio}.")
for i, (balde, precio) in enumerate(zip("ABC", total_b)):
    print(f"El precio de {cantidades[i]} baldes {balde} es {precio}.")
print(f"El precio total es {sum(total_b)}.")
