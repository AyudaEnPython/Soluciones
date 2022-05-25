"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Existe un arreglo de tamaño 5 que representa una cola en el banco para
hacer un pago en ventanilla. Escriba un programa que pida ingresar un
número entero aleatorio como nuevo dato a la cola, así también pida
eliminar un dato de la cola (que representa que sale de la cola para
ser atentido en ventanilla).
Tener en cuenta que al agregar un dato se coloca al final de la cola y
al eliminar un dato de la cola se elimina el que está adelante y todos
corren un asiento. Ventanilla está cerca al índice 0 de la cola.
Mostrar la cola (arreglo) cada vez que se realiza una acción (agregar
o eliminar).
"""
from collections import deque
from random import randint
# pip install prototools
from prototools import main_loop, menu_input, int_input


def ventanilla(cola: deque) -> None:
    s = menu_input(("agregar", "eliminar"), numbers=True, lang="es")
    if s == "agregar":
        dato = int_input("Ingrese un dato: ", lang="es")
        cola.append(dato)
    else:
        cola.popleft()
    print(cola)


if __name__ == "__main__":
    cola = deque([randint(0, 10) for _ in range(5)])
    main_loop(ventanilla, args=(cola,))
