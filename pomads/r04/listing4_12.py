from numpy import array

# Przekształcenie 1
i_daszek1 = array([0, 1])
j_daszek1 = array([-1, 0])
przeksztalcenie1 = array([i_daszek1, j_daszek1]).transpose()

# Przekształcenie 2
i_daszek2 = array([1, 0])
j_daszek2 = array([1, 1])
przeksztalcenie2 = array([i_daszek2, j_daszek2]).transpose()

# Łączymy przekształcenia, stosując najpierw ścięcie, a potem obrót
polaczone = przeksztalcenie1 @ przeksztalcenie2

# Testujemy
print("POŁĄCZONA MACIERZ:\n {}".format(polaczone))

v = array([1, 2])
print(polaczone.dot(v)) # [-2 3]
