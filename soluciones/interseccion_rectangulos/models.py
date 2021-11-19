"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from collections import namedtuple
from typing import Tuple, Type
from dataclasses import dataclass

Point_ = namedtuple("Point_", "x y")


@dataclass(order=True)
class Point:
    x: float
    y: float

    @staticmethod
    def max_(a, b) -> Tuple[float, float]:
        return max(a.x, b.x), max(a.y, b.y)

    @staticmethod
    def min_(a, b) -> Tuple[float, float]:
        return min(a.x, b.x), min(a.y, b.y)

    def __sub__(self, other: Type["Point"]) -> Type["Point"]:
        return Point(abs(self.x - other.x), abs(self.y - other.y))


@dataclass(order=True)
class Rectangle:
    bl: Point
    tr: Point

    def __post_init__(self) -> None:
        p = self.tr - self.bl
        self.w, self.h = p.x, p.y
    
    def area(self) -> float:
        return self.w * self.h