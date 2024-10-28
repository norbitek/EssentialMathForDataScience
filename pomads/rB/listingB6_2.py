import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

# Wczytujemy dane
df = pd.read_csv("https://bit.ly/3imidqa", delimiter=",")

# Wyodrębniamy dane wejściowe (wszystkie wiersze, wszystkie kolumny oprócz ostatniej)
X = df.values[:, :-1]

# Wyodrębniamy kolumnę wyjściową (wszystkie wiersze, ostatnia kolumna)
Y = df.values[:, -1]

model = LogisticRegression(solver='liblinear')

X_trening, X_test, Y_trening, Y_test = train_test_split(X, Y, test_size=.33)
model.fit(X_trening, Y_trening)
prognoza = model.predict(X_test)

"""
Macierz błędów ocenia dokładność w każdej kategorii.
[[prawdziwie_pozytywne fałszywie_negatywne]
[fałszywie_pozytywne prawidziwie_negatywne]]

Przekątna reprezentuje poprawne przewidywania, więc chcemy, aby te wartości były wyższe
"""
macierz = confusion_matrix(y_true=Y_test, y_pred=prognoza)
print(macierz)
