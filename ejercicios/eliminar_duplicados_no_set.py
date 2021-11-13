"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Eliminar duplicados de la lista ['a', 'b', 'c', 'a', 'c', 'c']
"""

# usando set:
letras = ['a', 'b', 'c', 'a', 'c', 'c']
print(set(letras))

# sin usar set:
sin_duplicados = []
for letra in letras:
    if letra not in sin_duplicados:
        sin_duplicados.append(letra)
print(sin_duplicados)
