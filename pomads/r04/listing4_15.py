from numpy.linalg import det
from numpy import array

i_daszek = array([-2, 1])
j_daszek = array([1, 2])

baza = array([i_daszek, j_daszek]).transpose()

wyznacznik = det(baza)

print(wyznacznik) # wypisuje -5.0
