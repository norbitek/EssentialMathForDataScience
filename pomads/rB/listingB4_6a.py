from numpy.linalg import det
from numpy import array

i_daszek = array([2, 6])
j_daszek = array([1, 3])

baza = array([i_daszek, j_daszek]).transpose()
print(baza)

wyznacznik = det(baza)

print(wyznacznik) # -3.330669073875464e-16
