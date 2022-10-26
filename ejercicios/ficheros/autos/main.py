"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realizar un módulo que contenga una función que reciba como parámetros:
archivo (nombre del archivo o ruta del archivo más nombre, como se vio
en clase), separador (caracter de separación del archivo). Ejemplo de
llamado a la función:

print(leer_archivo("nombre_archivo.csv", ";"))

Como resultado se deberá imprimir una lista que contenga tuplas, ese es
el formato que se necesita para guardar varias líneas en un archivo con
la clase csv (como lo vimos en clase), cada tupla representa una fila y
cada elemento de la tupla representa una columna en esa fila.

Ejemplo de lo que debe devolver la función:

[('Empresa', 'Año', 'Monto Ventas', 'Mercado',
'Cantidad'), ('Chevrolet', '2010', '105', '20', '95'),
('Targit', '2010', '68', '114', '46')]

Nota: Los errores deben ser controlados, si la función tiene algún
error en el proceso, se deberá capturar y presentar en pantalla.
"""
import csv


def leer_archivo(archivo, separador=";"):
    data = []
    with open(archivo, "r", encoding="utf-8") as f:
        lines = csv.reader(f, delimiter=separador)
        for line in lines:
            data.append(tuple(line))
    return data


def main():
    print(leer_archivo("data.csv"))


if __name__ == "__main__":
    main()
