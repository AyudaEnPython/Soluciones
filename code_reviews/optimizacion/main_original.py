"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import cvxpy as cp
import numpy as np

w = cp.Variable(shape=(3,1), name="w")
Sigma = np.array([[0.040,0.003,0.009],
                  [0.003,0.024,0.011],
                 [0.009,0.011,0.031]])
mu_t = np.array([0.15,0.07,0.09])
objective = cp.Minimize(cp.quad_form(w,Sigma))
retornos = [0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15]
for i in retornos:
    constraints = np.array([mu_t@w == i,
               cp.sum(w,axis=0) == 1, 
               w>=0])
print(constraints)
problem = cp.Problem(objective, constraints)
solution = problem.solve()
print('Valor mínimo: ', np.round(solution,4))
print('Solución: ', np.round(w.value,4))

# Output:
# [Equality(Expression(AFFINE, UNKNOWN, (1,)), Constant(CONSTANT, NONNEGATIVE, ()))
#  Equality(Expression(AFFINE, UNKNOWN, (1,)), Constant(CONSTANT, NONNEGATIVE, ()))
#  Inequality(Constant(CONSTANT, ZERO, ()))]
# Valor mínimo:  0.04
# Solución:  [[1.]
#  [0.]
#  [0.]]