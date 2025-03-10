"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: Revisar las notas del README
"""
from prototools import clear_screen, Menu, menu_input, textbox
from prototools.components import Box, render
from prototools.colorize import magenta, cyan, yellow

MESSAGE = "Tu número es"
OPTS = "si", "no"


def show_instructions():
    render(Box(
        title=cyan("¿Cómo jugar?"),
        title_align="center",
        color=magenta,
        subtitle="Lee las siguientes instrucciones:",
        textnl="""
        - Piensa en un número del 1 al 100 y lo adivinaré.
        - Responde con 'si' o 'no' a mis preguntas.
        """
    ))


def main():
    low = 1
    high = 100
    while low <= high:
        mid = (low + high) // 2
        response = menu_input(OPTS, prompt=f"¿{MESSAGE} {mid}?\n")
        if response == "si":
            textbox(f"¡Genial, lo adiviné! {MESSAGE} {mid}.", bcolor="magenta")
            break
        response = menu_input(OPTS, prompt=f"¿{MESSAGE} mayor que {mid}?\n")
        if response == "si":
            low = mid + 1
        else:
            high = mid - 1
        clear_screen()
    if low > high:
        textbox("Parece que hay contradicciones en tus respuestas.")
    textbox(cyan("¡Fin del juego!"), bcolor="magenta")


if __name__ == "__main__":
    menu = Menu(
        cyan("Adivino tu número"),
        yellow("AyudaEnPython"),
        exit_option_text=magenta("Salir"),
        exit_option_color=magenta,
    )
    menu.add_options(
        ("Leer instrucciones", show_instructions),
        ("Jugar", main),
    )
    menu.settings(
        subtitle_align="center",
        style="double",
        color=magenta,
        separators=True,
    )
    menu.run()
