from scipy.stats import norm

# Średni czas zdrowienia z przeziębienia to 18 dni, z odchyleniem standardowym 1,5
srednia = 18
odch_std = 1.5

# 95% prawdopodobieństwa, że zdrowienie potrwa 15 - 21 dni
x = norm.cdf(21, srednia, odch_std) - norm.cdf(15, srednia, odch_std)
print(x) # 0.9544997361036416
