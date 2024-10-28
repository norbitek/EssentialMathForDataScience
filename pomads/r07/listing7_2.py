from sympy import *

# Kreślimy funkcję logistyczną
x = symbols('x')
logistyczna = 1 / (1 + exp(-x))
plot(logistyczna)
