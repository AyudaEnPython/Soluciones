"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import os
from datetime import datetime


def _limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def _ingresar_numero(mensaje, min=None, max=None):
    while True:
        try:
            valor = int(input(mensaje))
            if min is not None and max is not None:
                if min <= valor <= max:
                    return valor
                else:
                    print(f"El valor debe estar entre {min} y {max}")
            else:
                return valor
        except ValueError:
            print("Ingrese no válido, volver a intentar")


def _ingresar_fecha(msj):
    while True:
        try:
            fecha = input(msj)
            return datetime.strptime(fecha, "%d/%m/%Y").date()
        except ValueError:
            print("Ingresar una fecha válida, volver a intentar")


def ejercicio_1():
    cantidad = _ingresar_numero("Cantidad de números: ")
    for _ in range(cantidad):
        numero = _ingresar_numero("Ingrese un numero: ")
        if numero > 0:
            print(f"{numero} es positivo")
        elif numero < 0 and numero % 2 != 0:
            print(f"{numero} -> {numero * -1}")
        else:
            print(f"{numero} no es positivo")


def ejercicio_2():
    canasta = {1: 0, 2: 0, 3: 0}
    frutas = {1: "Peras", 2: "Manzanas", 3: "Piñas"}
    cantidad = _ingresar_numero("Cantidad de frutas: ")
    for n in range(cantidad):
        print("Selecciona una fruta ([1] Peras, [2] Manzana, [3] Piña)\n")
        fruta = _ingresar_numero("Opcion: ", 1, 3)
        canasta[fruta] += 1
    print("\nCanastos:")
    for fruta, cantidad in canasta.items():
        print(f"{frutas[fruta]}: {cantidad}")


def ejercicio_3():
    registro = {}
    cantidad = _ingresar_numero("Cantidad de clientes: ")
    for _ in range(cantidad):
        dulce = input("Dulce: ")
        precio = _ingresar_numero("Precio: ")
        cantidad = _ingresar_numero("Cantidad: ")
        registro[dulce] = precio * cantidad
    print("\nRegistro:")
    for dulce, precio in registro.items():
        print(f"{dulce}: {precio}")
    print(f"Total: {sum(registro.values())}")


def ejercicio_4():
    fecha_actual = datetime.now().date()
    cantidad = _ingresar_numero("Cantidad de personas: ")
    for _ in range(cantidad):
        fecha_nacimiento = _ingresar_fecha("Fecha de nacimiento (dd/mm/yy): ")
        dias = fecha_actual - fecha_nacimiento
        print(f"{dias.days} dias")


def menu():
    print("Menu")
    for n in range(1, 5):
        print(f"[{n}] Ejercicio {n}")
    print("[5] Salir")


def main():
    while True:
        menu()
        opcion = _ingresar_numero("Opcion: ", 1, 5)
        if opcion == 5:
            print("\nFin del programa")
            break
        print(f"\nEjercicio {opcion}")
        if opcion == 1:
            ejercicio_1()
        elif opcion == 2:
            ejercicio_2()
        elif opcion == 3:
            ejercicio_3()
        elif opcion == 4:
            ejercicio_4()
        input("\nPresione enter para continuar...")
        _limpiar_pantalla()


if __name__ == "__main__":
    main()
