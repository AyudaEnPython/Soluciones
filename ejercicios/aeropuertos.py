"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Recopilamos los registros de los vuelos que ocurrieron durante un día
entre aeropuertos ubicados en Estados Unidos y los organizamos en un
diccionario de diccionarios. Ahora queremos que nos ayudes a
identificar si hay aeropuertos a los cuales hayan llegado vuelos
durante ese día, pero no hayan salido vuelos.

El parámetro vuelos de la función es un diccionario de diccionarios con
la información de los vuelos.
Las llaves en este diccionario son el código de cada vuelo.
Los valores en este diccionario son diccionarios con la información de
un vuelo, organizado de acuerdo con las siguientes llaves:

- aerolínea, que corresponde al nombre de la aerolínea
- origen, que corresponde al código de aeropuerto de origen
- destino, que corresponde al aeropuerto destino del vuelo
- distancia, que corresponde a la distancia entre el origen y el destino
- retraso, que corresponde a la cantidad de minutos de retraso que tuvo
el vuelo
- duracion, que corresponde a la duración planeada del vuelo en minutos
- salida, que corresponde a un entero que representa la hora de salida.

La hora de salida se representa usando la hora en formato 24 horas
multiplicada por 100 más la cantidad de minutos (por ejemplo, las 2007
indica que el vuelo salió a las 8:07 pm).
"""
from typing import Dict, List, Union

vuelos = {
    "DL123": {
        "aerolinea": "Latam", "origen": "Peru", "destino": "Colombia",
        "distancia": 8156, "retraso": 12, "duracion": 24, "salida": 1707
    },
    "FY453": {
        "aerolinea": "DHL", "origen": "Colombia", "destino": "Bolivia",
        "distancia": 4356, "retraso": 23, "duracion": 72, "salida": 1208
    },
    "RE542": {
        "aerolinea": "Crossfire", "origen": "Argentina", "destino": "Honduras",
        "distancia": 2134, "retraso": 18, "duracion": 36, "salida": 1545
    },
    "TY765": {
        "aerolinea": "EricRojo", "origen": "Bolivia", "destino": "Ecuador",
        "distancia": 5642, "retraso": 20, "duracion": 10, "salida": 1650
    },
    "TR675": {
        "aerolinea": "Oltursa", "origen": "Chile", "destino": "Bolivia",
        "distancia": 8346, "retraso": 16, "duracion": 16, "salida": 1930
    },
}


def sin_salida_naive(vuelos: Dict[str, Dict[str, Union[str, float]]]) -> List[str]:
    """Retorna una lista de aeropuertos a los cuales hayan llegado vuelos
    pero no hayan salido vuelos de este.

    :param vuelos: Información de los vuelos.
    :vuelos type: Dict[str, Dict[str, Union[str, float]]]
    :return: Lista de aeropuertos
    :rtype: List[str]
    """
    salidas, llegadas, aeropuertos = [], [], []
    for vuelo in vuelos.values():
        salidas.append(vuelo['origen'])
        llegadas.append(vuelo['destino'])
    for aeropuerto in llegadas:
        if aeropuerto not in salidas:
            aeropuertos.append(aeropuerto)
    return aeropuertos


def sin_salida_naive_alt(vuelos: Dict[str, Dict[str, Union[str, float]]]) -> List[str]:
    """Retorna una lista de aeropuertos a los cuales hayan llegado vuelos
    pero no hayan salido vuelos de este.

    :param vuelos: Información de los vuelos.
    :vuelos type: Dict[str, Dict[str, Union[str, float]]]
    :return: Lista de aeropuertos
    :rtype: List[str]
    """
    salidas, llegadas = [], []
    for vuelo in vuelos.values():
        salidas.append(vuelo['origen'])
        llegadas.append(vuelo['destino'])
    return [a for a in llegadas if a not in salidas]


def sin_salida_alt_list(vuelos: Dict[str, Dict[str, Union[str, float]]]) -> List[str]:
    """Retorna una lista de aeropuertos a los cuales hayan llegado vuelos
    pero no hayan salido vuelos de este.

    :param vuelos: Información de los vuelos.
    :vuelos type: Dict[str, Dict[str, Union[str, float]]]
    :return: Lista de aeropuertos
    :rtype: List[str]
    """
    return [a for a in [v["destino"] for v in vuelos.values()]
            if a not in [v["origen"] for v in vuelos.values()]]


def sin_salida_alt_dict(vuelos: Dict[str, Dict[str, Union[str, float]]]) -> List[str]:
    """Retorna una lista de aeropuertos a los cuales hayan llegado vuelos
    pero no hayan salido vuelos de este.

    :param vuelos: Información de los vuelos.
    :vuelos type: Dict[str, Dict[str, Union[str, float]]]
    :return: Lista de aeropuertos
    :rtype: List[str]
    """
    t = {v["origen"]: v["destino"] for v in vuelos.values()}
    return [a for a in t.values() if a not in t]


def main():
    print(sin_salida_naive(vuelos))


if __name__ == "__main__":
    main()