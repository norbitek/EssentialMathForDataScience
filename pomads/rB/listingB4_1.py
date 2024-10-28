from numpy import array

v = array([1,2])

i_daszek = array([2, 0])
j_daszek = array([0, 1.5])

# Wektor bazowy
baza = array([i_daszek, j_daszek])

# przekształcamy wektor v w w
w = baza.dot(v)

print(w) # [2. 3.]
