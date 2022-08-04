"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List, Tuple, Optional, Union

MIN = 0
ERROR_MSG = "Error: El valor no puede ser negativo"
ASSERT_ERROR = "Error: Debe contener 3 elementos"


def _validate(n: float, msg: str = ERROR_MSG) -> float:
    if n >= MIN:
        return n
    raise ValueError(msg)


class Point3D:

    __slots__ = "x", "y", "z"

    def __init__(
        self,
        x: Optional[Union[float, List[float], Tuple[float, ...]]] = 0,
        y: Optional[float] = 0,
        z: Optional[float] = 0,
    ) -> None:
        if isinstance(x, (int, float)):
            self.x = x
            self.y = y
            self.z = z
        elif isinstance(x, (list, tuple)):
            try:
                assert len(x) == 3
                self.x, self.y, self.z = x
            except AssertionError:
                raise ValueError(ASSERT_ERROR)


class Point4D(Point3D):

    def __init__(
        self,
        x: Optional[Union[float, List[float], Tuple[float, ...]]] = 0,
        y: Optional[float] = 0,
        z: Optional[float] = 0,
        t: Optional[float] = 0,
    ) -> None:
        super().__init__(x, y, z)
        self._t = _validate(t)

    @property
    def t(self) -> float:
        return self._t

    @t.setter
    def t(self, t) -> None:
        self._t = _validate(t)

    def __str__(self) -> str:
        return f"Point4D({self.x}, {self.y}, {self.z}, {self.t})"


if __name__ == "__main__":
    punto = Point4D(-1.5, 2.3, -3.7, 4)
    print(punto)
