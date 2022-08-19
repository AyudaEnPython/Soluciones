"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

## Ejercicio 1

Piensa al menos en 3 alternativas o funcionalidades del código del
archivo "MiRedS4-Funciones.py" que podrían convertirse en función.
Modifica el código para incluir estas funciones y no repetir código.

NOTE: refactored.
"""
CURRENT_YEAR = 2022
SIZE = 70
SALIR = 0
TITULO = """
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/
"""
BARRA = "-" * SIZE


def bienvenida():
    print("Bienvenido a ...")
    print(TITULO)


def mostrar_opciones():
    print("Acciones disponibles:")
    print("\t1. Escribir un mensaje")
    print("\t2. Mostrar los datos del perfil")
    print("\t0. Salir")


def mostrar_perfil(nombre, edad, estatura, amigos):
    e_m, e_cm = int(estatura), int((estatura%1)*100)
    print("\n" + BARRA)
    print(f"Nombre  : {nombre}")
    print(f"Edad    : {edad} años")
    print(f"Estatura: {e_m} metros y {e_cm} centímetros")
    print(f"Amigos  : {amigos}")
    print(BARRA +"\n")


def mostrar_mensaje(nombre, mensaje):
    print("\n" + BARRA)
    print(f"{nombre} dice: {mensaje}")
    print(BARRA +"\n")


def publicar_mensaje(nombre):
    print("\nVamos a publicar un mensaje.")
    mensaje = input("¿Qué piensas hoy?\n> ")
    mostrar_mensaje(nombre, mensaje)


def menu(nombre, edad, estatura, amigos):
    opcion = -1
    while opcion != SALIR:
        mostrar_opciones()
        opcion = int(input("Ingresa una opción:\n> "))
        if opcion == 1:
            publicar_mensaje(nombre)
        elif opcion == 2:
            mostrar_perfil(nombre, edad, estatura, amigos)
        elif opcion == SALIR:
            print("\nHas decidido salir.")
        else:
            print("\nNo conozco la opción que has ingresado. Inténtalo otra vez.")


def obtener_datos():
    nombre = input("Para empezar, dime como te llamas.\n> ")
    print(f"Hola {nombre}, bienvenido a Mi Red\n")
    dob = int(input("Para preparar tu perfil, dime en qué año naciste.\n> "))
    edad = CURRENT_YEAR - dob
    print("\nCuéntame más de ti, para agregarlo a tu perfil.")
    estatura = float(input("¿Cuánto mides? Dímelo en metros.\n> "))
    amigos = int(input(
        "\nMuy bien. Finalmente, cuéntame cuantos amigos tienes.\n> "
    ))
    return nombre, edad, estatura, amigos


def main():
    bienvenida()
    nombre, edad, estatura, amigos = obtener_datos()
    print(
        f"\nMuy bien, {nombre}."
        f"Entonces podemos crear un perfil con estos datos."
    )
    mostrar_perfil(nombre, edad, estatura, amigos)
    print("Gracias por la información. Esperamos que disfrutes con Mi Red\n")
    menu(nombre, edad, estatura, amigos)


if __name__ == "__main__":
    main()
    print("\nGracias por usar Mi Red. ¡Hasta pronto!\n")
