from prototools.menu import EzMenu
from app import App


def main():
    app = App()
    menu = EzMenu()
    menu.titulo('Banco de materiales')
    menu.agregar_opciones(
        "Registrar alumno",
        "Registrar material",
        "Materiales disponibles por materia",
        "Ver documento",
        "Materiales disponibles por carrera",
        "Materiales por calificación",
        "Aportantes",
        "Guadar datos",
        "Cargar datos",
        "Salir",
    )
    menu.agregar_funciones(
        app.registrar_estudiante,
        app.registrar_material,
        app.materiales_disponibles,
        app.ver_documento,
        app.materiales_por_carrera,
        app.materiales_por_calificacion,
        app.aportantes,
        app.save,
        app.load,
    )
    menu.run()


if __name__ == '__main__':
    main()