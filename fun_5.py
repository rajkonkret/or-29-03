# funkcja, ktora oblicz srednia ale z dowolnej ilosci danych

def liczby(c, *cyfry):
    print(c)
    print(cyfry)
    print(type(cyfry))
    suma = 0
    for i in cyfry:
        suma += i
    print(f"Suma {suma}")
    count = len(cyfry)
    try:
        print(f"Średnia {suma / count}")
    except ZeroDivisionError:
        print("Dzielenie przez zero")


liczby(c="Radek")
liczby("Radek", 2)
liczby("Radek", 2, 3, 4, 5, 6, 7, 89, 10, 100)
# 1
# ()
# 1
# (2,)
# 1
# (2, 3, 4, 5, 6, 7, 89, 10, 100)
