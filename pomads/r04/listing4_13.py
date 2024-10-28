from numpy.linalg import det
from numpy import array

i_daszek = array([3, 0])
j_daszek = array([0, 2])

baza = array([i_daszek, j_daszek]).transpose()

wyznacznik = det(baza)

print(wyznacznik) # wypisuje 6.0
