"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------

Utilizando POO implemente un programa principal y una clase llamada
productos que tenga un vector de máximo 10 elementos que permitan hacer
lo siguiente:

- Ingresar un producto: solo se almacena su nombre
- Consultar un producto: presentar todos los productos almacenados o
    uno específico.
- Modificar un producto: permite modificar el nombre del producto
- Eliminar un producto: permite eliminarlo físicamente del vector. Como
    restricción se encuentra qué si se elimina un elemento, todos los
    demás que están posterior a este deben subir una posición en el
    vector, de esa manera se garantiza un almacenamiento secuencial.

"""
from dataclasses import dataclass
from collections import UserList
# pip install prototools
from prototools import Menu, str_input, menu_input


@dataclass
class Product:
    _name: str

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name 

    def __repr__(self) -> str:
        return self._name


class Products(UserList):

    def __init__(self, iterable = []) -> None:
        if len(iterable) > 10:
            raise ValueError("El número máximo de productos es 10")
        super().__init__(iterable)

    def add(self, product):
        if len(self) < 10:
            self.append(product)
        else:
            print("No se pueden agregar más productos")

    def search(self, name=None):
        if not name:
            return self.data
        for product in self:
            if product.name == name:
                return product
        print("Producto no encontrado")

    def modify(self, current, new):
        for product in self:
            if product.name == current:
                product.name = new
                print("Producto modificado")
                return
        print("Producto no encontrado")

    def delete(self, name):
        for i, product in enumerate(self):
            if product.name == name:
                self.pop(i)
                print("Producto eliminado")
                return
        print("Producto no encontrado")


class App(Menu):

    def __init__(self, products):
        super().__init__()
        self.products = products
        self.add_options(
            ("Ingresar producto", self.add_product),
            ("Consultar producto", self.query_product),
            ("Modificar producto", self.modify_product),
            ("Eliminar producto", self.delete_product),
        )

    def add_product(self):
        name = str_input("Ingresar nombre del producto: ", lang="es")
        self.products.add(Product(name))

    def query_product(self):
        options = "Consultar un producto","Mostrar todos los productos"
        selected_option = menu_input(options, numbers=True, lang="es")
        self.clear_screen()
        if selected_option == options[0]:
            self._show_product()
        else:
            self._show_products()

    def _show_product(self):
        name = str_input("Ingresar nombre: ", lang="es")
        product = self.products.search(name)
        if product is not None:
            print(f"Producto: {product}")

    def _show_products(self):
        products = self.products.search()
        if products:
            print("Productos")
            print("\n".join(
                f"{i+1}. {p}" for i, p in enumerate(self.products.search())
            ))
        else:
            print("No existen productos")

    def modify_product(self):
        current = str_input("Ingresar nombre del producto: ", lang="es")
        new = str_input("Ingresar nuevo nombre del producto: ", lang="es")
        self.products.modify(current, new)

    def delete_product(self):
        name = str_input("Ingresar nombre del producto: ", lang="es")
        self.products.delete(name)


if __name__ == "__main__":
    app = App(Products())
    app.run()
