"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realizar un programa para calcular el monto a cobrar luego de poner un
dinero en plazo fijo. El programa debe permitir ingresar: el capital,
el tiempo (expresado en días) y la tasa de interés diario. Mostrar al
final la siguiente información:

Dentro de ... días, usted cobrará ... pesos.
"""


def monto_plazo_fijo(capital: float, tiempo: int, tasa: float) -> float:
    return capital * (1 + tasa / 100) ** tiempo


def main():
    capital = float(input("Ingrese el capital: "))
    tiempo = int(input("Ingrese el tiempo (en días): "))
    tasa = float(input("Ingrese la tasa de interés diaria: "))
    monto = monto_plazo_fijo(capital, tiempo, tasa)
    print(f"Dentro de {tiempo} días, usted cobrará {monto} pesos.")


if __name__ == "__main__":
    main()
