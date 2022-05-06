
from collections import deque
from random import randint
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = plt.axes(xlim=(0, 200), ylim=(0, 100))
line, = ax.plot([], [])
y_list = deque([-1] * 400)
x_list = deque(np.linspace(200, 0, num=400))


def init():
    line.set_data([], [])
    return line,


def animate(i):
    y_list.pop()
    y_list.appendleft(randint(12, 24))
    line.set_data(x_list, y_list)
    return line,


if __name__ == "__main__":
    anim = animation.FuncAnimation(
        fig,
        animate,
        init_func=init,
        frames=200,
        interval=100,
        blit=True,
    )
    plt.show()
