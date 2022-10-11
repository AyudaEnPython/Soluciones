"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

## Ejercicio 1

Agrega una opción que permita agregar un nuevo amigo a tu lista. Esta
funcionalidad solamente agregará al usuario, sin pedir autorización y
aceptación por parte del destinatario como hace Facebook. Es decir, que
la relación de amistad solamente existe en un sentido.

## Ejercicio 2

Agrega una opción que permita mostrar los últimos estados de todos los
amigos de un usuario. Ten en cuenta que esto no es equivalente a
publicar los mensajes de su muro, sino que necesitarás leer una línea
particular de los archivos de cada usuario en su lista de amigos.

NOTE: refactored.
"""
from utils import (
    bienvenida,
    mostrar_perfil,
    mostrar_mensaje,
    obtener_nombre,
    obtener_datos,
    obtener_opcion,
    obtener_mensaje,
    existe_archivo,
    leer_usuario,
    escribir_usuario,
    SALIR,
)


def main():
    bienvenida()
    nombre = obtener_nombre()
    print(f"Hola {nombre}, bienvenido a Mi Red\n")

    if existe_archivo(f"{nombre}.user"):
        print(f"Leyendo datos de usuario {nombre} desde archivo.")
        datos = leer_usuario(nombre)
    else:
        print()
        data = obtener_datos(nombre)
        datos = [*list(data), ""]
    print("Muy bien. Estos son los datos de tu perfil.")
    mostrar_perfil(*datos)
    nombre, edad, estatura_m, estatura_cm, genero, pais, amigos, estado = datos
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
            mostrar_perfil(
                nombre, genero, pais, edad,
                estatura_m, estatura_cm, amigos, estado,
            )
        elif opcion == "4":
            nombre, genero, pais, edad, estatura_m, estatura_cm, amigos, estado = obtener_datos(nombre)  # noqa: E501
            mostrar_perfil(
                nombre, genero, pais, edad,
                estatura_m, estatura_cm, amigos, estado,
            )
        elif opcion == "5":
            usuario = input("Nombre de usuario: ")
            if existe_archivo(f"{usuario}.user"):
                print(f"Leyendo datos de usuario {usuario} desde archivo.")
                datos = leer_usuario(usuario)
            else:
                print()
                print(f"No se puede cambiar al usuario {usuario}.")
        elif opcion == SALIR:
            print(f"\nHas decidido salir. Guardando perfil en {nombre}.user")
            escribir_usuario(nombre, datos)
            print(f"Archivo {nombre}.user guardado")


if __name__ == "__main__":
    main()
    print("\nGracias por usar Mi Red. ¡Hasta pronto!\n")
