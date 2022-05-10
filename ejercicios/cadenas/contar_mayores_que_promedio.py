"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Desarrolla un programa que pregunte al usuario cuántos datos ingresará,
a continuación le pida que ingrese los datos uno por uno, y finalmente
entregue como salida cuántos de los datos ingresados fueron mayores que
el promedio.

    +---------+-----------------+
    | Entrada | Salida          |
    +---------+-----------------+
    | 5       |                 |
    | 6.5     | 2 datos         |
    | 2.1     | son mayores     |
    | 2       | que el promedio |
    | 2.2     |                 |
    | 6.1     |                 |
    +---------+-----------------+
    | 10      |                 |
    | 9.8     |                 |
    | 9.8     |                 |
    | 9.8     |                 |
    | 9.8     | 9 datos         |
    | 1.1     | son mayores     |
    | 9.8     | que el promedio |
    | 9.8     |                 |
    | 9.8     |                 |
    | 9.8     |                 |
    | 9.8     |                 |
    +---------+-----------------+
"""
from typing import List
from unittest import main, TestCase
from statistics import mean


def input_data() -> List[float]:
    """Retorna una lista de números flotantes ingresados por el usuario
    """
    data = []
    n = int(input("Cantidad: "))
    for _ in range(n):
        data.append(float(input("Dato: ")))
    return data


def solver_a(data: List[float]) -> int:
    return len(list(filter(lambda x: x > mean(data), data)))


def solver_b(data: List[float]) -> int:
    return len([x for x in data if x > mean(data)])


def solver_c(data: List[float]) -> int:
    return sum(True for x in data if x > mean(data))


def solver_d(data: List[float]) -> int:
    result = []
    for x in data:
        if x > mean(data):
            result.append(x)
    return len(result)


class Test(TestCase):

    def test_solvers(self):
        for solver in (solver_a, solver_b, solver_c, solver_d):
            self.assertEqual(solver([1, 1, 1]), 0)
            self.assertEqual(solver([1, 2, 3]), 1)
            self.assertEqual(solver([4, 5, 6]), 1)
            self.assertEqual(solver([10, 11, 12, 13, 14]), 2)
            self.assertEqual(solver([6.5, 2.1, 2, 2.2, 6.1]), 2)
            self.assertEqual(
                solver(
                    [9.8, 9.8, 9.8, 9.8, 1.1, 9.8, 9.8, 9.8, 9.8, 9.8]
                    ), 
                9
            )


if __name__ == '__main__':
    main()
    # data = input_data()
    # print(f"{solver(data)} datos son mayores que el promedio")