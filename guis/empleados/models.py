"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import re
from dataclasses import dataclass, field
from datetime import date
# pip install prototools
from prototools.protosql import Incrementor, ProtoSqlite

DESCUENTO = 0.10
c = Incrementor()
db = ProtoSqlite("data.db", lang="es")


def generar_codigo():
    db = ProtoSqlite("data.db")
    last = db.get_last("empleados", index=3)
    if last is None:
        return "E001"
    id_ = c.count
    last = int(re.findall(r'\d+', last)[0])
    if last >= id_:
        id_ = last + 1
    c.count = id_
    return f"E{id_:03}"


class Sistema(ProtoSqlite):

    def __init__(self) -> None:
        super().__init__("data.db", lang="es")

    def insertar(self, object_: object) -> None:
        self.add("empleados", object_.__dict__)

    def eliminar(self, pk: str) -> None:
        self._delete("empleados", f"codigo='{pk}'")

    def actualizar(self, value: str, pk: str) -> None:
        self.update("empleados", f"sueldo='{value}'", f"codigo='{pk}'")

    def seleccionar(self, pk: str) -> object:
        return self.get("empleados", f"codigo='{pk}'")


@dataclass
class Empleado:
    nombre: str
    cargo: str
    sueldo: float
    codigo: str = field(init=False)
    fecha: date = field(
        default_factory=lambda: date.today().strftime("%d/%m/%Y")
    )
    descuento: float = field(init=False)
    neto: float = field(init=False)

    def __post_init__(self):
        self.codigo = generar_codigo()
        if self.sueldo > 1800:
            self.descuento = self.sueldo * DESCUENTO
        else:
            self.descuento = 0
        self.neto = self.sueldo - self.descuento

    def to_str(self) -> str:
        return (
            f"Empleado: {self.nombre}\n"
            f"Código: {self.codigo}\n"
            f"Sueldo Total: {self.sueldo}\n"
            f"Descuento: {self.descuento}\n"
            f"Sueldo Neto: {self.neto}"
        )


if __name__ == "__main__":
    db = ProtoSqlite("data.db", lang="es")
    db.create_table("empleados", Empleado, pk="codigo")
