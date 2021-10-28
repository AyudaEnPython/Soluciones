"""
Escriba un programa para solicitar una puntuación entre 0.0 y 1.0. Si
el puntaje está fuera de ese rango, imprima un error. Si el puntaje
está entre 0.0 y 1.0, imprima un grado usando la tabla siguiente:

Score      Grado
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
< 0.6      E

Si el usuario ingresa un valor fuera de rango, imprima un mensaje de
error adecuado y salga.

Para probar el código, ingrese un puntaje de 0.85.

    Salida deseada
    +------------+
    | B          |
    +------------+
"""

score = float(input("Puntaje: "))

if 0.0 <= score <= 1.0:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("E")
else:
    print("Error")