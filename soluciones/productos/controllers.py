"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from models import Client, Product


class MainController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_client(self):
        values = self.view.add_client()
        self.model.add_client(Client(values))
        self.view.message_box("Cliente ingresado correctamente", True)

    def add_product(self):
        values = self.view.add_product()
        self.model.add_producto(Product(values))
        self.view.message_box("Producto ingresado correctamente", True)

    def search_client(self):
        self.view.search_and_display(
            type_="int",
            prompt="Cédula del cliente",
            method=self.model.get_client,
            model="Client",
        )

    def search_product(self):
        self.view.search_and_display(
            type_="str",
            prompt="Nombre del producto",
            method=self.model.get_product,
            model="Product",
            show_id=True,
        )

    def show_client_products(self):
        cedula = self.view.get("int", "Cédula del cliente")
        products = self.model.get_client_products(cedula)
        if products:
            print(self.view.show_products(
                items=[Product(*product[1:]).info() for product in products],
                client_id=cedula,
            ))
        else:
            self.view.message_box(
                "No se encontraron productos para el cliente especificado",
            )

    def set_relation(self):
        cedula = self.view.get("int", "Cédula del cliente: ")
        producto_id = self.view.get("int", "ID del producto: ")
        cliente, *_ = self.model.get_client(cedula)
        producto, *_ = self.model.get_product_id(producto_id)
        if cliente and producto:
            if self.model.associate(cliente, producto):
                self.view.message_box(
                    "Producto asociado al cliente correctamente", True,
                )
            else:
                self.view.message_box("El producto ya está asociado")
        else:
            if not cliente or not producto:
                self.view.message_box()

    def run(self):
        self.view.run()
