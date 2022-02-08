"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba un programa en Python para dividir una lista dada en dos partes
donde se da la longitud de la primera parte de la lista.

Lista originial:
[1, 1, 2, 3, 4, 4, 5, 1]

Longitud de la primera parte de la lista: 3

Dividida dicha lista en dos partes:
[[1, 1, 2], [3, 4, 4, 5, 1]]
"""

arr = [1, 1, 2, 3, 4, 4, 5, 1]
i = 3
arr = [arr[:i]] + [arr[i:]]

print(arr)
