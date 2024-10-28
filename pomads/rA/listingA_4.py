# Silnia to iloczyn kolejnych malejących liczb całkowitych aż do 1
# Przykład: 5! = 5 * 4 * 3 * 2 * 1
def silnia(n: int):
    f = 1
    for i in range(n):
        f *= (i + 1)
    return f

def przybliz_calke(a, b, n, f):
    delta_x = (b - a) / n
    suma = 0

    for i in range(1, n + 1):
        pkt_srodkowy = 0.5 * (2 * a + delta_x * (2 * i - 1))
        suma += f(pkt_srodkowy)

    return suma * delta_x

def rozklad_beta(x: float, alfa: float, beta: float) -> float:
    if x < 0.0 or x > 1.0:
        raise ValueError("x musi należeć do zakresu 0.0 - 1.0")
    licznik = x ** (alfa - 1.0) * (1.0 - x) ** (beta - 1.0)
    mianownik = (1.0 * silnia(alfa - 1) * silnia(beta - 1)) / \
        (1.0 * silnia(alfa + beta - 1))
    return licznik / mianownik

wiekszy_niz_90 = przybliz_calke(a=.90, b=1.0, n=1000, \
    f=lambda x: rozklad_beta(x, 8, 2))
mniejszy_niz_90 = 1.0 - wiekszy_niz_90

print("WIĘKSZY NIŻ 90%: {}, MNIEJSZY NIŻ 90%: {}".format(wiekszy_niz_90, \
    mniejszy_niz_90))
