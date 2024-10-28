import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Importujemy punkty
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

# Wyodrębniamy dane wejściowe (wszystkie wiersze, wszystkie kolumny oprócz ostatniej)
X = df.values[:, :-1]

# Wyodrębniamy kolumnę wyjściową (wszystkie wiersze, ostatnia kolumna)
Y = df.values[:, -1]

# Dopasowujemy linię do punktów
dopasowanie = LinearRegression().fit(X, Y)

# m = 1,7867224, b = -16,51923513
m = dopasowanie.coef_.flatten()
b = dopasowanie.intercept_.flatten()
print("m = {0}".format(m))
print("b = {0}".format(b))

# Pokazujemy na wykresie
plt.plot(X, Y, 'o') # wykres punktowy
plt.plot(X, m*X+b) # linia
plt.show()
