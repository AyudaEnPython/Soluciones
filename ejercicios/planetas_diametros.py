"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------ Enunciado Original -------------------------
Dado los siguientes diccionarios relacionados a los planetas del
sistema planetario solar, el cual contiene los siguientes atributos:
planeta y diámetro

    +-------------------------------------------------------+
    | mercurio = {'planeta': 'Mercurio', 'diametro': 4.878} |
    | venus = {'planeta': 'Venus', 'diametro': 12.104}      |
    | tierra = {'planeta': 'Tierra', 'diametro': 12.756}    |
    | marte = {'planeta': 'Marte', 'diametro': 6.794}       |
    | jupiter = {'planeta': 'Jupiter', 'diametro': 142.800} |
    | saturno = {'planeta': 'Saturno', 'diametro': 120.660} |
    | urano = {'planeta': 'Urano', 'diametro': 51.800}      |
    | neptuno = {'planeta': 'Neptuno', 'diametro': 49.500}  |
    +-------------------------------------------------------+

Se pide lo siguiente:
- Agregar los diccionarios a una lista
- Encontrar el planeta con diámetro más igual a 12.104 usando el
    algoritmo de búsqueda binaria.

    +-------------------------------------------------------+
    | Lista:                                                |
    | [{'planeta': 'Mercurio', 'diametro': 4.878},          |
    |  {'planeta': 'Venus', 'diametro': 12.104},            |
    |  {'planeta': 'Tierra', 'diametro': 12.756},           |
    |  {'planeta': 'Marte', 'diametro': 6.794},             |
    |  {'planeta': 'Jupiter', 'diametro': 142.800},         |
    |  {'planeta': 'Saturno', 'diametro': 120.660},         |
    |  {'planeta': 'Urano', 'diametro': 51.800},            |
    |  {'planeta': 'Neptuno', 'diametro': 49.500}]          |
    |                                                       |
    | El planeta con diámetro más igual a 12.104 es venus   |
    +-------------------------------------------------------+

# ---------------------------------------------------------------------
NOTE: El diccionario contiene 'llaves'('claves') y 'valores' mas no
    atributos. El ejercicio tiene partes redundantes e innecesarias
    (agregar los diccionarios a una lista).
"""
# Algoritmo de búsqueda binaria
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/algo_binary_search.py


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid]['diametro'] == x:
            return mid
        elif arr[mid]['diametro'] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


mercurio = {'planeta': 'Mercurio', 'diametro': 4.878}
venus = {'planeta': 'Venus', 'diametro': 12.104}
tierra = {'planeta': 'Tierra', 'diametro': 12.756}
marte = {'planeta': 'Marte', 'diametro': 6.794}
jupiter = {'planeta': 'Jupiter', 'diametro': 142.800}
saturno = {'planeta': 'Saturno', 'diametro': 120.660}
urano = {'planeta': 'Urano', 'diametro': 51.800}
neptuno = {'planeta': 'Neptuno', 'diametro': 49.500}

planetas = [
    mercurio, venus, tierra, marte, jupiter, saturno, urano, neptuno,
]
planetas = sorted(planetas, key=lambda planeta: planeta['diametro'])
i = binary_search(planetas, 12.104)
print(
    f"El planeta con diámetro más igual a 12.104 es {planetas[i]['planeta']}"
)
