"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba un programa que imprima cada elemento y su tipo correspondiente
de la siguiente lista.

Lista de muestra:
[1452, 11.23, 1+2j, True, 'Python', (0, -1), [5, 12], {"Clase": "V", "Seccion": "A"}]
"""

muestra = [
    1452, 11.23, 1+2j, True, 'Python', (0, -1),
    [5, 12], {"Clase": "V", "Seccion": "A"},
]

for elemento in muestra:
    print(f"{elemento} es de tipo {type(elemento).__name__}")
