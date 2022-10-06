"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List, Dict

FICHERO: str = "script.py"
ADVERTENCIAS: Dict[str, str] = {
    "E501": "Linea demasiado larga",
}


def leer_fichero(fichero: str) -> List[str]:
    """Lee el fichero *.py a ser analizado.

    :param fichero: Nombre del fichero a leer.
    :fichero: str
    :return: Lista de líneas del fichero.
    :rtype: List[str]
    """
    with open(fichero, "r") as f:
        return f.read().splitlines()


def analizar(lineas: List[str]) -> List[List[str]]:
    """Analiza linea a linea el codigo fuente.

    :param lineas: Lista de líneas del codigo fuente.
    :type lineas: List[str]
    :return: Lista de advertencias.
    :rtype: List[List[str]]
    """
    advertencias = []
    for i, linea in enumerate(lineas):
        if len(linea) > 79:
            advertencias.append([i, linea, ADVERTENCIAS["E501"]])
    return advertencias


def resultados(advertencias: List[str]) -> None:
    """Impresión de resultados.

    :param advertencias: Lista de advertencias.
    :type advertencias: List[str]
    """
    for linea, codigo, advertencia in advertencias:
        print(f"Línea {linea + 1}: {codigo} -- {advertencia}")


def main():
    codigo = leer_fichero(FICHERO)
    resultados(analizar(codigo))


if __name__ == "__main__":
    main()
