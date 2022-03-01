"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

"""
from prototools import Menu
from prototools.colorize import cyan, yellow, magenta

from controllers import Controlador
from models import Modelo
from views import VistaFancy


def main():
    menu = Menu(
        cyan("Generador de números aleatorios"),
        yellow("Ejemplo MVC"),
        exit_option_text=magenta("Salir"),
        exit_option_color=magenta,
    )
    controlador = Controlador(Modelo(), VistaFancy())
    menu.add_options(
        ("Configurar", controlador.configurar),
        ("Mostrar Numeros", controlador.numeros),
        ("Mostrar Pares", controlador.pares),
        ("Mostrar Impares", controlador.impares),
    )
    menu.settings(
        subtitle_align="center",
        style="double",
        color=magenta,
        options_color=yellow,
        separators=True,
    )
    menu.run()


if __name__ == '__main__':
    main()
