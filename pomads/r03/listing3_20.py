from scipy.stats import norm

# Średni czas zdrowienia z przeziębienia to 18 dni, z odchyleniem standardowym 1,5
srednia = 18
odch_std = 1.5

# Prawdopodobieństwo wyzdrowienia w 16 lub mniej dni
wartosc_p = norm.cdf(16, srednia, odch_std)

print(wartosc_p) # 0.09121121972586788
