"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

s = ""
for x in range(1, 10):
    s += str(x)
    print(f"{s} * 8 + {x} = {int(s) * 8 + x}")
