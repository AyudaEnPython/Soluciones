# pip install prototools
from prototools import Menu
from empresa import Empresa


def main():
    empresa = Empresa()
    menu = Menu(
        "Ayuda En Python",
        "Gestión de Empleados",
        exit_option_text="Salir",
    )
    menu.add_options(
        ("Dar de alta a emplado", lambda: print()),
        ("Aumentar sueldo a empleado", empresa.aumentar_sueldo),
        ("Lista de empleados", lambda: print()),
        ("Buscar empleado", lambda: print()),
        ("Mostrar empleados por tipo", lambda: print()),
        ("Asignar supervisor a empleado", lambda: print()),
    )
    menu.settings(
        style="double",
    )
    menu.run()


if __name__ == "__main__":
    main()