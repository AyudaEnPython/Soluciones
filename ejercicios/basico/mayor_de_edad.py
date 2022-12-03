"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Hacer un programa en Python que cargue nombre, apellido y edad de
afiliados de un club deportivo en una tabla.
Luego se deberá mostrar todos los afiliados que sean mayores de edad
(de 18 años en adelante).

Ejs:

apellido (* para salir): zuluaga
nombre: inés
edad: 30
Apellido (* para salir): alberti
nombre: juan
edad: 23
Apellido (* para salir): balcarce
nombre: emilia
edad: 20
Apellido (* para salir): zeidel
nombre: daniel emilio
edad: 17
Apellido (* para salir): *

Afiliados mayores de edad:
ZULUAGA INËS 30
ALBERTI JUAN 23
BALCARCE EMILIA 20
"""


def obtener_datos():
    datos = []
    while True:
        apellido = input("Apellido (* para salir): ")
        if apellido == "*":
            break
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        datos.append([apellido, nombre, edad])
    return datos


def mayores_de_edad(datos):
    mayores = []
    for apellido, nombre, edad in datos:
        if edad >= 18:
            mayores.append([apellido, nombre, edad])
    return mayores


def main():
    afiliados = obtener_datos()
    mayores = mayores_de_edad(afiliados)
    print("Afiliados mayores de edad:")
    for apellido, nombre, edad in mayores:
        print(f"{apellido.upper()} {nombre.upper()} {edad}")


if __name__ == "__main__":
    main()
