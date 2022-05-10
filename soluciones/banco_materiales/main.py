"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from prototools import Menu
from app import App


def main():
    app = App()
    menu = Menu("Banco de Materiales")
    menu.add_options(
        ("Registrar alumno", app.registrar_estudiante),
        ("Registrar material", app.registrar_material),
        ("Materiales disponibles por materia", app.materiales_disponibles),
        ("Ver documento", app.ver_documento),
        ("Materiales disponibles por carrera",
            app.materiales_disponibles_carrera),
        ("Aportantes", app.aportantes),
        ("Guardar datos", app.save),
        ("Cargar datos", app.load),
    )
    menu.run()


if __name__ == '__main__':
    main()
