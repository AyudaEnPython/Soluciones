"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------ Enunciado Original -------------------------
Pedir al usuario la cantidad de números de la secuencia de Fibonacci
que desea ver.

Por ejemplo si el usuario digita 10, deberá mostrarse en pantalla la
secuencia:
1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# ---------------------------------------------------------------------
NOTE: la secuencia para n = 10 es: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""
from unittest import main, TestCase
from typing import Generator, List


def fibonacci_while(n: int) -> Generator[int, None, None]:
    """Genera la secuencia de Fibonacci de 'n' elementos.

    :param n: cantidad de elementos de la secuencia
    :n type: int
    :return: secuencia de Fibonacci
    :rtype: Generator[int, None, None]
    """

    a, b = 0, 1
    while n > 0:
        yield a
        a, b = b, a + b
        n -= 1


def fibonacci_for(n: int) -> List[int]:
    """Genera la secuencia de Fibonacci de 'n' elementos.

    :param n: cantidad de elementos de la secuencia
    :n type: int
    :return: secuencia de Fibonacci
    :rtype: List[int]
    """
    secuencia = [0, 1]
    for i in range(2, n):
        secuencia.append(secuencia[i - 1] + secuencia[i - 2])
    return secuencia


def fibonacci_binet(n: int) -> List[int]:
    """Genera la secuencia de Fibonacci de 'n' elementos.

    :param n: cantidad de elementos de la secuencia
    :n type: int
    :return: secuencia de Fibonacci
    :rtype: List[int]
    """
    p = (1 + 5**0.5) / 2
    q = 1 / p
    return [int((p**i + q**i) / 5 ** 0.5) for i in range(n)]
    # One-liner:
    # return [
    #    int((((1 + 5**0.5) / 2)** i - ((1 - 5**0.5) / 2)** i) / 5**0.5)
    #    for i in range(n)
    # ]


def main_(): # comment/uncomment to switch between while and for versions
    n = int(input("Ingrese la cantidad de elementos de la secuencia: "))
    print(", ".join(str(x) for x in fibonacci_while(n)))
    # print(", ".join(str(x) for x in fibonacci_for(n)))
    # print(", ".join(str(x) for x in fibonacci_binet(n)))


class Test(TestCase):

    def test_functions(self):
        for function in (fibonacci_while, fibonacci_for, fibonacci_binet):
            self.assertEqual(list(function(10)), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])


if __name__ == "__main__":
    # main() # uncomment this line and comment the next one to run the tests
    main_()
