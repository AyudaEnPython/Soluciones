from typing import List, Tuple

def _helper(arr: list, n: int = 2) -> Tuple:
    return tuple([arr[x:x+n] for x in range(0, len(arr), n)])

def process_input(s1: str, s2: str) -> List[tuple]:
    return [tuple(map(int, value.split())) for value in (s1, s2)]

def point_factory(class_: object, data: List[tuple]) -> List[object]:
    return [class_(*points) for value in data for points in _helper(value)]

def rectangle_factory(class_: object, points: List[object]) -> List[object]:
    return [class_(x, y) for x, y in _helper(points)]

def area(a: tuple, b: tuple) -> float:
    return (b.x - a.x) * (b.y - a.y)

def max_(a: tuple, b: tuple) -> Tuple:
    return max(a.x, b.x), max(a.y, b.y)

def min_(a: tuple, b: tuple) -> Tuple:
    return min(a.x, b.x), min(a.y, b.y)

def area_alt(a: tuple, b: tuple) -> float:
    return (b[0] - a[0]) * (b[1] - a[1])

def max_alt(a: tuple, b: tuple) -> Tuple:
    return max(a[0], b[0]), max(a[1], b[1])

def min_alt(a: tuple, b: tuple) -> Tuple:
    return min(a[0], b[0]), min(a[1], b[1])