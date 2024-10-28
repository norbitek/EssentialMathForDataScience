p_picie_kawy = .65
p_rak = .005
p_picie_kawy_jesli_rak = .85
p_rak_jesli_picie_kawy = p_picie_kawy_jesli_rak * p_rak / p_picie_kawy
# wypisuje 0.006538461538461539
print(p_rak_jesli_picie_kawy)
