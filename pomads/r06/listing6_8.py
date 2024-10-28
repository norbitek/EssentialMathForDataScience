from sympy import *
import pandas as pd

punkty = list(pd.read_csv("https://tinyurl.com/y2cocoo7").itertuples())

b1, b0, i, n = symbols('b1 b0 i n')
x, y = symbols('x y', cls=Function)
pp_laczne = Sum(log((1.0 / (1.0 + exp(-(b0 + b1 * x(i))))) ** y(i) \
    * (1.0 - (1.0 / (1.0 + exp(-(b0 + b1 * x(i)))))) ** (1 - y(i))), (i, 0, n))

# Pochodna cząstkową względem b1, z podstawionymi punktami
d_b1 = diff(pp_laczne, b1) \
    .subs(n, len(punkty) - 1).doit() \
    .replace(x, lambda i: punkty[i].x) \
    .replace(y, lambda i: punkty[i].y)

# Pochodna cząstkowa względem b0, z podstawionymi punktami
d_b0 = diff(pp_laczne, b0) \
    .subs(n, len(punkty) - 1).doit() \
    .replace(x, lambda i: punkty[i].x) \
    .replace(y, lambda i: punkty[i].y)

# Kompilujemy za pomocą lambdify, aby przyspieszyć obliczenia
d_b1 = lambdify([b1, b0], d_b1)
d_b0 = lambdify([b1, b0], d_b0)

# Metoda gradientu prostego
b1 = 0.01
b0 = 0.01
L = .01

for j in range(10_000):
    b1 += d_b1(b1, b0) * L
    b0 += d_b0(b1, b0) * L

print(b1, b0)
# 0.6926693075370812 -3.175751550409821
