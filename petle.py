# petla for
import random

lista_parzyste = []
for i in range(10):  # 0..9
    # pass      # nie rob nic
    if i % 2 == 0:  # reszta z dzielenia
        print("Jest parzysta")
        lista_parzyste.append(i)
    print(i)

print("Wyszedłem z pętli")
print(lista_parzyste)

lista_2 = list(range(1, 50))  # list - rzutowanie na liste, range - zwraca nam lkolekcje z podanego zakresu 1..49
lista_3 = []

for i in range(6):  # 0..5
    wyn = random.choice(lista_2)
    lista_2.remove(wyn)
    lista_3.append(wyn)

print(lista_3)

lista = [2, 7, 9, 10, 23, 45]

for cyfra in lista:  # cyfra przyjmuje kolejne wartosci z listy
    if cyfra == 2:
        cyfra += 1  # cyfra = cyfra + 1
    print(cyfra)

lista_4 = [j for j in range(10) if j % 2 == 0]
# for j in range(10):
#     if j % 2 == 0:
#         lista_4.append(j)
print(lista_4)

imiona = ["Radek", "Zenek", "Marta"]

for p in imiona:
    print(p, end=", ")  # end="" zmiana znaku konca wiersza na pusty, nie zmienia lini

# 0 Radek, 1 Zenek..
# len(imiona) - długosc listy
for p in range(len(imiona)):  # range(3) 0..2
    print(p, imiona[p], end=", ")  # p - index, w - imiona[p] - pobieranie z listy po indeksie

# enumerate - ponumerowanie kolekcji
for p, w in enumerate(imiona):
    print(p, w, end=", ")

ludzie = ["Radek", "Zenek", "Asia", "Michał"]
wiek = [47, 67, 32, 34]
jezyk = ['java', 'pythton', 'c++']
for p, o in enumerate(ludzie):
    print(p, o)

for p, o in enumerate(ludzie):
    print(p, o, wiek[p])

ind = list(range(len(ludzie)))
# zip - łaczenie list
for o, w, j in zip(ludzie, wiek, jezyk):
    print(o, w, j)

for i, o, w, j in zip(ind, ludzie, wiek, jezyk):
    print(i, o, w, j)
