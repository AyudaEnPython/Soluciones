"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Entre todos los números en el intervalo de 1 hasta 100, se pide contar
los números que son múltiplos de 4 y mostrar la suma de todos los
números multiplos de 4.
"""

c = s = 0
for i in range(1, 101):
    if i % 4 == 0:
        c += 1
        s += i
print(f"{c} números son múltiplos de 4 en el rango del 1 al 100 y suman {s}")
