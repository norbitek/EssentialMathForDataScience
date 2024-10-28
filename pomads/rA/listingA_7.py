import random
from scipy.special import erfinv

def normalny_odwrotna_cdf(p: float, srednia: float, odch_std: float):
    return srednia + (odch_std * (2.0 ** 0.5) * erfinv((2.0 * p) - 1.0))

srednia = 29.23
odch_std = 1.37

for i in range(0,1000):
    losowe_p = random.uniform(0.0, 1.0)
    print(normalny_odwrotna_cdf(losowe_p, srednia, odch_std))
