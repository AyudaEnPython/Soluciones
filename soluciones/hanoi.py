"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Usando la clase pila, implemente la solución del juego de las Torres
de Hanoi (mínimo debe funcionar para 3 discos).
"""
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/pilas.py
from pilas import Pila


class Hanoi:

    def __init__(self, discos, l, m, r) -> None:
        self.discos = discos
        self.torres = {
            l: Pila(),
            m: Pila(),
            r: Pila()
        }
        for i in range(discos, 0, -1):
            self.torres[l].push(i)

    def mover_disco(self, l, r):
        self.torres[r].push(self.torres[l].pop())
        print(f"{r} -> {l}")

    def mover_torre(self, n, l, m, r):
        if n >= 1:
            self.mover_torre(n - 1, l, r, m)
            self.mover_disco(l, r)
            self.mover_torre(n - 1, m, l, r)


if __name__ == "__main__":
    hanoi = Hanoi(3, 'A', 'B', 'C')
    hanoi.mover_torre(3, 'A', 'B', 'C')