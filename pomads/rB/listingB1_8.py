from sympy import *

# Deklarujemy 'x' w SymPy
x = symbols('x')

# Teraz używamy zwykłej składni Pythona do zadeklarowania funkcji
f = 3*x**2 + 1

# Obliczamy całkę funkcji względem x
# dla obszaru między x = 0 a x = 2
pole = integrate(f, (x, 0, 2))
print(pole) # wypisuje 10
