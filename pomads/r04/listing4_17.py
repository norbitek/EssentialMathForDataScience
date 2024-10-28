from sympy import *

# 4x + 2y + 4z = 44
# 5x + 3y + 7z = 56
# 9x + 3y + 6z = 72

A = Matrix([
[4, 2, 4],
[5, 3, 7],
[9, 3, 6]
])

# pomnożenie macierzy A przez jej odwrotność
# daje w wyniku macierz jednostkową
odwrotna = A.inv()
jednostkowa = inverse * A

# wypisuje Matrix([[-1/2, 0, 1/3], [11/2, -2, -4/3], [-2, 1, 1/3]])
print("MACIERZ ODWROTNA: {}".format(odwrotna))

# Wypisuje Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print("MACIERZ JEDNOSTKOWA: {}".format(jednostkowa))
