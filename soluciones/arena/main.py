"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from models import Arena, Guerrero
# pip install prototools
from prototools import Menu, int_input, str_input, textbox


class Game(Menu):

    def __init__(self, arena: Arena):
        super().__init__()
        self.arena = arena
        self.add_options(
            ("Simular batalla", self.arena.simulacion),
            ("Añadir guerrero", self._add_guerrero),
            ("Ver guerreros", self._ver_guerreros),
            ("Restaurar guerreros", self._restaurar_guerreros),
        )

    def _add_guerrero(self):
        textbox("Añadir nuevo guerrero")
        self.arena.guerreros.append(Guerrero(
            str_input("Nombre: "),
            int_input("Vida: "),
            int_input("Fuerza: "),
            int_input("Precision: "),
            int_input("Velocidad: "),
            int_input("Defensa: "),
        ))
        textbox("Guerrero añadido")

    def _ver_guerreros(self):
        print("\n".join(map(str, self.arena.guerreros)))

    def _restaurar_guerreros(self):
        for guerrero in self.arena.guerreros:
            guerrero.vida = 100


if __name__ == "__main__":
    game = Game(Arena([
        Guerrero("Superman", 100, 70, 80, 30, 20),
        Guerrero("Goku", 100, 60, 80, 40, 20),
        Guerrero("Chuck Norris", 200, 99, 99, 99, 99),
    ]))
    game.run()
