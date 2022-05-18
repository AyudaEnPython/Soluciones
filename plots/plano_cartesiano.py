"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import numpy as np
import matplotlib.pyplot as plt

xs = [0, 2, -3, -1.5]
ys = [0, 3, 1, -2.5]
colors = ['m', 'g', 'r', 'b']
xmin, xmax, ymin, ymax = -5, 5, -5, 5
ticks_frequency = 1

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(xs, ys, c=colors)

for x, y, c in zip(xs, ys, colors):
    ax.plot([x, x], [0, y], c=c, ls='--', lw=1.5, alpha=0.5)
    ax.plot([0, x], [y, y], c=c, ls='--', lw=1.5, alpha=0.5)

ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
y_ticks = np.arange(ymin, ymax+1, ticks_frequency)

ax.set_xticks(x_ticks[x_ticks != 0])
ax.set_yticks(y_ticks[y_ticks != 0])
ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
ax.set_yticks(np.arange(ymin, ymax+1), minor=True)
ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

arrow_fmt = dict(markersize=4, color='black', clip_on=False)

ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
plt.show()
