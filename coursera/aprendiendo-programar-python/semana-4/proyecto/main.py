"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

## Ejercicio 1

Agrega los atributos "género" y "pais de nacimiento" (no pongas tildes
en "país" en tu código) a los datos que se le piden al usuario. Realiza
un código que solicite datos y los lea utilizando funciones. Identifica
qué partes del código que te facilitamos en "MiredS4b-Funciones.py"
debes variar para hacerlo.

NOTE: refactored.
"""
from utils import (
    bienvenida,
    mostrar_perfil,
    mostrar_mensaje,
    obtener_datos,
    obtener_opcion,
    obtener_mensaje,
    SALIR,
)


def main():
    bienvenida()
    nombre, genero, pais, edad, estatura_m, estatura_cm, amigos = obtener_datos()  # noqa: E501
    print(
        f"\nMuy bien, {nombre}."
        f"Entonces podemos crear un perfil con estos datos."
    )
    mostrar_perfil(nombre, genero, pais, edad, estatura_m, estatura_cm, amigos)
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
            mostrar_perfil(
                nombre, genero, pais, edad, estatura_m, estatura_cm, amigos
            )
        elif opcion == "4":
            nombre, genero, pais, edad, estatura_m, estatura_cm, amigos = obtener_datos()  # noqa: E501
            mostrar_perfil(
                nombre, genero, pais, edad, estatura_m, estatura_cm, amigos
            )
        elif opcion == SALIR:
            print("\nHas decidido salir.")


if __name__ == "__main__":
    main()
    print("\nGracias por usar Mi Red. ¡Hasta pronto!\n")
