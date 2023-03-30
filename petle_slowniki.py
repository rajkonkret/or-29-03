dictionary = {'imie': 'Radek', 'nazwisko': 'Kowalski'}

print(dictionary)

# petla zwraca klucze
for k in dictionary:
    print(k)

# zwraca wartosci
for v in dictionary.values():
    print(v)

# zwraca klucze
for k in dictionary.keys():
    print(k)

for k, v in dictionary.items():
    print(k, "=>", v)

# utworzyc słownik i wypisac
dict = {'name': 'imie', 'company': 'Orange'}
for k, v in dict.items():
    print(k, "=>", v)

for i in range(1, 10, 2):  # start, koniec, krok
    print(i)

for i in range(10, 1, -1):
    print(i)

for i in range(-10, 1, 1):
    print(i)

slownik = {'pan': 'Tomek', 'pani': 'Ania'}
# zamiana klucza z wartoscia w słowniku
# wez wartosc ze słownika, wypisz jako piersze, dodaj :, wez klucz ze słownika i wypisz
print({value: key for key, value in slownik.items()})
# for key, value in slownik.items():
#     value, key = key, value
