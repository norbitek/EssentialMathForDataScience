from numpy import array

# Tworzymy macierz bazową z wektorów i-daszek i j-daszek
baza = array(
    [[3, 0],
    [0, 2]]
)

#	deklarujemy wektor v
v = array([1,1])

#	Tworzymy nowy wektor poprzez
# przekształcenie v za pomocą iloczynu skalarnego
nowy_v = baza.dot(v)

print(nowy_v) # [3 2]
