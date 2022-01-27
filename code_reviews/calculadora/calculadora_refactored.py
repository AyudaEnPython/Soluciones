"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import sys

OPERADOR = "-s", "--suma", "-r", "--resta", "-m", "--mult", "-d", "--div"
ES = {"+": slice(0, 2), "-": slice(2, 4), "*": slice(4, 6), "/": slice(6, 8)}
AYUDA = """\
AyudaEnPython: https://www.facebook.com/groups/ayudapython

-h or --help: Ayuda
-s or --suma: Sumar
-r or --resta: Restar
-m or --mult: Multiplicar
-d or --div: Dividir

Ejemplo:
> python calculadora.py -s 1 2 3"""


def mensaje(msg, flag):
    print(msg)
    sys.exit(flag)


def pre_proceso(operador, argumentos):
    if operador in ("-h", "--help"):
        mensaje(AYUDA, 0)
    if operador not in OPERADOR:
        mensaje("Argumento inválido!", 1)
    return operador, argumentos, 1 if operador in OPERADOR[ES["+"]] else 0


def procesar(operador, argumentos, inicial):
    resultado = inicial
    for i, arg in enumerate(argumentos):
        arg = int(arg) if arg.isdigit() else mensaje("Argumento inválido!", 1)
        if operador in OPERADOR[ES["+"]]:
            resultado += arg
        elif operador in OPERADOR[ES["*"]]:
            resultado *= arg
        elif operador in OPERADOR[ES["-"]]:
            resultado = arg if i == 0 else resultado - arg
        elif operador in OPERADOR[ES["/"]]:
            resultado = arg if i == 0 else (
                mensaje("No se puede dividir por 0!", 1) 
                if arg == 0 else resultado / arg
            )
    return resultado


def main():
    mensaje("Faltan argumentos!", 1) if len(sys.argv) < 2 else None
    operador, *argumentos = sys.argv[1:]
    print(procesar(*pre_proceso(operador, argumentos)))


if __name__ == "__main__":
    main()