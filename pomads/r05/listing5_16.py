from scipy.stats import t

n = 10
dolna_wk = t(n-1).ppf(.025)
gorna_wk = t(n-1).ppf(.975)

print(dolna_wk, gorna_wk)
# -2.262157162740992 2.2621571627409915
