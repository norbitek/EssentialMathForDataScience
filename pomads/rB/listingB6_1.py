import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import KFold, cross_val_score

# Wczytujemy dane
df = pd.read_csv("https://bit.ly/3imidqa", delimiter=",")

X = df.values[:, :-1]
Y = df.values[:, -1]

kfold = KFold(n_splits=3, shuffle=True)
model = LogisticRegression(penalty='none')
wyniki = cross_val_score(model, X, Y, cv=kfold)

print("Średnia dokładność: %.3f (odch. std=%.3f)" % (wyniki.mean(), wyniki.std()))
