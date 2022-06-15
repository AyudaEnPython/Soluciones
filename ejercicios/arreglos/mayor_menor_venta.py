"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Elaborar un algoritmo para leer 30 días de ventas realizadas por un
empleado, y que imprima el día en que tuvo la mayor y la menor venta,
así como las cantidades correspondientes.
"""
from typing import List


def main():
    dias: List[int] = []
    for i in range(1, 31):
        dias.append(int(input(f"Ingrese ventas del dia {i}: ")))
    print(f"El dia con mayor venta es el {dias.index(max(dias))+1}")
    print(f"El dia con menor venta es el {dias.index(min(dias))+1}")


if __name__ == "__main__":
    main()
