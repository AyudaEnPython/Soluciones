"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

El fichero cotizacion.csv contiene las cotizaciones de las empresas del
IBEX35 con las siguientes columnas: Nombre(nombre de la empresa), Final
(precio de la acción al cierre de la bolsa), Máximo (precio máximo de
la acción durante la jornada), Mínimo (precio mínimo de la acción
durante la jornada), Volumen (volumen al cierre de la bolsa), Efectivo
(capitalización al cierre en miles de euros).

1. Construir una función que reciba el fichero de cotizaciones y
    devuelva un diccionario con los datos del fichero por columnas.
2. Construir una función que reciba el diccionario devuelto por la
    función anterior y cree un fichero en formato csv con el mínimo, el
    máximo y la media de dada columna.
"""
import locale
from statistics import mean
from typing import Dict, List


def parse_number(number: str, locale_: str = "es_ES") -> float:
    """Parsea un número a float.

    :param number: Número a parsear
    :number type: str
    """
    locale.setlocale(locale.LC_ALL, locale_)
    return locale.atof(number)


def get_data(filename: str) -> Dict[str, List[str]]:
    """Obtiene los datos de un fichero csv.

    :param filename: Nombre del fichero en formato csv
    :filename type: str
    """
    with open(f"{filename}.csv", "r", encoding="utf-8") as f:
        data = [line.split(";") for line in f.read().splitlines()]
    for i in range(1, len(data)):
        for j in range(1, len(data[i])):
            data[i][j] = parse_number(data[i][j])
    return {
        label: [row[i] for row in data[1:]]
        for i, label in enumerate([s for s in data[0]])
    }


def get_min_max_avg(data: Dict[str, List[str]]) -> None:
    """Obtiene los valores mínimo, máximo y media de cada columna
    y los guarda en un fichero csv.

    :param data: Diccionario con los datos del fichero
    :data type: Dict[str, List[str]]
    """
    _, *tags = list(data.keys())
    print(data)
    data_ = [
        (min(data[tag]), max(data[tag]), mean([float(x) for x in data[tag]]))
        for tag in tags
    ]
    with open("min_max_avg.csv", "w", encoding="utf-8") as f:
        f.write("columna,min,max,avg\n")
        for col, row in zip(tags, data_):
            f.write(f"{col},{','.join([str(x) for x in row])}\n")


def main():
    get_min_max_avg(get_data("cotizacion"))


if __name__ == "__main__":
    main()
