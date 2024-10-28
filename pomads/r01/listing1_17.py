def pochodna_x(f, x, rozmiar_kroku):
    m = (f(x + rozmiar_kroku) - f(x)) / ((x + rozmiar_kroku) - x)
    return m

def moja_funkcja(x):
    return x**2

nachylenie_w_punkcie_2 = pochodna_x(moja_funkcja, 2, .00001)
print(nachylenie_w_punkcie_2) # wypisuje 4.000010000000827
