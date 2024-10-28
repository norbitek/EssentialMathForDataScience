import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Wczytujemy dane
df = pd.read_csv('https://bit.ly/3cIH97A', delimiter=",")

# Wyodrębniamy zmienne wejściowe (wszystkie wiersze, wszystkie kolumny oprócz ostatniej)
X = df.values[:, :-1]

# Wyodrębniamy kolumnę wyjściową (wszystkie wiersze, ostatnia kolumna)
Y = df.values[:, -1]

# Oddzielamy dane treningowe i testowe
# W ten sposób jedna trzecia danych zostaje nam do testów
X_trening, X_test, Y_trening, Y_test = train_test_split(X, Y, test_size=1/3)

model = LinearRegression()
model.fit(X_trening, Y_trening)
wynik = model.score(X_test, Y_test)
print("r^2: %.3f" % wynik)
