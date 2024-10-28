from sympy import *
from sympy.plotting import plot3d
import pandas as pd

punkty = list(pd.read_csv("https://bit.ly/2KF29Bd").itertuples())
m, b, i, n = symbols('m b i n')
x, y = symbols('x y', cls=Function)

suma_kwadratow = Sum((m*x(i) + b - y(i)) ** 2, (i, 0, n)) \
    .subs(n, len(punkty) - 1).doit() \
    .replace(x, lambda i: punkty[i].x) \
    .replace(y, lambda i: punkty[i].y)

plot3d(suma_kwadratow)
