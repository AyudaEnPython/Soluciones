"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

El Cesfam de la comuna de San Miguel requiere que usted desarrolle una
aplicación estadística en Python, esta debe registrar a las personas
que asisten a vacunarse por Corona Virus, para tal efecto ha enviado
un conjunto de requerimientos que usted debe implementar en la
aplicación.

Requerimientos
- Cada día el paramédico ingresará a la aplicación Python la cantidad
    de personas citadas a vacunarse.
- Los datos que se deben ingresar son: edad, género (mujer u hombre),
    número de vacuna (primera dosis o segunda dosis o tercera dosis) y
    el tipo (Sinovac o Pfizer).
- El paramédico ingresará a la aplicación: - En género ingresará: "M"
    para mujer y "H" para hombre. - En número de vacuna: 1, 2, o 3era
    dosis. - En tipo: "S" para Sinovac y "P" para Pfizer. - Luego del
    ingreso de los datos la aplicación debe entregar la siguiente
    estadística:
    - Cantidad de personas vacunadas con primera dosis
    - Promedio de edad de Mujeres vacunadas
    - Porcentaje de hombres vacunados
    - Cantidad de vaucnas Pfizer aplicadas a las personas

TODO: El enunciado original posee varios errores.
"""
# pip install prototools
from prototools import int_input, menu_input


def get_data(n):
    data = {k: [] for k in ("edad", "genero", "dosis", "vacuna")}
    for _ in range(n):
        data["edad"].append(int_input("Edad: ", lang="es"))
        data["genero"].append(
            menu_input(("Masculino" ,"Femenino"), numbers=True, lang="es")
        )
        data["dosis"].append(int_input("Dosis: ", min=1, max=3, lang="es"))
        data["vacuna"].append(
            menu_input(("Sinovac", "Pfizer"), numbers=True, lang="es")
        )
    return data


def promedio(data, n=2):
    try:
        return round(sum(data)/len(data), n)
    except ZeroDivisionError:
        return 0


def porcentaje(data, k, xs):
    return xs / len(data[k]) * 100


def cantidades(data, k, v):
    return sum(1 for e in data[k] if e == v)


def edades_por_genero(data, g):
    return [
        edad for edad, genero in zip(data["edad"], data["genero"])
        if genero == g
    ]


def main():
    cantidad = int_input("Cantidad de personas: ")
    registro = get_data(cantidad)
    dosis_1 = cantidades(registro, "dosis", 1)
    vacuna_p = cantidades(registro, "vacuna", "Pfizer")
    hombres = cantidades(registro, "genero", "Masculino")
    mujeres = edades_por_genero(registro, "Femenino")
    print(f"Personas vacunadas con la primer dosis: {dosis_1}")
    print(f"Edad promedio de mujeres vacunadas: {promedio(mujeres)}")
    print(
        f"Porcentaje de hombres vacunados: "
        f"{porcentaje(registro, 'genero', hombres)}%"
    )
    print(f"Vacunas Pfizer aplicadas: {vacuna_p}")


if __name__ == "__main__":
    main()
