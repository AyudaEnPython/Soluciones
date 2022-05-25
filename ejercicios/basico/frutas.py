"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Leer el nombre de 10 frutas para preparar un salpicón; el programa debe
permitir mostrar las 10 frutas ingresadas al mismo tiempo en sentido
inverso al ingresado.

NOTE: el enunciado no es claro.
"""

for _ in range(10):
    fruta = input("> ")
    print(fruta[::-1])
