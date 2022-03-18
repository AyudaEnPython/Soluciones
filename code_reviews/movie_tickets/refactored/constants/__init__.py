"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Any, Dict, List, Tuple, Union

DataList = List[str]
Data = List[List[Any]]
QueryResult = Tuple[bool, List[List[Any]]]
Token = Dict[str, str]

DATA = "data/registro.csv"
CREDENTIALS = "data/credenciales.json"
MOVIES = "data/movies.txt"

CONVERSION: Dict[str, Union[int, float]] = {"local": 1, "foreign": 0.27}
CFG = {"padx": 5,"pady": 5}
DIAS = (
    'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'
)
LABELS: Tuple[str, str, str, str] = (
    "Identificación",
    "Cantidad de Tickets",
    "Dias disponibles",
    "Películas disponibles",
)
MAP = {
    "id": "Identificación",
    "cantidad": "Cantidad de Tickets",
    "dia": "Dias disponibles",
    "pelicula": "Películas disponibles",
    "total": "Total",
}
PRICE = {
    "lun-mar": 20_000,
    "mie-jue": 15_000,
    "vie-sab": 30_000,
    "dom": 35_000,
}