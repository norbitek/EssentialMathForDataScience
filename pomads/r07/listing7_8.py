from sympy import *

Z2 = symbols('Z2')

logistyczna = lambda x: 1 / (1 + exp(-x))

A2 = logistyczna(Z2)
dA2_dZ2 = diff(A2, Z2)
print(dA2_dZ2) # exp(-Z2)/(1 + exp(-Z2))**2
