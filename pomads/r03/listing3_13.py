import random
from scipy.stats import norm

for i in range(0,1000):
    losowe_p = random.uniform(0.0, 1.0)
    losowa_waga = norm.ppf(losowe_p, loc=29.23, scale=1.37)
    print(losowa_waga)
