# Silnia to iloczyn kolejnych malejących liczb całkowitych aż do 1
# Przykład: 5! = 5 * 4 * 3 * 2 * 1
def silnia(n: int):
    f = 1
    for i in range(n):
        f *= (i + 1)
    return f

# Generuje współczynnik potrzebny do rozkładu dwumianowego
def wspolczynnik_dwumianowy(n: int, k: int):
    return silnia(n) / (silnia(k) * silnia(n - k))

# Rozkład dwumianowy oblicza prawdopodobieństwo k zdarzeń w n próbach
# przy prawdopodobieństwie p zajścia zdarzenia k
def rozklad_dwumianowy(k: int, n: int, p: float):
    return wspolczynnik_dwumianowy(n, k) * (p ** k) * (1.0 - p) ** (n - k)

# 10 prób, w których każda ma 90-procentowe prawdopodobieństwo sukcesu
n = 10
p = 0.9

for k in range(n + 1):
    prawdopodobienstwo = rozklad_dwumianowy(k, n, p)
    print("{0} - {1}".format(k, prawdopodobienstwo))
