wiek = 47  # int
rok = 2023  # int
temp = 36.6  # float - zmiennoprzecinkowy
print(0.2 + 0.7)  # bład zaokrąglenia

# wypisac wartosci tych zmiennych
print(wiek)
print(rok)
print(temp)
print(type(wiek))
print(type(rok))
print(type(temp))
# ctrl d - powielenie lini
# 11:30

print(wiek * rok)
print(wiek - rok)
print(wiek + rok)
print(wiek / rok)  # wynik bedzie typu float
print(wiek // rok)  # czesc całkowita z dzielenia
print(wiek ** rok)  # potęgowanie
print(54 - (5 * 43) + (4 / 2 + 4) / 2)

print("Sprawdzam zmienna temp {} {}".format(wiek, temp))
print(f"\tSprawdzam zmienna temp {wiek} {temp}\n")

# tekst wielolinijkowy z formatowaniem (literka f na początku)
print(f"""
    {wiek}
    {temp}
""")

imie = "Radek Radek"
print(imie)
print(imie.upper())  # zwraca kopie, nie zmienia bazowej zmiennej(imie)
imie_2 = imie.capitalize()
print(imie)
print(imie_2)
print(imie.lower())
print(imie)
print(imie.count("a"))

# Fałsz / Prawda
# False / True
czy_znasz_pythona = True
print(czy_znasz_pythona)
print(type(czy_znasz_pythona))  # <class 'bool'>
print(int(czy_znasz_pythona))  # rzutownie bool na int 1 - True, 0 - False
print(bool(1))  # rzutowanie 1 na bool czyli dostajemy True
czy_znasz_pythona = False
print(czy_znasz_pythona)