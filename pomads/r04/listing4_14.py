from numpy.linalg import det
from numpy import array

i_daszek = array([1, 0])
j_daszek = array([1, 1])

baza = array([i_daszek, j_daszek]).transpose()

wyznacznik = det(baza)

print(wyznacznik) # wypisuje 1.0
