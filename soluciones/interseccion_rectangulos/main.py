"""
Escribe un programa que dadas las coodenadas de un par de esquinas
opuestas de cada cancha calcule el área total por ambas canchas.

Entrada
Tu programa deberá leer del teclado dos líneas, cada una de 4 números
enteros separados por un espacio que representaran las coordenadas
x1, y1, x2, y2, de cada una de las canchas.

Salida
Tu programa deberá escribir en pantalla un único número que represente
el área total cubierta por ambas canchas.

Ejemplo
1 1 3 4
2 3 6 7
21
"""
from typing import List
from unittest import main, TestCase

from models import Point_, Point, Rectangle
from utils import (
    process_input, _helper,
    point_factory, rectangle_factory,
    area, max_, min_,
    area_alt, max_alt, min_alt,
)


def solver_dataclass(data: List[tuple]) -> float:
    p1, p2, p3, p4 = point_factory(Point, data)
    r1, r2 = rectangle_factory(Rectangle, [p1, p2, p3, p4])
    x, y = Point.max_(p1, p3), Point.min_(p2, p4)
    if max(x) > min(y):
        x, y = (0, 0), (0, 0)
    return r1.area() + r2.area() - Rectangle(Point(*x), Point(*y)).area()


def solver_namedtuple(data: List[tuple]) -> float:
    p1, p2, p3, p4 = point_factory(Point_, data)
    x, y = max_(p1, p3), min_(p2, p4)
    if max(x) > min(y):
        x, y = (0, 0), (0, 0)
    x, y = Point_(*x), Point_(*y)
    return area(p1, p2) + area(p3, p4) - area(x, y)


def solver_alt_helpers(data: List[tuple]) -> float:
    r1_p, r2_p = data
    (p1, p2), (p3, p4) = _helper(r1_p), _helper(r2_p)
    x, y = max_alt(p1, p3), min_alt(p2, p4)
    if max(x) > min(y):
        x, y = (0, 0), (0, 0)
    return area_alt(p1, p2) + area_alt(p3, p4) - area_alt(x, y)


def solver_alt(data: List[tuple]) -> float:
    points = lambda m, n=2: tuple([m[x:x+n] for x in range(0, len(m), n)])
    area = lambda a, b: (b[0] - a[0]) * (b[1] - a[1])
    f = lambda a, b, g: (g(a[0], b[0]), g(a[1], b[1]))
    (p1, p2), (p3, p4) = points(data[0]), points(data[1])
    x, y = f(p1, p3, max), f(p2, p4, min)
    (x, y) = ((0, 0), (0, 0)) if max(x) > min(y) else (x, y)
    return area(p1, p2) + area(p3, p4) - area(x, y)


solver_dataclass.__doc__ = """\
Returns the total area of two rectangles (fields).

:param data: Points of the rectangles
:return: Total area
:rtype: float

..Note:

    p1, p2: bottom left point and top right point (R1)
    p3, p4: bottom left point and top right point (R2)
"""


class Test(TestCase):
    data = (
        ("1 1 3 4", "2 3 6 7", 21),
        ("0 0 2 2", "2 2 4 4", 8),
        ("1 1 4 3", "2 4 7 6", 16),
        ("1 1 2 2", "4 3 5 4", 2),
        ("0 0 5 3", "1 1 4 2", 15),
        ("1 1 4 5", "2 1 6 5", 20),
        ("1 1 6 5", "2 2 5 4", 20),
        ("1 1 5 4", "2 2 5 4", 12),
        ("1 1 5 5", "2 2 7 4", 20),
        ("2 1 5 2", "2 4 4 5", 5),
        ("5 1 7 3", "1 1 4 5", 16),
        ("5 1 7 3", "4 5 1 1", 16),
        ("1 1 4 5", "5 1 7 3", 16),
        ("4 5 1 1", "7 3 5 1", 16),
    )
    functions = (
        solver_namedtuple,
        solver_dataclass,
        solver_alt_helpers,
        solver_alt,
    )
    
    def test_process_input(self):
        self.assertEqual([
            (1, 1, 3, 4), (2, 3, 6, 7)], 
            process_input("1 1 3 4", "2 3 6 7")
            )
    
    def test_solvers(self):
        for function in self.functions:
            for s1, s2, total_area in self.data:
                points = process_input(s1, s2)
                self.assertEqual(function(points), total_area)


if __name__ == "__main__":
    main()