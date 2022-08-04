"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

MIN, MAX = 0, 20
ERROR_MSG = f"El valor debe ser un número mayor a {MIN:.1f} y menor a {MAX:.1f}"


def _validate(n: float, msg: str = ERROR_MSG) -> float:
    try:
        n = float(n)
        if MIN < n < MAX:
            return n
    except ValueError:
        raise ValueError(msg)
    raise ValueError(msg)


class Rectangulo:

    def __init__(self, longitud: float = 1, anchura: float = 1) -> None:
        self._longitud = _validate(longitud)
        self._anchura = _validate(anchura)

    @property
    def longitud(self) -> float:
        return self._longitud

    @longitud.setter
    def longitud(self, longitud: float) -> None:
        self._longitud = _validate(longitud)

    @property
    def anchura(self) -> float:
        return self._anchura

    @anchura.setter
    def anchura(self, anchura: float) -> None:
        self._anchura = _validate(anchura)

    def perimetro(self) -> float:
        return 2 * (self._longitud + self._anchura)

    def area(self) -> float:
        return self._longitud * self._anchura

    def __str__(self) -> str:
        return f"Rectangulo({self._longitud}, {self._anchura})"


if __name__ == "__main__":
    rectangulo = Rectangulo()
    assert rectangulo.longitud == 1
    assert rectangulo.anchura == 1
    rectangulo.longitud = 10
    rectangulo.anchura = 5
    print(rectangulo)
    assert rectangulo.perimetro() == 30
    print(f"Perímetro: {rectangulo.perimetro():.1f}")
    assert rectangulo.area() == 50
    print(f"Área: {rectangulo.area():.1f}")
