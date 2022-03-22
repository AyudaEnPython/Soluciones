"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
Realizar un programa que ingrese números y llame a una función
"tipoDeNumero" el cual se encargará de definir si el número ingresado
es par o impar demás nos dirá si el número es Primo y/o perfecto. El
programa terminará cuando el número ingresado es 0.

NOTE: Se opta por renombrar la función a sumar_numeros (PEP8). Además,
    si se esta trabajando con funciones, se deberia implementar
    funciones para casos concretos (entrada de datos, es_primo, etc.).
    El enunciado presenta errores ortonográficos.
TODO: add docstring and tests.
"""


def es_par(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False


def es_primo(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def es_perfecto(n: int) -> bool:
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    if suma == n:
        return True
    else:
        return False


def tipo_de_numero(n: int) -> None:
    if es_par(n):
        print("El número es par.")
    else:
        print("El número es impar.")
    if es_primo(n):
        print("El número es primo.")
    else:
        print("El número no es primo.")
    if es_perfecto(n):
        print("El número es perfecto.")
    else:
        print("El número no es perfecto.")


def main():
    while True:
        numero = int(input("Ingrese el número: "))
        if numero == 0:
            break
        tipo_de_numero(numero)


if __name__ == "__main__":
    main()
