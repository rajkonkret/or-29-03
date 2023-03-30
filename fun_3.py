a = 10
b = 10


def dodaj():
    a = 6
    b = 7
    print(a + b)  # działania wykonywałe na zmiennej ktora jest wyzej niz nasza funkcja


def dodaj_2():
    global a    # a przyjmuje zzmienna globalną
    a = 6   # nadpisanie zmiennej globalnej
    b = 7
    print(a + b)


print("Zmienna a z gory", a)
dodaj()
print("Zmienna a z gory", a)
dodaj_2()
print("Zmienna a z gory", a)
