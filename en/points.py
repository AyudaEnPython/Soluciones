"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english
speakers are welcome.
"""
import pprint
from random import random


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"


points = [Point(random(), random()) for _ in range(6)]
pprint.pprint(points)

# output:
# [Point(0.0936581990985863, 0.7656646716638154),
#  Point(0.8876376436791956, 0.5291663094799327),
#  Point(0.431149343848124, 0.09748661733209496),
#  Point(0.8025570219318642, 0.7045163531204794),
#  Point(0.2708733864963654, 0.9144483540886966),
#  Point(0.7568795323245214, 0.7165259876633254)]