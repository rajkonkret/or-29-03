# while  - petla bez licznika
# działanie uzależnione od warunku

# petla nieskonczona
licznik = 0
while True:  # zawsze prawda
    licznik += 1  # licznik = licznik + 1
    print("Komunikat")
    if licznik > 10:
        break  # przerywa biezaca petle
# 11:20
print(licznik)
# tu licznik ma 11
licznik = 0
while licznik < 10:
    print("Komunikat")
    licznik += 1

# gdy podasz cos innego niz liczbe to wychodzimy z petli
lista = []
while True:
    wejscie = input("Podaj liczbe")
    if not wejscie.isnumeric():
        break
    lista.append(wejscie)

print(lista)
