"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import cvxpy as cp
import numpy as np
from typing import NewType, Tuple

Expression = NewType("Expression", object)


def solve_(w: Expression) -> Tuple[np.float64, np.ndarray]:
    solution = cp.Problem(
        cp.Minimize(cp.quad_form(w, sigma)),
        np.array([mu_t@w == x, cp.sum(w, axis=0) == 1, w >= 0])
    ).solve()
    return solution, w.value


sigma = np.array([
    [0.040, 0.003, 0.009],
    [0.003, 0.024, 0.011],
    [0.009, 0.011, 0.031],
])
mu_t = np.array([0.15, 0.07, 0.09])
xs = np.arange(0.09, 0.151, 0.01)

for x in xs:
    sol, val = solve_(cp.Variable(shape=(3, 1), name="w"))
    print(f"Valor mínimo: {np.round(sol, 4)}")
    print(f"Solución:\n {np.round(val, 4)}")

# Output:
# Valor mínimo: 0.0155
# Solución:
#  [[0.1889]
#  [0.5668]
#  [0.2442]]
# Valor mínimo: 0.0151
# Solución:
#  [[0.3191]
#  [0.4574]
#  [0.2235]]
# Valor mínimo: 0.0164
# Solución:
#  [[0.4493]
#  [0.3479]
#  [0.2028]]
# Valor mínimo: 0.0195
# Solución:
#  [[0.5795]
#  [0.2385]
#  [0.182 ]]
# Valor mínimo: 0.0244
# Solución:
#  [[0.7097]
#  [0.129 ]
#  [0.1613]]
# Valor mínimo: 0.0311
# Solución:
#  [[0.8399]
#  [0.0196]
#  [0.1406]]
# Valor mínimo: 0.04
# Solución:
#  [[1.]
#  [0.]
#  [0.]]