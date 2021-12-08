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

    def aumentrar_sueldo(self, aumento):
        if aumento < 0:
            print("No se puede aumentar el sueldo")
        self.sueldo += aumento

    def datos(self):
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

    def supervisar(self):
        pass

    def datos(self):
        super().datos()
        print(f"Licenciatura: {self.licenciatura}")


@dataclass
class Administrativo(Empleado):
    nivel_estudios: str
    supervisor: Supervisor


@dataclass
class Analista(Administrativo):
    habilidades: str

    def analizar(self):
        pass

    def optimizar(self):
        pass

    def datos(self):
        super().datos()
        print(f"Nivel de estudios: {self.nivel_estudios}")
        print(f"Habilidades: {self.habilidades}")
        print(f"Supervisor: {self.supervisor.nombres}")


@dataclass
class Operativo(Administrativo):
    habilidades: str

    def tecnicas(self):
        pass
    
    def ejecutar(self):
        pass

    def datos(self):
        super().datos()
        print(f"Habilidades: {self.habilidades}")
        print(f"Supervisor: {self.supervisor.nombres}")