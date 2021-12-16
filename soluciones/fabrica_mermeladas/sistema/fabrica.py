"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass
from time import sleep
from typing import ClassVar
# pip install prototools
from prototools import tabulate
from .helpers import bar, read_data, CODIGO


@dataclass
class Fabrica:

    CODE: ClassVar = CODIGO

    def ingresar_ventas(self):
        self.data = read_data()
        bar(sum(self.data.values()))

    def resumenes_totales(self):
        data = [
            ["Monto total de ventas",
                sum(self._info(codigo, "precio") for codigo in self.data)],
            ["Monto total de kilos",
                sum(self._info(codigo, "kg") for codigo in self.data)],
            ["Cantidad de productos vendidos",
                sum(self.data.values())],
        ]
        print(tabulate(data, headless=True, inner=True))

    def mostrar_detalles_por_producto(self):
        for codigo, cantidad in self.data.items():
            data = [
                ["Código", codigo, "Cantidad vendida", cantidad],
                ["Capacidad", self._info(codigo, "kg"), "Precio", self._info(codigo, "precio")],
            ]
            print(tabulate(data, headless=True, inner=True))

    def mostrar_detalles_por_tipo_de_envase(self):
        data = [
            ["Tipo de envase", "Cantidad vendida", "Capacidad", "Precio"],
            *[self._info_envase(tipo) for tipo in ("Bolsa", "Frasco")],
        ]
        print(tabulate(data, headless=True, inner=True))

    def _info_envase(self, tipo):
        t = tipo
        code = "0001" if tipo == "Bolsa" else "1011"
        n = self.data[code[:2]] + self.data[code[2:]]
        kg = self._info(code[:2], "kg") + self._info(code[2:], "kg")
        s = self._info(code[:2], "precio") + self._info(code[2:], "precio")
        return t, n, kg, s

    def _info(self, codigo, key):
        return self.CODE[codigo][key] * self.data[codigo]