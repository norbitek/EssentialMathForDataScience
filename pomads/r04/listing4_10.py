from numpy import array

# Deklarujemy wektory i-daszek i j-daszek
i_daszek = array([2, 3])
j_daszek = array([2, -1])

# Tworzymy macierz bazową z wektorów i-daszek i j-daszek,
# musimy też transponować wiersze i kolumny
baza = array([i_daszek, j_daszek]).transpose()

# Deklarujemy wektor v
v = array([2,1])

#	Tworzymy nowy wektor poprzez
# przekształcenie v za pomocą iloczynu skalarnego
nowy_v = baza.dot(v)

print(nowy_v) # [6 5]
