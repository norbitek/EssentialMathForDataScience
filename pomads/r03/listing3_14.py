def wynik_z (x, srednia, std):
    return (x - srednia) / std

def z_na_x(z, srednia, std):
    return (z * std) + srednia

srednia = 140000
odch_std = 3000
x = 150000

# Przekształcamy na wynik Z, a następnie z powrotem na X
z = wynik_z (x, srednia, odch_std)
z_powrotem_na_x = z_na_x(z, srednia, odch_std)

print("Wynik Z: {}".format(z)) # Wynik Z: 3.333
print("Z powrotem na X: {}".format(z_powrotem_na_x)) # Z powrotem na X: 150000.0
