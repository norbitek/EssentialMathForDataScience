import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score

# Wczytujemy dane
df = pd.read_csv("https://tinyurl.com/y6r7qjrp", delimiter=",")

X = df.values[:, :-1]
Y = df.values[:, -1]

# "random_state" to losowe ziarno, które ustawiamy na 7
kfold = KFold(n_splits=3, random_state=7, shuffle=True)
model = LogisticRegression(penalty='none')
wyniki = cross_val_score(model, X, Y, cv=kfold)

print("Średnia dokładności: %.3f (odch. std=%.3f)" % (wyniki.mean(), wyniki.std()))
