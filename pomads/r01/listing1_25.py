from sympy import *
x, y = symbols('x y')
# pochodna pierwszej funkcji
# poprzedzamy y znakiem podkreślenia, aby zapobiec konfliktowi zmiennych
_y = x**2 + 1
dy_dx = diff(_y)
# pochodna drugiej funkcji
z = y**3 - 2
dz_dy = diff(z)
# obliczamy pochodną przy użyciu i bez użycia
# reguły łańcuchowej, podstawiając funkcję y
dz_dx_z_regula = (dy_dx * dz_dy).subs(y, _y)
dz_dx_bez_reguly = diff(z.subs(y, _y))
# dowodzimy reguły łańcuchowej, pokazując, że obie pochodne są równe
print(dz_dx_z_regula) # 6*x*(x**2 + 1)**2
print(dz_dx_bez_reguly) # 6*x*(x**2 + 1)**2
