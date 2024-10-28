from math import sqrt
from scipy.stats import norm

def krytyczna_wartosc_z (p, srednia=0.0, std=1.0):
    rozkl_norm = norm(loc=srednia, scale=std)
    lewy_obszar = (1.0 - p) / 2.0
    prawy_obszar = 1.0 - ((1.0 - p) / 2.0)
    return rozkl_norm.ppf(lewy_obszar), rozkl_norm.ppf(prawy_obszar)

def ci_duza_proba(p, srednia_proby, odch_std_proby, n):
    # Rozmiar próby musi być większy niż 30
    dolna, gorna = krytyczna_wartosc_z (p)
    dolna_ci = dolna * (odch_std_proby / sqrt(n))
    gorna_ci = gorna * (odch_std_proby / sqrt(n))

    return srednia_proby + dolna_ci, srednia_proby + gorna_ci

print(ci_duza_proba(p=.99, srednia_proby=1.715588, odch_std_proby=0.029252, n=34))
# (1.7026658973748656, 1.7285101026251342)
