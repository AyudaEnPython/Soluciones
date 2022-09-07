"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Cree una clase Alumno e inicialícela con el nombre y el número de
registro. Haga los métodos para:

1. Display - Debe mostrar toda la información del estudiante (nombre y
    número de registro).
2. setAge - Debe asignar la edad del estudiante
3. setNota - Debe asignar las notas del estudiante.

NOTE: Se opta por seguir las instrucciones (lo ideal seria usar
    dataclasses y properties). Se modifica los nombres de los métodos
    para seguir PEP8.
"""


class Alumno:

    def __init__(self, nombre, registro) -> None:
        self._nombre = nombre
        self._registro = registro

    def display(self):
        print(f"Nombre: {self._nombre}")
        print(f"Registro: {self._registro}")

    def set_edad(self, edad):
        self._edad = edad

    def set_nota(self, nota):
        self._nota = nota

    def get_edad(self):
        return self._edad

    def get_nota(self):
        return self._nota


if __name__ == "__main__":
    alumno = Alumno("Jason Becker", "55620158")
    alumno.set_edad(19)
    alumno.set_nota(20)
    alumno.display()
    print(f"Edad: {alumno.get_edad()}")
    print(f"Nota: {alumno.get_nota()}")
