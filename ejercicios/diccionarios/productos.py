"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Diseñe un algoritmo en Python, que permita almacenar en un diccionario
con lista, que tenga como clave el nombre del producto y como valor el
precio de compra de cada uno de los cinco productos.

También se requieren las siguientes operaciones:
- Agregar dos productos nuevos.
- Buscar la información de un producto específico.
- Actualizar el precio de un producto específico.
- Eliminar del diccionario un producto.
- Eliminar la información de un producto específico.
- Calcular el precio venta, será el 45% mas del precio de compra.
- Calcular la utilidad de un producto específico.
- Agregar un elemento mas cada producto llamado existencia.

NOTE: el enunciado no es muy claro y el diccionario esta mal diseñado.
"""
from typing import Dict, List
# pip install prototools
from prototools import Menu, int_input

productos: Dict[str, int] = {
    "lavadora": 1300,
    "horno": 600,
    "nevera": 1200,
    "licuadora": 180,
}

def agregar():
    nombre = input("Nombre del producto: ")
    precio = int_input("Precio del producto: ")
    productos[nombre] = precio


def buscar():
    nombre = input("Nombre del producto: ")
    producto = productos.get(nombre, None)
    if producto is None:
        print("No se encontró el producto")
        return
    return producto


def main():
    menu = Menu()
    menu.add_options(
        ("Agregar producto", print),
        ("Buscar producto", print),
        ("Actualizar producto", print),
        ("Eliminar producto", print),
        ("Calcular precio de venta", print),        
    )


if __name__ == "__main__":
    main()
