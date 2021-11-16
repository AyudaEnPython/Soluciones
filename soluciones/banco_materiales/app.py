import pickle
from typing import Dict, List, Optional

from models import Carrera, Estudiante, Materia, Material, BancoMateriales
from prototools.entradas import entrada_choices, entrada_int, entrada_str, entrada_choice, entrada_fecha

CARRERAS: Dict[str, Carrera] = {
    "C01": Carrera("C01", "Informática", "Ciencias"),
    "C02": Carrera("C02", "Economía", "Ciencias"),
    "C03": Carrera("C03", "Electrónica", "Ciencias"),
    "C04": Carrera("C04", "Sociales", "Letras"),
}
MATERIAS: Dict[str, Materia] = {
    "M01": Materia("M01", "M001", "I", CARRERAS["C01"]),
    "M02": Materia("M02", "M002", "II", CARRERAS["C02"]),
    "M03": Materia("M03", "M003", "III", CARRERAS["C03"]),
    "M04": Materia("M04", "M004", "IV", CARRERAS["C04"]),
}


def registrar_datos_estudiante(datos: Dict[str, Estudiante]) -> Estudiante:
    f = lambda x: True if x == "si" else False
    codigo = entrada_str("Ingresar código: ")
    if codigo in datos:
        print("El código ya existe")
        return
    return Estudiante(
        codigo=codigo,
        nombre=entrada_str("Ingresar nombre: "),
        apellido=entrada_str("Ingresar apellido: "),
        ingreso=entrada_fecha("Ingresar fecha de ingreso: "),
        recibido=f(entrada_choice(("si", "no"), "¿Recibido?")),
    )


def registrar_material(datos: List[Material]) -> Material:
    codigo = entrada_str("Ingresar código: ")
    for data in datos:
        if data.codigo == codigo:
            print("El código ya existe")
            return
    return Material(
        codigo=codigo,
        titulo=entrada_str("Ingresar título: "),
        contenido=entrada_str("Ingresar contenido: "),
        materia=entrada_choices(MATERIAS, "Ingresar materia: "),
        gestor=entrada_str("Ingresar gestor: "),
        calificacion=entrada_int("Ingresar calificación: "),
    )


class App(BancoMateriales):

    def __init__(
        self,
        estudiantes: Optional[Dict[str, Estudiante]] = None,
        materiales: Optional[List[Material]] = None
    ) -> None:
        super().__init__(materiales)
        if estudiantes is None and materiales is None:
            self.load()
        self._estudiantes = estudiantes
        self._materiales = materiales
    
    def registrar_estudiante(self) -> None:
        estudiante = registrar_datos_estudiante(self._estudiantes)
        self._estudiantes[estudiante.codigo] = estudiante

    def registrar_material(self) -> None:
        material = registrar_material(self._materiales)
        self._materiales.add_material(material)

    def materiales_disponibles(self) -> None:
        materia = input('Ingrese la materia: ')
        self._materiales.ver_por_materia(materia)

    def ver_documento(self) -> None:
        codigo = input('Ingrese el codigo del material: ')
        self._materiales.ver_documento(codigo)

    def materiales_por_carrera(self) -> None:
        carrera = input('Ingrese la carrera: ')
        self._materiales.cantidad_materiales_por_carrera(carrera)

    def materiales_por_calificacion(self) -> None:
        calificacion = input('Ingrese la calificacion: ')
        self._materiales.ver_por_calificacion(int(calificacion))

    def aportantes(self) -> None:
        self._materiales.ver_gestores()

    def save(self) -> None: # 'soluciones/banco_materiales/'
        with open('data/materiales.pickle', 'wb') as f:
            pickle.dump(self._materiales, f)
        with open('data/estudiantes.pickle', 'wb') as f:
            pickle.dump(self._estudiantes, f)

    def load(self) -> None: # 'soluciones/banco_materiales/'
        with open('data/materiales.pickle', 'rb') as f:
            self._materiales = pickle.load(f)
        with open('data/estudiantes.pickle', 'rb') as f:
            self._estudiantes = pickle.load(f)