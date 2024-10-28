from scipy.stats import norm

def krytyczna_wartosc_z(p):
    norm_dist = norm(loc=0.0, scale=1.0)
    lewy_ogon = (1.0 - p) / 2.0
    prawy_ogon = 1.0 - ((1.0 - p) / 2.0)
    return norm_dist.ppf(lewy_ogon), norm_dist.ppf(prawy_ogon)

print(krytyczna_wartosc_z(p=.95)) # (-1.959963984540054, 1.959963984540054)
