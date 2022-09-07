"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Lee la hora actual del ordenador y la devuelve en un formato legible.
"""

import time

# 1
print(time.asctime())

# 2
print(time.strftime("%c"))

# 3
print(time.strftime("%H:%M:%S %d/%m/%Y"))
