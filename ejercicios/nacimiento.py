"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realice un programa que le pregunte al usuario el mes del cumpleaños,
el proceso se va a repetir hasta que digite la palabra No, una vez que
se termine se debe poder consultar por los siguientes criterios:

- la cantidad de personas que cumplen años dado un mes.
- la cantidad de personas que cumplen años en todos los meses
- cual es el mes en que mas personas cumplen años
- cual es el mes en que menos personas cumplen años
- existe un mes que alguien no cumpla años?

Todo esto se debe ejecutar hasta que el usuario digite la palabra salir

TODO: add typing later...
"""
# pip install prototools
from prototools import MESES, menu_input, main_loop

MES = {mes: x for mes, x in zip(MESES, range(12))}


def _mes(f, data):
    return MESES[data.index(f(data))]


def ingresar():
    datos = [0] * 12
    while True:
        mes = input("Ingresar mes: ").lower()
        if mes == "no":
            break
        if mes not in MES:
            print("Datos incorrectos, ingresar un mes válido!")
            continue
        else:
            datos[MES[mes]] += 1
    return datos


def results(datos, mes):
    print(f"Cantidad de personaes en el mes de {mes}: {datos[MES[mes]]}")
    print(f"Total de personas: {sum(datos)}")
    print(f"Mes con mas personas: {_mes(max, datos)}")
    print(f"Mes con menos personas: {_mes(min, datos)}")


def main():
    datos = ingresar()
    mes = menu_input(MESES, numbers=True)
    results(datos, mes)
    if any(True for n in datos if n == 0):
        print("si")
    else:
        print("no")


if __name__ == "__main__":
    main_loop(main)
