tuple_1 = ("Tomek", "Asia", "Marek", "Paulina")
print(tuple_1)
tuple_2 = ("radek",)  # tupla jednoelementowa, zmienna, niezmienna (stała)
print(type(tuple_2))
tuple_3 = (43, 55, 22.42, 11, 200)
print(tuple_3)
print(tuple_1.count("Tomek"))
print(tuple_1.index("Tomek"))
a, b, c = 1, 2, 3
print(a)
a, *b, c = 1, 2, 3, 4
print(b)  # z b zrobił liste [2, 3]
a, b, *c = 1, 2, 3, 4
print(c)
imie_1, imie_2, *imie_3 = tuple_1  # rozpakowanie tupli
print(imie_3)

lista = list(tuple_1)  # zamiana tupli na liste
print(lista)