"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------ Enunciado Original -------------------------
Un centro meteorológico ubicado en Matagalpa lleva los registros de los
promedios mensuales de temperaturas de las principales regiones de
Nicaragua. Existen 6 regiones denominadas: NORTE, CENTRO, SUR,
OCCIDENTE, PACÍFICO y CARIBE. Escriba un programa que obtenga lo
siguiente:

    a. El promedio anual de cada región.
    b. El menor y el registro con la mayor y la menor temperatura, y
        que además indiquen a que zona pertenecen estos registros.

Determinar cuál de las regiones SUR, PACÍFICO y CARIBE tiene el mayor
promedio de temperatura anual.
# ---------------------------------------------------------------------
NOTE: No es claro el enunciado, se opta por usar números aleatorios
    para simular los datos.
"""
from random import randint
from typing import Dict, List, Tuple

REGIONES: Tuple[str] = (
    "norte", "centro", "occidente", "sur", "pacifico", "caribe",
)
datos: Dict[str, List[int]] = {
    k: [randint(10, 34) for _ in range(12)] for k in REGIONES
}


def promedio_anual(dict_: Dict[str, List[int]]) -> Dict[str, int]:
    """Calcula el promedio anual de cada región.

    :param dict_: Diccionario con los datos de las regiones
    :dict_ type: Dict[str, List[int]]
    :return: Diccionario con los promedios anuales de cada región
    :rtype: Dict[str, int]
    """
    return {k: round(sum(v) / len(v), 2) for k, v in dict_.items()}


def menor_temperatura(dict_: Dict[str, List[int]]) -> Tuple[str, int]:
    """Determina el menor registro de cada región.

    :param dict_: Diccionario con los datos de las regiones
    :dict_ type: Dict[str, List[int]]
    :return: Tupla con el nombre de la región y el menor registro
    :rtype: Tuple[str, int]
    """
    return {k: min(v) for k, v in dict_.items()}


def limites_anual(dict_: Dict[str, List[int]]) -> Tuple[str, int, int]:
    """Determina el menor y el mayor registro de cada región.

    :param dict_: Diccionario con los datos de las regiones
    :dict_ type: Dict[str, List[int]]
    :return: Tupla con el nombre de la región, el menor registro y el
        mayor registro
    :rtype: Tuple[str, int, int]
    """
    return {k: (min(v), max(v)) for k, v in dict_.items()}


def mayor_promedio_anual(
    dict_: Dict[str, int], regiones: Tuple[str, ...]
) -> str:
    """Determina la región con mayor promedio anual dentro de un
    conjunto de regiones.

    :param dict_: Diccionario con los promedios anuales de las regiones
    :dict_ type: Dict[str, int]
    :param regiones: Tupla con las regiones a evaluar
    :regiones type: Tuple[str, ...]
    :return: Nombre de la región con mayor promedio anual
    :rtype: str
    """
    return max(regiones, key=dict_.get)


def main_():
    # print(datos)
    anual = promedio_anual(datos)
    menor = menor_temperatura(datos)
    limites = limites_anual(datos)
    print("Promedio anual por región")
    for k, v in anual.items():
        print(f"{k}: {v}")
    print(
        f"Menor temperatura: "
        f"{min(menor, key=menor.get)} {min(menor.values())}"
    )
    print("Menor y mayor temperatura por región")
    for k, v in limites.items():
        print(f"{k}: {', '.join(map(str, v))}")
    print(
        f"Mayor promedio anual: {mayor_promedio_anual(anual, REGIONES[3:])}"
    )


if __name__ == "__main__":
    main_()
