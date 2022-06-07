"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

El ministro de educación en Pythonia tiene una política para atender
las necesidades que tienen los colegios que están bajo su jurisdicción.
Cada vez que se requiere hacer reparaciones en la infraestructura en un
colegio, el ministro les sugiere organizar un bingo para que se puedan
recaudar los fondos necesarios.

Para jugar al bingo, se utilizan cartones que tienen N números distintos
y desordenados, representados por strings de la forma
"número1-número2-...númeroN" con el caracter guión "-" como separador
de los números. Tener en cuenta que los números del cartón están en el
rango 0 < x < 99, es decir, pueden tener máximo dos dígitos.

En base a lo anterior, se le solicita:

a) Escriba la función verificar_numero(numero, carton) que recibe como
    parámetro un número entero y un string con un cartón de bingo. Esta
    función deberá retornar True si el número ingresado está contenido
    en el cartón de bingo y False en caso contrario.

NOTA: Puede hacer uso de la función definida en la pregunta 1.

    +-------------------------------------------+
    | >>> verificar_numero(2, "1-12-54-5")      |
    | False                                     |
    | >>> verificar_numero(54, "1-12-54-5")     |
    | True                                      |
    +-------------------------------------------+
"""


def verificar_numero(numero: int, carton: str) -> bool:
    """Comprueba si el número está en el cartón de bingo.

    :param numero: Número a verificar
    :numero type: int
    :param carton: Cartón de bingo
    :carton type: str
    :return: Bool que indica si el número está en el cartón
    :rtype: bool
    >>> verificar_numero(2, "1-12-54-5")
    False
    >>> verificar_numero(54, "1-12-54-5")
    True
    """
    return str(numero) in carton.split('-')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
