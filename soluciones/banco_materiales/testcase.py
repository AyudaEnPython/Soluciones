"""
TODO: add testcases
"""
from unittest import main, TestCase

from models import Estudiante, Carrera, Materia, Material, BancoMateriales
from app import MATERIAS

estudiantes = {
    "001": Estudiante("001", "John", "Wick", "01/01/2020", True),
    "002": Estudiante("002", "Jane", "Doe", "11/01/2020", True),
    "003": Estudiante("003", "John", "Doe", "11/03/2020", True),
}

materiales = BancoMateriales([
    Material("01", "AAA", "aaa", MATERIAS["M01"], estudiantes["001"], 10),
    Material("02", "BBB", "bbb", MATERIAS["M02"], estudiantes["002"], 8),
    Material("03", "CCC", "ccc", MATERIAS["M03"], estudiantes["003"], 5),
    Material("04", "DDD", "ddd", MATERIAS["M04"], estudiantes["003"], 2),
])


class TestApp(TestCase):

    def test_estudiante(self):
        self.assertEqual(estudiantes["001"].nombre, "John")
        self.assertEqual(estudiantes["001"].apellido, "Wick")

    def test_materiales(self):
        self.assertEqual(materiales.materiales[0].nombre, "AAA")
        self.assertEqual(materiales.materiales[0].descripcion, "aaa")
        self.assertEqual(materiales.materiales[0].materia, MATERIAS["M01"])
        self.assertEqual(
            materiales.materiales[0].estudiante, estudiantes["001"]
        )
        self.assertEqual(materiales.materiales[0].calificacion, 10)


if __name__ == "__main__":
    # main()
    materiales.ver_por_materia("M003")
    materiales.ver_documento("01")
    materiales.cantidad_materiales_por_carrera("Informática")
    materiales.ver_por_calificacion(5)
    materiales.ver_gestores()