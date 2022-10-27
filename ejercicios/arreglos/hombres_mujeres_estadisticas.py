"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
Diseñe un algoritmo utilizando listas, en este caso llamarlo lst_talla,
lst_peso, lst_edad. Se desconoce la cantidad de elementos persona.
Se pide:

- Unos métodos para cargar las listas necesarias (No recibe en
    parámetros, devuelve valor es decir la lista)
- Un método para promedio de talla de mujeres (Recibe parámetros,
    devuelve valor, es decir el promedio)
- Un método para la cantidad de varones con peso mayor a 40kg y talla
    menor a 90cm. (Recibe un parámetros, devuelve valor, es decir
    cantidad de varones con la condición dada)
- Un método para porcentaje de mujeres y varones. (Recibe en
    parámetros, No devuelve valor, es decir cantidad de varones con la
    cantidad dada)

NOTE: El enunciado presenta errores.
"""
# pip install prototools
from prototools import int_input, float_input, menu_input

GENERO = "Masculino", "Femenino"
UMBRAL_PESO_M = 40
UMBRAL_TALLA_M = 90


def _porcentaje(x, y):
    return round(100 * (x/y), 1)


def _cantidad(datos, idx, valor):
    return sum(1 for dato in datos if dato[idx] == valor)


def ingresar_datos(n):
    datos = []
    for i in range(n):
        genero = menu_input(GENERO, numbers=True, lang="es")[0]
        talla = float_input(f"[{i+1}] Estatura: ")
        peso = float_input(f"[{i+1}] Peso: ")
        edad = int_input(f"[{i+1}] Edad: ")
        datos.append([genero, talla, peso, edad])
    return datos


def calcular_promedio(datos, idx, valor="F"):
    n = _cantidad(datos, 0, valor)
    try:
        return sum(dato[idx] for dato in datos if dato[0] == valor)/n
    except ZeroDivisionError:
        return 0


def calcular_varones_umbral(datos, s="M"):
    return sum(
        1 for genero, talla, peso, _ in datos
        if genero == s and peso > UMBRAL_PESO_M and talla < UMBRAL_TALLA_M
    )


def porcentaje(datos):
    len_ = len(datos)
    hombres = _cantidad(datos, 0, "M")
    mujeres = _cantidad(datos, 0, "F")
    return _porcentaje(hombres, len_), _porcentaje(mujeres, len_)


def main():
    n = int(input("Ingresar cantidad de personas: "))
    datos = ingresar_datos(n)
    print(f"Estatura promedio (mujeres): {calcular_promedio(datos, 1)}")
    print(
        f"Peso mayor a {UMBRAL_PESO_M}kg y estatura menor a "
        f"{UMBRAL_TALLA_M}cm (hombres): {calcular_varones_umbral(datos)}"
    )
    hombres, mujeres = porcentaje(datos)
    print(f"Porcentaje (hombres): {hombres}")
    print(f"Porcentaje (mujeres): {mujeres}")


if __name__ == "__main__":
    main()
