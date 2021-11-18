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
from prototools.menu import EzMenu
from prototools.experimental import main_loop
from prototools.utils import continuar, boxln

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
        main_loop(self._add_user, continuar)
        boxln("Lista de usuarios", ancho=80)
        self._show_users()

    def delete_users(self) -> None:
        main_loop(self._delete_user, continuar)
        boxln("Lista de usuarios actualizada", ancho=80)
        self._show_users()    

    def _show_users(self) -> None:
        for nombre, usuario in self.usuarios.items():
            print(f'{nombre} - {usuario.correo}')


def main():
    sistema = Sistema()
    menu = EzMenu(ancho=80)
    menu.titulo("Bienvenidos al CTPN CALUFA")
    menu.agregar_opciones(
        "Agregar usuarios",
        "Eliminar usuarios",
        "Salir",
    )
    menu.agregar_funciones(
        sistema.add_users,
        sistema.delete_users,
    )
    menu.run()


if __name__ == '__main__':
    main()