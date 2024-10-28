from math import exp

# Prawdopodobieństwo wycieku w ciągu roku = 0,05
p_wycieku = .05
# Liczba lat
t = 5

# Prawdopodobieństwo wycieku w ciagu 5 lat
# 0.22119921692859512
p_wycieku_5_lat = 1.0 - exp(-p_wycieku * t)
print("PRAWDOPODOBIEŃSTWO WYCIEKU W CIĄGU 5 LAT: {}".format(p_wycieku_5_lat))
