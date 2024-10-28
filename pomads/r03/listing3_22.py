from scipy.stats import norm

# Średni czas zdrowienia z przeziębienia to 18 dni, z odchyleniem standardowym 1,5
srednia = 18
odch_std = 1.5

# Prawdopodobieństwo 16 lub mniejszej liczby dni
p1 = norm.cdf(16, srednia, odch_std)

# Prawdopodobieństwo 20 lub większej liczby dni
p2 = 1.0 - norm.cdf(20, srednia, odch_std)

# Wartość p obu „ogonów”
wartosc_p = p1 + p2

print(wartosc_p) # 0.18242243945173575
