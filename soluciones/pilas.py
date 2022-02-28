"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Multiplique los elementos de una pila por un valor. Solo se debe
utilizar funciones de pila (push y pop). Los elementos de la pila
resultante deberán estar en el orden original.

Reemplazar un elemento de una pila por otro.
"""
from typing import Any, List


class Pila:

    def __init__(self) -> None:
        self.items: List[Any] = []

    def push(self, item) -> None:
        self.items.append(item)
    
    def pop(self) -> None:
        if self.is_empty():
            raise Exception("La pila está vacía")
        return self.items.pop()
    
    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)


def multiplicar_pila(pila: Pila, valor: float) -> Pila:
    resultado, aux = Pila(), Pila()
    while not pila.is_empty():
        aux.push(pila.pop())
    while not aux.is_empty():
        resultado.push(valor * aux.pop())
    return resultado


def reemplazar_elemento(pila: Pila, valor: Any, nuevo_valor: Any) -> Pila:
    resultado, aux = Pila(), Pila()
    while not pila.is_empty():
        aux.push(pila.pop())
    while not aux.is_empty():
        tmp = aux.pop()
        if tmp == valor:
            tmp = nuevo_valor
        resultado.push(tmp)
    return resultado


if __name__ == "__main__":
    pila = Pila()
    pila.push(2)
    pila.push(3)
    pila.push(4)
    print(pila)
    pila = multiplicar_pila(pila, 5)
    print(pila)
    pila = reemplazar_elemento(pila, 15, 0)
    print(pila)
