def odejmij(a, b):
    return a - b


odejmij_2 = lambda a, b: a - b  # lmbda - odpowiednik funkcji w skroconym zapisie
print(odejmij_2(4, 5))
print(odejmij(4, 5))

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(5), wiek(15))
print(wiek(15))
print(wiek(25))

lista = [1, 2, 7, 8, 10, 55]

# map() - mapuje dane na inne
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")
# filter() - filtruje dane
print(f"Zastosowanie filter: {list(filter(lambda x: x < 3, lista))}")
# wyfiltrowac wieksze od 8
print(f"Zastosowanie filter: {list(filter(lambda x: x > 8, lista))}")
# wieksze od 3, mniejsze od 20
print(f"Zastosowanie filter: {list(filter(lambda x: 3 < x < 20, lista))}")
# | or & and
print(f"Zastosowanie filter: {list(filter(lambda x: x < 8 or x > 20 , lista))}")
