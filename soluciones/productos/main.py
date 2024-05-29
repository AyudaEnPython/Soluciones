"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from views import MainView
from models import Database
from controllers import MainController
from config import SETTINGS


def main():
    model = Database()
    view = MainView(SETTINGS["main"])
    controller = MainController(model, view)
    view.add_options(
        ("Ingresar cliente", controller.add_client),
        ("Ingresar producto", controller.add_product),
        ("Buscar cliente", controller.search_client),
        ("Buscar producto", controller.search_product),
        ("Asociar producto a cliente", controller.set_relation),
        ("Mostrar productos del cliente", controller.show_client_products),
    )
    view.settings(**SETTINGS["extra"])
    controller.run()


if __name__ == "__main__":
    main()
