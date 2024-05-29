"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import Menu, textbox, cyan, yellow
from prototools.tabulate import tabulate, to_list
from prototools.inputs import str_input, int_input, date_input

from models import Client, Product
from config import HEADERS, COLORS


class MainView(Menu):

    def __init__(self, settings):
        super().__init__(**settings)

    def add_client(self):
        nombre = str_input("Nombre: ")
        apellido = str_input("Apellido: ")
        cedula = int_input("Cédula: ")
        return Client(nombre, apellido, cedula)

    def add_product(self):
        nombre = str_input("Nombre: ")
        mfg = date_input("Fecha de elaboración (m/d/Y): ")
        exp =  date_input("Fecha de vencimiento (m/d/Y): ")
        return Product(nombre, mfg, exp)

    def get(self, type_, prompt):
        return {"int": int_input, "str": str_input}[type_](f"{prompt}: ")

    def message_box(self, message="No encontrado", success=False):
        textbox(message, bcolor="green" if success else "red")

    def _update_colors(self, item):
        item.update({"Estado": COLORS[item.get("Estado")]})

    def _show_info(self, item):
        return tabulate(to_list(item), inner=True, color=yellow)
    
    def show_products(self, items, client_id):
        for item in items:
            self._update_colors(item)
        return tabulate(
            to_list(items), headers=HEADERS["product"], color=cyan,
            title=f"Productos adquiridos por el cliente ({client_id})",
        )

    def search_and_display(
        self,
        type_,
        prompt,
        method,
        model,
        show_id=False,
    ):
        id_value = self.get(type_, prompt)
        data = method(id_value)
        if data:
            if show_id:
                print(f"ID: {data[0]}")
            model = Client if model == "Client" else Product
            instance = model(*data[1:])
            item = instance.info()
            if item.get("Estado"):
                self._update_colors(item)
            print(self._show_info(item))
        else:
            self.message_box()
