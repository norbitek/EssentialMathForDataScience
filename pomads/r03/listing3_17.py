from math import sqrt
from scipy.stats import norm

def krytyczna_wartosc_z(p):
    norm_dist = norm(loc=0.0, scale=1.0)
    lewy_ogon = (1.0 - p) / 2.0
    prawy_ogon = 1.0 - ((1.0 - p) / 2.0)
    return norm_dist.ppf(lewy_ogon), norm_dist.ppf(prawy_ogon)

def przedzial_ufnosci(p, srednia_proby, odch_proby, n):
    # Rozmiar próby musi być większy niż 30

    dolna, gorna = krytyczna_wartosc_z(p)
    dolna_ci = dolna * (odch_proby / sqrt(n))
    gorna_ci = gorna * (odch_proby / sqrt(n))

    return srednia_proby + dolna_ci, srednia_proby + gorna_ci

print(przedzial_ufnosci(p=.95, srednia_proby=29.214, odch_proby=1.37, n=31))
# (28.73173270493526, 29.696267295064736)
