"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Una empresa de servicios públicos desea liquidar el total de la factura
teniendo en cuenta:

    +---------+------------------+---------------+
    | Estrato | Nivel de Consumo | Tarifa Básica |
    +---------+------------------+---------------+
    |    1    |      <= 10       |     $5000     |
    +---------+------------------+---------------+
    |    2    |      <= 25       |    $10000     |
    +---------+------------------+---------------+
    |    3    |      <= 35       |    $15000     |
    +---------+------------------+---------------+
    |    4    |      <= 40       |    $20000     |
    +---------+------------------+---------------+

Si el nivel de consumo se excede, debe pagar por cada punto adicional
en el nivel de consumo $800, en cualquiera de los 4 estratos.

Ejemplo: Si el estrato es 3 y el nivel de consumo 45 entonces el valor
    de la factura es de:

    Valor factura = 15000 + (10*800) = 23000 pesos

Realizar:
    a. Una función que tenga como parámetros de entrada el estrato y el
        nivel de consumo, y debe retornar el valor de la factura a
        pagar.
"""

tabla = {
    1: (5000, 10),
    2: (10000, 25),
    3: (15000, 35),
    4: (20000, 40),
}


def calcular(estrato: float, consumo: float) -> float:
    """Calcula el valor de la factura a pagar.

    :param estrato: Estrato del cliente.
    :estrato type: float
    :param consumo: Nivel de consumo del cliente.
    :consumo type: float
    :return: Valor de la factura a pagar.
    :rytpe: float

    >>> calcular(3, 45)
    23000
    """
    tarifa_basica, limite = tabla[estrato]
    if consumo <= limite:
        return tarifa_basica
    else:
        return tarifa_basica + (consumo - limite) * 800


if __name__ == "__main__":
    import doctest

    doctest.testmod()
