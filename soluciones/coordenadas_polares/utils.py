from random import randint
from typing import List, Tuple


def _ingresar_coordenadas() -> Tuple[int, int]:
    """Ingreso de coordenadas.

    :return: Coordenadas x e y
    :rtype: Tuple[int, int]
    """
    x = int(input("x: "))
    y = int(input("y: "))
    return x, y


def crear_coordenadas(
    class_: object,
    n: int = 4,
    rango: Tuple[int, int] = (-10, 10)
) -> List[object]:
    """Crea una lista de coordenadas aleatorias enteras.

    :param class_: Clase de la cual se crearán las coordenadas.
    :class_ type: object
    :param n: Cantidad de coordenadas a crear.
    :n type: int
    :param rango: Rango de valores de las coordenadas.
    :rtype: Tuple[int, int]
    :return: Lista de coordenadas.
    :rtype: List[object]
    """
    return [class_(randint(*rango), randint(*rango)) for _ in range(n)]


def crear_coordenadas_usuario(class_: object) -> List[object]:
    """Crea una lista de coordenadas ingresadas por el usuario.

    :param class_: Clase de la cual se crearán las coordenadas.
    :class_ type: object
    :return: Lista de coordenadas.
    :rtype: List[object]
    """
    n = int(input("Ingresar cantidad de coordenadas: "))
    return [class_(*_ingresar_coordenadas()) for _ in range(n)]


def mostrar(coordenadas: List[Tuple[int, int]]) -> None:
    """Muestra el cuadrante al que pertenece cada coordenada.

    :param coordenadas: Lista de coordenadas
    :type coordenadas: List[Tuple[int, int]]
    """
    for coordenada in coordenadas:
        print(coordenada.cuadrante())
