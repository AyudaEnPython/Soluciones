"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def main():
    i = 0
    sum_ = 0
    promedio = 0
    while True:
        valor = input("Ingresar un valor (0 para terminar): ")
        if valor == "0" and i == 0:
            print("Ingresar por lo menos un valor")
        try:
            valor = float(valor)
        except ValueError:
            print("Ingresar un valor númerico")
        else:
            sum_ += valor
        if valor == 0 and i != 0:
            promedio = sum_ / i
            break
        i += 1
    print(f"El promedio es: {promedio:.2f}")


if __name__ == "__main__":
    main()
