"""Standalone version (7 lines of code without ';', 1 line with ';').
"""

h = lambda m, n=2: tuple([m[x:x+n] for x in range(0, len(m), n)])
t = lambda a, b: (b[0] - a[0]) * (b[1] - a[1])
f = lambda a, b, g: (g(a[0], b[0]), g(a[1], b[1]))
(p, q), (r, s) = list(map(h, [list(map(int, input().split())) for _ in "mk"]))
x, y = f(p, r, max), f(q, s, min)
(x, y) = ((0, 0), (0, 0)) if max(x) > min(y) else (x, y)
print(t(p, q) + t(r, s) - t(x, y))