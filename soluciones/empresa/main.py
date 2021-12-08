# pip install prototools
from prototools import Menu
from prototools.colorize import magenta, yellow, red, green, cyan
from empresa import Empresa


def main():
    empresa = Empresa()
    menu = Menu(
        yellow("Ayuda En Python"),
        prologue_text=cyan("Gestión de Empleados"),
        exit_option_text="Salir",
        exit_option_color=red,
    )
    menu.add_options(
        (yellow("Dar de alta a emplado"), empresa.agregar_empleado),
        (yellow("Aumentar sueldo a empleado"), empresa.aumentar_sueldo),
        (yellow("Lista de empleados"), empresa.mostrar_empleados),
        (yellow("Buscar empleado"), empresa.buscar_empleado),
        (yellow("Mostrar empleados por tipo"), empresa.mostrar_por_tipo),
        (yellow("Asignar supervisor a empleado"), empresa.asignar_supervisor),
    )
    menu.settings(
        style="double",
        color=magenta,
        options_color=green,
        header_bottom=True,
        separators=True,
    )
    menu.run()


if __name__ == "__main__":
    main()