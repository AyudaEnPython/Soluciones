"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

En una universidad, el pago de la matrícula de los alumnos se determina
según el número de materias que cursan. El costo de cada crédito es de
$800. Si un estudiante matricula más de 12 créditos, solo se le
cobrarán 12.

Se ha establecido un programa para estimular a los estudiantes a sacar
buenas notas, el cual es el siguiente:

- Si el promedio obtenido por el alumno en el último período es mayor o
    igual a 70, se le hará un descuento del 30% sobre la matrícula.
- En casos de que el promedio haya sido menor a 70, se le cobrará la
    totalidad de la matrícula, según la cantidad de créditos
    matriculados.

Cree un programa que reciba la cantidad de créditos por el estudiante y
el promedio obtenido en el semestre anterior, e indique como respuesta
la cantidad de dinero a pagar por el estudiante.
"""
PRECIO_POR_CREDITO = 800


def calcular(creditos, promedio):
    if creditos > 12:
        creditos = 12
    if promedio >= 70:
        return creditos * PRECIO_POR_CREDITO * 0.7
    return creditos * PRECIO_POR_CREDITO


def main():
    creditos = int(input("Ingrese la cantidad de créditos: "))
    promedio = int(input("Ingrese el promedio obtenido: "))
    print(f"El pago es de: ${calcular(creditos, promedio):.2f}")


if __name__ == "__main__":
    main()
