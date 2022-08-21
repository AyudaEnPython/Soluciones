"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

## Ejercicio 1

Al leer las líneas del archivo, siempre se leen como últimos caracteres
algunos caracteres en blancos, como espacios o el caracter cambio de
línea ("\n"). Esto hace que los nombres de archivos creados incluyan
estos caracteres adicionales. 

Utiliza métodos de 'str' para eliminar este tipo de caracteres que
denominamos "no imprimibles". Es decir, "limpia" toda línea que leas,
de manera que no tengan caracteres adicionales a lo esperado (ya sean
saltos de línea y/o espacios en blanco).

## Ejercicio 2

Utiliza tu conocimiento de funciones para crear funciones que lean
desde un archivo, y retornen el conjunto de datos leídos, de manera de
encapsular el proceso de lectura y escritura, y reducir el tamaño de tu
código.

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
        datos = obtener_datos(nombre) 
        datos.append("")
    
    print("Muy bien. Estos son los datos de tu perfil.")
    mostrar_perfil(*datos[:-1])

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
            mostrar_perfil(nombre, genero, pais, edad, estatura_m, estatura_cm, amigos)
        elif opcion == "4":
            nombre, genero, pais, edad, estatura_m, estatura_cm, amigos = obtener_datos()
            mostrar_perfil(nombre, genero, pais, edad, estatura_m, estatura_cm, amigos)
        elif opcion == SALIR:
            print(f"\nHas decidido salir. Guardando perfil en {nombre}.user")
            escribir_usuario(nombre, datos)
            print(f"Archivo {nombre}.user guardado")


if __name__ == "__main__":
    main()
    print("\nGracias por usar Mi Red. ¡Hasta pronto!\n")
