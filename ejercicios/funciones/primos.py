"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dada una lista de números enteros, escribir una función que:
- Devuelva una lista con todos los que sean primos.
"""


# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/es_primo.py
def es_primo(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def primos(numeros):
    son_primos = []
    no_son_primos = []
    for numero in numeros:
        if es_primo(numero):
            son_primos.append(numero)
        else:
            no_son_primos.append(numero)
    return sorted(son_primos), sorted(no_son_primos)


def ingresar(texto):
    numeros = []
    while True:
        n = input(texto)
        if n == "0":
            return numeros
        try:
            n = int(n)
        except ValueError:
            print("Ingresar un número entero")
        else:
            numeros.append(n)


def main():
    numeros = ingresar("Ingresar un número entero (0 para terminar): ")
    son_primos, no_son_primos = primos(numeros)
    print(f"Números ingresados que son primos: {son_primos}")
    print(f"Números ingresados que no son primos: {no_son_primos}")


if __name__ == "__main__":
    main()
