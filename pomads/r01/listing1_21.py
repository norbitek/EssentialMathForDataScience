from sympy import *
from sympy.plotting import plot3d
# Deklarujemy x i y w SymPy
x,y = symbols('x y')
# Teraz używamy zwykłej składni Pythona do zadeklarowania funkcji
f = 2*x**3 + 3*y**3
# Obliczamy pochodne cząstkowe względem x i y
dx_f = diff(f, x)
dy_f = diff(f, y)
print(dx_f) # wypisuje 6*x**2
print(dy_f) # wypisuje 9*y**2
# Tworzymy wykres funkcji
plot3d(f)
