from typing import Any, Dict, List, Tuple, Union

Data: List[List[Any]]
DataList: List[str]
QueryResult: Tuple[bool, Data]

CONVERSION: Dict[str, Union[int, float]] = {"local": 1, "foreign": 0.27}
DATA = "data/registro.csv"
MOVIES = "data/movies.txt"
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