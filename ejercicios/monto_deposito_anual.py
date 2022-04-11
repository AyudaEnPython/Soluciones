"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba un programa que le solicite al usuario la edad actual, la edad
a la qu desea retirar, el monto que desea tener en su cuenta bancaria
a la edad de su retiro y la tasa de interes que le ofrecen. Su programa
deberá informarle el monto del deposito anual que debe hacer para
cumplir su objetivo.

Para resolver este ejercicio considere que el monto Cf resultante del
deposito de cuotas anuales de un monto C, invertido a una tasa de
interes anual r(en % anual), al cabo de t años viene dado por la
siguiente formula:

    Cf = C * (1 + i) * (((1 + i)^t - 1) / i)

Donde: i = r / 100

Note que la incógnita a obtener es el valor de C, por tanto deberá
despejar C en la fórmula.
"""


def f(r: int, t: int, Cf: float) -> float:
    """Calcula el monto de depósito anual teniendo en cuenta la tasa de
    interés, el tiempo y el monto a retirar.

    :param r: tasa de interes anual
    :r type: int
    :param t: tiempo
    :r type: int
    :param Cf: monto a retirar
    :r type: float
    :return: monto de deposito anual
    :r type: float

    >>> f(3, 25, 135193.68)
    3600.07
    """
    return round(
        Cf / ((1 + r / 100) * (((1 + r / 100) ** t - 1) / (r / 100))),
        2,
    )


def main():
    edad_actual = int(input("Ingrese la edad actual: "))
    edad_retiro = int(input("Ingrese la edad de retiro: "))
    cf = float(input("Ingrese el monto de retiro: "))
    r = int(input("Ingrese la tasa de interes en % anual: "))
    t = edad_retiro - edad_actual
    c = f(r, t, cf)
    print(
        f"Usted debera aportar cuotas anuales de {c} "
        f"para acumular {cf} al cabo de {t} años."
    )


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    main()
