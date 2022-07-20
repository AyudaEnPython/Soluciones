"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict, List, Tuple
# pip install prototools
from prototools import Menu, textbox, float_input, str_input
from prototools.colorize import magenta, cyan, yellow


def _buscar(tienda: List[Dict[str, float]], nombre: str) -> Tuple[bool, int]:
    for i, producto in enumerate(tienda):
        if nombre in producto.values():
            return True, i
    return False, -1


def agregar(tienda: List[Dict[str, float]]) -> None:
    nombre = str_input("Nombre del producto: ")
    precio = float_input("Precio: ", min=0, lang="es")
    encontrado, _ = _buscar(tienda, nombre)
    if not encontrado:
        tienda.append({"nombre": nombre, "precio": precio})
        textbox("Producto agregado")
    else:
        textbox("El producto ya existe!")


def modificar(tienda: List[Dict[str, float]]) -> None:
    nombre = str_input("Nombre del producto: ")
    encontrado, posicion = _buscar(tienda, nombre)
    if encontrado:
        precio = float_input("Precio: ", min=0, lang="es")
        tienda[posicion]["precio"] = precio
        textbox("Producto modificado")
    else:
        textbox("El producto no existe!")


def eliminar(tienda: List[Dict[str, float]]) -> None:
    nombre = str_input("Nombre del producto: ")
    encontrado, posicion = _buscar(tienda, nombre)
    if encontrado:
        tienda.pop(posicion)
        textbox("Producto eliminado")
    else:
        textbox("El producto no existe!")


def listar(tienda: List[Dict[str, float]]) -> None:
    for producto in tienda:
        print(f"{producto['nombre']} - ${producto['precio']}")


def main():
    tienda = []
    menu = Menu(
        cyan("Tienda"),
        yellow("Ayuda en Python"),
        exit_option_text=magenta("Salir"),
        exit_option_color=magenta,
    )
    menu.add_options(
        ("Agregar", lambda: agregar(tienda)),
        ("Modificar", lambda: modificar(tienda)),
        ("Eliminar", lambda: eliminar(tienda)),
        ("Listar", lambda: listar(tienda)),
    )
    menu.settings(
        subtitle_align="center",
        style="double",
        color=magenta,
        options_color=yellow,
        separators=True,
    )
    menu.run()


if __name__ == "__main__":
    main()
