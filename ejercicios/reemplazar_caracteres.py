"""
Reemplaza pares de caracteres.
'30' -> 'a'
'55' -> 'b'
'10' -> 'c'

entrada:
'1030'

salida:
'ca'

TODO: add complete description of the exercise (current description is
    based on assumptions)
"""
from unittest import main, TestCase

analizador = {
    "30": "a",
    "55": "b",
    "10": "c",
}


def solucion_a(fuente: str, analizador: dict) -> str:
    """Reemplaza pares de caracteres si son encontrados en el 
    analizador.

    :param fuente: Texto fuente
    :fuente type: str
    :param analizador: Mapeo de caracteres a reemplazar
    :analizador type: dict
    :returns: Texto modificado
    :rtype: str
    """
    salida = ""
    for impar, par in zip(fuente[::2], fuente[1::2]):
        if impar + par in analizador.keys():
            salida += analizador[impar + par]
    return salida


def solucion_b(fuente: str, analizador: dict) -> str:
    """Reemplaza pares de caracteres si son encontrados en el 
    analizador.

    :param fuente: Texto fuente
    :fuente type: str
    :param analizador: Mapeo de caracteres a reemplazar
    :analizador type: dict
    :returns: Texto modificado
    :rtype: str

    .. Nota:
        x: caracter en posicion impar del texto fuente
        y: caracter en posicion par del texto fuente
    """
    return "".join(
        [analizador[x + y] for x, y in zip(fuente[::2], fuente[1::2]) 
        if x+y in analizador]
        )


def solucion_c(fuente: str, analizador: dict, n: int = 2) -> str:
    """Reemplaza 'n' caracteres si son encontrados en el 
    analizador.

    :param fuente: Texto fuente
    :fuente type: str
    :param analizador: Mapeo de caracteres a reemplazar
    :analizador type: dict
    :param n: Cantidad de caracteres a analizar
    :type n: int
    :returns: Texto modificado
    :rtype: str
    """
    return "".join(
        [analizador[fuente[x:x+n]] for x in range(0, len(fuente), n) 
        if fuente[x:x+n] in analizador]
        )


def solucion_d(fuente: str, analizador: dict, n: int = 2) -> str:
    """Reemplaza 'n' caracteres si son encontrados en el 
    analizador.

    :param fuente: Texto fuente
    :fuente type: str
    :param analizador: Mapeo de caracteres a reemplazar
    :analizador type: dict
    :param n: Cantidad de caracteres a analizar
    :type n: int
    :returns: Texto modificado
    :rtype: str
    """
    from itertools import zip_longest
    
    salida = ""

    def _grupos(iterable, n):
        args = [iter(iterable)] * n
        return zip_longest(*args, fillvalue="")

    for s in _grupos(fuente, n):
        if "".join(s) in analizador:
            salida += analizador["".join(s)]
    return salida


class Test(TestCase):

    datos = (
        ("1030", "ca"),
        ("5530", "ba"),
        ("5510", "bc"),
        ("10301", "ca"),
        ("0510301", "ca"),
        ("1010335556101", "ccbc"),
        ("155", ""),
        ("0", ""),
        ("", ""),
    )
    funciones = (
        solucion_a,
        solucion_b,
        solucion_c,
        solucion_d,
    )

    def test_soluciones(self):
        for f in self.funciones:
            for entrada, salida in self.datos:
                self.assertEqual(f(entrada, analizador), salida)


if __name__ == "__main__":
    main()