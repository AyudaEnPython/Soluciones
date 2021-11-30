"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dada la siguiente matriz de países y medallas:

    +----------------+--------+--------+--------+
    |      País      |  Oro   | Plata  | Bronce |
    +----------------+--------+--------+--------+
    | Estados Unidos |   40   |   35   |   29   |
    +----------------+--------+--------+--------+
    |     Rusia      |   39   |   32   |   28   |
    +----------------+--------+--------+--------+
    |   Inglaterra   |   26   |   33   |   27   |
    +----------------+--------+--------+--------+
    |     China      |   23   |   30   |   26   |
    +----------------+--------+--------+--------+
    |    Alemania    |   22   |   31   |   27   |
    +----------------+--------+--------+--------+

Implemente un algoritmo que realice lo siguiente:

- Crea la matriz de datos en el programa principal.
- Calcule e imprima el total de cada medalla.
- Calcule e imprima la medalla que ha sido repartida más veces.

La salida de este programa sería:

    +-------------------------------------+
    | Oro: 1500                           |
    | Plata: 1610                         |
    | Bronce: 1370                        |
    | La medalla más repartida fue: Plata |
    +-------------------------------------+
"""
# pip install prototools
from prototools import tabulate

m = [
    [40, 35, 29],
    [39, 32, 28],
    [26, 33, 27],
    [23, 30, 26],
    [22, 31, 27],
]

medallas = ["Oro", "Plata", "Bronce"]
max_ = [sum([i[j] for i in m]) for j in range(len(m[0]))]
result = {k:v for k,v in zip(medallas, max_)}

# Opcional ===================================================================
paises = ("Estados Unidos", "Rusia", "Inglaterra", "China", "Alemania")
for i in range(len(m)):
    m[i].insert(0, paises[i])
medallas.insert(0, "Pais")
print(tabulate(m, headers=medallas, align="center", inner=True))
medallas.pop(0)
# ============================================================================

for medalla in medallas:
    print(f"{medalla}: {result[medalla]}")
print(f"La medalla más repartida fue: {max(result, key=result.get)}")