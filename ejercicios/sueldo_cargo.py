"""
Escribir un progrma para ayudar a una empresa que desea asignar sueldos
para los cargos de sus trabajadores.

+-----------+--------+
| Cargo     | Sueldo |
+-----------+--------+
| Externo   |    50  |
| Ejecutivo |    90  |
| Jefe      |   100  |
+-----------+--------+
"""
from dataclasses import asdict, dataclass, field, fields
from unittest import main, TestCase

def sueldo(cargo: str) -> int:
    """Devuelve el sueldo acorde al cargo del trabajador.

    :param cargo: Cargo del trabajador.
    :cargo type: str
    :return: Sueldo del trabajador
    :rtype: int

    >>> sueldo("Externo")
    50
    """
    dinero = 0
    cargo = cargo.capitalize()
    if cargo == "Externo":
        dinero = 50
    elif cargo == "Ejecutivo":
        dinero = 90
    elif cargo == "Jefe":
        dinero = 100
    return dinero


def sueldo_(cargo):
    """Devuelve el sueldo acorde al cargo del trabajador.

    :param cargo: Cargo del trabajador.
    :cargo type: str
    :return: Sueldo del trabajador
    :rtype: int

    >>> sueldo_("ejecutivo")
    90
    """
    cargo = cargo.capitalize()
    sueldos = {
        "Externo": 50,
        "Ejecutivo": 90,
        "Jefe": 100
    }
    return sueldos.get(cargo, None)


@dataclass
class Sueldo:
    jefe: int = field(default=100, metadata={'unit': 'dollars'})
    ejecutivo: int = field(default=90, metadata={'unit': 'dollars'})
    externo: int= field(default=50, metadata={'unit': 'dollars'})


def _sueldo(cargo):
    sueldo = Sueldo()
    return asdict(sueldo).get(cargo, None)


class Test(TestCase):

    def test_sueldo(self):
        self.assertEqual(sueldo("jefe"), 100)
        self.assertEqual(sueldo("Ejecutivo"), 90)
        self.assertEqual(sueldo("EXTERNO"), 50)

        self.assertEqual(sueldo_("JEFE"), 100)
        self.assertEqual(sueldo_("auxiliar"), None)

        self.assertEqual(_sueldo("jefe"), 100)
        self.assertEqual(sueldo_("auxiliar"), None)

        s = Sueldo()
        self.assertEqual(fields(s)[0].metadata["unit"], "dollars")
        self.assertEqual(fields(s)[1].metadata["unit"], "dollars")
        self.assertEqual(fields(s)[2].metadata["unit"], "dollars")


if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
    main()