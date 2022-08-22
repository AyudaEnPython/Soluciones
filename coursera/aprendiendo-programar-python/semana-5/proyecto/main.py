"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# Parte I

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

# Parte II

## Ejercicio 1

Ingresa al progmra de red social con distintos usuarios. Déspues de
esto, tendrás varios archivos generados con extensión '.user'. Abre
cualquiera de estos archivos con un editor de texto y edita alguno de
los valores del fichero. Por ejemplo, cambia el nombre de usuario de
alguno de los usuarios de la red. A continuación, ejecuta de nuevo tu
programa y entra con el nombre de uno de los usuarios que constaba en
alguno de los archivos con extensión '.user'.
¿Se han actualizado los datos que cambiaste en el fichero? Prueba esto
varias veces a ver qué ocurre.

## Ejercicio 2

Agrega al menú una nueva opción que se llame "Cambiar de usuario". Esta
opción debe permitir al usuario que está en el programa, sin salirse
de la red, solicitar un nuevo nombre de usuario y, en caso de que
exista un archivo con este nombre, cargar sus datos. Si el archivo no
existe, basta con indicar que no se puede cambiar este usuario.

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
            mostrar_perfil(nombre, genero, pais, edad, estatura_m, estatura_cm, amigos, estado)
        elif opcion == "4":
            nombre, genero, pais, edad, estatura_m, estatura_cm, amigos, estado = obtener_datos(nombre)
            mostrar_perfil(nombre, genero, pais, edad, estatura_m, estatura_cm, amigos, estado)
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
