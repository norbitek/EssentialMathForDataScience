import pandas as pd
from sklearn.linear_model import LogisticRegression

# Wczytujemy dane
df = pd.read_csv('https://bit.ly/33ebs2R', delimiter=",")

# Wyodrębniamy dane wejściowe (wszystkie wiersze, wszystkie kolumny oprócz ostatniej)
X = df.values[:, :-1]

# Wyodrębniamy kolumnę wyjściową (wszystkie wiersze, ostatnia kolumna)
Y = df.values[:, -1]

# Przeprowadzamy regresję logistyczną
# Wyłączamy karę
model = LogisticRegression(penalty='none')
model.fit(X, Y)

# Wypisujemy beta1
print(model.coef_.flatten()) # 0.69267212

# Wypisujemy beta0
print(model.intercept_.flatten()) # -3.17576395
