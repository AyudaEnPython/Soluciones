"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Utilizando 3 vectores de 10 posiciones c/u, guardar en el primer vector
los números consecutivos a partir de 5, en el segundo vector el
cuadrado de los números almacenados en el primer vector, y en el tercer
vector la diferencia de los números del segundo vector menos los
valores del primer vector.

Vector 1
+-----+-----+-----+-----+-----+-----+-----+
|  5  |  6  |  7  |  8  |  9  | ... | ... |
+-----+-----+-----+-----+-----+-----+-----+

Vector 2
+-----+-----+-----+-----+-----+-----+-----+
| 25  | 36  | 49  | 64  | 81  | ... | ... |
+-----+-----+-----+-----+-----+-----+-----+

Vector 3
+-----+-----+-----+-----+-----+-----+-----+
|  20 | 30  | 42  | 56  | 72  | ... | ... |
+-----+-----+-----+-----+-----+-----+-----+
"""
# pip install prototools
from prototools import show_matrix

INITIAL, SIZE = 5, 10


def main():
    a = []*SIZE
    b = []*SIZE
    c = []*SIZE
    for x in range(INITIAL, INITIAL+SIZE):
        a.append(x)
    for i in range(SIZE):
        b.append(a[i]**2)
    for i in range(SIZE):
        c.append(b[i] - a[i])
    for i, v in enumerate((a, b, c), 1):
        print(f"Vector {i}")
        show_matrix(v)


def main_alt():
    a = [x for x in range(INITIAL, INITIAL+SIZE)]
    b = [x ** 2 for x in a]
    c = [x - y for x, y in zip(b, a)]
    for i, v in enumerate((a, b, c), 1):
        print(f"Vector {i}")
        show_matrix(v)


if __name__ == "__main__":
    main()
    # main_alt()
