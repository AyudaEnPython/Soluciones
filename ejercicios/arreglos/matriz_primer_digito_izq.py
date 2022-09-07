"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Ejemplo:

+-----+-----+-----+-----+    +---+---+---+---+
| 123 | 112 | 548 | 896 |    | 1 | 1 | 5 | 8 |
+-----+-----+-----+-----+    +---+---+---+---+
| 456 | 321 | 236 | 563 |    | 4 | 3 | 2 | 5 |
+-----+-----+-----+-----+ -> +---+---+---+---+
| 789 | 159 | 214 | 458 |    | 7 | 1 | 2 | 4 |
+-----+-----+-----+-----+    +---+---+---+---+
| 101 | 357 | 478 | 459 |    | 1 | 3 | 4 | 4 |
+-----+-----+-----+-----+    +---+---+---+---+
"""
from random import randint
# from math import log10
# pip install prototools
from prototools import show_matrix

n = 4
arr = [[randint(100, 1000) for _ in range(n)] for _ in range(n)]
sol = lambda arr: [[int(str(n)[0]) for n in row] for row in arr]  # noqa: E731
# sol = lambda arr: [[n//100 for n in row] for row in arr]  # noqa: E731
# sol = lambda arr: [[int(n / pow(10, int(log10(n)))) for n in row] for row in arr]  # noqa: E731, E501

show_matrix(arr)
show_matrix(sol(arr))
