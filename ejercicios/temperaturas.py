"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

El SENAMHI dio a conocer las temperaturas más bajas registradads en la
ciudad de Lima, desde el 22/05/2019 hasta 14/06/2019, que se detalla a
continuación:

    +-----------------------------------------------------------+
    | lima = {                                                  |
    |     "22/05/2019": 17, "23/05/2019": 17, "24/05/2019": 19, |
    |     "25/05/2019": 23, "26/05/2019": 20, "27/05/2019": 18, |
    |     "28/05/2019": 20, "29/05/2019": 19, "30/05/2019": 22, |
    |     "31/05/2019": 19, "01/06/2019": 20, "02/06/2019": 19, |
    |     "03/06/2019": 17, "04/06/2019": 16, "05/06/2019": 18, |
    |     "06/06/2019": 21, "07/06/2019": 19, "08/06/2019": 15, |
    |     "09/06/2019": 17, "10/06/2019": 20, "11/06/2019": 15, |
    |     "12/06/2019": 22, "13/06/2019": 14, "14/06/2019": 16, |
    | }                                                         |
    +-----------------------------------------------------------+

El responsable del SENAMHI le pide ayuda para desarrollar un programa
que tenga las siguientes opciones:

- Agregar más temperaturas bajas por fecha (debe solictar la cantidad de
    datos a agregar, luego debe solicitar las fechas y las temperaturas
    para agregarlos al diccionario).
- Obtener la fecha con la temperatura más baja.
- Obtener la fecha con la temperatura más alta.

Ayudemos al responsable del SENAMHI. Escribe un programa con todas las
opciones solicitadas por el responsable del SENAMHI.

Un ejemplo de diálogo de este programa sería:

    +------------------------------------------------------------+
    | Ingrese la candidad de datos a agregar: 3                  |
    | Ingrese la fecha: 15/06/2019                               |
    | Ingrese la temperatura: 21                                 |
    | Ingrese la fecha: 16/06/2019                               |
    | Ingrese la temperatura: 19                                 |
    | Ingrese la fecha: 17/06/2019                               |
    | Ingrese la temperatura: 18                                 |
    | La fecha donde la temperatura fue más baja fue: 13/06/2019 |
    | La fecha donde la temperatura fue más alta fue: 25/05/2019 |
    +------------------------------------------------------------+
"""
# pip install prototools
from prototools import int_input, date_input

lima = {
    "22/05/2019": 17, "23/05/2019": 17, "24/05/2019": 19,
    "25/05/2019": 23, "26/05/2019": 20, "27/05/2019": 18,
    "28/05/2019": 20, "29/05/2019": 19, "30/05/2019": 22,
    "31/05/2019": 19, "01/06/2019": 20, "02/06/2019": 19,
    "03/06/2019": 17, "04/06/2019": 16, "05/06/2019": 18,
    "06/06/2019": 21, "07/06/2019": 19, "08/06/2019": 15,
    "09/06/2019": 17, "10/06/2019": 20, "11/06/2019": 15,
    "12/06/2019": 22, "13/06/2019": 14, "14/06/2019": 16,
}


def ingresar_temperaturas():
    cantidad = int_input("Ingrese la cantidad de datos a agregar: ", min=1)
    for _ in range(cantidad):
        fecha = date_input(
            "Ingrese la fecha: ", ("%d/%m/%Y",)
        ).strftime("%d/%m/%Y")
        temperatura = int_input("Ingrese la temperatura: ", min=-30, max=40)
        lima[fecha] = temperatura


if __name__ == "__main__":
    ingresar_temperaturas()
    print(
        "La fecha donde la temperatura fue más baja fue:",
        min(lima, key=lima.get)
    )
    print(
        "La fecha donde la temperatura fue más alta fue:",
        max(lima, key=lima.get)
    )
