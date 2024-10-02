import os
from typing import Callable, Dict, Optional, Union 

Data = Dict[int, Dict[str, Union[str, int, float]]]
MENU = """¿Que operación desea realizar?, las opciones son:
1) Ingresar artículo
2) Consultar artículo
3) Comprar
4) Vender
5) Eliminar artículo
6) Salir
"""


def _input(prompt: str, tipo: type) -> Union[int, float]:
    while True:
        try:
            return tipo(input(prompt))
        except ValueError:
            print(f"Por favor, ingrese un {tipo.__name__} válido")


def _obtener_codigo(prompt: str = "Ingresar código: ") -> int:
    return _input(prompt, int)


def _verificar(registro: Data, codigo: int, debe_existir: bool = True) -> bool:
    existe = codigo in registro
    if debe_existir and not existe:
        print("Artículo no encontrado.")
    elif not debe_existir and existe:
        print("El código ya existe. Intentar con otro código.")
    return existe == debe_existir


def ingresar(registro: Data) -> Data:
    codigo = _obtener_codigo()
    if not _verificar(registro, codigo, debe_existir=False):
        return registro
    registro[codigo] = {
        "cantidad": _input("Ingresar cantidad: ", int),
        "precio": _input("Ingresar precio: ", float),
        "nombre": input("Ingresar nombre: "),
    }
    print("Artículo ingresado correctamente.")
    return registro


def consultar(registro: Data) -> Data:
    codigo = _obtener_codigo()
    if _verificar(registro, codigo):
        for k, v in  registro[codigo].items():
            print(f"{k}: {v}")
    return registro


def _actualizar(
        registro: Data,
        codigo: int,
        operacion: Callable[[int, int], int],
        mensaje_cantidad: str,
        mensaje_exito: str,
    ) -> Optional[bool]:
    if not _verificar(registro, codigo):
        return None
    cantidad = _input(mensaje_cantidad, int)
    actual = registro[codigo]["cantidad"]
    nueva = operacion(actual, cantidad)
    if nueva < 0:
        print("Cantidad insuficiente para realizar una venta.")
        return False
    registro[codigo]["cantidad"] = nueva
    print(mensaje_exito)
    return True


def comprar(registro: Data) -> Data:
    codigo = _obtener_codigo()
    _actualizar(
        registro,codigo,
        lambda actual, cantidad: actual + cantidad,
        "Ingresar cantidad a agregar: ",
        "Cantidad actualizada correctamente"
    )
    return registro


def vender(registro: Data) -> Data:
    codigo = _obtener_codigo()
    _actualizar(
        registro,codigo,
        lambda actual, cantidad: actual - cantidad,
        "Ingresar cantidad a vender: ",
        "Venta realizada correctamente"
    )
    return registro


def eliminar(registro: Data) -> Data:
    codigo = _obtener_codigo()
    if _verificar(registro, codigo):
        del registro[codigo]
        print("Artículo eliminado.")
    return registro


def main():
    registro: Data = {}
    opciones = {
        "1": ingresar,
        "2": consultar,
        "3": comprar,
        "4": vender,
        "5": eliminar,
    }
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(MENU)
        opcion = input("Elija una opción: ")
        if opcion == "6":
            break
        if opcion in opciones:
            registro = opciones[opcion](registro)
        else:
            print("Opción no válida. Intentar de nuevo.")
        input("Presionar 'Enter' para continuar...")
    print("Fin del programa")


if __name__ == "__main__":
    main()
