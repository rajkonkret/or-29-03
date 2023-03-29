# słownik - klucz, wartosć - {"name":"radek"}
dict = {}  # pusty słownik
print(type(dict))

dict['imie'] = "Radek"  # dodawanie przez klucz => wartosc
print(dict['imie'])
print(dict)
dict['wiek'] = 39
print(dict)
print(dict.keys())  # wyswietlenie klucy ze słownika
print(dict.values())    # wyswietlenie wartosci
print(dict.items())
dict.update({"data": "12-12-2023"})
print(dict)
dictionary = {'x': 2}
print(dictionary)
# chcemy dodac dwie pary {'y':3, 'z':0}
dictionary.update([('y', 3), ('z', 0)])  # dodanie do słownika poprzez liste krotek
print(dictionary)

dict_2 = {'imie': 'name', 'kot': 'cat'}
print(dict_2['imie'])
print(dict_2['kot'])

print("Mamy w słowniku", dict_2.keys())
key = input("Podaj wyraz do przetłumaczenia")  # input zawsze zwraca str
print(dict_2[key.lower().replace(" ", "")].upper())

a = float(input("podaj liczbe a"))  # rzutowane na float
b = float(input("podaj liczbe b"))
print((a + b))
