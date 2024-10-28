from scipy.stats import t

# Zakres wartości krytycznych dla 95-procentowej ufności
# przy rozmiarze próby równym 25

n = 25
dolna = t.ppf(.025, df=n-1)
gorna = t.ppf(.975, df=n-1)

print(dolna, gorna)
# -2.063898561628021 2.0638985616280205
