from numpy.linalg import det
from numpy import array

i_daszek = array([-2, 1])
j_daszek = array([3, -1.5])

baza = array([i_daszek, j_daszek]).transpose()

wyznacznik = det(baza)

print(wyznacznik) # wypisuje 0.0
