"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from calendar import isleap
from datetime import datetime
from typing import Dict, List, Tuple

MESES: Tuple[str, ...] = (
    'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
    'julio', 'agosto', 'setiembre', 'octubre', 'noviembre', 'diciembre'
)
MES: Dict[str, int] = {k: v for k, v in zip(
    MESES,
    (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
)}
_T: Dict[int, str] = {k: v for k, v in zip(range(1, 11), MESES)}
_S: Dict[int, Tuple[Tuple[int, ...]]] = {
    7: (slice(0, 1, 1), slice(1, 3, 1), slice(3, 7, 1)),
    8: (slice(0, 2, 1), slice(2, 4, 1), slice(4, 8, 1)),
}


def _fecha(fecha: int) -> List[int]:
    fecha = str(fecha)
    return list(map(int, [fecha[s] for s in _S[len(fecha)]]))


def _escribir(fecha: int) -> str:
    dd, mm, yy = _fecha(fecha)
    return f"{dd} {_T[mm]} {yy}"


def dia_mes(m: int, yy: int) -> int:
    days = MES[_T[m]]
    return days + 1 if isleap(yy) else days


def es_fecha(fecha: int) -> bool:
    fecha = str(fecha)
    if len(fecha) < 7 or len(fecha) > 8:
        return False
    dd, mm, yy = _fecha(fecha)
    if 0 < dd < dia_mes(mm, yy) and mm in _T:
        return True
    return False


def comparar(a: int, b: int) -> int:
    a = datetime(*_fecha(a)[::-1])
    b = datetime(*_fecha(b)[::-1])
    return 0 if a == b else (1 if a > b else -1)


def escribir(fecha: int) -> None:
    print(_escribir(fecha))
