import numpy as np
from numpy.linalg import det

i_daszek = np.array([1, 0])
j_daszek = np.array([2, 2])

baza = np.array([i_daszek,j_daszek]).transpose()

wyznacznik = det(baza)

print(wyznacznik) # 2.0
