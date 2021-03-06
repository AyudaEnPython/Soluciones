"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: add tests.
"""
import sys
from functools import reduce
from operator import add, sub, mul, truediv
from textwrap import dedent
from typing import Callable, List, Dict


def _accion(s: str) -> Callable:
    """Ejecuta la accion correspondiente a la opcion ingresada

    :param s: Opcion ingresada por el usuario
    :type s: str
    :return: Funcion que ejecuta la accion correspondiente
    :rtype: Callable
    """
    accion: Dict[str, Callable] = {
        s == "-s" or s == "--suma": add,
        s == "-r" or s == "--resta": sub,
        s == "-m" or s == "--mul": mul,
        s == "-d" or s == "--div": truediv,
    }
    return accion[True]


def _validar(args: List[str]) -> None:
    """Valida que el usuario haya ingresado alguna de las opciones
    -h, --help, -s, --suma, -r, --resta, -m, --mult, -d, --div

    :param args: Argumentos ingresados por el usuario
    :type args: List[str]
    :raises Exception: Si el usuario no ingreso ninguna de las opciones
    """
    if len(args) <= 1:
        raise Exception("Faltan argumentos!")
    if args[1] == "-h" or args[1] == "--help":
        help()
        sys.exit(0)
    if args[1] not in (
        "-s", "--suma", "-r", "--resta", "-m", "--mul", "-d", "--div"
    ):
        raise Exception("Argumento invalido!")
    if not all(map(lambda s: s.isdigit(), args[2:])):
        raise Exception("Argumentos inválidos!")


def help() -> None:
    """Muestra la ayuda del programa"""
    print("AyudaEnPython: https://www.facebook.com/groups/ayudapython\n")
    print(dedent("""\
        -h or --help: Ayuda
        -s or --suma: Sumar
        -r or --resta: Restar
        -m or --mult: Multiplicar
        -d or --div: Dividir

        Ejemplo:
        > python calculadora.py -s 1 2 3"""))


def calcular(args: List[str]) -> float:
    """Calcula la operacion ingresada por el usuario

    :param args: Argumentos ingresados por el usuario
    :type args: List[str]
    :return: Resultado de la operacion
    :rtype: float
    """
    try:
        resultado = reduce(_accion(args[0]), map(float, args[1:]))
    except ZeroDivisionError:
        print("Error: No se puede dividir entre 0")
        sys.exit(1)
    return resultado


def main():
    """Ejecuta el programa principal"""
    try:
        _validar(sys.argv)
    except Exception as e:
        print(e)
        sys.exit(1)
    print(calcular(sys.argv[1:]))


if __name__ == "__main__":
    main()
