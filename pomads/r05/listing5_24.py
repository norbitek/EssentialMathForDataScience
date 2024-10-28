import pandas as pd
from sklearn.linear_model import LinearRegression

#	Wczytujemy dane
df = pd.read_csv('https://bit.ly/2X1HWH7', delimiter=",")

# Wyodrębniamy zmienne wejściowe (wszystkie wiersze, wszystkie kolumny oprócz ostatniej)
X = df.values[:, :-1]

# Wyodrębniamy kolumnę wyjściową (wszystkie wiersze, ostatnia kolumna)
Y = df.values[:, -1]

#	Trening
dop = LinearRegression().fit(X, Y)

#	Wypisujemy współczynniki
print("Współczynniki = {0}".format(dop.coef_))
print("Wyraz wolny = {0}".format(dop.intercept_))
print("z = {0} + {1}x + {2}y".format(dop.intercept_, dop.coef_[0], dop.coef_[1]))
