"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: get rid off magic numbers
"""
from turtle import Turtle, Screen, done

W, H = 600, 400
POSITIONS = ((60, 150), (90, 120), (120, 90), (150, 60))


def _draw(t, x, y, color, g, *args):
    t.pu()
    t.setpos(x, y)
    t.pd()
    t.color(color)
    t.begin_fill()
    g(*args)
    t.end_fill()
    t.ht()


def _rect(t, w, h):
    for n in (w, h, w, h):
        t.fd(n)
        t.rt(90)


def _star(t):
    for _ in range(5):
        t.fd(50)
        t.rt(144)


def leaves(t, size, pos):
    t.color("forest green")
    t.begin_fill()
    t.setpos(0, pos)
    t.setpos(size, pos - size)
    t.setpos(-size, pos - size)
    t.setpos(0, pos)
    t.end_fill()
    t.ht()


def trunk(t):
    w, h = W // 15, H // 8
    _draw(t, -(w//2), -90, "chocolate", _rect, t, w, h)


def snow(t):
    _draw(t, -(W//2), -140, "white", _rect, t, W, W//10)


def star(t):
    _draw(t, -25, 170, "yellow", _star, t)


def main():
    xmas = Screen()
    b, y, m, k = Turtle(), Turtle(), Turtle(), Turtle()
    xmas.tracer(0)
    xmas.setup(W, H)
    xmas.bgcolor("sky blue")
    trunk(y)
    snow(m)
    for size, pos in POSITIONS:
        leaves(b, size, pos)
    star(k)
    xmas.update()
    done()


if __name__ == "__main__":
    main()
