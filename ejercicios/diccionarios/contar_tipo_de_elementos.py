"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Contar los elementos de cada tipo de dato dentro de una lista y mostrar
la salida.

elementos = [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]
"""

data = [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]


def count_datatypes_(data):
    d = {}
    for e in data:
        k = type(e).__name__
        if k not in d:
            d[k] = 0
        d[k] += 1
    return d


def count_datatypes(data):
    d = {}
    for el in data:
        k = type(el).__name__
        d[k] = d.get(k, 0) + 1
    return d


print(count_datatypes_(data))
print(count_datatypes(data))
