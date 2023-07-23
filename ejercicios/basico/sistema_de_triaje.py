"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

El directorio de un hospital desaa implementar un sistema de triaje
inteligente. Un paso hacia este propósito es el de categorizar las
temperaturas corporales de los pacientes que visitan urgencias de
acuerdo con las siguientes características: las temperaturas menores
a los 35.0°C son etiquetadas como 'hipotermia', las temperaturas
entre 36.0°C y 37.5°C son rotuladas como 'temperaturas normales',
las temperaturas entre 37.5°C y 39.5°C son etiquetadas como 'fiebre',
las temperaturas entre 39.5°C y 41.0°C son etiquetadas como 'fiebre
alta' y las temperaturas superiores a 41.0°C son rotuladas como
'hipertermia'. El director del área de gestión de la información del
hospital le solicita implementar el sistema inteligente en Python, y
le pide que incluya el flujograma y pseudocódigo en la entrega de la
implementación.
"""

from prototools import float_input

MIN = 32
MAX = 42.9


def main():
    temperatura = float_input(
        "Ingresar temperatura: ", min=MIN, max=MAX, lang="es",
    )
    if temperatura < 36:
        resultado = "hipotermia"
    elif 36.0 < temperatura <= 37.5:
        resultado = "temperaturas normales"
    elif 37.5 < temperatura <= 39.5:
        resultado = "fiebre"
    elif 39.5 < temperatura <= 41.0:
        resultado = "fiebre alta"
    else:
        resultado = "hipertermia"
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
