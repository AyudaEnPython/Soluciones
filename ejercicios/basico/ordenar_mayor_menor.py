"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realizar un programa en Python que ordene de MAYOR a MENOR la siguiente
secuencia.

[45, 78, 12, 10, 9, 7, 98, -96, 18, 79]
"""

ns = [45, 78, 12, 10, 9, 7, 98, -96, 18, 79]

for i in range(len(ns)):
    for j in range(i + 1, len(ns)):
        if ns[i] < ns[j]:
            ns[i], ns[j] = ns[j], ns[i]

print(ns)