from sympy import *
x = symbols('x')
f = 1 / x
wynik = limit(f, x, oo)
print(wynik) # 0
