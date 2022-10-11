"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: needs to be refactored
"""

from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt


def _f(n: int, k: int = 8) -> List[float]:
    x, t = n, []
    for _ in range(k):
        x = x - (x * 0.02)
        t.append(x)
    return t


def calcular(xs: List[float]) -> Tuple[List[float], List[float]]:
    t, r = [], []
    for i in range(len(xs)):
        t.append(_f(xs[i]))
        r.append(t[i][-1])
    return t, r


def plot_comparativa(
    serie_inicial: List[float],
    serie_final: List[float],
    ancho_barras: float = 0.35,
) -> None:
    """Muestra una gráfica comparativa de obsolescencia.

    :param serie_inicial: Lista de valores iniciales.
    :param serie_final: Lista de valores finales.
    :serie_inicial type: List[float]
    :serie_final type: List[float]
    :return: None
    """
    _xticks = tuple([f"Pieza {i}" for i in range(1, len(serie_inicial) + 1)])
    numero_de_grupos = len(serie_inicial)
    indice_barras = np.arange(numero_de_grupos)
    plt.bar(
        indice_barras,
        serie_inicial,
        width=ancho_barras,
        label='Precio Inicial',
    )
    plt.bar(
        indice_barras + ancho_barras, serie_final,
        width=ancho_barras,
        label='Precio final',
    )
    plt.legend(loc='best')
    plt.xticks(indice_barras + ancho_barras, _xticks)
    plt.ylabel('Precios')
    plt.xlabel('Productos')
    plt.title('Comparativa de Obsolescencia')
    plt.show()
