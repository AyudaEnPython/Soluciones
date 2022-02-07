"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


class Punto:

    """Representación de un punto en coordenadas polares.

    :param x: coordenada x del punto.
    :x type: int
    :param y: coordenada y del punto.
    :y type: int
    """

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def cuadrante(self) -> str:
        """Devuelve el cuadrante en el que se encuentra el punto."""
        return f"{self} se encuentra en el {self._posicion()}."

    def _posicion(self) -> str:
        if self.x > 0 and self.y > 0:
            return "I° cuadrante"
        elif self.x < 0 and self.y > 0:
            return "II° cuadrante"
        elif self.x < 0 and self.y < 0:
            return "III° cuadrante"
        elif self.x > 0 and self.y < 0:
            return "IV° cuadrante"
        elif self.x != 0 and self.y == 0:
            return "eje X"
        elif self.x == 0 and self.y != 0:
            return "eje Y"
        else:
            return "origen"

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
