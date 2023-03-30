# funkcja zwracajaca wynik

def dodaj(a, b):
    return a + b


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


wyn = dodaj(5, 6)
print(wyn)
print(dodaj(3, 4))
print(dodaj(5, 6) * dodaj(7, 8))
print(oblicz_vat(1000))
o = 9
j = 19
print(dodaj(o, j))