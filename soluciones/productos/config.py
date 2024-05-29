"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import magenta, cyan, yellow, red, green

SETTINGS = {
    "main": {
        "title": cyan("AyudaEnPython"),
        "subtitle": "Sistema",
        "exit_option_text": magenta("Salir"),
        "exit_option_color": magenta,
        "arrow_keys": False,
    },
    "extra": {
        "subtitle_align": "center",
        "style": "double",
        "color": magenta,
        "options_color": yellow,
        "separators": True,
    }
}
HEADERS = {
    "product": ("Producto", "Elaboración", "Vencimiento", "Estado"),
    "client": ("Nombre", "Apellido", "Cédula"),
}
COLORS = {
    "vencido": red("vencido"),
    "por vencer": yellow("por vencer"),
    "vigente": green("vigente"),
}
