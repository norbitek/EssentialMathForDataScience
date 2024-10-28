from sympy import *

# Deklarujemy 'x' w SymPy
x = symbols('x')

# Teraz używamy zwykłej składni Pythona do zadeklarowania funkcji
f = 3*x**2 + 1

# Obliczamy pochodną funkcji
dx_f = diff(f)
print(dx_f) # wypisuje 6*x
print(dx_f.subs(x,3)) # 18
