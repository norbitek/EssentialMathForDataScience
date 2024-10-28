from sympy import *

# Kreślimy funkcję ReLU
x = symbols('x')
relu = Max(0, x)
plot(relu)
