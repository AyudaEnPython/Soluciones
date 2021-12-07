"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

En un informe anual de CastilloGas S.A., el presidente informa a sus
accionistas la cantidad anual de producción de barriles de 50 litros de
lubricantes normal, extra y súper, en sus dos refinerías:

    +-----------+--------+-------+-------+
    | Refinería | Normal | Extra | Super |
    +-----------+--------+-------+-------+
    | A         |   3000 |  7000 |  2000 |
    | B         |   4000 |   500 |   600 |
    +-----------+--------+-------+-------+

Además, informa que en cada barril de 50 litros de lubricante existe la
siguiente composición en litros de aceites finos, alquitrán y grasas
residuales:

    +-------------------+--------+-------+-------+
    | Componente        | Normal | Extra | Super |
    +-------------------+--------+-------+-------+
    | Aceites fino      |     10 |     5 |    35 |
    | Alquitrán         |     15 |     4 |    31 |
    | Grasas residuales |     18 |     2 |    30 |
    +-------------------+--------+-------+-------+

a) Escriba la función 'totales_anuales(a, b)' que recibe como
    parámetros ambas matrices y retorne un arreglo con los totales de
    aceites finos, alquitrán y grasas residuales presentes en la
    producción anual.

b) Escriba la función 'maximo_alquitran(a, b)' que recibe como
    parámetros ambas matrices y retorne el valor máximo de alquitrán
    consumidos por ambas refinierías.

c) Determine cuál es la matriz que entrega el consumo de todos los
    elementos que forman parte de un lubricante, en cada refinería.
"""
from typing import List, Iterable, Sequence, Tuple

COMPONENTE: Tuple[str] = ("Aceites fino", "Alquitrán", "Grasas residuales")
componentes: Iterable[Sequence[int]] = [
    [10, 5, 35],
    [15, 4, 31],
    [18, 2, 30],
]
A = [3, 7, 2]
B = [4, 5, 6]

_mul = lambda a, b: map(lambda x, y: x * y, a, b)
_sum = lambda a, b: map(lambda x, y: x + y, a, b)


def totales_anuales(a: List[int], b: List[int]) -> List[int]:
    return list(map(lambda v: sum(_mul(v, _sum(a, b))), componentes))


def maximo_alquitran(a, b):
    return max(max(list(map(lambda x: list(_mul(componentes[1], x)), (a, b)))))

def consumo(a, b):
    return [[sum([componentes[j][i] * x[j] for j in range(len(a))])
            for i in range(len(componentes))] for x in (a, b)]


totales = totales_anuales(A, B)
alquitran = maximo_alquitran(A, B)
consumos = consumo(A, B)

for c, total in zip(COMPONENTE, totales):
    print(f"{c:>17}: {total}")
print(f"\nAlquitrán máximo: {alquitran}")
print(f"\n{'F':>16} {'A':>4} {'R':>3}")
for r, consumo in zip("AB", consumos):
    print(f"Refineria {r}: {consumo}")