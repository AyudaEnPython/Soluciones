"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Usando un ciclo for, escribe el siguiente programa: todos los números
de dos dígitos que son iguales al doble del producto de los dígitos
que conforman el número brindado se muestran en una columna.
"""

for n in range(10, 100):
    x, y = str(n)
    if 2 * int(x) * int(y) == n:
        print(n)

# oneliner:
# print(*[n for n in range(10, 100) if 2 * int(str(n)[0]) * int(str(n)[1]) == n])
