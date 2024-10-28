def przybliz_calke(a, b, n, f):
    delta_x = (b - a) / n
    suma = 0

    for i in range(1, n + 1):
        pkt_srodkowy = 0.5 * (2 * a + delta_x * (2 * i - 1))
        suma += f(pkt_srodkowy)

    return suma * delta_x

def moja_funkcja(x):
    return x**2 + 1

pole = przybliz_calke(a=0, b=1, n=5, f=moja_funkcja)
print(pole) # wypisuje 1.33
