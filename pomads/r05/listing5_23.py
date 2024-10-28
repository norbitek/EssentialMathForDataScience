import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, ShuffleSplit

df = pd.read_csv('https://bit.ly/38XwbeB', delimiter=",")

# Wyodrębniamy zmienne wejściowe (wszystkie wiersze, wszystkie kolumny oprócz ostatniej)
X = df.values[:, :-1]

# Wyodrębniamy kolumnę wyjściową (wszystkie wiersze, ostatnia kolumna)
Y = df.values[:, -1]

# Przeprowadzamy prostą regresję liniową
kfold = ShuffleSplit(n_splits=10, test_size=.33, random_state=7)
model = LinearRegression()
wyniki = cross_val_score(model, X, Y, cv=kfold)

print(wyniki)
print("średnia=%.3f (odch. standardowe-%.3f)" % (wyniki.mean(), wyniki.std()))
