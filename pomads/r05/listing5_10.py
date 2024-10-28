from sympy import *

m, b, i, n = symbols('m b i n')
x, y = symbols('x y', cls=Function)

suma_kwadratow = Sum((m*x(i) + b - y(i)) ** 2, (i, 0, n))

d_m = diff(suma_kwadratow, m)
d_b = diff(suma_kwadratow, b)

print(d_m)
print(d_b)

# WYNIKI
# Sum(2*(b + m*x(i) - y(i))*x(i), (i, 0, n))
# Sum(2*b + 2*m*x(i) - 2*y(i), (i, 0, n))
