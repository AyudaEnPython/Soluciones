"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: refactored.
"""
import os

CURRENT_YEAR = 2022
SIZE = 70
SALIR = "0"
TITULO = """
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \\/ /  / ___/ _ \\/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \\___/\\__,_/
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
    print("\t5. Cambiar de usuario")
    print("\t0. Salir")


def mostrar_perfil(
    nombre,
    edad,
    estatura_m,
    estatura_cm,
    genero,
    pais,
    amigos,
    estado,
):
    print("\n" + BARRA)
    print(f"Nombre  : {nombre}")
    print(f"Edad    : {edad} años")
    print(f"Estatura: {estatura_m} metros y {estatura_cm} centímetros")
    print(f"Género  : {genero}")
    print(f"País    : {pais}")
    print(f"Amigos  : {amigos}")
    print(f"Estado  : {estado}")
    print(BARRA + "\n")


def mostrar_mensaje(origen, destinatario, mensaje):
    print("\n" + BARRA)
    if destinatario is None:
        print(f"{origen} dice: {mensaje}")
    else:
        print(f"{origen} dice: @{destinatario} {mensaje}")
    print(BARRA + "\n")


def obtener_mensaje():
    return input("\nAhora vamos a publicar un mensaje. ¿Qué piensas hoy?\n> ")


def obtener_nombre():
    return input("Para empezar, dime como te llamas.\n> ")


def obtener_genero():
    while True:
        genero = input("¿Cuál es tu género? Masculino(M) o Femenino(F)?\n> ")
        if genero in "MmFf":
            if genero == "M" or genero == "m":
                return "Masculino"
            return "Femenino"
        print("No conozco el género que has ingresado. Inténtalo otra vez.")


def obtener_pais():
    return input("¿En qué país naciste?\n> ")


def obtener_edad():
    return (
        CURRENT_YEAR -
        int(input("Para preparar tu perfil, dime en qué año naciste.\n> "))
    )


def obtener_estatura():
    print("\nCuéntame más de ti, para agregarlo a tu perfil.")
    estatura = float(input("¿Cuánto mides? Dímelo en metros.\n> "))
    return int(estatura), int((estatura % 1) * 100)


def obtener_amigos():
    return int(input(
        "\nMuy bien. Finalmente, cuéntame cuantos amigos tienes.\n> "
    ))


def obtener_datos(nombre):
    edad = obtener_edad()
    estatura_m, estatura_cm = obtener_estatura()
    genero = obtener_genero()
    pais = obtener_pais()
    amigos = obtener_amigos()
    return nombre, edad, estatura_m, estatura_cm, genero, pais, amigos


def obtener_opcion():
    mostrar_opciones()
    while True:
        opcion = input("Ingresa una opción:\n> ")
        if opcion in "012345":
            return opcion
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")


def existe_archivo(ruta):
    return os.path.isfile(ruta)


def leer_usuario(nombre):
    datos = []
    with open(f"{nombre}.user", "r") as f:
        for line in f:
            datos.append(line.strip())
    return datos


def escribir_usuario(nombre, datos):
    with open(f"{nombre}.user", "w") as f:
        f.writelines(f"{line}\n" for line in datos)
