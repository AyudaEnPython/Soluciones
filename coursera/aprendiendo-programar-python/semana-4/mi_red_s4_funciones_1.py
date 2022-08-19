"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

## Ejercicio 1

Piensa al menos en 3 alternativas o funcionalidades del código del
archivo "MiRedS4-Funciones.py" que podrían convertirse en función.
Modifica el código para incluir estas funciones y no repetir código.

NOTE: refactored.
"""
CURRENT_YEAR = 2022
SIZE = 70
SALIR = "0"
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
    print("\t1. Escribir un mensaje público")
    print("\t2. Escribir un mensaje solo a algunos amigos")
    print("\t3. Mostrar los datos del perfil")
    print("\t4. Actualizar el perfil de usuario")
    print("\t0. Salir")


def mostrar_perfil(nombre, edad, estatura_m, estatura_cm, amigos):
    print("\n" + BARRA)
    print(f"Nombre  : {nombre}")
    print(f"Edad    : {edad} años")
    print(f"Estatura: {estatura_m} metros y {estatura_cm} centímetros")
    print(f"Amigos  : {amigos}")
    print(BARRA +"\n")


def mostrar_mensaje(origen, destinatario, mensaje):
    print("\n" + BARRA)
    if destinatario is None:
        print(f"{origen} dice: {mensaje}")
    else:
        print(f"{origen} dice: @{destinatario} {mensaje}")
    print(BARRA +"\n")


def obtener_mensaje():
    return input("\nAhora vamos a publicar un mensaje. ¿Qué piensas hoy?\n> ")


def obtener_nombre():
    return input("Para empezar, dime como te llamas.\n> ")


def obtener_edad():
    return (
        CURRENT_YEAR -
        int(input("Para preparar tu perfil, dime en qué año naciste.\n> "))
    )


def obtener_estatura():
    estatura = float(input("¿Cuánto mides? Dímelo en metros.\n> "))
    return int(estatura), int((estatura % 1) * 100)


def obtener_amigos():
    return int(input(
        "\nMuy bien. Finalmente, cuéntame cuantos amigos tienes.\n> "
    ))


def obtener_datos():
    nombre = obtener_nombre()
    print(f"Hola {nombre}, bienvenido a Mi Red\n")
    edad = obtener_edad()
    print("\nCuéntame más de ti, para agregarlo a tu perfil.")
    estatura_m, estatura_cm = obtener_estatura()
    amigos = obtener_amigos()
    return nombre, edad, estatura_m, estatura_cm, amigos


def obtener_opcion():
    mostrar_opciones()
    while True:
        opcion = input("Ingresa una opción:\n> ")
        if opcion in "01234":
            return opcion
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")


def main():
    bienvenida()
    nombre, edad, estatura_m, estatura_cm, amigos = obtener_datos()
    print(
        f"\nMuy bien, {nombre}."
        f"Entonces podemos crear un perfil con estos datos."
    )
    mostrar_perfil(nombre, edad, estatura_m, estatura_cm, amigos)
    print("Gracias por la información. Esperamos que disfrutes con Mi Red\n")
    opcion = ""
    while opcion != SALIR:
        opcion = obtener_opcion()
        if opcion == "1":
            mostrar_mensaje(nombre, None, obtener_mensaje())
        elif opcion == "2":
            mensaje = obtener_mensaje()
            for _ in range(amigos):
                amigo = input("Ingresa el nombre de tu amig@: ")
                mostrar_mensaje(nombre, amigo, mensaje)
        elif opcion == "3":
            mostrar_perfil(nombre, edad, estatura_m, estatura_cm, amigos)
        elif opcion == "4":
            nombre, edad, estatura_m, estatura_cm, amigos = obtener_datos()
            mostrar_perfil(nombre, edad, estatura_m, estatura_cm, amigos)
        elif opcion == SALIR:
            print("\nHas decidido salir.")


if __name__ == "__main__":
    main()
    print("\nGracias por usar Mi Red. ¡Hasta pronto!\n")
