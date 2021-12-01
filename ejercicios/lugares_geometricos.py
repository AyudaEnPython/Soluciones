"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un programa en Python que lea las coordenadas de dos puntos P
y Q, junto con dos números reales r1 y r2, donde P es el centro de una
o dos circunferencias concéntricas de radios respectivos r1 y r2. El
algoritmo debe determinar en qué lugar geométrico que determinan las
circunferencias se encuentra un punto Q. En la solución se debe tener
en cuenta:

- Si los dos números reales r1 y r2 son positivos la entrada debe
    considerarse como válida sin que el programa le imponga cualquier
    otra condición al usuario para el ingreso de datos. Si la entrada
    no es válida solo basta con informarle al usuario y terminar.
- Los lugares geométricos a determinar son tanto las circunstancias
    como los lugares que ellas definen. Por ejemplo: el interior de la
    circunferencia de menor radio, la circunferencia de mayor radio, el
    exterior de la circunferencia de mayor radio, etc.

Ejecuta el programa con los mismos datos para la circunferencia, pero
con distintos puntos Q de tal forma que se muestre todas las posibles
respuestas del programa.

TODO: add testcases.
"""
from dataclasses import dataclass
from typing import Tuple
# pip install prototools
from prototools import custom_input, float_input

results = {
    1: "Q{} está en el interior de la circunferencia de menor radio ({}).",
    2: "Q{} está en el exterior de la circunferencia de menor radio ({}).",
    3: "Q{} está en el interior de la circunferencia de mayor radio ({}).",
    4: "Q{} está en el exterior de la circunferencia de mayor radio ({}).",
    5: "Q{} está sobre la circunferencia de menor radio {}.",
    6: "Q{} está sobre la circunferencia de mayor radio {}.",
    7: "Q{} está en el centro de ambas circunferencias.",
}


@dataclass(order=True)
class Point:
    x: float
    y: float

    @staticmethod
    def dist(a, b) -> float:
        return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'


def datos() -> Tuple[Point, Point]:
    p = custom_input("> P ( ", ")")
    p = p.split(",")
    q = custom_input("> Q ( ", ")")
    q = q.split(",")
    if len(p) != 2 or len(q) != 2:
        print("\nLa entrada no es válida.\n")
        return
    try:
        p = Point(*map(float, p))
        q = Point(*map(float, q))
        return p, q
    except ValueError:
        print("\nLa entrada no es válida.\n")
        return


def evaluar(p: Point, q: Point, r1: int, r2: int) -> None:
    d = Point.dist(p, q)
    if r1 > r2:
        r1, r2 = r2, r1
    if d == 0:
        print(results[7].format(q))
    elif d < r1:
        print(results[1].format(q, r1))
    elif d == r1:
        print(results[5].format(q, r1))
    elif r1 < d < r2:
        print(results[2].format(q, r1))
        print(results[3].format(q, r2))
    elif d == r2:
        print(results[6].format(q, r2))
    elif d > r2:
        print(results[4].format(q, r2))


def main():
    try:
        p, q = datos()
    except TypeError:
        return
    r1 = float_input("> r1: ", min=0)
    r2 = float_input("> r2: ", min=0)
    evaluar(p, q, r1, r2)


if __name__ == "__main__":
    main()