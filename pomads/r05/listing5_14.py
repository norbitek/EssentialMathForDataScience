import pandas as pd

# Wczytujemy dane do ramki danych Pandas
df = pd.read_csv('https://bit.ly/2KF29Bd', delimiter=",")

# Wypisujemy korelacje między zmiennymi
korelacje = df.corr(method='pearson')
print(korelacje)

# WYNIKI:
#                   x              y
# x  1.000000 0.957586
# y  0.957586 1.000000
