# deklaracja pustej listy
lista = []

print(lista)
print(type(lista))
lista.append("Radek")  # dodawanie elementu na końcu listy
lista.append("Maciek")
lista.append("Zenek")
lista.append("Paweł")
print(lista)
# indeksy w liscie są numerowane do 0
print(lista[0])  # Radek
print(lista[3])
print(lista[-2])

# wstawienie elementu do listy pomiedzy indeks 0 i 1
lista.insert(1, "Piotr")
print(lista)

# nadpisanie elementu w liscie
lista[2] = "Agnieszka"
print(lista)

# usuniecie obiektu z listy ( po wartosci)
lista.remove("Piotr")
print(lista)

# usuniecie po indeksie i zwrócenie tego elementu do nas
element = lista.pop(2)
print(element)
print(lista)
lista_copy = lista.copy()
lista.clear()  # kasowanie wszystkich elementów w liscie
print(lista_copy)
print(lista)
print("Radek" in lista_copy)
print("Zenek" in lista_copy)

liczby = [54, 999, 34, 22, 12.54, 687]
print(liczby)
liczby.sort()
print(liczby)
liczby.reverse()
print(liczby)
liczby[2] = 6666
print(liczby)
print(liczby[0:3])  # od indeksu 0 do indeksu 2 (3 nie jest brana juz pod uwage)
print(liczby[:3])
print(liczby[:-2])
print(liczby[2:])  # od 2 włacznie do końca włącznie
liczby.remove(34)
print(liczby)
print(len(liczby))  # ilosc elementow w kolekcji

krotka = tuple(liczby)  # zamiana listy na tuple
print(krotka)
print(type(krotka))
