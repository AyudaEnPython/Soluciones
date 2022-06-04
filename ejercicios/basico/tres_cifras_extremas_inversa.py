"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Digite un número aleatorio entero positivo de tres cifras, luego
visualice el nuevo formado por sus cifras extremas y la inversa
de dicho número.

Prueba des Escritorio:
n = 483
nnum = 43
inv_nnum = 34
"""
# ----------------------------------------------------------- version 1
c, d, u = input("n: ")
print(f"Número original: {c + d + u}")
print(f"Nuevo número: {c + u}")
print(f"Inverso del nuevo número: {u + c}")

# ----------------------------------------------------------- version 2
n = int(input("n: "))
c = n // 100
u = n % 10
nn = c * 10 + u
nni = u * 10 + c
print(f"Número original: {n}")
print(f"Nuevo número: {nn}")
print(f"Inverso del nuevo número: {nni}")

# ----------------------------------------------------------- version 3
from math import log10

n = int(input("n: "))
c = int(n / pow(10, int(log10(n))))
u = n % pow(10, int(log10(n/10)))
nn = c * 10 + u
nni = u * 10 + c
print(f"Número original: {n}")
print(f"Nuevo número: {nn}")
print(f"Inverso del nuevo número: {nni}")
