from sympy import *

# Deklarujemy 'x' w SymPy
x = symbols('x')

# Teraz używamy zwykłej składni Pythona do zadeklarowania funkcji
f = x**2 + 1

# Obliczamy całkę funkcji względem x
# w obszarze między x = 0 a 1
pole = integrate(f, (x, 0, 1))

print(pole) # wypisuje 4/3
