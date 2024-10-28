import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np
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

# Testujemy prognozy
while True:
    n = input("Wprowadź kolor {czerwony},{zielony},{niebieski}: ")
    (r, g, b) = n.split(",")
    x = model.predict(np.array([[int(r), int(g), int(b)]]))
    if model.predict(np.array([[int(r), int(g), int(b)]]))[0] == 0.0:
        print("JASNA")
    else:
        print("CIEMNA")
