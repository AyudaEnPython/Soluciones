"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from models import Category, Product, Provider, Store
# pip install prototools
from prototools import Menu, textbox
from prototools.inputs import str_input, int_input, float_input


def _message_box(item, suffix, color="green"):
    textbox(f"{item} registrad{suffix} exitosamente!", bcolor=color)


class MainView(Menu):

    def __init__(self):
        super().__init__()
        self.add_options(
            ("Registrar categoría",
                lambda: self.register_category(self.model)),
            ("Registrar producto",
                lambda: self.register_product(self.model)),
            ("Registrar proveedor",
                lambda: self.register_provider(self.model)),
            ("Registrar bodega",
                lambda: self.register_store(self.model)),
            ("Agregar stock",
                lambda: self.add_stock(self.model)),
            ("Remover stock",
                lambda: self.remove_stock(self.model)),
            ("Consultar",
                lambda: self.get_info(self.model)),
            ("Ver reporte",
                lambda: self.view_report(self.model)),
        )

    def set_model(self, model):
        self.model = model

    def register_category(self, model):
        name = str_input("Ingresar el nombre de la categoría: ")
        description = str_input("Ingresar una descripción: ")
        category = Category(name, description)
        model.record_manager.register_category(category)
        _message_box("Categoría", "a")

    def register_product(self, model):
        name = str_input("Ingresar nombre del producto: ")
        description = str_input("Ingresar una descripción: ")
        price = float_input("Enter product price: ")
        stock = int_input("Ingresar stock inicial: ")
        category_name = input("Ingresar una categoría: ")
        product = Product(name, description, price, stock)
        model.record_manager.register_product(product, category_name)
        _message_box("Producto", "o")

    def register_provider(self, model):
        name = str_input("Ingresar el nombre del proveedor: ")
        address = str_input("Ingresa dirección: ")
        phone = str_input("Ingresar número telefónico: ")
        provider = Provider(name, address, phone)
        model.record_manager.register_provider(provider)
        _message_box("Proveedor", "o")

    def register_store(self, model):
        name = str_input("Ingresar nombre de la tienda: ")
        location = str_input("Ingresa ubicación: ")
        capacity = int_input("Ingresar capacidad: ")
        store = Store(name, location, capacity)
        model.record_manager.register_store(store)
        _message_box("Bodega", "a")

    def add_stock(self, model):
        product_name = str_input("Ingresar el nombre del producto: ")
        quantity = int_input("Cantidad a agregar: ")
        model.stock_manager.add_stock(product_name, quantity)
        print("Stock añadido exitosamente")

    def remove_stock(self, model):
        product_name = str_input("Ingresar el nombre del producto: ")
        quantity = int_input("Cantidad a remover: ")
        model.stock_manager.remove_stock(product_name, quantity)
        print("Stock removido exitosamente")

    def get_info(self, model):
        # TODO
        ...

    def view_report(self, model):
        model.report_manager.report()
