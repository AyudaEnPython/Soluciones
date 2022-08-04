"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from enum import Enum
from turtle import Screen, Turtle


class Color(Enum):
    RED = 3
    YELLOW = 1
    GREEN = 2


class Semaforo:

    def __init__(self) -> None:
        self.luz = Color.YELLOW

    def cambiar(self) -> Color:
        if self.luz == Color.RED:
            self.luz = Color.GREEN
        elif self.luz == Color.YELLOW:
            self.luz = Color.RED
        else:
            self.luz = Color.YELLOW
        return self.luz.name.lower()

    def tiempo(self) -> int:
        return self.luz.value


class App:

    POS = {"red": 70, "yellow": 0, "green": -70}

    def __init__(self) -> None:
        self.semaforo = Semaforo()
        self.screen = Screen()
        self.luz = Turtle()
        self._setup()

    def _setup(self) -> None:
        self.screen.bgcolor("black")
        self.screen.setup(140, 260)
        for ypos in self.POS.values():
            cursor = Turtle()
            self.encender(cursor, ypos, "gray")
        self.start()

    def encender(self, cursor: Turtle, d_y: int, color: str) -> None:
        cursor.ht()
        cursor.speed(0)
        cursor.penup()
        cursor.sety(d_y)
        cursor.pendown()
        cursor.shape("circle")
        cursor.shapesize(3)
        cursor.fillcolor(color)
        cursor.showturtle()

    def start(self) -> None:
        color = self.semaforo.cambiar()
        self.encender(self.luz, self.POS[color], color)
        self.screen.ontimer(self.start, self.semaforo.tiempo()*1000)


if __name__ == "__main__":
    app = App()
    app.screen.mainloop()
