"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Solucion completa en:
https://github.com/AyudaEnPython/Soluciones/blob/main/ejercicios/vacaciones.py
"""

def registrar():
    nombre = input("Nombre y Apellido: ")
    while True:
        contraseña = input("contraseña: ")
        confirmar = input("Confirmar contraseña: ")
        if contraseña == confirmar:
            print("Confirmacion de contraseña correcta!")
            break
        else:
            print("Digitar nuevamente la contraseña!")
    return nombre, contraseña


def tiempo_servicio():
    while True:
        años = input("años de servicio: ")
        try:
            años = int(años)
            if 0 <= años <= 20:
                return años
        except ValueError:
            print("Digitar nuevamente los años de servicios")


def dias(años):
    vacaciones = {1 < años <= 5: 10, 5 < años <= 10: 15, 10 < años <= 20: 30}
    return vacaciones[True]


if __name__ == "__main__":
    nombre, contraseña = registrar()
    años = tiempo_servicio()
    print(f"{nombre} tiene derecho a {dias(años)} dias de vacaciones")