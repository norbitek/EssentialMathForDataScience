from sympy import *
# Deklarujemy 'x' w SymPy
x = symbols('x')
# Teraz używamy zwykłej składni Pythona, aby zadeklarować funkcję
f = x**2
# Obliczamy pochodną funkcji
dx_f = diff(f)
print(dx_f) # wypisuje 2*x
