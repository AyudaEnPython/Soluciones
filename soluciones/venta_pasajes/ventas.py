"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from database import VentaDAO


class Gestor:

    def __init__(self, dao: VentaDAO) -> None:
        dao = dao

    def registrar(self, obj) -> None:
        # TODO: Implementar
        self.dao.insertar(obj)

    def modificar(self, obj) -> None:
        # TODO: Implementar
        self.dao.actualizar(obj)

    def eliminar(self, obj) -> None:
        # TODO: Implementar
        self.dao.eliminar(obj)

    def seleccionar(self, obj) -> None:
        # TODO: Implementar
        self.dao.seleccionar(obj)
