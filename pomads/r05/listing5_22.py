import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score

df = pd.read_csv('https://bit.ly/3cIH97A', delimiter=",")

# Wyodrębniamy zmienne wejściowe (wszystkie wiersze, wszystkie kolumny oprócz ostatniej)
X = df.values[:, :-1]

# Wyodrębniamy kolumnę wyjściową (wszystkie wiersze, ostatnia kolumna)
Y = df.values[:, -1]

# Przeprowadzamy prostą regresję liniową
kfold = KFold(n_splits=3, random_state=7, shuffle=True)
model = LinearRegression()
wyniki = cross_val_score(model, X, Y, cv=kfold)
print(wyniki)
print("MSE: średnia=%.3f (odch. standardowe-%.3f)" % (wyniki.mean(), wyniki.std()))
