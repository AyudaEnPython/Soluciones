"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Se deben definir tres funciones que permitan la interaccion de las
opciones del menú, en la opción 1 se debe preguntar el nombre del
usuario y su correo electrónico, pero antes de añadirlos al
diccionario deberá validar que el correo ingresado pertenezca al
dominio de la institución, podrá ingresar la cantidad de usuarios que
desee. Después se debe mostrar por pantalla la lista de los usuarios
admitidos con su respectivo correo electrónico. Una vez completos se
podrá regresar al menú principal.
En la opción 2, se debe solicitar el nombre del usuario que se desea
eliminar y se mostrará el diccionario actualizado. Una vez completos
los usuarios se podrá regresar al menú principal.
Si se digita un nombre que no esté en el diccionario, debe enviar un
mensaje indicando que la entrada es incorrecta.
"""
from dataclasses import dataclass, field
from typing import Dict
# pip install prototools
from prototools import Menu, main_loop, text_align


# https://github.com/AyudaEnPython/Soluciones/blob/main/ejercicios/validar_correo.py
def _validar_correo(usuario: str, dominio: str = '@calufa.com') -> bool:
    if usuario.endswith(dominio):
        return True
    return False


@dataclass
class Usuario:
    nombre: str
    correo: str


@dataclass
class Sistema:
    usuarios: Dict[str, Usuario] = field(default_factory=dict)

    def _add_user(self) -> None:
        nombre = input('Nombre de usuario: ')
        correo = input('Correo electrónico: ')
        if _validar_correo(correo):
            self.usuarios[nombre] = Usuario(nombre, correo)
        else:
            print('Correo inválido')

    def _delete_user(self) -> None:
        nombre = input('Nombre de usuario: ')
        if nombre in self.usuarios:
            del self.usuarios[nombre]
        else:
            print('Usuario no encontrado')

    def add_users(self) -> None:
        main_loop(self._add_user)
        text_align("Lista de usuarios")
        self._show_users()

    def delete_users(self) -> None:
        main_loop(self._delete_user)
        text_align("Lista de usuarios actualizada")
        self._show_users()

    def _show_users(self) -> None:
        for nombre, usuario in self.usuarios.items():
            print(f'{nombre} - {usuario.correo}')


def main():
    sistema = Sistema()
    menu = Menu("Bienvenidos al CTPN CALUFA")
    menu.add_options(
        ("Agregar usuarios", sistema.add_users),
        ("Eliminar usuarios", sistema.delete_users),
    )
    menu.run()


if __name__ == '__main__':
    main()
