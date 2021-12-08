"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass


@dataclass
class Empleado:
    nombres: str
    apellidos: str
    edad: int
    sueldo: float
    id_: int
    antiguedad: int

    def aumentrar_sueldo(self, aumento) -> None:
        if aumento < 0:
            print("No se puede aumentar el sueldo")
        self.sueldo += aumento

    def datos(self) -> None:
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Edad: {self.edad}")
        print(f"Sueldo: {self.sueldo}")
        print(f"ID: {self.id_empleado}")
        print(f"Antiguedad: {self.antiguedad}")


@dataclass
class Supervisor(Empleado):
    licenciatura: str
    area_supervisada: str

    def supervisar(self) -> None:
        ...

    def datos(self) -> None:
        super().datos()
        print(f"Licenciatura: {self.licenciatura}")


@dataclass
class Administrativo(Empleado):
    nivel_estudios: str
    supervisor: Supervisor


@dataclass
class Analista(Administrativo):
    habilidades: str

    def analizar(self) -> None:
        ...

    def optimizar(self) -> None:
        ...

    def datos(self) -> None:
        super().datos()
        print(f"Nivel de estudios: {self.nivel_estudios}")
        print(f"Habilidades: {self.habilidades}")
        print(f"Supervisor: {self.supervisor.nombres}")


@dataclass
class Operativo(Administrativo):
    habilidades: str

    def tecnicas(self) -> None:
        ...
    
    def ejecutar(self) -> None:
        ...

    def datos(self) -> None:
        super().datos()
        print(f"Habilidades: {self.habilidades}")
        print(f"Supervisor: {self.supervisor.nombres}")