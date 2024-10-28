from numpy import array, diag
from numpy.linalg import eig, inv

A = array([
[1, 2],
[4, 5]
])

wart_wlasne, wekt_wlasne = eig(A)

print("WARTOŚCI WŁASNE")
print(wart_wlasne)
print("\nWEKTORY WŁASNE")
print(wekt_wlasne)
"""
WARTOŚCI WŁASNE
[-0.46410162  6.46410162]

WEKTORY WŁASNE
[[-0.80689822 -0.34372377]
[ 0.59069049 -0.9390708 ]]
"""
