import pandas as pd
from sympy import *

# Importujemy punkty z pliku CSV
punkty = list(pd.read_csv("https://bit.ly/2KF29Bd").itertuples())

m, b, i, n = symbols('m b i n')
x, y = symbols('x y', cls=Function)

suma_kwadratow = Sum((m*x(i) + b - y(i)) ** 2, (i, 0, n))

d_m = diff(suma_kwadratow, m) \
    .subs(n, len(punkty) - 1).doit() \
    .replace(x, lambda i: punkty[i].x) \
    .replace(y, lambda i: punkty[i].y)

d_b = diff(suma_kwadratow, b) \
    .subs(n, len(punkty) - 1).doit() \
    .replace(x, lambda i: punkty[i].x) \
    .replace(y, lambda i: punkty[i].y)

# Kompilujemy za pomocą lambdify w celu przyspieszenia obliczeń
d_m = lambdify([m, b], d_m)
d_b = lambdify([m, b], d_b)

# Budujemy model
m = 0.0
b = 0.0

# Tempo nauki
L = .001

# Liczba iteracji
iteracje = 100_000

# Gradient prosty
for i in range(iteracje):

    # Aktualizujemy m i b
    m -= d_m(m,b) * L
    b -= d_b(m,b) * L

print("y = {0}x + {1}".format(m, b))
# y = 1.939393939393954x + 4.733333333333231
