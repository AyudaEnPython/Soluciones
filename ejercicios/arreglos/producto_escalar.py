"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dado dos vectores (listas) de la misma dimensión, utilice la función
zip() para calcular su producto escalar.
"""

v1 = [4, 3, 8, 1]
v2 = [9, 2, 7, 3]

# ---------------------------------------- usando for loop, sum y zip
producto_escalar = []
for x, y in zip(v1, v2):
    producto_escalar.append(x * y)
print(sum(producto_escalar))


# --------------------------------------- usando sum, generator y zip
producto_escalar = sum(x * y for x, y in zip(v1, v2))
print(producto_escalar)
