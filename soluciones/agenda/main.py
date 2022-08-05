"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict, List
# pip install prototools
from prototools import Menu, str_input, textbox, tabulate


def _mostrar(contactos: Dict[str, List[str]]) -> None:
    if len(contactos) == 0:
        textbox("No hay contactos")
    else:
        print(tabulate(
            [p.to_list() for p in contactos.values()],
            headers=["Nombre", "Telefono", "Email"],
        ))


class Persona:

    def __init__(self, nombre: str, telefono: str, email: str) -> None:
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def to_list(self) -> List[str]:
        return [self.nombre, self.telefono, self.email]

    def __str__(self) -> str:
        return (
            f"Nombre: {self.nombre}\nTelefono: {self.telefono}"
            f"\nEmail: {self.email}"
        )


class Agenda:

    def __init__(self) -> None:
        self.contactos: Dict[str, Persona] = {}

    def _buscar(self, nombre: str) -> bool:
        if nombre not in self.contactos:
            return False
        return True

    def agregar(self, nombre: str, telefono: str, email: str) -> None:
        self.contactos[nombre] = Persona(nombre, telefono, email)

    def buscar(self, nombre: str) -> Persona:
        if self._buscar(nombre):
            return self.contactos[nombre]

    def editar(self, nombre: str, telefono: str, email: str) -> None:
        self.contactos[nombre].telefono = telefono
        self.contactos[nombre].email = email

    def eliminar(self, nombre: str) -> None:
        del self.contactos[nombre]

    def mostrar(self) -> None:
        _mostrar(self.contactos)


class App(Menu):

    def __init__(self) -> None:
        super().__init__()
        self.agenda = Agenda()
        self.title = "Agenda"
        self.add_options(
            ('Agregar contacto', self.agregar_contacto),
            ("Lista de contactos", self.listar_contactos),
            ("Buscar contacto", self.buscar_contacto),
            ("Editar contacto", self.editar_contacto),
            ("Eliminar contacto", self.eliminar_contacto),
        )

    def agregar_contacto(self) -> None:
        nombre = str_input("Nombre: ")
        telefono = str_input("Telefono: ")
        email = str_input("Email: ")
        contacto = self.agenda.buscar(nombre)
        if contacto is None:
            self.agenda.agregar(nombre, telefono, email)
        else:
            textbox("Contacto ya existe")

    def listar_contactos(self) -> None:
        self.agenda.mostrar()

    def buscar_contacto(self) -> None:
        nombre = str_input("Nombre: ")
        contacto = self.agenda.buscar(nombre)
        if contacto is None:
            textbox("Contacto no encontrado")
        else:
            print(f"\n{contacto}")

    def editar_contacto(self) -> None:
        nombre = str_input("Nombre: ")
        contacto = self.agenda.buscar(nombre)
        if contacto is None:
            textbox("Contacto no encontrado")
        else:
            telefono = str_input("Telefono: ")
            email = str_input("Email: ")
            self.agenda.editar(nombre, telefono, email)

    def eliminar_contacto(self) -> None:
        nombre = str_input("Nombre: ")
        contacto = self.agenda.buscar(nombre)
        if contacto is None:
            textbox("Contacto no encontrado")
        else:
            self.agenda.eliminar(nombre)


if __name__ == "__main__":
    app = App()
    app.run()
