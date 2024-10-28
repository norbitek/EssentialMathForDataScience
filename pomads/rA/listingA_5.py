import math

def normalny_pdf(x: float, srednia: float, odch_std: float) -> float:
    return (1.0 / (2.0 * math.pi * odch_std ** 2) ** 0.5) * \
        math.exp(-1.0 * ((x - srednia) ** 2 / (2.0 * odch_std ** 2)))

def przybliz_calke(a, b, n, f):
    delta_x = (b - a) / n
    suma = 0

    for i in range(1, n + 1):
        pkt_srodkowy = 0.5 * (2 * a + delta_x * (2 * i - 1))
        suma += f(pkt_srodkowy)

    return suma * delta_x

p_miedzy_27_5_a_28 = przybliz_calke(a=27.5, b=28, n=1000, \
    f= lambda x: normalny_pdf(x,29.23,1.37))

print(p_miedzy_27_5_a_28) # 0.08130811236891686
