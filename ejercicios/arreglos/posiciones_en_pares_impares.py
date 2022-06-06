"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dado un lote de N números, colocar los números ordenados de manera
ascendente en el vector y luego mostrarlo, con las siguientes
condiciones:
- Colocar los números pares en las posiciones pares del vector.
- Colocar los números impares en las posciones impares del vector.
- Colocar ceros en las posiciones que quedan vacias en el vector
    (opcional).

Ejemplo:

+------------------+-------------------+
| Entrada          | Salida            |
+------------------+-------------------+
| 7                | 4 3 8 3 10 67 26  |
| 4 67 3 26 3 8 10 |                   |
+------------------+-------------------+
| 8                | 0 1 2 3 4 5 6 0 8 |
| 0 1 2 3 4 5 6 8  |                   |
+------------------+-------------------+
"""
from typing import List, Tuple


def get_data() -> Tuple[int, List[int]]:
    n = int(input())
    return (n, list(map(int, input().split())))


def sol(n, numbers) -> List[int]:
    """
    >>> sol(7, [4, 67, 3, 26, 3, 8, 10])
    [4, 3, 8, 3, 10, 67, 26]
    >>> sol(8, [0, 1, 2, 3, 4, 5, 6, 8])
    [0, 1, 2, 3, 4, 5, 6, 0, 8]
    """
    result = []
    numbers.sort()
    pares = [x for x in numbers if x % 2 == 0]
    impares = [x for x in numbers if x % 2 != 0]
    for i in range(n//2 + 1):
        if pares:
            result.append(pares.pop(0))
        elif impares and not pares and i % 2 == 0:
            result.append(0)
        if impares:
            result.append(impares.pop(0))
        elif pares and not impares and i % 2 != 0:
            result.append(0)
    return result


def main():
    n, numbers = get_data()
    print(sol(n, numbers))


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    main()
