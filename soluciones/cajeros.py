"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

En una tienda por departamento, se desea realizar un estadística de las
horas de atención del del personal de caja por mes. Debe solicitar el
ingreso de los nombres de los cajeros (hasta que el usuario responda
que ya no desea continuar) y las horas mensuales, tal como se muestra
en la siguiente tabla:

    +----------+-------+---------+-------+-----+----------+-------+
    | Cajero   | Enero | Febrero | Marzo | ... | Dicembre | Total |
    +----------+-------+---------+-------+-----+----------+-------+
    | Cajero 1 |       |         |       |     |          |       |
    +----------+-------+---------+-------+-----+----------+-------+
    | Cajero 2 |       |         |       |     |          |       |
    +----------+-------+---------+-------+-----+----------+-------+
    | ...      |       |         |       |     |          |       |
    +----------+-------+---------+-------+-----+----------+-------+
    | Total    |       |         |       |     |          |       |
    +----------+-------+---------+-------+-----+----------+-------+

Cargar la table a un archivo Excel y grabarlo y mostrar las siguientes
estadísticas:
- El total anual de horas por cajero
- El total mensual de horas de todos los cajeros
- El nombre y total de horas más trabajadas por cajeros al año
- El mes que tuvo mas horas trabajadas
- Haga un histrograma de frecuencias del total de horas mensuales por
    cajero y grafíquelo, señalando el máximo, mínimo y media.
- Haga un histograma de frecuencias del total de horas mensuales y
    grafíquelo, señalando el máximo, mínimo y media.

NOTE: needs to refactor even more.
"""
from dataclasses import dataclass, field
from random import randint, sample
from string import ascii_uppercase
from typing import Iterable, List

from matplotlib import pyplot as plt
import pandas as pd
# pip install prototools
from prototools import int_input, Menu, MESES, ask_to_finish


def _histograma(
    data: List[float],
    bins: Iterable,
    title: str,
    xlabel: str,
    ylabel: str
) -> None:
    plt.hist(data, bins=bins)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


@dataclass
class Cajero:
    nombre: str
    horas: dict = field(default_factory=dict)

    def __post_init__(self):
        self.horas["total"] = sum(self.horas.values())


@dataclass
class Tienda:
    personal: List[Cajero] = field(default_factory=list)

    def total_mensual(self, mes: str) -> float:
        return sum(cajero.horas[mes] for cajero in self.personal)
    
    def total_anual(self) -> float:
        return sum(cajero.horas["total"] for cajero in self.personal)
    
    def cajero_mas_trabajador(self) -> Cajero:
        cajero = max(self.personal, key=lambda cajero: cajero.horas["total"])
        return f"Cajero: {cajero.nombre} | Horas: {cajero.horas['total']} " 

    def mes_con_mas_horas(self) -> str:
        mes = max(MESES, key=lambda mes: self.total_mensual(mes))
        return f"Mes: {mes} | Horas: {self.total_mensual(mes)}"

    def mostrar(self) -> pd.DataFrame:
        data = {}
        data["cajero"] = [cajero.nombre for cajero in self.personal]
        for mes in MESES:
            data[mes] = [cajero.horas[mes] for cajero in self.personal]
        data["total"] = [cajero.horas["total"] for cajero in self.personal]
        df = pd.DataFrame(data)
        new_row = {"cajero": "total", "total": self.total_anual()}
        for mes in MESES:
            new_row[mes] = self.total_mensual(mes)
        df = df.append(new_row, ignore_index=True)
        return df

    def histograma_frecuencias_total_mensual(self) -> None:
        meses = [self.total_mensual(mes) for mes in MESES]
        _histograma(
            data=meses,
            bins=range(min(meses), max(meses) + 1, 50),
            title="Histograma de frecuencias de horas mensuales",
            xlabel="Horas mensuales",
            ylabel="Frecuencia",
        )

    def histograma_frecuencias_total_por_cajero(self) -> None:
        total_horas = [cajero.horas["total"] for cajero in self.personal]
        _histograma(
            data=total_horas,
            bins=range(min(total_horas), max(total_horas) + 1, 50),
            title="Histograma de frecuencias de horas por cajero",
            xlabel="Horas por cajero",
            ylabel="Frecuencia",
        )


def _cargar_cajero() -> Cajero:
    """Carga los datos de un cajero."""
    data = {}
    nombre = input("Ingrese el nombre del cajero: ")
    for mes in MESES:
        data[mes] = int_input(
            f"Horas trabajadas en {mes}: ", min=0, max=240,
        )
    return Cajero(nombre, data)


def cargar_personal() -> Tienda:
    """Carga los datos del personal de la tienda."""
    personal = []
    while True:
        personal.append(_cargar_cajero())
        if not ask_to_finish(lang="es"):
            break
    return Tienda(personal)


def load_random_data() -> Tienda:
    data = []
    fake_data = lambda: {k: v for k, v in zip(MESES, sample(range(120, 240), 12))}
    for nombre in sample(ascii_uppercase, randint(5, 10)):
        data.append(Cajero(nombre, fake_data()))
    return Tienda(data)


def main():
    #tienda = load_random_data()
    tienda = cargar_personal()
    menu = Menu()
    menu.add_options(
        ("Mostrar datos",
        lambda: print(tienda.mostrar())),
        ("Mejor cajero",
        lambda: print(tienda.cajero_mas_trabajador())),
        ("Mes con mayor horas trabajadas",
        lambda: print(tienda.mes_con_mas_horas())),
        ("Histograma frecuencias total mensual",
        lambda: tienda.histograma_frecuencias_total_mensual()),
        ("Histograma frecuencias total por cajero",
        lambda: tienda.histograma_frecuencias_total_por_cajero()),
    )
    menu.run()


if __name__ == "__main__":
    main()
