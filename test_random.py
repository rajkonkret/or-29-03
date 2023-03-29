import random

# random - generator liczb pseudolosowych
print(random.randint(1, 6))  # losuje od 1..6
print(random.random() * 10)  # 0..1 * 10 0..9.9999
print(random.randrange(6))  # 0..5 całkowite
print(random.randrange(1, 6))  # 1..5 całkowite

lista = [5, 7, 6, 45, 34, 56]
print(random.choice(lista))  # wylosowanie elementu z listy
lista_2 = list(range(1, 50))  # list - rzzutowanie na liste, range - zwraca nam lkolekcje z podanego zakresu 1..49
lista_3 = []
print(lista_2)
wyn = random.choice(lista_2)  # losowanie z lista_2 i zapisanie w zmiennej wyn
lista_2.remove(wyn)  # usuniecie z lista_2 (z bębna)
lista_3.append(wyn)  # dodanie do lista_3
wyn = random.choice(lista_2)
lista_2.remove(wyn)
lista_3.append(wyn)
wyn = random.choice(lista_2)
lista_2.remove(wyn)
lista_3.append(wyn)
wyn = random.choice(lista_2)
lista_2.remove(wyn)
lista_3.append(wyn)
wyn = random.choice(lista_2)
lista_2.remove(wyn)
lista_3.append(wyn)
wyn = random.choice(lista_2)
lista_2.remove(wyn)
lista_3.append(wyn)
lista_3.sort()
print(lista_3)
