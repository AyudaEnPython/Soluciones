"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Simulador de dado simple

┌────────-┬-─────┬────────-┬──────┬─────────┬──────┐
│ Unicode │ Char │ Unicode │ Char │ Unicode │ Char │
└─────────┴──────┴─────────┴──────┴─────────┴──────┘
  u+2680     ⚀     u+2681     ⚁     u+2682     ⚂
  u+2683     ⚃     u+2684     ⚄     u+2685     ⚅
"""
from random import randint
from typing import Tuple


def lanzar(n: int = 2) -> Tuple[str, int]:
    """Lanza 'n' dados al azar. Devuelve un tupla con la representación
    de los dados lanzados y la suma de estos. 

    :param n: Número de dados a lanzar, por defecto 2
    :type n: int
    :returns: Tupla (representación, suma)
    :rtype: Tuple(str, int)
    """
    caras = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    dados = [randint(1, 6) for _ in range(n)]
    return " ".join(caras[dado-1] for dado in dados), sum(dados)


while True:
    dados, resultado = lanzar()
    print(f"{dados} -> {resultado}")
    if input("Volver a lanzar los dados? ").lower() not in "si":
        break