"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realizar un programa que llene el nombre y la duración de canciones y
luego aparezca el siguiente menú:

1. Mostrar el nombre y la duración de la canción de la misma.
2. Buscar por palabra contenidas en el nombre.
3. Buscar con duraciones mayores a un valor.
4. Despedirse y salir del programa.
5. Mostrar estadísticas (promedio, nombre canción menor duracion)
6. Agregar Canción

El programa debe realizar la opción seleccionada y volver a preguntar
el menú (al menos que seleccione salir)

Nota 1: Si utiliza la biblioteca interface escribir WINDOWS=False
Nota 2: Se recomienda usar diccionarios con llave el nombre de la
    canción, pero si desea tambien puede hacerlo solo con lista.

Datos iniciales del cancionero:

canciones = {
    "bicicleta": 4.5,
    "meu pintinho amarelinho": 2.5,
    "formiguinha": 3.0,
    "borboletinha": 3.2,
    "Brilha Brilha estrelinha": 1.9,
}
NOTE: Se opta por cambiar el diseño.
TODO: add docstrings and tests later...
"""
from prototools import Menu

canciones = {
    "bicicleta": 4.5,
    "meu pintinho amarelinho": 2.5,
    "formiguinha": 3.0,
    "borboletinha": 3.2,
    "Brilha Brilha estrelinha": 1.9,
}


def agregar_cancion():
    nombre = input("Ingrese el nombre de la canción: ")
    duracion = float(input("Ingrese la duración de la canción: "))
    canciones[nombre] = duracion


def buscar_cancion():
    palabra = input("Ingrese la palabra a buscar: ")
    for nombre, duracion in canciones.items():
        if palabra in nombre:
            print(f"{nombre} - {duracion}")


def mostrar_estadisticas():
    duracion_total = 0
    duracion_menor = canciones[list(canciones.keys())[0]]
    for _, duracion in canciones.items():
        duracion_total += duracion
        if duracion < duracion_menor:
            duracion_menor = duracion
    print(f"Promedio: {duracion_total / len(canciones)}")
    print(f"Cancion menor duración: {duracion_menor}")


def buscar_duracion_mayor_a():
    duracion = float(input("Ingrese la duración mayor a la buscar: "))
    for nombre, duracion_cancion in canciones.items():
        if duracion_cancion > duracion:
            print(f"{nombre} - {duracion_cancion}")


def buscar_por_palabra_contenida():
    palabra = input("Ingrese la palabra a buscar: ")
    for nombre, duracion in canciones.items():
        if palabra in nombre:
            print(f"{nombre} - {duracion}")


def mostrar_canciones():
    for nombre, duracion in canciones.items():
        print(f"{nombre} - {duracion}")


def main():
    menu = Menu()
    menu.add_options(
        ("Mostrar canciones", mostrar_canciones),
        ("Buscar por palabra contenida", buscar_por_palabra_contenida),
        ("Buscar duración mayor a", buscar_duracion_mayor_a),
        ("Mostrar estadísticas", mostrar_estadisticas),
        ("Agregar canción", agregar_cancion),
    )
    menu.run()


if __name__ == "__main__":
    main()
