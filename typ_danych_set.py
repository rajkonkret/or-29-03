# set - nie przechowuje zdublowanych elementow
lista = [44, 55, 666, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # rzutowanie na set
print(zbior)
zbior.add(33)
print(zbior)
zbior.add(18)
print(zbior)
print(zbior.pop())  # usuniecie i pobranie
print(zbior)
print(zbior.pop())
print(zbior)

zbior_2 = {66, 66, 11, 44, 18, 55, 62, 999}
print(zbior_2)
print(zbior | zbior_2)  # suma zbiorów (or)
print(zbior & zbior_2)  # czesc wspolna (and)
print(zbior - zbior_2)
print(zbior.difference(zbior_2))
empty = set()  # pusty set
